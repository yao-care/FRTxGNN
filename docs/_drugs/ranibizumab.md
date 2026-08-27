---
layout: default
title: Ranibizumab
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
---

# Ranibizumab
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

# Ranibizumab : De la Dégénérescence Maculaire Néovasculaire à la Rétinopathie Diabétique Non Proliférante Sévère

## Résumé en Une Phrase

Le ranibizumab est un anticorps monoclonal anti-VEGF-A, connu à l'origine pour le traitement de pathologies rétiniennes néovasculaires (dégénérescence maculaire liée à l'âge, œdème maculaire diabétique). Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Rétinopathie Diabétique Non Proliférante Sévère**, avec **6 essais cliniques** (dont 3 essais de Phase 3 complétés) et **19 publications** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans le pack de preuves (`original_indications` vide ; information générale connue : DMLA néovasculaire / OMD) |
| Nouvelle Indication Prédite | Rétinopathie Diabétique Non Proliférante Sévère (severe NPDR) |
| Score de Prédiction TxGNN | 99.99 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action officiel (`original_moa`) ne sont pas disponibles dans ce pack de preuves (Data Gap de sévérité High, en attente de requête DrugBank API). Sur la base des informations disponibles dans les données de preuve elles-mêmes, le ranibizumab est un fragment Fab d'anticorps monoclonal dirigé contre le VEGF-A, qui bloque directement la néovascularisation et l'augmentation de la perméabilité vasculaire induites par le VEGF — un mécanisme déjà validé dans plusieurs pays pour la rétinopathie diabétique, y compris la forme non proliférante sévère.

La rétinopathie diabétique et les pathologies rétiniennes néovasculaires pour lesquelles le ranibizumab est déjà utilisé partagent la même voie physiopathologique centrale : une surexpression du VEGF entraînant néovascularisation et fuite vasculaire rétinienne. La progression de la NPDR sévère vers la forme proliférante (PDR) et l'œdème maculaire diabétique est directement médiée par le VEGF, ce qui rend le mécanisme du ranibizumab directement transposable à cette indication, plutôt qu'une simple extrapolation de similarité de classe.

Cette cohérence mécanistique est renforcée par le fait que plusieurs essais de Phase 3 inclus dans ce pack (Port Delivery System, PANORAMA) ciblent spécifiquement la prévention de la progression de la NPDR sévère vers des complications menaçant la vision, ce qui constitue une preuve d'efficacité directe plutôt qu'une simple plausibilité mécanistique.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Phase 3 | Terminé | 691 | Comparaison laser seul vs laser + triamcinolone vs laser + ranibizumab vs ranibizumab seul dans l'œdème maculaire diabétique (étude type DRCR.net) |
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Phase 3 | Terminé | 174 | Port Delivery System avec ranibizumab (PDS) vs comparateur, efficacité/sécurité/PK chez patients NPDR sans OMD centro-maculaire |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Phase 3 | Terminé | 399 | Traitement anti-VEGF intravitréen pour la prévention de la rétinopathie diabétique menaçant la vision chez patients à haut risque (type PANORAMA) |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Phase 4 | Terminé | 25 | Étude pilote monocentrique sur l'effet du ranibizumab sur le turnover des microanévrismes et la zone rétinienne non perfusée dans la NPDR avec OMD |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Phase 3 | Statut inconnu | 118 | Efficacité/sécurité du ranibizumab intravitréen vs injections simulées pour la prévention de la RD à haut risque |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | Statut inconnu | 1000 | Observation en vie réelle de la thérapie anti-VEGF (dont ranibizumab) dans la DMLA exsudative, la PDR, l'OMD et la néovascularisation choroïdienne |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | ECR (Pavilion) | JAMA Ophthalmology | Port Delivery System avec ranibizumab vs surveillance dans la NPDR sans OMD ; injections anti-VEGF prophylactiques réduisent le risque de progression |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | ECR (post-hoc RIDE/RISE) | Clinical Ophthalmology | Facteurs prédictifs de régression précoce de la RD sous ranibizumab |
| [35417296](https://pubmed.ncbi.nlm.nih.gov/35417296/) | 2022 | ECR (post-hoc RIDE/RISE) | Ophthalmic Surg Lasers Imaging Retina | Évolution de la RD dans les yeux controlatéraux non traités (histoire naturelle sans traitement) |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | Rapport à 5 ans (DRCR.net Protocol I) | Retina | Changements de sévérité de la RD chez les yeux traités par ranibizumab pour OMD |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | Analyse secondaire d'ECR | JAMA Ophthalmology | Évolution de la RD à 2 ans, comparaison aflibercept/bevacizumab/ranibizumab |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Revue systématique/méta-analyse | Health Technology Assessment | Comparaison anti-VEGF vs photocoagulation laser dans la RD |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Revue systématique/analyse économique | Health Technology Assessment | Mise à jour comparant anti-VEGF vs laser dans la RD, incluant analyse coût-efficacité |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Méta-analyse (essais Phase 3) | Ophthalmology Retina | Sévérité initiale de la RD et délai de résolution de l'OMD sous ranibizumab |
| [30973596](https://pubmed.ncbi.nlm.nih.gov/30973596/) | 2019 | Cohorte | JAMA Ophthalmology | Caractéristiques de non-perfusion rétinienne en angiographie ultra-grand champ dans la NPDR sévère et la PDR |
| [36580154](https://pubmed.ncbi.nlm.nih.gov/36580154/) | 2023 | Cohorte/biomarqueur | International Ophthalmology | Taux sériques et vitréens de VEGF comme marqueurs de progression de la RD |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Le niveau de preuve L1 repose sur 3 essais de Phase 3 complétés (dont le Port Delivery System et le type PANORAMA) évaluant directement la NPDR sévère, renforcés par des analyses post-hoc RIDE/RISE de niveau ECR et des revues systématiques récentes (2024-2025). Toutefois, le médicament n'est actuellement pas commercialisé en France (0 AMM) et deux data gaps bloquants/majeurs subsistent : l'absence des mises en garde/contre-indications TFDA (bloquant pour l'évaluation de sécurité S1) et l'absence du MOA formel (impact sur l'analyse de pertinence mécanistique).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération des mises en garde et contre-indications officielles (TFDA ou équivalent français/ANSM) — gap bloquant DG001
- Récupération du MOA formalisé via DrugBank API — gap DG002
- Clarification du statut réglementaire en France (voie d'AMM ou d'extension d'indication) pour la NPDR sévère
- Évaluation de la compatibilité de voie d'administration (intravitréenne) et du schéma posologique spécifique à la NPDR sévère

Les 9 autres indications prédites (cataracte immature/mature/tétanique/de craniosténose, cataracte associée au diabète de type 2, cataracte nucléaire sénile/corticale/sénile, maladie hémorragique du nouveau-né) présentent un niveau de preuve L4/L5 sans lien mécanistique positif — elles ont été classées **Hold** et sont exclues de ce rapport, qui se concentre sur le candidat principal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

