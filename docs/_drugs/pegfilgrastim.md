---
layout: default
title: Pegfilgrastim
parent: Prédiction du modèle uniquement (L5)
nav_order: 583
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Pegfilgrastim : nouvelle indication prédite, Rétinopathie diabétique non proliférante sévère (seconde prédiction :… (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM…"
monitor_inn: "PEGFILGRASTIM"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Pegfilgrastim
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

## Pegfilgrastim : D'un facteur de croissance des neutrophiles à la rétinopathie diabétique non proliférante sévère
{: .text-alpha }

## Résumé en Une Phrase

Pegfilgrastim est un facteur de croissance des granulocytes (G-CSF) pégylé, qui stimule la production de neutrophiles. Le texte des indications des autorisations françaises n'est pas renseigné dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **rétinopathie diabétique non proliférante sévère**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Rétinopathie diabétique non proliférante sévère (seconde prédiction : rétinopathie diabétique, terme plus général) |
| Score de Prédiction TxGNN | 0,9989 (rétinopathie diabétique : 0,9973) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 10 sur 10) |
| Nombre d'AMM | 10 (valides : 10) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le pégfilgrastim est un analogue pégylé du G-CSF : il stimule la production de neutrophiles en se liant au récepteur du G-CSF.

Un lien plausible, mais non testé, serait la mobilisation de cellules progénitrices endothéliales issues de la moelle osseuse, qui pourrait soutenir la réparation vasculaire dans les rétinopathies ischémiques.

L'effet pourrait toutefois aller dans le sens inverse. L'activation des neutrophiles, l'inflammation et la leucostase, ainsi que des signaux pro-angiogéniques associés au G-CSF, pourraient aggraver les lésions vasculaires rétiniennes. Le sens de l'effet est donc incertain. Les deux indications prédites sont de plus liées (la seconde est le terme parent de la première) : elles ne constituent pas deux preuves indépendantes. Il s'agit à ce stade d'une prédiction purement computationnelle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 10 AMM recensées sont annulées. Le texte de l'indication approuvée n'est pas disponible pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 63655026 | GRASUSTEK 6 mg, seringue préremplie | Solution injectable | Active |
| 60457929 | FULPHILA 6 mg, seringue préremplie | Solution injectable | Active |
| 64847677 | PELGRAZ 6 mg, stylo injecteur prérempli | Solution injectable | Active |
| 61553026 | PELGRAZ 6 mg, seringue préremplie | Solution injectable | Active |
| 63626633 | ZIEXTENZO 6 mg, seringue préremplie | Solution injectable | Active |

## Considérations de Sécurité

**Interactions Médicamenteuses** : 100 interactions ont été recensées. Les 20 premières, toutes de niveau modéré, concernent notamment : pegvaliase, iobenguane (I-131), fludéoxyglucose (18F), ibritumomab tiuxétan, tositumomab, lévamisole, triméthrexate, mercaptopurine, abémaciclib, paclitaxel, acalabrutinib, aldesleukine, alemtuzumab, altrétamine, trioxyde d'arsenic, asparaginase, avapritinib, azacitidine et bélantamab mafodotin.

Veuillez consulter la notice pour les mises en garde et contre-indications, qui ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication. Le sens de l'effet est incertain, avec un risque théorique d'aggravation de la pathologie rétinienne.
- Les 10 AMM françaises sont valides (10 sur 10) et le médicament est commercialisé, mais les données de sécurité issues de la notice font défaut, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde, contre-indications, indications approuvées)
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Réaliser une revue de la littérature préclinique (G-CSF, cellules progénitrices endothéliales, rétinopathie diabétique) et rechercher d'éventuels essais
- Évaluer la compatibilité de la voie d'administration (injection systémique par rapport à une administration oculaire)
- Vérifier le statut réglementaire actuel du produit en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

