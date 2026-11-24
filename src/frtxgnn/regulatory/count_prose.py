"""正文 AMM 張數的程式改寫（2026-11-24，用戶決定；概念比照 KrTxGNN／MyTxGNN 同名檔與 TwTxGNN page_postprocess.rewrite_count_prose，
規則是本站法文句型）。

正文裡「N AMM valides」「N AMM sur M sont valides」「Au total, N AMM sont recensées」這類 BDPM 張數敘述，由程式依許可證快照
（snapshots/fr_licenses.json.gz 的 facts）改寫，每週資料更新後跟著改，不逐筆寫查核紀錄（程式改寫的張數敘述是程式產生的正文）。

只改「句型明確、數字確定是本藥 AMM 張數」的地方，其餘一律不動：
  - 句子要有 AMM／autorisation 字樣，且沒有試驗、文獻、劑量、年份等字樣（NOT_LICENSE）。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、front matter、引言框；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）；事實層 partial 的頁整頁不動。
  - 整句不動（skipped 記 hedged/subset，不列待查）：有保留（au moins、partielle、une partie、environ、plus de）、
    講表上幾筆（listées、affichées、ci-dessus、ci-dessous、tableau、premières、principales、parmi celles）、相對數（autres、dont、
    supplémentaire）、劑型、劑量、廠商、單方／複方子集（seul、association、princeps、génériques…）、證據包或查詢（Evidence Pack、requête）。
  - 數字只認阿拉伯數字與 deux～douze；une／un／seule／unique 不認（單數改成複數會連動動詞與形容詞的配合）。
角色（看數字前後）：sont valides／valides／actives→有效；annulées／abrogées／archivées／retirées→非有效；
「N AMM … sur M」「N des M AMM」的 M、「Sur les M AMM」「Au total, N AMM」「N AMM sont recensées」→總數；
「Les N AMM (…) sont (toutes) valides」→全部有效（總數＝有效數才成立，否則列 premise）。
數字已等於該角色的任一合理讀法（沒有限定詞的總數＝總數或有效數）就不動；不等於時兩種讀法相同才改，不同列 ambiguous。
原數字或新數字是 0 或 1 的不改（0 是前提不同、1 會牽動單複數配合），列 zero-premise／singular。
前提：句子說「toutes valides／aucune annulée」而有效≠總數，或說全部是單方而事實有複方時整句不動、列 premise。
同一行只要有一句含張數而被略過，整行都不動（免得前後句數字對不上）。
"""
from __future__ import annotations

import re

NUMW = {"deux": 2, "trois": 3, "quatre": 4, "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10, "onze": 11, "douze": 12}
SINGW = r"\b(?:une?|seule?|unique|l'unique)\b"
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý*\[(«-])")
NUM = re.compile(r"(?<![\w.,/°-])(\d{1,4}|" + "|".join(NUMW) + r")(?![\w.,/%°-]|,\d)", re.I)
NOUN = r"(?:AMM|autorisations?(?: de mise sur le marché)?)"
LICENSE = re.compile(r"\bAMM\b|\bautorisations?\b", re.I)
NOT_LICENSE = re.compile(r"essai|étude|publication|article|PMID|NCT|patients?|cas\b|\bmg\b|\bml\b|µg|microgramme|%|\b(19|20)\d\d\b|"
                         r"\bans?\b|mois|semaines?|jours?|score|prédiction|interaction|effets? indésirables?|dose", re.I)
HEDGED = re.compile(r"au moins|partielle|partiel|une partie|environ|plus de|moins de|près de|jusqu'à|"
                    r"list[ée]e?s?\b|\bliste\b|affich|ci-dessus|ci-dessous|tableau|premières|principales|présentées|suivantes|exemples?|parmi celles|"
                    r"\bautres?\b|\bdont\b|supplémentaire|également|aussi\b|en plus|"
                    r"\bseule?s?\b|substance unique|principe actif unique|mono-?substance|monocomposant|associations?\b|combin|princeps|"
                    r"génériques?|biosimilaires?|titulaire|détenue|laboratoire|commercialisées par|"
                    r"comprimé|gélule|injectable|solution|suspension|crème|pommade|gel\b|collyre|sirop|poudre|suppositoire|patch|forme|dosage|"
                    r"Evidence Pack|requête|interrog|vétérinaire|\bdes\s+\d+\s+(?:\w+\s+)?(?:recherch|retrouv)", re.I)
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)
CANC = r"(?:annul[ée]e?s|abrog[ée]e?s|archiv[ée]e?s|retir[ée]e?s|suspendues|caduques)"
VALID = r"(?:valides|actives|en vigueur)"


def _val(tok):
    t = tok.lower()
    return NUMW[t] if t in NUMW else int(t)


