#!/usr/bin/env python3
"""市場段落的許可證表改由程式依證據包產生（2026-11-24，用戶決定「程式產生許可證表」；範本 UkTxGNN／SgTxGNN 同名檔）。

為什麼：藥物頁「## Informations de Marché en France」段落原本是 AI 寫的自由格式許可證表（欄位五花八門，號碼格夾「(annulée)」、
適應症欄全是「Non renseignée」），BDPM 每週變動後表上的狀態就過期，checker 擋整頁、要人處理。
改成程式依證據包（data/bundles/<藥>/drug_bundle.json 的 tfda.records，BDPM CIS_bdpm）產生：

  | Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
  - 列＝證據包存的全部紀錄（收集器最多存 20 筆），有效（Autorisation active）在前，其餘照證據包順序。
  - 狀態欄＝BDPM「Statut administratif de l'AMM」原文的簡寫（Active／Abrogée／Archivée／Suspendue／Retirée）；
    license_adapter 標 bdpm_not_listed 的號碼寫「Ne figure plus dans la BDPM」（不寫撤銷）。
  - 表後一句來源（SOURCE）；證據包只收到部分 AMM（total_matches 大於紀錄數）時另加 PART_NOTE（同 known_use_pages 原本的程式句）。
  - 證據包沒有任何紀錄時不放表，改一句 NONE_LINE。
程式區塊前後有「<!-- licenses:begin -->」「<!-- licenses:end -->」；gate（src/frtxgnn/regulatory/licenses.py）依
snapshots/fr_licenses.json.gz 的 rows 檢查程式區塊＝重算結果。每週許可證排程經 scripts/license_adapter.py 的 sync_tables 重排。

第一次換表（--migrate）時另做兩件事（之後頁面上已是程式區塊，不會再發生）：
  - AI 表緊鄰的上一行／下一行裡，只講「表上列了幾筆／前 N 筆／清單可能不完整」的句子（CAPTION）與子句（CAP_CLAUSE）一併拿掉
    （程式表列出證據包全部紀錄並有自己的說明句，舊說明的筆數會跟新表對不上）；同一行其他句子留著；查核紀錄的更正文字所在的行不動。
  - 錨在被取代的表或說明上的查核紀錄標 status: superseded＋superseded_by（紀錄保留、頁面不顯示框，同 Tw 慣例）。
用法（repo 根目錄，先還原 data/）：
  python3 scripts/sync_license_tables.py [--dry-run] [--migrate] [頁 ...]
  carry_block(old, new)：sync_notes_to_docs.py 整頁重寫時把舊頁的程式區塊移植到新頁。
"""
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC_RE = re.compile(r"^## Informations de [Mm]arch[ée] en France\s*$")
HEAD = ["| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |", "|------|------|------|------|------|"]
SOURCE = "Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier."
PART_NOTE = "Les données ne contiennent qu'une partie des autorisations ; la liste peut être incomplète."
NONE_LINE = "Aucune AMM de ce médicament ne figure dans les données BDPM utilisées pour ce rapport."
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
NOT_LISTED = "Ne figure plus dans la BDPM"
ST = {"autorisation active": "Active", "autorisation abrogée": "Abrogée", "autorisation archivée": "Archivée",
      "autorisation suspendue": "Suspendue", "autorisation retirée": "Retirée"}
SUPERSEDED_BY = "Tableau d'AMM généré par programme (scripts/sync_license_tables.py, 2026-11-24, d'après la BDPM)"
NUMW = r"(?:\d+|une?|deux|trois|quatre|cinq|six|sept|huit|neuf|dix|onze|douze|quinze|vingt)"
# 只講表上列了幾筆的整句說明（--migrate 時跟著舊表拿掉）
CAPTION = re.compile(
    r"^\*?(?:"
    rf"(?:Voici |Aperçu des )?(?:les |Les )?{NUMW} (?:premières|principales)(?: AMM)?(?: (?:sont|figurent) (?:listées|présentées|affichées))?(?: ci-dessous| ci-dessus| ici)?(?: \({NUMW} AMM au total\))?\s*[.:]"
    r"|Principales AMM(?: \(\d+ sur \d+\))?\s*:"
    rf"|(?:La|Cette) liste(?: ci-dessus| ci-dessous)? (?:est limitée aux {NUMW} premières AMM|est (?:probablement )?partielle|peut être partielle|est partielle et ne reprend que {NUMW} AMM|présente les {NUMW} premières)\."
    rf"|Seule?s? (?:les )?{NUMW} (?:premières |principales )?(?:AMM )?(?:sur (?:les )?{NUMW}(?: recensées)? )?(?:sont|figurent) (?:listées|présentées)(?: ci-dessus| ci-dessous| ici)?(?: \(limite du format\))?\."
    rf"|Le tableau ci-dessus présente les {NUMW} premières\."
    rf"|{NUMW} AMM sur {NUMW} sont (?:listées|affichées)\."
    rf"|{NUMW} AMM sont présentées sur un total de {NUMW}\."
    r"|Les cinq AMM ci-dessous sont des exemples\."
    r"|Les données ne contiennent qu'une partie des autorisations ; la liste peut être incomplète\."
    r")\*?$", re.I)
