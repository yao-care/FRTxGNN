---
layout: default
title: Aztreonam
parent: Prédiction du modèle uniquement (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
monitor_inn: "aztreonam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
last_modified_at: 2026-10-28
description: "Aztreonam : nouvelle indication prédite, Hyperamylasémie (hyperamylasemia) (niveau de preuve L5). En France, AMM dans la BDPM : 3 (valides : 3)"
---

# Aztreonam
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

## Aztréonam : monobactame antibactérien → Hyperamylasémie (hyperamylasemia)
{: .text-alpha }

## Résumé en Une Phrase

L'aztréonam est un antibiotique de la classe des monobactames, actif contre les bactéries à Gram négatif.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hyperamylasémie (hyperamylasemia)**,
mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hyperamylasémie (hyperamylasemia) |
| Score de Prédiction TxGNN | 0,9973 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Aztreonam (traduction non officielle) : « L'aztréonam est un agent bactéricide qui agit par inhibition de la synthèse de la paroi cellulaire bactérienne. L'aztréonam est actif en présence de certaines bêta-lactamases, à la fois pénicillinases et céphalosporinases, des bactéries à Gram négatif et à Gram positif. » Texte original en anglais : "Aztreonam is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Aztreonam has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: aztreonam prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d4500795-3b07-4a7d-b432-73cafbb3dbc6), version du 2024-06-03 ; consulté le 2026-11-19). D'après les connaissances générales, l'aztréonam est un monobactame qui inhibe la protéine de liaison à la pénicilline 3 (PBP3) des bactéries à Gram négatif, ce qui bloque la synthèse de leur paroi.

Aucun lien mécanistique plausible n'est identifié entre cette action antibactérienne et l'hyperamylasémie, qui est une anomalie biologique (élévation de l'amylase sérique) et non une infection. L'aztréonam n'a pas d'effet connu sur le métabolisme ou la clairance de l'amylase.

Le score élevé reflète une prédiction issue du modèle uniquement. Il ne repose sur aucune donnée expérimentale ou clinique et doit être interprété avec une grande prudence : il s'agit très probablement d'un artefact de modélisation.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61054849 | CAYSTON 75 mg, poudre et solvant pour solution pour inhalation par nébiliseur | Poudre et solvant pour solution pour inhalation par nébuliseur | Non renseignée dans les données locales |
| 63918096 | AZACTAM 1 g, poudre pour solution injectable/pour perfusion | Poudre pour solution injectable pour perfusion | Non renseignée dans les données locales |
| 68544663 | EMBLAVEO 1,5 g/0,5 g, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | Non renseignée dans les données locales |

## Considérations de Sécurité

- **Interactions médicamenteuses** : 27 interactions sont recensées dans les données compilées. Les interactions de niveau modéré concernent l'acide picosulfurique, le dicoumarol et la warfarine (surveillance de l'anticoagulation à envisager). Les autres interactions listées, dont le niveau n'est pas précisé, incluent notamment l'oméprazole, le pantoprazole, la vancomycine, l'amikacine, le tacrolimus, l'amphotéricine B, l'héparine et la morphine.

Veuillez consulter la notice pour les autres informations de sécurité (mises en garde et contre-indications).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (0,9973), sans essai clinique, sans publication et sans mécanisme plausible. Les preuves sont insuffisantes pour justifier un développement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Un rationnel biologique crédible reliant l'aztréonam à l'hyperamylasémie
- Des données de mécanisme d'action détaillées
- Les mises en garde et contre-indications issues des notices officielles de l'ANSM
- Toute étude (précliniques ou cliniques) étudiant directement l'hyperamylasémie avec l'aztréonam

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: aztreonam prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d4500795-3b07-4a7d-b432-73cafbb3dbc6) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