def _role(s, a, b):
    left, right = s[max(0, a - 30):a].lower(), s[b:b + 70].lower()
    if re.search(r"(?:\bsur|\bdes|\bparmi les|\bsur les|\bsur un total de)\s+$", left):
        return "total"
    if re.match(rf"\s+(?:sont\s+|étant\s+|restent\s+)?{CANC}\b", right) or \
            re.match(rf"\s+{NOUN}\s+(?:\w+\s+)?{CANC}\b", right, re.I):
        return "cancelled"
    if re.match(rf"\s+(?:sont\s+|restent\s+)?{VALID}\b", right) or \
            re.match(rf"\s+{NOUN}\s+(?:françaises\s+)?{VALID}\b", right, re.I):
        return "valid"
    # 「N AMM (françaises) sur M sont valides」「N des M AMM … sont valides」：N 是有效數
    if re.match(rf"\s+(?:{NOUN}\s+(?:françaises\s+)?)?(?:sur|des)\s+\d+\b[^.;]{{0,40}}?\b(?:sont|soient|est)\s+(?:\w+\s+)?{VALID}", right, re.I):
        return "valid"
    if re.match(rf"\s+{NOUN}\b", right, re.I):
        if re.search(r"\bles\s+$", left) and re.match(rf"\s+{NOUN}\s+(?:\w+\s+){{0,3}}(?:sont|étant)\s+(?:toutes\s+|tous\s+)?{VALID}", right, re.I):
            return "allvalid"
        return "total"
    return None


def _readings(role, f, explicit=False):
    t, v, c = f.get("total"), f.get("valid"), f.get("cancelled")
    nonvalid = None if t is None or v is None else t - v
    if role == "cancelled":
        return {c, nonvalid}, (c if c == nonvalid else None)
    if role == "valid":
        return {v}, v
    if role == "allvalid":
        return {t}, t
    if explicit:
        return {t}, t
    return {t, v}, (t if t == v else None)


def _premise_ok(sent, f, roles):
    lo = sent.lower()
    allv = "allvalid" in roles or re.search(r"\b(toutes|tous)\s+(?:\w+\s+)?valides\b|\baucune\s+(?:n'est\s+)?(?:annul|abrog|archiv)|\b0\s+annul", lo)
    if allv and (f.get("valid") != f.get("total") or f.get("cancelled")):
        return False
    return True


ONE = re.compile(r"(?<![\w'])(?:une|l'unique|la seule)\s+(?:seule\s+)?(?:AMM|autorisation)\s+(?:française\s+|recensée\s+|enregistrée\s+)?(?:est\s+)?(?:valide|active|en vigueur)\b"
                 r"|(?<![\w'])une seule AMM\b", re.I)


def rewrite_sentence(sent, f):
    """回傳 (新句子, 跳過理由或 None)。"""
    if ONE.search(sent) and LICENSE.search(sent) and not NOT_LICENSE.search(sent) and not HEDGED.search(sent) \
            and f.get("valid") != 1 and f.get("total") != 1 and not re.search(r"\b(?:pas|plus|sans|ni|aucune?)\b", sent, re.I):
        return sent, "singular"  # 「Une AMM valide」而事實不是 1 張：要改單複數配合，列待查
    if not NUM.search(sent) or not LICENSE.search(sent):
        return sent, None
    if NOT_LICENSE.search(sent):
        return sent, None
    found = [(m, _role(sent, m.start(), m.end())) for m in NUM.finditer(sent)]
    if not any(r for _, r in found):
        return sent, None
    if HEDGED.search(sent):
        return sent, "hedged/subset"
    explicit = any(r in ("valid", "cancelled") for _, r in found)
    subs, roles = [], {r for _, r in found if r}
    for m, role in found:
        if role is None:
            continue
        old = _val(m.group(1))
        ok, v = _readings(role, f, explicit)
        if old in ok:
            continue
        if v is None:
            return sent, "ambiguous"
        if old == 0 or v == 0:
            return sent, "zero-premise"
        if old == 1 or v == 1 or re.search(SINGW + r"\s*$", sent[:m.start()].lower()):
            return sent, "singular"
        subs.append((m, v))
    if not subs:
        return sent, None
    if not _premise_ok(sent, f, roles):
        return sent, "premise"
    out, pos = [], 0
    for m, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(str(v))
        pos = m.end(1)
    out.append(sent[pos:])
    new = "".join(out)
    if new[:1].isdigit() and sent[:1].isalpha():  # 句首原本是文字數字（« Cinq AMM … »）：維持句首大寫的寫法不成立，不改
        return sent, "ambiguous"
    return new, None


def _line(ln, f, protect, skipped):
    if ln.startswith(("|", "#", ">")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格不動。"""
    skipped = []
    if not facts or facts.get("partial") or facts.get("total") is None:
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines = [ln if "\x00" in ln else _line(ln, facts, protect, skipped) for ln in body.split("\n")]
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
