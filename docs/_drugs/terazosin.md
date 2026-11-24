---
layout: default
title: Terazosin
parent: Prédiction du modèle uniquement (L5)
nav_order: 742
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Terazosin : nouvelle indication prédite, Hypotrichose simple du cuir chevelu (niveau de preuve L5). Indication d'origine : Hypertension artérielle…"
monitor_inn: "terazosin"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine disorder", "migraine with brainstem aura", "Raynaud disease", "Ambras type hypertrichosis universalis congenita", "manic bipolar affective disorder", "kyphoscoliotic heart disease"]
---

# Terazosin
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

## Terazosine : De l'Hypertension à l'Hypotrichose simple du cuir chevelu
{: .text-alpha }

## Resume en Une Phrase

La terazosine est un alpha-1 bloquant, initialement utilisé pour le traitement de l'hypertension artérielle et de l'hyperplasie bénigne de la prostate.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypotrichose simple du cuir chevelu** (rang 1), mais cette prédiction repose uniquement sur le modèle, sans aucun essai clinique ni publication.
Parmi les autres pistes prédites, la **maladie de Raynaud** est la mieux documentée, avec **1 publication** de 1997, et la **migraine** dispose de **2 publications** anciennes.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle, hyperplasie bénigne de la prostate (texte d'indication de l'AMM non disponible) |
| Nouvelle Indication Predite | Hypotrichose simple du cuir chevelu |
| Score de Prediction TxGNN | 0,9997 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 6 sur 7) |
| Nombre d'AMM | 7 (valides : 6) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Terazosin (traduction non officielle) : « Hyperplasie bénigne de la prostate Les symptômes associés à l'hyperplasie bénigne de la prostate (HBP) sont liés à une obstruction du col vésical, qui comprend deux composantes sous-jacentes : statique et dynamique. La composante statique est liée à une augmentation du volume de la prostate causée, en partie, par une prolifération des cellules musculaires lisses du stroma prostatique. […] Le blocage du récepteur alpha-1 diminue la résistance urétrale et peut lever l'obstruction des symptômes de l'HBP et améliorer le débit urinaire Hypertension Le mécanisme d'action de la térazosine est le blocage sélectif du sous-type alpha-1 des récepteurs adrénergiques. » Texte original en anglais : "Benign Prostatic Hyperplasia The symptoms associated with benign prostatic hyperplasia (BPH) are related to bladder outlet obstruction, which is comprised of two underlying components: static and dynamic. The static component is related to an increase in prostate size caused, in part by a proliferation of smooth muscle cells in the prostatic stroma. […] Blockade of the alpha-1 receptor decreases urethral resistance and may relieve the obstruction of BPH symptoms and improve urine flow Hypertension The mechanism of action of terazosin is selective blockade of the alpha-1 subtype of adrenergic receptors." ([DailyMed: Tezruly (terazosin) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=69582e0c-6569-490c-8c14-999f3750336f), version du 2025-04-18 ; consulté le 2026-11-19). Sur la base des informations connues, la terazosine est un alpha-1 bloquant adrénergique à activité vasodilatatrice. Son efficacité dans l'hypertension et l'hyperplasie bénigne de la prostate est établie.

Pour l'hypotrichose du cuir chevelu, le lien mécanistique reste très spéculatif : on pourrait imaginer un effet via la perfusion du follicule pileux, mais aucune donnée ne le soutient. Il s'agit d'une affection héréditaire, et le score élevé provient du modèle TxGNN (deep learning) : il peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

Parmi les autres prédictions, deux pistes ont un fondement plus plausible. La maladie de Raynaud : le blocage alpha-1 réduit la vasoconstriction sympathique, ce qui est biologiquement cohérent. La migraine : une modulation du tonus vasculaire adrénergique a été évoquée. Pour l'alopécie au sens large, une seule revue sur les effets extracardiaques des médicaments cardiovasculaires est disponible. Elle est indirecte et centrée sur le minoxidil, non sur la terazosine.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