# 同一句後半只講表上列了幾筆的子句（「…; seules les 5 premières sont listées ici.」）：--migrate 時只拿掉這個子句
CAP_CLAUSE = re.compile(rf"\s*;\s*(?:seules les {NUMW} (?:premières|principales) sont (?:listées|présentées)(?: ici| ci-dessus| ci-dessous)?|ce tableau en présente les {NUMW} premières)(?=\.$)", re.I)
SPLIT = re.compile(r"(?<=[.!?:])\s+(?=[A-ZÀ-Ý*\[(«])")


def cell(x, n=90):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    return t if len(t) <= n else t[:n - 1].rstrip() + "…"


def status_label(r):
    if r.get("bdpm_not_listed"):
        return NOT_LISTED
    s = str(r.get("status") or "").strip()
    return ST.get(s.lower(), s or "–")


def table_rows(recs):
    seen, act, rest = set(), [], []
    for r in recs:
        k = str(r.get("license_id") or "").strip()
        if not k or k in seen:
            continue
        seen.add(k)
        lab = status_label(r)
        forme = str(r.get("dosage_form") or "").strip()
        row = f"| {k} | {cell(r.get('brand_name_zh') or r.get('brand_name_en'))} | {cell(forme[:1].upper() + forme[1:], 60) or '–'} " \
              f"| {cell(r.get('license_holder') or r.get('manufacturer'), 60) or '–'} | {lab} |"
        (act if lab == "Active" else rest).append(row)
    return act + rest


def rows_of(tf, fc=None):
    """快照用：(表格列, 證據包總數)，跟 process 同一套"""
    rows = table_rows(tf.get("records") or [])
    return rows, max(len(rows), int(tf.get("total_matches") or 0))


def program_block(rows, partial=False):
    if not rows:
        return [NONE_LINE]
    return HEAD + rows + ["", SOURCE] + ([PART_NOTE] if partial else [])


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def _section(lines):
    a = next((i + 1 for i, l in enumerate(lines) if SEC_RE.match(l)), None)
    if a is None:
        return None, None
    return a, next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))


def _caption_trim(line, protect=()):
    """拿掉行裡只講表上列了幾筆的整句（CAPTION）與子句（CAP_CLAUSE）：回 (新行, 拿掉的文字)"""
    if not line.strip() or line.startswith(("|", "#", "<!--", "---", ">")):
        return line, []
    if any(line.strip() in p or any(x.strip() and x.strip() in p for x in SPLIT.split(line.strip())) for p in protect):
        return line, []  # 查核紀錄的更正文字所在的行不動（拿掉會讓更正框消失）
    sents = SPLIT.split(line.strip())
    out, gone = [], []
    for x in sents:
        if CAPTION.match(x.strip()):
            gone.append(x.strip())
            continue
        m = CAP_CLAUSE.search(x)
        if m:
            gone.append(m.group(0).strip())
            x = x[:m.start()] + x[m.end():]
        out.append(x)
    if gone:
        return " ".join(out), gone
    return line, []


def process(text, recs, partial=False, migrate=False, protect=()):
    """回傳 (新內容或 None, 拿掉的文字)。只動市場段落的第一張表（或程式區塊）與 --migrate 時緊鄰的表說明。"""
    lines = text.split("\n")
    a, b = _section(lines)
    if a is None:
        return None, ""
    rows = table_rows(recs)
    blk = wrap(program_block(rows, partial))
    removed = []
    if BEGIN in lines[a:b] and END in lines[a:b]:
        x = lines.index(BEGIN, a)
        y = lines.index(END, x)
        out = lines[:x] + blk + lines[y + 1:]
    else:
        tb = [k for k in range(a, b) if lines[k].startswith("|")]
        if not tb:
            if not rows:
                return None, ""
            out = lines[:a] + [""] + blk + [""] + lines[a:]
        else:
            x = y = tb[0]
            while y + 1 < b and lines[y + 1].startswith("|"):
                y += 1
            removed += lines[x:y + 1]
            pre, post = lines[:x], lines[y + 1:]
            if migrate:
                k = len(pre) - 1
                while k >= a and not pre[k].strip():
                    k -= 1
                if k >= a:
                    nl, cap = _caption_trim(pre[k], protect)
                    if cap:
                        pre[k] = nl
                        removed += cap
                k = 0
                while k < len(post) and k < b - y - 1 and not post[k].strip():
                    k += 1
                if k < b - y - 1:
                    nl, cap = _caption_trim(post[k], protect)
                    if cap:
                        post[k] = nl
                        removed += cap
            out = pre + [""] + blk + [""] + post
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return (t2 if t2 != text else None), "\n".join(removed)


