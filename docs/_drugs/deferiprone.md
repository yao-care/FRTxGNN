---
layout: default
title: Deferiprone
parent: Preuves modérées (L3-L4)
nav_order: 220
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-14
description: "Deferiprone : nouvelle indication prédite, Porphyrie hépatique (niveau de preuve L4). Indication d'origine : Hémosidérose, bêta-thalassémie et hémoglobinopathies apparentées"
monitor_inn: "deferiprone"
predicted_indications: ["hepatic porphyria", "hepatopulmonary syndrome", "hepatoportal sclerosis", "primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "pyruvate kinase deficiency of red cells", "beta-thalassemia with other manifestations", "pyropoikilocytosis, hereditary"]
---

# Deferiprone
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **9** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Déferiprone : De l'hémosidérose et de la bêta-thalassémie à la porphyrie hépatique

## Résumé en Une Phrase

La déferiprone est un chélateur oral du fer, initialement utilisé dans la prise en charge de la surcharge en fer liée aux hémoglobinopathies, notamment la bêta-thalassémie.
Le modèle TxGNN prédit qu'elle pourrait être utile dans la **porphyrie hépatique**, mais les données compilées pour ce rapport ne comptent **aucun essai clinique** et seulement **2 publications précliniques** (modèles animaux).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémosidérose, bêta-thalassémie et hémoglobinopathies apparentées (d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Porphyrie hépatique |
| Score de Prédiction TxGNN | 99,20 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Toutes les AMM sont annulées |
| Nombre d'AMM | 6 (0 valide, 6 annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, la déferiprone est un chélateur oral du fer, dont l'efficacité a été établie dans la surcharge en fer liée à la bêta-thalassémie et pourrait, mécanistiquement, être applicable aux pathologies où le fer joue un rôle pathogène.

Dans la porphyrie cutanée tardive, la surcharge hépatique en fer et l'inhibition de l'uroporphyrinogène décarboxylase dépendante du fer sont des éléments centraux. Réduire le fer labile est donc plausible. Un modèle murin d'uroporphyrie a testé un chélateur oral du fer (la déferiprone), et une publication de 2020 a décrit une amélioration de l'anémie hémolytique et de la photosensibilité dans la porphyrie érythropoïétique congénitale grâce à la chélation du fer.

Ces éléments restent précliniques ou indirects. Aucune donnée humaine n'est disponible, et la similarité avec l'indication originale n'a pas été évaluée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [32678895](https://pubmed.ncbi.nlm.nih.gov/32678895/) | 2020 | Préclinique (modèle animal) | Blood | La chélation du fer corrige l'anémie hémolytique et la photosensibilité cutanée dans un modèle de porphyrie érythropoïétique congénitale |
| [17854053](https://pubmed.ncbi.nlm.nih.gov/17854053/) | 2007 | Préclinique (modèle murin) | Hepatology | Chez des souris Hfe-/-, la déferiprone est comparée à un régime pauvre en fer pour réduire l'accumulation hépatique d'uroporphyrine dans un modèle de porphyrie cutanée tardive |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61628308 | DEFERIPRONE ARROW 500 mg | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |
| 69438015 | DEFERIPRONE ARROW 1000 mg | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |
| 65987486 | FERRIPROX 500 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 60508302 | FERRIPROX 1000 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 69694018 | FERRIPROX 100 mg/ml | Solution buvable | Non renseignée (AMM annulée) |

Une sixième AMM annulée existe (66508896, DEFERIPRONE LIPOMED 500 mg, comprimé pelliculé).

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 246 interactions ont été identifiées. Parmi les principales, toutes de niveau modéré, figurent les sels de calcium (phosphate, acétate, carbonate, citrate, gluconate, lactate), les sels de magnésium (oxyde, carbonate, chlorure, citrate, gluconate, hydroxyde, sulfate), l'hydroxyde d'aluminium, le magaldrate, l'attapulgite, le kaolin, le sucralfate et le fer. Il s'agit surtout de cations polyvalents et d'antiacides qui peuvent se lier à la déferiprone.

Veuillez consulter la notice pour les mises en garde et contre-indications, qui ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle et sur deux études précliniques (niveau L4), sans essai clinique. Toutes les AMM françaises sont annulées, et les données de sécurité issues de la notice sont absentes, ce qui bloque le passage à l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Mener une revue de littérature ciblée sur la chélation du fer dans les porphyries, notamment la porphyrie cutanée tardive
- Clarifier les raisons de l'annulation des AMM en France et les voies d'accès possibles au médicament
- Évaluer la faisabilité d'une étude clinique exploratoire si les données précliniques sont confirmées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