Aucune littérature associée disponible actuellement pour l'hypotrichose simple du cuir chevelu. Les publications ci-dessous concernent des indications prédites voisines ou alternatives :

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [9273472](https://pubmed.ncbi.nlm.nih.gov/9273472/) | 1997 | Étude clinique (conception à vérifier) | Minerva Cardioangiologica | Raynaud : diminution du nombre, de l'intensité et de la durée des crises vasospastiques, avec amélioration des examens télethermographiques et échographiques |
| [7911406](https://pubmed.ncbi.nlm.nih.gov/7911406/) | 1994 | Étude clinique ouverte (petite, conception peu claire) | La Clinica Terapeutica | Migraine sans aura : 46 patients, dont 10 sous terazosine, évalués pour une activité prophylactique |
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Revue / série de cas | Headache | Prophylaxie de la migraine : amélioration chez presque tous les 10 patients traités par terazosine ou doxazosine, mais 5 arrêts pour effets indésirables |
| [34779371](https://pubmed.ncbi.nlm.nih.gov/34779371/) | 2022 | Revue | Current Cardiology Reviews | Effets extracardiaques des médicaments cardiovasculaires, dont des effets capillaires ; lien indirect, surtout lié au minoxidil |

## Informations de Marche en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 60376815 | HYTRINE 1 mg, comprimé | Comprimé | AMDIPHARM | Active |
| 66297890 | HYTRINE 5 mg, comprimé | Comprimé | AMDIPHARM | Active |
| 62446447 | DYSALFA 1 mg, comprimé | Comprimé | AMDIPHARM | Active |
| 62866910 | TERAZOSINE BIOGARAN 5 mg, comprimé | Comprimé | BIOGARAN | Active |
| 64171583 | TERAZOSINE TEVA 5 mg, comprimé | Comprimé | TEVA SANTE | Active |
| 66227027 | DYSALFA 5 mg, comprimé | Comprimé | AMDIPHARM | Active |
| 65566430 | TERAZOSINE MYLAN 5 mg, comprimé | Comprimé | MYLAN SAS | Abrogée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, hypotension orthostatique, priapisme, syndrome de l'iris hypotonique peropératoire.
- **Interactions médicamenteuses** : 137 interactions recensées. Les principales, de niveau modéré, concernent les corticoïdes (hydrocortisone, prednisone, prednisolone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), les inhibiteurs du SGLT2 (canagliflozine, dapagliflozine, empagliflozine, ertugliflozine), les opioïdes (morphine, morphine liposomale, opium), le bupropion, ainsi que les cannabinoïdes (dronabinol, nabilone). Des interactions de niveau inconnu sont signalées avec le calcitriol, le pantoprazole et le glimépiride.
- Le profil connu de la classe (hypotension, vertiges) est pertinent pour toute évaluation de sécurité initiale, notamment dans la maladie de Raynaud.

Veuillez consulter la notice pour les mises en garde détaillées, qui ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- L'indication principale prédite (hypotrichose simple du cuir chevelu) repose uniquement sur le score du modèle (niveau L5), sans essai ni publication, et sans mécanisme plausible.
- Les pistes les plus intéressantes sont la maladie de Raynaud (niveau L3, « Research Question ») et la migraine (niveau L4, « Research Question »), mais les preuves sont anciennes et de faible qualité.

<!-- review:begin fr-lic-20261106-terazosin-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « L'indication principale prédite (hypotrichose simple du cuir chevelu) repose uniquement sur le score du modèle (niveau L5), sans essai ni publication, et sans mécanisme plausible. Les produits français sont en outre tous annulés. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-terazosin-1 -->

**Pour avancer, les elements suivants sont necessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le dépistage de sécurité)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Pour la maladie de Raynaud : vérifier la conception et l'effectif de l'étude de 1997 et rechercher des essais contrôlés plus récents
- Pour la migraine : des données contrôlées modernes avant toute considération au-delà de la génération d'hypothèses
- Une étude préclinique ou mécanistique sur les follicules pileux avant d'envisager une indication capillaire
- Une clarification du statut réglementaire, puisque la plupart des AMM françaises sont valides (statut des AMM : voir l'Aperçu rapide)

<!-- review:begin fr-lic-20261124-terazosin-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « puisque les 2 AMM françaises sur 2 sont valides » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans l'Aperçu rapide. Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés : le nombre et le statut à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché, générés à partir des données BDPM. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-terazosin-1 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Les produits français sont en outre tous annulés » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Tezruly (terazosin) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=69582e0c-6569-490c-8c14-999f3750336f) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

