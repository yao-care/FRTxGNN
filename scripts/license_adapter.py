"""FR（ANSM／BDPM）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：BDPM 公開檔 CIS_bdpm.txt（tab 分隔，免金鑰）。欄位：0 CIS、4 Statut administratif de l'AMM。
證據包紀錄的 license_id＝CIS、status＝Statut administratif（例：Autorisation active／Autorisation archivée），
reviewer 依 status 文字判定（archiv、abrog… 算註銷）。

2026-11-17（用戶要求確認「新資料查不到」的許可證）：
- 下載網址改成 https 的 /download/file/<檔名>（舊的 index.php/download/file 會 301 到 http，雲端環境走不通）。
- CIS_bdpm.txt 不是完整的 CIS 清單：同一天的 CIS_CIP_bdpm.txt（包裝層級）另有 478 個 CIS 不在 CIS_bdpm.txt
  （2026-11-17 實測；全是「Présentation active」、有 Déclaration de commercialisation）。2026-11-16 排程列的 40 張
  「查不到」全在這批，BDPM 產品頁（/medicament/<CIS>/extrait）都寫「Statut de l'autorisation : Valide」。
  包裝狀態不等於 AMM 狀態（兩份都有的 CIS 裡，593 個 Autorisation abrogée 仍有 Présentation active），
  所以只在 CIS_CIP、不在 CIS_bdpm 的本站許可證號逐張讀產品頁：寫 Valide 的收成「Autorisation active」；
  其他寫法不收（仍列「查不到」，不推定）。
- 兩份檔都沒有、產品頁也回 404 的本站許可證號＝BDPM 已不收（BDPM 連 Autorisation abrogée／archivée 也收），
  preprocess 標 license_status＝cancelled 與 bdpm_not_listed（第一次發現日）；之後又出現就取消標記。
  任一份檔下載失敗、筆數過少，或產品頁讀不到（非 404 的錯誤）時不判定。2026-11-17 這類 0 張。
"""
import json
import re
import time
from pathlib import Path

import requests

RAW_FILE = "raw/CIS_bdpm.json"
HOST = "https://base-donnees-publique.medicaments.gouv.fr"
URLS = [HOST + "/download/file/CIS_bdpm.txt", HOST + "/index.php/download/file/CIS_bdpm.txt"]
CIP_URLS = [HOST + "/download/file/CIS_CIP_bdpm.txt", HOST + "/index.php/download/file/CIS_CIP_bdpm.txt"]
PAGE_URL = HOST + "/medicament/{}/extrait"
BUNDLES = Path(__file__).resolve().parents[1] / "data/bundles"
UA = {"User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)"}

CURRENT: set = set()   # fetch() 填：CIS_bdpm＋CIS_CIP 的 CIS；空的就不做「不在清單」判定
PAGE_VALID: set = set()  # fetch() 填：產品頁寫 Valide 的本站許可證號
ABSENT: set = set()    # fetch() 填：本站許可證號裡兩份檔都沒有、產品頁 404 的
MIN_CURRENT = 15000    # 兩份合計少於這個數＝下載或格式有問題，不判定（2026-11-17：16,277）


def _get(urls, tries=4):
    last = None
    for url in urls:
        for attempt in range(tries):
            try:
                r = requests.get(url, timeout=180, headers=UA)
                r.raise_for_status()
                return r.content
            except Exception as e:
                last = e
                time.sleep(10 * (attempt + 1))
    raise last


def _text(raw):
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("latin-1")


def _page_status(cis):
    """BDPM 產品頁的 AMM 狀態：'Valide'／其他原文／'404'（BDPM 沒有這個 CIS）；讀不到回 None"""
    for attempt in range(3):
        try:
            r = requests.get(PAGE_URL.format(cis), timeout=60, headers=UA)
            if r.status_code == 404:
                return "404"
            r.raise_for_status()
            t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", r.text)).replace("&#039;", "'").replace("&apos;", "'")
            m = re.search(r"Statut de l'autorisation : (\S+)", t)
            return m.group(1) if m else ""
        except Exception:
            time.sleep(5 * (attempt + 1))
    return None


def _site_ids():
    ids = set()
    for f in BUNDLES.glob("*/drug_bundle.json"):
        try:
            b = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        for r in (b.get("tfda") or {}).get("records") or []:
            lid = str(r.get("license_id") or "").strip()
            if lid.isdigit():
                ids.add(lid)
    return ids


