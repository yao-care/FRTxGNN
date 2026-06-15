---
layout: default
title: Doxycycline
parent: 僅模型預測 (L5)
nav_order: 109
evidence_level: L5
indication_count: 10
---

# Doxycycline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Doxycycline : Des Infections Bactériennes à la Kératoconjonctivite Épithéliale Ponctuée

## Résumé en Une Phrase

La doxycycline est un antibiotique à large spectre de la famille des tétracyclines, principalement utilisé dans le traitement des infections bactériennes intracellulaires telles que les infections à *Chlamydia trachomatis*, *Rickettsia spp.* et *Mycoplasma spp.*, ainsi que dans diverses infections courantes à bactéries sensibles.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **Kératoconjonctivite Épithéliale Ponctuée**,
avec **0 essai clinique** et **1 publication** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée dans ce pack (antibiotique tétracycline à large spectre — infections bactériennes intracellulaires et systémiques) |
| Nouvelle Indication Prédite | Kératoconjonctivite Épithéliale Ponctuée |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Non commercialisé (données pipeline — vérification ANSM requise) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce pack. Sur la base des informations connues, la doxycycline appartient à la classe des tétracyclines ; son efficacité dans les infections à *Chlamydia trachomatis* a été largement prouvée, et mécanistiquement elle agit en inhibant la synthèse protéique bactérienne par liaison à la sous-unité ribosomale 30S, bloquant l'accès des ARNt aminoacylés au site A du ribosome. Cette action est particulièrement efficace contre les pathogènes intracellulaires obligatoires.

La kératoconjonctivite épithéliale ponctuée peut constituer une séquelle cornéenne persistante après résolution d'une conjonctivite folliculaire à *Chlamydia trachomatis*. Comme le décrit la seule publication disponible (PMID 1424659, 1992), des lésions épithéliales cornéennes bilatérales récurrentes avec aspect ponctué à la fluorescéine ont été observées chez des patients pourtant traités par tétracycline ou doxycycline orale, après disparition des follicules. La prédiction du modèle TxGNN capture donc vraisemblablement la relation mécanistique indirecte entre l'activité anti-chlamydiale de la doxycycline et cette manifestation oculaire post-infectieuse.

Il convient toutefois de souligner que la kératoconjonctivite épithéliale ponctuée ne constitue pas une indication thérapeutique directe reconnue de la doxycycline. La prédiction repose sur une extension logique du mécanisme d'action plutôt que sur des preuves cliniques contrôlées, ce qui limite fortement la portée opérationnelle de cette indication.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Série de cas | *Cornea* | Deux cas de kératite épithéliale ponctuée bilatérale récurrente après traitement d'une conjonctivite folliculaire à *Chlamydia trachomatis* par tétracycline ou doxycycline orale ; les lésions cornéennes (opacités grisâtres ponctuées, fluorescéine positive, œdème stromal antérieur focal) persistaient malgré la résolution des follicules, suggérant une atteinte post-infectieuse indépendante de l'éradication du pathogène |

---

## Informations de Marché en France

Aucune AMM documentée dans ce pack de données.

> **Remarque importante :** Le statut « Non commercialisé » et l'absence d'AMM reflètent les données issues du pipeline de collecte (base réglementaire taiwanaise — TFDA, 0 résultat trouvé). Ce résultat est vraisemblablement un artefact du pipeline et ne correspond pas à la réalité du marché français : la doxycycline est un médicament établi, disponible en Europe sous plusieurs spécialités (ex. : Doxypalu®, Tolexine®, Vibramycine®). Une vérification directe auprès de l'ANSM est impérative avant toute interprétation réglementaire.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le niveau de preuve L4 est insuffisant pour aller au-delà d'une question de recherche exploratoire. La prédiction TxGNN repose sur une relation pathogène–médicament indirecte sans aucun essai clinique dédié à cette indication spécifique, et la seule publication disponible est une série de deux cas datant de 1992 sans groupe contrôle.

**Pour avancer, les éléments suivants sont nécessaires :**

- Vérification du statut réglementaire réel auprès de l'ANSM (les données pipeline semblent erronées)
- Données complètes sur le mécanisme d'action (MOA) via DrugBank
- Données de sécurité complètes (mises en garde ANSM, contre-indications, interactions médicamenteuses)
- Recherche bibliographique actualisée (post-1992) sur la kératoconjonctivite épithéliale ponctuée d'origine infectieuse ou post-chlamydiale
- Évaluation de la pertinence d'une formulation ophtalmique topique versus traitement systémique pour cette localisation
- Consultation d'un ophtalmologue expert en pathologie de surface oculaire pour valider la plausibilité clinique
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

