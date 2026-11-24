---
layout: default
title: Vortioxetine
parent: Prédiction du modèle uniquement (L5)
nav_order: 821
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "vortioxetine"
predicted_indications: ["neurotic disorder", "benign paroxysmal torticollis of infancy"]
description: "Vortioxetine : nouvelle indication prédite, Trouble névrotique (neurotic disorder) (niveau de preuve L5). En France, AMM dans la BDPM : 4 (valides : 4)"
---

# Vortioxetine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Vortioxetine: Trouble névrotique (neurotic disorder)
{: .text-alpha }

## Résumé en Une Phrase

La vortioxétine est un antidépresseur à action sérotoninergique multimodale, commercialisé en France sous le nom BRINTELLIX.
Le modèle TxGNN prédit qu'elle pourrait être utile dans le **trouble névrotique (neurotic disorder)**, avec un score de 0,9924.
Aucun essai clinique n'est enregistré et **1 publication** (un article de revue sur la dépression névrotique) est associée ; aucune étude ne teste directement la vortioxétine dans cette maladie, le niveau de preuve est donc **L5**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Trouble névrotique (neurotic disorder) |
| Score de Prédiction TxGNN | 0.9924 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Vortioxetine (traduction non officielle) : « Le mécanisme de l'effet antidépresseur de la vortioxétine n'est pas entièrement élucidé, mais on pense qu'il est lié à son renforcement de l'activité sérotoninergique dans le SNC par l'inhibition de la recapture de la sérotonine (5-HT). Elle possède également plusieurs autres activités, notamment un antagonisme des récepteurs 5-HT3 et un agonisme des récepteurs 5-HT1A. » Texte original en anglais : "The mechanism of the antidepressant effect of vortioxetine is not fully understood, but is thought to be related to its enhancement of serotonergic activity in the CNS through inhibition of the reuptake of serotonin (5-HT). It also has several other activities including 5-HT3 receptor antagonism and 5-HT1A receptor agonism." ([DailyMed: Trintellix (vortioxetine) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bd0107e5-1cb9-4b40-a6af-fa65fcbe6b4e), version du 2026-04-23 ; consulté le 2026-11-19). D'après les informations générales, la vortioxétine inhibe le transporteur de la sérotonine (SERT) et module plusieurs récepteurs sérotoninergiques (5-HT), ce qui en fait un antidépresseur à action multimodale.

Le « trouble névrotique » est une catégorie diagnostique ancienne et large, qui recouvre en partie les troubles dépressifs et anxieux. Le score élevé du modèle reflète probablement ce chevauchement nosologique plutôt qu'un mécanisme réellement nouveau. L'activité sérotoninergique de la vortioxétine pourrait être pertinente pour les composantes dépressive et anxieuse de ce type de tableau, mais il s'agit d'une hypothèse et non d'une démonstration.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Revue | Zhurnal nevrologii i psikhiatrii imeni S.S. Korsakova | Présentation d'un cas de dépression névrotique ; les auteurs soulignent l'intérêt d'une prise en charge associant antidépresseurs et psychothérapie (thérapie cognitivo-comportementale). Cet article ne teste pas la vortioxétine. |

## Informations de Marché en France

La vortioxétine est commercialisée en France. Les données compilées recensent 4 AMM valides, toutes pour des formes de comprimé pelliculé (laboratoire Lundbeck, Danemark).

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 60316362 | BRINTELLIX 20 mg, comprimé pelliculé | Comprimé pelliculé | LUNDBECK (DANEMARK) | Active |
| 61439909 | BRINTELLIX 15 mg, comprimé pelliculé | Comprimé pelliculé | LUNDBECK (DANEMARK) | Active |
| 62792157 | BRINTELLIX 5 mg, comprimé pelliculé | Comprimé pelliculé | LUNDBECK (DANEMARK) | Active |
| 68562572 | BRINTELLIX 10 mg, comprimé pelliculé | Comprimé pelliculé | LUNDBECK (DANEMARK) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

**Interactions médicamenteuses** : 151 interactions sont recensées. Parmi celles listées, les interactions de niveau majeur concernent notamment :
- le bupropion
- la lorcasérine
- la diéthylpropione
- la dolasétron
- le palonosétron
- la phentermine

Des interactions de niveau modéré sont également signalées, notamment avec la morphine, l'acide acétylsalicylique, la dexaméthasone, les sulfamides hypoglycémiants (chlorpropamide, glimépiride) et plusieurs insulines.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Aucun essai clinique ni étude ne teste la vortioxétine dans le trouble névrotique ; la prédiction repose uniquement sur le modèle (niveau L5) et reflète vraisemblablement un chevauchement avec des catégories diagnostiques dépressives et anxieuses plutôt qu'une indication réellement nouvelle.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des données détaillées sur le mécanisme d'action
- Les mises en garde et contre-indications issues de la notice officielle
- Des études cliniques ciblant directement cette population
- Une définition diagnostique moderne de la population visée, la catégorie « trouble névrotique » étant ancienne

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Trintellix (vortioxetine) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bd0107e5-1cb9-4b40-a6af-fa65fcbe6b4e) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

