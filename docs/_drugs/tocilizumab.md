---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 312
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab : De la Polyarthrite Rhumatoïde à la Spondylarthrite Ankylosante

## Résumé en Une Phrase

Tocilizumab est un anticorps monoclonal anti-récepteur de l'IL-6, dont l'usage documenté dans la littérature disponible concerne la polyarthrite rhumatoïde et l'arthrite juvénile idiopathique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Spondylarthrite Ankylosante**, avec un score de **99,99%**,
soutenu par **9 essais cliniques** et **19 publications** — mais les deux essais de Phase 3 spécifiquement dédiés à cette indication ont été **interrompus**, ce qui constitue une preuve directe négative plutôt qu'une simple lacune de données.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde (d'après la littérature disponible dans le dossier ; données réglementaires TFDA non disponibles) |
| Nouvelle Indication Prédite | Spondylarthrite Ankylosante |
| Score de Prédiction TxGNN | 99,99% |
| Niveau de Preuve | L1 (voir mise en garde ci-dessous) |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action n'ont pas pu être récupérées depuis DrugBank (lacune bloquante référencée dans le dossier). Sur la base des informations disponibles dans la littérature associée, tocilizumab est un anticorps monoclonal humanisé qui bloque le récepteur de l'interleukine-6 (IL-6R), initialement développé pour la polyarthrite rhumatoïde et les formes systémique/polyarticulaire de l'arthrite juvénile idiopathique, où l'IL-6 joue un rôle pathogénique central.

La spondylarthrite ankylosante partage avec la polyarthrite rhumatoïde un terrain inflammatoire auto-immun articulaire, ce qui rend l'hypothèse de repositionnement biologiquement plausible et explique le score TxGNN élevé. Cependant, la spondylarthrite ankylosante est une maladie dont la physiopathologie repose davantage sur l'axe IL-17/TNF que sur l'IL-6, ce qui limite a priori la pertinence mécanistique du blocage de l'IL-6 seul.

Ce doute mécanistique est confirmé par les données cliniques réelles : les deux essais de Phase 3 spécifiquement conçus pour tester tocilizumab dans la spondylarthrite ankylosante (NCT01209689 et NCT01209702) ont été **interrompus**, ce qui constitue une preuve directe que l'efficacité attendue ne s'est pas confirmée dans cette population — et non une simple absence de données.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Interrompu | 113 | RCT contrôlé placebo chez patients SA en échec d'un anti-TNF ; essai **interrompu** (preuve négative directe) |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | Interrompu | 306 | RCT « seamless » chez patients SA naïfs d'anti-TNF ; essai **interrompu** (preuve négative directe) |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Phase 2 | Pas encore en recrutement | 52 | Essai bayésien sur le secukinumab (autre molécule) dans la maladie de Takayasu ; population non confirmée |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Terminé | 60 | Étude mécanistique sur les cellules T folliculaires auxiliaires — population PR, non SA |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | En recrutement | 2500 | Profilage de cytokines dans les maladies inflammatoires systémiques, non interventionnel |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | En recrutement | 10000 | Registre coréen des biothérapies (PR, SA, arthrite psoriasique), observationnel |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Pas encore en recrutement | 80 | Gestion périopératoire des immunosuppresseurs en chirurgie de l'épaule, non lié à l'efficacité |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Terminé | 1431 | Registre national d'utilisation réelle de l'Infliximab — autre molécule |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Statut inconnu | 750000 | Registre de risque de maladies inflammatoires immuno-médiées multiples sous biothérapies |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | ECR | Annals of the Rheumatic Diseases | Rapporte les essais BUILDER-1/2 (= NCT01209689 et NCT01209702, tous deux interrompus) évaluant l'efficacité symptomatique à court terme du tocilizumab dans la SA |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Revue systématique / Méta-analyse en réseau | Medicine | Comparaison de l'efficacité des différentes biothérapies disponibles dans la SA |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Revue | Inflammation & Allergy Drug Targets | Discussion du rôle de l'IL-6 (par rapport au TNF-α et à l'IL-10) dans la physiopathologie de la SA |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Méta-analyse | Clinical Rheumatology | Risque d'infections graves sous biothérapies dans la SA et la spondyloarthrite axiale non radiographique |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Cas clinique | Frontiers in Medicine | Traitement réussi de l'amylose AA secondaire compliquant une SA, par tocilizumab (2 cas) |
| [20959960](https://pubmed.ncbi.nlm.nih.gov/20959960/) | 2011 | Revue | Osteoporosis International | Effets osseux systémiques des biothérapies dans la PR et la SA |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Revue | Seminars in Arthritis and Rheumatism | Optimisation de la biothérapie de seconde ligne dans PR, arthrite psoriasique et SA |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Revue | Clinical and Experimental Rheumatology | Différences physiopathologiques entre PR et SA et implications pour les biothérapies |
| [21803631](https://pubmed.ncbi.nlm.nih.gov/21803631/) | 2011 | Revue | Joint Bone Spine | Agents biologiques pour la SA au-delà des antagonistes du TNFα |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Revue | Current Opinion in Rheumatology | Options thérapeutiques chez les patients SA réfractaires aux anti-TNF |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Malgré un score TxGNN très élevé (99,99%) et un volume important d'essais et de publications, les deux essais de Phase 3 spécifiquement dédiés à la spondylarthrite ankylosante (NCT01209689, NCT01209702) ont été interrompus — une preuve clinique directe que le blocage de l'IL-6 seul n'a pas atteint les résultats attendus dans cette population, cohérent avec une physiopathologie de la SA davantage portée par l'axe IL-17/TNF.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications officielles TFDA (lacune bloquante actuelle, empêche l'évaluation de sécurité S1)
- Données détaillées de mécanisme d'action via DrugBank
- Résultats complets (critères d'efficacité, pas seulement le statut d'arrêt) des essais NCT01209689 et NCT01209702
- Confirmation du statut réglementaire réel (marché non identifié dans le dossier actuel)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

