---
layout: default
title: Canakinumab
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
---

# Canakinumab
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

# Canakinumab : Des Syndromes Auto-inflammatoires à la Fièvre Méditerranéenne Familiale

## Résumé en Une Phrase

Canakinumab (Ilaris®) est un anticorps monoclonal humain anti-IL-1β approuvé dans de nombreux pays pour les maladies auto-inflammatoires rares, mais actuellement **non commercialisé en France**. Le modèle TxGNN prédit son efficacité pour la **Fièvre Méditerranéenne Familiale (FMF) de forme autosomique dominante** — l'indication la mieux étayée parmi les 10 candidats prédits, avec **7 essais cliniques** et **20 publications** soutenant cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non commercialisé en France (approuvé globalement pour CAPS, FMF résistante à la colchicine, TRAPS, sJIA) |
| Nouvelle Indication Prédite | Fièvre Méditerranéenne Familiale — forme autosomique dominante |
| Score de Prédiction TxGNN | 99.41% |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de données réglementaire française. Sur la base des informations connues, canakinumab est un anticorps monoclonal entièrement humain qui neutralise sélectivement l'interleukine-1β (IL-1β) libre, bloquant son interaction avec les récepteurs IL-1RI et IL-1RAcP. Cette inhibition ciblée supprime la cascade inflammatoire médiée par NF-κB et interrompt la production de médiateurs pro-inflammatoires secondaires (IL-6, CRP, SAA).

La Fièvre Méditerranéenne Familiale est causée par des mutations gain-de-fonction du gène MEFV, qui encode la protéine pyrin — un régulateur négatif de l'inflammasome. Ces mutations entraînent une suractivation de l'inflammasome pyrin avec libération excessive d'IL-1β active, provoquant des crises récurrentes de fièvre, péritonite, pleurite et arthrite, avec risque d'amylose AA à long terme si non traitée. Canakinumab cible directement le médiateur causal de la FMF, établissant un lien mécanistique parmi les plus directs de la médecine auto-inflammatoire.

