---
layout: default
title: Terbutaline
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 3
---

# Terbutaline
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

# Terbutaline : De l'Usage Établi en Bronchodilatation vers une Confirmation en Maladie Pulmonaire Obstructive

## Résumé en Une Phrase

La terbutaline est un bêta-2-agoniste utilisé comme bronchodilatateur ; les données réglementaires françaises officielles sur son indication d'origine ne sont pas disponibles dans ce dossier, mais les essais cliniques recensés montrent qu'elle est déjà largement employée dans l'asthme et la bronchopneumopathie chronique obstructive (BPCO). Le modèle TxGNN confirme cette direction en prédisant une efficacité pour la **Maladie Pulmonaire Obstructive** (« obstructive lung disease »), avec **48 essais cliniques** et **20 publications** disponibles — mais aucune AMM ni fiche de sécurité TFDA/ANSM n'est actuellement enregistrée en France.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible via AMM française (aucune licence enregistrée) — selon les essais cliniques inclus, la terbutaline est utilisée comme bronchodilatateur dans l'asthme et les états de mal asthmatique |
| Nouvelle Indication Prédite | Maladie Pulmonaire Obstructive (asthme / BPCO) |
| Score de Prédiction TxGNN | 99.96 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier (donnée manquante de sévérité élevée). Sur la base des informations connues issues des essais cliniques inclus, la terbutaline appartient à la classe des bêta-2-agonistes à courte durée d'action (formes Bricanyl®/Turbuhaler®), utilisée comme bronchodilatateur de secours dans l'asthme, y compris l'état de mal asthmatique (status asthmaticus).

La particularité de ce dossier est que la « nouvelle indication prédite » — la maladie pulmonaire obstructive (asthme/BPCO) — correspond en réalité à l'usage déjà documenté du médicament : dans la quasi-totalité des essais cliniques recensés, la terbutaline apparaît comme traitement de secours de référence (comparateur actif « as needed ») face à des associations ICS/LABA (Symbicort®, Seretide®) dans l'asthme, ou en add-on dans la BPCO. Il s'agit donc moins d'un repositionnement thérapeutique inédit que d'une confirmation, par le modèle TxGNN, d'un usage clinique déjà bien établi et documenté dans la littérature.

Mécanistiquement, l'action bronchodilatatrice bêta-2-adrénergique de la terbutaline est directement pertinente pour l'obstruction bronchique réversible caractéristique de l'asthme et, dans une moindre mesure, de la BPCO — ce qui explique la cohérence entre la prédiction du modèle et le corpus d'essais existant.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Phase 3 | Terminé | 4215 | Symbicort® à la demande vs Pulmicort® biquotidien + terbutaline à la demande dans l'asthme léger |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Phase 3 | Terminé | 3850 | Symbicort® à la demande vs terbutaline à la demande vs Pulmicort®+terbutaline à la demande |
| [NCT00242775](https://clinicaltrials.gov/study/NCT00242775) | Phase 3 | Terminé | 2100 | Symbicort® vs Seretide®+terbutaline à la demande dans l'asthme persistant (étude AHEAD) |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | Terminé | 2091 | Symbicort® SMART vs Symbicort®+terbutaline à la demande, 12 mois |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Phase 3 | Terminé | 860 | Budésonide/formotérol à la demande vs traitement régulier+terbutaline à la demande dans l'asthme persistant léger-modéré |
| [NCT00326053](https://clinicaltrials.gov/study/NCT00326053) | Phase 3 | Terminé | 600 | Budésonide/formotérol vs budésonide+terbutaline pour la prévention des rechutes d'asthme après urgences |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Phase 3 | Terminé | 95 | Bricanyl® (terbutaline) Turbuhaler M3 vs M2 : effet protecteur contre la bronchoconstriction à la méthacholine |
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Phase 3 | Terminé | 120 | Sulfate de magnésium IV vs terbutaline chez l'enfant en exacerbation aiguë d'asthme (2024) |
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Phase 3 | Terminé | 24 | Terbutaline Turbuhaler® 0,4 mg vs salbutamol pMDI 200 μg chez des patients asthmatiques japonais |
| [NCT00837967](https://clinicaltrials.gov/study/NCT00837967) | Phase 3 | Terminé | 25 | Tolérabilité de la terbutaline Turbuhaler® en add-on à Symbicort® chez des patients asthmatiques japonais |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | ECR | Acad Emerg Med | Terbutaline + ipratropium nébulisés vs terbutaline seule dans l'exacerbation aiguë de BPCO sous ventilation non invasive |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | ECR (double insu) | Br J Dis Chest | Terbutaline orale et fonction diaphragmatique dans la BPCO |
| [8296260](https://pubmed.ncbi.nlm.nih.gov/8296260/) | 1993 | Étude comparative | Thorax | Réversibilité bronchodilatatrice à faible/forte dose de terbutaline et d'ipratropium dans la BPCO |
| [6107217](https://pubmed.ncbi.nlm.nih.gov/6107217/) | 1980 | ECR (double insu, croisé) | Chest | Interaction bêta-bloquants et terbutaline dans la BPCO |
| [1615190](https://pubmed.ncbi.nlm.nih.gov/1615190/) | 1992 | ECR (double insu, croisé) | Respir Med | Effet de la terbutaline inhalée sur le VEMS, la CVF, la dyspnée et le périmètre de marche dans la BPCO |
| [2951811](https://pubmed.ncbi.nlm.nih.gov/2951811/) | 1986 | Étude randomisée | Respiration | Comparaison fénotérol-ipratropium vs terbutaline dans la BPCO |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | ECR (double insu) | Int J Clin Pharmacol Ther Toxicol | Clenbutérol oral vs terbutaline dans la BPCO, étude de 2 semaines |
| [2031046](https://pubmed.ncbi.nlm.nih.gov/2031046/) | 1991 | Étude randomisée croisée | Pneumologie | Terbutaline nébulisée et pression expiratoire positive dans la BPCO |
| [18761816](https://pubmed.ncbi.nlm.nih.gov/18761816/) | 2008 | Étude clinique | Cell Mol Immunol | Inhalation par atomisation de terbutaline et budésonide : amélioration de l'immunité et de la fonction pulmonaire dans l'exacerbation aiguë de BPCO |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | ECR (double insu, croisé) | Lung | Effet de la terbutaline sur la capacité d'exercice et la fonction pulmonaire dans la BPCO |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité (aucune donnée TFDA/ANSM sur les mises en garde, contre-indications ou interactions médicamenteuses n'est disponible dans ce dossier).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le niveau de preuve clinique est élevé (L1, avec de multiples essais de Phase 3 terminés confirmant l'usage de la terbutaline dans l'asthme et la BPCO), mais l'évaluation ne peut pas avancer : l'absence des mises en garde/contre-indications TFDA (donnée manquante bloquante, DG001) empêche l'évaluation de sécurité initiale (S1), et le médicament n'a actuellement aucune AMM en France (0 licence, statut « non commercialisé »).

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice/l'étiquetage officiel (mises en garde, contre-indications, interactions) auprès de la source réglementaire compétente
- Compléter les données de mécanisme d'action (MOA) via DrugBank (DG002)
- Clarifier le statut réglementaire réel de la terbutaline en France (import, ATU, ou absence totale de commercialisation) avant toute décision de repositionnement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

