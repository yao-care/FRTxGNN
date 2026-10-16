---
layout: default
title: Serotonin
parent: Preuves modérées (L3-L4)
nav_order: 700
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Serotonin : nouvelle indication prédite, Insomnie (niveau de preuve L4). Indication d'origine : Non renseignée (le texte d'indication de l'AMM est vide)"
---

# Serotonin
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Sérotonine : D'une préparation homéopathique (indication non renseignée) à l'insomnie

## Résumé en Une Phrase

La sérotonine (préparation homéopathique SEROTONINUM BOIRON, granules) ne dispose d'aucune indication officielle renseignée dans les données compilées pour ce rapport, et son unique AMM française est annulée.
Le modèle TxGNN prédit qu'elle pourrait être utile dans l'**insomnie**, mais aucun des essais cliniques retrouvés ne teste la sérotonine elle-même et aucune publication n'a été retrouvée pour cette indication.
Le niveau de preuve est donc très faible (**L4**) : la prédiction repose sur un raisonnement mécanistique indirect, et la décision recommandée est **Hold**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée (le texte d'indication de l'AMM est vide) |
| Nouvelle Indication Prédite | Insomnie |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. La sérotonine (5-HT) est un neurotransmetteur impliqué dans la régulation de l'humeur, de l'anxiété et du cycle veille-sommeil. Elle est aussi un précurseur de la mélatonine. Le produit référencé en France est une préparation homéopathique diluée (3CH à 30CH ou 6DH à 60DH), sans indication documentée.

Sur le plan biologique, un lien existe : la sérotonine intervient dans les circuits veille-sommeil (noyau du raphé dorsal) et la voie de la mélatonine. Toutefois, la sérotonine administrée par voie exogène ne franchit pas la barrière hémato-encéphalique et n'a pas d'usage thérapeutique établi comme hypnotique. Le score TxGNN élevé reflète donc surtout la proximité de la sérotonine avec cette voie biologique, et non une démonstration d'efficacité.

Les autres prédictions du modèle vont dans le même sens : les troubles anxieux (rang 2), la migraine (rang 3) et l'agoraphobie (rang 5) sont des pathologies où les médicaments agissant sur le système sérotoninergique (ISRS, IRSN, triptans) sont établis. Le modèle capte donc l'implication du système sérotoninergique, qui ne se traduit pas en bénéfice pour la sérotonine elle-même. Pour le trouble bipolaire maniaque (rang 9), les données suggèrent plutôt un risque (virage maniaque sous médicaments sérotoninergiques).

## Preuves d'Essais Cliniques

Deux essais sont associés à l'insomnie. Aucun ne teste la sérotonine (pertinence jugée faible).

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT06559306](https://clinicaltrials.gov/study/NCT06559306) | Phase 3 | En recrutement | 752 | Séltorexant 20 mg en traitement adjuvant des antidépresseurs dans la dépression majeure avec symptômes d'insomnie. Autre agent expérimental, pas de la sérotonine ; pas de résultats disponibles |
| [NCT05705830](https://clinicaltrials.gov/study/NCT05705830) | Non applicable | Inconnu | 400 | Magnétothérapie pulsée associée à un traitement médicamenteux dans l'anxiété avec insomnie. Intervention non médicamenteuse, sans lien avec la sérotonine |

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'insomnie.

À titre de contexte, des publications existent pour d'autres indications prédites (troubles anxieux, migraine), mais elles portent sur des médicaments modulant la sérotonine (ISRS, IRSN, triptans) ou sur la physiopathologie, et non sur la sérotonine exogène.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63553427 | SEROTONINUM BOIRON, degré de dilution compris entre 3CH et 30CH ou entre 6DH et 60DH | Granules | Non renseignée (AMM annulée) |

## Considérations de Sécurité

Les données de sécurité issues de la notice (mises en garde, contre-indications) ne sont pas disponibles, et aucune interaction médicamenteuse n'a été retrouvée dans les bases interrogées. Veuillez consulter la notice pour les informations de sécurité.

À titre indicatif, les éléments de la littérature compilée soulignent que la sérotonine exogène est non sélective et possède des effets périphériques (notamment vasoconstricteurs). Les médicaments sérotoninergiques peuvent aussi provoquer un syndrome sérotoninergique et un virage maniaque chez les patients bipolaires.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle et un raisonnement mécanistique indirect. Aucun essai ne teste la sérotonine, aucune publication n'a été retrouvée pour l'insomnie, et l'unique AMM est annulée.
- La sérotonine exogène ne franchit pas la barrière hémato-encéphalique, ce qui limite fortement sa plausibilité comme hypnotique. Les données de sécurité de la notice sont également absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle auprès de l'ANSM (mises en garde et contre-indications), préalable indispensable à toute évaluation de sécurité.
- Obtenir les données sur le mécanisme d'action (par exemple via DrugBank).
- Examiner s'il serait plus pertinent d'évaluer des précurseurs ou des agents agissant sur la voie sérotonine-mélatonine, plutôt que la sérotonine elle-même.
- Documenter des études précliniques ou cliniques directes de la sérotonine dans l'insomnie, ainsi que la faisabilité d'une voie d'administration adaptée (compatibilité de voie non évaluée à ce stade).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

