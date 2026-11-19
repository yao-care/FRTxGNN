---
layout: default
title: Liothyronine
parent: Prédiction du modèle uniquement (L5)
nav_order: 453
evidence_level: L5
indication_count: 9
monitor_inn: "LIOTHYRONINE"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Carney complex", "peripheral dysostosis", "Potter sequence", "acrodysostosis with or without hormone resistance", "angiomyxoma", "myxoma", "hypotrichosis simplex of the scalp"]
last_modified_at: 2026-11-12
description: "Liothyronine : nouvelle indication prédite, Hypoplasie/aplasie rénale (renal hypodysplasia/aplasia) (niveau de preuve L5). En France, AMM dans la BDPM : 1 (valides : 1)"
---

# Liothyronine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Liothyronine : hormone thyroïdienne (triiodothyronine, T3) → hypoplasie/aplasie rénale (renal hypodysplasia/aplasia)
{: .text-alpha }

## Résumé en Une Phrase

La liothyronine est une hormone thyroïdienne de synthèse (T3). Les données locales ne renseignent pas d'indication approuvée en France pour ce médicament.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypoplasie/aplasie rénale (renal hypodysplasia/aplasia)**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hypoplasie/aplasie rénale (renal hypodysplasia/aplasia) |
| Score de Prédiction TxGNN | 0,9995 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Liothyronine (traduction non officielle) : « Les hormones thyroïdiennes exercent leurs actions physiologiques par le contrôle de la transcription de l'ADN et de la synthèse des protéines. La triiodothyronine (T3) et la L-thyroxine (T4) diffusent dans le noyau cellulaire et se lient aux protéines réceptrices thyroïdiennes fixées à l'ADN. » Texte original en anglais : "Thyroid hormones exert their physiologic actions through control of DNA transcription and protein synthesis. Triiodothyronine (T3) and L-thyroxine (T4) diffuse into the cell nucleus and bind to thyroid receptor proteins attached to DNA." ([DailyMed: Cytomel (liothyronine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51452b31-ff68-4e0c-b982-c15502ebf1d3), version du 2026-05-18 ; consulté le 2026-11-19). La liothyronine est la forme active de l'hormone thyroïdienne (T3) : elle se fixe sur les récepteurs nucléaires des hormones thyroïdiennes et régule l'expression de nombreux gènes impliqués dans le métabolisme et le développement.

Les hormones thyroïdiennes jouent un rôle général dans le développement des organes, dont le rein. Toutefois, aucun lien mécanistique direct n'est établi avec le traitement de l'hypoplasie/aplasie rénale, qui est une malformation structurelle congénitale. Un médicament administré après la naissance a peu de chances d'inverser une telle anomalie.

Le score élevé du modèle (0,9995) reste donc une simple prédiction, sans confirmation clinique ni documentaire.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour cette indication.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69081937 | EUTHYRAL 100 microgrammes/20 microgrammes, comprimé sécable | Comprimé sécable | Non renseignée |

Cette AMM correspond à un produit associant deux principes actifs (100 µg/20 µg) ; elle ne décrit pas l'autorisation de la liothyronine seule.

<!-- review:begin fr-lic-20261106-liothyronine-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Cette AMM correspond à un produit associant deux principes actifs (100 µg/20 µg) ; elle ne décrit pas l'autorisation de la liothyronine seule. Le statut de cette AMM est enregistré comme annulé dans les données locales. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-liothyronine-1 -->

## Considérations de Sécurité

- **Contre-indications à surveiller (relations de contre-indication issues des données de modélisation, hors texte de notice)** : hypertension artérielle, déficits hypophysaires (hypopituitarisme, syndrome de Sheehan, déficit en hormone de croissance), hypogonadisme hypogonadotrope (dont syndrome de Kallmann), ostéoporose (y compris post-ménopausique), diabète et acidocétose diabétique, maladie coronarienne et infarctus du myocarde, maladie du thymus.
- **Interactions médicamenteuses** (100 interactions recensées, exemples de niveau modéré) : antidiabétiques (metformine, pioglitazone, canagliflozine, dapagliflozine, empagliflozine, linagliptine, alogliptine, chlorpropamide, acarbose, albiglutide, dulaglutide), inhibiteurs de la pompe à protons (oméprazole, rabéprazole, dexlansoprazole), sels de calcium et de magnésium (phosphate de calcium, acétate de calcium, oxyde de magnésium), et sympathomimétiques (épinéphrine, isométheptène, diéthylpropion).

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles : veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle, sans essai clinique ni publication portant sur l'hypoplasie/aplasie rénale. Il n'existe pas de justification pharmacologique plausible pour une malformation congénitale structurelle.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données mécanistiques montrant un rôle de la T3 dans la néphrogenèse pertinent pour cette malformation
- Études précliniques ou cliniques portant directement sur cette maladie
- Mises en garde et contre-indications issues de la notice officielle (ANSM)
- Données détaillées sur le mécanisme d'action

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Le statut de cette AMM est enregistré comme annulé dans les données locales » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Cytomel (liothyronine sodium) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=51452b31-ff68-4e0c-b982-c15502ebf1d3) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

