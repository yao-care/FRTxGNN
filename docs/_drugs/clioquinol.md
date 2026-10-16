---
layout: default
title: Clioquinol
parent: Preuves modérées (L3-L4)
nav_order: 180
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-14
description: "Clioquinol : nouvelle indication prédite, Candidose cutanée (niveau de preuve L4). Indication d'origine : Dermatophyties : pied d'athlète (tinea pedis), tinea corporis…"
---

# Clioquinol
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **7** 
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

# Clioquinol : Des Dermatophyties (Teignes) à la Candidose Cutanée

## Résumé en Une Phrase

Le clioquinol est une hydroxyquinoléine halogénée, initialement utilisée contre les dermatophyties cutanées (pied d'athlète, teigne du corps, atteinte de l'aine et de la région périanale).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **candidose cutanée**,
mais **aucun essai clinique** et seulement **1 publication**, ancienne et indirecte, soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dermatophyties : pied d'athlète (tinea pedis), tinea corporis, dermatophytose de l'aine et de la région périanale (source : graphe de connaissances ; le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Candidose cutanée |
| Score de Prédiction TxGNN | 99,84 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Autorisation annulée uniquement |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le clioquinol est une hydroxyquinoléine halogénée chélatrice de métaux (cuivre, zinc, fer), dotée d'une activité antifongique et antibactérienne. Son efficacité dans les dermatophyties est reconnue et, sur le plan mécanistique, il pourrait être applicable à la candidose cutanée.

La perturbation de l'homéostasie des métaux dans la cellule fongique pourrait s'étendre aux levures du genre *Candida*. Les dermatophyties et la candidose cutanée sont deux mycoses superficielles de la peau, ce qui rend l'extension plausible.

Cette hypothèse reste toutefois théorique : l'unique article retrouvé (1988, prévention de l'infection professionnelle à *Candida albicans* par des additifs de savons) est indirect, et son titre ne montre pas que le clioquinol ait été testé.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [2978600](https://pubmed.ncbi.nlm.nih.gov/2978600/) | 1988 | Rapport de santé préventive/professionnelle | Przeglad dermatologiczny | Étude *in vitro* d'additifs de savons de toilette sur des souches de *C. albicans* de patients ; effet fongicide en solution fortement alcaline. Le clioquinol n'est pas clairement évalué. |

Pour une autre indication prédite, la mycose superficielle, une étude préclinique de 2021 ([33772895](https://pubmed.ncbi.nlm.nih.gov/33772895/), *Mycoses*) a évalué l'association du clioquinol avec le ciclopirox et la terbinafine dans des modèles alternatifs de dermatophytose (activité et toxicité). Elle suggère une synergie antifongique, mais ne constitue pas une preuve d'efficacité clinique.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64835493 | TRUE TEST 36, patch pour test épicutané | Patch | Non renseignée (AMM annulée) |

Ce produit est un patch de test épicutané (diagnostic allergologique) fabriqué par SmartPractice Denmark, et non un antifongique thérapeutique.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance corticosurrénale, maladie d'Addison, atrophie cutanée, télangiectasies, maladies capillaires, maladie de Rendu-Osler, maladie vasculaire périphérique, claudication intermittente, artériopathie périphérique.
- **Autres points** : l'historique de sécurité du clioquinol (neurotoxicité en cas d'exposition systémique) impose la prudence. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

Veuillez consulter la notice pour les informations de sécurité complètes : les mises en garde et contre-indications officielles ne sont pas disponibles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est mécanistiquement plausible, mais elle ne repose que sur le modèle et sur une publication ancienne et indirecte, sans essai clinique. De plus, l'autorisation française est annulée et les données de sécurité officielles sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) auprès de l'ANSM, étape bloquante pour le criblage de sécurité
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Générer des données *in vitro* directes sur les espèces de *Candida*, puis des données précliniques cutanées
- Vérifier la compatibilité de la voie d'administration (topique) et la faisabilité réglementaire, l'AMM étant annulée
- Évaluer le risque de neurotoxicité et d'absorption systémique pour une formulation topique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

