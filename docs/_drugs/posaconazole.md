---
layout: default
title: Posaconazole
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 1
---

# Posaconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# POSACONAZOLE : Des Infections Fongiques Invasives Vers la Pneumocystose

## Résumé en Une Phrase

Le posaconazole est un antifongique triazolé, historiquement utilisé en prophylaxie des infections fongiques invasives chez les patients immunodéprimés à haut risque.
Le modèle TxGNN prédit qu'il pourrait être pertinent pour la **pneumocystose**,
avec **2 essais cliniques** et **5 publications** actuellement recensés en lien avec ce champ, mais dont la pertinence directe reste à confirmer.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Prophylaxie des infections fongiques invasives *(non renseignée dans les données source ; classification générale connue du produit — voir section suivante)* |
| Nouvelle Indication Prédite | Pneumocystose |
| Score de Prédiction TxGNN | 99.77 % |
| Niveau de Preuve | L3 |
| Statut de Marché en Taïwan | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont actuellement pas disponibles dans le dossier source (écart de données DG002, sévérité élevée). Sur la base des informations générales connues, le posaconazole fait partie de la classe des antifongiques triazolés, dont l'action repose sur l'inhibition de la synthèse de l'ergostérol fongique. Son efficacité en prophylaxie des infections fongiques invasives (aspergillose, candidose) chez les patients hémato-oncologiques et greffés a été largement démontrée, ce qui pourrait justifier mécanistiquement un intérêt pour la prévention d'autres infections fongiques opportunistes telles que la pneumocystose chez des populations à risque similaire (immunodépression sévère, allogreffe).

Cependant, il est important de noter que la pneumocystose (due à *Pneumocystis jirovecii*) est classiquement traitée en première intention par le triméthoprime-sulfaméthoxazole, et non par les azolés. La pertinence de cette prédiction TxGNN repose donc davantage sur un chevauchement épidémiologique de populations à risque (patients immunodéprimés, greffés) que sur une preuve pharmacologique directe et spécifique.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Terminé | 602 | Étude comparant le rezafungin IV au traitement antifongique standard pour la prévention des infections fongiques invasives chez les greffés de moelle/sang allogéniques ; le posaconazole n'est pas le médicament étudié mais peut figurer dans le bras "traitement standard". |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | En cours de recrutement | 358 | Étude plateforme comparant des schémas de prophylaxie du GVHD après greffe de cellules souches à donneur non apparenté ; n'évalue pas spécifiquement le posaconazole ni la pneumocystose. |

*Remarque : aucun de ces essais n'évalue directement le posaconazole dans le traitement ou la prévention de la pneumocystose ; la pertinence indiquée dans le dossier source est encore "en attente d'évaluation".*

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Recommandation | The Lancet Infectious Diseases | Recommandations de bonnes pratiques (British Society for Medical Mycology) sur le diagnostic des maladies fongiques graves, incluant la pneumocystose. |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Revue | Swiss Medical Weekly | Vue d'ensemble des infections fongiques invasives (candidose, aspergillose, cryptococcose, pneumonie à Pneumocystis) ; mentionne le rôle prophylactique du posaconazole dans la réduction de la candidose invasive chez les patients à haut risque. |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Recommandation | Zhonghua Jie He He Hu Xi Za Zhi | Lignes directrices chinoises 2025 pour le diagnostic et la prise en charge des maladies fongiques pulmonaires invasives. |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revue pharmacocinétique | Clinical Pharmacokinetics | Revue de la pénétration pulmonaire des agents anti-infectieux, incluant les antifongiques comme le posaconazole. |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Étude rétrospective | Transplant Infectious Disease | Complications infectieuses du GVHD aigu après transplantation hépatique ; contexte de population à risque d'infections fongiques opportunistes. |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Les preuves disponibles pour l'association posaconazole–pneumocystose restent indirectes : les essais cliniques identifiés évaluent d'autres médicaments (rezafungin) ou des schémas de prophylaxie plus larges, sans porter spécifiquement sur le posaconazole ni sur la pneumocystose, et la littérature est majoritairement composée de recommandations et revues générales plutôt que d'essais contrôlés dédiés. Surtout, l'absence totale de données de sécurité TFDA (mises en garde, contre-indications — DG001, sévérité bloquante) empêche toute évaluation de sécurité de niveau S1, et le produit n'est pas commercialisé à Taïwan (0 AMM).

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les mises en garde et contre-indications TFDA (DG001, bloquant)
- Obtenir le mécanisme d'action détaillé via l'API DrugBank (DG002)
- Compléter la classification de pertinence ("pending") des essais cliniques et publications listés, en confirmant si le posaconazole est réellement utilisé comme comparateur standard
- Rechercher des études cliniques dédiées évaluant spécifiquement le posaconazole en prévention ou traitement de la pneumocystose
- Clarifier le statut réglementaire local avant toute démarche de repositionnement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

