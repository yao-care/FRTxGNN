---
layout: default
title: Alfacalcidol
parent: Prédiction du modèle uniquement (L5)
nav_order: 34
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Alfacalcidol : nouvelle indication prédite, Hypoparathyroïdie isolée familiale due à un défaut de sécrétion de la… (niveau de preuve L5). Indication d'origine : Hyperparathyroïdie"
monitor_inn: "ALFACALCIDOL"
predicted_indications: ["familial isolated hypoparathyroidism due to impaired PTH secretion", "Dahlberg-Borer-Newcomer syndrome", "craniofacial conodysplasia", "acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis"]
---

# Alfacalcidol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Alfacalcidol : De l'hyperparathyroïdie à l'hypoparathyroïdie isolée familiale par défaut de sécrétion de la PTH

## Résumé en Une Phrase

Alfacalcidol est un analogue de la vitamine D (1-alpha-hydroxylé), initialement utilisé dans l'hyperparathyroïdie, l'ostéite fibreuse, l'hypoparathyroïdie et l'ostéodystrophie rénale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypoparathyroïdie isolée familiale due à un défaut de sécrétion de la PTH**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction précise.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hyperparathyroïdie (indication issue du graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Hypoparathyroïdie isolée familiale due à un défaut de sécrétion de la PTH |
| Score de Prédiction TxGNN | 99,61 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées |
| Nombre d'AMM | 10 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'alfacalcidol est un analogue de la vitamine D déjà hydroxylé en position 1-alpha. Il contourne donc l'étape de la 1-alpha-hydroxylase rénale et n'a pas besoin de la stimulation par la PTH pour devenir actif. Il peut ainsi augmenter la calcémie dans les situations de carence en PTH.

L'hypoparathyroïdie fait déjà partie des indications d'origine du médicament dans le graphe de connaissances. La forme prédite ici est un sous-type génétique de cette indication. Le score élevé du modèle (0,996) reflète probablement cette proximité plutôt qu'un véritable nouveau signal de repositionnement.

Aucun essai ni publication n'a été fourni pour ce sous-type précis. La plausibilité biologique est bonne, mais elle n'est pas démontrée directement.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour cette indication.

Pour information, les autres indications prédites (rang 2 à 5) sont brièvement résumées ci-dessous :

| Indication prédite | Score TxGNN | Niveau de preuve | Observation |
|------|------|------|------|
| Syndrome de Dahlberg-Borer-Newcomer | 99,60 % | L5 | 20 publications récupérées, mais surtout indirectes (hypophosphatémie liée au FGF23) ou sans rapport ; correspondance du nom de la maladie à vérifier |
| Conodysplasie craniofaciale | 99,55 % | L5 | Aucune donnée ; aucun lien mécanistique identifiable |
| Dysplasie acromésomélique, type Campailla-Martinelli | 99,53 % | L5 | Aucune donnée ; aucun lien mécanistique clair |
| Acidose tubulaire rénale | 99,27 % | L4 | 5 cas cliniques d'ostéomalacie secondaire (plusieurs liés au syndrome de Sjögren) améliorée sous traitement incluant de la vitamine D active ; le bénéfice vise la complication osseuse, et les co-traitements (alcalinisants, phosphate) brouillent l'attribution |

## Informations de Marché en France

Les 10 AMM sont annulées ; aucune n'est actuellement valide. Le texte d'indication approuvée n'est pas renseigné dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 65401076 | UN-ALFA 0,10 microgramme, solution buvable en gouttes | Solution buvable en gouttes | Annulée |
| 68578562 | UN-ALFA 1 microgramme/0,5 ml, solution injectable IV en ampoule | Solution injectable | Annulée |
| 64661847 | ALFACALCIDOL THERAMEX 0,25 microgramme | Capsule molle | Annulée |
| 62092176 | UN ALFA 1 microgramme | Capsule | Annulée |
| 62626139 | ALFACALCIDOL THERAMEX 1 microgramme | Capsule molle | Annulée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

À titre d'observation tirée de la littérature : l'association de vitamine D active et de calcium dans l'hypoparathyroïdie post-thyroïdectomie peut exposer à une hypercalcémie et à un syndrome des buveurs de lait (calcium-alcalins). Une surveillance de la calcémie est donc essentielle.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai ni publication ne concerne ce sous-type. Le score élevé reflète surtout la proximité avec l'indication d'hypoparathyroïdie déjà connue.
- Toutes les AMM françaises sont annulées, et les données de sécurité issues de la notice sont absentes, ce qui bloque le passage à l'étape d'évaluation de la sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) sur le site de l'ANSM
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Rechercher des données cliniques ou des cas publiés spécifiques à l'hypoparathyroïdie familiale par défaut de sécrétion de la PTH
- Clarifier la disponibilité commerciale actuelle du produit en France, puisque toutes les AMM sont annulées
- Vérifier la correspondance du nom de maladie pour le syndrome de Dahlberg-Borer-Newcomer avant toute exploitation
- Si une piste secondaire est envisagée, l'acidose tubulaire rénale (niveau L4) pourrait être traitée comme une question de recherche, en distinguant l'effet sur l'atteinte osseuse de celui des co-traitements
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

