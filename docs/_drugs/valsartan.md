---
layout: default
title: Valsartan
parent: Preuves modérées (L3-L4)
nav_order: 803
evidence_level: L4
indication_count: 6
last_modified_at: 2026-11-20
monitor_inn: "VALSARTAN"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "Prinzmetal angina"]
description: "Valsartan : nouvelle indication prédite, Maladie rénale hypertensive maligne (malignant hypertensive renal disease) (niveau de preuve L4). Indication d'origine : Non renseignée dans les données local…"
---

# Valsartan
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **6** 
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

## Valsartan: Maladie rénale hypertensive maligne (malignant hypertensive renal disease)
{: .text-alpha }

## Résumé en Une Phrase

Valsartan est un antagoniste des récepteurs de l'angiotensine II (type AT1), initialement utilisé pour le traitement de l'hypertension artérielle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie rénale hypertensive maligne**, mais aucun essai clinique n'est enregistré et une seule publication préclinique, portant sur un autre médicament (l'avosentan), est disponible : le niveau de preuve est donc faible.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Maladie rénale hypertensive maligne (malignant hypertensive renal disease) |
| Score de Prédiction TxGNN | 0.9997 |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Valsartan (traduction non officielle) : « L'angiotensine II est formée à partir de l'angiotensine I au cours d'une réaction catalysée par l'enzyme de conversion de l'angiotensine (ECA, kininase II). L'angiotensine II est le principal agent vasopresseur du système rénine-angiotensine, avec des effets qui comprennent la vasoconstriction, la stimulation de la synthèse et de la libération d'aldostérone, la stimulation cardiaque et la réabsorption rénale du sodium. […] Diovan (valsartan) bloque les effets vasoconstricteurs et de sécrétion d'aldostérone de l'angiotensine II en bloquant sélectivement la liaison de l'angiotensine II au récepteur AT 1 dans de nombreux tissus, tels que le muscle lisse vasculaire et la glande surrénale. » Texte original en anglais : "Angiotensin II is formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the principal pressor agent of the renin-angiotensin system, with effects that include vasoconstriction, stimulation of synthesis and release of aldosterone, cardiac stimulation, and renal reabsorption of sodium. […] Diovan (valsartan) blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively blocking the binding of angiotensin II to the AT 1 receptor in many tissues, such as vascular smooth muscle and the adrenal gland." ([DailyMed: Diovan (valsartan) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ddba454-f3e6-43c2-a7a6-58365d297213), version du 2026-08-11 ; consulté le 2026-11-19). Sur la base des informations connues, le valsartan est un bloqueur du récepteur AT1 de l'angiotensine II. Son efficacité dans l'hypertension est établie.

L'hypertension maligne avec atteinte rénale est liée à une forte activation du système rénine-angiotensine-aldostérone (SRAA). Le blocage du récepteur AT1 est donc mécanistiquement plausible, et cette indication est proche de l'indication antihypertensive d'origine.

Cependant, le soutien disponible reste indirect. La seule publication retrouvée concerne l'avosentan (un antagoniste de l'endothéline) dans la néphropathie hypertensive, chez le rat, et non le valsartan.

Deux autres pistes prédites ont un soutien un peu plus étayé : l'**hypertension rénovasculaire maligne** (une étude animale de 2001 montre que le blocage AT1 prévient l'hypertension maligne létale, mais sans données spécifiques au valsartan) et le **cœur pulmonaire chronique** (niveau L3, données surtout observationnelles et indirectes).

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour la maladie rénale hypertensive maligne.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Préclinique (animal) | Pharmacological Research | L'avosentan (antagoniste de l'endothéline, et non le valsartan) protège contre la néphropathie hypertensive chez le rat à des doses ne provoquant pas de rétention hydrique |

---

## Informations de Marché en France

Le texte d'indication approuvée n'est pas disponible pour ces AMM. Voici les cinq premières :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 67519721 | VALSARTAN EG 160 mg | Comprimé pelliculé sécable |
| 62518793 | TAREG 3 mg/ml | Solution buvable |
| 62435881 | VALSARTAN SANDOZ 80 mg | Comprimé pelliculé |
| 65471256 | VALSARTAN BIOGARAN 80 mg | Comprimé pelliculé sécable |
| 62582582 | VALSARTAN TEVA 160 mg | Comprimé pelliculé sécable |

---

## Considérations de Sécurité

- **Contre-indications (issues du graphe de connaissances, et non du texte de la notice)** : insuffisance hépatique et maladies hépatiques, encéphalopathie hépatique, pancréatite, maladie de la vésicule biliaire, angio-œdème (y compris héréditaire et induit par les bloqueurs du SRAA), lupus érythémateux systémique, carence en potassium, diabète et acidocétose diabétique, neutropénie et agranulocytose, hypotension, anurie, sténose ou obstruction de l'artère rénale, insuffisance rénale, goutte, hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore, hyperparathyroïdie, ostéite fibreuse et ictère néonatal.
- **Interactions médicamenteuses** : 100 interactions recensées. Les plus importantes sont de niveau **majeur** avec le **bicarbonate de potassium** et le **chlorure de potassium** (risque d'hyperkaliémie). De nombreuses interactions de niveau modéré concernent l'hydrocortisone, l'éluxadoline, l'exénatide et les différentes insulines (effet sur la glycémie), ainsi que le polyéthylène glycol avec électrolytes.
- **Point d'attention spécifique** : la sténose bilatérale des artères rénales est une précaution connue pour cette classe, ce qui est pertinent pour l'hypertension rénovasculaire.

Les mises en garde de la notice n'ont pas pu être consultées ; veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique n'est enregistré, et la seule publication retrouvée est un travail préclinique sur un autre médicament. Le niveau de preuve est L4 (mécanistique uniquement).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications) pour permettre l'évaluation de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Rechercher des études spécifiques au valsartan (précliniques puis cliniques) dans la maladie rénale hypertensive maligne.
- Clarifier la situation réglementaire en France (la plupart des AMM sont actives ; certaines sont abrogées ou archivées) et la compatibilité des voies d'administration.
- Envisager l'hypertension rénovasculaire maligne comme piste de suivi, en tenant compte de la précaution liée à la sténose bilatérale des artères rénales.

<!-- review:begin fr-lic-20261115-valsartan-1 -->

> **Correction de vérification (2026-11-15)**: Texte initial : « Clarifier la situation réglementaire en France (AMM annulées) » D’après la BDPM complète (CIS_bdpm et CIS_COMPO_bdpm, 2026-11-15), les spécialités contenant VALSARTAN comptent 130 AMM, dont 124 actives et 6 abrogées ou archivées. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_bdpm.txt); [Base de données publique des médicaments (BDPM) – CIS_COMPO_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_COMPO_bdpm.txt).

<!-- review:end fr-lic-20261115-valsartan-1 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-15 | « Clarifier la situation réglementaire en France (AM » → « Clarifier la situation réglementaire en France (la » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_bdpm.txt); [Base de données publique des médicaments (BDPM) – CIS_COMPO_bdpm](https://base-donnees-publique.medicaments.gouv.fr/download/file/CIS_COMPO_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Diovan (valsartan) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ddba454-f3e6-43c2-a7a6-58365d297213) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

