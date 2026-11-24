---
layout: default
title: Eslicarbazepine
parent: Preuves élevées (L1-L2)
nav_order: 298
evidence_level: L2
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "eslicarbazepine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "insomnia (disease)", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
description: "Eslicarbazepine : nouvelle indication prédite, Migraine (migraine disorder) (niveau de preuve L2). En France, AMM dans la BDPM : 2 (valides : 2)"
drugbank_id: DB14575
---

# Eslicarbazepine
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **5** 
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

## Eslicarbazepine: Migraine (migraine disorder)
{: .text-alpha }

## Résumé en Une Phrase

Le modèle TxGNN prédit qu'il pourrait être efficace pour la **migraine (traitement préventif)**,
avec **1 essai clinique** de phase 2 terminé et **aucune publication** portant directement sur l'eslicarbazépine dans la migraine.

<!-- review:begin fr-lic-20261106-eslicarbazepine-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « L'eslicarbazépine est un antiépileptique (anticonvulsivant) dont les autorisations françaises sont aujourd'hui toutes annulées, et dont le texte d'indication d'origine n'est pas renseigné dans les données compilées pour ce rapport. / Le modèle TxGNN prédit qu'il pourrait être efficace pour la **migraine (traitement préventif)**, » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-eslicarbazepine-1 -->

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Migraine (migraine disorder) |
| Score de Prédiction TxGNN | 0.9978 |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Eslicarbazepine (traduction non officielle) : « APTIOM est largement converti en eslicarbazépine, qui est considérée comme responsable des effets thérapeutiques chez l'homme. Le ou les mécanismes précis par lesquels l'eslicarbazépine exerce son activité anticonvulsivante sont inconnus, mais on pense qu'ils impliquent une inhibition des canaux sodiques voltage-dépendants. » Texte original en anglais : "APTIOM is extensively converted to eslicarbazepine, which is considered to be responsible for therapeutic effects in humans. The precise mechanism(s) by which eslicarbazepine exerts anticonvulsant activity is unknown but is thought to involve inhibition of voltage-gated sodium channels." ([DailyMed: Aptiom (eslicarbazepine acetate) prescribing information, Sumitomo Pharma America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3d0c9554-eaeb-4694-8089-00133fcadce3), version du 2023-11-10 ; consulté le 2026-11-19). Sur la base des informations connues, l'eslicarbazépine appartient à la classe des antiépileptiques bloqueurs des canaux sodiques voltage-dépendants : elle stabilise l'état inactivé du canal et réduit l'hyperexcitabilité neuronale. Ce lien est déduit de la classe pharmacologique et n'est pas documenté dans les données compilées.

Une hyperexcitabilité corticale et la dépression corticale envahissante sont impliquées dans la physiopathologie de la migraine. D'autres antiépileptiques (topiramate, valproate) sont des traitements préventifs établis, ce qui rend l'hypothèse plausible. Le score TxGNN très élevé (0,9978) est cohérent avec ce raisonnement de classe.

Les résultats doivent être vérifiés avant toute recommandation.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01820559](https://clinicaltrials.gov/study/NCT01820559) | Phase 2 | Terminé | 452 | Essai multinational randomisé en double aveugle contre placebo : acétate d'eslicarbazépine 800 mg/j ou 1200 mg/j (une prise par jour) en prévention de la migraine avec ou sans aura (2009-2010). Aucun résultat n'est fourni dans les données compilées. |

## Preuves de la Littérature

Aucune publication ne porte directement sur l'eslicarbazépine dans la migraine. Les références liées sont des revues générales ou indirectes :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Revue | Expert Rev Neurother | Mise à jour sur la pharmacothérapie de la névralgie trigéminale ; mentionne les anticonvulsivants de troisième génération et les nouveaux inhibiteurs du CGRP dans la migraine comme options possibles |
| [32217376](https://pubmed.ncbi.nlm.nih.gov/32217376/) | 2020 | Revue | J Neurol Sci | Tolérance et sécurité de l'acétate d'eslicarbazépine dans les troubles neurologiques |
| [32025776](https://pubmed.ncbi.nlm.nih.gov/32025776/) | 2020 | Étude préclinique | Psychopharmacology | L'eslicarbazépine associée à des analgésiques standard ou alternatifs réduit la nociception trigéminale (interaction favorable) |
| [35363878](https://pubmed.ncbi.nlm.nih.gov/35363878/) | 2022 | Méta-analyse | Cochrane Database Syst Rev | Méta-analyse en réseau des monothérapies antiépileptiques dans l'épilepsie (indirect) |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 63927729 | ESLICARBAZEPINE ARROW 800 mg, comprimé sécable | Comprimé sécable | ARROW GENERIQUES | Active |
| 68829121 | ZEBINIX 800 mg, comprimé | Comprimé | BIAL - PORTELA & CA (PORTUGAL) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 125 interactions sont recensées. Parmi les interactions de niveau modéré figurent : aprépitant, morphine (y compris liposomale), opium, difénoxine, diphénoxylate, dronabinol, nabilone, éliglustat, naloxégol, mannitol, métoclopramide, nitisinone, rolapitant, rosuvastatine, simvastatine, sibutramine, éthanol, acide folique et cobicistat.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les autres indications prédites (sous-types de migraine, insomnie, affections dermatologiques rares) reposent sur le modèle seul ou sur des données indirectes. Pour l'insomnie, la seule publication suggère plutôt un effet indésirable sur le sommeil.
- Les données de sécurité de la notice font défaut.

<!-- review:begin fr-lic-20261106-eslicarbazepine-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les AMM françaises sont toutes annulées et les données de sécurité de la notice font défaut. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-eslicarbazepine-2 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Retrouver les résultats publiés ou enregistrés de l'essai NCT01820559 (efficacité et tolérance)
- Obtenir la notice (mises en garde, contre-indications) auprès de l'ANSM
- Compléter les données sur le mécanisme d'action
- Regrouper les entrées de migraine apparentées (sous-types, terme de susceptibilité génétique) sous une seule indication

<!-- review:begin fr-lic-20261106-eslicarbazepine-3 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Compléter les données sur le mécanisme d'action / Clarifier les raisons de l'annulation des AMM et le statut de marché actuel » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-eslicarbazepine-3 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « L'eslicarbazépine est un antiépileptique (anticonvulsivant) dont les autorisations françaises sont aujourd'hui toutes annulées, et dont le t » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « es AMM françaises sont toutes annulées et l » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « Clarifier les raisons de l'annulation des AMM et le statut de marché actuel » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Aptiom (eslicarbazepine acetate) prescribing information, Sumitomo Pharma America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3d0c9554-eaeb-4694-8089-00133fcadce3) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

