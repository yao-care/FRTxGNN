---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 1
---

# Olaparib
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

Utilisation du modèle de rapport pour générer l'évaluation Olaparib (Neoplasme du sein).

# Olaparib : Du Cancer de l'Ovaire BRCA-Muté au Cancer du Sein (Female Breast Carcinoma)

## Résumé en Une Phrase

Olaparib est un inhibiteur de PARP1/2, initialement développé et utilisé pour le traitement d'entretien du cancer de l'ovaire épithélial de haut grade, muté BRCA, sensible au platine. Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Cancer du Sein (Female Breast Carcinoma)**, avec **50 essais cliniques** et **20 publications** soutenant actuellement cette direction — dont plusieurs essais de Phase III déjà complétés (OlympiAD, OlympiA).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer de l'ovaire épithélial de haut grade, muté BRCA, sensible au platine (traitement d'entretien) — non commercialisé en France, aucune AMM enregistrée dans ce dossier |
| Nouvelle Indication Prédite | Cancer du Sein (Female Breast Carcinoma) |
| Score de Prédiction TxGNN | 99.09% |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Olaparib est un inhibiteur de PARP1/2 qui agit par un mécanisme de létalité synthétique ciblant les cellules tumorales présentant un déficit de recombinaison homologue (HRD), notamment celles porteuses de mutations BRCA1/2. En bloquant la réparation des cassures simple-brin de l'ADN, il provoque l'effondrement des fourches de réplication et la mort des cellules déficientes en recombinaison homologue. Ce mécanisme n'est pas une simple association statistique issue de TxGNN : il repose sur une base biochimique bien établie et déjà validée cliniquement.

Le cancer de l'ovaire et le cancer du sein partagent tous deux une sous-population de tumeurs BRCA1/2-mutées ou HRD-positives, indépendamment de l'organe d'origine. Comme la vulnérabilité thérapeutique exploitée par olaparib (déficit de réparation de l'ADN) est définie par le statut génomique de la tumeur plutôt que par son tissu d'origine, l'extension mécanistique du cancer de l'ovaire vers le cancer du sein est cohérente sur le plan pharmacologique.

