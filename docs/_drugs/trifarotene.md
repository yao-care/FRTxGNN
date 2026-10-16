---
layout: default
title: Trifarotene
parent: Prédiction du modèle uniquement (L5)
nav_order: 788
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Trifarotene : nouvelle indication prédite, Élévation du zinc plasmatique (niveau de preuve L5). Indication d'origine : Acné"
monitor_inn: "trifarotene"
predicted_indications: ["zinc, elevated plasma", "pyogenic arthritis-pyoderma gangrenosum-acne syndrome"]
---

# Trifarotene
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

# Trifarotène : De l'Acné à l'Élévation du Zinc Plasmatique

## Résumé en Une Phrase

Le trifarotène est un rétinoïde topique (crème) initialement utilisé pour le traitement de l'acné.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**élévation du zinc plasmatique**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Acné |
| Nouvelle Indication Prédite | Élévation du zinc plasmatique |
| Score de Prédiction TxGNN | 99,40 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisation annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les informations pharmacologiques disponibles, le trifarotène est un agoniste des récepteurs de l'acide rétinoïque (RAR), avec une activité décrite sur les sous-types alpha, bêta et gamma (RARA, RARB, RARG), et il est considéré comme sélectif du sous-type gamma. Son efficacité dans l'acné a été démontrée lors d'essais de phase 3, dont une étude de sécurité à long terme (NCT02189629). Il a été approuvé aux États-Unis en octobre 2019 sous forme de crème à 0,005 %.

**Aucun lien mécanistique établi** n'existe avec l'élévation du zinc plasmatique. Il s'agit d'une anomalie biologique/métabolique et non d'une affection dermatologique pilotée par la signalisation des rétinoïdes. De plus, le trifarotène est très instable sur le plan métabolique, ce qui laisse supposer une exposition systémique limitée en usage topique ; un effet systémique sur le zinc plasmatique paraît donc peu plausible.

Le score TxGNN élevé (99,40 %) reflète une association dans le graphe de connaissances, sans soutien mécanistique, clinique ou bibliographique dans les données disponibles.

### Seconde prédiction (pour information)

Le syndrome PAPA (arthrite pyogène, pyoderma gangrenosum et acné ; score de 99,32 %) est également prédit. Son volet cutané acnéique chevauche l'indication d'origine, ce qui peut expliquer le score. Cependant, il s'agit d'une maladie auto-inflammatoire (mutations de PSTPIP1, activation de l'inflammasome pyrine, excès d'IL-1β) que le trifarotène topique ne traiterait pas. Au mieux, il pourrait être envisagé en appoint pour les lésions cutanées acnéiformes, sans aucun test à ce jour. Aucun essai ni publication n'est disponible.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63631908 | AKLIEF 50 microgrammes/g, crème (GALDERMA INTERNATIONAL) | Crème | Texte d'indication non disponible (AMM annulée) |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : aucune interaction médicamenteuse cliniquement caractérisée n'a été identifiée. Les 3 entrées retrouvées correspondent à des interactions pharmacologiques avec des cibles (récepteurs de l'acide rétinoïque alpha, bêta et gamma), sans niveau de gravité attribué.
- **Exposition systémique** : le trifarotène étant métaboliquement très instable, une exposition systémique limitée est attendue en application topique.

Veuillez consulter la notice pour les informations complètes de sécurité (mises en garde et contre-indications).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai, aucune publication et aucun lien mécanistique plausible ne la soutiennent. L'usage topique avec exposition systémique minimale rend un effet sur le zinc plasmatique improbable, et l'AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice de l'ANSM (mises en garde et contre-indications), indispensable avant tout examen de sécurité
- Compléter les données sur le mécanisme d'action (par exemple via DrugBank)
- Démontrer un lien biologique plausible entre la signalisation RAR et le métabolisme du zinc
- Rechercher des données précliniques ou observationnelles étayant l'indication prédite
- Évaluer la compatibilité de la voie d'administration (topique) avec l'indication visée
- Clarifier le statut réglementaire en France (AMM annulée)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

