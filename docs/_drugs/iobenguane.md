---
layout: default
title: Iobenguane
parent: Preuves modérées (L3-L4)
nav_order: 405
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-30
monitor_inn: "IOBENGUANE"
predicted_indications: ["hypotensive disorder", "multiple system atrophy", "variably protease-sensitive prionopathy", "postural orthostatic tachycardia syndrome"]
description: "Iobenguane : nouvelle indication prédite, Hypotensive disorder (niveau de preuve L4). Indication d'origine : Non renseignée dans les données locales"
---

# Iobenguane
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **4** 
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

## Iobenguane: Hypotensive disorder
{: .text-alpha }

## Resume en Une Phrase

L'iobenguane (MIBG) est un analogue de la noradrénaline, commercialisé en France sous forme de solution injectable marquée à l'iode 123 ; son AMM est aujourd'hui annulée et le texte de l'indication approuvée n'est pas disponible.
Le modèle TxGNN prédit qu'il pourrait être pertinent pour le **trouble hypotensif**, avec **0 essai clinique** et **2 publications** indirectement liées (revues).
Ces publications ne montrent pas que l'iobenguane traite l'hypotension : tout rôle réaliste serait diagnostique (scintigraphie au MIBG) et non thérapeutique.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Predite | Hypotensive disorder |
| Score de Prediction TxGNN | 0.9990 |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales, l'iobenguane est un analogue de la noradrénaline, capté par le transporteur de la noradrénaline dans les neurones sympathiques et les cellules chromaffines. Il permet donc d'explorer l'intégrité sympathique cardiaque et périphérique.

Ce lien explique la proximité avec l'hypotension orthostatique et les défaillances autonomes. La revue sur l'hypotension orthostatique dans la maladie de Parkinson éclaire la physiopathologie de l'hypotension neurogène, et l'article sur la chirurgie du phéochromocytome concerne les perturbations tensionnelles liées aux catécholamines. Aucun des deux ne démontre un effet thérapeutique de l'iobenguane.

Le score élevé (0,999) est une prédiction du modèle uniquement. Le rôle plausible est diagnostique (scintigraphie au MIBG marqué), pas thérapeutique.

### Autres indications prédites (à titre informatif)

| Rang | Indication prédite | Score TxGNN | Niveau de preuve | Commentaire |
|---|---|---|---|---|
| 2 | Atrophie multisystématisée | 0,9990 | L5 | Usage diagnostique établi : la fixation cardiaque du MIBG aide à distinguer la maladie de Parkinson (fixation réduite) de l'AMS (fixation typiquement préservée). Aucun essai ; une seule revue indirecte. |
| 3 | Prionopathie variablement sensible à la protéase | 0,9986 | L5 | Aucun lien mécanistique plausible ; le score provient du modèle TxGNN (deep learning) et peut refléter des similitudes apprises par le modèle entre maladies apparentées, non des preuves biologiques. |
| 4 | Syndrome de tachycardie orthostatique posturale | 0,9967 | L5 | Lien hypothétique (dysautonomie, déficit du transporteur de la noradrénaline) ; rôle éventuel uniquement diagnostique. |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [11482743](https://pubmed.ncbi.nlm.nih.gov/11482743/) | 2001 | Revue | Drugs & Aging | Physiopathologie et prise en charge de l'hypotension orthostatique dans la maladie de Parkinson : prévalence symptomatique pouvant atteindre 20 %, liée aux médicaments dopaminergiques et à la dysautonomie primaire. |
| [2666677](https://pubmed.ncbi.nlm.nih.gov/2666677/) | 1989 | Revue | Journal of the National Medical Association | Avancées de la prise en charge chirurgicale du phéochromocytome : dosages biochimiques, imagerie, surveillance périopératoire et bloqueurs adrénergiques. |

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 64886840 | MIBG [123 I] 74 MBq/mL solution injectable (CURIUM NETHERLANDS, Pays-Bas) — statut : active | Solution injectable | Non renseignée |

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- Aucun essai clinique n'a été retrouvé et les deux publications sont des revues indirectes, sans démonstration d'un bénéfice thérapeutique de l'iobenguane dans l'hypotension. Le score TxGNN élevé reflète une prédiction du modèle, non une preuve.
- La seule AMM française est annulée, et les données de sécurité et de mécanisme d'action sont manquantes, ce qui empêche toute évaluation de sécurité.

**Pour avancer, les elements suivants sont necessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour l'évaluation de sécurité).
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank).
- Préciser si l'objectif est diagnostique (scintigraphie MIBG dans l'AMS, la maladie de Parkinson, le POTS) ou thérapeutique ; une hypothèse thérapeutique n'est pas soutenue à ce jour.
- Clarifier le statut réglementaire actuel du produit en France (AMM annulée) et la disponibilité d'autres spécialités.
- Rechercher des études cliniques ou observationnelles ciblées sur l'usage diagnostique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

