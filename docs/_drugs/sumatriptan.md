---
layout: default
title: Sumatriptan
parent: Prédiction du modèle uniquement (L5)
nav_order: 725
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Sumatriptan : nouvelle indication prédite, Migraine avec aura du tronc cérébral (niveau de preuve L5). Indication d'origine : Migraine"
---

# Sumatriptan
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Sumatriptan : De la migraine à la migraine avec aura du tronc cérébral

## Résumé en Une Phrase

Le sumatriptan est un agoniste des récepteurs 5-HT1B/1D (classe des triptans), initialement utilisé pour le traitement de la migraine et de l'algie vasculaire de la face.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **migraine avec aura du tronc cérébral**, mais **aucun essai clinique** n'est enregistré et les **18 publications** identifiées portent surtout sur la migraine en général, sans preuve spécifique à ce sous-type.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Migraine (indications issues du graphe de connaissances : migraine avec ou sans aura, algie vasculaire de la face, hémicrânie paroxystique, hémicrânie continue) |
| Nouvelle Indication Prédite | Migraine avec aura du tronc cérébral |
| Score de Prédiction TxGNN | 99,74 % |
| Niveau de Preuve | L5 (prédiction du modèle, sans étude spécifique à ce sous-type) |
| Statut de Marché en France | Autorisations annulées uniquement |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

*Remarque : le système de scoring interne classe cette prédiction en L4 (« Research Question »). Selon la grille de ce rapport, aucune étude préclinique ou de mécanisme spécifique n'étant disponible, le niveau L5 est retenu pour ce sous-type précis.*

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances générales, le sumatriptan est un agoniste sélectif des récepteurs 5-HT1B/1D. Il soulagerait la crise migraineuse par vasoconstriction des vaisseaux crâniens et par inhibition de la libération de neuropeptides (dont le CGRP) et de la transmission nociceptive trigéminale.

La migraine avec aura du tronc cérébral est un sous-type clinique de la migraine. Elle partage donc la physiopathologie trigéminovasculaire de l'indication d'origine. Ce lien ontologique étroit explique probablement le score élevé du modèle (0,997), qui reflète plus la proximité avec la migraine que des preuves propres à ce sous-type.

**Point d'attention majeur :** les triptans ont historiquement été utilisés avec prudence, voire considérés comme contre-indiqués, dans la migraine avec aura du tronc cérébral (anciennement migraine basilaire), par crainte théorique d'une vasoconstriction dans la circulation postérieure. Cette question de sécurité doit être clarifiée avant toute recommandation.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune publication ne porte spécifiquement sur le sumatriptan dans la migraine avec aura du tronc cérébral. Les références les plus pertinentes concernent la migraine en général ou la migraine avec aura.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | ECR | Phytotherapy Research | Gingembre vs sumatriptan dans la migraine sans aura (100 patients, double aveugle) |
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | Essai randomisé contre placebo | Cephalalgia | Efficacité du sumatriptan oral 200 mg dans la migraine avec aura |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Étude clinique | Neurology | Efficacité réduite du sumatriptan dans la migraine avec aura par rapport à la migraine sans aura |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Revue (évaluation des preuves) | Headache | Évaluation actualisée des preuves des traitements aigus de la migraine chez l'adulte |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Revue | Cephalalgia | Revue critique du sumatriptan dans la migraine et l'algie vasculaire de la face |
| [12917936](https://pubmed.ncbi.nlm.nih.gov/12917936/) | 2003 | Revue Cochrane | Cochrane Database Syst Rev | Sumatriptan oral dans la migraine aiguë |
| [8559405](https://pubmed.ncbi.nlm.nih.gov/8559405/) | 1996 | Publication | Neurology | Sumatriptan sous-cutané et aura migraineuse |
| [26628293](https://pubmed.ncbi.nlm.nih.gov/26628293/) | 2016 | Revue | Drugs | Association sumatriptan/naproxène sodique dans la migraine avec ou sans aura |
| [27681528](https://pubmed.ncbi.nlm.nih.gov/27681528/) | 2016 | Revue | Drugs | Poudre nasale de sumatriptan dans le traitement aigu de la migraine |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Revue | Handbook of Clinical Neurology | État de mal migraineux, complication de la migraine avec ou sans aura |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67153334 | IMIGRANE 10 mg/0,1 ml, solution pour pulvérisation nasale (annulée) | Solution pour pulvérisation | Non renseignée |
| 66276750 | IMIJECT 6 mg/0,5 ml, solution injectable pour voie sous-cutanée en seringue pré-remplie (annulée) | Solution injectable | Non renseignée |
| 67876328 | IMIGRANE 20 mg/0,1 ml, solution pour pulvérisation nasale (annulée) | Solution pour pulvérisation | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : maladies cardiovasculaires (maladie coronarienne, infarctus du myocarde, insuffisance cardiaque congestive, cardiopathies, maladie vasculaire périphérique, claudication intermittente), accident vasculaire cérébral et maladies cérébrovasculaires (infarctus cérébral), hypertension, insuffisance hépatique et maladies hépatiques, maladie rénale, épilepsie, diabète et acidocétose diabétique, troubles de la coagulation, obésité, maladies de la vésicule biliaire, hémoglobinopathies et anémies, abus ou dépendance aux substances.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - **Majeures** : dexfenfluramine, fenfluramine, lorcasérine, sibutramine (risque de syndrome sérotoninergique), dolasétron, granisétron, ondansétron, palonosétron.
  - **Modérées** : morphine (y compris liposomale).
  - Plusieurs autres interactions de niveau non classé (inhibiteurs de la pompe à protons, metformine, doxycycline, cimétidine, etc.).
- **Préoccupation spécifique à l'indication** : la prudence historique des triptans dans la migraine avec aura du tronc cérébral (risque théorique d'ischémie du territoire vertébrobasilaire) est détaillée plus haut.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, non disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle et la proximité avec la migraine générale. Aucun essai clinique ni publication spécifique n'existe pour ce sous-type, et la préoccupation de sécurité vasculaire (circulation postérieure) n'est pas résolue.
- Toutes les AMM françaises sont annulées, et les données de notice (mises en garde, contre-indications) manquent, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Réaliser une revue ciblée de la sécurité des triptans dans la migraine avec aura du tronc cérébral (recommandations des sociétés savantes, séries de cas).
- Clarifier la situation réglementaire actuelle en France (autres spécialités à base de sumatriptan éventuellement commercialisées).
- Évaluer la compatibilité des voies d'administration pour cette indication.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

