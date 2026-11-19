---
layout: default
title: Alteplase
parent: Prédiction du modèle uniquement (L5)
nav_order: 48
evidence_level: L5
indication_count: 6
monitor_inn: "alteplase"
predicted_indications: ["heparin cofactor 2 deficiency", "congenital coronary artery anomaly", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "coronary stenosis"]
last_modified_at: 2026-10-28
description: "Alteplase : nouvelle indication prédite, Déficit en cofacteur II de l'héparine (heparin cofactor 2 deficiency) (niveau de preuve L5). En France, AMM dans la BDPM : 2 (valides : 2)"
---

# Alteplase
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Altéplase : activateur tissulaire du plasminogène recombinant (thrombolytique) → déficit en cofacteur II de l'héparine (heparin cofactor 2 deficiency)
{: .text-alpha }

## Résumé en Une Phrase

L'altéplase est un thrombolytique, un activateur tissulaire du plasminogène recombinant qui dissout les caillots de fibrine. Le modèle TxGNN prédit qu'il pourrait être efficace pour le **déficit en cofacteur II de l'héparine (heparin cofactor 2 deficiency)**. Aucun essai clinique ni aucune publication ne soutient actuellement cette direction : **0 essai clinique** et **0 publication**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Déficit en cofacteur II de l'héparine (heparin cofactor 2 deficiency) |
| Score de Prédiction TxGNN | 0,9972 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Alteplase (traduction non officielle) : « L'altéplase est une enzyme (sérine protéase) qui possède la propriété de convertir le plasminogène en plasmine, cette conversion étant renforcée par la fibrine. Elle ne produit qu'une conversion limitée du plasminogène en l'absence de fibrine. L'altéplase se lie à la fibrine d'un thrombus et convertit le plasminogène piégé en plasmine, déclenchant ainsi une fibrinolyse locale. » Texte original en anglais : "Alteplase is an enzyme (serine protease) that has the property of fibrin-enhanced conversion of plasminogen to plasmin. It produces limited conversion of plasminogen in the absence of fibrin. Alteplase binds to fibrin in a thrombus and converts the entrapped plasminogen to plasmin, thereby initiating local fibrinolysis." ([DailyMed: Cathflo Activase (alteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91ecdef2-95ff-42dd-a31c-c8a09cab3ad9), version du 2026-01-20 ; consulté le 2026-11-19). D'après les connaissances générales, l'altéplase convertit le plasminogène en plasmine, ce qui dégrade la fibrine des caillots. Cette action est pertinente dans les situations de thrombose aiguë.

Le déficit en cofacteur II de l'héparine est une thrombophilie héréditaire, c'est-à-dire une prédisposition à former des caillots. L'altéplase pourrait en principe dissoudre un thrombus aigu survenant dans ce contexte. Elle traiterait alors l'événement thrombotique, et non le déficit sous-jacent, qu'elle ne corrige pas.

Cette prédiction reste donc purement théorique. Aucune étude n'a été identifiée pour ce déficit précis, et le score élevé du modèle ne remplace pas une preuve clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

L'altéplase est commercialisée en France. Les autorisations de mise sur le marché recensées dans les données locales sont les suivantes. Le texte d'indication approuvée n'y est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 63617876 | ACTILYSE, poudre et solvant pour solution injectable et perfusion | Poudre et solvant pour solution injectable et pour perfusion |
| 67177673 | ACTILYSE 2 mg, poudre pour solution injectable et perfusion | Poudre pour solution injectable ou pour perfusion |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 140 interactions sont recensées au total. Voici quelques-unes parmi les premières listées :
  - Interactions majeures : abciximab, acalabrutinib, apixaban, fondaparinux, anisindione, déférasirox, ibritumomab tiuxétan, tositumomab. Elles concernent surtout un risque hémorragique additif avec les antithrombotiques et agents apparentés.
  - Interactions modérées : acide acétylsalicylique, kétorolac, ibuprofène, fluvoxamine, fosinopril, acide aminocaproïque, aprotinine, fenfluramine, dexfenfluramine, sibutramine.

Pour les mises en garde et contre-indications, veuillez consulter la notice, car ces informations ne figurent pas dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5). Aucun essai clinique ni aucune publication ne porte sur ce déficit. L'altéplase ne traiterait de toute façon que l'événement thrombotique aigu, non la cause du déficit, avec un risque hémorragique important.

**Pour avancer, les éléments suivants sont nécessaires :**
- Une revue de la littérature ciblée sur la thrombolyse chez les patients atteints de ce déficit, ou une série de cas.
- Les mises en garde et contre-indications de la notice ANSM, qui sont actuellement manquantes.
- Les données détaillées sur le mécanisme d'action.
- Une évaluation du rapport bénéfice/risque hémorragique dans cette population.

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Cathflo Activase (alteplase) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=91ecdef2-95ff-42dd-a31c-c8a09cab3ad9) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

