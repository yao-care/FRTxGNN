---
layout: default
title: Ammonium Chloride
parent: Prédiction du modèle uniquement (L5)
nav_order: 60
evidence_level: L5
indication_count: 1
monitor_inn: "Ammonium chloride"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-10-23
description: "Ammonium Chloride : nouvelle indication prédite, Maladie de la cavité nasale (niveau de preuve L5). Indication d'origine : Pharyngite, rhume, rhinopharyngite"
---

# Ammonium Chloride
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Chlorure d'ammonium : Du rhume et de la pharyngite à la maladie de la cavité nasale
{: .text-alpha }

## Résumé en Une Phrase

Le chlorure d'ammonium est une substance historiquement utilisée comme expectorant, dont les indications enregistrées dans le graphe de connaissances sont la pharyngite, le rhume et la rhinopharyngite.
Le modèle TxGNN prédit qu'il pourrait être utile pour la **maladie de la cavité nasale**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Pharyngite, rhume, rhinopharyngite (relations enregistrées dans le graphe de connaissances ; aucun texte d'indication dans les AMM françaises compilées) |
| Nouvelle Indication Prédite | Maladie de la cavité nasale |
| Score de Prédiction TxGNN | 0,9994 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Le chlorure d'ammonium est connu comme un expectorant historique et un irritant muqueux léger, qui augmente les sécrétions fluides des voies respiratoires. Cette explication reste une hypothèse non vérifiée.

Le score de 0.9994 pour la maladie de la cavité nasale provient du modèle TxGNN (deep learning) et peut refléter des similarités que le modèle a apprises entre des maladies apparentées (pharyngite, rhume, rhinopharyngite), et non une preuve biologique. La maladie de la cavité nasale est anatomiquement et symptomatiquement proche de ces affections, ce qui peut expliquer en partie ce score élevé. Il s'agirait plutôt d'une extension de l'usage respiratoire supérieur que d'un mécanisme nouveau.

Le score très élevé est une sortie de modèle uniquement. Aucune donnée ne montre un bénéfice dans la maladie de la cavité nasale. Cette catégorie est très large et devrait être précisée (rhinite, sinusite, polypes nasaux, etc.) avant toute évaluation.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les quatre AMM compilées sont des produits à substance unique, valides, sous forme de solutions pour perfusion. Aucun texte d'indication approuvée n'est disponible pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63262521 | Solution injectable d'oligo-éléments Aguettant enfants et nourrissons | Solution injectable pour perfusion | Non renseignée |
| 68575185 | Pediaven AP-HP G15 | Solution pour perfusion | Non renseignée |
| 67678175 | Pediaven AP-HP G20 | Solution pour perfusion | Non renseignée |
| 62083608 | Pediaven AP-HP G25 | Solution pour perfusion | Non renseignée |

Ces produits sont des formes pour perfusion et ne correspondent pas à un usage nasal ou respiratoire.

## Considérations de Sécurité

- **Contre-indications (relations du graphe de connaissances, et non texte de notice)** : hypertension, insuffisance hépatique, épilepsie, insuffisance rénale ou anurie, insuffisance surrénalienne (maladie d'Addison), ulcère gastroduodénal, hypercalcémie, néphrocalcinose, glaucome à angle fermé, hyperthyroïdie, œdème pulmonaire, ischémie myocardique et maladie coronarienne, troubles de la conduction cardiaque, arrêt cardiaque, entérocolite nécrosante, ainsi que plusieurs troubles anxieux et psychiatriques. Cette liste n'est pas exhaustive.
- **Interactions Médicamenteuses** : 21 interactions recensées.
  - Modérées : amphétamine, dextroamphétamine, lisdexamfétamine, métamfétamine, benzphétamine.
  - Mineures : éphédrine, pseudoéphédrine, antidépresseurs tricycliques (amitriptyline, clomipramine, désipramine, doxépine, imipramine, nortriptyline, protriptyline, trimipramine), méthadone, méxilétine, flécaïne.

Les mises en garde issues des notices ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication portant sur la maladie de la cavité nasale. Les AMM françaises concernent des perfusions, sans lien avec une voie nasale ou respiratoire, et les données de sécurité issues des notices manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications des notices auprès de l'ANSM (lacune bloquante pour le criblage de sécurité)
- Obtenir les données sur le mécanisme d'action
- Préciser l'indication visée (rhinite, sinusite, polypes nasaux, etc.)
- Rechercher des études cliniques ou publiées portant directement sur cette affection
- Évaluer la compatibilité de la voie d'administration, aucune formulation adaptée n'étant identifiée dans les AMM compilées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

