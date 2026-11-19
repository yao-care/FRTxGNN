---
layout: default
title: Zolpidem
parent: Prédiction du modèle uniquement (L5)
nav_order: 831
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-04
monitor_inn: "zolpidem"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia"]
description: "Zolpidem : nouvelle indication prédite, Torticolis paroxystique bénin du nourrisson (benign paroxysmal torticollis of infancy) (niveau de preuve L5)."
---

# Zolpidem
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

## Zolpidem: Torticolis paroxystique bénin du nourrisson (benign paroxysmal torticollis of infancy)
{: .text-alpha }

## Résumé en Une Phrase

Le zolpidem est un hypnotique sédatif utilisé dans les troubles du sommeil.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **torticolis paroxystique bénin du nourrisson (benign paroxysmal torticollis of infancy)**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction (niveau de preuve L5).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Torticolis paroxystique bénin du nourrisson (benign paroxysmal torticollis of infancy) |
| Score de Prédiction TxGNN | 0.9926 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 11 sur 11) |
| Nombre d'AMM | 11 (valides : 11) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Zolpidem (traduction non officielle) : « Le zolpidem est un modulateur positif des récepteurs GABA A qui exercerait ses effets thérapeutiques dans le traitement à court terme de l'insomnie par liaison au site des benzodiazépines des récepteurs GABA A contenant la sous-unité α1, augmentant la fréquence d'ouverture des canaux chlorure, ce qui entraîne l'inhibition de l'excitation neuronale. » Texte original en anglais : "Zolpidem is a GABA A receptor positive modulator presumed to exert its therapeutic effects in the short-term treatment of insomnia through binding to the benzodiazepine site of α1 subunit containing GABA A receptors, increasing the frequency of chloride channel opening resulting in the inhibition of neuronal excitation." ([DailyMed: Ambien (zolpidem tartrate) prescribing information, Cosette Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=747949c5-2c91-4909-8a07-71b6826f8e97), version du 2025-02-07 ; consulté le 2026-11-19). Sur la base des informations connues, le zolpidem est un sédatif-hypnotique qui agit sur les récepteurs GABA-A, avec une sélectivité pour la sous-unité alpha-1.

Le torticolis paroxystique bénin du nourrisson est un trouble pédiatrique rare et spontanément résolutif, rattaché au spectre de la migraine et à des mécanismes de type canalopathie. Aucun rôle établi d'un hypnotique agissant sur les récepteurs GABA-A n'est connu dans cette affection.

Le lien repose uniquement sur un score de prédiction élevé. Aucun raisonnement mécanistique plausible n'apparaît, et la prédiction est vraisemblablement un artefact du modèle. Par ailleurs, l'utilisation du zolpidem chez le nourrisson ne serait pas appropriée sur le plan de la sécurité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les données compilées font état de 11 AMM, toutes valides, pour des spécialités à base de zolpidem seul.

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 61705683 | ZOLPIDEM ALMUS 10 mg (BIOGARAN) | Comprime pellicule secable | Active |
| 62969974 | ZOLPIDEM BIOGARAN 10 mg | Comprime pellicule secable | Active |
| 61843104 | ZOLPIDEM ZYDUS 10 mg | Comprime pellicule secable | Active |
| 63179285 | STILNOX 10 mg (SANOFI WINTHROP) | Comprime pellicule secable | Active |
| 69329603 | ZOLPIDEM CRISTERS 10 mg | Comprime pellicule secable | Active |

La liste est limitée aux 5 premières AMM.

## Considérations de Sécurité

- **Interactions médicamenteuses** : 274 interactions sont recensées. Parmi elles, des interactions de niveau majeur avec la morphine et la morphine liposomale. Plusieurs interactions de niveau modéré, notamment avec le bupropion, l'aprépitant, la dexaméthasone, la cimétidine, la clarithromycine, le métoclopramide, le miconazole et le clotrimazole.

Pour les mises en garde et contre-indications détaillées, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau de preuve L5), sans essai clinique ni publication portant sur le torticolis paroxystique bénin du nourrisson. Aucun lien mécanistique plausible n'est identifié, et l'usage chez le nourrisson soulève des préoccupations de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des données sur le mécanisme d'action détaillé
- Des études précliniques ou cliniques portant directement sur cette affection
- Les mises en garde et contre-indications issues de la notice officielle
- Une évaluation de la sécurité spécifique à la population pédiatrique

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Ambien (zolpidem tartrate) prescribing information, Cosette Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=747949c5-2c91-4909-8a07-71b6826f8e97) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

