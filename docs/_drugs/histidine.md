---
layout: default
title: Histidine
parent: Prédiction du modèle uniquement (L5)
nav_order: 144
evidence_level: L5
indication_count: 2
---

# Histidine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Histidine : D'un Acide Aminé de Nutrition et de Conservation d'Organes à la Gastroparésie

## Résumé en Une Phrase

L'histidine est un acide aminé présent dans plusieurs produits commercialisés en France : solutions de conservation d'organes, solutions de nutrition parentérale et un complément d'acides aminés pour l'insuffisance rénale. Le texte d'indication officiel n'est pas renseigné dans les données ANSM disponibles.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **gastroparésie**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée dans les données ANSM (texte d'indication vide) |
| Nouvelle Indication Prédite | Gastroparésie |
| Score de Prédiction TxGNN | 99,55 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. L'histidine est un acide aminé entrant dans la composition de solutions de conservation d'organes, de solutions de perfusion et de préparations nutritionnelles. Son efficacité dans une indication précise n'est pas documentée dans les données fournies, et sa transposition mécanistique à la gastroparésie n'est pas démontrée.

Le seul élément biologique connu est que l'histidine est le précurseur de l'histamine. Un lien avec la motilité gastrique serait donc envisageable en théorie. Aucune donnée fournie ne l'étaye : la prédiction repose uniquement sur le score du graphe de connaissances TxGNN (rang 3483), sans essai clinique ni publication.

À titre de contexte, la deuxième prédiction du modèle (cholangite sclérosante) dispose de publications précliniques. Elles suggèrent que la voie histidine → histamine est plutôt pathogène dans les maladies biliaires, ce qui va à l'encontre d'un effet bénéfique d'une supplémentation. Cela invite à la prudence sur l'hypothèse « histidine = histamine bénéfique ».

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Cinq des 20 AMM sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Fabricant |
|---------|------|------|-----------|
| 68491709 | PERISOC, solution de cardioplégie / solution pour conservation d'organe | Solution cardioplégique | Dr. Franz Köhler Chemie (Allemagne) |
| 65635346 | CELSIOR, solution pour conservation d'organes | Solution | Institut Georges Lopez |
| 66534581 | KETOSTERIL, comprimé enrobé | Comprimé enrobé | Fresenius Kabi France |
| 61960303 | AMINOVEN 10 POUR CENT, solution pour perfusion | Solution pour perfusion | Fresenius Kabi France |
| 69667989 | AMINOVEN 5 POUR CENT, solution pour perfusion | Solution pour perfusion | Fresenius Kabi France |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (L5), sans aucune donnée clinique ni bibliographique pour la gastroparésie. Les informations de sécurité de l'ANSM et le mécanisme d'action manquent, ce qui bloque le passage à l'étape de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications des notices ANSM (donnée bloquante)
- Obtenir les données de mécanisme d'action via DrugBank
- Rechercher des études sur l'histidine, ou sur la voie histaminique, dans la motilité gastrique et la gastroparésie
- Clarifier les indications officielles des produits contenant de l'histidine
- Évaluer la compatibilité des voies d'administration (orale ou parentérale) avec l'usage visé

*Ce rapport est fourni à titre de référence pour la recherche et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

