"""FR（ANSM／BDPM）許可證下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：BDPM 公開檔 CIS_bdpm.txt（tab 分隔，免金鑰）。欄位：0 CIS、4 Statut administratif de l'AMM。
證據包紀錄的 license_id＝CIS、status＝Statut administratif（例：Autorisation active／Autorisation archivée），
reviewer 依 status 文字判定（archiv、abrog… 算註銷）。新檔沒有的 CIS 保留原狀態。
"""
import time

import requests

RAW_FILE = "raw/CIS_bdpm.json"
URL = "https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt"


def fetch():
    for attempt in range(4):
        try:
            r = requests.get(URL, timeout=180)
            r.raise_for_status()
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(10 * (attempt + 1))
    raw = r.content
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    out = []
    for line in text.splitlines():
        c = line.split("\t")
        if len(c) >= 7 and c[0].strip().isdigit():
            out.append({"cis": c[0].strip(), "name": c[1].strip(), "statut_amm": c[4].strip(), "commercialisation": c[6].strip()})
    return out


def validate(new, old):
    p = []
    if len(new) < 10000:
        p.append(f"只解析出 {len(new)} 筆（BDPM 通常 >15,000 筆），疑似格式改變")
    if sum(1 for r in new if not r["statut_amm"]) > 0.01 * max(1, len(new)):
        p.append("超過 1% 缺 Statut administratif 欄")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["cis"]: r["statut_amm"] for r in new}


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    if rec.get("status") == new:
        return False
    rec["status"] = new
    return True
