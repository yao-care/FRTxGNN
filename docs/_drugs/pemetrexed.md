---
layout: default
title: Pemetrexed
parent: Preuves élevées (L1-L2)
nav_order: 585
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Pemetrexed : nouvelle indication prédite, Mésothéliome péritonéal malin (niveau de preuve L2). Indication d'origine : Cancer bronchique non à petites cellules, cancer du poumon…"
monitor_inn: "pemetrexed"
predicted_indications: ["pleural adenomatoid tumor", "pleural biphasic mesothelioma", "pericardium cancer", "well differentiated papillary mesothelioma", "lymphohistiocytoid mesothelioma", "iminoglycinuria"]
---

# Pemetrexed
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **10** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

# Pémétrexed : Du Cancer Bronchique Non à Petites Cellules et du Mésothéliome Pleural au Mésothéliome Péritonéal Malin

## Résumé en Une Phrase

Le pémétrexed est un antifolate cytotoxique, initialement utilisé pour le traitement du cancer bronchique non à petites cellules et du mésothéliome pleural malin.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **mésothéliome péritonéal malin**,
avec **7 essais cliniques** et **20 publications** compilés dans les données de ce rapport, dont plusieurs séries de cas traités par pémétrexed-cisplatine.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer bronchique non à petites cellules, cancer du poumon, mésothéliome pleural malin (le texte d'indication des AMM n'est pas renseigné ; indications issues du graphe de connaissances TxGNN) |
| Nouvelle Indication Prédite | Mésothéliome péritonéal malin |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 10 (dont 10 annulées) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action issues de la base de médicaments ne sont pas disponibles. D'après les connaissances pharmacologiques établies, le pémétrexed est un antifolate à cibles multiples : il inhibe la thymidylate synthase (TS), la dihydrofolate réductase (DHFR) et la GARFT (glycinamide ribonucléotide formyltransférase). Il perturbe ainsi la synthèse des purines et des pyrimidines dans les cellules tumorales à division rapide.

Le mésothéliome péritonéal partage l'histologie et la biologie du mésothéliome pleural, pour lequel l'association pémétrexed-cisplatine est le traitement de référence depuis l'essai de phase 3 de Vogelzang et al. (2003). Le mécanisme est donc attendu comme transposable. Les essais de phase 2 incluent à la fois la maladie pleurale et péritonéale, et les recommandations actuelles utilisent l'association pémétrexed-platine pour la maladie péritonéale non résécable.

