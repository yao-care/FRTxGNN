---
layout: default
title: L-Lysine
parent: Prédiction du modèle uniquement (L5)
nav_order: 427
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "L-Lysine : nouvelle indication prédite, Gastroparésie (niveau de preuve L5). Indication d'origine : Non renseignée dans les données compilées"
---

# L-Lysine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# L-Lysine : D'un usage nutritionnel (indication originale non renseignée) à la Gastroparésie

## Résumé en Une Phrase

La L-lysine est un acide aminé essentiel, présent dans des solutions de nutrition parentérale et de dialyse péritonéale. Les deux autorisations françaises recensées sont aujourd'hui annulées et ne mentionnent aucune indication.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **gastroparésie**, mais cette prédiction repose uniquement sur le calcul : **aucun essai clinique** et **1 publication** non pertinente (une étude préclinique sur des cellules souches) sont disponibles.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données compilées |
| Nouvelle Indication Prédite | Gastroparésie |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisations annulées uniquement |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la L-lysine est un acide aminé essentiel utilisé comme composant de solutions nutritionnelles (perfusion, dialyse péritonéale). Son usage dans ces produits relève d'un apport nutritionnel, et non du traitement d'une maladie digestive.

Aucun lien mécanistique établi n'a été identifié entre la L-lysine et la gastroparésie. Le score élevé du modèle (0,998) est une prédiction informatique. La seule publication retrouvée porte sur l'administration de cellules souches mésenchymateuses via des hydrogels de gélatine-alginate dans l'estomac : elle n'évalue pas la L-lysine comme agent thérapeutique. Tout rapprochement (par exemple via les acides aminés de biomatériaux à base de gélatine) serait spéculatif.

À titre d'information, deux autres prédictions de rang inférieur ont été examinées : la déficience congénitale en prothrombine (score 99,13 %) et la carence en vitamine D, terme obsolète dans l'ontologie (score 99,02 %). Aucune n'a d'essai ni de publication, ni de lien mécanistique démontré. Les analogues de la lysine (acide tranexamique, acide aminocaproïque) sont des antifibrinolytiques, mais cette pharmacologie ne peut pas être transposée à la L-lysine.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [29414870](https://pubmed.ncbi.nlm.nih.gov/29414870/) | 2018 | Étude préclinique (biomatériaux) | Bioengineering (Basel) | Administration de cellules souches mésenchymateuses à partir d'hydrogels de gélatine-alginate vers la lumière gastrique pour la gastroparésie ; la L-lysine n'est pas évaluée |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62789435 | PRIMENE 10 %, solution injectable pour perfusion (annulée) | Solution pour perfusion | Non renseignée |
| 65461618 | NUTRINEAL PD4 À 1,1 % D'ACIDES AMINÉS, solution pour dialyse péritonéale (annulée) | Solution pour dialyse péritonéale | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune donnée issue des notices n'a pu être exploitée pour ce rapport, et aucune interaction médicamenteuse n'a été retrouvée.

À titre indicatif, le graphe de connaissances utilisé par le modèle associe la L-lysine à des contre-indications potentielles dans les maladies suivantes (relations du graphe, et non texte d'étiquetage) :
- **Atteintes rénales** : maladie rénale, insuffisance rénale chronique, insuffisance rénale terminale, néphropathie urique aiguë, néphrolithiase, néphrocalcinose, pyourétère
- **Troubles calciques et phosphorés** : hypercalcémie, hypercalcémie humorale d'origine maligne, sarcoïdose, trouble du métabolisme du phosphore
- **Atteintes cardiovasculaires** : cardiopathie, maladie cardiovasculaire, fibrillation ventriculaire, intoxication digitalique
- **Troubles du métabolisme de la phénylalanine** : phénylcétonurie

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai clinique, aucune publication pertinente, aucun lien mécanistique démontré. De plus, les deux autorisations françaises sont annulées et les données de sécurité des notices manquent (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser les notices (mises en garde, contre-indications) auprès de l'ANSM
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Rechercher une justification biologique plausible entre la L-lysine et la gastroparésie, puis des études précliniques ou cliniques ciblées
- Évaluer la pertinence des contre-indications rénales, cardiaques et calciques signalées par le graphe de connaissances
- Clarifier l'indication originale et la compatibilité de voie d'administration
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

