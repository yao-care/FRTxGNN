---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib : Du Cancer du Poumon Non à Petites Cellules ALK+ à la Fibromatose Gingivale

## Résumé en Une Phrase

Brigatinib est un inhibiteur de tyrosine kinase de nouvelle génération (ALK/ROS1/EGFR), reconnu internationalement pour le traitement du cancer du poumon non à petites cellules (CBNPC) ALK-positif, mais non enregistré en France.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **fibromatose gingivale**, avec un score de **99,89%** (rang 1 sur l'ensemble des indications prédites).
Cependant, cette piste ne dispose actuellement d'**aucun essai clinique** ni d'**aucune publication** directement associée, ce qui la classe au niveau de preuve le plus bas (L5).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer du poumon non à petites cellules ALK+ (non enregistré en France) |
| Nouvelle Indication Prédite | Fibromatose gingivale |
| Score de Prédiction TxGNN | 99,89% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de brigatinib ne sont pas disponibles dans ce dossier. Sur la base des informations connues issues de la littérature fournie, brigatinib est un inhibiteur de tyrosine kinase de 2e génération ciblant principalement ALK (Anaplastic Lymphoma Kinase), avec une activité secondaire sur ROS1 et EGFR. Son efficacité dans le CBNPC ALK+ a été démontrée dans plusieurs essais de Phase 3 (ALTA-1L, ALTA-3), justifiant son utilisation comme traitement standard de première et deuxième ligne dans cette indication.

La fibromatose gingivale est une maladie caractérisée par une prolifération excessive du tissu fibreux gingival, dont la pathogenèse est principalement liée à des mutations des gènes SOS1 et FGFR. Ces voies de signalisation n'ont aucune intersection documentée avec l'axe ALK/ROS1/EGFR ciblé par brigatinib. La prédiction de haute probabilité par TxGNN s'explique vraisemblablement par une proximité topologique dans le graphe de connaissances entre les nœuds représentant les maladies fibrotiques, plutôt que par une véritable association biologique mécanistique.

En l'absence de toute littérature ou essai clinique établissant un lien entre brigatinib et la fibromatose gingivale, cette prédiction doit être considérée comme une hypothèse exploratoire nécessitant une validation préclinique approfondie avant tout investissement de recherche.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée — Inhibiteur de tyrosine kinase ALK/ROS1/EGFR de 2e génération |
| Risque de Myélosuppression | Faible à modéré (lymphopénie et neutropénie occasionnellement rapportées dans les essais ALTA-1L) |
| Classification d'Émétogenicité | Faible à modérée (per os, profil similaire aux autres ALK-TKI) |
| Éléments de Surveillance | NFS avec différentielle, bilan hépatique (ASAT/ALAT), fonction pulmonaire (risque de pneumopathie interstitielle précoce caractéristique de brigatinib), pression artérielle, glycémie |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques ; comprimés à avaler entiers, pas de broyage |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

> **Note :** Un cas de syndrome de lyse tumorale fatal induit par brigatinib a été rapporté (PMID 34987411) chez un patient traité séquentiellement par des inhibiteurs ALK pour un adénocarcinome pulmonaire ALK+. Bien que rare dans les tumeurs solides, ce risque mérite une vigilance particulière lors d'une réponse tumorale rapide.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La fibromatose gingivale est une maladie fibrotique d'origine génétique (mutations SOS1/FGFR) sans intersection documentée avec les cibles moléculaires de brigatinib (ALK/ROS1/EGFR). Le score TxGNN élevé (99,89%) reflète probablement une proximité topologique dans le graphe de connaissances plutôt qu'une pertinence biologique réelle, et aucune donnée clinique ou préclinique ne soutient cette direction.

**Pour avancer, les éléments suivants sont nécessaires :**
- Validation du mécanisme d'action (MOA) complet de brigatinib via DrugBank API
- Études précliniques explorant un éventuel effet de brigatinib sur des modèles de fibromatose (cellules fibroblastiques gingivales, modèles murins)
- Analyse des voies SOS1/FGFR pour identifier une éventuelle convergence avec les cibles ALK/ROS1
- Évaluation de l'enregistrement de brigatinib en France (voie ATU/AAP à explorer si pertinence clinique future établie)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

