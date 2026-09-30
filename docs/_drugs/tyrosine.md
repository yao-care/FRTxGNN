---
layout: default
title: Tyrosine
parent: Prédiction du modèle uniquement (L5)
nav_order: 329
evidence_level: L5
indication_count: 10
---

# Tyrosine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Tyrosine : De la nutrition en acides aminés au syndrome de la queue de cheval

## Résumé en Une Phrase

La tyrosine est un acide aminé présent dans plusieurs produits de nutrition (solutions pour perfusion d'acides aminés, comprimés Ketosteril). Le texte de l'indication approuvée n'est pas renseigné dans les données ANSM, cette utilisation est donc déduite des noms de produits.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome de la queue de cheval**, mais **aucun essai clinique** et **une seule publication** (un rapport de cas sans lien thérapeutique) existent pour cette direction. Il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM (déduite : nutrition en acides aminés) |
| Nouvelle Indication Prédite | Syndrome de la queue de cheval (cauda equina syndrome) |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. La tyrosine est un acide aminé qui entre dans la composition de solutions de nutrition parentérale et d'autres produits (Aminoven, Aminoplasmal, Aminomix, Ketosteril). Physiologiquement, elle est le précurseur des catécholamines et des hormones thyroïdiennes.

Aucun lien mécanistique n'a été identifié entre la tyrosine et le syndrome de la queue de cheval, qui est une compression des racines nerveuses lombo-sacrées. La seule publication retrouvée est un rapport de cas sur un sarcome à cellules claires, une tumeur de la racine nerveuse S1 qui avait d'abord été diagnostiquée comme un schwannome mélanocytaire. Elle concerne l'anatomopathologie tumorale (voie de la mélanine et de la tyrosinase) et non un rôle thérapeutique de la tyrosine.

Le score élevé du modèle TxGNN provient donc d'une proximité dans le graphe de connaissances, sans soutien clinique. Il doit être traité comme une hypothèse à vérifier, non comme un signal d'efficacité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [17341045](https://pubmed.ncbi.nlm.nih.gov/17341045/) | 2006 | Rapport de cas | Neurosurgical Focus | Sarcome à cellules claires né de la racine nerveuse S1, d'abord diagnostiqué comme schwannome mélanocytaire psammomateux. Aucune intervention par tyrosine. |

Le « S-1 » du résumé désigne la racine nerveuse sacrée, et non l'association médicamenteuse du même nom.

## Informations de Marché en France

Le texte de l'indication approuvée n'est pas disponible pour ces AMM. Sur 20 AMM, les 5 premières sont listées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 66534581 | KETOSTERIL, comprimé enrobé | Comprimé enrobé | Fresenius Kabi France |
| 61960303 | AMINOVEN 10 POUR CENT, solution pour perfusion | Solution pour perfusion | Fresenius Kabi France |
| 69667989 | AMINOVEN 5 POUR CENT, solution pour perfusion | Solution pour perfusion | Fresenius Kabi France |
| 63183821 | AMINOPLASMAL 8, solution pour perfusion | Solution pour perfusion | B Braun Melsungen |
| 61786735 | AMINOMIX 500, solution pour perfusion | Solution et solution pour perfusion | Fresenius Kabi France |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L5 : aucun essai clinique et une seule publication, sans rapport thérapeutique avec la tyrosine. Le score TxGNN seul ne suffit pas.
- Les données de sécurité de la notice ANSM sont absentes, ce qui empêche de passer à l'étape de sélection sur la sécurité.
- Les autres indications prédites du même dossier (par exemple hyperthyroïdie, hyperthyroxinémie, syndrome de tachycardie orthostatique posturale) sont également en Hold. Pour la sphère thyroïdienne, la tyrosine étant un précurseur des hormones thyroïdiennes, un risque d'aggravation est plausible.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, interactions)
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Obtenir le texte des indications approuvées pour les AMM françaises
- Rechercher un rationnel physiopathologique ou des données précliniques reliant la tyrosine à la queue de cheval. Sans cela, ne pas poursuivre l'évaluation.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

