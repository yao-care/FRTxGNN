---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapone : De la Maladie de Parkinson à la Neurodégénérescence Associée à PLA2G6

## Résumé en Une Phrase

Entacapone est un inhibiteur sélectif de la catéchol-O-méthyltransférase (COMT), utilisé comme traitement adjuvant à la lévodopa dans la prise en charge des fluctuations motrices de la **maladie de Parkinson**.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Neurodégénérescence associée à PLA2G6 (PLAN)**,
sans essai clinique ni publication scientifique soutenant actuellement cette direction spécifique.

---

## Aperçu Rapide

| Élément | Contenu |
|---------|---------|
| Indication Originale | Maladie de Parkinson (adjuvant lévodopa/carbidopa) |
| Nouvelle Indication Prédite | Neurodégénérescence associée à PLA2G6 (PLAN) |
| Score de Prédiction TxGNN | 99.76% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations connues, Entacapone appartient à la classe des inhibiteurs de la COMT — il bloque la dégradation périphérique de la lévodopa par la catéchol-O-méthyltransférase, prolongeant ainsi la fenêtre thérapeutique dopaminergique chez les patients parkinsoniens. Son efficacité dans la maladie de Parkinson comme adjuvant à la lévodopa est établie, et mécanistiquement, il pourrait être envisagé dans d'autres maladies neurodégénératives présentant une composante dopaminergique ou extrapyramidale.

La neurodégénérescence associée à PLA2G6 (PLAN) est une maladie rare causée par des mutations du gène PLA2G6 (codant une phospholipase A2 indépendante du calcium), conduisant à une accumulation de fer dans le cerveau (NBIA — Neurodegeneration with Brain Iron Accumulation). Certaines formes cliniques de PLAN présentent des manifestations extrapyramidales marquées (dystonie, parkinsonisme juvénile), ce qui constitue un lien indirect et théorique avec la pharmacologie de l'inhibition de la COMT.

Cependant, la connexion mécanistique reste hypothétique : la voie COMT/dopamine n'est pas impliquée dans la pathophysiologie primaire liée à PLA2G6 (métabolisme des phospholipides membranaires). Le score élevé du modèle TxGNN (99.76%) pourrait s'expliquer par une proximité dans le graphe de connaissances entre maladies neurodégénératives à composante extrapyramidale, sans refléter nécessairement une pertinence pharmacologique directe. Aucune donnée préclinique ne soutient ce repositionnement à ce stade.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Entacapone ne dispose d'aucune AMM enregistrée dans la base de données consultée (statut : non commercialisé).

> **Note contextuelle** : Entacapone est commercialisé dans d'autres pays (Europe, États-Unis) sous les noms Comtan® (monothérapie COMT) et Stalevo® (combinaison fixe lévodopa/carbidopa/entacapone). L'absence d'enregistrement reflète le périmètre réglementaire de la base de données interrogée.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Vue d'Ensemble des 10 Indications Prédites

| Rang | Indication | Score TxGNN | Niveau de Preuve | Essais | Publications | Recommandation |
|------|-----------|-------------|-----------------|--------|--------------|----------------|
| 1 | PLA2G6-associated neurodegeneration | 99.76% | L5 | 0 | 0 | Hold |
| 2 | Rasmussen subacute encephalitis | 99.73% | L5 | 0 | 0 | Hold |
| 3 | Myelitis | 99.63% | L5 | 0 | 0 | Hold |
| **4** | **Paralysis agitans, juvenile, of Hunt** | **99.60%** | **L4** | 0 | 0 | **Research Question** |
| 5 | Transaldolase deficiency | 99.43% | L5 | 0 | 0 | Hold |
| 6 | Lethal infantile mitochondrial myopathy | 99.28% | L5 | 0 | 0 | Hold |
| **7** | **Lewy body dementia** | **99.25%** | **L4** | 1 | 3 | **Research Question** |
| 8 | Fructose-1,6-bisphosphatase deficiency | 99.22% | L5 | 0 | 0 | Hold |
| 9 | Polymicrogyria périsylvienne avec hypoplasie cérébelleuse | 99.06% | L5 | 0 | 0 | Hold |
| 10 | Progressive supranuclear palsy-CBS | 99.04% | L5 | 1 | 0 | Hold |

### Indications Prioritaires à Investiguer

**Rang 4 — Paralysis agitans juvenile de Hunt (parkinsonisme juvénile)**
Le parkinsonisme juvénile partage une pathophysiologie dopaminergique quasi identique à la maladie de Parkinson de l'adulte. L'inhibition de la COMT par Entacapone pour potentialiser la lévodopa y dispose d'une base théorique solide et directement transposable depuis l'indication approuvée. Limite principale : absence de données PK/PD et de sécurité à long terme dans la population pédiatrique.

**Rang 7 — Lewy body dementia (démence à corps de Lewy)**
Deux voies mécanistiques plausibles : (1) augmentation de la disponibilité striatale de la dopamine via inhibition COMT → amélioration des symptômes moteurs et cognitifs ; (2) données in vitro (PMID 23913715) suggérant une influence des agents antiparkinsoniens sur la formation d'oligomères α-synuclein/β-amyloïde. L'essai NCT04246437 ([18F]F-DOPA) constitue un outil de validation biomarqueur du déficit dopaminergique dans la DLB, sans évaluer Entacapone directement.

| Essai | Phase | Statut | Participants | Résumé |
|-------|-------|--------|-------------|--------|
| [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) | Phase 1 | En recrutement | 40 | Imagerie [18F]F-DOPA dans les alpha-synucléinopathies (PD, MSA, DLB) — étude de biomarqueur dopaminergique, pas d'intervention Entacapone |

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-------|------|-------|---------------------|
| [23913715](https://pubmed.ncbi.nlm.nih.gov/23913715/) | 2013 | In vitro | J Neurosci Res | Les agents antiparkinsoniens (incluant des composés de la classe COMT) peuvent influencer la formation d'oligomères β-amyloïde et α-synuclein |
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | Modèle iPSC | Science Advances | Modèle organoides corticaux SNCA triplication reproduisant la pathologie α-synuclein dans la DLB — identification de candidats thérapeutiques |
| [11268898](https://pubmed.ncbi.nlm.nih.gov/11268898/) | 2001 | Revue | Presse Médicale | Revue de la maladie de Parkinson — contexte mécanistique dopaminergique |

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction TxGNN pour PLAN (rang 1) repose uniquement sur le modèle (L5), sans données précliniques ni cliniques à l'appui. Le lien mécanistique entre l'inhibition de la COMT et la pathophysiologie de PLA2G6 est indirect, non étayé, et peu plausible biologiquement. Sur l'ensemble du top 10, deux indications (rangs 4 et 7) présentent un ancrage mécanistique suffisant pour justifier une investigation plus poussée avant tout engagement clinique.

**Pour avancer, les éléments suivants sont nécessaires :**

- **[Bloquant — DG001]** Obtention des données de sécurité officielles (notice/RCP) : contre-indications, mises en garde, interactions médicamenteuses
- **[Prioritaire — DG002]** Récupération du mécanisme d'action complet via DrugBank API (DB00494)
- Recherche de littérature préclinique sur l'axe COMT/dopamine dans les modèles PLAN (PLA2G6 KO, modèles NBIA)
- Évaluation approfondie en parallèle des indications **rang 4** (Paralysis agitans juvenile) et **rang 7** (Lewy body dementia) — candidates prioritaires avec meilleur niveau de preuve mécanistique
- Pour rang 7 (LBD) : préciser le risque d'aggravation des hallucinations lors d'une utilisation conjointe avec la lévodopa dans cette population particulièrement sensible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

