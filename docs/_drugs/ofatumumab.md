---
layout: default
title: Ofatumumab
parent: Preuves élevées (L1-L2)
nav_order: 553
evidence_level: L2
indication_count: 4
monitor_inn: "OFATUMUMAB"
predicted_indications: ["follicular lymphoma", "metastatic neoplasm", "malignant spiradenoma", "Langerhans cell histiocytosis"]
last_modified_at: 2026-10-23
description: "Ofatumumab : nouvelle indication prédite, Lymphome folliculaire (niveau de preuve L2). Indication d'origine : Leucémie lymphoblastique aiguë et syndrome de Richter"
---

# Ofatumumab
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **4** 
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

## Ofatumumab : De la leucémie lymphoblastique aiguë au lymphome folliculaire
{: .text-alpha }

## Résumé en Une Phrase

L'ofatumumab est un anticorps monoclonal humain anti-CD20. La base de connaissances utilisée par le modèle y associe la **leucémie lymphoblastique aiguë** et le **syndrome de Richter**, qui sont des relations enregistrées dans cette base et non des indications approuvées.
Le modèle TxGNN prédit qu'il pourrait être efficace dans le **lymphome folliculaire**, avec **11 essais cliniques** et **20 publications** compilés pour cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie lymphoblastique aiguë et syndrome de Richter (relations enregistrées dans la base de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Lymphome folliculaire |
| Score de Prédiction TxGNN | 0,9970 |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'ofatumumab est un anticorps monoclonal entièrement humain dirigé contre CD20. Il se fixe sur un épitope distinct, proche de la membrane cellulaire. Cette fixation favorise une forte cytotoxicité dépendante du complément et une cytotoxicité cellulaire dépendante des anticorps.

Le lymphome folliculaire est une hémopathie maligne à cellules B exprimant CD20. La cible est donc présente directement sur les cellules tumorales. Cette biologie est proche de celle des hémopathies B associées à l'ofatumumab dans la base de connaissances (leucémie lymphoblastique aiguë, syndrome de Richter). Elle soutient la plausibilité de la prédiction, y compris dans les maladies réfractaires au rituximab.

