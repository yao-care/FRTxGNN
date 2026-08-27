---
layout: default
title: Tiotropium
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
---

# Tiotropium
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

# Tiotropium : De la BPCO au Trouble Ventilatoire Obstructif (Obstructive Lung Disease)

## Résumé en Une Phrase

Le tiotropium est un bronchodilatateur anticholinergique de longue durée d'action (classe LAMA), utilisé de longue date dans la bronchopneumopathie chronique obstructive (BPCO) — sous les marques Spiriva/HandiHaler/Respimat. Le modèle TxGNN prédit une efficacité pour l'« obstructive lung disease » (trouble ventilatoire obstructif), avec **69 essais cliniques** et **20 publications** disponibles dans le dossier ; il faut toutefois noter que ce terme est l'entité ontologique parente de la BPCO elle-même, ce qui limite la nouveauté réelle du signal (voir section suivante).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | BPCO (bronchopneumopathie chronique obstructive) — connue par la littérature du dossier (cf. rationale du candidat n°5) ; non renseignée dans les données réglementaires structurées |
| Nouvelle Indication Prédite | Obstructive Lung Disease (trouble ventilatoire obstructif) |
| Score de Prédiction TxGNN | 99.99 % |
| Niveau de Preuve | L1 |
| Statut de Marché (Taïwan)* | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

*\*Le dossier source (`taiwan_regulatory`) concerne Taïwan ; aucune donnée française (ANSM) n'est disponible dans cet Evidence Pack.*

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier structuré (« [Data Gap] » sur `original_moa`). Sur la base des informations connues du secteur, le tiotropium est un antagoniste muscarinique de longue durée d'action (LAMA) qui bloque les récepteurs M3 du muscle lisse bronchique, produisant une bronchodilatation prolongée — c'est le mécanisme qui sous-tend son indication historique dans la BPCO (spécialité Spiriva).

**Point de vigilance important** : l'« obstructive lung disease » n'est pas une indication distincte de la BPCO — c'est son terme ontologique parent. Le dossier le confirme explicitement : la justification associée à ce candidat indique que « obstructive lung disease... est le terme ontologique parent de la BPCO/asthme... les preuves se recoupent fortement avec l'entrée "chronic obstructive pulmonary disease", il s'agit du même hit à un niveau ontologique différent, non un signal nouveau et indépendant ». Le score TxGNN élevé (99,99 %) reflète donc surtout la reconnaissance d'un consensus clinique déjà établi plutôt qu'une découverte de repositionnement.

