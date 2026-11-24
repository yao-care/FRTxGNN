"""FR 證據包依成分補收 BDPM 現行清單上屬於本藥、卻不在證據包的 AMM（2026-11-24，用戶決定「依成分補進證據包」；全程不用 AI）。

證據包的許可證紀錄（tfda 區塊）是 collectors/frfda.py 依 data/processed/drug_mapping.csv 收的：CIS 的每個成分名 → DrugBank ID，
跟本藥同一個 DrugBank ID 的 CIS 都收（單方、複方都收），最多存 20 筆、total_matches 記總數。
drug_mapping 的成分名比對只認得「RALOXIFÈNE (CHLORHYDRATE DE)」這種寫法，同一個成分寫成「CHLORHYDRATE DE RALOXIFÈNE」就對不到
（2026-11-24 實測：raloxifene 證據包只收到 OPTRUMA 1 張，BDPM 另有 EVISTA 與 8 張學名藥，成分都是 BDPM 物質代碼 79270）。
這支不放寬成分名比對，改用 BDPM 自己的物質代碼（CIS_COMPO_bdpm.txt 第 3 欄，nature＝SA 的列）：
  1. 本藥的物質代碼＝證據包既有 CIS 的 SA 列中，成分名跟 drug_mapping 裡對到本藥 DrugBank ID 的成分名相同的那幾列
     （成分名完全相同才算，只去重音、大小寫與空白；不去鹽類——去鹽類會把 FLUORURE DE SODIUM、FOLINATE DE CALCIUM 算成 sodium、calcium）；
     證據包裡 2026-10-31 依成分補入的紀錄（source＝BDPM（依成分查詢））直接用它的成分名對 SA 列。
  2. 現行 CIS_COMPO 有這些代碼（SA 列）、不在證據包的 CIS，就是原規則該收、因成分名寫法收不到的 AMM（複方照原規則一起收）。
  3. 只收 CIS_bdpm.txt 有的 CIS（status＝Statut administratif de l'AMM，與排程 license_adapter 相同；只在 CIS_CIP 的 CIS 不收，
     狀態要讀產品頁，交給每週排程）。欄位照 2026-10-31 補入的格式，加 source（BDPM 物質代碼、檔案日期）與 added（補收日）。
  4. 20 筆上限照原收集器（比照 Au add_current_pbs_items.py）：records 未滿 20 筆才存（單方優先），其餘只記在 bdpm_not_stored
     並算進 total_matches；原規則本來就對得到、只是因上限沒存的 CIS（drug_mapping 對到本藥）已算在 total_matches 裡，不重算。
  5. 離子／抗衡離子證據包不擴充（2026-11-24 用戶決定「全站但排除離子類」，EXCLUDE）：drug_mapping 本來就把鹽類的成分名
     對到裸離子的 DrugBank ID（FLUORURE DE SODIUM→sodium、FOLINATE DE CALCIUM→calcium），用物質代碼擴充會把無關的鹽類產品灌進去。
可重複執行、只加不刪（已在證據包或 bdpm_not_stored 的 CIS 不重補）。
用法（repo 根目錄）：python3 scripts/add_current_amm.py --cis CIS_bdpm.txt --compo CIS_COMPO_bdpm.txt [--dry-run] [--report out.tsv]
"""
import argparse
import csv
import json
import re
import sys
import time
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAP = 20  # collectors/frfda.py LocalFDACollector._format 的 records[:20]
SRC_1031 = "BDPM（依成分查詢）"
# 2026-11-24 試跑：這些證據包的 DrugBank ID 是裸離子／元素，擴充後收進的多是別的藥的鹽類（括號內為試跑時會新增的張數與例子）
EXCLUDE = {
    "sodium": "DB09395 鈉離子；會收進 153 張（氯化鈉輸液、DURAPHAT 氟化鈉、fusidate de sodium 等）",
    "potassium": "DB14500 鉀離子；會收進 65 張（DIFFU-K、KALEORID 等氯化鉀，屬補鉀劑而非本頁的鉀）",
    "calcium": "DB01373 鈣離子；會收進 62 張（FOLINATE DE CALCIUM 等，主成分是亞葉酸）",
    "zinc": "DB01593 鋅元素；會收進 16 張（RUBOZINC 等鋅鹽、OLIGOSTIM ZINC CUIVRE 複方）",
    "aluminium": "DB01370 鋁元素；會收進 10 張（MAALOX 等氫氧化鋁／氫氧化鎂制酸劑）",
    "ammonium": "銨離子（試跑 0 張，列入以免日後擴充）",
    "magnesium": "鎂離子（本站目前沒有這個證據包，列入以免日後擴充）",
    "chloride": "氯離子（本站目前沒有這個證據包，列入以免日後擴充）",
}


def rd(p):
    raw = Path(p).read_bytes()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("latin-1")


def norm(x):
    return " ".join(unicodedata.normalize("NFKD", str(x or "")).encode("ascii", "ignore").decode().lower().split())


def base(sub):
    s = re.sub(r"\s*\([^)]*\)", "", norm(sub))
    s = re.sub(r"^\w+(ure|ate|ite|ide)\s+(de|d')\s*", "", s)  # chlorhydrate de quinapril → quinapril
    return s.strip()


