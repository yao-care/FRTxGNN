---
layout: default
title: Temsirolimus
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 3
---

# Temsirolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Temsirolimus : Du Carcinome Rénal Avancé au Liposarcome

## Résumé en Une Phrase

Temsirolimus (Torisel) est un inhibiteur de mTOR, initialement approuvé pour le carcinome à cellules rénales avancé mais non commercialisé en France/Taïwan à ce jour.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Liposarcome**,
avec **5 essais cliniques** (dont 2 utilisant directement le temsirolimus) et **1 publication** soutenant actuellement cette direction — mais les données de sécurité locales restent manquantes.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome à cellules rénales avancé* |
| Nouvelle Indication Prédite | Liposarcome |
| Score de Prédiction TxGNN | 99,54 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

*Non fourni dans les données réglementaires (le médicament n'est pas commercialisé localement) ; il s'agit de l'indication d'origine documentée publiquement (hors Taïwan/France).

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Temsirolimus est un promédicament (CCI-779) converti en son métabolite actif, le sirolimus, qui inhibe mTORC1 et bloque ainsi la voie de signalisation PI3K/AKT/mTOR — une voie centrale de la prolifération cellulaire.

Cette voie est également fréquemment dérégulée dans le liposarcome, en particulier dans le sous-type dédifférencié, via l'amplification de MDM2/CDK4 et la perte de fonction de PTEN. La similarité mécanistique entre le carcinome rénal (indication d'origine, déjà validée par l'inhibition mTOR) et le liposarcome constitue donc une base biologique plausible pour le repositionnement.

Cette hypothèse est renforcée par un effet de classe : d'autres inhibiteurs de mTOR (sirolimus, évérolimus, ridaforolimus) montrent déjà des signaux d'activité dans les sarcomes avancés, et le temsirolimus lui-même dispose de preuves cliniques directes (essais de phase 1/2) dans les sarcomes des tissus mous et osseux, incluant des cohortes de liposarcome.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Terminé | 24 | Torisel (temsirolimus) + doxorubicine liposomale dans les sarcomes des tissus mous/osseux avancés récidivants (incl. liposarcome) — détermination de dose et évaluation d'efficacité. Preuve directe du médicament. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Terminé | 46 | Cixutumumab + temsirolimus chez des enfants atteints de sarcomes récidivants/réfractaires. Preuve directe du médicament, population pédiatrique. |
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Terminé | 70 | Sirolimus (métabolite actif du temsirolimus) + cyclophosphamide dans le liposarcome myxoïde/chondrosarcome métastatique ou inopérable — preuve de classe (mTOR), spécifique au liposarcome. |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Terminé | 216 | Ridaforolimus (autre inhibiteur mTOR) en monothérapie dans le sarcome avancé, large cohorte — preuve d'effet de classe. |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Actif (non recrutant) | 48 | Ribociclib + évérolimus (autre inhibiteur mTOR) dans le liposarcome dédifférencié avancé et le léiomyosarcome — preuve de classe, spécifique au liposarcome, résultats attendus fin 2025. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Revue | Bulletin du cancer | Revue sur les traitements ciblés des sarcomes rares et tumeurs conjonctives, décrivant les altérations moléculaires (dont la voie mTOR) justifiant les stratégies thérapeutiques ciblées. |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de mTOR/mTORC1) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. La notice officielle (TFDA) n'a pas encore été obtenue, ce qui bloque actuellement l'évaluation de sécurité initiale (S1).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Malgré un niveau de preuve L2 encourageant (essais directs de phase 1/2 avec le temsirolimus dans les sarcomes, dont le liposarcome), une lacune de données bloquante sur les mises en garde/contre-indications (notice TFDA) empêche toute évaluation de sécurité initiale, et le médicament n'a aucune AMM en France/Taïwan.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice officielle TFDA/EMA pour compléter l'évaluation de sécurité S1 (lacune bloquante)
- Compléter les données DrugBank sur le mécanisme d'action et la toxicité (myélosuppression, émétogénicité)
- Suivre les résultats finaux de NCT03114527 (achèvement prévu fin 2025)
- Évaluer la faisabilité d'une demande d'AMM locale, le marché étant actuellement vierge (0 licence)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