def carry_block(old_text, new_text):
    """sync_notes_to_docs.py 重寫整頁時用：舊頁的程式區塊移植到新頁市場段落（取代新頁段落的第一張表）；舊頁沒有就原樣"""
    old = old_text.replace("\r\n", "\n").split("\n")
    if BEGIN not in old or END not in old:
        return new_text
    blk = old[old.index(BEGIN):old.index(END) + 1]
    lines = new_text.split("\n")
    a, b = _section(lines)
    if a is None:
        return new_text
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if BEGIN in lines[a:b]:
        x = lines.index(BEGIN, a)
        out = lines[:x] + blk + lines[lines.index(END, x) + 1:]
    elif not tb:
        out = lines[:a] + [""] + blk + [""] + lines[a:]
    else:
        x = y = tb[0]
        while y + 1 < b and lines[y + 1].startswith("|"):
            y += 1
        out = lines[:x] + [""] + blk + [""] + lines[y + 1:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def bundle_for(stem):
    for key in (stem, stem.replace("-", "_"), stem.replace("_", "-")):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return json.loads(f.read_text(encoding="utf-8"))
    return None


def _skip(raw):
    h = raw[:3000]
    return "layout: id_redirect" in h or 'http-equiv="refresh"' in h


def supersede(removed_by_page, today=None):
    """--migrate 時：錨在拿掉的文字上、新頁面上也找不到的查核紀錄標 superseded（紀錄保留）。回傳標記的 id"""
    data = ROOT / "docs/_data/drug_reviews.json"
    doc = json.loads(data.read_text(encoding="utf-8"))
    today = today or dt.date.today().isoformat()
    marked = []
    for r in doc["records"]:
        stem = r["file"][:-3]
        gone = removed_by_page.get(stem)
        if not gone or r.get("status") or r.get("action") not in ("correct", "annotate", "rereview"):
            continue
        page = (ROOT / "docs/_drugs" / r["file"]).read_text(encoding="utf-8")
        page = re.sub(r"<!-- review:begin (\S+) -->.*?<!-- review:end \1 -->", "", page, flags=re.S)
        page = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), "", page, flags=re.S)  # 程式表裡的號碼不算錨點
        keys = [x for x in (r.get("anchor"), r.get("replacement"), r.get("claim")) if x and x.strip()]
        if not keys:
            continue
        loc = r.get("anchor") or (r.get("replacement") if r["action"] == "correct" else r.get("claim")) or r.get("claim")
        if loc and loc.strip() and loc in page:
            continue  # 錨點還在頁面上：照舊套用
        if any(k in gone or any(k.strip() in g for g in gone.split("\n") if g) or any(g.strip() and g.strip() in k for g in gone.split("\n"))
               for k in keys):
            r["status"] = "superseded"
            r["superseded_by"] = SUPERSEDED_BY
            r["superseded_on"] = today
            marked.append(r["id"])
    if marked:
        data.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return marked


def _protect():
    out = {}
    f = ROOT / "docs/_data/drug_reviews.json"
    if f.exists():
        for r in json.loads(f.read_text(encoding="utf-8")).get("records", []):
            if r.get("status"):
                continue
            out.setdefault(r["file"][:-3], []).extend(x for x in (r.get("replacement"), r.get("anchor")) if x and x.strip())
    return out


def resync(stems=None, dry=False, migrate=False):
    """回傳 ([(頁, 欄位, 前值, 後值)], {頁: 拿掉的文字})"""
    changed, removed = [], {}
    prot = _protect() if migrate else {}
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if stems is not None and page.stem not in stems:
            continue
        b = bundle_for(page.stem)
        if b is None:
            continue
        raw = page.read_bytes().decode("utf-8")
        if _skip(raw):
            continue
        crlf = "\r\n" in raw[:500]
        tf = b.get("tfda") or {}
        recs = tf.get("records") or []
        new, gone = process(raw.replace("\r\n", "\n"), recs, int(tf.get("total_matches") or 0) > len(recs), migrate,
                            prot.get(page.stem, ()))
        if new is None:
            continue
        changed.append((page.stem, "Tableau des AMM (programme)", "", f"{len(table_rows(recs))} lignes"))
        if gone:
            removed[page.stem] = gone
        if not dry:
            page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return changed, removed


def main(argv):
    dry, migrate = "--dry-run" in argv, "--migrate" in argv
    only = {a for a in argv if not a.startswith("--")} or None
    changed, removed = resync(only, dry, migrate)
    print(f"許可證表（程式）改 {len(changed)} 頁" + (f"；拿掉舊表／表說明的頁 {len(removed)}" if migrate else ""))
    if migrate and not dry:
        ids = supersede(removed)
        print(f"錨在被取代的表或表說明上的查核紀錄標 superseded：{len(ids)} 筆")
        for i in ids:
            print("  ", i)


if __name__ == "__main__":
    main(sys.argv[1:])