def n_ing(s):
    return len([x for x in re.split(r"[;,+/]", str(s or "")) if x.strip()])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cis", required=True)
    ap.add_argument("--compo", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report")
    a = ap.parse_args()

    cis = {}
    for line in rd(a.cis).splitlines():
        c = line.split("\t")
        if len(c) >= 11 and c[0].strip().isdigit():
            cis[c[0].strip()] = c
    sa = {}       # CIS → [(code, 成分名)]（只取 SA 列）
    by_code = {}  # code → {CIS}
    for line in rd(a.compo).splitlines():
        c = line.split("\t")
        if len(c) >= 7 and c[0].strip().isdigit() and c[6].strip() == "SA":
            k, code, name = c[0].strip(), c[2].strip(), c[3].strip()
            sa.setdefault(k, []).append((code, name))
            by_code.setdefault(code, set()).add(k)
    if len(cis) < 12000 or len(sa) < 12000:
        sys.exit(f"CIS_bdpm {len(cis)} 個、CIS_COMPO（SA）{len(sa)} 個，疑似下載或格式有問題")
    fdate = time.strftime("%Y-%m-%d", time.gmtime(Path(a.cis).stat().st_mtime))

    # drug_mapping：CIS → {DrugBank ID: {成分名 base}}（collectors/frfda.py 原收錄就是這樣對的）
    dm = {}
    with open(ROOT / "data/processed/drug_mapping.csv", encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            db = str(r.get("drugbank_id") or "").strip().upper()
            if db and str(r.get("mapping_success")).strip().lower() in ("true", "1", "yes"):
                dm.setdefault(str(r["license_id"]).strip(), {}).setdefault(db, set()).add(norm(r.get("original_ingredient")))

    today = time.strftime("%Y-%m-%d")
    out, n_b, n_stored, n_count, skipped_nocis = [], 0, 0, 0, 0
    for f in sorted((ROOT / "data/bundles").glob("*/drug_bundle.json")):
        if f.parent.name in EXCLUDE:
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        t = b.get("tfda") or {}
        recs = t.get("records") or []
        dbs = {str(x).upper() for x in (t.get("drugbank_ids") or [])}
        if not dbs or not recs:
            continue
        have = {str(r.get("license_id") or "").strip() for r in recs}
        not_stored = t.get("bdpm_not_stored") or []
        have |= {str(x.get("license_id")) for x in not_stored}
        codes = set()
        for r in recs:
            k = str(r.get("license_id") or "").strip()
            if r.get("source") == SRC_1031:
                names = {norm(r.get("ingredients"))}
            else:
                names = set().union(*[v for d, v in dm.get(k, {}).items() if d in dbs]) if dm.get(k) else set()
            codes |= {code for code, name in sa.get(k, []) if norm(name) in names}
        if not codes:
            continue
        cand = set().union(*(by_code.get(c, set()) for c in codes)) - have
        if not cand:
            continue
        skipped_nocis += sum(1 for k in cand if k not in cis)
        cand = [k for k in cand if k in cis]
        if not cand:
            continue
        # 原規則對得到（drug_mapping 對到本藥）＝已算在 total_matches 裡；其他是因成分名寫法收不到的
        known = {k for k in cand if set(dm.get(k, {})) & dbs}
        cand.sort(key=lambda k: (n_ing("; ".join(n for _, n in sa.get(k, []))), k))  # 單方優先
        add_recs, add_count = [], []
        for k in cand:
            c = cis[k]
            sub = "; ".join(name for code, name in sa.get(k, []))
            rec = {"license_id": k, "brand_name_zh": c[1].strip(), "brand_name_en": sub, "ingredients": sub, "indication": "",
                   "dosage_form": c[2].strip(), "manufacturer": c[10].strip(), "license_holder": c[10].strip(),
                   "approval_date": c[7].strip(), "expiry_date": "", "status": c[4].strip(), "commercialisation": c[6].strip(),
                   "source": f"BDPM（物質代碼 {'、'.join(sorted(codes & {code for code, _ in sa.get(k, [])}))}；CIS_bdpm／CIS_COMPO {fdate}）",
                   "added": today}
            if len(recs) + len(add_recs) < CAP:
                add_recs.append(rec)
            else:
                add_count.append({"license_id": k, "brand_name": c[1].strip(), "status": c[4].strip(), "added": today})
            out.append(f"{f.parent.name}\t{'stored' if rec in add_recs else 'counted'}\t{'known' if k in known else 'new'}\t{k}\t{c[1].strip()}\t{c[4].strip()}")
        recs.extend(add_recs)
        tm = int(t.get("total_matches") or 0)
        # 新存進 records 的筆數照原 total_matches 的算法：原規則對不到的才加；對得到的本來就算過
        t["total_matches"] = max(len(recs) + len(not_stored) + len(add_count), tm + sum(1 for k in cand if k not in known))
        if add_count:
            t["bdpm_not_stored"] = not_stored + add_count
        t["records"], t["found"] = recs, True
        b["tfda"] = t
        n_b += 1
        n_stored += len(add_recs)
        n_count += len(add_count)
        if not a.dry_run:
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"補收 {n_stored + n_count} 筆、{n_b} 個證據包（存進 records {n_stored} 筆、超過上限只算張數 {n_count} 筆；"
          f"只在 CIS_CIP、不在 CIS_bdpm 而略過 {skipped_nocis} 筆）{'（試跑，未寫回）' if a.dry_run else ''}")
    if a.report:
        Path(a.report).write_text("pack\tstore\trule\tcis\tname\tstatus\n" + "\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
