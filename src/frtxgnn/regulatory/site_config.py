"""本站查核機制的在地設定（2026-11-12 建；核心流程比照 TwTxGNN、UsTxGNN，程式在同目錄與 scripts/）。

頁面上的查核框、查核紀錄表、說明文字用本站語言（法文）；依據是 BDPM（Base de données publique des médicaments）。
改這裡的字樣後跑 python3 scripts/apply_drug_reviews.py 重套，gate（scripts/check_seo_docs.py）會檢查。
COMMITS／REGEN_COMMITS：2026-10-31～11-06 正文的許可證刪改提交與期間內 AI 重產報告的提交（scripts/reviews_from_edits.py --git 用）。
"""
import json as _json

C = _json.loads(r"""{
 "SITE": "FRTxGNN",
 "ID_PREFIX": "fr",
 "SNAPSHOT": "fr_licenses.json.gz",
 "HEADER_LABEL": "Niveau de preuve",
 "OVERVIEW_LABELS": [
  "Niveau de Preuve",
  "Niveau de preuve"
 ],
 "WITHDRAWN_RE": "Retiré|Retirée",
 "DESC_LEVEL_RE": "niveau de preuve (L[1-5]|N/A)",
 "DESC_LEVEL_FMT": "niveau de preuve {lv}",
 "NA_DESC": "usages connus uniquement",
 "HEADER_RULE_NOTE": "2026-11-12 實測：有 Quick Overview 等級的 790 頁，頁首全部等於第一個等級（整格取最高會有 16 頁不同）",
 "MARKET_RE": "[Mm]arch[ée]",
 "ID_RE": "\\b\\d{8}\\b",
 "PROSE_ID_RE": null,
 "ORIGINAL_LABELS": [
  "Indication Originale",
  "Indication originale"
 ],
 "ORIGINAL_NONE_RE": "^\\s*(non renseign|non disponible|aucune|n/a|–|-)",
 "ORIGINAL_SPLIT_RE": "[;,/()]+|\\bet\\b|\\bou\\b",
 "ORIGINAL_NOTE": "2026-11-12：證據包的許可證紀錄來自 BDPM（CIS_bdpm）；可比對頁數以程式輸出為準",
 "COMMITS": [
  "71f8271a",
  "a38eef41"
 ],
 "REGEN_COMMITS": [
  "afe67379",
  "92d85850",
  "0180c76b",
  "f4008db7",
  "8f5be5fd",
  "cf6bc19c",
  "915089f6",
  "438ba79b",
  "bae2335b",
  "35a09b45",
  "1fc6254b"
 ],
 "SOURCES": [
  {
   "title": "Base de données publique des médicaments (BDPM) – CIS_bdpm",
   "url": "https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt"
  }
 ],
 "PROGRAM_LINE_RE": null,
 "CLASSIFY": [
  [
   "tw",
   "Ta[iï]wan|TFDA|台灣|臺灣"
  ],
  [
   "combo",
   "monocomposant|en association|combinaison|principe actif unique|mono-?principe"
  ],
  [
   "cancel",
   "annul|abrog|retir|suspend|caduc|non commercialis|aucune AMM (?:valide|active|en vigueur)|n'est (?:plus )?(?:autoris|commercialis)|archiv"
  ],
  [
   "count",
   "\\b\\d+\\b[^.;]{0,40}(?:AMM|autorisation|présentation|spécialit|produit)|(?:AMM|autorisation|présentation)[^.;]{0,30}\\b\\d+\\b|\\b(?:tous|toutes|les deux)\\b[^.;]{0,30}(?:AMM|valide)|\\bvalides?\\b"
  ],
  [
   "product",
   "\\b(?:sous forme|forme pharmaceutique|comprimé|gélule|injectable|pommade|commercialis)"
  ]
 ],
 "T": {
  "label": {
   "correct": "Correction de vérification",
   "annotate": "Note de vérification",
   "rereview": "Réévaluation en attente",
   "rereview_result": "Résultat de la réévaluation"
  },
  "action": {
   "correct": "Corrigé",
   "annotate": "Note ajoutée",
   "rereview": "Marqué pour réévaluation",
   "section": "Section sourcée ajoutée",
   "rereview_result": "Réévaluation effectuée",
   "header_level": "Niveau de preuve de l'en-tête recalculé à partir de l'aperçu rapide",
   "description_level": "Niveau de preuve de la description aligné sur l'en-tête"
  },
  "verdict": {
   "maintain": "Maintenu",
   "downgrade": "Abaissé",
   "upgrade": "Relevé",
   "withdraw": "Retiré"
  },
  "log_head": "## Journal de vérification",
  "disclaimer_re": "Avertissement",
  "log_cols": [
   "Date de vérification",
   "Élément",
   "Action",
   "Source"
  ],
  "level_same": "niveau de preuve {o} inchangé",
  "level_change": "niveau de preuve {o} → {n}",
  "orig": "Texte initial : « {x} »",
  "table_updated": "Les éléments « {labels} » de cette page ont été mis à jour selon le résultat de la réévaluation ; les valeurs d'origine figurent dans le journal ci-dessous.",
  "decision": "Recommandation de décision : {x}",
  "source": "Source",
  "rereviewed": "Marqué pour réévaluation → réévalué (voir le résultat de la réévaluation)",
  "hdr": "Niveau de preuve de l'en-tête recalculé à partir de l'aperçu rapide ({o} → {n})",
  "hdr_withdraw": "Prédiction principale retirée lors de la réévaluation ; niveau de preuve de l'en-tête recalculé ({o} → {n})",
  "now_listed": ", désormais classé sous « {x} »",
  "rr": "Réévaluation : {v}, {c}",
  "tu": " ; {l} : « {a} » → « {b} »",
  "desc": "Description de la page : « {a} » remplacé par « {b} » (suit l'en-tête ; reste du texte inchangé, original conservé dans le journal)",
  "revised": " (révisé le {d} ; version antérieure conservée dans le journal)",
  "superseded": "Remplacé par le tableau d'AMM généré par programme (auparavant : {a})",
  "regen": "N'apparaît plus après la régénération du rapport ({d} : {n} ; auparavant : {a})",
  "program": "N'apparaît plus après une correction du programme ({d} : {n} ; auparavant : {a})",
  "withdrawn": "Vérification retirée ({d} : {n} ; auparavant : {a})",
  "intro": "Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.",
  "intro_header": "Voici le journal de vérification de cette page ; le niveau de preuve de l'en-tête suit l'aperçu rapide. Les prédictions du modèle, le tableau récapitulatif et les conclusions n'ont pas été réécrits.",
  "intro_rr": "Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base et le texte de la prédiction n'a pas été réécrit ; les niveaux de preuve et les décisions n'ont été modifiés que par un résultat de réévaluation (abaissement, relèvement ou retrait), les valeurs d'origine figurant ci-dessous.",
  "figures": "Les données (Base de données publique des médicaments (BDPM)) recensent {total} AMM pour ce médicament, dont {valid} valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché.",
  "data_as_of": "Base de données publique des médicaments (BDPM), au {date}",
  "notes": {
   "rewrite": "Corrigé : l'affirmation ne correspondait pas aux données d'AMM ({d}) et a été remplacée par le texte actuel.",
   "tw": "Supprimé : texte résiduel du modèle taïwanais (TFDA), sans objet pour cette page.",
   "combo": "Supprimé : l'indication de médicaments monocomposants ou en association ne correspondait pas aux données d'AMM ({d}).",
   "cancel": "Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM ({d}).",
   "count": "Supprimé : le nombre ou le statut des AMM indiqué ne correspondait pas aux données d'AMM ({d}).",
   "product": "Supprimé : la description des spécialités ne correspondait pas aux données d'AMM ({d}).",
   "generic": "Supprimé : l'affirmation contredisait les données d'AMM ({d})."
  },
  "notes_with_figures": [
   "cancel",
   "count",
   "product",
   "generic"
  ],
  "summary": "Supprimé : « {x} »",
  "regen_note": "le rapport a été régénéré en novembre 2026 et ne contient plus cette affirmation"
 }
}""")
