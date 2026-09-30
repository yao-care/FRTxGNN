---
layout: default
title: Pilocarpine
parent: Prédiction du modèle uniquement (L5)
nav_order: 237
evidence_level: L5
indication_count: 1
---

# Pilocarpine
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

# Pilocarpine : D'une Indication Originale Non Renseignée au Glaucome Héréditaire Primaire

## Résumé en Une Phrase

La pilocarpine est un agoniste muscarinique, commercialisé en France sous forme de collyre (Isopto Pilocarpine 2 %). Son indication originale n'est pas renseignée dans les données disponibles.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **glaucome héréditaire primaire**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée (le texte d'indication de l'AMM est vide) |
| Nouvelle Indication Prédite | Glaucome héréditaire primaire |
| Score de Prédiction TxGNN | 99,83 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après la pharmacologie générale, la pilocarpine est un agoniste muscarinique (principalement du récepteur M3). Elle contracte le muscle ciliaire et provoque un myosis. Cela élargit la voie d'écoulement de l'humeur aqueuse par le trabéculum et fait baisser la pression intraoculaire. Ce mécanisme est plausible pour le glaucome en général.

Cette explication vient de la pharmacologie générale et non des données fournies. La pilocarpine est déjà un myotique topique établi pour d'autres types de glaucome. Le score élevé de 0,998 pourrait donc refléter en partie cet usage connu plutôt qu'une découverte nouvelle.

L'adéquation mécanistique à ce sous-type est incertaine. Le glaucome héréditaire primaire (congénital) résulte d'anomalies du développement du trabéculum et de l'angle iridocornéen. Sa prise en charge est généralement chirurgicale, et les myotiques ne constituent pas un traitement de première intention.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66997501 | ISOPTO PILOCARPINE 2 POUR CENT, collyre (NOVARTIS PHARMA) | Collyre en solution | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Les données de sécurité de la notice ANSM manquent, ce qui empêche le passage à l'étape de dépistage de sécurité. La pertinence mécanistique pour le glaucome héréditaire primaire reste incertaine, car la prise en charge y est surtout chirurgicale.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde et contre-indications)
- Compléter les données sur le mécanisme d'action (par exemple via l'API DrugBank)
- Rechercher la littérature et les essais sur les myotiques dans le glaucome congénital, et vérifier si le score reflète un usage déjà établi dans d'autres glaucomes
- Confirmer l'indication approuvée de l'AMM 66997501
- Évaluer la compatibilité de la voie d'administration (collyre) et son utilisation en population pédiatrique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