Les données compilées ne contiennent pas d'essai randomisé de phase 3 achevé dans cette indication. La plausibilité mécanistique repose donc surtout sur des essais de phase 2.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01077518](https://clinicaltrials.gov/study/NCT01077518) | Phase 3 | Terminé prématurément | 346 | Ofatumumab + bendamustine vs bendamustine seule dans les lymphomes B indolents non répondeurs au rituximab ; résultats non fournis dans les données |
| [NCT01286272](https://clinicaltrials.gov/study/NCT01286272) | Phase 2 | Complété | 135 | Essai randomisé : ofatumumab + bendamustine avec ou sans bortézomib dans le lymphome folliculaire non traité |
| [NCT00494780](https://clinicaltrials.gov/study/NCT00494780) | Phase 2 | Complété | 59 | Essai randomisé à deux doses d'ofatumumab + CHOP dans le lymphome folliculaire non traité |
| [NCT01190449](https://clinicaltrials.gov/study/NCT01190449) | Phase 2 | Complété | 51 | Ofatumumab en monothérapie dans le lymphome folliculaire non traité |
| [NCT00394836](https://clinicaltrials.gov/study/NCT00394836) | Phase 2 | Complété | 116 | Bras unique : ofatumumab dans le lymphome folliculaire réfractaire au rituximab |
| [NCT02710643](https://clinicaltrials.gov/study/NCT02710643) | Phase 2 | Complété | 110 | Étude MIRO : radiothérapie locale avec ou sans ofatumumab dans le lymphome folliculaire de stade I/II |
| [NCT01239394](https://clinicaltrials.gov/study/NCT01239394) | Phase 2 | Complété | 43 | Ofatumumab en traitement systémique initial des lymphomes B indolents |
| [NCT00823719](https://clinicaltrials.gov/study/NCT00823719) | Phase 2 | Complété | 61 | Ofatumumab + ICE ou DHAP avant autogreffe dans les lymphomes agressifs en rechute ou réfractaires |
| [NCT00742144](https://clinicaltrials.gov/study/NCT00742144) | Phase 1 | Complété | 6 | Sécurité et pharmacocinétique chez des patients japonais atteints de lymphome folliculaire CD20+ ou de LLC |
| [NCT01119794](https://clinicaltrials.gov/study/NCT01119794) | Phase 2 | Terminé prématurément | 10 | Ofatumumab + bortézomib dans les lymphomes non hodgkiniens de bas grade ; effectif trop faible pour conclure |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31174236](https://pubmed.ncbi.nlm.nih.gov/31174236/) | 2019 | ECR (phase 2) | Cancer | CALGB 50904 : ofatumumab + bendamustine avec ou sans bortézomib dans le lymphome folliculaire à haut risque non traité ; évaluation des réponses complètes, de l'efficacité et de la tolérance |
| [22409295](https://pubmed.ncbi.nlm.nih.gov/22409295/) | 2012 | Essai de phase 2 | British Journal of Haematology | Ofatumumab (500 ou 1000 mg) + CHOP en première ligne chez 59 patients atteints de lymphome folliculaire |
| [22389254](https://pubmed.ncbi.nlm.nih.gov/22389254/) | 2012 | Essai de phase 2 multicentrique à bras unique | Blood | Ofatumumab en monothérapie chez 116 patients atteints de lymphome folliculaire réfractaire au rituximab ; taux de réponse global de 13 % et 10 % selon les groupes de dose |
| [30723894](https://pubmed.ncbi.nlm.nih.gov/30723894/) | 2019 | Essai de phase 2 | British Journal of Haematology | CALGB 50901 : ofatumumab seul dans le lymphome folliculaire non traité, de risque faible ou intermédiaire |
| [38937025](https://pubmed.ncbi.nlm.nih.gov/38937025/) | 2024 | Essai de phase 2 | The Lancet Haematology | FIL MIRO : radiothérapie locale et immunothérapie guidée par la maladie résiduelle mesurable dans le lymphome folliculaire de stade précoce |
| [18390837](https://pubmed.ncbi.nlm.nih.gov/18390837/) | 2008 | Essai de phase 1/2 | Blood | Première utilisation clinique de l'ofatumumab dans le lymphome folliculaire en rechute ou réfractaire |
| [24443277](https://pubmed.ncbi.nlm.nih.gov/24443277/) | 2014 | Analyse pharmacocinétique de population | Journal of Clinical Pharmacology | Pharmacocinétique chez 477 patients (LLC, lymphome folliculaire, polyarthrite rhumatoïde) |
| [26043777](https://pubmed.ncbi.nlm.nih.gov/26043777/) | 2015 | Revue | Expert Opinion on Biological Therapy | Activité de l'ofatumumab dans les lymphomes B CD20+ |
| [29934061](https://pubmed.ncbi.nlm.nih.gov/29934061/) | 2018 | Revue fondée sur les preuves | Clinical Lymphoma, Myeloma & Leukemia | Schémas associant un anti-CD20 dans la LLC, le lymphome B diffus à grandes cellules et le lymphome folliculaire en rechute ou réfractaires |
| [23610620](https://pubmed.ncbi.nlm.nih.gov/23610620/) | 2013 | Revue | Therapeutic Advances in Hematology | Nouveaux agents dans les lymphomes indolents |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60690011 | KESIMPTA 20 mg, solution injectable en stylo prérempli (NOVARTIS EUROPHARM) | Solution injectable | Texte d'indication non renseigné dans les données compilées |

L'ofatumumab est commercialisé en France sous la forme d'un stylo prérempli injectable. Les données compilées ne permettent pas de confirmer la disponibilité d'une présentation adaptée au traitement des lymphomes, alors que les essais cités reposent sur des perfusions.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Immunothérapie (anticorps monoclonal anti-CD20) |
| Risque de Myélosuppression | Non précisé dans les données compilées ; à évaluer surtout en association avec une chimiothérapie (CHOP, bendamustine, ICE/DHAP) |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | NFS avec formule, fonction hépatique et rénale ; surveillance renforcée en association avec une chimiothérapie |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 80 interactions ont été identifiées, dont 20 sont détaillées dans les données compilées.
  - Interactions de niveau **majeur** : déféripone, samarium (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribine, clozapine.
  - Interactions de niveau **modéré** : strontium-89, roflumilast, chloramphénicol, zidovudine, alemtuzumab, azathioprine, anakinra, canakinumab, alefacept, ainsi que plusieurs vaccins (anatoxine tétanique, charbon, choléra vivant).
  - L'association avec d'autres immunosuppresseurs ou myélosuppresseurs mérite une attention particulière.

Les mises en garde et contre-indications de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 2 achevés, dont des essais randomisés, étudient directement l'ofatumumab dans le lymphome folliculaire. Il n'existe pas de phase 3 achevée dans les données, d'où un niveau de preuve L2.
- Le mécanisme anti-CD20 est cohérent avec la maladie. Les données de sécurité de la notice et le mécanisme d'action détaillé manquent, et la présentation commercialisée en France n'est pas confirmée comme adaptée à cet usage.
- Les autres prédictions du modèle (néoplasme métastatique, spiradénome malin, histiocytose à cellules de Langerhans) reposent sur des preuves nettement plus faibles.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications) pour permettre le criblage de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action.
- Obtenir les résultats de l'essai de phase 3 NCT01077518 (terminé prématurément) et du CALGB 50904 pour évaluer l'efficacité comparative.
- Vérifier la disponibilité en France d'une présentation et d'une voie d'administration adaptées au traitement du lymphome folliculaire.
- Établir un plan de surveillance de l'hématotoxicité et du risque infectieux, en particulier en association avec une chimiothérapie ou d'autres immunosuppresseurs.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

