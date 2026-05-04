---
layout: default
title: Maprotiline
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 0
---

# Maprotiline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Maprotiline : Évaluation du Potentiel de Repositionnement

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
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Profil Pharmacologique Connu

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans cet ensemble de données. Sur la base des informations bibliographiques connues, la Maprotiline est un antidépresseur tétracyclique (apparenté aux tricycliques) dont l'effet principal repose sur le blocage sélectif de la recapture de la noradrénaline au niveau des terminaisons présynaptiques, avec des effets secondaires antihistaminiques et anticholinergiques notables.

Commercialisée historiquement sous le nom Ludiomil, la Maprotiline a été utilisée dans le traitement de la dépression unipolaire, des épisodes dépressifs associés à des troubles anxieux, et de l'insomnie d'accompagnement. Son profil sédatif prononcé la distingue des inhibiteurs sélectifs de la recapture de la sérotonine (ISRS) plus récents.

En l'absence de prédictions TxGNN et de données de mécanisme d'action formalisées dans cet ensemble de données, il n'est pas possible d'identifier une nouvelle indication cible ni d'évaluer la plausibilité mécanistique d'un repositionnement à ce stade.

---

## Informations de Marché en France

Aucune autorisation de mise sur le marché (AMM) n'est enregistrée pour la Maprotiline en France selon les données disponibles.

> **Note :** Des AMM historiques ont pu exister et avoir été retirées ou expirées. Une vérification auprès de la base de données publique de l'ANSM est recommandée pour confirmer le statut réglementaire actuel.

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
- **Analyser la notice ANSM/TFDA** pour extraire les avertissements, contre-indications et interactions médicamenteuses
- **Vérifier le statut réglementaire historique** en France via la base transparence ANSM (AMM potentiellement retirées ou expirées)
- **Relancer le pipeline d'evidence gathering** une fois les données de base complétées (Phase 5 — collecte d'essais cliniques et de littérature)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

