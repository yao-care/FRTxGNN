---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

# Imiquimod : Des Lésions Cutanées Précancéreuses vers le Néoplasme Pré-malin

## Résumé en Une Phrase

Imiquimod est un agent topique immunomodulateur (agoniste du TLR7), historiquement utilisé pour traiter des lésions cutanées précancéreuses telles que la kératose actinique et le carcinome basocellulaire superficiel.
Le modèle TxGNN prédit qu'il pourrait être efficace, de façon plus large, pour le **Néoplasme Pré-malin**,
avec **19 essais cliniques** et **9 publications** actuellement recensés — la pertinence directe variant toutefois fortement selon les essais.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non structurée dans l'Evidence Pack (donnée réglementaire manquante) — usage cliniquement établi pour lésions cutanées précancéreuses (kératose actinique, carcinome basocellulaire superficiel), tel que mentionné dans les essais cliniques inclus |
| Nouvelle Indication Prédite | Néoplasme Pré-malin (*pre-malignant neoplasm*) |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données structurées de mécanisme d'action (MOA) ne sont actuellement pas disponibles dans l'Evidence Pack (écart de données identifié, sévérité élevée). Sur la base de la littérature synthétisée, l'imiquimod est un agoniste du récepteur Toll-like 7 (TLR7) : appliqué localement, il induit la libération de cytokines (IFN-α, TNF-α) par les kératinocytes et les cellules dendritiques, activant l'immunité innée et adaptative pour éliminer les cellules épidermiques atypiques en prolifération.

Ce mécanisme a déjà été validé cliniquement sur plusieurs types de néoplasies intraépithéliales à divers sites anatomiques : kératose actinique, néoplasie intraépithéliale cervicale (CIN), vulvaire (VIN), anale (AIN), et papulose bowénoïde. La prédiction d'une efficacité pour le « Néoplasme Pré-malin » au sens large s'apparente donc largement à une **généralisation** d'usages déjà documentés (dont certains hors AMM), plutôt qu'à une direction thérapeutique entièrement nouvelle.

Deux réserves importantes doivent toutefois être soulignées. Premièrement, « Néoplasme Pré-malin » est une catégorie hétérogène regroupant des sites anatomiques très divers (peau, muqueuses cervicale/vulvaire/anale/orale), avec une force de preuve très variable selon le site. Deuxièmement, une part importante des essais cliniques associés à cette prédiction concerne en réalité l'utilisation de l'imiquimod comme **adjuvant vaccinal** dans des cancers déjà invasifs (mélanome, gliome, cancer de la prostate) — un usage sans rapport direct avec le traitement des lésions pré-malignes, et qui ne doit pas être confondu avec l'indication étudiée ici.

---

## Preuves d'Essais Cliniques

*Note : sur 19 essais recensés, environ 10 concernent l'imiquimod comme adjuvant vaccinal dans des cancers invasifs (mélanome, gliome, prostate, poumon) sans rapport direct avec le traitement des lésions pré-malignes ; ils ont été exclus du tableau ci-dessous au profit des essais directement pertinents.*

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminé | 9 | RCT visant à traiter les CIN de haut grade par imiquimod topique plutôt que par exérèse chirurgicale (LLETZ) ; essai arrêté prématurément, portée statistique très limitée |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Terminé | 259 | Évaluation de l'imiquimod néoadjuvant pour réduire la taille d'exérèse et le risque d'excision incomplète dans le lentigo malin du visage |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Inconnu | 145 | Non-infériorité : exérèse chirurgicale seule vs curetage + imiquimod pour le carcinome basocellulaire nodulaire |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Terminé | 20 | Étude en ouvert sur la durée d'effet de l'imiquimod 5 % (3 jours/semaine, 1-2 cycles) pour la kératose actinique du cuir chevelu |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Terminé | 90 | RCT brésilien évaluant l'efficacité de l'imiquimod topique dans les lésions intraépithéliales cervicales de haut grade liées au HPV 16/18 |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Terminé | 5 | Étude exploratoire sur les mécanismes d'échappement immunitaire et l'efficacité de l'imiquimod dans la VIN 2/3 et les condylomes anogénitaux |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | Inconnu | 20 | Sécurité/efficacité de l'imiquimod 3,75 % après cryothérapie pour kératoses actiniques hypertrophiques des mains et avant-bras |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminé | 49 | Comparaison imiquimod 5 %, 0,05 % et formulation nano-encapsulée 0,05 % pour la chéilite actinique (lésion labiale potentiellement maligne) ; essai arrêté |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | Terminé | 16 | Étude pilote néoadjuvante d'imiquimod (agoniste TLR7) dans le carcinome épidermoïde buccal à un stade précoce, usage hors AMM |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Revue Systématique (Cochrane) | Cochrane Database Syst Rev | Interventions pour la néoplasie intraépithéliale anale (AIN), lésion précancéreuse HPV fréquente chez les HSH séropositifs |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Revue Systématique (Cochrane) | Cochrane Database Syst Rev | Traitements médicaux de la néoplasie intraépithéliale vulvaire de haut grade (VIN), sans consensus thérapeutique établi |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Revue | Int J Mol Sci | Traitements combinés par photothérapie dynamique pour les cancers cutanés non mélanome |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Revue | Skin Therapy Lett | Prise en charge actuelle des kératoses actiniques, incluant les traitements topiques de champ (dont imiquimod) |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Revue | Semin Cutan Med Surg | Stratégies topiques pour cancers cutanés non mélanome et lésions précurseurs (5-FU, diclofénac, imiquimod, PDT) |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Cohorte (animale) | Urol Oncol | PK/PD chez le rat de deux agonistes TLR7 (TMX-101/202), utilisés pour lésions cutanées (pré)malignes et à l'étude pour le cancer de vessie |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Rapport de Cas | Int J STD AIDS | Traitement réussi d'une VIN de haut grade par imiquimod 5 % chez une patiente greffée rénale immunodéprimée |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Rapport de Cas | Hautarzt | Imagerie OCT d'une porokératose actinique disséminée, associée à kératoses actiniques et carcinomes épidermoïdes résistants au traitement |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Rapport de Cas | Int J STD AIDS | Papulose bowénoïde du pénis (lésion précancéreuse ano-génitale HPV) traitée avec succès par imiquimod 5 % topique |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le mécanisme d'action de l'imiquimod (agoniste TLR7) est déjà cliniquement validé sur plusieurs néoplasies intraépithéliales (AK, CIN, VIN, AIN), et deux revues systématiques Cochrane ainsi qu'un essai de Phase 2 complet (CIN, n=90) soutiennent la direction — d'où un niveau de preuve L2. Toutefois, l'hétérogénéité de la catégorie « Néoplasme Pré-malin » et l'absence de données réglementaires/sécuritaires structurées imposent une progression encadrée plutôt qu'un feu vert complet.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les mises en garde, contre-indications et interactions médicamenteuses officielles (notice TFDA/EMA) — écart de donnée **bloquant** pour l'évaluation de sécurité (S1)
- Obtenir les données structurées de mécanisme d'action (MOA) via DrugBank
- Évaluer séparément les sous-groupes anatomiques du « Néoplasme Pré-malin » (peau vs muqueuses génitales vs muqueuse orale), dont la force de preuve diffère nettement
- Clarifier la voie d'accès réglementaire en France, le produit n'étant actuellement pas commercialisé (0 AMM)
- Écarter explicitement les essais où l'imiquimod agit comme adjuvant vaccinal dans des cancers invasifs, non pertinents pour cette indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

