---
layout: default
title: Sorbitol
parent: Prédiction du modèle uniquement (L5)
nav_order: 286
evidence_level: L5
indication_count: 1
---

# Sorbitol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Sorbitol : Du laxatif osmotique à l'hyperthermie maligne d'effort

## Résumé en Une Phrase

Le sorbitol est un polyol (alcool de sucre) utilisé comme laxatif osmotique, édulcorant, excipient et solution d'irrigation. Aucune indication officielle n'est renseignée dans les données réglementaires françaises disponibles.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hyperthermie maligne d'effort**, avec un score élevé (99,40 %), mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Hyperthermie maligne d'effort (exercise-induced malignant hyperthermia) |
| Score de Prédiction TxGNN | 99,40 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Le sorbitol est connu comme un alcool de sucre à effet osmotique, utilisé comme laxatif, édulcorant, excipient et solution d'irrigation.

L'hyperthermie maligne et les coups de chaleur d'effort reposent sur une libération dérégulée du calcium dans le muscle squelettique, typiquement liée à des variants des gènes *RYR1* ou *CACNA1S*. Leur prise en charge repose sur le dantrolène, le refroidissement et les soins de support. Le sorbitol n'a aucune action connue sur cette voie.

**Aucun lien mécanistique crédible n'a été identifié.** Le score élevé de TxGNN (0,994) est une prédiction issue d'un graphe de connaissances. Elle pourrait provenir de voisins partagés de type polyol, comme le mannitol, présent dans certaines formulations de dantrolène. Ce score ne doit pas être interprété comme un soutien biologique. Sans hypothèse mécanistique, la prédiction ne peut pas être priorisée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 67851645 | SORBITOL DELALANDE 5 g, poudre pour solution buvable en sachet-dose | Poudre pour solution buvable | ZENTIVA FRANCE |
| 64714196 | SORBITOL H2 PHARMA 5 g, poudre pour solution buvable en sachet | Poudre pour solution buvable | H2 PHARMA |
| 67939789 | HEPARGITOL, poudre orale en sachet bipoche | Poudre et poudre | ELERTE |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible avec la physiopathologie de l'hyperthermie maligne. Les données de sécurité issues de la notice ANSM sont également manquantes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le dépistage de sécurité)
- Obtenir les données de mécanisme d'action depuis DrugBank
- Identifier une hypothèse mécanistique plausible reliant le sorbitol à la dérégulation calcique musculaire, ou vérifier si la prédiction provient d'un artefact de voisinage (mannitol, polyols)
- Rechercher dans la littérature et les registres d'essais toute donnée directe sur le sorbitol dans cette indication
- Compléter les indications approuvées des trois AMM pour clarifier l'indication d'origine

*Ces résultats sont fournis à titre de référence pour la recherche et ne constituent pas un avis médical. Tout candidat au repositionnement doit faire l'objet d'une validation clinique avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

