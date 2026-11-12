---
noindex: true
sitemap: false
layout: default
title: Maprotiline
parent: Prédiction du modèle uniquement (L5)
nav_order: 473
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Maprotiline
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **0** 
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

## Maprotiline : Évaluation du Potentiel de Repositionnement
{: .text-alpha }

## Résumé en Une Phrase

Maprotiline est un antidépresseur tétracyclique dont le mécanisme d'action repose principalement sur l'inhibition sélective de la recapture de la noradrénaline, initialement indiqué pour le traitement de la dépression et des troubles anxieux.
Aucune nouvelle indication n'a été prédite par le modèle TxGNN dans cet ensemble de données,
et les lacunes importantes dans les données disponibles ne permettent pas de mener une analyse de repositionnement complète.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dépression et troubles anxieux (antidépresseur tétracyclique) |
| Nouvelle Indication Prédite | Aucune prédiction TxGNN disponible |
| Score de Prédiction TxGNN | N/A |
| Niveau de Preuve | L5 — Données insuffisantes pour évaluation |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Profil Pharmacologique Connu

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans cet ensemble de données. Sur la base des informations bibliographiques connues, la Maprotiline est un antidépresseur tétracyclique (apparenté aux tricycliques) dont l'effet principal repose sur le blocage sélectif de la recapture de la noradrénaline au niveau des terminaisons présynaptiques, avec des effets secondaires antihistaminiques et anticholinergiques notables.

Commercialisée historiquement sous le nom Ludiomil, la Maprotiline a été utilisée dans le traitement de la dépression unipolaire, des épisodes dépressifs associés à des troubles anxieux, et de l'insomnie d'accompagnement. Son profil sédatif prononcé la distingue des inhibiteurs sélectifs de la recapture de la sérotonine (ISRS) plus récents.

En l'absence de prédictions TxGNN et de données de mécanisme d'action formalisées dans cet ensemble de données, il n'est pas possible d'identifier une nouvelle indication cible ni d'évaluer la plausibilité mécanistique d'un repositionnement à ce stade.

---

## Informations de Marché en France

Aucune autorisation de mise sur le marché (AMM) n'est enregistrée pour la Maprotiline en France selon les données disponibles.

> Une vérification auprès de la base de données publique de l'ANSM est recommandée pour confirmer le statut réglementaire actuel.

<!-- review:begin fr-lic-20261106-maprotiline-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « > **Note :** Des AMM historiques ont pu exister et avoir été retirées ou expirées. Une vérification auprès de la base de données publique de l'ANSM est recommandée pour confirmer le statut réglementaire actuel. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-maprotiline-1 -->

---

## Considérations de Sécurité

Veuillez consulter la notice officielle pour les informations de sécurité complètes (avertissements, contre-indications, interactions médicamenteuses).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
L'absence totale de prédictions TxGNN combinée aux lacunes critiques dans les données (mécanisme d'action non documenté, avertissements de sécurité manquants, aucune AMM française enregistrée) rend toute analyse de repositionnement impossible à ce stade ; les conditions minimales d'évaluation ne sont pas réunies.

**Pour avancer, les éléments suivants sont nécessaires :**

- **Compléter les prédictions TxGNN** pour la Maprotiline (DB00934) afin d'identifier des indications candidates
- **Récupérer les données MOA depuis DrugBank** (API DrugBank — DB00934) pour formaliser le mécanisme d'action
- **Analyser la notice ANSM** pour extraire les avertissements, contre-indications et interactions médicamenteuses
- **Vérifier le statut réglementaire historique** en France via la base transparence ANSM
- **Relancer le pipeline d'evidence gathering** une fois les données de base complétées (Phase 5 — collecte d'essais cliniques et de littérature)

<!-- review:begin fr-lic-20261106-maprotiline-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « **Analyser la notice ANSM/TFDA** pour extraire les avertissements, contre-indications et interactions médicamenteuses / **Vérifier le statut réglementaire historique** en France via la base transparence ANSM (AMM potentiellement retirées ou expirées) » Supprimé : texte résiduel du modèle taïwanais (TFDA), sans objet pour cette page. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-maprotiline-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « **Note :** Des AMM historiques ont pu exister et avoir été retirées ou expirées » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « /TFDA (AMM potentiellement retirées ou expirées) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

