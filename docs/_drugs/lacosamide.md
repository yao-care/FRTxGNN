---
layout: default
title: Lacosamide
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Lacosamide
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

# Lacosamide : Des Crises Épileptiques Partielles au Trouble Affectif Bipolaire Maniaque

## Résumé en Une Phrase

Lacosamide est un antiépileptique de troisième génération (Vimpat®), initialement utilisé pour traiter les crises épileptiques partielles (focales).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Trouble Affectif Bipolaire Maniaque**,
avec **1 essai clinique** (Phase 3, en cours) et **11 publications** soutenant actuellement cette direction, le niveau de preuve restant préliminaire (L3).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Crises épileptiques partielles (épilepsie focale) |
| Nouvelle Indication Prédite | Trouble Affectif Bipolaire Maniaque |
| Score de Prédiction TxGNN | 99.96% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données officielles sur le mécanisme d'action (MOA) de la lacosamide ne sont pas disponibles dans notre base (lacune signalée, priorité haute). Sur la base des informations disponibles dans la littérature associée à cette prédiction, la lacosamide est un antiépileptique de troisième génération qui agit en favorisant sélectivement l'inactivation lente des canaux sodiques voltage-dépendants (Nav), un mécanisme distinct des antiépileptiques classiques qui bloquent l'inactivation rapide. Elle est commercialisée sous le nom de Vimpat® pour le traitement des crises épileptiques partielles (focales) chez l'adulte.

Le lien entre épilepsie et trouble bipolaire est bien documenté sur le plan clinique : plusieurs antiépileptiques (lamotrigine, carbamazépine, valproate) sont déjà utilisés comme stabilisateurs de l'humeur, en exploitant leur action sur l'excitabilité neuronale. Des études observationnelles incluses dans ce dossier (PMID 30251375, PMID 28845834) rapportent une amélioration des symptômes dépressifs et maniaques chez des patients épileptiques traités par lacosamide, ce qui a motivé l'hypothèse d'un effet stabilisateur de l'humeur indépendant du simple contrôle des crises.

Mécanistiquement, la stabilisation membranaire via les canaux Nav pourrait réduire l'hyperexcitabilité du système limbique impliquée dans les épisodes maniaques. Toutefois, contrairement aux stabilisateurs de l'humeur classiques, la lacosamide ne dispose pas de preuve directe d'action sur les systèmes GABAergique ou glutamatergique, ce qui rend le lien mécanistique modéré plutôt que fort.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Phase 3 | Recrutement en cours | 40 | Étude randomisée en double aveugle évaluant la lacosamide en add-on dans les épisodes dépressifs majeurs du trouble bipolaire de type I et II ; conception directement pertinente mais aucun résultat disponible à ce jour (achèvement prévu 2027-01) |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Cohorte (contrôle rétrospectif) | Psychiatry Clin Neurosci | Évaluation sur 30 jours de la lacosamide chez des patients bipolaires sans épilepsie, comparée à un groupe contrôle rétrospectif traité par d'autres antiépileptiques |
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Essai pilote ouvert | J Clin Psychopharmacol | Essai pilote ouvert de 12 semaines évaluant l'efficacité et la sécurité de la lacosamide dans la dépression bipolaire |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Cas clinique | Acta Biomed | Stabilisation clinique de l'humeur sous lacosamide chez un patient avec trouble de l'humeur comorbide à un TSPT et une épilepsie fronto-temporale |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Cas clinique | Indian J Psychol Med | Neutropénie précipitée par la lacosamide chez un patient bipolaire avec épilepsie comorbide — signal de sécurité à surveiller |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | Cas clinique | Cureus | Prise en charge complexe d'une patiente bipolaire enceinte avec comorbidités multiples incluant épilepsie/crises non épileptiques psychogènes |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Revue | Ther Drug Monit | Mise à jour 2018 sur le suivi thérapeutique des antiépileptiques, incluant leur usage élargi dans le trouble bipolaire |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Revue | ACS Chem Neurosci | Revue sur la « druggabilité » de CRMP2, cible moléculaire impliquée dans l'action de la lacosamide |
| [37782796](https://pubmed.ncbi.nlm.nih.gov/37782796/) | 2023 | Étude structurale | PNAS | Structures cryo-EM démontrant l'inhibition à double poche des canaux Nav par la lamotrigine, éclairant la pharmacologie de classe |
| [22210279](https://pubmed.ncbi.nlm.nih.gov/22210279/) | 2012 | Revue | Adv Drug Deliv Rev | Propriétés chimiques des antiépileptiques approuvés entre 1990 et 2011, incluant la lacosamide |
| [16732716](https://pubmed.ncbi.nlm.nih.gov/16732716/) | 2006 | Revue | Expert Opin Investig Drugs | Revue des antiépileptiques de seconde génération et de leurs avantages pharmacocinétiques |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité (aucune donnée officielle de mises en garde, contre-indications ou interactions médicamenteuses n'est disponible dans ce dossier). À noter toutefois qu'un cas de neutropénie sous lacosamide chez un patient bipolaire a été rapporté dans la littérature (PMID 30275630) et mérite une attention particulière en pharmacovigilance.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le niveau de preuve (L3) repose sur une cohorte rétrospective et un essai pilote ouvert prometteurs mais non confirmatoires ; le seul essai de Phase 3 pertinent (NCT07412132) est en cours de recrutement et n'a pas encore de résultats.
- Les données réglementaires et de sécurité (notice TFDA, MOA officiel) sont totalement absentes, ce qui empêche toute évaluation de sécurité initiale.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice / résumé des caractéristiques du produit (lacune bloquante)
- Compléter les données MOA officielles via DrugBank
- Attendre les résultats de l'essai NCT07412132 (achèvement prévu 2027-01)
- Intégrer le signal de neutropénie rapporté (PMID 30275630) dans un plan de surveillance hématologique
- Évaluer la faisabilité réglementaire, le médicament n'étant actuellement pas commercialisé en France (0 AMM)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

