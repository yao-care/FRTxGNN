---
layout: default
title: Ebastine
parent: Prédiction du modèle uniquement (L5)
nav_order: 267
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Ebastine : nouvelle indication prédite, Maladie coronarienne (coronary artery disease) (niveau de preuve L5). Indication d'origine : Rhinite allergique, rhinite vasomotrice, urticaire idiopathique"
monitor_inn: "ebastine"
predicted_indications: ["coronary artery disease", "myocardial ischemia"]
---

# Ebastine
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

# Ebastine : De la rhinite allergique à la maladie coronarienne

## Résumé en Une Phrase

Ebastine est un antihistaminique H1 de deuxième génération, initialement utilisé pour le traitement de la rhinite allergique, de la rhinite vasomotrice et de l'urticaire idiopathique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie coronarienne** (et, de façon corrélée, l'**ischémie myocardique**).
Aucun essai clinique ni aucune publication ne soutient actuellement cette direction : la prédiction repose uniquement sur le score du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Rhinite allergique, rhinite vasomotrice, urticaire idiopathique (issues du graphe de connaissances, le texte d'indication des AMM étant vide) |
| Nouvelle Indication Prédite | Maladie coronarienne (coronary artery disease) |
| Score de Prédiction TxGNN | 99,18 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (aucune AMM valide) |
| Nombre d'AMM | 16 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations générales connues, l'ebastine est un antihistaminique H1 de deuxième génération. Son efficacité dans les affections allergiques est établie, mais ce rapport ne dispose d'aucune donnée sur son mécanisme dans le domaine cardiovasculaire.

Un lien hypothétique, non vérifié, pourrait être le rôle de l'histamine et des mastocytes dans le vasospasme coronarien, l'inflammation de l'athérosclérose et les lésions d'ischémie-reperfusion, que le blocage des récepteurs H1 pourrait moduler. Ce raisonnement est spéculatif et n'est étayé par aucune des données compilées pour ce rapport.

La seconde prédiction, l'**ischémie myocardique** (score de 99,10 %), est très proche de la première. Les deux résultats proviennent probablement du même voisinage dans le graphe et ne constituent pas des signaux indépendants. Par ailleurs, l'ebastine et son métabolite actif, la carébastine, sont associés à des préoccupations d'allongement de l'intervalle QT à forte exposition, ce qui appelle à la prudence dans une population cardiaque.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 16 AMM recensées sont toutes annulées ; aucune n'est valide. Le texte des indications approuvées n'est pas renseigné. Les 5 premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 62338553 | EBASTINE ARROW 10 mg | Comprimé pelliculé | Annulée |
| 64894972 | EBASTINE BIOGARAN 10 mg | Comprimé orodispersible | Annulée |
| 69272860 | EBASTINE ZENTIVA 10 mg | Comprimé pelliculé | Annulée |
| 63385125 | EBASTINE ARROW LAB 10 mg | Comprimé orodispersible | Annulée |
| 61147189 | EBASTINE CRISTERS 10 mg | Comprimé orodispersible | Annulée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Point d'attention lié à la nouvelle indication : l'allongement possible de l'intervalle QT à forte exposition (ebastine et carébastine) constitue une considération de sécurité cardiovasculaire importante pour une population atteinte de maladie coronarienne. La recherche d'interactions médicamenteuses n'a retourné aucun résultat.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle TxGNN (niveau L5), sans essai clinique ni publication. Les deux indications cardiovasculaires prédites sont probablement corrélées, et le risque d'allongement du QT plaide pour la prudence. Toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (consultation de DrugBank) et analyse du lien mécanistique avec la pathologie coronarienne
- Notice officielle de l'ANSM (mises en garde et contre-indications), indispensable avant toute évaluation de sécurité
- Revue de la littérature préclinique et clinique sur l'histamine, les mastocytes et la maladie coronarienne
- Évaluation de la sécurité cardiaque (QT) de l'ebastine et de la carébastine
- Clarification du statut réglementaire en France, toutes les AMM étant annulées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

