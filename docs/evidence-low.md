---
layout: default
title: Prédiction du modèle uniquement (L5)
nav_order: 23
permalink: /evidence-low/
description: "Candidats de niveau L5 dans FRTxGNN : prédiction du modèle uniquement, sans preuve clinique ni littérature à ce jour."
---

# Prédiction du modèle uniquement (L5)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L5 %}
Cette page présente **{{ pd_m }}** des **{{ site.data.drug_stats.total_drugs }}** médicaments ayant un rapport publié sur ce site ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %). Définition des niveaux : [Méthodologie]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

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

### L5 ({{ l5_drugs.size }} médicaments)

| Médicament | Indications | Lien |
|---------|---------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Voir le rapport]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Avertissement</strong><br>
Ce rapport est destiné uniquement à la recherche académique et <strong>ne constitue pas un avis médical</strong>. Suivez toujours les instructions de votre médecin ; ne modifiez jamais votre traitement de votre propre initiative. Toute décision de repositionnement de médicament nécessite une validation clinique complète et un examen réglementaire.
<br><br>
<small>Relu par : 藥提醒科技有限公司 (yao.care)</small>
</div>