def fetch():
    out = []
    for line in _text(_get(URLS)).splitlines():
        c = line.split("\t")
        if len(c) >= 7 and c[0].strip().isdigit():
            out.append({"cis": c[0].strip(), "name": c[1].strip(), "statut_amm": c[4].strip(), "commercialisation": c[6].strip()})
    CURRENT.clear()
    ABSENT.clear()
    PAGE_VALID.clear()
    try:
        cip = {line.split("\t")[0].strip() for line in _text(_get(CIP_URLS)).splitlines() if line.split("\t")[0].strip().isdigit()}
    except Exception as e:
        print(f"CIS_CIP_bdpm 下載失敗，不補產品頁、不判定不在清單的許可證號：{e}")
        return out
    in_cis = {r["cis"] for r in out}
    mine = _site_ids()
    for cis in sorted(mine - in_cis):
        st = _page_status(cis)
        if st == "Valide":   # 產品頁寫 Valide＝AMM 有效（只在 CIS_CIP 的 CIS 都是這種）
            PAGE_VALID.add(cis)
            out.append({"cis": cis, "name": "", "statut_amm": "Autorisation active", "commercialisation": "",
                        "source": "fiche BDPM (Statut de l'autorisation : Valide)"})
        elif st == "404" and cis not in cip:
            ABSENT.add(cis)
    if len(in_cis | cip) >= MIN_CURRENT:
        CURRENT.update(in_cis | cip)
    else:
        ABSENT.clear()
    return out


def confirmed_absent(lid):
    """給 license_refresh：兩份 BDPM 檔都沒有、產品頁 404（而且兩份檔都有成功下載）＝BDPM 已不收這個 CIS"""
    return bool(CURRENT) and str(lid).strip() in ABSENT


def preprocess(bundle):
    """BDPM 已不收的 CIS 標 cancelled（bdpm_not_listed＝第一次發現日）；又出現的取消標記。有改回 True"""
    if not CURRENT:
        return False
    today = time.strftime("%Y-%m-%d")
    ch = False
    for r in (bundle.get("tfda") or {}).get("records") or []:
        lid = str(r.get("license_id") or "").strip()
        if not lid.isdigit():
            continue
        if lid in ABSENT:
            if not r.get("bdpm_not_listed"):
                r["bdpm_not_listed"] = today
                r["license_status"] = "cancelled"
                ch = True
        elif r.get("bdpm_not_listed") and (lid in CURRENT or lid in PAGE_VALID):
            r.pop("bdpm_not_listed", None)
            r.pop("license_status", None)
            ch = True
    return ch


def validate(new, old):
    p = []
    if len(new) < 10000:
        p.append(f"只解析出 {len(new)} 筆（BDPM 通常 >15,000 筆），疑似格式改變")
    if sum(1 for r in new if not r["statut_amm"]) > 0.01 * max(1, len(new)):
        p.append("超過 1% 缺 Statut administratif 欄")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


_VERIFY_MAP = {"valide": "Autorisation active", "archivée": "Autorisation archivée", "abrogée": "Autorisation abrogée",
               "suspendue": "Autorisation suspendue", "retirée": "Autorisation retirée"}


def verify(lid):
    """反覆跳動防呆的線上查核（2026-11-24）：讀 BDPM 產品頁的「Statut de l'autorisation」，換成 CIS_bdpm 的寫法回傳；
    讀不到、404 或不認得的寫法回 None（排程就保留現狀、列進 issue）"""
    st = _page_status(lid)
    if not st or st == "404":
        return None
    return _VERIFY_MAP.get(st.strip().lower())


def status_index(new):
    return {r["cis"]: r["statut_amm"] for r in new}


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    if rec.get("status") == new:
        return False
    rec["status"] = new
    return True


# 程式產生的許可證表（2026-11-24，用戶決定；scripts/sync_license_tables.py）：狀態有變或證據包有改的藥，表依新證據包重排。
# 排程 3b 自我檢查只放行表格列；程式區塊裡會跟著變的非表格行（來源句、部分收錄句、沒有紀錄句、區塊標記）列在 PAGE_NOTE。
PAGE_NOTE = (r"^(Source : Base de données publique des médicaments \(BDPM\), statut administratif de l'AMM ; AMM actives en premier\."
             r"|Les données ne contiennent qu'une partie des autorisations ; la liste peut être incomplète\."
             r"|Aucune AMM de ce médicament ne figure dans les données BDPM utilisées pour ce rapport\."
             r"|<!-- licenses:(begin|end) -->)$")


def sync_tables(site_root, bundles):
    """證據包有改的藥：程式許可證表依新證據包重排（回傳 [(頁, 欄位, 前值, 後值)]）"""
    import importlib.util
    p = Path(site_root) / "scripts" / "sync_license_tables.py"
    s = importlib.util.spec_from_file_location("fr_sync_license_tables", p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    stems = set(bundles) | {b.replace("_", "-") for b in bundles} | {b.replace("-", "_") for b in bundles}
    return m.resync(stems)[0]
