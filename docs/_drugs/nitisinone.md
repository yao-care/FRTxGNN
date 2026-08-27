---
layout: default
title: Nitisinone
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Nitisinone
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

# Nitisinone : De la Tyrosinémie Héréditaire de Type 1 à l'Acidose Tubulaire Rénale

## Résumé en Une Phrase

Le nitisinone (NTBC, DB00348) est utilisé pour traiter la tyrosinémie héréditaire de type 1 (HT‑1), une maladie métabolique rare, en inhibant l'enzyme HPPD pour bloquer l'accumulation de métabolites toxiques du catabolisme de la tyrosine.
Le modèle TxGNN prédit qu'il pourrait être associé à l'**Acidose Tubulaire Rénale**, avec **0 essai clinique** et **2 publications** soutenant actuellement cette direction — un signal qui, à l'examen, correspond en réalité à un bénéfice secondaire déjà connu du traitement de la HT‑1 plutôt qu'à une nouvelle cible thérapeutique indépendante.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Tyrosinémie héréditaire de type 1 (HT‑1) *(non présente dans les champs réglementaires structurés fournis — déduite du contexte des publications associées)* |
| Nouvelle Indication Prédite | Acidose Tubulaire Rénale |
| Score de Prédiction TxGNN | 99.96% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données formelles de mécanisme d'action (DrugBank) ne sont pas disponibles dans ce pack de preuves (data gap DG002). Sur la base des informations contenues dans les publications associées, le nitisinone agit comme inhibiteur de la 4‑hydroxyphénylpyruvate dioxygénase (HPPD), bloquant une étape en amont du catabolisme de la tyrosine et réduisant l'accumulation de succinylacétone, le métabolite toxique responsable des lésions hépatiques et de la dysfonction tubulaire rénale caractéristiques de la HT‑1.

L'acidose tubulaire rénale prédite ici n'est pas une maladie indépendante de l'indication d'origine : elle est décrite dans la littérature comme une **complication rénale de la HT‑1 elle-même**, déjà connue pour s'améliorer sous traitement par NTBC. Autrement dit, le lien mécanistique proposé par TxGNN reflète un effet secondaire déjà documenté du traitement existant, et non une extension d'indication vers une population de patients distincte.

Cette distinction est importante pour l'évaluation : contrairement à un repositionnement classique (où un médicament traiterait une maladie sans rapport avec son usage d'origine), il s'agit ici essentiellement de confirmer/quantifier un bénéfice rénal chez les patients HT‑1 déjà traités — ce qui limite la portée d'un éventuel dossier de repositionnement au sens strict.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [25172236](https://pubmed.ncbi.nlm.nih.gov/25172236/) | 2014 | Étude de cohorte | Molecular Genetics and Metabolism | Effet précoce du NTBC sur la dysfonction tubulaire rénale chez des patients atteints de tyrosinémie héréditaire de type 1 — amélioration de la fonction tubulaire sous traitement |
| [27109516](https://pubmed.ncbi.nlm.nih.gov/27109516/) | 2016 | Série de cas | Indian Journal of Gastroenterology | Série de 4 enfants atteints de tyrosinémie traités par NTBC ; fonction hépatique normalisée et absence de complication tubulaire rénale rapportée sous traitement prolongé |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

*(Note : les mises en garde et contre-indications officielles TFDA ne sont actuellement pas disponibles dans ce dossier — voir data gap bloquant DG001 ci-dessous.)*

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve (L3) repose uniquement sur une étude de cohorte et une série de cas, sans essai clinique contrôlé ; l'indication prédite correspond en réalité à une complication déjà connue de la maladie d'origine plutôt qu'à un mécanisme de repositionnement indépendant.
- Un data gap **bloquant** (DG001 — absence des mises en garde/contre-indications TFDA) empêche à ce stade toute évaluation de sécurité initiale (S1), et le médicament n'est actuellement pas commercialisé (0 AMM).

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les données de notice/mises en garde TFDA (DG001, bloquant)
- Obtenir les données formelles de mécanisme d'action via DrugBank (DG002)
- Clarifier si l'acidose tubulaire rénale doit être évaluée comme indication indépendante ou comme extension d'étiquette rattachée à la HT‑1
- Les 9 autres candidats prédits (galactosémie, sérpinopathie, déficit en inhibiteur C1, glycogénoses, syndrome de Griscelli, granulomatose chronique liée à l'X, phénotype ermine) sont tous classés L4/L5 avec recommandation Hold — absence de littérature ou de lien mécanistique substantiel, non retenus pour approfondissement à ce stade.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

