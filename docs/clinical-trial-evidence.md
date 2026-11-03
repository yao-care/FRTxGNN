---
layout: default
title: "Médicaments en France : essais pour une nouvelle indication"
nav_order: 25
permalink: /clinical-trial-evidence/
description: "Médicaments de la BDPM (ANSM) dont la nouvelle indication prédite par TxGNN a des preuves d'essais cliniques (L1-L2) : indication, niveau, essais."
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答 AI 搜尋常問的「本國藥物中，哪些新適應症有臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字。
收錄＝公開藥物頁（排除 id_redirect 與 noindex）中 evidence_level 為 L1 或 L2（本站 evidence-high 標準：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁快速總覽表；下列欄名是本站藥物頁實際用到的寫法（建頁時逐頁核對），
新寫法抓不到時顯示「voir le rapport」、等級仍取 front matter。試驗數＝該藥物頁引用的不重複 NCT 編號數。
{%- endcomment -%}
{%- assign ind_labels = "Nouvelle Indication Prédite|Nouvelle indication prédite|Nouvelle Indication Predite" | split: "|" -%}
{%- assign lev_labels = "Niveau de Preuve|Niveau de preuve" | split: "|" -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# Médicaments en France avec des preuves d'essais cliniques pour une nouvelle indication

<p class="key-answer" data-question="Quels médicaments en France ont des preuves d'essais cliniques pour une nouvelle indication ?">
<strong>{{ trial_drugs.size }}</strong> des {{ listed.size }} médicaments disposant d'un rapport FRTxGNN ont une nouvelle indication prédite par TxGNN classée au niveau de preuve <strong>L1 ou L2</strong> ({{ l1.size }} en L1, {{ l2.size }} en L2) : des preuves issues d'essais cliniques (essais randomisés, essais de phase 2–3 ou revues systématiques) ont donc été trouvées.
</p>

Les médicaments proviennent de la Base de données publique des médicaments ([BDPM](https://base-donnees-publique.medicaments.gouv.fr/), ANSM) : médicaments autorisés en France, avec le statut de leur AMM dans chaque rapport ; la liste reflète les rapports de médicaments mis à jour pour la dernière fois le {{ latest_date }}.

<div class="key-takeaway">
Des preuves d'essais pour une indication prédite ne démontrent pas l'efficacité. Chaque candidat ci-dessous <strong>nécessite encore une validation clinique</strong> et un examen réglementaire avant tout usage clinique.
</div>

---

## Médicaments avec preuves d'essais (L1–L2)

<div class="table-wrapper"><table>
<thead>
<tr><th>Médicament</th><th>Nouvelle indication prédite</th><th>Niveau de preuve</th><th>Essais enregistrés cités (NCT)</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign indication = "" -%}
{%- for lab in ind_labels -%}{%- if indication == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign qo = drug.content | split: needle -%}{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign level_cell = "" -%}
{%- for lab in lev_labels -%}{%- if level_cell == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign lv = drug.content | split: needle -%}{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}voir le rapport{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">(avec réserve)</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## Comment lire cette liste

- **Niveau de preuve** suit les [critères]({{ '/evidence-high/' | relative_url }}) du site : L1 = Plusieurs ECR de phase 3 / revues systématiques ; L2 = Un seul ECR ou plusieurs essais de phase 2. « (avec réserve) » signifie que le rapport nuance le niveau ; lisez la note du rapport avant de vous y fier.
- **Nouvelle indication prédite** est la prédiction principale de chaque rapport. Les indications et contre-indications déjà enregistrées dans le graphe de connaissances de TxGNN sont exclues, mais certaines prédictions peuvent encore recouper un usage établi ; le rapport le précise le cas échéant.
- **Essais enregistrés cités** compte les numéros ClinicalTrials.gov (NCT) cités dans le rapport. Les rapports citent une sélection des essais trouvés ; 0 signifie que le rapport ne cite aucun essai enregistré, et sa section sur les preuves bibliographiques indique le fondement du niveau.
- Pour tous les niveaux et la méthode complète, voir [Preuves élevées (L1-L2)]({{ '/evidence-high/' | relative_url }}), [Tous les médicaments]({{ '/drugs/' | relative_url }}) et la [méthodologie]({{ '/methodology/' | relative_url }}).

---

<div class="disclaimer">
<strong>Avertissement</strong><br>
Ce rapport est destiné uniquement à la recherche académique et <strong>ne constitue pas un avis médical</strong>. Suivez toujours les instructions de votre médecin ; ne modifiez jamais votre traitement de votre propre initiative. Toute décision de repositionnement de médicament nécessite une validation clinique complète et un examen réglementaire.
<br><br>
<small>Relu par : 藥提醒科技有限公司 (yao.care)</small>
</div>
