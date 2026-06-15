---
layout: default
title: Clonidine
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Clonidine
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

# Clonidine : De l'Hypertension Artérielle au Syndrome de Tourette

## Résumé en Une Phrase

Clonidine est un agoniste des récepteurs α2-adrénergiques centraux, initialement utilisé pour le traitement de l'hypertension artérielle grâce à ses effets sympatholytiques centraux.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Syndrome de Tourette**,
avec **3 essais cliniques** et **19 publications** soutenant actuellement cette direction — dont des lignes directrices européennes et des ECR multicentriques publiés en 2024.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle |
| Nouvelle Indication Prédite | Syndrome de Tourette |
| Score de Prédiction TxGNN | 99.98% |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé (0 AMM dans les données réglementaires) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de Clonidine ne sont pas disponibles dans le pack de données actuel. Sur la base des informations connues, Clonidine est un agoniste des récepteurs α2-adrénergiques centraux appartenant à la classe des antihypertenseurs à action centrale. Son efficacité dans le traitement de l'hypertension artérielle est établie de longue date, et ce même mécanisme de modulation du système noradrénergique constitue le fondement biologique de son repositionnement vers le Syndrome de Tourette.

Le Syndrome de Tourette est caractérisé par une suractivation du locus coeruleus entraînant un dérèglement du circuit striato-thalamo-cortical, se manifestant par des tics moteurs et vocaux involontaires. En inhibant la libération de noradrénaline (NE) via les récepteurs α2A pré-synaptiques, Clonidine réduit l'excitabilité corticale et atténue ce circuit pathologique — un mécanisme directement pertinent à la physiopathologie du trouble. Un modèle animal publié en 2025 (PMID 40392363) a en outre confirmé que Clonidine peut inhiber la neuro-inflammation dans le cerveau de rats atteints du Syndrome de Tourette, élargissant ainsi la compréhension de ses effets bénéfiques au-delà de la simple modulation noradrénergique.

