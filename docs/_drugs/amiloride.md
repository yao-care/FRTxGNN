---
layout: default
title: Amiloride
parent: Prédiction du modèle uniquement (L5)
nav_order: 56
evidence_level: L5
indication_count: 5
monitor_inn: "AMILORIDE"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-24
description: "Amiloride : nouvelle indication prédite, Maladie rénale hypertensive maligne (malignant hypertensive renal disease) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données local…"
---

# Amiloride
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

## Amiloride : bloqueur du canal sodique épithélial (ENaC), diurétique épargneur de potassium → maladie rénale hypertensive maligne (malignant hypertensive renal disease)
{: .text-alpha }

## Résumé en Une Phrase

L'amiloride est un diurétique épargneur de potassium qui agit sur le canal sodique épithélial du néphron distal.
Le modèle TxGNN prédit qu'il pourrait être utile dans la **maladie rénale hypertensive maligne (malignant hypertensive renal disease)**, mais aucun essai clinique ni aucune publication ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Maladie rénale hypertensive maligne (malignant hypertensive renal disease) |
| Score de Prédiction TxGNN | 0,9982 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Amiloride (traduction non officielle) : « Le chlorhydrate d'amiloride est un médicament épargneur de potassium (antikaliurétique) qui possède une activité natriurétique, diurétique et antihypertensive faible (par rapport aux diurétiques thiazidiques). Ces effets se sont partiellement additionnés à ceux des diurétiques thiazidiques dans certaines études cliniques. » Texte original en anglais : "Amiloride HCl is a potassium-conserving (antikaliuretic) drug that possesses weak (compared with thiazide diuretics) natriuretic, diuretic, and antihypertensive activity. These effects have been partially additive to the effects of thiazide diuretics in some clinical studies." ([DailyMed: amiloride hydrochloride prescribing information, Kesin Pharma Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5eedadbd-9be9-b920-e063-6394a90afa68), version du 2026-11-11 ; consulté le 2026-11-19). D'après les connaissances pharmacologiques générales, l'amiloride bloque le canal sodique épithélial (ENaC) du néphron distal, ce qui diminue la réabsorption du sodium et contribue au contrôle de la pression artérielle tout en épargnant le potassium.

Ce mécanisme est plausiblement lié à une atteinte rénale d'origine hypertensive, puisque la maîtrise de la pression artérielle et de la volémie est centrale dans ce contexte. Le score élevé du modèle (0,9982) reflète probablement une proximité avec les usages antihypertenseurs du médicament plutôt qu'une preuve propre à la forme maligne et rénale.

Aucun essai ni publication n'a été fourni pour cette présentation précise ; le lien reste donc hypothétique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63371015 | MODAMIDE 5 mg, comprimé | comprimé | Non renseignée |
| 63824615 | LOGIRENE, comprimé sécable | comprimé sécable | Non renseignée |
| 64343809 | MODUCREN, comprimé | comprimé | Non renseignée |

## Considérations de Sécurité

- **Contre-indications** : les données compilées ne contiennent pas de texte de notice. À titre indicatif uniquement (relations de contre-indication issues de bases de données, et non du libellé officiel), des situations telles que l'insuffisance rénale, l'anurie, les maladies hépatiques, le diabète, la déficience en potassium, l'acidose et la goutte sont signalées comme à risque.
- **Interactions médicamenteuses** : 100 interactions sont recensées. Parmi celles de niveau modéré : metformine, hydrocortisone, bétaméthasone, dexaméthasone, budésonide, bupropion, canagliflozine, dapagliflozine, empagliflozine, ertugliflozine, exénatide, lactulose. Parmi celles de niveau mineur : doxycycline, amoxicilline, cimétidine.
- Une surveillance de la kaliémie et de la fonction rénale est essentielle (risque d'hyperkaliémie).

Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication portant sur la maladie rénale hypertensive maligne. Le profil de sécurité (hyperkaliémie, atteinte rénale) impose une prudence particulière dans cette population.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action
- Texte de la notice ANSM (mises en garde et contre-indications)
- Études précliniques ou cliniques ciblant la maladie rénale hypertensive maligne
- Évaluation du risque d'hyperkaliémie chez les patients à fonction rénale altérée

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: amiloride hydrochloride prescribing information, Kesin Pharma Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5eedadbd-9be9-b920-e063-6394a90afa68) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

