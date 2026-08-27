---
layout: default
title: Lactulose
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 8
---

# Lactulose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Lactulose : De la Constipation Chronique/Encéphalopathie Hépatique à l'Acute Urate Nephropathy (Néphropathie Uratique Aiguë)

## Résumé en Une Phrase

Le lactulose est un disaccharide non absorbable classiquement utilisé dans la constipation chronique et l'encéphalopathie hépatique (encéphalopathie porto-systémique), par piégeage colique de l'ammoniac. Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Acute Urate Nephropathy (Néphropathie Uratique Aiguë)**, avec un score de **99,89 %**, mais **aucun essai clinique ni publication** ne soutient actuellement cette direction, et le lien mécanistique est jugé faible.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Constipation chronique / Encéphalopathie hépatique (non documentée dans les données réglementaires françaises fournies) |
| Nouvelle Indication Prédite | Acute Urate Nephropathy (Néphropathie Uratique Aiguë) |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le Evidence Pack. Sur la base des informations connues, le lactulose est un disaccharide non absorbable dont l'efficacité dans la constipation et l'encéphalopathie hépatique repose sur la fermentation colique (acidification du côlon, effet osmotique, réduction de l'absorption d'ammoniac) — un mécanisme purement digestif et hépato-intestinal.

L'Acute Urate Nephropathy est une atteinte tubulaire rénale aiguë causée par la précipitation intratubulaire de cristaux d'acide urique (typiquement lors d'un syndrome de lyse tumorale). Il n'existe pas de recoupement physiopathologique connu entre l'action colique du lactulose et la cristallisation urique intra-tubulaire rénale.

L'évaluation interne du dossier qualifie d'ailleurs explicitement cette prédiction de faiblement fiable : « Lactulose 藥理作用限於腸道（滲透性瀉劑、氨捕捉），與尿酸腎病變之機轉路徑無已知交集，判定為 TxGNN 嵌入相似性導致的低可信度預測 ». Autrement dit, ce signal est probablement un artefact de similarité d'embedding du modèle plutôt qu'une relation pharmacologique réelle.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le score TxGNN est élevé, mais aucune preuve clinique, préclinique ou mécanistique ne relie le lactulose à l'Acute Urate Nephropathy ; l'évaluation interne considère ce signal comme un probable artefact du modèle (stade de décision S0).

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA) du lactulose (DG002, sévérité High)
- Mises en garde et contre-indications issues de la notice ANSM/TFDA (DG001, sévérité Blocking — bloque l'évaluation de sécurité S1)
- Études précliniques explorant un éventuel effet du lactulose sur les lésions tubulaires rénales induites par l'acide urique, avant toute poursuite
- **Note d'orientation** : ce même Evidence Pack contient une piste bien mieux étayée pour le lactulose — l'*obstructive jaundice* (rang 3, niveau de preuve L3, stade S2 « Research Question »), avec 1 essai clinique et 20 publications, dont un essai multicentrique randomisé (PMID 2032107) sur la prévention de l'insuffisance rénale post-opératoire par le lactulose. Il est recommandé de prioriser cette indication pour la suite des travaux plutôt que l'Acute Urate Nephropathy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

