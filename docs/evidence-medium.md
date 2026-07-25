---
layout: default
title: Preuves modérées (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "Candidats au repositionnement de médicaments de niveau L3-L4 dans FRTxGNN, appuyés par des données observationnelles ou précliniques."
---

# Preuves modérées (L3-L4)

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

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

### L3 ({{ l3_drugs.size }} médicaments)

| Médicament | Indications | Lien |
|---------|---------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Voir le rapport]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 ({{ l4_drugs.size }} médicaments)

| Médicament | Indications | Lien |
|---------|---------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Voir le rapport]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Avertissement</strong><br>
Ce rapport est destiné uniquement à la recherche académique et <strong>ne constitue pas un avis médical</strong>. Suivez toujours les instructions de votre médecin ; ne modifiez jamais votre traitement de votre propre initiative. Toute décision de repositionnement de médicament nécessite une validation clinique complète et un examen réglementaire.
<br><br>
<small>Relu par : 藥提醒科技有限公司 (yao.care)</small>
</div>
