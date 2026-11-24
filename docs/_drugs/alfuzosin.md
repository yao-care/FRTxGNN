---
layout: default
title: Alfuzosin
parent: Prédiction du modèle uniquement (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "alfuzosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly", "allergic urticaria", "persistent fetal circulation syndrome", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
description: "Alfuzosin : nouvelle indication prédite, Ambras type hypertrichosis universalis congenita (niveau de preuve L5). En France, AMM dans la BDPM : 14 (valides : 13)"
---

# Alfuzosin
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

## Alfuzosin: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## Résumé en Une Phrase

Alfuzosine est un antagoniste des récepteurs alpha-1 adrénergiques, initialement utilisé pour le traitement de l'hyperplasie bénigne de la prostate.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertrichose congénitale universelle de type Ambras**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Ambras type hypertrichosis universalis congenita |
| Score de Prédiction TxGNN | 1.0000 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 13 sur 14) |
| Nombre d'AMM | 14 (valides : 13) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Alfuzosin (traduction non officielle) : « L'alfuzosine est un antagoniste sélectif des récepteurs alpha 1 -adrénergiques post-synaptiques, qui sont situés dans la prostate, la base de la vessie, le col vésical, la capsule prostatique et l'urètre prostatique. » Texte original en anglais : "Alfuzosin is a selective antagonist of post-synaptic alpha 1 -adrenoreceptors, which are located in the prostate, bladder base, bladder neck, prostatic capsule, and prostatic urethra." ([DailyMed: Uroxatral (alfuzosin hcl) prescribing information, Advanz Pharma (US) Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9fc7f119-f36b-44cf-945d-940160f3afe3), version du 2024-12-05 ; consulté le 2026-11-19). Sur la base des informations connues, l'alfuzosine est un antagoniste alpha-1 adrénergique, dont l'efficacité symptomatique dans l'hyperplasie bénigne de la prostate repose sur la relaxation du muscle lisse prostatique et cervical vésical.

**Il n'existe pas de lien mécanistique établi** avec la nouvelle indication. Le syndrome d'Ambras est une maladie génétique rare, associée à des remaniements du chromosome 8q affectant la régulation de TRPS1, sans voie adrénergique connue.

Les autres prédictions du modèle vont dans le même sens : hypertrichose (direction de l'effet incertaine, certains vasodilatateurs comme le minoxidil *provoquant* une hypertrichose), anomalies de la tige pilaire, hypotrichoses, syndromes malformatifs (dentaires, Dandy-Walker). L'urticaire allergique est l'indication la plus plausible sur le plan biologique, mais reste sans aucune preuve, des traitements établis existant déjà (antihistaminiques anti-H1, omalizumab). Dans le syndrome de circulation fœtale persistante, l'hypotension systémique induite par un alpha-bloquant pourrait aggraver le shunt droite-gauche.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64068708 | XATRAL 2,5 mg, comprimé pelliculé (SANOFI WINTHROP INDUSTRIE) | Comprimé pelliculé | Non renseignée (AMM active) |

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, hypotension orthostatique, troubles hypotensifs, syndrome du QT long (y compris familial), torsades de pointes, insuffisance hépatique, maladie hépatique, maladie de la vésicule biliaire, syndrome de l'iris hypotonique peropératoire.
- **Interactions médicamenteuses** : 198 interactions recensées. Parmi celles affichées :
  - **Majeures** : cisapride, clarithromycine, dolasétron (risque lié à l'allongement de l'intervalle QT et/ou à l'inhibition du CYP3A4).
  - **Modérées** : famotidine, aprépitant, bisacodyl, bupropion, canagliflozine, dapagliflozine, empagliflozine, ertugliflozine, clotrimazole, dronabinol, granisétron, lévofloxacine, ricin (huile), glycérine, lactitol, lactulose.
  - **Mineure** : cimétidine.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible ; le profil de sécurité (hypotension, allongement du QT) est défavorable pour des indications bénignes ou génétiques.

<!-- review:begin fr-lic-20261106-alfuzosin-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible ; le profil de sécurité (hypotension, allongement du QT) est défavorable pour des indications bénignes ou génétiques. Le produit n'est en outre plus commercialisé en France (AMM annulée). » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-alfuzosin-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Mise à disposition des mises en garde et contre-indications de la notice (ANSM), actuellement bloquante pour l'évaluation de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Données précliniques ou mécanistiques justifiant un lien entre la voie adrénergique et la pathologie visée
- Réévaluation de l'ordre de priorité des indications prédites (en particulier l'urticaire allergique, la plus plausible biologiquement) avant tout investissement

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Le produit n'est en outre plus commercialisé en France (AMM annulée) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Uroxatral (alfuzosin hcl) prescribing information, Advanz Pharma (US) Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9fc7f119-f36b-44cf-945d-940160f3afe3) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

