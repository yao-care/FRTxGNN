---
layout: default
title: "Usages connus uniquement (aucune nouvelle prédiction)"
nav_order: 24
permalink: /known-uses/
description: "Pour ces médicaments, tous les candidats du modèle TxGNN sont déjà des usages connus (enregistrés dans le graphe de connaissances ou dans une autorisation)…"
---

# Usages connus uniquement (aucune nouvelle prédiction)

Pour ces médicaments, tous les candidats du modèle TxGNN sont déjà des usages connus (enregistrés dans le graphe de connaissances ou dans une autorisation), il n'y a donc aucune nouvelle indication prédite. Chaque page présente les usages connus et le statut de commercialisation local.

{% assign known_drugs = site.drugs | where: "evidence_level", "N/A" | sort: "title" %}

**{{ known_drugs.size }} médicaments**

| Médicament | Rapport |
|------|------|
{% for drug in known_drugs %}| **{{ drug.title }}** | [Voir la page]({{ drug.url | relative_url }}) |
{% endfor %}
