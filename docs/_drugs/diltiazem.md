---
layout: default
title: Diltiazem
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 1
---

# Diltiazem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Diltiazem : Du Traitement Cardiovasculaire à la Prédisposition à l'Accident Vasculaire Cérébral Ischémique

## Résumé en Une Phrase

Diltiazem est un bloqueur des canaux calciques de type L (L-type CCB), classiquement utilisé dans le traitement des maladies cardiovasculaires telles que l'hypertension artérielle, l'angine de poitrine et certaines arythmies.
Le modèle TxGNN prédit qu'il pourrait être potentiellement efficace pour la **prédisposition à l'accident vasculaire cérébral ischémique** (terme ontologique obsolète),
avec **0 essai clinique** et **0 publication** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Non disponible (aucune AMM enregistrée dans la base consultée) |
| Nouvelle Indication Prédite | Prédisposition à l'AVC ischémique *(terme ontologique obsolète)* |
| Score de Prédiction TxGNN | 99.08% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Diltiazem est un bloqueur des canaux calciques de type L (L-type CCB). Théoriquement, ce mécanisme d'action présente une pertinence dans le contexte de l'AVC ischémique : lors d'un épisode ischémique cérébral, une surcharge calcique intraneuronale massive déclenche une cascade excitotoxique. Un CCB pourrait en principe atténuer cette surcharge et, par vasodilatation cérébrale, améliorer la perfusion via la circulation collatérale.

Cependant, les données cliniques disponibles sur les CCB dans l'AVC ischémique reposent principalement sur la **nimodipine**, un CCB à sélectivité cérébrale marquée. Diltiazem, dont le profil pharmacocinétique et la sélectivité vasculaire diffèrent, ne dispose d'aucun essai clinique ni d'aucune publication directement consacrés à cette indication. La transposabilité du mécanisme reste donc purement hypothétique à ce stade.

Un point de vigilance méthodologique majeur : le terme de la maladie cible porte le préfixe **« obsolete »**, signalant que cette ontologie (DOID ou équivalent) a été abandonnée dans les classifications actuelles. Une remise en correspondance explicite vers le terme en vigueur (ex. DOID:3454 *ischemic stroke*, ou CIM-11 8B11) est indispensable avant toute évaluation clinique ou réglementaire sérieuse.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

> Les données de mises en garde, contre-indications et interactions médicamenteuses n'ont pas été retrouvées dans la base consultée lors de cette évaluation. Une consultation de la notice ANSM officielle est indispensable avant tout usage clinique.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction TxGNN s'appuie uniquement sur le modèle algorithmique (niveau de preuve L5), sans aucune donnée clinique ou bibliographique disponible pour soutenir l'efficacité de Diltiazem dans cette indication. De surcroît, le terme de maladie cible est ontologiquement obsolète, rendant toute interprétation directe prématurée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Remise en correspondance du terme « obsolete susceptibility to ischemic stroke » vers la classification actuelle (DOID:3454, CIM-11 8B11 ou équivalent) et relance de la recherche de preuves avec les termes actualisés
- Obtention des données détaillées de mécanisme d'action (MOA) de Diltiazem via DrugBank API
- Recherche active d'essais cliniques et de publications avec les termes mis à jour (« diltiazem » + « ischemic stroke » / « AVC ischémique »)
- Téléchargement et analyse de la notice ANSM officielle pour compléter l'évaluation de sécurité (mises en garde, contre-indications, interactions)
- Vérification du statut réglementaire réel de Diltiazem en France — des AMM existent vraisemblablement mais n'ont pas été retrouvées dans la base TFDA consultée, qui est orientée marché taïwanais
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

