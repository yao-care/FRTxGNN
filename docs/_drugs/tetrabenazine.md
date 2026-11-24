---
layout: default
title: Tetrabenazine
parent: Prédiction du modèle uniquement (L5)
nav_order: 748
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "tetrabenazine"
predicted_indications: ["polycystic kidney disease 3 with or without polycystic liver disease", "renal-hepatic-pancreatic dysplasia", "Joubert syndrome with renal defect", "karyomegalic interstitial nephritis", "thoracic malformation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "acute intermittent porphyria", "adult familial nephronophthisis-spastic quadriparesia syndrome", "atypical glycine encephalopathy", "congenital disorder of glycosylation with defective fucosylation"]
description: "Tetrabenazine : nouvelle indication prédite, Polycystic kidney disease 3 with or without polycystic liver disease (niveau de preuve L5). En France, AMM dans la BDPM : 2 (valides : 2)"
---

# Tetrabenazine
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

## Tetrabenazine: Polycystic kidney disease 3 with or without polycystic liver disease
{: .text-alpha }

## Résumé en Une Phrase

La tétrabénazine est un médicament initialement utilisé pour traiter les mouvements anormaux de la maladie de Huntington et de syndromes apparentés.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie rénale polykystique de type 3 (avec ou sans maladie polykystique du foie)**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Polycystic kidney disease 3 with or without polycystic liver disease |
| Score de Prédiction TxGNN | 0.9990 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Tetrabenazine (traduction non officielle) : « Le mécanisme précis par lequel XENAZINE (tétrabénazine) exerce ses effets anti-chorée est inconnu, mais on pense qu'il est lié à son effet de déplétion réversible des monoamines (telles que la dopamine, la sérotonine, la noradrénaline et l'histamine) des terminaisons nerveuses. La tétrabénazine inhibe de manière réversible le transporteur vésiculaire des monoamines humain de type 2 (VMAT2) (K i ≈ 100 nM), ce qui entraîne une diminution de la recapture des monoamines dans les vésicules synaptiques et une déplétion des réserves de monoamines. » Texte original en anglais : "The precise mechanism by which XENAZINE (tetrabenazine) exerts its anti-chorea effects is unknown but is believed to be related to its effect as a reversible depletor of monoamines (such as dopamine, serotonin, norepinephrine, and histamine) from nerve terminals. Tetrabenazine reversibly inhibits the human vesicular monoamine transporter type 2 (VMAT2) (K i ≈ 100 nM), resulting in decreased uptake of monoamines into synaptic vesicles and depletion of monoamine stores." ([DailyMed: Xenazine (tetrabenazine) prescribing information, Lundbeck Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac768bab-8afa-4446-bc7f-caeeffec0cda), version du 2026-11-06 ; consulté le 2026-11-19). D'après les connaissances générales, la tétrabénazine est un inhibiteur réversible du transporteur vésiculaire des monoamines de type 2 (VMAT2) : elle déplète les monoamines présynaptiques (dopamine notamment) et soulage ainsi de façon symptomatique les mouvements hyperkinétiques.

La relation entre l'indication originale (trouble moteur neurologique) et la nouvelle indication (maladie rénale/hépatique kystique d'origine génétique, de type ciliopathie) n'est pas évidente. Aucun lien mécanistique plausible entre l'inhibition de VMAT2 et la physiopathologie de la polykystose rénale n'a été identifié.

Le score élevé de TxGNN (0,9990) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique ou clinique. Cette prédiction doit donc être considérée avec une grande prudence. Les autres prédictions du même classement (dysplasie rénale-hépatique-pancréatique, syndrome de Joubert avec atteinte rénale, néphrite interstitielle karyomégalique, etc.) présentent le même profil : niveau L5, sans essai ni publication pertinente.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour cette indication.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 64487229 | TETMODIS 25 mg, comprimé sécable | Comprimé sécable | WALTER RITTER (ALLEMAGNE) | Active |
| 62463044 | XENAZINE 25 mg, comprimé sécable | Comprimé sécable | BAUSCH HEALTH IRELAND (IRLANDE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, hypotension orthostatique et troubles hypotensifs, syndrome du QT long (y compris familial) et torsades de pointes, troubles anxieux, troubles névrotiques et dysthymie, maladie hépatique, maladie de la vésicule biliaire, dyskinésie tardive et dyskinésie linguo-faciale-buccale, syndrome parkinsonien et maladie de Parkinson, akathisie induite par les médicaments, hyperprolactinémie (y compris familiale ou acquise) et tumeur hypophysaire sécrétant de la prolactine.
- **Interactions médicamenteuses** : 168 interactions recensées. Parmi les principales :
  - Majeures : bupropion, dolasétron, métoclopramide
  - Modérées : famotidine, lopéramide, morphine, lorcasérine, clarithromycine, lévofloxacine, dronabinol, éliglustat, palonosétron, nabilone, diphénoxylate, difénoxine, ainsi que plusieurs laxatifs/préparations de lavage intestinal (bisacodyl, acide picosulfurique, polyéthylène glycol avec électrolytes, sulfate de sodium)
  - Mineure : métronidazole

Veuillez consulter la notice pour les informations de sécurité détaillées (mises en garde et contre-indications officielles non disponibles dans les données compilées).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et aucun lien mécanistique plausible n'existe entre l'inhibition de VMAT2 et la polykystose rénale. De plus, le médicament n'a actuellement plus d'AMM valide en France, et son profil de sécurité (dépression, QT long, contre-indication en cas de maladie hépatique) est préoccupant.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (MOA) détaillé, afin d'évaluer un éventuel lien mécanistique
- Mises en garde et contre-indications officielles issues de la notice de l'ANSM
- Données précliniques (modèles de ciliopathie ou de polykystose) justifiant un intérêt biologique
- Clarification du statut réglementaire et de la voie d'accès éventuelle
- Évaluation du rapport bénéfice/risque dans une population à atteinte rénale et/ou hépatique

<!-- review:begin fr-lic-20261106-tetrabenazine-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarification du statut réglementaire (AMM annulées) et de la voie d'accès éventuelle » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-tetrabenazine-1 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « (AMM annulées) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Xenazine (tetrabenazine) prescribing information, Lundbeck Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ac768bab-8afa-4446-bc7f-caeeffec0cda) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

