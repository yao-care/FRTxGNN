---
layout: default
title: Histidine
parent: Prédiction du modèle uniquement (L5)
nav_order: 141
evidence_level: L5
indication_count: 2
---

# Histidine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Histidine : De Supplément en Acide Aminé Essentiel à la Gastroparésie

## Résumé en Une Phrase

Histidine est un acide aminé semi-essentiel, précurseur biochimique de l'histamine, utilisé principalement dans la nutrition parentérale et comme composant fondamental de la synthèse protéique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Gastroparésie**,
avec **0 essai clinique** et **aucune publication** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Acide aminé essentiel — nutrition clinique et synthèse protéique |
| Nouvelle Indication Prédite | Gastroparésie |
| Score de Prédiction TxGNN | 99.55% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé (substance isolée) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de l'histidine (DB00117) ne sont pas disponibles dans les sources consultées. Sur la base des informations biochimiques connues, l'histidine est convertie en histamine par la L-histidine décarboxylase (HDC) — c'est son principal rôle métabolique en lien avec la physiologie gastrique.

L'histamine agit sur les récepteurs H2 de la muqueuse gastrique pour moduler la sécrétion d'acide chlorhydrique et pourrait, en théorie, influencer la motilité gastrique. Dans la gastroparésie, la vidange gastrique est pathologiquement ralentie ; un lien indirect via l'axe histidine→histamine→H2 est biologiquement concevable, mais reste à ce stade purement hypothétique.

Ce lien est cependant sans soutien empirique : il n'existe aucune étude préclinique sur modèle animal ni aucune donnée clinique soutenant la supplémentation en histidine comme traitement de la gastroparésie. Le score TxGNN élevé (0,9955) reflète vraisemblablement la haute connectivité des nœuds histamine-estomac dans le graphe de connaissances, et non une preuve de direction thérapeutique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Aucune AMM enregistrée pour l'histidine en tant que substance médicamenteuse isolée en France.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Il n'existe aucune preuve préclinique ou clinique soutenant l'efficacité de l'histidine dans la gastroparésie. Le score TxGNN de 99,55 % reflète une association topologique dans le graphe de connaissances (nœuds histamine-estomac) et non une direction thérapeutique validée. Par ailleurs, il convient de noter que pour la seconde indication prédite (cholangite sclérosante, score 99,27 %), les données mécanistiques disponibles indiquent un **conflit de direction** : l'axe histidine→histamine favorise la prolifération biliaire et la fibrose, suggérant qu'une supplémentation pourrait aggraver la maladie plutôt que la traiter.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (MOA) à récupérer via l'API DrugBank
- Notice officielle TFDA/ANSM pour le profil de sécurité complet
- Études précliniques explorant l'effet de la supplémentation en histidine sur la motilité gastrique
- Revue systématique de l'axe histidine–histamine–récepteurs H2 dans le contexte gastrique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

