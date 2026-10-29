---
layout: default
title: Fluvastatin
parent: Prédiction du modèle uniquement (L5)
nav_order: 343
evidence_level: L5
indication_count: 6
monitor_inn: "fluvastatin"
predicted_indications: ["HIV infectious disease", "cholesterol-ester transfer protein deficiency", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "fibroma of prostate"]
last_modified_at: 2026-10-29
description: "Fluvastatin : nouvelle indication prédite, Infection par le VIH (niveau de preuve L5). Indication d'origine : Non précisée dans les textes d'AMM disponibles"
---

# Fluvastatin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Fluvastatine : De l'athérosclérose à l'infection par le VIH
{: .text-alpha }

## Résumé en Une Phrase

La fluvastatine est une statine, initialement utilisée contre les dyslipidémies et l'athérosclérose (relations enregistrées dans le graphe de connaissances).
Le modèle TxGNN prédit qu'elle pourrait être utile pour l'**infection par le VIH**, mais aucun essai clinique n'est enregistré et les **13 publications** retrouvées portent surtout sur la gestion des dyslipidémies et des interactions médicamenteuses chez les patients infectés par le VIH, et non sur un effet antiviral.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les textes d'AMM disponibles ; le graphe de connaissances enregistre l'athérosclérose, les troubles artériosclérotiques et l'hyperlipidémie familiale combinée |
| Nouvelle Indication Prédite | Infection par le VIH |
| Score de Prédiction TxGNN | 0,9988 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 13 sur 15) |
| Nombre d'AMM | 15 (valides : 13) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. La fluvastatine fait partie de la classe des statines (inhibiteurs de l'HMG-CoA réductase), utilisées pour abaisser le cholestérol et prévenir les complications cardiovasculaires. Les scores de prédiction proviennent du modèle TxGNN (deep learning) et peuvent refléter des similarités apprises par le modèle entre maladies apparentées, et non des preuves biologiques.

Les liens plausibles avec le VIH restent indirects : les statines ont des propriétés anti-inflammatoires et immunomodulatrices pouvant réduire des marqueurs d'activation immunitaire chez les patients traités, et un effet protecteur des podocytes a été observé dans un modèle murin de néphropathie associée au VIH. La fluvastatine est métabolisée par le CYP2C9 plutôt que le CYP3A4, d'où un risque d'interaction relativement faible avec les inhibiteurs de protéase.

Aucune donnée ne montre que la fluvastatine traite l'infection par le VIH elle-même. Les études concernent l'usage lipidique de la molécule chez des patients infectés. Le niveau de preuve est donc plafonné à L5 : aucune étude citée n'évalue la fluvastatine comme traitement de l'infection par le VIH.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [20118492](https://pubmed.ncbi.nlm.nih.gov/20118492/) | 2010 | ECR ouvert | J Antimicrob Chemother | Fluvastatine en adjuvant de l'interféron pégylé et de la ribavirine chez des patients co-infectés VIH/VHC (objectif : réplication du VHC) |
| [15293079](https://pubmed.ncbi.nlm.nih.gov/15293079/) | 2004 | Étude clinique | Infection | Comparaison fluvastatine/pravastatine pour les lipides chez des patients VIH sous traitement antirétroviral, interaction avec l'indinavir |
| [12351967](https://pubmed.ncbi.nlm.nih.gov/12351967/) | 2002 | Étude clinique | AIDS | Efficacité et tolérance de la fluvastatine chez des patients VIH hyperlipidémiques sous inhibiteurs de protéase |
| [33238713](https://pubmed.ncbi.nlm.nih.gov/33238713/) | 2021 | Cohorte | AIDS Res Hum Retroviruses | Effet des statines sur l'inflammation et l'activation immunitaire chez des personnes VIH sous traitement efficace |
| [23703578](https://pubmed.ncbi.nlm.nih.gov/23703578/) | 2013 | Revue | Clin Pharmacokinet | Interactions entre statines et inhibiteurs de protéase antiviraux |
| [12660532](https://pubmed.ncbi.nlm.nih.gov/12660532/) | 2003 | Revue | AIDS | Statines et fibrates dans l'hyperlipidémie des patients VIH sous traitement antirétroviral |
| [19215577](https://pubmed.ncbi.nlm.nih.gov/19215577/) | 2009 | Étude pilote | J Viral Hepat | Effet de la fluvastatine sur la réplication du VHC chez des patients co-infectés VIH-VHC |
| [19188342](https://pubmed.ncbi.nlm.nih.gov/19188342/) | 2009 | Étude préclinique (souris) | Nephrol Dial Transplant | Protection des podocytes dans un modèle murin de néphropathie associée au VIH |
| [16868453](https://pubmed.ncbi.nlm.nih.gov/16868453/) | 2006 | Étude clinique (médicament différent) | AIDS | Ézétimibe vs fluvastatine 80 mg : baisse du LDL-cholestérol similaire (20 % vs 24 %) chez des patients VIH |
| [19838098](https://pubmed.ncbi.nlm.nih.gov/19838098/) | 2010 | ECR (autre statine) | AIDS | Rosuvastatine vs pravastatine chez des patients VIH dyslipidémiques sous inhibiteurs de protéase |

## Informations de Marché en France

La fluvastatine est commercialisée en France. Les textes d'indication ne sont pas renseignés dans les données compilées pour ces AMM. Sur les 15 AMM, 14 sont valides et 1 est annulée.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60852004 | LESCOL L.P. 80 mg | Comprimé pelliculé à libération prolongée | Non renseignée |
| 66946962 | FLUVASTATINE BIOGARAN 40 mg | Gélule | Non renseignée |
| 66605982 | FLUVASTATINE CEVIDRA 20 mg | Gélule | Non renseignée |
| 68067589 | FLUVASTATINE SANDOZ LP 80 mg | Comprimé pelliculé à libération prolongée | Non renseignée |
| 62756595 | FLUVASTATINE SANDOZ 20 mg | Gélule | Non renseignée |

## Considérations de Sécurité

- **Contre-indications enregistrées dans le graphe de connaissances** (et non issues d'un texte de notice) : maladie du foie, maladie de la vésicule biliaire, myopathie, maladies musculaires, maladie du muscle squelettique, paralysie périodique familiale, troubles hypotensifs, abus/dépendance de substances, rhabdomyolyse, fasciite nodulaire, traumatisme.
- **Interactions médicamenteuses** : 159 interactions recensées. Parmi les interactions de niveau modéré : aprépitant, métronidazole, oxandrolone, naltrexone, natéglinide, nitisinone, rosuvastatine, simvastatine, tinidazole, glibenclamide, pectine. Plusieurs autres (calcitriol, doxycycline, cimétidine, acide acétylsalicylique, pantoprazole, etc.) sont de niveau non déterminé.
- Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un score de modèle élevé, sans essai clinique ni étude évaluant la fluvastatine comme traitement de l'infection par le VIH. Les publications concernent la prise en charge des lipides, des interactions et des marqueurs inflammatoires. Les autres indications prédites (déficit en CETP, simien, félin, fibrome de la prostate, trouble neurodéveloppemental rare) n'ont aucune preuve et ne justifient pas d'avancer.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action et sur les mises en garde et contre-indications de la notice
- Études précliniques démontrant une activité antivirale ou immunomodulatrice pertinente dans le VIH
- Essais cliniques dont le critère principal porte sur la maladie VIH (réservoir viral, activation immunitaire, événements cliniques)
- Évaluation des interactions avec les antirétroviraux
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

