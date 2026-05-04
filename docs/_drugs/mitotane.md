---
layout: default
title: Mitotane
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 0
---

# Mitotane
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

En analysant le JSON Evidence Pack reçu, je constate des lacunes critiques : `predicted_indications` est vide, le MOA est absent, et toutes les données de sécurité sont manquantes. Le rapport reflétera fidèlement cet état de dossier incomplet.

---

# Mitotane : Carcinome Corticosurrénalien — Évaluation en Attente de Prédictions TxGNN

## Résumé en Une Phrase

Le Mitotane est un agent adrénocorticolytique utilisé dans le traitement du carcinome corticosurrénalien, une tumeur maligne rare des glandes surrénales. Le modèle TxGNN **n'a pas encore généré de prédictions d'indications** pour ce médicament dans la version v4 du dossier d'évaluation (2026-04-20). En l'absence de toute indication cible prédite et face à des lacunes bloquantes dans les données de sécurité et de mécanisme d'action, aucune recommandation de repositionnement ne peut être émise à ce stade.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Carcinome corticosurrénalien |
| Nouvelle Indication Prédite | Non disponible — prédictions TxGNN absentes |
| Score de Prédiction TxGNN | Non disponible |
| Niveau de Preuve | L5 — aucune prédiction ni étude disponible |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi le Dossier est-il Incomplet ?

Le dossier d'évaluation actuel comporte deux lacunes majeures qui bloquent toute analyse de repositionnement.

**Absence de prédictions TxGNN.** La liste `predicted_indications` est vide. Sans indication cible issue du modèle, il est impossible de structurer l'analyse de repositionnement, d'identifier les essais cliniques pertinents, d'évaluer la littérature associée ou de déterminer la force des preuves. L'ensemble des sections centrales du rapport (justification mécanistique, preuves cliniques, preuves bibliographiques) ne peut donc être produit.

**Données de mécanisme d'action manquantes (DG002 — Sévérité : High).** Le MOA du Mitotane n'est pas renseigné dans ce dossier. Cette lacune empêche l'analyse de la pertinence mécanistique entre l'indication oncologique originale et toute nouvelle cible thérapeutique potentielle.

Sur la base des données publiques disponibles, le Mitotane est un dérivé organochloré apparenté au DDT, doté d'une action cytotoxique sélective sur le cortex surrénalien. Il supprime la stéroïdogenèse et induit une nécrose des cellules corticosurrénaliennes, ce qui constitue le fondement de son efficacité dans le carcinome corticosurrénalien. Ces informations contextuelles demeurent insuffisantes pour conduire une analyse de repositionnement structurée sans les prédictions du modèle.

---

## Cytotoxicité

Le Mitotane étant un médicament antinéoplasique indiqué dans un carcinome (tumeur maligne des glandes surrénales), la section cytotoxicité s'applique.

| Élément | Contenu |
|---|---|
| Classification de Cytotoxicité | Cytotoxique conventionnel — agent adrénocorticolytique (apparenté aux alkylants organochlorés) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétagénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les données relatives aux mises en garde, contre-indications et interactions médicamenteuses ne sont pas disponibles dans ce dossier (lacune DG001 — Sévérité : Blocking ; requête DDI : not_found).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le dossier d'évaluation est insuffisant pour émettre toute recommandation de repositionnement. L'absence de prédictions TxGNN rend impossible la rédaction du rapport dans sa forme complète, et les lacunes critiques en sécurité (DG001 — Blocking) bloquent l'entrée en phase d'évaluation.

**Pour avancer, les éléments suivants sont nécessaires :**
- Exécuter le pipeline TxGNN pour générer les prédictions d'indications pour le Mitotane (DB00648) — `predicted_indications` est actuellement vide
- Récupérer les données MOA depuis DrugBank (DG002 — Sévérité : High) via l'API DrugBank
- Télécharger et analyser la notice ANSM pour les mises en garde, contre-indications et précautions d'emploi (DG001 — Sévérité : Blocking)
- Relancer la collecte des interactions médicamenteuses (DDI — résultat : not_found lors de la requête du 2026-03-29)
- Vérifier le statut réglementaire en France (0 AMM enregistrée) et documenter si une procédure d'autorisation temporaire d'utilisation (ATU/AAP) est applicable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

