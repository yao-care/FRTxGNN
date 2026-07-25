---
layout: default
title: Preuves élevées (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "Candidats au repositionnement de médicaments de niveau L1-L2 dans FRTxGNN, appuyés par des essais cliniques ou des revues systématiques."
---

# Preuves élevées (L1-L2)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidats pouvant être évalués en priorité sur le plan clinique
</p>

---

## Critères

| Niveau | Définition | Signification clinique |
|-------|------------|------------------|
| **L1** | Plusieurs ECR de phase 3 / revues systématiques | Appui solide ; un usage clinique peut être envisagé |
| **L2** | Un seul ECR ou plusieurs essais de phase 2 | Appui modéré ; des essais de validation peuvent être conçus |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

### L1 ({{ l1_drugs.size }} médicaments)

| Médicament | Indications | Lien |
|---------|---------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Voir le rapport]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 ({{ l2_drugs.size }} médicaments)

| Médicament | Indications | Lien |
|---------|---------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Voir le rapport]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Avertissement</strong><br>
Ce rapport est destiné uniquement à la recherche académique et <strong>ne constitue pas un avis médical</strong>. Suivez toujours les instructions de votre médecin ; ne modifiez jamais votre traitement de votre propre initiative. Toute décision de repositionnement de médicament nécessite une validation clinique complète et un examen réglementaire.
<br><br>
<small>Relu par : 藥提醒科技有限公司 (yao.care)</small>
</div>
