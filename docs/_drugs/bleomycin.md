---
layout: default
title: Bleomycin
parent: Prédiction du modèle uniquement (L5)
nav_order: 111
evidence_level: L5
indication_count: 5
monitor_inn: "bleomycin"
predicted_indications: ["cauda equina neoplasm", "adult astrocytic tumour", "primary pulmonary lymphoma", "pulmonary blastoma", "well-differentiated fetal adenocarcinoma of the lung"]
last_modified_at: 2026-11-24
description: "Bleomycin : nouvelle indication prédite, Tumeur de la queue de cheval (cauda equina neoplasm) (niveau de preuve L5). En France, AMM dans la BDPM : 2 (valides : 2)"
---

# Bleomycin
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

## Bleomycin: Tumeur de la queue de cheval (cauda equina neoplasm)
{: .text-alpha }

## Résumé en Une Phrase

La bléomycine est un antibiotique cytotoxique qui provoque des cassures de brins d'ADN et entre dans plusieurs protocoles de chimiothérapie.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **tumeur de la queue de cheval (cauda equina neoplasm)**, avec un score de 0.9930.
À ce jour, **aucun essai clinique** et **une seule publication**, indirecte (radiothérapie d'un germinome du système nerveux central en rechute), soutiennent cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Tumeur de la queue de cheval (cauda equina neoplasm) |
| Score de Prédiction TxGNN | 0.9930 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Bleomycin (traduction non officielle) : « Bien que le mécanisme d'action exact de la bléomycine soit inconnu, les données disponibles indiquent que le principal mode d'action est l'inhibition de la synthèse de l'ADN, avec certaines données en faveur d'une inhibition moindre de la synthèse de l'ARN et des protéines. La bléomycine est connue pour provoquer des cassures simple brin et, dans une moindre mesure, double brin de l'ADN. » Texte original en anglais : "Although the exact mechanism of action of bleomycin is unknown, available evidence indicates that the main mode of action is the inhibition of DNA synthesis with some evidence of lesser inhibition of RNA and protein synthesis. Bleomycin is known to cause single, and to a lesser extent, double-stranded breaks in DNA." ([DailyMed: Bleomycin (bleomycin sulfate) prescribing information, Meitheal Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=640602f9-a7df-46f0-a9b1-19c471008bee), version du 2026-04-17 ; consulté le 2026-11-19). D'après les connaissances générales, la bléomycine est un cytotoxique qui casse les brins d'ADN, utilisé dans des protocoles de tumeurs germinales.

Le seul lien documenté avec la prédiction est indirect : une étude rétrospective sur la radiothérapie de germinomes du système nerveux central en rechute après une chimiothérapie comprenant carboplatine, étoposide et bléomycine. Cette étude ne concerne ni la tumeur de la queue de cheval ni l'efficacité propre de la bléomycine.

Le score élevé (0.9930) est une prédiction computationnelle et ne remplace pas des données cliniques. Aucune donnée spécifique à cette tumeur n'est disponible, et le niveau de preuve reste donc L5.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Cohorte | Journal of Clinical Oncology | Évaluation rétrospective de la radiothérapie de rattrapage chez des patients atteints de germinome du SNC en rechute après chimiothérapie primaire (carboplatine, étoposide, bléomycine). Association indirecte, sans lien avec la tumeur de la queue de cheval. |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 60033389 | BLEOMYCINE ACCORD 15000 UI, poudre pour solution injectable / pour perfusion | Poudre pour solution injectable ou pour perfusion | ACCORD HEALTHCARE FRANCE | Active |
| 62789360 | BLEOMYCINE BELLON 15 mg, poudre pour solution injectable | Poudre pour solution injectable | HIKMA FRANCE | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (antibiotique antitumoral, cassures de l'ADN) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter la notice |
| Éléments de Surveillance | Fonction respiratoire (toxicité pulmonaire à la bléomycine documentée dans la littérature), fonction hépatique et rénale |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

- **Toxicité pulmonaire** : la littérature compilée pour ce rapport évoque une toxicité pulmonaire de la bléomycine, qui doit être prise en compte dans toute extension d'usage.
- **Interactions médicamenteuses** : 205 interactions sont recensées. Les plus courantes concernent notamment la lévofloxacine (mineure), le pantoprazole, le palonosétron, le lactulose, l'aprépitant, la morphine, l'oméprazole, le lansoprazole, la vancomycine et la prednisone (niveau de gravité non précisé). Veuillez consulter la notice pour la liste complète.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (0.9930). Aucun essai ni publication ne porte directement sur la tumeur de la queue de cheval, d'où un niveau de preuve L5.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données cliniques ou précliniques portant directement sur la tumeur de la queue de cheval
- Données détaillées sur le mécanisme d'action
- Mises en garde et contre-indications issues de la notice française
- Évaluation de la faisabilité d'une administration locale ou intrathécale et du risque de toxicité pulmonaire

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Bleomycin (bleomycin sulfate) prescribing information, Meitheal Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=640602f9-a7df-46f0-a9b1-19c471008bee) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

