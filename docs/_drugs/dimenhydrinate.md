---
layout: default
title: Dimenhydrinate
parent: Prédiction du modèle uniquement (L5)
nav_order: 246
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Dimenhydrinate : nouvelle indication prédite, Urticaire allergique (niveau de preuve L5). Indication d'origine : Vertige d'origine centrale"
monitor_inn: "DIMENHYDRINATE"
predicted_indications: ["allergic urticaria", "cold urticaria"]
---

# Dimenhydrinate
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

## Dimenhydrinate : Du Vertige d'Origine Centrale à l'Urticaire Allergique
{: .text-alpha }

## Résumé en Une Phrase

Le dimenhydrinate est un sel de diphénhydramine (antihistaminique H1 de première génération) et de 8-chlorothéophylline, initialement utilisé contre le vertige d'origine centrale et le mal des transports.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**urticaire allergique**, mais aucun essai clinique n'est enregistré et une seule publication (une étude pharmacocinétique chez le chien, sans critère d'efficacité) est associée à cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Vertige d'origine centrale ; mal des transports (selon le graphe de connaissances, l'indication autorisée n'étant pas renseignée dans les AMM) |
| Nouvelle Indication Prédite | Urticaire allergique |
| Score de Prédiction TxGNN | 99,74 % |
| Niveau de Preuve | L5 (prédiction du modèle, aucune étude d'efficacité réelle) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

> Remarque : le niveau L4 figurait dans l'évaluation initiale des données. Il est ramené ici à L5, car l'unique publication est une étude pharmacocinétique vétérinaire sans critère d'efficacité, et non une étude de mécanisme ou préclinique d'efficacité.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le dimenhydrinate est un sel de diphénhydramine, antihistaminique H1 de première génération, et de 8-chlorothéophylline. Son efficacité dans le mal des transports et le vertige est établie, et mécanistiquement il pourrait être applicable à l'urticaire.

L'urticaire est une affection médiée par la libération d'histamine par les mastocytes. Le blocage des récepteurs H1 par la fraction diphénhydramine est donc un mécanisme plausible et bien connu, et les antihistaminiques de première génération ont été employés cliniquement dans cette situation. Le score TxGNN très élevé est cohérent avec ce raisonnement fondé sur la classe pharmacologique, mais il reste une prédiction.

Il faut toutefois nuancer : les recommandations actuelles privilégient les antihistaminiques H1 de seconde génération, non sédatifs. Un agent sédatif de première génération apporte peu d'avantage, et le statut commercial (AMM toutes annulées) limite l'intérêt pratique d'un développement.

La seconde prédiction, l'**urticaire au froid** (score 99,24 %), repose sur la même logique mécanistique mais ne dispose d'aucun essai ni d'aucune publication. Elle reste au niveau L5 avec une décision Hold.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Étude pharmacocinétique (étude pilote chez le chien) | Veterinary Dermatology | Compare la pharmacocinétique de la diphénhydramine après administration orale et intraveineuse, et après administration orale de dimenhydrinate. Le dimenhydrinate aurait une meilleure absorption orale de la diphénhydramine. Aucun critère d'efficacité clinique ; l'effet sur la formation de papules induites par l'histamine est évalué de façon pharmacodynamique. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69806008 | NAUSICALM 15,7 mg ENFANTS, sirop en sachet (BROTHIER) | Sirop | Non renseignée (AMM annulée) |
| 63137902 | NAUSICALM, sirop (BROTHIER) | Sirop | Non renseignée (AMM annulée) |
| 60173964 | NAUSICALM ADULTES 50 mg, gélule (BROTHIER) | Gélule | Non renseignée (AMM annulée) |
| 68461541 | MERCALM, comprimé pelliculé sécable (LABORATOIRES MAJORELLE) | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, ne provenant pas du texte de la notice) : hypertension, maladie hépatique, maladie de la vésicule biliaire, thrombopénie, hyperglycémie, diabète et acidocérose diabétique, ulcère gastroduodénal, hypertrophie bénigne de la prostate, obstruction du col vésical, hypotension, goutte, abus/dépendance à des substances, troubles de la coagulation, syndromes coronariens aigus, maladie coronarienne et infarctus du myocarde, hémoglobinopathie, hypertension oculaire et glaucome à angle fermé, sténose du pylore, hyperthyroïdie (maladie de Basedow, thyrotoxicose), hypophosphatémie.
- **Interactions médicamenteuses** : 67 interactions recensées. Les plus importantes :
  - **Majeures** : chlorure de potassium, citrate de potassium.
  - **Modérées** (surtout cumul d'effets anticholinergiques ou dépresseurs) : atropine, scopolamine, hyoscyamine, glycopyrronium, dicyclomine, clidinium, trospium, propanthéline, méthscopolamine, mépenzolate, morphine, opium, lopéramide, métoclopramide, nabilone, éluxadoline, prucalopride.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles dans les données compilées ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune preuve clinique directe ne soutient l'usage du dimenhydrinate dans l'urticaire : aucun essai, et une seule étude pharmacocinétique vétérinaire. Les alternatives de seconde génération sont préférées, et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles de la notice ANSM (information bloquante pour le criblage de sécurité)
- Les données sur le mécanisme d'action (DrugBank)
- Des preuves cliniques directes (essais ou études observationnelles) dans l'urticaire
- Une comparaison avec les antihistaminiques H1 de seconde génération
- Une évaluation de la faisabilité réglementaire, compte tenu de l'absence d'AMM valide
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