Cette cohérence est renforcée par le volume de preuves cliniques déjà accumulé : les essais pivots OlympiAD (métastatique) et OlympiA (adjuvant) ont établi l'efficacité d'olaparib spécifiquement dans le cancer du sein HER2-négatif BRCA1/2-muté, ce qui explique le score de prédiction TxGNN élevé (99.09%) — la relation n'est pas seulement prédite mais largement corroborée par la littérature de Phase III.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Complété | 266 | Essai pivot randomisé (base d'OlympiAD) : olaparib monothérapie vs chimiothérapie au choix du médecin chez patientes gBRCA1/2-mutées, cancer de l'ovaire sensible au platine — établit le profil d'efficacité/sécurité exploité pour l'extension au sein. |
| [NCT03402841](https://clinicaltrials.gov/study/NCT03402841) | Phase 3b | Complété | 279 | Étude multicentrique à bras unique évaluant olaparib en traitement d'entretien chez patientes non-gBRCA, cancer de l'ovaire de haut grade sensible au platine — soutient l'applicabilité au-delà des porteuses germinales strictes. |
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | Complété | 99 | AZD2281 (nom de développement d'olaparib) chez porteuses BRCA, cancer de l'ovaire et cancer du sein triple négatif — étude fondatrice ayant établi le taux de réponse objective dans le sein BRCA-muté. |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Complété | 202 | Étude post-commercialisation en Inde chez patientes avec cancer de l'ovaire sensible au platine et cancer du sein métastatique gBRCA1/2-muté — preuve de sécurité/efficacité en vie réelle incluant spécifiquement le sein. |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | Complété | 25 | Carboplatine-olaparib puis olaparib en monothérapie vs capécitabine, en première ligne du cancer du sein avancé HER2-négatif BRCA1/2-muté — preuve directe de concept dans l'indication ciblée. |
| [NCT03162627](https://clinicaltrials.gov/study/NCT03162627) | Phase 1 | Actif, non recrutant | 90 | Combinaison sélumétinib + olaparib dans tumeurs solides avancées (endomètre, ovaire, autres) avec altérations de la voie Ras — exploratoire, non spécifique au sein. |
| [NCT04421963](https://clinicaltrials.gov/study/NCT04421963) | Phase 3 | Actif, non recrutant | 185 | Étude de prolongation (roll-over) pour patients bénéficiant cliniquement d'un traitement antérieur par olaparib — données de suivi de sécurité à long terme, non une preuve d'efficacité indépendante. |
| [NCT05564377](https://clinicaltrials.gov/study/NCT05564377) | Phase 2 | Recrutement en cours | 2900 | Plateforme de dépistage moléculaire ComboMATCH orientant vers des combinaisons thérapeutiques selon le profil génétique — multi-cancers, non spécifique au sein. |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | ECR (Phase 3) | New England Journal of Medicine | Essai OlympiA : olaparib adjuvant réduit significativement la récidive du cancer du sein précoce à haut risque, BRCA1/2 germinal-muté. |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | ECR (Phase 3) | New England Journal of Medicine | Essai OlympiAD : olaparib démontre une activité antitumorale prometteuse dans le cancer du sein métastatique gBRCA-muté. |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | ECR (Phase 3) | Annals of Oncology | Survie globale de l'essai OlympiA : bénéfice confirmé de l'olaparib adjuvant chez les patientes BRCA1/2 à haut risque. |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | ECR (Phase 3) | Annals of Oncology | OlympiAD, résultats finaux de survie globale et tolérance : olaparib améliore la survie sans progression vs chimiothérapie standard. |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | ECR (Phase 3, suivi étendu) | European Journal of Cancer | Suivi étendu d'OlympiAD confirmant le profil de sécurité et la tendance de survie globale à plus long terme. |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | ECR (Phase 2 adaptatif) | Cancer Cell | Essai I-SPY2 : ajout de durvalumab + olaparib au paclitaxel néoadjuvant augmente le taux de réponse pathologique complète, cancer du sein stade II/III HER2-négatif. |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Étude de cohorte (Phase 2) | Journal of Clinical Oncology | TBCRC 048 : olaparib actif dans le cancer du sein métastatique porteur de mutations somatiques BRCA1/2 ou d'autres gènes de recombinaison homologue. |
| [39520738](https://pubmed.ncbi.nlm.nih.gov/39520738/) | 2024 | Étude de Phase 2 (bras unique) | Breast (Edinburgh) | NOBROLA : olaparib en monothérapie efficace dans le cancer du sein triple négatif avancé avec déficit de recombinaison homologue, sans mutation germinale BRCA1/2. |
| [38112922](https://pubmed.ncbi.nlm.nih.gov/38112922/) | 2024 | Étude en vie réelle (Phase 3b) | Breast Cancer Research and Treatment | LUCY, analyse finale : efficacité et sécurité d'olaparib confirmées en pratique réelle, cohérentes avec l'essai OlympiAD. |
| [25366685](https://pubmed.ncbi.nlm.nih.gov/25366685/) | 2015 | Étude de Phase 2 (panier) | Journal of Clinical Oncology | Olaparib en monothérapie montre une activité chez les patientes porteuses d'une mutation germinale BRCA1/2, sein et ovaire confondus — données fondatrices précoces. |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de PARP1/2, létalité synthétique) — non un agent cytotoxique conventionnel |
| Risque de Myélosuppression | Données non disponibles dans ce dossier — veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Données non disponibles dans ce dossier — veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Données non disponibles dans ce dossier — veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Données non disponibles dans ce dossier — veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune donnée de mise en garde, contre-indication ou interaction médicamenteuse n'est disponible dans ce dossier (le TFDA/registre français et la base DDI n'ont retourné aucun résultat).

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Le niveau de preuve L1 est atteint grâce à plusieurs essais de Phase III complétés (OlympiAD, OlympiA, LUCY IIIb) démontrant un bénéfice clinique constant d'olaparib dans le cancer du sein BRCA1/2-muté, avec un mécanisme d'action bien caractérisé et transposable de l'ovaire au sein. Toutefois, le médicament n'est pas commercialisé en France (0 AMM) et les données de sécurité réglementaire locales sont totalement absentes, ce qui impose des garde-fous avant toute utilisation clinique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice/RCP officielle (TFDA ou équivalent français) : mises en garde, contre-indications, interactions médicamenteuses — actuellement bloquant (DG001)
- Confirmation du statut réglementaire et d'une éventuelle AMM en France
- Données de mécanisme d'action officielles de DrugBank pour compléter l'analyse (DG002)
- Plan de test compagnon BRCA1/2 / HRD pour la sélection des patientes candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