Un signal plus authentiquement nouveau, bien que de niveau de preuve plus modeste (L2, « Research Question »), concerne la BPCO sévère à début précoce (rang 4) : cette sous-population pourrait présenter une susceptibilité génétique différente (p. ex. déficit en alpha-1-antitrypsine), mais les essais actuels ne stratifient pas spécifiquement selon ce sous-type.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02096731](https://clinicaltrials.gov/study/NCT02096731) | N/A | Terminé | 115 397 | Étude observationnelle de population évaluant le risque cardio-pulmonaire des bronchodilatateurs combinés, dont le tiotropium, dans la BPCO |
| [NCT02796677](https://clinicaltrials.gov/study/NCT02796677) | Phase 3 | Terminé | 1 595 | Aclidinium/formotérol vs tiotropium seul dans la BPCO stable (essai tête-à-tête) |
| [NCT00680056](https://clinicaltrials.gov/study/NCT00680056) | Phase 4 | Terminé | 33 | Formotérol+tiotropium vs formotérol seul sur dyspnée et hyperinflation dynamique en BPCO modérée à sévère |
| [NCT00615992](https://clinicaltrials.gov/study/NCT00615992) | N/A | Terminé | 754 | Surveillance post-commercialisation : effet du tiotropium (Spiriva) sur le score d'activités de la vie quotidienne (lignes directrices autrichiennes BPCO) |
| [NCT02489981](https://clinicaltrials.gov/study/NCT02489981) | N/A | Terminé | 359 | Surveillance post-commercialisation de Spiriva Respimat chez des asthmatiques sévères persistants — sécurité en vie réelle |
| [NCT01785433](https://clinicaltrials.gov/study/NCT01785433) | Phase 1/2 | Terminé | 36 | Comparaison pharmacocinétique du tiotropium délivré par BAI, HandiHaler et Respimat chez des patients BPCO |
| [NCT01559116](https://clinicaltrials.gov/study/NCT01559116) | Phase 3 | Terminé | 219 | VIVACITO — profil de fonction pulmonaire sur 24h de tiotropium+olodatérol vs tiotropium seul dans la BPCO |
| [NCT01964352](https://clinicaltrials.gov/study/NCT01964352) | Phase 3 | Terminé | 813 | Efficacité sur 12 semaines de la combinaison fixe tiotropium+olodatérol vs tiotropium et placebo dans la BPCO modérée à sévère |
| [NCT00387088](https://clinicaltrials.gov/study/NCT00387088) | Phase 3 | Terminé | 3 991 | Efficacité et sécurité à long terme (1 an) du tiotropium Respimat 5 mcg sur les exacerbations de BPCO |
| [NCT00168831](https://clinicaltrials.gov/study/NCT00168831) | Phase 3 | Terminé | 1 007 | Comparaison de deux doses de tiotropium Respimat sur un an dans la BPCO |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [29605624](https://pubmed.ncbi.nlm.nih.gov/29605624/) | 2018 | ECR | Lancet Respir Med | DYNAGITO — l'ajout d'olodatérol au tiotropium réduit-il le taux d'exacerbations de BPCO ? |
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Tiotropium vs placebo dans la BPCO stable — efficacité confirmée sur exacerbations et fonction pulmonaire |
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Comparaison tiotropium vs ipratropium dans la BPCO |
| [27271056](https://pubmed.ncbi.nlm.nih.gov/27271056/) | 2016 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | ICS/LABA + tiotropium vs tiotropium seul ou association seule dans la BPCO |
| [19402836](https://pubmed.ncbi.nlm.nih.gov/19402836/) | 2009 | Méta-analyse | Respirology | Efficacité et sécurité du tiotropium chez des patients chinois atteints de BPCO stable |
| [27724909](https://pubmed.ncbi.nlm.nih.gov/27724909/) | 2016 | Revue systématique | BMC Pulm Med | Tiotropium Respimat vs HandiHaler — impact du dispositif d'inhalation sur les résultats cliniques |
| [35510163](https://pubmed.ncbi.nlm.nih.gov/35510163/) | 2022 | Cohorte | Int J COPD | Étude de cohorte multicentrique taïwanaise comparant tiotropium/olodatérol, uméclidinium/vilantérol et indacatérol/glycopyrronium dans la BPCO |
| [36714923](https://pubmed.ncbi.nlm.nih.gov/36714923/) | 2023 | Étude observationnelle | Expert Rev Respir Med | Efficacité et sécurité du tiotropium chez des patients BPCO symptomatiques chinois (étude prospective multicentrique) |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Revue | Respir Res | Revue du développement clinique du tiotropium comme traitement LAMA de première intention (GOLD groupes B, C, D) |
| [22562275](https://pubmed.ncbi.nlm.nih.gov/22562275/) | 2012 | Cohorte | Pneumonol Alergol Pol | Effet du formotérol, formotérol+tiotropium, formotérol+corticostéroïde inhalé et tiotropium seul sur la fonction pulmonaire et la tolérance à l'effort en BPCO |

---

## Informations de Marché

Aucune autorisation de mise sur le marché (AMM) n'est enregistrée dans le dossier. Le statut réglementaire indique « non commercialisé » (0 licence), la liste `licenses` étant vide. Cette absence de données réglementaires structurées constitue en elle-même un frein à toute décision de repositionnement (voir Data Gap DG001, bloquant, ci-dessous).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Le dossier signale par ailleurs une lacune de données **bloquante** (DG001) : les mises en garde et contre-indications de la notice TFDA n'ont pas pu être récupérées, ce qui empêche toute évaluation de sécurité initiale (S1).

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le niveau de preuve global est élevé (L1, essais de phase 3 multiples incluant un essai de grande envergure NCT02096731 à 115 397 patients), mais cette preuve confirme surtout l'indication déjà connue (BPCO/LAMA) plutôt qu'un nouveau signal de repositionnement — l'« obstructive lung disease » étant le terme ontologique parent de la BPCO d'après la justification même du modèle.
- La décision « Proceed with Guardrails » doit donc être comprise comme une **validation de cohérence du modèle** (le TxGNN retrouve correctement l'usage établi du médicament) plutôt qu'une opportunité de repositionnement à fort potentiel commercial.
- Le candidat le plus proche d'un véritable signal nouveau — la BPCO sévère à début précoce (rang 4, L2, « Research Question ») — mérite un examen distinct, à un stade de maturité moindre (S2).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice TFDA (mises en garde, contre-indications) — actuellement bloquante (DG001)
- Données détaillées sur le mécanisme d'action (MOA) depuis DrugBank (DG002)
- Clarification du statut de commercialisation réel (les données actuelles indiquent 0 AMM et un statut « non commercialisé », à vérifier)
- Le cas échéant, analyse stratifiée dédiée à la BPCO sévère à début précoce comme piste de recherche distincte, plutôt que le simple report ontologique de la BPCO générale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

