---
layout: default
title: Prédiction du modèle uniquement (L5)
nav_order: 23
permalink: /evidence-low/
description: "660 médicaments de niveau de preuve L5 sur ce site (France), p. ex. Salbutamol, Acyclovir, Adalimumab, avec pour chacun la principale indication prédite, les AMM de la BDPM et le journal de vérification."
---

# Prédiction du modèle uniquement (L5)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Cette page présente **{{ site.data.evidence_tier_facts.low.count }}** des **{{ site.data.drug_stats.total_drugs }}** médicaments ayant un rapport publié sur ce site ({{ site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %) : L5 **{{ site.data.evidence_tier_facts.low.by_level.L5 }}**.
Part médiane des niveaux L5 sur les 30 sites TxGNN : {{ site.data.evidence_tier_facts.low.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.low.cross.median_share %}Ce site est au-dessus de la médiane.{% elsif ev_share < site.data.evidence_tier_facts.low.cross.median_share %}Ce site est en dessous de la médiane.{% else %}Ce site est à la médiane.{% endif %}

{% if site.data.evidence_tier_facts.low.count > 0 %}
Dans les données locales (AMM de la BDPM), **{{ site.data.evidence_tier_facts.low.with_current }}** de ces médicaments ont au moins une autorisation actives, **{{ site.data.evidence_tier_facts.low.none_current }}** en ont mais aucune actives et **{{ site.data.evidence_tier_facts.low.without_data }}** ne figurent pas dans les données locales. **{{ site.data.evidence_tier_facts.low.with_reviews }}** ont des entrées dans le journal de vérification (corrections de données réglementaires sur la page du médicament). **{{ site.data.evidence_tier_facts.low.cross.unique_drugs }}** ont une indication prédite qu'aucun autre site TxGNN ne mentionne pour le même médicament.
{% if site.data.evidence_tier_facts.low.none_current_list.size > 0 %}

Avec des autorisations, mais aucune actives : {% for r in site.data.evidence_tier_facts.low.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}

Les médicaments ayant une autorisation locale actives sont présentés en premier.
{% endif %}

Définition de tous les niveaux : [Méthodologie]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidats reposant uniquement sur la prédiction du modèle, sans preuve chez l'humain à ce jour
</p>

---

## Critères

| Niveau | Définition | Signification clinique |
|-------|------------|------------------|
| **L5** | Prédiction du modèle uniquement | Stade d'hypothèse ; aucune preuve chez l'humain à ce jour |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L5 ({{ site.data.evidence_tier_facts.low.by_level.L5 }} médicaments)

<!-- tier-table:start L5（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Médicament | Niveau | Principale nouvelle indication prédite | AMM de la BDPM : actives / total | Journal de vérification | Uniquement sur ce site |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.low.rows %}{% if r.l == "L5" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}oui ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Avertissement</strong><br>
Ce rapport est destiné uniquement à la recherche académique et <strong>ne constitue pas un avis médical</strong>. Suivez toujours les instructions de votre médecin ; ne modifiez jamais votre traitement de votre propre initiative. Toute décision de repositionnement de médicament nécessite une validation clinique complète et un examen réglementaire.
<br><br>
<small>Relu par : 藥提醒科技有限公司 (yao.care)</small>
</div>