Cette connexion n'est pas uniquement théorique : canakinumab est déjà approuvé par l'EMA et la FDA pour la FMF résistante à la colchicine, avec une efficacité démontrée dans plusieurs essais de Phase 3 et études en vie réelle. L'absence d'AMM en France représente une opportunité réglementaire d'expansion — environ 5 à 10 % des patients FMF sont non-répondeurs ou intolérants à la colchicine, définissant une population cible médicalement non satisfaite et bien délimitée.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00465985](https://clinicaltrials.gov/study/NCT00465985) | Phase 3 | Terminé | 35 | Étude randomisée double-aveugle contrôlée par placebo en conception de retrait dans le syndrome de Muckle-Wells — évaluation directe du maintien de l'efficacité anti-IL-1β vs placebo |
| [NCT00685373](https://clinicaltrials.gov/study/NCT00685373) | Phase 3 | Terminé | 166 | Plus grande cohorte de l'programme clinique (n=166) ; sécurité et efficacité à long terme (≥6 mois) dans les CAPS — base de la demande d'AMM internationale |
| [NCT01302860](https://clinicaltrials.gov/study/NCT01302860) | Phase 3 | Terminé | 17 | Étude ouverte multicentrique chez les enfants ≤4 ans avec CAPS ; évaluation de l'innocuité, de l'efficacité et de la compatibilité avec les vaccinations pédiatriques |
| [NCT00991146](https://clinicaltrials.gov/study/NCT00991146) | Phase 3 | Terminé | 19 | Étude ouverte japonaise dans CAPS (FCAS, MWS, NOMID) avec phase d'extension jusqu'à l'approbation nationale — données de réplication en population asiatique |
| [NCT01576367](https://clinicaltrials.gov/study/NCT01576367) | Phase 3 | Terminé | 17 | Étude d'extension ouverte à long terme pour les patients ayant complété CACZ885D2307 — données de durabilité thérapeutique et tolérance prolongée |
| [NCT01242813](https://clinicaltrials.gov/study/NCT01242813) | Phase 2 | Terminé | 20 | Traitement 4 mois + suivi 6 mois dans le TRAPS actif récurrent ou chronique — données posologiques et taux de rechute après arrêt du traitement |
| [NCT06838143](https://clinicaltrials.gov/study/NCT06838143) | N/A | En recrutement | 25 | Étude observationnelle vie réelle (REASSURE) dans CAPS, crFMF, TRAPS et HIDS/MKD chez adultes et enfants — données de pharmacovigilance post-commercialisation en cours de collecte |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37769252](https://pubmed.ncbi.nlm.nih.gov/37769252/) | 2024 | Méta-analyse | Rheumatology (Oxford) | Méta-analyse dédiée à l'efficacité et la sécurité des anti-IL-1 spécifiquement dans la FMF — niveau de preuve le plus élevé disponible |
| [35874710](https://pubmed.ncbi.nlm.nih.gov/35874710/) | 2022 | Revue Systématique | Frontiers in Immunology | Synthèse systématique de l'efficacité et la sécurité des trois anti-IL-1 approuvés (anakinra, canakinumab, rilonacept) dans l'ensemble des maladies immuno-médiées |
| [32806879](https://pubmed.ncbi.nlm.nih.gov/32806879/) | 2020 | Revue Systématique | Turkish J Medical Sciences | Revue de la pathogenèse de la FMF et des développements thérapeutiques récents, dont le rôle des anti-IL-1 pour les patients résistants à la colchicine |
| [36062765](https://pubmed.ncbi.nlm.nih.gov/36062765/) | 2022 | Revue | Clinical and Experimental Rheumatology | Inhibition IL-1 dans la FMF : résultats cliniques, stratégies de gestion pour les patients résistants ou intolérants à la colchicine |
| [29768139](https://pubmed.ncbi.nlm.nih.gov/29768139/) | 2018 | Revue | New England Journal of Medicine | Canakinumab dans les syndromes de fièvres périodiques auto-inflammatoires récurrentes (FMF, MKD, TRAPS) — publication dans le NEJM soulignant l'importance clinique |
| [40040547](https://pubmed.ncbi.nlm.nih.gov/40040547/) | 2025 | Cohorte | Int J Rheumatic Diseases | Comparaison canakinumab avec vs sans colchicine dans la FMF : caractéristiques des crises, réactants de phase aiguë et résultats rénaux à long terme |
| [34568239](https://pubmed.ncbi.nlm.nih.gov/34568239/) | 2021 | Cohorte | Frontiers in Pediatrics | Efficacité du canakinumab dans la FMF pédiatrique résistante à la colchicine (n=65, suivi ≥6 mois) — données pédiatriques en situation réelle |
| [28362189](https://pubmed.ncbi.nlm.nih.gov/28362189/) | 2017 | Revue | Expert Review of Clinical Immunology | Rôle de canakinumab dans la FMF ; revue ciblée sur le positionnement comme alternative à la colchicine et profil de sécurité |
| [36961326](https://pubmed.ncbi.nlm.nih.gov/36961326/) | 2023 | Cohorte | Rheumatology (Oxford) | Faisabilité du sevrage du canakinumab chez des enfants FMF résistants à la colchicine — protocole d'arrêt progressif et résultats cliniques |
| [31463794](https://pubmed.ncbi.nlm.nih.gov/31463794/) | 2019 | Cohorte | Paediatric Drugs | Analyse rétrospective monocentrique du canakinumab chez l'enfant atteint de FMF — données de pratique clinique pédiatrique réelle |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Canakinumab dispose d'un niveau de preuve L1 pour la FMF, incluant des essais de Phase 3 randomisés double-aveugle contrôlés par placebo, avec une approbation réglementaire déjà accordée par l'EMA et la FDA pour la FMF résistante à la colchicine — le principal obstacle en France est l'absence d'AMM nationale et non un déficit de preuves cliniques ou mécanistiques.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération des données complètes sur le mécanisme d'action (MOA) via DrugBank API
- Obtention de la notice EMA/ANSM pour les mises en garde, contre-indications et interactions médicamenteuses détaillées
- Évaluation de la taille de la population cible en France (patients FMF résistants ou intolérants à la colchicine)
- Analyse de faisabilité réglementaire pour une demande d'AMM nationale ou recours à une autorisation d'accès précoce (AAP)
- Plan de surveillance de sécurité adapté : suivi des infections opportunistes, neutropénie, réactions injection-site et réactivation tuberculose
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

