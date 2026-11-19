---
layout: default
title: Fluorescein
parent: Prédiction du modèle uniquement (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Fluorescein : nouvelle indication prédite, Angor de Prinzmetal (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM disponibles"
monitor_inn: "fluorescein"
predicted_indications: ["Prinzmetal angina", "antithrombin deficiency type 2", "rheumatoid arthritis", "factor 5 excess with spontaneous thrombosis", "hemoglobinopathy", "heparin cofactor 2 deficiency", "thrombophilia", "hyperthyroidism", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations"]
---

# Fluorescein
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

## Fluorescéine : De l'usage diagnostique ophtalmique à l'angor de Prinzmetal
{: .text-alpha }

## Résumé en Une Phrase

La fluorescéine est un colorant fluorescent à usage diagnostique, utilisé en ophtalmologie (collyre et solution injectable pour l'angiographie). Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**angor de Prinzmetal**, mais **aucun essai clinique** ni **aucune publication** ne soutient cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM disponibles |
| Nouvelle Indication Prédite | Angor de Prinzmetal |
| Score de Prédiction TxGNN | 0,9981 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Fluorescein (traduction non officielle) : « La fluorescéine sodique réagit aux rayonnements électromagnétiques et à la lumière de longueurs d'onde comprises entre 465 et 490 nm et émet une fluorescence, c'est-à-dire qu'elle émet de la lumière à des longueurs d'onde de 520 à 530 nm. Ainsi, l'hydrocarbure est excité par la lumière bleue et émet une lumière qui apparaît vert jaunâtre. » Texte original en anglais : "Fluorescein sodium responds to electromagnetic radiation and light between the wavelengths of 465 to 490 nm and fluoresces, i.e., emits light at wavelengths of 520 to 530 nm. Thus, the hydrocarbon is excited by blue light and emits light that appears yellowish green." ([DailyMed: Ak-Fluor (fluorescein) prescribing information, Long Grove Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=73511e79-c050-4dc0-aa2f-a79ed320b5b0), version du 2026-02-26 ; consulté le 2026-11-19). La fluorescéine est un colorant diagnostique fluorescent, utilisé pour visualiser la surface oculaire et la vascularisation rétinienne. Elle n'est pas connue pour avoir une action thérapeutique.

Le lien mécanistique avec l'angor de Prinzmetal n'est **pas établi** : la fluorescéine n'a aucune action vasodilatatrice ou anti-vasospastique connue. Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique ou une plausibilité pharmacologique. Cette prédiction doit donc être considérée avec une grande prudence.

Les autres indications prédites (déficit en antithrombine de type 2, polyarthrite rhumatoïde, excès de facteur V, hémoglobinopathie, déficit en cofacteur II de l'héparine, thrombophilie, hyperthyroïdie, délétion partielle du bras court du chromosome 16, bêta-thalassémie) présentent le même constat : aucun lien pharmacologique plausible. Pour la polyarthrite rhumatoïde, l'hémoglobinopathie, la thrombophilie et l'hyperthyroïdie, la littérature retrouvée décrit uniquement l'usage diagnostique de la fluorescéine (coloration de la surface oculaire, angiographie) dans les manifestations oculaires de ces maladies, et non un effet thérapeutique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'angor de Prinzmetal.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 69497711 | Fluorescéine Faure 0,5 pour cent, collyre en solution en récipient unidose | Collyre en solution | Non renseignée | Active |
| 63233249 | Fluocyne 10 %, solution injectable I.V. | Solution injectable | Non renseignée | Active |
| 63485289 | Fluorescéine sodique Faure 10 pour cent, solution injectable | Solution injectable | Non renseignée | Active |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible entre un colorant diagnostique et l'angor de Prinzmetal.
- Les données de sécurité de la notice ne sont pas disponibles.

<!-- review:begin fr-lic-20261106-fluorescein-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les trois AMM françaises sont annulées, et les données de sécurité de la notice ne sont pas disponibles. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 3 AMM pour ce médicament, dont 3 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-fluorescein-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération des mises en garde et contre-indications de la notice (ANSM)
- Données détaillées sur le mécanisme d'action (DrugBank)
- Démonstration d'un rationnel pharmacologique pour l'indication visée, puis études précliniques avant toute évaluation clinique
- Clarification de l'indication originale d'après les AMM

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « es trois AMM françaises sont annulées, et l » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Ak-Fluor (fluorescein) prescribing information, Long Grove Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=73511e79-c050-4dc0-aa2f-a79ed320b5b0) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

