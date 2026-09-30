---
layout: default
title: Pyrazinamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
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

# Pyrazinamide : De la Tuberculose à l'Otite Moyenne Infectieuse

## Résumé en Une Phrase

Le pyrazinamide est un antimycobactérien de première ligne, utilisé dans les schémas antituberculeux multi-médicaments (l'indication exacte de l'AMM n'est pas renseignée dans les données reçues).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**otite moyenne infectieuse**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction précise.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les AMM fournies (usage antituberculeux d'après la classe du médicament) |
| Nouvelle Indication Prédite | Otite moyenne infectieuse |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le pyrazinamide fait partie de la classe des antimycobactériens et de l'association fixe Rifater. Son efficacité dans la tuberculose est établie. Il agit surtout sur les bacilles semi-dormants en milieu acide.

Le lien avec l'otite moyenne est faible. Le pyrazinamide n'a pas d'activité établie contre les bactéries responsables des otites courantes. Un lien plausible se limite au sous-ensemble mycobactérien, c'est-à-dire l'otite moyenne tuberculeuse, qui est rare. La prédiction du modèle est donc probablement un signal trop général.

Les indications voisines montrent des signaux plus concrets. Pour la « maladie de l'oreille moyenne » et l'« otite chronique », la littérature est dominée par des cas d'otite tuberculeuse traités par une association antituberculeuse incluant le pyrazinamide (par ex. PMID [26785789](https://pubmed.ncbi.nlm.nih.gov/26785789/), [12680299](https://pubmed.ncbi.nlm.nih.gov/12680299/)). Il s'agit d'une extension de l'indication antituberculeuse à une forme extrapulmonaire, et non d'un nouveau mécanisme. La contribution propre du pyrazinamide ne peut pas être isolée de celle du schéma combiné.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66454982 | PIRILENE 500 mg, comprimé | Comprimé | Non précisée dans les données reçues |
| 64208131 | RIFATER, comprimé enrobé | Comprimé enrobé | Non précisée dans les données reçues |

Les deux produits sont fabriqués par SANOFI WINTHROP INDUSTRIE.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été trouvée dans la base interrogée.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour l'otite moyenne infectieuse repose uniquement sur le score du modèle (L5), sans essai ni publication, et sans lien mécanistique plausible hors cause mycobactérienne.
- Les signaux les plus solides concernent l'otite moyenne tuberculeuse (cas cliniques, niveau L4). Cette piste relève d'une question de recherche, non d'une décision d'adoption.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications, indications autorisées), une lacune bloquante pour le criblage de sécurité
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Reformuler la question en « otite moyenne tuberculeuse » et réaliser une revue systématique ciblée
- Évaluer la pénétration du pyrazinamide dans l'oreille moyenne et l'oreille interne
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

