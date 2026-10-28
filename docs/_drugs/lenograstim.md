---
layout: default
title: Lenograstim
parent: Prédiction du modèle uniquement (L5)
nav_order: 443
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
monitor_inn: "lenograstim"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease", "severe nonproliferative diabetic retinopathy"]
description: "Lenograstim : nouvelle indication prédite, Trouble de libération plaquettaire primaire (primary release disorder of platelets) (niveau de preuve L5). Indication d'origine : Non renseignée dans les do…"
---

# Lenograstim
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

## Lenograstim: Trouble de libération plaquettaire primaire (primary release disorder of platelets)
{: .text-alpha }

## Résumé en Une Phrase

Le lénograstim est un facteur de croissance des granulocytes (G-CSF recombinant glycosylé). Les données compilées pour ce rapport ne précisent pas son indication d'origine, car le texte d'indication des deux AMM françaises est vide.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble de libération plaquettaire primaire**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Trouble de libération plaquettaire primaire (primary release disorder of platelets) |
| Score de Prédiction TxGNN | 0.9991 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le lénograstim est un G-CSF recombinant qui se fixe au récepteur du G-CSF pour favoriser la prolifération et la différenciation des neutrophiles. Son action porte sur la lignée granulocytaire.

**La prédiction ne repose sur aucun lien mécanistique clair.** Les troubles de libération plaquettaire sont des défauts qualitatifs de la fonction plaquettaire (sécrétion des granules, signalisation altérée). Le G-CSF n'a pas d'effet établi sur la libération des granules ou sur la fonction plaquettaire. Le score élevé (0,9991) provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

Les trois autres prédictions de même nature ne sont pas mieux soutenues :
- **Thrombasthénie de Glanzmann** (99,89 %) : déficit de l'intégrine αIIbβ3, sans lien connu avec le G-CSF.
- **Pseudo-maladie de von Willebrand** (99,88 %) : mutation gain de fonction de la GPIbα, sans voie reliant le médicament à l'interaction GPIb-VWF.
- **Rétinopathie diabétique non proliférante sévère** (99,61 %) : lien seulement spéculatif (mobilisation de cellules progénitrices endothéliales, neuroprotection), avec un risque théorique de mobilisation de cellules pro-angiogéniques. Des traitements standards bien établis existent déjà.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66807418 | GRANOCYTE 13 Millions UI/ml, poudre et solvant pour solution injectable/perfusion en seringue préremplie | Poudre et solvant pour solution injectable pour perfusion | Non renseignée (AMM active) |
| 65066667 | GRANOCYTE 34 Millions UI/ml, poudre et solvant pour solution injectable/perfusion en seringue préremplie | Poudre et solvant pour solution injectable pour perfusion | Non renseignée (AMM active) |


---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées, et aucune contre-indication issue du graphe de connaissances n'est rapportée. Cela ne vaut pas absence de risque, les données de la notice n'ayant pas pu être exploitées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et sans lien mécanistique plausible entre un G-CSF et les troubles de la fonction plaquettaire.
- Le médicament n'a plus d'AMM valide en France, et les données de sécurité de la notice sont absentes, ce qui bloque toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle de l'ANSM (mises en garde, contre-indications, indications d'origine).
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Réaliser une recherche bibliographique ciblée pour identifier d'éventuelles données précliniques ou cliniques sur le G-CSF et la fonction plaquettaire.
- Clarifier la situation réglementaire (AMM annulées) et la faisabilité d'un développement ou d'un accès au produit.
- Si une piste est poursuivie, privilégier des études de mécanisme avant toute étude clinique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