Il convient de noter que, pour les formes péritonéales, la chirurgie de cytoréduction associée à la chimiothérapie hyperthermique intrapéritonéale (CHIP) reste le traitement privilégié chez les patients éligibles ; la chimiothérapie systémique concerne surtout les formes avancées ou non résécables.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Terminé | 48 | Pémétrexed + gemcitabine en première ligne dans le mésothéliome pleural ou péritonéal ; étude à bras unique, sites mixtes |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | En recrutement | 66 | Étude randomisée : carboplatine-pémétrexed-bévacizumab avec ou sans atézolizumab dans le mésothéliome péritonéal ; résultats non disponibles |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspendu | 66 | MESOTIP : PIPAC + chimiothérapie systémique (cisplatine-pémétrexed) vs chimiothérapie seule en première ligne |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | En recrutement | 28 | Sintilimab + bévacizumab + pémétrexed-cisplatine, bras unique, mésothéliome péritonéal non résécable |
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | En recrutement | 64 | ICARuS II : chimiothérapie intrapéritonéale vs intraveineuse après chirurgie de cytoréduction et CHIP ; le pémétrexed n'est probablement pas l'agent principal testé |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Actif, hors recrutement | 30 | TRC102 avec cisplatine-pémétrexed dans les tumeurs solides avancées ; le mésothéliome n'en est qu'un sous-groupe |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Terminé | 19 | Cisplatine, pémétrexed et imatinib dans le mésothéliome malin ; détermination de la dose maximale tolérée et tolérance uniquement |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Étude rétrospective | Jpn J Clin Oncol | Efficacité et tolérance de pémétrexed-cisplatine en première ligne dans le mésothéliome péritonéal avancé |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Étude rétrospective | Expert Rev Anticancer Ther | Évaluation de pémétrexed-cisplatine en première ligne dans le mésothéliome péritonéal |
| [21528659](https://pubmed.ncbi.nlm.nih.gov/21528659/) | 2011 | Série monocentrique | Tumori | Pémétrexed-cisplatine chez des patients naïfs de chimiothérapie : efficacité et tolérance |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Étude comparative | Clin Med Insights Oncol | Comparaison pémétrexed-platine vs gemcitabine-platine en première ligne |
| [39413826](https://pubmed.ncbi.nlm.nih.gov/39413826/) | 2024 | Revue | J Natl Compr Canc Netw | Options systémiques : essais spécifiques rares, recommandations extrapolées du mésothéliome pleural ; immunothérapie ou chimiothérapie à base de pémétrexed |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Étude multicentrique | Ann Surg Oncol | Stratégies thérapeutiques et résultats dans le mésothéliome péritonéal |
| [36765620](https://pubmed.ncbi.nlm.nih.gov/36765620/) | 2023 | Revue | Cancers | Parcours diagnostique et thérapeutique ; survie médiane de 34 à 92 mois après chirurgie de cytoréduction et CHIP |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Revue | J Clin Med | Traitement du mésothéliome péritonéal malin |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Revue | Transl Lung Cancer Res | Revue du mésothéliome péritonéal malin |
| [33257382](https://pubmed.ncbi.nlm.nih.gov/33257382/) | 2020 | Cas clinique | BMJ Case Rep | Nivolumab dans le mésothéliome péritonéal après chimiothérapie systémique initiale |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67323808 | ALIMTA 500 mg | Poudre pour solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 67713231 | ALIMTA 100 mg | Poudre pour solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 66335088 | PEMETREXED FRESENIUS KABI 500 mg | Poudre pour solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 62103459 | PEMETREXED FRESENIUS KABI 25 mg/ml | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 61543078 | PEMETREXED VIATRIS 25 mg/ml | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |

Au total, 10 AMM sont recensées, toutes annulées ; aucune n'est actuellement valide.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (antimétabolite, classe des antifolates) |
| Risque de Myélosuppression | Élevé : le graphe de connaissances signale des contre-indications liées à la neutropénie, la thrombocytopénie, l'agranulocytose et l'anémie |
| Classification d'Émétogénicité | Faible à moyenne (selon la catégorie du médicament) |
| Éléments de Surveillance | Numération formule sanguine, fonction rénale (insuffisance rénale signalée), fonction hépatique |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

- **Contre-indications signalées dans le graphe de connaissances** (et non issues de la notice) : maladie rénale, insuffisance de la fonction rénale, pyo-uretère, thrombocytopénie, neutropénie, agranulocytose, anémie, anémie macrocytaire.
- **Interactions médicamenteuses** : 367 interactions recensées. Les interactions de niveau modéré les plus notables concernent : famotidine, ranitidine, cimétidine, metformine, amoxicilline, acide acétylsalicylique, mésalazine, balsalazide, olsalazine, vancomycine, kanamycine, néomycine, lévofloxacine, polymyxine B, saproptérine et plusieurs formes d'amphotéricine B. Beaucoup concernent des médicaments néphrotoxiques ou à élimination rénale.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le pémétrexed-platine est déjà la référence du mésothéliome pleural (essai de phase 3), et plusieurs séries et essais de phase 2 incluent la forme péritonéale. Toutefois, aucun essai de phase 3 spécifique au péritoine n'existe, et l'évidence repose sur des études de phase 2, rétrospectives et sur une extrapolation.
- Toutes les AMM françaises du pémétrexed sont annulées, et les données de sécurité issues de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice (mises en garde et contre-indications) sur le site de l'ANSM
- Obtenir les données détaillées sur le mécanisme d'action auprès de DrugBank
- Clarifier le statut réglementaire actuel en France (AMM annulées) et la disponibilité réelle du produit
- Suivre les résultats des essais randomisés de phase 2 en cours (NCT05001880, NCT03875144) ainsi que ceux d'ICARuS II
- Définir un plan de surveillance hématologique et rénale, avec supplémentation en acide folique et vitamine B12 selon la pratique habituelle
- Réserver la chimiothérapie systémique aux formes non résécables ou avancées, la chirurgie de cytoréduction avec CHIP restant privilégiée chez les patients éligibles
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

