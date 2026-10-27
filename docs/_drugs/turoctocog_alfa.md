---
layout: default
title: Turoctocog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 795
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Turoctocog Alfa : nouvelle indication prédite, Trouble primaire de la libération plaquettaire (niveau de preuve L5). Indication d'origine : Hémophilie"
monitor_inn: "TUROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency", "thrombotic thrombocytopenic purpura", "hereditary thrombocytosis with transverse limb defect"]
---

# Turoctocog Alfa
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

## Turoctocog alfa : De l'hémophilie au trouble de libération plaquettaire primaire
{: .text-alpha }

## Résumé en Une Phrase

Turoctocog alfa est un facteur VIII de la coagulation recombinant, initialement utilisé pour le traitement de l'hémophilie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble primaire de la libération plaquettaire**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémophilie (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Trouble primaire de la libération plaquettaire |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Uniquement des AMM annulées |
| Nombre d'AMM | 6 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, turoctocog alfa est un facteur VIII recombinant de substitution, dont l'efficacité dans l'hémophilie (déficit en facteur VIII) repose sur la restauration de l'activité de ce cofacteur de la coagulation.

Pour le trouble primaire de la libération plaquettaire, le lien mécanistique est **faible**. Il s'agit d'un défaut intrinsèque de la fonction plaquettaire (sécrétion des granules ou signalisation), que l'apport de facteur VIII ne corrige pas. Le score élevé reflète probablement la proximité dans le graphe au sein du groupe des troubles hémorragiques plutôt qu'une véritable logique pharmacologique.

Les autres prédictions du modèle présentent le même constat. La plupart concernent des anomalies plaquettaires (thrombasthénie de Glanzmann, syndrome de Scott, pseudo-maladie de von Willebrand, défaut des récepteurs du collagène, thrombopénie constitutionnelle) non corrigées par le facteur VIII. La seule piste biologiquement plausible est le **déficit acquis en facteur de coagulation** (par exemple l'hémophilie A acquise), mais les inhibiteurs neutralisent généralement le FVIII exogène, ce qui fait préférer des agents de contournement. Le purpura thrombotique thrombocytopénique et la thrombocytose héréditaire avec malformation des membres posent en outre une question de sécurité (risque prothrombotique théorique). L'entité « flood factor deficiency » semble être un artefact d'ontologie ou une erreur de nomenclature.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 64266526 | NOVOEIGHT 3000 UI | Poudre et solvant pour solution injectable | Non renseignée | Annulée |
| 67582344 | NOVOEIGHT 1500 UI | Poudre et solvant pour solution injectable | Non renseignée | Annulée |
| 65044350 | NOVOEIGHT 1000 UI | Poudre et solvant pour solution injectable | Non renseignée | Annulée |
| 66990599 | NOVOEIGHT 250 UI | Poudre et solvant pour solution injectable | Non renseignée | Annulée |
| 62333524 | NOVOEIGHT 2000 UI | Poudre et solvant pour solution injectable | Non renseignée | Annulée |

Une sixième AMM (68274043, NOVOEIGHT 500 UI) est également annulée. Le titulaire est NOVO NORDISK (Danemark) pour l'ensemble des AMM.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées pour ce rapport.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Le mécanisme est biologiquement peu plausible pour les pathologies plaquettaires, et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications issues de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Une revue ciblée de la littérature et des registres d'essais pour le déficit acquis en facteur de coagulation, seule piste plausible
- La clarification de l'entité « flood factor deficiency » et une évaluation du risque thrombotique
- La confirmation de la disponibilité du produit, compte tenu du statut « annulé uniquement »
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

