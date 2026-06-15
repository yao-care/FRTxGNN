---
layout: default
title: Bicalutamide
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Bicalutamide
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

# Bicalutamide : Du Cancer de la Prostate à l'Hypertrichosis

## Résumé en Une Phrase

Bicalutamide est un antiandrogène non stéroïdien, principalement connu pour son utilisation dans le traitement du cancer de la prostate en bloquant de manière compétitive les récepteurs aux androgènes (AR).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Hypertrichosis**, avec **0 essai clinique** et **1 publication** soutenant actuellement cette direction.
La connexion mécanistique reste indirecte, limitée à un contexte très spécifique de gestion d'effet secondaire, et le niveau de preuve est insuffisant pour envisager une application clinique directe.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer de la prostate (indication internationale reconnue ; non commercialisé en France) |
| Nouvelle Indication Prédite | Hypertrichosis |
| Score de Prédiction TxGNN | 99,69 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations connues, bicalutamide est un antagoniste compétitif du récepteur aux androgènes (AR) : il se lie au récepteur avec haute affinité sans activer la transcription, bloquant ainsi les effets des androgènes endogènes (testostérone, DHT) sur les cellules cibles. Son efficacité dans le cancer de la prostate androgéno-sensible est bien établie.

La croissance des follicules pileux dans les zones sensibles aux androgènes est effectivement régulée par la signalisation AR. En théorie, le blocage de l'AR pourrait atténuer une croissance pilaire excessive médiée par les androgènes. Cependant, l'hypertrichosis — contrairement à l'hirsutisme — n'est généralement pas une condition androgéno-dépendante. Elle peut être d'origine génétique, médicamenteuse (ex. minoxidil, ciclosporine, phénytoïne) ou idiopathique, sans excès d'androgènes circulants.

L'unique preuve disponible est une lettre-commentaire (PMID 35304167, 2022) discutant l'amélioration de l'hypertrichosis induite par le minoxidil grâce au bicalutamide — autrement dit, il s'agit de la gestion d'un effet secondaire indésirable dans un contexte très particulier de l'alopécie féminine, et non d'un traitement de l'hypertrichosis primaire. Le lien mécanistique est donc faible, et cette prédiction TxGNN s'explique probablement par une connexion indirecte dans le graphe de connaissances entre les nœuds « androgènes » et « follicule pileux ».

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Lettre / Commentaire | Journal of the American Academy of Dermatology | Commentaire sur l'utilisation du bicalutamide pour réduire l'hypertrichosis induite par le minoxidil chez des patientes atteintes d'alopécie féminine à pattern ; contexte de gestion d'effet secondaire, non de traitement primaire |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie hormonale ciblée — Antiandrogène non stéroïdien (classe Biarylpropionamide) ; non cytotoxique conventionnel |
| Risque de Myélosuppression | Faible (mécanisme purement hormonal/récepteur, sans effet myélosuppresseur direct) |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | Bilan hépatique (ASAT/ALAT — hépatotoxicité rapportée), NFS de base, PSA dans le contexte oncologique |
| Protection de Manipulation | Précautions standard pour médicaments hormonaux ; manipulation cytotoxique lourde non requise |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
L'hypertrichosis n'étant typiquement pas une maladie androgéno-dépendante, la plausibilité biologique du bicalutamide dans cette indication est faible. L'unique preuve disponible est une lettre commentaire portant sur la gestion d'un effet secondaire dans un contexte très spécifique (alopécie féminine traitée au minoxidil), sans aucun essai clinique, ce qui ne justifie pas de poursuivre le développement.

> **Note importante :** Parmi les 10 indications prédites analysées dans ce dossier, le **carcinome mammaire féminin** (rang 9, score TxGNN 99,11 %) représente le candidat le plus avancé sur le plan clinique avec un niveau de preuve **L2** (1 essai de Phase 2 actif, 20 publications, dont plusieurs études mécanistiques et précliniques). Si l'objectif est d'identifier la piste de repositionnement la plus prometteuse pour bicalutamide, c'est cette indication qui devrait faire l'objet d'un rapport prioritaire.

**Pour avancer sur la piste hypertrichosis, les éléments suivants sont nécessaires :**
- Données pharmacologiques complètes (MOA, profil DrugBank) confirmant l'activité anti-AR
- Identification du sous-type d'hypertrichosis ciblé (androgéno-dépendant vs. indépendant) avant toute exploration
- Études précliniques sur des modèles validés d'hypertrichosis androgéno-dépendante
- Évaluation du profil bénéfice/risque dans des populations non oncologiques (exposition à un antineoplastique hormonal pour une indication bénigne)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

