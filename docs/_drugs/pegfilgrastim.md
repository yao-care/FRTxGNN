---
layout: default
title: Pegfilgrastim
parent: Prédiction du modèle uniquement (L5)
nav_order: 583
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Pegfilgrastim : nouvelle indication prédite, Rétinopathie diabétique non proliférante sévère (seconde prédiction :… (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM…"
monitor_inn: "PEGFILGRASTIM"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Pegfilgrastim
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Pegfilgrastim : D'un facteur de croissance des neutrophiles à la rétinopathie diabétique non proliférante sévère
{: .text-alpha }

## Résumé en Une Phrase

Pegfilgrastim est un facteur de croissance des granulocytes (G-CSF) pégylé, qui stimule la production de neutrophiles. Le texte des indications des autorisations françaises n'est pas renseigné dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **rétinopathie diabétique non proliférante sévère**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Rétinopathie diabétique non proliférante sévère (seconde prédiction : rétinopathie diabétique, terme plus général) |
| Score de Prédiction TxGNN | 0,9989 (rétinopathie diabétique : 0,9973) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 12 sur 12) |
| Nombre d'AMM | 12 (valides : 12) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Pegfilgrastim (traduction non officielle) : « Les produits à base de pegfilgrastim sont des facteurs de croissance hématopoïétiques (facteurs stimulant les colonies) qui agissent sur les cellules hématopoïétiques en se liant à des récepteurs spécifiques de surface cellulaire, stimulant ainsi la prolifération, la différenciation, l'engagement et l'activation fonctionnelle des cellules terminales. » Texte original en anglais : "Pegfilgrastim products are colony-stimulating factor that acts on hematopoietic cells by binding to specific cell surface receptors, thereby stimulating proliferation, differentiation, commitment, and end cell functional activation." ([DailyMed: Armlupeg (pegfilgrastim-unne) prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c48fe1a7-63d7-4dce-bb53-a913cb0ade83), version du 2026-10-29 ; consulté le 2026-11-19). Sur la base des informations connues, le pégfilgrastim est un analogue pégylé du G-CSF : il stimule la production de neutrophiles en se liant au récepteur du G-CSF.

Un lien plausible, mais non testé, serait la mobilisation de cellules progénitrices endothéliales issues de la moelle osseuse, qui pourrait soutenir la réparation vasculaire dans les rétinopathies ischémiques.

L'effet pourrait toutefois aller dans le sens inverse. L'activation des neutrophiles, l'inflammation et la leucostase, ainsi que des signaux pro-angiogéniques associés au G-CSF, pourraient aggraver les lésions vasculaires rétiniennes. Le sens de l'effet est donc incertain. Les deux indications prédites sont de plus liées (la seconde est le terme parent de la première) : elles ne constituent pas deux preuves indépendantes. Il s'agit à ce stade d'une prédiction purement computationnelle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Le texte de l'indication approuvée n'est pas disponible pour ces AMM.

<!-- review:begin fr-lic-20261106-pegfilgrastim-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les 10 AMM recensées sont annulées. Le texte de l'indication approuvée n'est pas disponible pour ces AMM. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-pegfilgrastim-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 63655026 | GRASUSTEK 6 mg, solution injectable en seringue préremplie | Solution injectable | JUTA PHARMA (ALLEMAGNE) | Active |
| 60457929 | FULPHILA 6 mg, solution injectable en seringue préremplie | Solution injectable | BIOSIMILAR COLLABORATIONS IRELAND (IRLANDE) | Active |
| 64847677 | PELGRAZ 6 mg, solution injectable en stylo injecteur prérempli | Solution injectable | ACCORD HEALTHCARE (ESPAGNE) | Active |
| 61553026 | PELGRAZ 6 mg, solution injectable en seringue préremplie | Solution injectable | ACCORD HEALTHCARE (ESPAGNE) | Active |
| 63626633 | ZIEXTENZO 6 mg, solution injectable en seringue préremplie | Solution injectable | SANDOZ (AUTRICHE) | Active |
| 60647992 | CEGFILA 6 mg, solution injectable en seringue préremplie | Solution injectable | MUNDIPHARMA CORPORATION (IRELAND) | Active |
| 68735818 | NEULASTA 6 mg, solution injectable | Solution injectable | AMGEN EUROPE | Active |
| 68698437 | NYVEPRIA 6 mg, solution injectable | Solution injectable | PFIZER EUROPE MA EEIG (BELGIQUE) | Active |
| 61378153 | PELMEG 6 mg, solution injectable en seringue préremplie | Solution injectable | MUNDIPHARMA CORPORATION (IRELAND) | Active |
| 69578572 | STIMUFEND 6 mg, solution injectable en seringue préremplie | Solution injectable | FRESENIUS KABI DEUTSCHLAND (ALLEMAGNE) | Active |
| 60390334 | DYRUPEG 6 mg, solution injectable en seringue préremplie | Solution injectable | CURATEQ BIOLOGICS (MALTE) | Active |
| 67692246 | VIVLIPEG 6 mg, solution injectable en seringue préremplie | Solution injectable | BIOSIMILAR COLLABORATIONS IRELAND (IRLANDE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

**Interactions Médicamenteuses** : 100 interactions ont été recensées. Les 20 premières, toutes de niveau modéré, concernent notamment : pegvaliase, iobenguane (I-131), fludéoxyglucose (18F), ibritumomab tiuxétan, tositumomab, lévamisole, triméthrexate, mercaptopurine, abémaciclib, paclitaxel, acalabrutinib, aldesleukine, alemtuzumab, altrétamine, trioxyde d'arsenic, asparaginase, avapritinib, azacitidine et bélantamab mafodotin.

Veuillez consulter la notice pour les mises en garde et contre-indications, qui ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication. Le sens de l'effet est incertain, avec un risque théorique d'aggravation de la pathologie rétinienne.
- Des AMM françaises sont valides (statut des AMM : voir l'Aperçu rapide) et le médicament est commercialisé, mais les données de sécurité issues de la notice font défaut, ce qui bloque l'évaluation de sécurité.

<!-- review:begin fr-lic-20261124-pegfilgrastim-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les 10 AMM françaises sont valides (10 sur 10) » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans l'Aperçu rapide. Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés : le nombre et le statut à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché, générés à partir des données BDPM. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-pegfilgrastim-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde, contre-indications, indications approuvées)
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Réaliser une revue de la littérature préclinique (G-CSF, cellules progénitrices endothéliales, rétinopathie diabétique) et rechercher d'éventuels essais
- Évaluer la compatibilité de la voie d'administration (injection systémique par rapport à une administration oculaire)
- Vérifier le statut réglementaire actuel du produit en France

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Les 10 AMM recensées sont annulées » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Armlupeg (pegfilgrastim-unne) prescribing information, Lupin Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c48fe1a7-63d7-4dce-bb53-a913cb0ade83) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

