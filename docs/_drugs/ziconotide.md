---
layout: default
title: Ziconotide
parent: Preuves modérées (L3-L4)
nav_order: 828
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Ziconotide : nouvelle indication prédite, Migraine (migraine disorder) (niveau de preuve L4). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "ZICONOTIDE"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "cauda equina syndrome", "obesity disorder", "transient ischemic attack (disease)", "open-angle glaucoma", "obsolete neurogenic bladder (disease)", "migraine with or without aura, susceptibility to", "primary hereditary glaucoma", "preeclampsia"]
---

# Ziconotide
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
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

# Ziconotide : De l'indication originale non renseignée à la migraine

## Résumé en Une Phrase

Ziconotide est un analgésique administré par voie intrathécale (spécialité PRIALT), dont l'indication originale n'est pas renseignée dans les données d'AMM compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **migraine** (trouble migraineux), avec **0 essai clinique** et **1 publication** directement associée (un rapport de cas), soit un niveau de preuve faible.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Migraine (migraine disorder) |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Autorisation annulée uniquement |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues dans l'analyse de la prédiction, le ziconotide est un bloqueur sélectif des canaux calciques voltage-dépendants de type N (Cav2.2). Il réduit la libération de neurotransmetteurs impliqués dans la nociception (substance P, CGRP, glutamate) au niveau de la corne dorsale de la moelle épinière et des voies trigéminales.

La migraine implique l'activation du système trigémino-vasculaire et la libération de CGRP. Il existe donc un lien mécanistique plausible : moduler la transmission nociceptive pourrait, en théorie, soulager des migraines chroniques réfractaires.

Cependant, les preuves restent anecdotiques : un rapport de cas de 2015 décrit la résolution de migraines chroniques sous ziconotide intrathécal, et une revue de 2022 évoque cette piste. La voie intrathécale, invasive, et la marge thérapeutique étroite (effets indésirables psychiatriques et neurologiques) limitent l'intérêt pratique face aux nombreuses options non invasives existantes.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26392785](https://pubmed.ncbi.nlm.nih.gov/26392785/) | 2015 | Rapport de cas | Journal of Pain Research | Résolution de migraines chroniques sous ziconotide intrathécal chez un patient |
| [35505713](https://pubmed.ncbi.nlm.nih.gov/35505713/) | 2022 | Revue / rapport de cas | Cureus | Le ziconotide intrathécal est présenté comme option émergente pour les migraines réfractaires aux traitements conventionnels |
| [41628204](https://pubmed.ncbi.nlm.nih.gov/41628204/) | 2026 | Revue narrative | Pain Physician | Revue sur le choix des dispositifs de neuromodulation dans la douleur chronique ; preuve indirecte |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66495139 | PRIALT 100 microgrammes/ml, solution pour perfusion | Solution pour perfusion | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations du graphe de connaissances, et non le texte de la notice) : trouble psychotique, trouble schizophréniforme, trouble mental, trouble schizo-affectif, trouble de la coagulation sanguine.
- **Interactions médicamenteuses** : 48 interactions recensées, toutes de niveau modéré parmi les 20 principales listées. Elles concernent notamment :
  - les opioïdes (morphine, codéine, hydrocodone, opium) ;
  - les antihistaminiques sédatifs (prométhazine, chlorphéniramine, cétirizine, clémastine, brompheniramine, carbinoxamine) ;
  - les cannabinoïdes (dronabinol, nabilone) ;
  - l'éthanol, le métoclopramide, le dextrométhorphane et la sibutramine.

  Le point commun est un risque d'addition des effets dépresseurs sur le système nerveux central.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, non disponibles dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La preuve se limite à un rapport de cas et à des revues, sans aucun essai clinique. Le produit n'a plus d'AMM valide en France (autorisation annulée) et la voie intrathécale invasive présente un rapport bénéfice-risque défavorable pour la migraine. Les données de sécurité officielles sont absentes, ce qui bloque le passage au criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), donnée bloquante.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Confirmer l'indication originale de l'AMM annulée.
- Réaliser une étude prospective ou une série de cas plus large chez des patients migraineux réfractaires, avec un plan de surveillance neuropsychiatrique.
- Comparer le ziconotide aux alternatives non invasives (anti-CGRP, par exemple) pour justifier l'intérêt clinique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

