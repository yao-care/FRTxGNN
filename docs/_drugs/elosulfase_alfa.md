---
layout: default
title: Elosulfase Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 276
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Elosulfase Alfa : nouvelle indication prédite, Syndrome de Scheie (niveau de preuve L5). Indication d'origine : Mucopolysaccharidose"
monitor_inn: "elosulfase alfa"
predicted_indications: ["camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye", "ptosis-vocal cord paralysis syndrome", "ptosis-strabismus-ectopic pupils syndrome", "ptosis-upper ocular movement limitation-absence of lacrimal punctum syndrome", "congenital Horner syndrome (disease)"]
---

# Elosulfase Alfa
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Elosulfase alfa : De la mucopolysaccharidose au syndrome de Scheie

## Résumé en Une Phrase

L'elosulfase alfa est une enzyme de remplacement (thérapie enzymatique substitutive) initialement utilisée pour traiter la mucopolysaccharidose (MPS), en pratique la MPS IVA (syndrome de Morquio A).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome de Scheie**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.
Cette prédiction repose uniquement sur le modèle (niveau de preuve L5) et l'analyse mécanistique la juge peu plausible.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mucopolysaccharidose (le texte d'indication de l'AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Syndrome de Scheie |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'elosulfase alfa est une enzyme recombinante qui remplace la N-acétylgalactosamine-6-sulfatase (GALNS). Cette enzyme dégrade le kératane sulfate et la chondroïtine-6-sulfate, et son efficacité dans la MPS IVA est établie.

Le syndrome de Scheie (forme atténuée de la MPS I) est causé par un déficit en alpha-L-iduronidase, avec accumulation de dermatane sulfate et d'héparane sulfate. Les enzymes et les substrats sont donc différents de ceux de l'elosulfase alfa. Le score élevé du modèle reflète vraisemblablement la proximité des maladies lysosomales (MPS) dans le réseau de connaissances, et non une véritable correspondance mécanistique.

De plus, une thérapie enzymatique par iduronidase (laronidase) existe déjà pour cette maladie. La prédiction doit donc être considérée comme peu plausible en l'état.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour le syndrome de Scheie.

À titre indicatif, pour d'autres indications prédites : un seul essai figure dans les données, NCT04532047 (Phase 1, syndrome de Hurler, 10 participants), qui ne concerne pas le syndrome de Scheie et n'apporte qu'une preuve indirecte.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour le syndrome de Scheie.

Les publications retrouvées pour d'autres prédictions (notamment le syndrome de Sanfilippo et la « maladie lysosomale avec atteinte squelettique ») portent presque exclusivement sur l'elosulfase alfa dans la MPS IVA, c'est-à-dire l'indication d'origine. Elles ne constituent pas une preuve pour les nouvelles indications prédites.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61673965 (annulée) | VIMIZIM 1 mg/ml, solution à diluer pour perfusion | Solution à diluer pour perfusion | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle, sans essai clinique ni publication, et le mécanisme (GALNS contre iduronidase) ne correspond pas à la maladie visée.
- Un traitement enzymatique approuvé existe déjà pour le syndrome de Scheie, et l'AMM française de l'elosulfase alfa est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action et justification d'un lien mécanistique avec le déficit en iduronidase
- Données précliniques (modèles de MPS I) démontrant un effet éventuel
- Mises en garde et contre-indications issues de la notice officielle (ANSM), dont l'absence bloque l'évaluation de sécurité
- Clarification du statut réglementaire (AMM annulée) et de la voie d'administration
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

