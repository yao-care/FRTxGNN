---
layout: default
title: Tous les médicaments
nav_order: 20
permalink: /drugs/
description: "Tous les rapports de validation de médicaments et les statistiques par niveau de preuve dans FRTxGNN."
---
{% assign l1_count = site.drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = site.drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = site.drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = site.drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = site.drugs | where: "evidence_level", "L5" | size %}

# Tous les médicaments

{{ site.drugs.size }} rapports de validation de médicaments

---

## Répartition par niveau de preuve

| Niveau de preuve | Médicaments | Description |
|---------|--------|------|
| **L1** | {{ l1_count }} | Plusieurs ECR / revues systématiques |
| **L2** | {{ l2_count }} | ECR unique / essais de phase 2 |
| **L3** | {{ l3_count }} | Études observationnelles / grandes séries de cas |
| **L4** | {{ l4_count }} | Études précliniques / mécanistiques |
| **L5** | {{ l5_count }} | Prédiction du modèle uniquement |

---

## Liste complète des médicaments

{% assign all_drugs = site.drugs | sort: 'title' %}

| Médicament | Niveau de preuve | Indications |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}

---

<div class="disclaimer">
<strong>Avertissement</strong><br>
Ce rapport est destiné uniquement à la recherche académique et <strong>ne constitue pas un avis médical</strong>. Suivez toujours les instructions de votre médecin ; ne modifiez jamais votre traitement de votre propre initiative. Toute décision de repositionnement de médicament nécessite une validation clinique complète et un examen réglementaire.
<br><br>
<small>Relu par : 藥提醒科技有限公司 (yao.care)</small>
</div>
