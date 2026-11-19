---
layout: default
title: Preuves modérées (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "88 médicaments de niveau de preuve L3–L4 sur ce site (France), p. ex. Abatacept, Acitretin, Almitrine, avec pour chacun la principale indication prédite, les AMM de la BDPM et le journal de vérification."
---

# Preuves modérées (L3-L4)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Cette page présente **{{ site.data.evidence_tier_facts.medium.count }}** des **{{ site.data.drug_stats.total_drugs }}** médicaments ayant un rapport publié sur ce site ({{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %) : L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**, L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**.
Part médiane des niveaux L3–L4 sur les 30 sites TxGNN : {{ site.data.evidence_tier_facts.medium.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}Ce site est au-dessus de la médiane.{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}Ce site est en dessous de la médiane.{% else %}Ce site est à la médiane.{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
Dans les données locales (AMM de la BDPM), **{{ site.data.evidence_tier_facts.medium.with_current }}** de ces médicaments ont au moins une autorisation actives, **{{ site.data.evidence_tier_facts.medium.none_current }}** en ont mais aucune actives et **{{ site.data.evidence_tier_facts.medium.without_data }}** ne figurent pas dans les données locales. **{{ site.data.evidence_tier_facts.medium.with_reviews }}** ont des entrées dans le journal de vérification (corrections de données réglementaires sur la page du médicament). **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}** ont une indication prédite qu'aucun autre site TxGNN ne mentionne pour le même médicament.
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

Avec des autorisations, mais aucune actives : {% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Définition de tous les niveaux : [Méthodologie]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidats disposant de preuves préliminaires qui nécessitent une validation complémentaire
</p>

---

## Critères

| Niveau | Définition | Signification clinique |
|-------|------------|------------------|
| **L3** | Études observationnelles / grandes séries de cas | Appui préliminaire ; nécessite une validation complémentaire |
| **L4** | Études précliniques / mécanistiques | Appui théorique ; encore loin d'un usage clinique |

---

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L3 ({{ site.data.evidence_tier_facts.medium.by_level.L3 }} médicaments)

<!-- tier-table:start L3（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Médicament | Niveau | Principale nouvelle indication prédite | AMM de la BDPM : actives / total | Journal de vérification | Uniquement sur ce site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L3" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}oui ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L4 ({{ site.data.evidence_tier_facts.medium.by_level.L4 }} médicaments)

<!-- tier-table:start L4（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Médicament | Niveau | Principale nouvelle indication prédite | AMM de la BDPM : actives / total | Journal de vérification | Uniquement sur ce site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L4" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}oui ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Avertissement</strong><br>
Ce rapport est destiné uniquement à la recherche académique et <strong>ne constitue pas un avis médical</strong>. Suivez toujours les instructions de votre médecin ; ne modifiez jamais votre traitement de votre propre initiative. Toute décision de repositionnement de médicament nécessite une validation clinique complète et un examen réglementaire.
<br><br>
<small>Relu par : 藥提醒科技有限公司 (yao.care)</small>
</div>
