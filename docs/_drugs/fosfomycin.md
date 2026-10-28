---
layout: default
title: Fosfomycin
parent: Prédiction du modèle uniquement (L5)
nav_order: 348
evidence_level: L5
indication_count: 8
monitor_inn: "fosfomycin"
predicted_indications: ["uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "pyelitis"]
last_modified_at: 2026-10-28
description: "Fosfomycin : nouvelle indication prédite, Uterine inflammatory disease (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Fosfomycin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Fosfomycin: Uterine inflammatory disease
{: .text-alpha }

## Résumé en une phrase

La fosfomycine est un antibiotique dont l'usage d'origine est le traitement de l'infection urinaire, relation enregistrée dans le graphe de connaissances du modèle.
Le modèle TxGNN prédit qu'elle pourrait être utile dans la **maladie inflammatoire de l'utérus**.
Cette direction repose sur **2 essais cliniques** et **1 publication**, mais aucun de ces travaux n'étudie directement cette maladie : la prédiction reste donc essentiellement théorique.

---

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans les données locales |
| Nouvelle indication prédite | Uterine inflammatory disease |
| Score de prédiction TxGNN | 0.9998 |
| Niveau de preuve | L5 |
| Statut de marché en France | Commercialisé (autorisations valides : 19 sur 19) |
| Nombre d'AMM | 19 (valides : 19) |
| Décision recommandée | Hold |

---

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales sur cet antibiotique, la fosfomycine inhibe MurA, une enzyme impliquée dans la synthèse de la paroi bactérienne. Elle est active sur de nombreuses bactéries à Gram négatif et à Gram positif. Ce mécanisme explique qu'elle soit utilisée contre les bactéries responsables d'infections urinaires.

Une inflammation de l'utérus d'origine bactérienne (infection du tractus génital) pourrait théoriquement relever d'un antibiotique à large spectre. Le lien avec l'infection urinaire est donc plausible, car des germes communs peuvent être en cause. Il reste toutefois indirect.

Aucune des données disponibles ne montre que la fosfomycine a été évaluée dans l'inflammation utérine.

---

## Preuves d'essais cliniques

| Numéro d'essai | Phase | Statut | Inscription | Résultats principaux |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Terminé | 3520 | Étude pharmacocinétique pédiatrique de médicaments peu étudiés, administrés selon les soins courants. Non spécifique à la fosfomycine ni à la maladie prédite ; aucun signal d'efficacité. |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | En recrutement | 5000 | Plateforme pharmacocinétique, pharmacodynamique et de sécurité chez l'enfant et le jeune adulte. Non spécifique à une indication ; aucun signal d'efficacité. |

---

## Preuves de la littérature

| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [35653789](https://pubmed.ncbi.nlm.nih.gov/35653789/) | 2022 | Cohorte | J Obstet Gynaecol | Étude de la cystite liée au dienogest chez des femmes atteintes d'endométriose après chirurgie par laparoscopie. Elle ne porte pas sur l'inflammation utérine ni sur un traitement par fosfomycine. |

---

## Informations de marché en France

La fosfomycine est commercialisée en France sous 19 AMM valides, toutes pour des produits mono-substance. Il s'agit surtout de granulés pour solution buvable en sachet (3 g), ainsi que de poudres pour perfusion ou injection. Le texte des indications approuvées n'est pas renseigné dans les données compilées. Les cinq AMM ci-dessous sont des exemples.

| Numéro d'AMM | Nom du produit | Forme pharmaceutique |
|---------|------|------|
| 61935264 | Fosfomycine Viatris Adultes 3 g | Granulés pour solution buvable en sachet |
| 66430643 | Fosfomycine Arrow 3 g | Granulés pour solution buvable en sachet |
| 67951706 | Monuril 3 g (Zambon France) | Granulés pour solution buvable en sachet |
| 65164104 | Fomicyt 4 g I.V. | Poudre pour solution à diluer pour perfusion |
| 63322018 | Fosfomycine Panpharma 4 g | Poudre pour solution injectable |

---

## Considérations de sécurité

- **Contre-indications issues du graphe de connaissances** (relations du graphe, pas le texte de la notice) : maladie rénale, pyo-uretère, colite à *Clostridium difficile*, entérocolite nécrosante périnatale.
- **Interactions médicamenteuses** (3 identifiées) :
  - balsalazide : modérée ;
  - acide picosulfurique : modérée ;
  - métoclopramide : mineure.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- Aucun essai ni aucune publication ne porte directement sur la maladie inflammatoire de l'utérus. Les deux essais sont des études pharmacocinétiques pédiatriques générales, et l'article concerne la cystite chez des femmes atteintes d'endométriose. Le niveau de preuve est donc L5, c'est-à-dire une prédiction du modèle seule.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des études cliniques ou microbiologiques évaluant la fosfomycine dans les infections utérines ou génitales hautes (germes en cause, sensibilité, pénétration tissulaire).
- Des données détaillées sur le mécanisme d'action et sur les mises en garde et contre-indications de la notice.
- Une évaluation de la voie d'administration adaptée (orale ou intraveineuse).
- Une priorité à donner à des candidates mieux étayées pour ce médicament, comme la pyélite, plus proche de l'usage connu en infection urinaire et appuyée par des essais sur la fosfomycine injectable dans les infections urinaires compliquées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

