---
layout: default
title: Levothyroxine
parent: Prédiction du modèle uniquement (L5)
nav_order: 451
evidence_level: L5
indication_count: 4
monitor_inn: "levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-11-24
description: "Levothyroxine : nouvelle indication prédite, Hypoplasie/aplasie rénale (niveau de preuve L5). Indication d'origine : Hypothyroïdie"
---

# Levothyroxine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

## Lévothyroxine : De l'hypothyroïdie à l'hypoplasie/aplasie rénale
{: .text-alpha }

## Résumé en Une Phrase

La lévothyroxine est une hormone thyroïdienne de substitution, utilisée à l'origine pour traiter l'hypothyroïdie et d'autres maladies de la thyroïde.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypoplasie/aplasie rénale**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypothyroïdie (relation enregistrée dans le graphe de connaissances ; les textes d'indication des AMM ne sont pas renseignés dans les données compilées) |
| Nouvelle Indication Prédite | Hypoplasie/aplasie rénale |
| Score de Prédiction TxGNN | 0,9967 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Levothyroxine (traduction non officielle) : « Les hormones thyroïdiennes exercent leurs actions physiologiques par le contrôle de la transcription de l'ADN et de la synthèse des protéines. La triiodothyronine (T3) et la L-thyroxine (T4) diffusent dans le noyau cellulaire et se lient aux protéines réceptrices thyroïdiennes fixées à l'ADN. » Texte original en anglais : "Thyroid hormones exert their physiologic actions through control of DNA transcription and protein synthesis. Triiodothyronine (T3) and L-thyroxine (T4) diffuse into the cell nucleus and bind to thyroid receptor proteins attached to DNA." ([DailyMed: Levoxyl (levothyroxine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=758588c3-c63e-491b-0aa2-4f50d80cb174), version du 2026-11-06 ; consulté le 2026-11-19). Sur la base des informations connues, la lévothyroxine est une forme synthétique de la thyroxine (T4), dont l'efficacité dans l'hypothyroïdie est établie. Les hormones thyroïdiennes jouent un rôle général dans le développement et la maturation de plusieurs organes, dont le rein.

Cependant, ce lien reste très faible. L'hypoplasie/aplasie rénale est un défaut du développement, le plus souvent d'origine génétique (par exemple PAX2, HNF1B, RET), qu'une hormone administrée après la naissance ne peut pas raisonnablement corriger. Le score élevé du modèle (0.9967) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées (rénales et thyroïdiennes), et non une preuve biologique ni un mécanisme thérapeutique validé.

D'autres prédictions du modèle (agénésie rénale bilatérale, séquence de Potter, complexe de Carney) présentent les mêmes limites : aucune preuve clinique, et une plausibilité biologique faible ou indirecte.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

La liste ci-dessous porte sur 5 des AMM de spécialités à base de lévothyroxine seule ; la liste complète peut comporter davantage d'AMM. Les textes d'indication approuvée ne sont pas renseignés dans les données compilées.

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 66426100 | LEVOTHYROX 112 microgrammes, comprimé sécable | Comprimé sécable | MERCK SANTE | Active |
| 65706277 | L-THYROXIN HENNING 137 microgrammes, comprimé sécable | Comprimé sécable | SANOFI WINTHROP INDUSTRIE | Active |
| 60254754 | TSOLUDOSE 150 microgrammes, solution buvable en récipient unidose | Solution buvable | IBSA PHARMA SAS | Active |
| 61296560 | TCAPS 137 microgrammes, capsule molle | Capsule molle | IBSA PHARMA SAS | Active |
| 64952190 | THYROFIX 125 microgrammes, comprimé | Comprimé | UNI-PHARMA KLEON TSETIS PHARMACEUTICAL LABORATORIES (GRECE) | Active |
| 68265172 | THYROFIX 25 microgrammes, comprimé | Comprimé | UNI-PHARMA KLEON TSETIS PHARMACEUTICAL LABORATORIES (GRECE) | Active |
| 62630116 | THYROFIX 150 microgrammes, comprimé | Comprimé | UNI-PHARMA KLEON TSETIS PHARMACEUTICAL LABORATORIES (GRECE) | Active |
| 65633434 | THYROFIX 137 microgrammes, comprimé | Comprimé | UNI-PHARMA KLEON TSETIS PHARMACEUTICAL LABORATORIES (GRECE) | Active |
| 68283252 | LEVOTHYROX 175 microgrammes, comprimé sécable | Comprimé sécable | MERCK SANTE | Active |
| 68588503 | LEVOTHYROX 25 microgrammes, comprimé sécable | Comprimé sécable | MERCK SANTE | Active |
| 60441558 | TCAPS 88 microgrammes, capsule molle | Capsule molle | IBSA PHARMA SAS | Active |
| 64826590 | THYROFIX 75 microgrammes, comprimé | Comprimé | UNI-PHARMA KLEON TSETIS PHARMACEUTICAL LABORATORIES (GRECE) | Active |
| 65845654 | TCAPS 150 microgrammes, capsule molle | Capsule molle | IBSA PHARMA SAS | Active |
| 62953888 | THYROFIX 62 microgrammes, comprimé | Comprimé | UNI-PHARMA KLEON TSETIS PHARMACEUTICAL LABORATORIES (GRECE) | Active |
| 67686072 | L-THYROXIN HENNING 200 microgrammes, comprimé sécable | Comprimé sécable | SANOFI WINTHROP INDUSTRIE | Active |
| 62864489 | L-THYROXIN HENNING 63 microgrammes, comprimé sécable | Comprimé sécable | SANOFI WINTHROP INDUSTRIE | Active |
| 64067524 | LEVOTHYROX 150 microgrammes, comprimé sécable | Comprimé sécable | MERCK SANTE | Active |
| 65315798 | LEVOTHYROX 200 microgrammes, comprimé sécable | Comprimé sécable | MERCK SANTE | Active |
| 60210811 | TCAPS 13 microgrammes, capsule molle | Capsule molle | IBSA PHARMA SAS | Active |
| 62513223 | L-THYROXIN HENNING 175 microgrammes, comprimé sécable | Comprimé sécable | SANOFI WINTHROP INDUSTRIE | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.
Les données ne contiennent qu'une partie des autorisations ; la liste peut être incomplète.

<!-- licenses:end -->

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Contre-indications enregistrées dans le graphe de connaissances** (relations du graphe, et non texte de la notice) : hypertension, déficits hypophysaires (dont hypopituitarisme et syndrome de Sheehan), hypogonadisme hypogonadotrope et syndrome de Kallmann, maladies du thymus, ostéoporose (dont post-ménopausique), diabète et acidocétose diabétique, maladie coronarienne et infarctus du myocarde.
- **Interactions médicamenteuses** : 666 interactions recensées. Parmi les principales, de niveau modéré : antidiabétiques (metformine, pioglitazone, acarbose, canagliflozine, dapagliflozine, empagliflozine, alogliptine, albiglutide, dulaglutide, chlorpropamide), inhibiteurs de la pompe à protons (oméprazole, rabéprazole, dexlansoprazole), sels de calcium et de magnésium (phosphate et acétate de calcium, oxyde de magnésium), épinéphrine, isométheptène et diéthylpropion. L'interaction avec la cimétidine est de niveau mineur.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (L5) : aucun essai clinique ni publication n'étudie cette maladie, et le lien biologique est peu plausible pour une malformation structurelle congénitale.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action de la lévothyroxine
- Mises en garde et contre-indications issues de la notice de l'ANSM
- Preuves précliniques ou cliniques directement liées à l'hypoplasie/aplasie rénale
- Justification mécanistique expliquant comment une hormone thyroïdienne pourrait agir sur un défaut de développement rénal

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Levoxyl (levothyroxine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=758588c3-c63e-491b-0aa2-4f50d80cb174) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

