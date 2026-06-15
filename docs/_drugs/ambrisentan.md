---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan : De l'Hypertension Artérielle Pulmonaire à la Malformation Artérioveineuse Pulmonaire

## Résumé en Une Phrase

Ambrisentan est un antagoniste sélectif des récepteurs de l'endothéline de type A (ETA), commercialisé à l'international sous les noms Letairis® (FDA) et Volibris® (EMA) pour le traitement de l'hypertension artérielle pulmonaire (HAP), mais ne disposant d'aucune AMM en France.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Malformation Artérioveineuse Pulmonaire (PAVM)**,
avec **0 essai clinique** et **1 publication** soutenant actuellement cette direction spécifique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle pulmonaire (HAP) — approbation FDA/EMA, non commercialisé en France |
| Nouvelle Indication Prédite | Malformation artérioveineuse pulmonaire (PAVM) |
| Score de Prédiction TxGNN | 99,41 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Non commercialisé (aucune AMM ANSM) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Research Question |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de données interrogée (DG002 — sévérité Haute). Sur la base des informations connues, Ambrisentan est un antagoniste sélectif du récepteur A de l'endothéline (ETA) qui bloque la liaison de l'endothéline-1 (ET-1) à ce récepteur, inhibant ainsi la vasoconstriction et le remodelage vasculaire pulmonaire. Cette cible est bien validée dans l'HAP idiopathique et associée, dans laquelle les niveaux circulants d'ET-1 sont significativement élevés.

La malformation artérioveineuse pulmonaire (PAVM) est une anomalie vasculaire structurelle caractérisée par une connexion anormale directe entre artères et veines pulmonaires, court-circuitant la circulation capillaire normale. Elle s'observe fréquemment dans le contexte de la télangiectasie hémorragique héréditaire (HHT), une vasculopathie génétique autosomique dominante rare. Dans ce cadre, une fraction des patients HHT-PAVM développe secondairement une HAP — créant ainsi un pont biologique indirect avec le mécanisme d'action d'Ambrisentan sur l'axe ET-1/ETA.

Il est cependant essentiel de souligner qu'Ambrisentan ne possède **aucun mécanisme d'action direct sur les PAVM elles-mêmes**, qui sont des lésions anatomiques relevant de l'embolisation percutanée ou de la chirurgie. La prédiction TxGNN reflète vraisemblablement une connexion topologique dans le graphe de connaissances (PAVM → HHT → HAP secondaire → traitement antagoniste ERA), et non une efficacité thérapeutique directe sur les malformations vasculaires structurelles.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Rapport de cas | World Journal of Clinical Cases | Patient HHT présentant une HAP associée traitée par thérapie ciblée HAP ; analyse génétique familiale réalisée ; souligne la rareté de cette comorbidité et son pronostic réservé sans prise en charge adaptée |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Research Question**

**Justification :**
Le lien mécanistique entre Ambrisentan et la PAVM est indirect et biologiquement marginal — la pertinence clinique se limite à la gestion d'une HAP secondaire survenant dans une minorité de patients HHT-PAVM, sans aucune action sur la lésion vasculaire structurelle elle-même. L'unique publication disponible est un rapport de cas centré sur la comorbidité HHT-HAP et ne concerne pas Ambrisentan directement dans cette indication.

> **Note sur le pack multi-indications :** Ce dossier couvre également des indications nettement mieux étayées qui méritent une évaluation prioritaire distincte : la HAP associée à l'infection VIH (**Rang 3 — L1**, 1 essai Phase 3 complété), la HAP associée aux cardiopathies congénitales (**Rang 2 — L2**, plusieurs essais Phase 2/3) et la HAP associée aux connectivites (**Rang 6 — L2**, 3 essais complétés dont 2 Phase 4).

**Pour avancer, les éléments suivants sont nécessaires :**
- Données complètes sur le mécanisme d'action (MOA) d'Ambrisentan — source : DrugBank API (DG002)
- Informations de sécurité ANSM/EMA : mises en garde, contre-indications, interactions médicamenteuses (DG001 — statut bloquant)
- Données précliniques ou registres ciblant spécifiquement l'HHT-PAVM avec antagonistes des récepteurs de l'endothéline
- Génération de rapports distincts pour les indications HAP de rang supérieur (VIH-PAH, CHD-PAH, CTD-PAH) qui présentent un niveau de preuve clinique suffisant pour progresser vers l'étape S3
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

