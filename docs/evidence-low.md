---
layout: default
title: Prédiction du modèle uniquement (L5)
nav_order: 23
permalink: /evidence-low/
description: "Candidats de niveau L5 dans FRTxGNN : prédiction du modèle uniquement, sans preuve clinique ni littérature à ce jour."
---

# Prédiction du modèle uniquement (L5)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Candidats reposant uniquement sur la prédiction du modèle, sans preuve chez l'humain à ce jour
</p>

---

## Critères

| Niveau | Définition | Signification clinique |
|-------|------------|------------------|
| **L5** | Prédiction du modèle uniquement | Stade d'hypothèse ; aucune preuve chez l'humain à ce jour |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

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
