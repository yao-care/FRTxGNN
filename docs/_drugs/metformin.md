---
layout: default
title: Metformin
parent: Prédiction du modèle uniquement (L5)
nav_order: 483
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "metformin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
description: "Metformin : nouvelle indication prédite, Focal stiff limb syndrome (niveau de preuve L5). En France, AMM dans la BDPM : 9 (valides : 9)"
---

# Metformin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

## Metformin: Focal stiff limb syndrome
{: .text-alpha }

## Résumé en Une Phrase

La metformine est un antidiabétique oral, initialement utilisé pour le traitement du diabète de type 2.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome du membre raide focal**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Focal stiff limb syndrome |
| Score de Prédiction TxGNN | 0.9945 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 9 sur 9) |
| Nombre d'AMM | 9 (valides : 9) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Metformin (traduction non officielle) : « La metformine est un agent antihyperglycémiant qui améliore la tolérance au glucose chez les patients atteints de diabète sucré de type 2, en abaissant la glycémie basale et postprandiale. La metformine diminue la production hépatique de glucose, diminue l'absorption intestinale du glucose et améliore la sensibilité à l'insuline en augmentant la captation et l'utilisation périphériques du glucose. » Texte original en anglais : "Metformin is an antihyperglycemic agent which improves glucose tolerance in patients with type 2 diabetes mellitus, lowering both basal and postprandial plasma glucose. Metformin decreases hepatic glucose production, decreases intestinal absorption of glucose, and improves insulin sensitivity by increasing peripheral glucose uptake and utilization." ([DailyMed: Metformin Hydrochloride Er (metformin hydrochloride) prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3dca884d-ec44-496f-9eeb-31fd8fa3f574), version du 2026-09-21 ; consulté le 2026-11-19). Sur la base des informations connues, la metformine appartient à la classe des biguanides. Elle est reconnue pour activer l'AMPK, réduire la production hépatique de glucose et exercer de légers effets anti-inflammatoires. Son efficacité dans le diabète de type 2 est établie.

Le syndrome du membre raide focal appartient au spectre du syndrome de la personne raide, un trouble neurologique d'origine auto-immune, souvent associé à des anticorps anti-GAD. Aucun lien mécanistique direct n'est établi entre les actions connues de la metformine et cette pathologie.

Par prudence, la plausibilité mécanistique de cette prédiction doit être considérée comme faible.

## Autres Indications Prédites

| Rang | Maladie | Score TxGNN | Niveau de Preuve | Remarque |
|------|------|------|------|------|
| 2 | Syndrome de la personne raide classique | 0,9945 | L5 | Même logique de comorbidité avec le diabète ; aucun mécanisme direct |
| 3 | Opsismodysplasie | 0,9940 | L5 | Lien spéculatif via la voie PI3K/AKT (INPPL1/SHIP2) et l'AMPK/mTOR |
| 4 | Syndrome de dysfonction répondant à la thiamine | 0,9940 | L5 | Lien indirect (phénotype diabétique, transporteurs) ; le traitement reste la thiamine |
| 5 | Lipodystrophie localisée d'origine médicamenteuse | 0,9906 | L5 | La plus plausible sur le plan biologique (sensibilité à l'insuline), mais sans données pour cette forme |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Le texte de l'indication approuvée n'est pas renseigné pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 68196071 | METFORMINE VIATRIS 500 mg | Comprimé pelliculé | Active |
| 61232102 | STAGID 700 mg | Comprimé sécable | Active |
| 61048305 | METFORMINE EG LABO 500 mg | Comprimé pelliculé | Active |
| 60915020 | METFORMINE VIATRIS 1000 mg | Comprimé pelliculé sécable | Active |
| 67231181 | METFORMINE EG LABO 850 mg | Comprimé pelliculé | Active |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, maladie rénale, pancréatite, maladie de la vésicule biliaire, insuffisance cardiaque congestive, insuffisance corticosurrénale, ainsi que plusieurs déficits hypophysaires et hypogonadismes hypogonadotropes (dont le syndrome de Kallmann et le syndrome de Sheehan).
- **Interactions médicamenteuses** : 642 interactions recensées. Parmi les exemples relevés :
  - *Majeures* : acétazolamide, éthanol
  - *Modérées* : dolutégravir, abémaciclib, phényléphrine, ranitidine, formotérol, pseudoéphédrine, kétorolac, nifédipine, épinéphrine, ibuprofène, éthinylestradiol, hydrocortisone, salbutamol, hydrochlorothiazide, acétohexamide
  - *Mineures* : acarbose, corticoïdes topiques (hydrocortisone, alclométasone)

Les mises en garde et contre-indications issues de la notice ANSM ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et aucun mécanisme plausible n'est identifié pour le syndrome du membre raide focal.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de la notice ANSM (mises en garde et contre-indications), actuellement bloquantes pour le criblage de sécurité
- Données détaillées sur le mécanisme d'action (via DrugBank)
- Revue de la littérature et des registres d'essais ciblée sur la metformine et le spectre du syndrome de la personne raide
- Si une piste est à poursuivre, envisager en priorité la lipodystrophie localisée d'origine médicamenteuse (rang 5), mécanistiquement la plus plausible, après une recherche de preuves dédiée

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Metformin Hydrochloride Er (metformin hydrochloride) prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3dca884d-ec44-496f-9eeb-31fd8fa3f574) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

