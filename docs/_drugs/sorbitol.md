---
layout: default
title: Sorbitol
parent: Prédiction du modèle uniquement (L5)
nav_order: 710
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Sorbitol : nouvelle indication prédite, Hyperthermie maligne induite par l'effort (niveau de preuve L5). Indication d'origine : Non renseignée dans les AMM disponibles"
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

# Sorbitol : De l'indication originale non renseignée à l'hyperthermie maligne induite par l'effort

## Résumé en Une Phrase

Le sorbitol est un polyol (alcool de sucre) à action osmotique ; aucune indication d'origine n'est renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hyperthermie maligne induite par l'effort**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM disponibles |
| Nouvelle Indication Prédite | Hyperthermie maligne induite par l'effort |
| Score de Prédiction TxGNN | 99,40 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Le sorbitol est connu comme un alcool de sucre à effet osmotique, mais aucune indication d'origine n'est enregistrée, ce qui empêche de confronter la prédiction à la pharmacologie connue du produit.

L'hyperthermie maligne est un trouble de la régulation calcique du muscle squelettique (par exemple, dysfonction de RYR1), déclenché par les anesthésiques volatils ou la succinylcholine. Aucun lien mécanistique n'est étayé par les données disponibles entre l'action osmotique du sorbitol et cette physiopathologie ; toute relation resterait spéculative et nécessiterait une validation biologique indépendante.

Le score élevé (0,994) peut refléter une proximité dans le réseau de connaissances ou des voisins communs dans le graphe, plutôt qu'une véritable relation thérapeutique. Il ne doit pas être interprété comme une preuve clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67851645 | SORBITOL DELALANDE 5 g, poudre pour solution buvable en sachet-dose (ZENTIVA FRANCE) | Poudre pour solution buvable | Non renseignée |
| 64714196 | SORBITOL H2 PHARMA 5 g, poudre pour solution buvable en sachet (H2 PHARMA) | Poudre pour solution buvable | Non renseignée |
| 67939789 | HEPARGITOL, poudre orale en sachet bipoche (ELERTE) | Poudre et poudre | Non renseignée |

Les trois AMM sont au statut « annulée » : aucune autorisation valide n'est actuellement recensée.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie du graphe PrimeKG, et non texte de notice) : ulcère gastroduodénal actif.
- **Interactions Médicamenteuses** (2 interactions identifiées) :
  - **Tolévamer** : niveau **Majeur**
  - **Lamivudine** : niveau Modéré

Les mises en garde et contre-indications issues de la notice n'ont pas pu être exploitées ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique démontré. Par ailleurs, toutes les AMM françaises sont annulées et les données de sécurité issues de la notice font défaut.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice (mises en garde et contre-indications) auprès de l'ANSM, étape bloquante pour le criblage de sécurité
- Obtenir les données sur le mécanisme d'action (par exemple via DrugBank)
- Documenter l'indication d'origine du sorbitol
- Réaliser une revue de la littérature et des registres d'essais pour l'hyperthermie maligne
- Mener une validation biologique indépendante de tout lien avec la régulation calcique musculaire
- Évaluer la compatibilité des voies d'administration et la similarité avec l'indication d'origine (actuellement en attente)
- Clarifier la pertinence de la contre-indication « ulcère gastroduodénal actif » et de l'interaction majeure avec le tolévamer
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

