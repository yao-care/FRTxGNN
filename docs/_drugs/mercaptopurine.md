---
layout: default
title: Mercaptopurine
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 10
---

# Mercaptopurine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# MERCAPTOPURINE : Évaluation Interrompue — Données Insuffisantes pour Compléter l'Analyse

## Résumé en Une Phrase

La Mercaptopurine (DB01033) est un médicament connu appartenant à la classe des thiopurines antinéoplasiques. Cependant, le présent Evidence Pack ne contient **aucune indication prédite par TxGNN**, en raison de deux lacunes de données bloquantes : l'absence de données sur le mécanisme d'action (MOA) et l'absence d'informations réglementaires locales. Une remédiation des données est nécessaire avant toute analyse de repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Non renseignée dans cet Evidence Pack |
| Nouvelle Indication Prédite | Aucune — `predicted_indications` vide |
| Score de Prédiction TxGNN | N/A |
| Niveau de Preuve | L5 (prédiction non disponible) |
| Statut de Marché en France | Non renseigné (données TFDA : 未上市 — non commercialisé) |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi l'Évaluation est Incomplète

Deux lacunes de données ont empêché la génération de prédictions TxGNN pour ce candidat :

**Lacune DG001 — Blocking** : Les données de pharmacovigilance réglementaire (mises en garde, contre-indications issues de la notice officielle) sont absentes. Sans ces données, l'évaluation de sécurité de niveau S1 ne peut être initiée. Remédiation requise : téléchargement et extraction de la notice officielle.

**Lacune DG002 — High** : Le mécanisme d'action (MOA) n'est pas disponible dans cet Evidence Pack. Sans MOA, le modèle TxGNN ne peut pas établir de liens mécanistiques entre la Mercaptopurine et des nouvelles indications candidates. Remédiation requise : interrogation de l'API DrugBank pour récupérer les données pharmacodynamiques.

En l'absence de ces deux éléments fondamentaux, le champ `predicted_indications` est resté vide, rendant impossible la rédaction des sections habituelles d'analyse de repositionnement.

---

## Cytotoxicité

> La Mercaptopurine est un agent antinéoplasique de la classe des thiopurines (analogue des purines). Cette section est incluse sur la base de la classification pharmacologique du principe actif.

| Élément | Contenu |
|---|---|
| Classification de Cytotoxicité | Cytotoxique conventionnel — antinéoplasique de la classe Thiopurine (analogue des bases puriques) |
| Risque de Myélosuppression | Élevé — la myélosuppression est l'effet indésirable dose-limitant principal des thiopurines |
| Classification d'Émétogénicité | Faible à modérée |
| Éléments de Surveillance | NFS complète avec formule, bilan hépatique (ASAT/ALAT), TPMT/NUDT15 génotypage recommandé avant traitement |
| Protection de Manipulation | Manipulation selon les protocoles des médicaments cytotoxiques ; éviter le contact cutané et l'inhalation de poussière |

---

## Considérations de Sécurité

Veuillez consulter la notice officielle pour les informations de sécurité complètes.

> Les champs `key_warnings`, `contraindications` et `ddi` sont tous en statut [Data Gap] ou non renseignés dans cet Evidence Pack. Aucune donnée d'interaction médicamenteuse n'a été trouvée lors de la requête du 2026-03-29.

---

## Informations de Marché

Aucune autorisation de mise sur le marché enregistrée pour la Mercaptopurine dans la base de données consultée (0 licence, statut : non commercialisé).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le pipeline de données n'a pas pu générer de prédictions TxGNN en raison de deux lacunes bloquantes (MOA absent, notice réglementaire non extraite). Sans indication prédite, aucune analyse de repositionnement ne peut être conduite.

**Pour avancer, les éléments suivants sont nécessaires :**

1. **[DG001 — Bloquant]** Télécharger et parser la notice officielle de la Mercaptopurine (source : notice EMA ou ANSM) pour extraire les mises en garde, contre-indications et interactions médicamenteuses
2. **[DG002 — Priorité haute]** Interroger l'API DrugBank (DB01033) pour récupérer le MOA, les cibles pharmacologiques et les catégories thérapeutiques
3. **Re-lancer le pipeline TxGNN** après remédiation des deux lacunes pour obtenir `predicted_indications` avec scores et preuves
4. **Compléter les données de statut de marché** en France (ANSM) en parallèle de la requête TFDA, afin d'évaluer le potentiel d'extension d'indication versus nouvelle AMM
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

