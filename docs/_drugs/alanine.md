---
layout: default
title: Alanine
parent: Prédiction du modèle uniquement (L5)
nav_order: 31
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Alanine : nouvelle indication prédite, Gastroparésie (niveau de preuve L5). Indication d'origine : Non précisée dans les données d'AMM"
monitor_inn: "ALANINE"
predicted_indications: ["gastroparesis (disease)"]
---

# Alanine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Alanine : D'un acide aminé nutritionnel à la gastroparésie
{: .text-alpha }

## Resume en Une Phrase

L'alanine est un acide aminé non essentiel, présent dans de nombreux produits de nutrition parentérale et de dialyse péritonéale commercialisés en France (aujourd'hui tous annulés).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **gastroparésie**, mais cette prédiction repose uniquement sur un score informatique.
Aucun essai clinique n'est enregistré, et les **3 publications** retrouvées ne traitent ni de l'alanine comme traitement ni de la gastroparésie comme critère de résultat.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données d'AMM |
| Nouvelle Indication Predite | Gastroparésie |
| Score de Prediction TxGNN | 99,37 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Toutes les AMM sont annulées |
| Nombre d'AMM | 20 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'alanine est un acide aminé non essentiel impliqué dans le cycle glucose-alanine et la néoglucogenèse hépatique. Elle entre dans la composition de nombreuses solutions de nutrition parentérale et de dialyse péritonéale.

Aucun lien mécanistique entre l'alanine et la gastroparésie n'est établi dans les données compilées. Une piste purement spéculative passerait par les perturbations métaboliques et hépatiques liées au diabète, première cause de gastroparésie. Il s'agit d'une inférence qu'aucune étude fournie ne soutient.

Le score élevé de TxGNN (0,994) est une prédiction computationnelle et non une preuve clinique. Il doit être considéré comme une simple hypothèse de départ.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [10926110](https://pubmed.ncbi.nlm.nih.gov/10926110/) | 2000 | Revue | Advances in Renal Replacement Therapy | Troubles digestifs et hépatiques dans l'insuffisance rénale terminale ; la gastroparésie y est plus fréquente. L'alanine n'est pas évaluée comme traitement. |
| [26315331](https://pubmed.ncbi.nlm.nih.gov/26315331/) | 2016 | Revue | Diabetic Medicine | Hépatosclérose diabétique, possible complication microvasculaire du diabète. Sans lien avec l'alanine ni la gastroparésie. |
| [33763324](https://pubmed.ncbi.nlm.nih.gov/33763324/) | 2021 | Revue (cas clinique) | Cureus | Hépatopathie glycogénique chez une patiente diabétique de type 1 ayant aussi une gastroparésie. La gastroparésie n'est qu'une comorbidité. |

Ces publications sont indirectes : aucune n'étudie l'alanine comme traitement de la gastroparésie.

---

## Informations de Marche en France

Les 20 AMM sont annulées. Les textes d'indication ne sont pas disponibles. Voici les 5 premières :

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 64728712 | ABUFENE 400 mg, comprimé | comprimé | Non disponible |
| 61960303 | AMINOVEN 10 POUR CENT | solution pour perfusion | Non disponible |
| 69667989 | AMINOVEN 5 POUR CENT | solution pour perfusion | Non disponible |
| 63183821 | AMINOPLASMAL 8 | solution pour perfusion | Non disponible |
| 61786735 | AMINOMIX 500 | solution et solution pour perfusion | Non disponible |

---

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (liaisons médicament-maladie, et non texte de notice) : maladie rénale, insuffisance rénale chronique et terminale, néphrolithiase, néphrocalcinose, hypercalcémie, sarcoïdose, maladies cardiaques et cardiovasculaires, intoxication digitalique, fibrillation ventriculaire, phénylcétonurie et troubles du métabolisme de la phénylalanine, néphropathie urique aiguë, pyourètre, troubles du métabolisme du phosphore.
- Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être récupérées.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La seule base est un score TxGNN élevé (niveau L5) : aucun essai clinique, aucune littérature directe et aucun lien mécanistique démontré. Toutes les AMM françaises sont annulées et les données de sécurité officielles manquent.

**Pour avancer, les elements suivants sont necessaires :**
- Récupérer les mises en garde et contre-indications officielles (notices ANSM), étape bloquante pour l'examen de sécurité
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Établir un lien mécanistique plausible entre l'alanine et la motricité gastrique
- Rechercher des études précliniques ou cliniques ciblant directement l'alanine dans la gastroparésie
- Vérifier la compatibilité de la voie d'administration et de la forme pharmaceutique avec cette indication
- Évaluer les contre-indications rénales et cardiovasculaires, fréquentes chez les patients gastroparétiques diabétiques
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

