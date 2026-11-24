---
layout: default
title: Calcifediol
parent: Prédiction du modèle uniquement (L5)
nav_order: 129
evidence_level: L5
indication_count: 1
monitor_inn: "calcifediol"
predicted_indications: ["renal tubular acidosis"]
last_modified_at: 2026-11-24
description: "Calcifediol : nouvelle indication prédite, Renal tubular acidosis (niveau de preuve L5). En France, AMM dans la BDPM : 4 (valides : 4)"
---

# Calcifediol
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

## Calcifediol: Renal tubular acidosis
{: .text-alpha }

## Résumé en Une Phrase

Le calcifédiol (25-hydroxyvitamine D3) est le précurseur circulant direct du calcitriol et le biomarqueur de référence du statut en vitamine D.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Renal tubular acidosis |
| Score de Prédiction TxGNN | 0.9986 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Calcifediol (traduction non officielle) : « Le calcifédiol (25-hydroxyvitamine D 3 ) est une prohormone de la forme active de la vitamine D 3, le calcitriol (1,25‑dihydroxyvitamine D 3 ). Le calcifédiol est converti en calcitriol par le cytochrome P450 27B1 (CYP27B1), également appelé 1-alpha hydroxylase, principalement dans le rein. » Texte original en anglais : "Calcifediol (25-hydroxyvitamin D 3 ) is a prohormone of the active form of vitamin D 3, calcitriol (1,25‑dihydroxyvitamin D 3 ). Calcifediol is converted to calcitriol by cytochrome P450 27B1 (CYP27B1), also called 1-alpha hydroxylase, primarily in the kidney." ([DailyMed: Rayaldee (calcifediol) prescribing information, OPKO Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6a95effd-32a5-46b6-a30e-7f4f9bf8cc77), version du 2024-01-19 ; consulté le 2026-11-19). Sur la base des informations connues, le calcifédiol est la forme 25-hydroxylée de la vitamine D3, l'intermédiaire circulant qui est ensuite converti en calcitriol, la forme active. C'est aussi le marqueur biologique standard utilisé pour évaluer le statut en vitamine D.

Cette position dans la voie métabolique rend le lien biologique avec une carence en vitamine D très plausible.

Une réserve importante : le terme de maladie est signalé comme obsolète dans l'ontologie. Il faudrait le rattacher au terme actuel de carence en vitamine D avant toute évaluation approfondie.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 67317463 | CALCIFEDIOL DESMA 15 mg/100 ml, solution buvable en gouttes | Solution buvable en gouttes | DESMA PHARMA | Active |
| 68280975 | DEDROGYL 15 mg/100 ml, solution buvable en gouttes | Solution buvable en gouttes | DESMA PHARMA | Active |
| 67563301 | LUZADEL 266 microgrammes, capsule molle | Capsule molle | BESINS HEALTHCARE FRANCE | Active |
| 60748767 | CALCIFEDIOL GERDA 15 mg/100 mL, solution buvable en gouttes | Solution buvable en gouttes | SOCIETE ALEPT | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues des données de relations médicament-maladie** (hors texte de notice) : maladie rénale, pyo-uretère, sarcoïdose, hypercalcémie, néphrocalcinose, trouble du métabolisme du phosphore, lithiase rénale (y compris la forme de susceptibilité liée à SLC26A1), néphropathie urique aiguë, hyperphosphatémie, hypervitaminose, artériosclérose oblitérante.
- **Interactions médicamenteuses** : 57 interactions recensées. Principales interactions de niveau majeur : cholécalciférol, burosumab, calcitriol. Interactions de niveau modéré, par exemple : fosphénytoïne, hydrochlorothiazide et autres thiazidiques, barbituriques (amobarbital, butalbital, butabarbital), hydroxyde d'aluminium, carbamazépine, résines chélatrices (cholestyramine, colésévélam, colestipol), digitoxine, analogues topiques de la vitamine D (calcipotriol, calcitriol).

Veuillez consulter la notice pour les informations de sécurité complètes : les mises en garde et contre-indications issues du texte officiel n'ont pas pu être compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau de preuve L5) : aucun essai clinique ni publication n'a été identifié, et le terme de maladie est obsolète. Le lien biologique est plausible, mais il n'est pas étayé par des études directes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Rattacher la prédiction au terme actuel de carence en vitamine D
- Rechercher des essais cliniques et des publications portant directement sur la carence en vitamine D
- Obtenir les données sur le mécanisme d'action
- Récupérer les mises en garde et contre-indications de la notice officielle (ANSM)
- Examiner la compatibilité des voies d'administration et le risque d'hypercalcémie lié aux interactions majeures

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Rayaldee (calcifediol) prescribing information, OPKO Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6a95effd-32a5-46b6-a30e-7f4f9bf8cc77) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

