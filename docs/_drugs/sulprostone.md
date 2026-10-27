---
layout: default
title: Sulprostone
parent: Prédiction du modèle uniquement (L5)
nav_order: 724
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sulprostone : nouvelle indication prédite, Cataracte tétanique (tetanic cataract) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "SULPROSTONE"
predicted_indications: ["tetanic cataract", "diabetes mellitus type 2 associated cataract", "immature cataract", "craniostenosis cataract", "mature cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "diabetic cataract", "diabetic retinopathy"]
---

# Sulprostone
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Sulprostone : D'un utérotonique à la cataracte tétanique (prédiction du modèle uniquement)
{: .text-alpha }

## Résumé en Une Phrase

Sulprostone est un agoniste sélectif des récepteurs EP1/EP3 de la prostaglandine E2, dont l'indication d'origine n'est pas documentée dans les données compilées pour ce rapport (son autorisation française est aujourd'hui annulée).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **cataracte tétanique**, avec un score élevé mais **aucun essai clinique** et **aucune publication** à l'appui.
Cette prédiction repose donc uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Cataracte tétanique (tetanic cataract) |
| Score de Prédiction TxGNN | 99,86 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | AMM annulée uniquement |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le sulprostone est un agoniste des récepteurs EP1/EP3 de la prostaglandine E2, à activité utérotonique, sans historique de développement en ophtalmologie.

La cataracte tétanique est habituellement associée à l'hypocalcémie ou à l'hypoparathyroïdie. Aucun mécanisme documenté ne relie le sulprostone à cette affection, et le lien ne peut pas être évalué faute de données sur le mécanisme d'action d'origine.

Le même score (99,86 %) est attribué à plusieurs sous-types de cataracte. Cela suggère un signal du graphe commun à la classe « cataracte » plutôt qu'un mécanisme propre à la cataracte tétanique. La prédiction doit donc être interprétée avec une grande prudence.

**Autres indications prédites (toutes de niveau L5, sans essai ni publication, décision Hold) :**

| Rang | Indication prédite | Score TxGNN |
|------|------|------|
| 2 | Cataracte associée au diabète de type 2 | 99,86 % |
| 3 | Cataracte immature | 99,86 % |
| 4 | Cataracte avec craniosténose | 99,86 % |
| 5 | Cataracte mature | 99,86 % |
| 6 | Cataracte sénile nucléaire | 99,85 % |
| 7 | Cataracte corticale | 99,85 % |
| 8 | Cataracte sénile | 99,84 % |
| 9 | Cataracte diabétique | 99,82 % |
| 10 | Rétinopathie diabétique | 99,67 % |

Pour la rétinopathie diabétique, un rationnel biologique est concevable (la signalisation de la PGE2 via les récepteurs EP intervient dans l'inflammation rétinienne et la perméabilité vasculaire). Cependant, l'agonisme EP1/EP3 pourrait aggraver la pathologie plutôt que l'améliorer. Pour la cataracte sénile, les analogues de prostaglandines utilisés en ophtalmologie (glaucome, surtout via le récepteur FP) ne soutiennent pas cette indication et ont été associés à d'autres effets oculaires indésirables, comme l'œdème maculaire cystoïde.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61722693 | NALADOR 500 microgrammes (TEOFARMA), AMM annulée | Lyophilisat pour usage parentéral | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les données compilées ne contiennent aucune mise en garde, contre-indication ni interaction médicamenteuse exploitable.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, avec un lien mécanistique non plausible en l'état. Le produit n'est plus commercialisé en France (AMM annulée) et n'a aucun historique de développement ophtalmologique.
- L'absence de données de sécurité issues de la notice constitue un point bloquant pour toute évaluation ultérieure.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle de l'ANSM (mises en garde, contre-indications, indications d'origine).
- Obtenir les données sur le mécanisme d'action (par exemple via DrugBank) afin d'évaluer un lien mécanistique.
- Mener une revue de la littérature préclinique sur les récepteurs EP1/EP3 dans le cristallin et l'œil.
- Évaluer la compatibilité de la voie d'administration (parentérale actuellement, alors que les affections oculaires nécessiteraient probablement une voie locale).
- Prioriser éventuellement les indications oculaires où un rationnel biologique est plus plausible, tout en évaluant le risque d'aggravation.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

