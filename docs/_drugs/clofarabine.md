---
layout: default
title: Clofarabine
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Clofarabine
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

# Clofarabine : De la Leucémie Lymphoblastique Aiguë Pédiatrique à la Leucémie Myéloïde

## Résumé en Une Phrase

Clofarabine est un analogue nucléosidique de purine de deuxième génération, initialement approuvé par la FDA pour le traitement des patients pédiatriques atteints de leucémie lymphoblastique aiguë (LLA) réfractaire ou en rechute ayant reçu au moins deux lignes de traitement antérieures.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Leucémie Myéloïde (LAM)**, avec **50 essais cliniques** et **20 publications** soutenant actuellement cette direction.
Ce médicament n'est pas commercialisé en France, mais dispose d'une base de preuves cliniques internationales substantielle dans cette nouvelle indication.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Leucémie lymphoblastique aiguë pédiatrique réfractaire/récidivante (approbation FDA ; absence d'AMM en France) |
| Nouvelle Indication Prédite | Leucémie Myéloïde (LAM) |
| Score de Prédiction TxGNN | 99,88 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Bien que les données formelles du mécanisme d'action (MOA) issues de DrugBank ne soient pas encore intégrées dans ce dossier, la littérature clinique disponible (PMID 22957815, PMID 17852710) décrit de manière convergente trois mécanismes complémentaires pour Clofarabine : (1) **inhibition de la ribonucléotide réductase (RNR)**, enzyme clé de la biosynthèse des désoxyribonucléotides, entraînant un effondrement des stocks intracellulaires de dNTP ; (2) **incorporation dans l'ADN et blocage de l'ADN polymérase**, provoquant l'arrêt de la réplication ; (3) **induction directe de l'apoptose** via la déstabilisation de la membrane mitochondriale. Sa résistance structurelle à la phosphorylase et à la déaminase lui confère une stabilité métabolique supérieure à ses prédécesseurs, cladribine et fludarabine.

La leucémie myéloïde aiguë (LAM) et la leucémie lymphoblastique aiguë (LLA) partagent une dépendance biologique critique à la fourniture rapide en désoxyribonucléotides pour soutenir la prolifération incontrôlée des blastes. Dans les cellules LAM, l'activité de la RNR est particulièrement élevée, rendant ces cellules vulnérables à son inhibition. La combinaison avec Cytarabine (Ara-C) exploite une synergie pharmacologique documentée : en inhibant la RNR, Clofarabine élève les concentrations intracellulaires d'Ara-CTP, amplifiant ainsi l'effet cytotoxique de son partenaire en phase S. Cette complémentarité mécanistique constitue la base rationnelle de tous les schémas CloCyA, CIA et CLAM évalués en LAM.

Les données cliniques accumulées confirment la prédiction du modèle TxGNN : de multiples essais de Phase 2 complétés ont démontré des taux de réponse globale (ORR) de 38 à 58 % dans la LAM réfractaire/récidivante. Le schéma CLARA (Clofarabine + Ara-C à dose intermédiaire), évalué dans un essai randomisé de Phase 2 multicentrique à grande échelle (NCT00932412, n = 735) en consolidation pour la LAM du sujet jeune, et les données du registre de programme thérapeutique AML (NCT00454480, n = 2 000 patients âgés) apportent le niveau de preuve L2 actuellement attribuable à cette indication.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT01423175](https://clinicaltrials.gov/study/NCT01423175) | Phase 2 | Inconnu | 60 | Essai randomisé multicentrique comparant ClAraC (Clofarabine + Ara-C × 5 j) vs FLAMSA avant conditionnement à intensité réduite et greffe allogénique pour LAM à haut risque et SMD avancé ; évalue l'activité antileucémique, l'immunosuppression et la tolérance de Clofarabine en contexte de préconditionnement |
| [NCT01794702](https://clinicaltrials.gov/study/NCT01794702) | Phase 1/2 | Terminé | 65 | Phase 1 : détermination de la dose maximale tolérée de Clofarabine en association avec Décitabine, Idarubicine et Cytarabine (DAC+CIA) dans la leucémie aiguë. Phase 2 : évaluation de l'efficacité du schéma quadruple ; résultats robustes sur le contrôle de la maladie avec suivi complet |
| [NCT00044889](https://clinicaltrials.gov/study/NCT00044889) | Phase 2 | Terminé | 40 | Étude en monothérapie de Clofarabine (open-label) chez des adultes avec LAM réfractaire ou en rechute précoce ; données fondatrices sur l'activité en agent unique, base de l'approbation FDA pédiatrique ALL et des développements ultérieurs en LAM adulte |
| [NCT01188174](https://clinicaltrials.gov/study/NCT01188174) | Phase 2 | Terminé | 26 | Traitement séquentiel prospectif combinant Clofarabine/Ara-C en rattrapage suivi d'un conditionnement à intensité réduite (RIC) allo-SCT pour LAM en échec primaire d'induction ; établit la faisabilité et l'efficacité de la stratégie pont-vers-greffe |
| [NCT00067028](https://clinicaltrials.gov/study/NCT00067028) | Phase 2 | Terminé | 116 | Essai randomisé prospectif comparant trois schémas : Clo/Ara-C vs Clo/Idarubicine vs Clo+Ida+Ara-C dans la LAM en première rechute ou premier rattrapage, ainsi que SMD à haute teneur en blastes et LMC en phase blastique ; données comparatives directes sur les trois combinaisons |
| [NCT00932412](https://clinicaltrials.gov/study/NCT00932412) | Phase 2 | Terminé | 735 | Essai randomisé multicentrique majeur (CLARA) : Clofarabine + Ara-C intermédiaire vs Ara-C haute dose (HDAC) en consolidation pour LAM du sujet jeune sans indication de greffe après rémission complète ; premier essai randomisé à grande échelle comparant Clofarabine en phase de consolidation |
| [NCT01295307](https://clinicaltrials.gov/study/NCT01295307) | Phase 2 | Terminé | 86 | Clofarabine en rattrapage pour LAM R/R avec objectif de permettre l'accès à l'allogreffe chez des patients plus jeunes ; analyse de la proportion de patients bridgés vers la greffe et facteurs pronostiques associés à la réponse |
| [NCT02686593](https://clinicaltrials.gov/study/NCT02686593) | Phase 2 | Terminé | 50 | Évaluation du schéma CLAM (Clofarabine 30 mg/m²/j J1–5 + Cytarabine 750 mg/m²/j J1–5 + Mitoxantrone 12 mg/m²/j J3–5) en premier rattrapage pour LAM réfractaire au schéma daunorubicine/cytarabine standard ; taux de rémission complète et capacité de bridging vers allogreffe |
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | Terminé | 2 000 | Programme thérapeutique multibras pour patients âgés atteints de LAM et SMD à haut risque, intégrant Clofarabine, Gemtuzumab ozogamicine et Tipifarnib ; cohorte la plus large disponible dans cette population avec évaluation comparative de stratégies incluant Clofarabine |
| [NCT01101880](https://clinicaltrials.gov/study/NCT01101880) | Phase 2 | Terminé | 50 | Clofarabine + Cytarabine haute dose + G-CSF (priming) chez des patients < 65 ans avec LAM nouvellement diagnostiquée, SMD avancé ou néoplasme myéloprolifératif avancé ; données d'efficacité en induction pour la LAM de novo |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [31281098](https://pubmed.ncbi.nlm.nih.gov/31281098/) | 2019 | Revue Systématique / Méta-analyse | The Lancet. Oncology | Synthèse de niveau 1 sur Clofarabine et Cytarabine dans la LAM ; consolide les données d'efficacité et de tolérance de la combinaison CloCyA issues de plusieurs essais cliniques |
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | ECR | J Clin Oncol | Essai AML08 multicenter randomisé : Clofarabine peut remplacer les anthracyclines et l'étoposide dans l'induction de rémission de la LAM pédiatrique (cours 1) avec efficacité comparable et profil de toxicité favorable ; résultats de survie à long terme |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Revue | Leukemia & Lymphoma | Ghanem et al. : rôle de Clofarabine dans la LAM — mécanismes d'action détaillés (inhibition RNR + DNA polymérase), résistance aux enzymes d'inactivation, données d'efficacité en monothérapie et en association, recommandations de schémas |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | Revue Critique | Critical Reviews Oncology/Hematology | Fozza et al. : analyse complète du rôle de Clofarabine chez les adultes atteints de LAM — développement en monothérapie, stratégies combinatoires en première et deuxième ligne, populations cibles, perspectives futures |
| [31905904](https://pubmed.ncbi.nlm.nih.gov/31905904/) | 2019 | Analyse Post-hoc d'ECR | Cancers | Fenwarth et al. : le schéma CLARA améliore spécifiquement la survie sans rechute dans la LAM du sujet jeune avec caryotype micro-complexe (SNP-array), identifiant un sous-groupe cytogénétique bénéficiaire du traitement par Clofarabine |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Phase 2 (Cohorte Rétrospective) | Cancer Medicine | Gill et al. : schéma CLAM dans la LAM R/R (n = 50) — taux de réponse élevés chez les 18–65 ans en rechute après 3+7 standard ; efficacité de bridging vers l'allogreffe démontrée |
| [36336258](https://pubmed.ncbi.nlm.nih.gov/36336258/) | 2023 | Cohorte Rétrospective | Transplantation and Cellular Therapy | Connor et al. : conditionnement myéloablatif Clofarabine/Busulfan 4 (Clo/Bu4) pour malignités myéloïdes actives chimiorésistantes avant allogreffe ; activité antileucémique avec tolérance acceptable jusqu'à 70 ans |
| [17852710](https://pubmed.ncbi.nlm.nih.gov/17852710/) | 2007 | Revue | Leukemia & Lymphoma | Kantarjian et al. : « Clofarabine : passé, présent et futur » — revue fondatrice décrivant les trois mécanismes d'action, la pharmacocinétique, les données précliniques et les premières données d'efficacité clinique en LAM |
| [19852733](https://pubmed.ncbi.nlm.nih.gov/19852733/) | 2009 | Revue Perspective | Future Oncology | Thomas et al. : Clofarabine pour la LAM adulte — activité en monothérapie comparable aux agents standard, combinaisons en évaluation, intégration future probable dans les schémas d'induction et de consolidation |
| [23526416](https://pubmed.ncbi.nlm.nih.gov/23526416/) | 2013 | Expert Review | American J Hematology | Estey et al. : mise à jour 2013 sur la stratification du risque et la prise en charge de la LAM ; contextualise la place de Clofarabine dans les algorithmes thérapeutiques contemporains par strate de risque |

---

## Cytotoxicité

| Élément | Contenu |
|---|---|
| Classification de Cytotoxicité | Cytotoxique conventionnel — Analogue nucléosidique de purine de 2ème génération (classe des désoxyadenosines dihalogénées) |
| Risque de Myélosuppression | **Élevé** — myélosuppression sévère et prolongée attendue (neutropénie fébrile, thrombocytopénie et anémie de grade ≥3 fréquentes ; les essais cliniques rapportent systématiquement des taux élevés de toxicités hématologiques nécessitant un suivi rapproché et un soutien transfusionnel) |
| Classification d'Émétogénicité | Faible à modérée (profil similaire aux autres analogues nucléosidiques IV ; prophylaxie antiémétique de bas niveau recommandée, à intensifier selon les associations médicamenteuses) |
| Éléments de Surveillance | NFS avec différentielle (avant chaque cycle et hebdomadaire pendant le traitement), bilan hépatique complet (ASAT, ALAT, bilirubine, phosphatases alcalines), fonction rénale (créatinémie, DFG estimé), électrolytes, surveillance du syndrome de lyse tumorale (uricémie, LDH, phosphore, calcium) |
| Protection de Manipulation | Obligatoire — préparation exclusive en pharmacie hospitalière sous hotte à flux laminaire, manipulation avec équipements de protection individuelle complets selon les protocoles nationaux de gestion des médicaments cytotoxiques |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Clofarabine dispose d'une base de preuves cliniques substantielle dans la leucémie myéloïde aiguë, soutenue par de multiples essais de Phase 2 complétés et un essai randomisé à grande échelle (NCT00932412, n = 735 ; schéma CLARA) ; le mécanisme de double inhibition RNR + ADN polymérase est parfaitement adapté aux caractéristiques prolifératives des blastes myéloïdes, et la synergie pharmacologique avec Cytarabine est solidement documentée. L'absence d'AMM en France constitue le principal obstacle réglementaire à l'usage clinique direct.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération des données complètes sur le mécanisme d'action via DrugBank (lacune DG002 identifiée)
- Obtention et analyse des mises en garde officielles et contre-indications de la notice (lacune DG001 — niveau Bloquant)
- Évaluation de la stratégie d'accès réglementaire en France : procédure d'AMM centralisée EMA, accès précoce (ATU/AAP) via l'ANSM, ou usage compassionnel
- Définition de la population cible prioritaire selon le profil de développement envisagé (LAM R/R chez l'adulte vs. consolidation chez le sujet jeune vs. population pédiatrique)
- Plan de surveillance de sécurité adapté aux sous-populations à risque (patients âgés ≥ 60 ans, insuffisance hépatique ou rénale préexistante, antécédents de greffe)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

