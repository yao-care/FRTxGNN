---
layout: default
title: Clofazimine
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 3
---

# Clofazimine
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

# Clofazimine : De la Lèpre et de la Tuberculose Résistante à la Pneumocystose

## Résumé en Une Phrase

Clofazimine est un antibiotique riminophénazine utilisé principalement dans le traitement de la lèpre (maladie de Hansen) et des régimes contre la tuberculose résistante aux médicaments (MDR-TB).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pneumocystose** (infection pulmonaire à *Pneumocystis jirovecii*),
avec **1 essai clinique** et **4 publications** associés à cette direction — bien que le lien mécanistique direct reste à établir.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Lèpre / Tuberculose résistante aux médicaments |
| Nouvelle Indication Prédite | Pneumocystose (*Pneumocystis jirovecii*) |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de la clofazimine ne sont pas disponibles dans le dossier actuel. Sur la base des informations connues dans la littérature, la clofazimine appartient à la classe des riminophénazines : elle agit en produisant des espèces réactives de l'oxygène (ROS) qui perturbent l'équilibre redox cellulaire des bactéries pathogènes — principalement les mycobactéries — et possède également des propriétés anti-inflammatoires accessoires.

La pneumocystose est une infection opportuniste causée par *Pneumocystis jirovecii* (anciennement *P. carinii*), survenant principalement chez les patients immunodéprimés, notamment ceux atteints du VIH/SIDA. La clofazimine est fréquemment utilisée dans ce même contexte épidémiologique : les patients traités par MDT (multithérapie antilépreuse) ou par régimes MDR-TB peuvent présenter un terrain compatible avec des co-infections opportunistes, dont la PCP. C'est par ce canal que TxGNN détecte un lien dans le graphe de connaissances — à travers la co-occurrence de ces pathologies chez les patients VIH.

Cependant, le rationnel mécanistique direct est faible. Aucune activité propre de la clofazimine contre *Pneumocystis jirovecii* n'est actuellement documentée. La haute prédiction TxGNN reflète probablement une association épidémiologique (co-infection SIDA : MAC + PCP chez les mêmes patients) plutôt qu'une action pharmacologique directe sur le pathogène fongique. Le rationnel mécanistique fourni dans le dossier confirme cette interprétation.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT00002058](https://clinicaltrials.gov/study/NCT00002058) | NA | Terminé | N/D | ECR évaluant la clofazimine en prophylaxie des infections à *Mycobacterium avium complex* (MAC) chez des patients VIH à risque. Population incluse présentant un antécédent de pneumocystose à *P. carinii* ou CD4 ≤ 100/mm³, mais l'endpoint principal est le MAC — pertinence pour la pneumocystose tangentielle (Grade C). |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | ECR (MAC) | The Journal of Infectious Diseases | ECR prospectif randomisé évaluant la clofazimine 50 mg/j en prophylaxie du MAC chez 110 patients VIH — population recrutée sur antécédent de pneumocystose à *P. carinii* ou CD4 ≤ 100/mm³ ; endpoint principal MAC, sans données sur la PCP. |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Revue | PI Perspective | Mise à jour sur les infections opportunistes chez les patients VIH ; contexte général incluant PCP et MAC, sans étude directe sur la clofazimine contre *P. jirovecii*. |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Rapport de cas | Infection | Patient SIDA présentant une co-infection à *M. kansasii* compliquée d'une pneumocystose à *P. carinii* — récupération après régime incluant clofazimine + ciprofloxacine (pour mycobactérie) et TMP-SMX (pour PCP) ; rôle de la clofazimine limité à la composante mycobactérienne. |
| [6299154](https://pubmed.ncbi.nlm.nih.gov/6299154/) | 1983 | Rapport de cas | Annals of Internal Medicine | Premier cas décrit d'un patient hémophile présentant une pneumocystose à *P. carinii* associée à une bactériémie à *M. avium-intracellulare* — document historique contextualisant l'épidémiologie des co-infections SIDA, sans implication directe de la clofazimine dans le traitement de la PCP. |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Aucune preuve directe d'activité de la clofazimine contre *Pneumocystis jirovecii* n'est disponible : l'unique essai clinique identifié cible le MAC (hors scope PCP), et les quatre publications se limitent à des rapports de cas ou des revues générales documentant la co-existence épidémiologique des infections opportunistes chez les patients SIDA. Le score TxGNN élevé (99,90 %) reflète vraisemblablement ce biais de co-occurrence dans le graphe de connaissances, et non un effet pharmacologique direct. Par ailleurs, la clofazimine n'est pas commercialisée en France (0 AMM), ce qui constitue un obstacle réglementaire supplémentaire.

**Pour avancer, les éléments suivants sont nécessaires :**
- Études in vitro confirmant (ou infirmant) une activité directe de la clofazimine ou de ses analogues riminophénazines contre *Pneumocystis jirovecii*
- Obtention du mécanisme d'action complet via DrugBank (DG002 — actuellement manquant) pour affiner l'analyse mécanistique
- Données de profil de sécurité via la notice ANSM ou le référentiel EMA (DG001 — actuellement manquant)
- Évaluation de la faisabilité d'une autorisation d'accès spécial (ATU/AAP) en France pour un usage compassionnel éventuel
- Revue systématique des données précliniques sur les riminophénazines dans les infections fongiques et parasitaires opportunistes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

