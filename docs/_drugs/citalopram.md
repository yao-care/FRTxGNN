---
layout: default
title: Citalopram
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 5
---

# Citalopram
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Citalopram : De la Dépression au Trouble Obsessionnel-Compulsif

## Résumé en Une Phrase

Citalopram est un inhibiteur sélectif de la recapture de la sérotonine (ISRS), principalement utilisé dans le traitement de la dépression majeure.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Trouble Obsessionnel-Compulsif (TOC)**,
avec **28 essais cliniques** et **16 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dépression (ISRS — aucune AMM enregistrée dans la base interrogée) |
| Nouvelle Indication Prédite | Trouble Obsessionnel-Compulsif (TOC) |
| Score de Prédiction TxGNN | 99,74 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Non commercialisé (selon données disponibles) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action (MOA) de citalopram ne sont pas disponibles dans ce dossier. Sur la base des informations connues, citalopram est un ISRS (inhibiteur sélectif de la recapture de la sérotonine) agissant sur le transporteur SERT pour augmenter la concentration synaptique de sérotonine. Son efficacité dans la dépression majeure est bien établie, et mécanistiquement, ce profil est directement applicable au TOC.

La physiopathologie du TOC repose sur une dysrégulation du circuit cortico-striato-thalamo-cortical (CSTC), avec une anomalie de la neurotransmission sérotoninergique. Les ISRS sont le traitement pharmacologique de première ligne du TOC : la FDA a approuvé la fluoxétine, la fluvoxamine, la sertraline et la paroxétine pour cette indication. Citalopram, en tant que membre de la même classe, partage ce mécanisme de classe. Deux publications directes (PMID 10471169 et 10572334) documentent explicitement l'efficacité de citalopram dans le TOC, y compris pour les cas résistants aux traitements.

L'énantiomère S du citalopram — l'escitalopram — a fait l'objet de plusieurs essais cliniques de Phase 3 et 4 complétés dans le TOC, renforçant considérablement la crédibilité de la prédiction. La transition de la dépression vers le TOC est donc mécanistiquement cohérente : les deux pathologies partagent une composante sérotoninergique commune, et la preuve de concept par classe existe déjà dans les lignes directrices internationales.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | Terminé | 100 | Escitalopram haute dose (jusqu'à 50 mg/j) pour le TOC en ambulatoire — évaluation tolérance et efficacité sur 18 semaines avec titration progressive |
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | Terminé | 176 | Comparaison escitalopram 20 mg vs 40 mg dans le TOC — étude randomisée double aveugle multicentrique, évaluée par Y-BOCS, HAM-D, CGI |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Terminé | 124 | TCC comme complément aux ISRS pour le TOC pédiatrique en réponse partielle — détermine l'apport additionnel de la thérapie comportementale |
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | Terminé | 30 | Escitalopram pour le TOC — efficacité et détermination de la dose optimale de traitement |
| [NCT00609531](https://clinicaltrials.gov/study/NCT00609531) | Phase 1 | Terminé | 12 | **Citalopram direct** — étude fMRI du mécanisme d'action sur les comportements répétitifs dans les troubles du spectre autistique ; seul essai avec le médicament cible |
| [NCT03993535](https://clinicaltrials.gov/study/NCT03993535) | Phase 4 | Terminé | 250 | Suivi naturaliste de 250 patients TOC — variables cliniques, neurocognitives et neuroimagerie associées à la réponse au traitement (étude NIH multicentrique internationale) |
| [NCT00456937](https://clinicaltrials.gov/study/NCT00456937) | Phase 4 | Terminé | 15 | Escitalopram jusqu'à 20 mg/j pour la schizophrénie avec comorbidité TOC — réduction de la symptomatologie obsessionnelle-compulsive |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Terminé | 78 | Efficacité comparée des ISRS, de l'ERP et de leur combinaison dans le TOC — population chinoise, avec identification des prédicteurs biologiques et psychologiques |
| [NCT03068429](https://clinicaltrials.gov/study/NCT03068429) | Phase 4 | Terminé | 69 | Conditionnement et extinction de la peur chez des patients TOC, avant et après traitement par sertraline — paradigme fMRI ; n=24 patients OCD vs n=24 contrôles |
| [NCT00708396](https://clinicaltrials.gov/study/NCT00708396) | Phase 4 | Inconnu | 20 | Escitalopram haute dose (20-40 mg/j) pour la schizophrénie/trouble schizoaffectif avec TOC non répondeurs aux doses standard |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | Essai ouvert | Int Clin Psychopharmacol | **Citalopram direct pour le TOC** — première documentation publiée de l'efficacité du citalopram dans le TOC, au-delà de son indication dépressive |
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | Essai ouvert | Eur Psychiatry | **Citalopram direct pour TOC résistant** — essai randomisé ouvert, citalopram seul vs citalopram + clomipramine, n=16 patients TOC réfractaires |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | Revue systématique | Compr Psychiatry | Sécurité et tolérance à long terme des ISRS hors-AMM à doses élevées dans le traitement du TOC |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Méta-analyse | J Affect Disord | Le TOC présente une réponse au placebo et aux antidépresseurs réduite par rapport aux autres troubles anxieux — méta-analyse comparative |
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | Méta-analyse | J Psychiatr Res | Comparaison de l'efficacité des traitements pharmacologiques et psychologiques, seuls ou combinés, chez les enfants et adolescents avec TOC — méta-analyse en réseau |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Méta-revue | Front Psychiatry | Efficacité, tolérance et risque suicidaire des antidépresseurs chez l'enfant et l'adolescent dans le traitement aigu du TOC et d'autres pathologies psychiatriques |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | Revue | BMJ Clin Evid | TOC : prévalence ~1 % chez les hommes, 1,5 % chez les femmes adultes ; revue de l'évolution naturelle, épidémiologie et options thérapeutiques |
| [35818708](https://pubmed.ncbi.nlm.nih.gov/35818708/) | 2022 | Revue systématique | Expert Opin Pharmacother | Efficacité et tolérance de la pharmacothérapie pour le trouble de la personnalité obsessionnelle-compulsive — revue systématique des ECR disponibles |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | Article | World J Biol Psychiatry | TOC et sérotonine — mécanismes neurobiologiques et neuroanatomiques du circuit CSTC ; bases des approches pharmacologiques sérotoninergiques |
| [19454066](https://pubmed.ncbi.nlm.nih.gov/19454066/) | 2007 | Revue | BMJ Clin Evid | TOC : revue clinique fondatrice sur l'évolution, les comorbidités et les stratégies de traitement pharmacologique et psychothérapeutique |

---

## Considérations de Sécurité

> Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Citalopram partage le mécanisme ISRS des molécules approuvées pour le TOC, deux publications directes documentent son efficacité dans cette indication, et les essais Phase 3 complétés sur l'escitalopram (énantiomère S du citalopram) constituent une preuve de classe solide. Toutefois, l'absence d'essai randomisé contrôlé de Phase 2/3 directement avec citalopram dans le TOC, combinée à l'indisponibilité des données de sécurité complètes, impose une progression encadrée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (MOA) issues de DrugBank (DG002)
- Informations de sécurité complètes : mises en garde, contre-indications et interactions médicamenteuses issues de la notice officielle ANSM (DG001)
- Vérification du statut d'AMM en France pour le citalopram (notamment Séropram® et génériques)
- Évaluation spécifique du risque d'allongement du QTc (effet de classe reconnu pour le citalopram à doses élevées — surveillance ECG recommandée)
- Plan de surveillance pour les populations à risque : patients âgés, insuffisants hépatiques, et utilisateurs de médicaments allongeant le QT
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

