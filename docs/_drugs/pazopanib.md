---
layout: default
title: Pazopanib
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Pazopanib
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

# Pazopanib : Du Carcinome à Cellules Rénales Avancé au Carcinome Rénal Non Classifié

## Résumé en Une Phrase

Le pazopanib est un inhibiteur de tyrosine kinase multi-cibles, établi comme traitement du carcinome à cellules rénales (CCR) avancé/métastatique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Carcinome Rénal Non Classifié** (unclassified renal cell carcinoma),
avec **1 essai clinique** et **6 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome à cellules rénales avancé/métastatique (indication établie ; aucune AMM française enregistrée dans les données disponibles) |
| Nouvelle Indication Prédite | Carcinome Rénal Non Classifié |
| Score de Prédiction TxGNN | 99.63% |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action (DrugBank) ne sont pas disponibles dans ce dossier de preuves. Sur la base des informations disponibles dans la littérature et les essais associés, le pazopanib est décrit comme un **inhibiteur de tyrosine kinase multi-cibles** à activité anti-angiogénique et antitumorale (cf. PMID 31010343, PMID 24041629), bloquant notamment les enzymes nécessaires à la croissance tumorale (cf. NCT01532687, NCT02601209). L'essai NCT01613846 confirme par ailleurs que le pazopanib est un traitement « enregistré » pour le carcinome à cellules rénales (CCR) avancé, aux côtés du sorafénib.

Le carcinome rénal non classifié est une entité histologique rattachée au groupe des CCR non à cellules claires (non-clear-cell RCC, nccRCC), pour lequel les données proviennent largement de l'extrapolation des résultats obtenus dans le CCR à cellules claires. Plusieurs études réelles (real-world) et rétrospectives multicentriques (PANORAMA, PMID 28108284 ; PMID 27568124 ; PMID 31921344) ainsi qu'une étude de phase II (PMID 28546525) évaluent spécifiquement l'activité du pazopanib dans ce sous-groupe nccRCC.

Mécanistiquement, l'extension au carcinome rénal non classifié est donc plausible : la cible pharmacologique (VEGFR/PDGFR, angiogenèse tumorale) reste pertinente indépendamment du sous-type histologique du CCR, mais les preuves directes restent limitées à des cohortes rétrospectives et un seul essai randomisé de phase III, ce dernier n'étant pas spécifiquement dédié au sous-type « non classifié ».

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01613846](https://clinicaltrials.gov/study/NCT01613846) | Phase 3 | Terminé | 544 | Étude randomisée séquentielle comparant sorafénib suivi de pazopanib vs pazopanib suivi de sorafénib dans le CCR avancé/métastatique ; les deux médicaments sont déjà enregistrés pour cette indication, aucune donnée comparative prospective n'existait auparavant sur la séquence thérapeutique optimale. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Étude de phase II (bras unique, ouverte) | Cancer Research and Treatment | Étude multicentrique déterminant l'efficacité et la sécurité du pazopanib chez les patients atteints de CCR non à cellules claires (nccRCC). |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Étude rétrospective en vie réelle | Ecancermedicalscience | Comparaison de l'efficacité du sunitinib et du pazopanib en première ligne pour nccRCC et CCR sarcomatoïde ; ces sous-types sont sous-représentés dans les essais cliniques classiques. |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Étude rétrospective multicentrique (PANORAMA) | Clinical Genitourinary Cancer | Analyse rétrospective italienne de l'efficacité et de la toxicité du pazopanib en première ligne dans le nccRCC. |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Étude rétrospective | Clinical Genitourinary Cancer | Évaluation des résultats chez des patients atteints de CCR métastatique non à cellules claires traités par pazopanib. |
| [30268423](https://pubmed.ncbi.nlm.nih.gov/30268423/) | 2019 | Série de cas / revue de littérature | Clinical Genitourinary Cancer | Caractéristiques histologiques et immunohistochimiques de patients avec carcinome de primitif inconnu associé à un CCR métastatique (CUP-mRCC) traités par thérapies ciblées, dont le pazopanib. |
| [41558869](https://pubmed.ncbi.nlm.nih.gov/41558869/) | 2026 | Étude de cohorte multicentrique (IMDC) | European Urology Oncology | Comparaison des thérapies de première ligne (dont ciblées traditionnelles) selon les sous-types histologiques de nccRCC, incluant le CCR non classifié et le CCR chromophobe. |

---

## Informations de Marché en France

Aucune AMM n'est enregistrée dans les données disponibles : le pazopanib est actuellement **non commercialisé** en France (0 AMM recensée).

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée — inhibiteur de tyrosine kinase multi-cibles à activité anti-angiogénique (d'après la littérature associée : PMID 31010343, PMID 24041629) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Le pazopanib dispose d'un niveau de preuve modéré (L2) pour le carcinome rénal non classifié, appuyé par un essai randomisé de phase III terminé (portant sur le CCR avancé en général) et six publications en vie réelle/rétrospectives ciblant spécifiquement le sous-groupe non à cellules claires/non classifié. Toutefois, le produit n'est pas commercialisé en France (0 AMM) et l'absence de données de sécurité structurées (avertissements, contre-indications, interactions) bloque l'évaluation de sécurité préliminaire (S1).

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir le résumé des caractéristiques du produit / notice officielle (TFDA/ANSM) pour compléter l'évaluation de sécurité S1 (data gap bloquant DG001)
- Compléter les données DrugBank sur le mécanisme d'action pour renforcer l'analyse de pertinence mécanistique (DG002)
- Finaliser la gradation de pertinence (relevance grade) de l'essai NCT01613846 et des 6 publications, actuellement marquée « pending »
- Évaluer la nécessité d'une demande d'AMM en France si un développement local est envisagé
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

