---
layout: default
title: Threonine
parent: Prédiction du modèle uniquement (L5)
nav_order: 755
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Threonine : nouvelle indication prédite, Gastroparésie (niveau de preuve L5). Indication d'origine : Non précisée dans les données compilées"
monitor_inn: "threonine"
predicted_indications: ["gastroparesis (disease)"]
---

# Threonine
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

# Thréonine : D'un acide aminé nutritionnel à la gastroparésie

## Résumé en Une Phrase

La thréonine est un acide aminé essentiel, présent dans des produits de nutrition (comprimés d'acides aminés, solutions de nutrition parentérale et de dialyse péritonéale) commercialisés en France.
Le modèle TxGNN prédit qu'elle pourrait être utile pour la **gastroparésie**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données compilées |
| Nouvelle Indication Prédite | Gastroparésie |
| Score de Prédiction TxGNN | 99,32 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées |
| Nombre d'AMM | 20 (0 valide, 20 annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. La thréonine est un acide aminé essentiel, utilisé comme composant de produits de nutrition entérale, parentérale et de dialyse péritonéale. Les données compilées ne renseignent aucune indication originale approuvée.

Aucun mécanisme reliant la thréonine à la motilité gastrique n'est documenté. Les voies physiopathologiques classiques de la gastroparésie (perte des cellules interstitielles de Cajal, dysfonction des neurones entériques, atteinte vagale) ne sont pas rattachées à ce médicament dans les données disponibles.

Toute hypothèse reste spéculative : la thréonine est abondante dans les mucines intestinales, et un soutien nutritionnel général pourrait être invoqué. Le score élevé reflète probablement une proximité dans le réseau de connaissances du modèle plutôt qu'une biologie causale démontrée. Cette prédiction doit donc être considérée comme une simple piste d'exploration.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 20 AMM recensées sont annulées. Les 5 principales sont listées ci-dessous (le texte d'indication n'est pas renseigné).

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 66534581 | KETOSTERIL, comprimé enrobé | Comprimé enrobé | Annulée |
| 61960303 | AMINOVEN 10 POUR CENT | Solution pour perfusion | Annulée |
| 69667989 | AMINOVEN 5 POUR CENT | Solution pour perfusion | Annulée |
| 62947013 | AMINOPLASMAL 25 | Solution pour perfusion | Annulée |
| 61786735 | AMINOMIX 500 | Solution et solution pour perfusion | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie du modèle, et non texte de notice) : phénylcétonurie et trouble du métabolisme de la phénylalanine.
- **Interactions médicamenteuses** : aucune interaction retrouvée dans la base interrogée.

Veuillez consulter la notice pour les autres informations de sécurité (mises en garde et contre-indications officielles).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La seule preuve est un score de prédiction élevé (niveau L5), sans essai clinique, sans publication ni mécanisme documenté. De plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde, contre-indications), actuellement manquante et bloquante pour le criblage de sécurité
- Obtenir les données sur le mécanisme d'action (DrugBank) et évaluer un lien plausible avec la motilité gastrique
- Réaliser une revue de la littérature préclinique et clinique sur la thréonine et la gastroparésie
- Clarifier l'indication originale et la compatibilité des voies d'administration pour cette nouvelle indication
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