Sur le plan clinique, les lignes directrices européennes de la Société d'Étude du Syndrome de Tourette (ESSTS, version 2.0, 2022 — PMID 34757514) classent déjà Clonidine comme une **option de première ligne** dans la prise en charge pharmacologique du Syndrome de Tourette. Cette reconnaissance par les guidelines valide rétrospectivement la prédiction du modèle TxGNN et souligne la robustesse de la base de preuves accumulée depuis la première publication clinique de Cohen et al. en 1979 (PMID 89558).

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00370838](https://clinicaltrials.gov/study/NCT00370838) | Phase 4 | Terminé | 12 | Essai croisé randomisé en double aveugle comparant Clonidine vs Levetiracetam pour la suppression des tics dans le Syndrome de Tourette chez l'enfant — Clonidine utilisé comme traitement de référence établi |
| [NCT00152750](https://clinicaltrials.gov/study/NCT00152750) | Phase 4 | Inconnu | 32 | Évaluation de Clonidine sur l'agressivité diurne chez les enfants atteints de Syndrome de Tourette avec ADHD comorbide, via l'amélioration de la qualité du sommeil nocturne |
| [NCT01172288](https://clinicaltrials.gov/study/NCT01172288) | Phase 2 | Terminé | 31 | Essai contrôlé de la N-acétylcystéine pour les tics ; Clonidine cité comme traitement pharmacologique de référence actuel pour les tics dans le Syndrome de Tourette |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39258554](https://pubmed.ncbi.nlm.nih.gov/39258554/) | 2024 | ECR | Clinical Neuropharmacology | ECR randomisé, double-aveugle, multicentrique évaluant l'efficacité du patch adhésif de Clonidine dans le Syndrome de Tourette — résultats positifs sur la réduction des tics |
| [36528030](https://pubmed.ncbi.nlm.nih.gov/36528030/) | 2023 | Méta-analyse en réseau | The Lancet. Child & Adolescent Health | Comparaison de l'efficacité, tolérance et acceptabilité des traitements pharmacologiques pour le Syndrome de Tourette chez l'enfant et l'adolescent — Clonidine inclus dans l'analyse comparative |
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Lignes directrices | European Child & Adolescent Psychiatry | Lignes directrices européennes ESSTS v2.0 pour le traitement pharmacologique du Syndrome de Tourette — Clonidine classé comme option de première ligne |
| [31061209](https://pubmed.ncbi.nlm.nih.gov/31061209/) | 2019 | Revue systématique | Neurology | Revue systématique complète sur les traitements des tics dans le Syndrome de Tourette et les troubles tics chroniques, évaluant l'efficacité et les risques de Clonidine |
| [38695046](https://pubmed.ncbi.nlm.nih.gov/38695046/) | 2024 | Étude clinique | Psychiatry Investigation | Évaluation de l'efficacité et de la sécurité du patch adhésif de Clonidine chez les patients atteints de Syndrome de Tourette avec ADHD comorbide |
| [40392363](https://pubmed.ncbi.nlm.nih.gov/40392363/) | 2025 | Étude animale | Journal of Neuroimmune Pharmacology | Clonidine atténue la neuro-inflammation dans un modèle rat du Syndrome de Tourette, suggérant un mécanisme anti-inflammatoire au-delà de la modulation adrénergique |
| [34286606](https://pubmed.ncbi.nlm.nih.gov/34286606/) | 2021 | Revue systématique | Journal of Psychopharmacology | Évaluation de la qualité des preuves du traitement pharmacologique du Syndrome de Tourette chez l'enfant et l'adulte |
| [23473832](https://pubmed.ncbi.nlm.nih.gov/23473832/) | 2013 | Revue | European Journal of Paediatric Neurology | Revue des options pharmacologiques actuelles pour le Syndrome de Tourette avec ADHD comorbide — Clonidine comme option reconnue |
| [1414629](https://pubmed.ncbi.nlm.nih.gov/1414629/) | 1992 | Essai clinique | Advances in Neurology | Étude clinique sur Clonidine et Clonazepam dans le Syndrome de Tourette |
| [89558](https://pubmed.ncbi.nlm.nih.gov/89558/) | 1979 | Étude clinique | Lancet | Rapport fondateur démontrant l'efficacité de Clonidine dans le Syndrome de Tourette chez des enfants non répondeurs à l'halopéridol, établissant la base de l'hypothèse noradrénergique |

---

## Informations de Marché en France

Aucune AMM enregistrée dans les données réglementaires disponibles pour Clonidine en France (statut : non commercialisé selon la requête).

> **Note importante :** Cette information reflète l'état des données de la requête réglementaire au moment de l'analyse (2026-06-07). Clonidine est historiquement commercialisé dans plusieurs pays européens sous des noms tels que **Catapressan®** (antihypertenseur) et **Kapvay®** (ADHD, FDA approuvé). Il est impératif de vérifier le statut actuel auprès de l'**ANSM** avant toute démarche de développement clinique ou de remboursement en France.

---

## Considérations de Sécurité

Les données spécifiques de sécurité (mises en garde, contre-indications, interactions médicamenteuses) n'ont pas pu être récupérées lors de la requête TFDA et ne sont pas disponibles dans le pack actuel.

> Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Les lignes directrices européennes (ESSTS 2022), une méta-analyse en réseau publiée dans *The Lancet* (2023), et un ECR multicentrique récent (2024) confirment collectivement l'efficacité de Clonidine dans le Syndrome de Tourette. Le niveau de preuve L1 et le statut de première ligne dans les guidelines internationales soutiennent une progression encadrée, sous réserve de clarification du statut réglementaire en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Vérification du statut d'AMM auprès de l'ANSM (présence possible sous Catapressan® ou autre dénomination commerciale)
- Données complètes sur le mécanisme d'action (MOA) à obtenir via DrugBank API (DG002)
- Mises en garde, contre-indications et profil d'interactions médicamenteuses à extraire de la notice TFDA (DG001 — bloquant)
- Plan de surveillance de sécurité adapté aux populations pédiatriques, principale population cible dans le Syndrome de Tourette
- Évaluation des formulations disponibles (comprimé oral, patch transdermique) pour adéquation thérapeutique selon l'âge et le contexte clinique
- Analyse comparative avec les traitements de référence actuellement remboursés en France (antipsychotiques atypiques, guanfacine)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

