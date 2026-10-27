---
layout: default
title: Conestat Alfa
parent: Preuves élevées (L1-L2)
nav_order: 197
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Conestat Alfa : nouvelle indication prédite, Déficit en inhibiteur de C1 (niveau de preuve L1). Indication d'origine : Angioedème héréditaire"
monitor_inn: "CONESTAT ALFA"
predicted_indications: ["C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization", "primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "fetal and neonatal alloimmune thrombocytopenia"]
---

# Conestat Alfa
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

## Conestat alfa : De l'angioedème héréditaire au déficit en inhibiteur de la C1 estérase
{: .text-alpha }

## Résumé en Une Phrase

Conestat alfa est un inhibiteur de la C1 estérase humain recombinant, initialement utilisé pour traiter l'angioedème héréditaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **déficit en inhibiteur de C1**, avec **4 essais cliniques** et **9 publications** soutenant cette direction.
Il faut toutefois noter que cette prédiction recoupe en pratique l'indication d'origine du médicament : il ne s'agit pas d'un repositionnement au sens strict.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Angioedème héréditaire (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Déficit en inhibiteur de C1 |
| Score de Prédiction TxGNN | 99,999 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, conestat alfa est une forme recombinante de l'inhibiteur de la C1 estérase (C1-INH), produite chez des lapins transgéniques. Son efficacité dans les crises d'angioedème héréditaire a été démontrée par des essais randomisés contrôlés par placebo.

Le déficit en C1-INH est la cause même de l'angioedème héréditaire de type I et II. Conestat alfa remplace la protéine fonctionnelle manquante ou dysfonctionnelle. Il rétablit ainsi le contrôle des voies du complément, de contact et de la kallikréine-kinine, ce qui réduit la production de bradykinine, médiateur principal de l'œdème.

La prédiction est donc cohérente sur le plan mécanistique, mais elle correspond à l'indication d'origine. Par ailleurs, le même modèle propose d'autres maladies (troubles plaquettaires, serpinopathies, etc.) pour lesquelles aucun lien mécanistique plausible ni aucune preuve clinique n'ont été identifiés ; elles relèvent très probablement d'artefacts du graphe et ne sont pas retenues ici.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00262301](https://clinicaltrials.gov/study/NCT00262301) | Phase 3 | Terminé | 75 | Essai randomisé, en double aveugle, contre placebo : efficacité et sécurité de C1-INH recombinant dans les crises aiguës d'angioedème héréditaire |
| [NCT00225147](https://clinicaltrials.gov/study/NCT00225147) | Phase 2/3 | Terminé | 77 | Étude randomisée, en double aveugle, contre placebo : sécurité, efficacité et pharmacocinétique/pharmacodynamie dans les crises aiguës |
| [NCT02247739](https://clinicaltrials.gov/study/NCT02247739) | Phase 2 | Terminé | 32 | Étude croisée à 3 périodes, contre placebo : prophylaxie des crises d'angioedème héréditaire |
| [NCT04414631](https://clinicaltrials.gov/study/NCT04414631) | Phase 2 | Arrêté | 80 | Prévention des formes sévères de COVID-19 hospitalisés ; indication différente, lien seulement indirect |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [30021471](https://pubmed.ncbi.nlm.nih.gov/30021471/) | 2018 | ECR (classification des données) | Expert Rev Clin Immunol | Conestat alfa en prophylaxie des crises chez l'adulte et l'adolescent ; enregistré en Europe pour les crises aiguës |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Revue systématique | Pneumonol Alergol Pol | Comparaison de l'efficacité de conestat alfa, du C1-INH humain et de l'icatibant dans les crises aiguës |
| [22946752](https://pubmed.ncbi.nlm.nih.gov/22946752/) | 2012 | Revue | BioDrugs | Efficacité démontrée dans deux essais randomisés similaires, en double aveugle, contre placebo |
| [24801469](https://pubmed.ncbi.nlm.nih.gov/24801469/) | 2014 | Cohorte | Allergy Asthma Proc | Traitement à domicile de 65 épisodes chez deux patientes : efficacité et sécurité en conditions réelles |
| [24556385](https://pubmed.ncbi.nlm.nih.gov/24556385/) | 2014 | Cohorte | Eur J Dermatol | Utilisation chez des patients avec crises résistantes ou fréquentes d'angioedème héréditaire ou acquis |
| [39675680](https://pubmed.ncbi.nlm.nih.gov/39675680/) | 2025 | Cohorte | J Allergy Clin Immunol | Réponse clinique et voies transcriptomiques sanguines avant/après traitement des prodromes |
| [29357215](https://pubmed.ncbi.nlm.nih.gov/29357215/) | 2018 | Revue | Skin Therapy Lett | Nouveaux traitements de l'angioedème héréditaire, dont le C1-INH recombinant |
| [23776358](https://pubmed.ncbi.nlm.nih.gov/23776358/) | 2010 | Revue | Appl Clin Genet | Traitement des crises abdominales et faciales, focus sur le C1-INH |
| [19093699](https://pubmed.ncbi.nlm.nih.gov/19093699/) | 2008 | Revue | Drugs | Prise en charge actuelle et émergente de l'angioedème héréditaire aux États-Unis |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61253153 | RUCONEST 2100 U, poudre et solvant pour solution injectable (annulée) | Poudre et solvant pour solution injectable | Non renseignée |
| 60634703 | RUCONEST 2100 U, poudre pour solution injectable (annulée) | Poudre pour solution injectable | Non renseignée |

---

## Considérations de Sécurité

- **Interactions médicamenteuses** : 41 interactions sont recensées. Une est de niveau **majeur** (carfilzomib). Les autres listées sont de niveau modéré, notamment :
  - androgènes et apparentés : oxandrolone, oxymétholone, stanozolol, testostérone, danazol, énanthate de prastérone ;
  - œstrogènes et apparentés : éthinylestradiol, estradiol, œstrogènes conjugués, œstrogènes estérifiés, diéthylstilbestrol, drospirénone ;
  - thrombolytiques : altéplase, anistreplase ;
  - agents stimulant l'érythropoïèse : darbépoétine alfa, érythropoïétine.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais randomisés contrôlés par placebo (dont un essai de phase 3 terminé) soutiennent l'efficacité dans l'angioedème héréditaire par déficit en C1-INH. Il s'agit toutefois de l'indication d'origine, non d'un véritable repositionnement, et toutes les AMM françaises sont annulées, ce qui limite la disponibilité pratique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications issues de la notice de l'ANSM (donnée bloquante pour le criblage de sécurité)
- Données détaillées sur le mécanisme d'action
- Clarification du statut réglementaire actuel et de la disponibilité du produit en France
- Texte des indications approuvées pour les AMM concernées
- Examen des interactions de niveau majeur et modéré avant toute utilisation
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

