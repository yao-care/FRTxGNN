---
layout: default
title: Travoprost
parent: Prédiction du modèle uniquement (L5)
nav_order: 325
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost : Du Glaucome à la Calciphylaxie Viscérale

## Résumé en Une Phrase

Travoprost est un analogue de la prostaglandine F2α (agoniste du récepteur FP), utilisé en collyre pour abaisser la pression intraoculaire dans le glaucome à angle ouvert et l'hypertension oculaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **calciphylaxie viscérale**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle seul.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Glaucome à angle ouvert et hypertension oculaire (déduite des essais cliniques ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Calciphylaxie viscérale |
| Score de Prédiction TxGNN | 99.9998% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, le travoprost est un agoniste du récepteur FP de la prostaglandine F2α. Son efficacité dans le glaucome est établie : il augmente l'écoulement uvéoscléral de l'humeur aqueuse et fait ainsi baisser la pression intraoculaire.

**Cette prédiction n'est pas plausible sur le plan pharmacologique.** La calciphylaxie viscérale est une pathologie de calcification vasculaire. Aucun lien pharmacologique connu ne relie l'agonisme FP à ce processus. De plus, un collyre entraîne une exposition systémique négligeable, ce qui rend peu probable l'atteinte des tissus concernés. Le score très élevé du modèle (proche de 1,0) est vraisemblablement un artefact du graphe de connaissances, et non le signe d'un véritable potentiel thérapeutique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68058227 | TRAVOPROST ZENTIVA 40 microgrammes/mL | Collyre en solution | Non renseignée |
| 63367401 | TRAVOPROST BIOGARAN 40 microgrammes/ml | Collyre en solution | Non renseignée |
| 67138300 | VIZITRAV 40 microgrammes/mL | Collyre en solution | Non renseignée |
| 66855039 | TRAVOPROST EG 40 microgrammes/mL | Collyre en solution | Non renseignée |
| 61698064 | TRAVOPROST ARROW 40 microgrammes/mL | Collyre en solution | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (L5), sans essai ni publication. Aucun mécanisme plausible n'est identifié, et une voie ophtalmique topique ne permet pas d'envisager une exposition systémique pertinente.

Parmi les autres indications prédites, seules « maladie vasculaire » et « hémangioendothéliome » disposent de données. Ces données sont soit du glaucome sous un autre nom (mots-clés), soit un signal de prudence : un cas d'effusion uvéale induite par le travoprost chez un patient atteint du syndrome de Sturge-Weber. Aucune ne soutient un bénéfice thérapeutique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde et contre-indications) : bloquant pour le criblage de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Justification mécanistique d'un lien entre l'agonisme FP et la calcification vasculaire
- Données d'exposition systémique après administration oculaire, et éventuellement des études précliniques
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

