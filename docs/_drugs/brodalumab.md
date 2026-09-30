---
layout: default
title: Brodalumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 62
evidence_level: L5
indication_count: 10
---

# Brodalumab
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

# Brodalumab : Du Psoriasis en Plaques à la Strongyloïdose

*(L'indication d'origine vient des connaissances générales sur le médicament : le texte d'indication de l'AMM n'est pas renseigné dans les données extraites.)*

## Résumé en Une Phrase

Brodalumab (Kyntheum) est un anticorps antagoniste du récepteur IL-17RA, connu pour le traitement des maladies inflammatoires cutanées comme le psoriasis en plaques.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **strongyloïdose**, mais **aucun essai clinique et aucune publication** ne soutiennent cette prédiction, et le raisonnement biologique va plutôt dans le sens contraire.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM extraites |
| Nouvelle Indication Prédite | Strongyloïdose |
| Score de Prédiction TxGNN | 99,84 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la source. D'après l'analyse associée, le brodalumab est un antagoniste d'IL-17RA : il bloque la signalisation de l'interleukine-17.

Or l'IL-17 participe à la défense des muqueuses et à la défense contre certains agents infectieux, dont les helminthes. Bloquer cette voie pourrait donc **augmenter** le risque d'infection plutôt que la traiter. Le score élevé de TxGNN n'est appuyé par aucune justification biologique identifiée. Il s'agit très probablement d'un artefact du graphe de connaissances.

Cette prédiction ne peut pas être considérée comme plausible en l'état. Elle n'est là que pour mémoire.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65620419 | KYNTHEUM 210 mg, solution injectable en seringue préremplie (LEO Pharma A/S, Danemark) | Solution injectable | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Deux points figurent néanmoins dans l'analyse associée à ce dossier :
- **Risque infectieux** : le blocage de l'IL-17 peut affaiblir la défense contre certaines infections, ce qui pèse directement sur la prédiction évaluée ici.
- **Idées et comportements suicidaires** : cet avertissement encadré est cité dans l'analyse associée. Il n'a pas été vérifié dans la notice ANSM.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5). Aucun essai ni aucune publication ne la soutient, et le mécanisme d'action va à l'encontre d'un bénéfice contre un parasite.

**Note sur les autres prédictions :** parmi les 10 prédictions du dossier, seule « maladie oculaire » (rang 2) s'appuie sur des éléments, à savoir un essai observationnel sans lien confirmé avec le brodalumab et une revue sur le blocage de l'IL-17. Elle est classée niveau L4, comme question de recherche. Les autres (carence vitaminique, anomalie de von Hippel, névrites optiques, épisclérites) restent en niveau L5 et en Hold.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde et contre-indications). Ce point est bloquant pour l'évaluation de sécurité.
- Obtenir les données de mécanisme d'action via l'API DrugBank.
- Préciser l'indication d'origine à partir du RCP de l'AMM 65620419.
- Toute piste ultérieure devrait porter sur la prédiction de rang 2 (atteintes oculaires inflammatoires), pas sur la strongyloïdose.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

