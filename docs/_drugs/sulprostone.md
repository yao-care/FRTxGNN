---
layout: default
title: Sulprostone
parent: Prédiction du modèle uniquement (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
---

# Sulprostone
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

# Sulprostone : D'une Indication Originale Non Renseignée à la Cataracte Tétanique

## Résumé en Une Phrase

Sulprostone est un analogue de la prostaglandine E2 (agoniste principalement des récepteurs EP1/EP3, à action utérotonique), commercialisé en France sous le nom NALADOR. Son indication originale n'est pas renseignée dans les données réglementaires fournies.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **cataracte tétanique**, avec un score très élevé (99,86 %).
Cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans l'AMM (texte d'indication vide) |
| Nouvelle Indication Prédite | Cataracte tétanique (tetanic cataract) |
| Score de Prédiction TxGNN | 99,86 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sulprostone est un analogue de la PGE2 agissant principalement sur les récepteurs EP1 et EP3. Aucune indication originale n'est documentée dans les données fournies.

Aucun lien documenté n'existe entre ce médicament et l'opacité du cristallin liée à l'hypocalcémie, qui caractérise la cataracte tétanique. Toute connexion resterait spéculative. Deux pistes théoriques, non étayées par des données, seraient la signalisation des prostanoïdes dans l'épithélium du cristallin et la régulation du calcium.

Le score élevé doit donc être interprété avec prudence. Il est identique pour plusieurs sous-types de cataracte (99,86 %), ce qui suggère que le modèle propage une association générique au niveau du nœud « cataracte » plutôt qu'un signal propre à chaque sous-type.

## Autres Indications Prédites

Toutes sont de niveau L5, sans essai clinique ni publication, avec une décision Hold.

| Rang | Maladie prédite | Score TxGNN | Commentaire |
|------|------|------|------|
| 2 | Cataracte associée au diabète de type 2 | 99,86 % | Risque cardiovasculaire systémique peu adapté à une population diabétique chronique |
| 3 | Cataracte immature | 99,86 % | Score identique aux autres sous-types, signal probablement générique |
| 4 | Cataracte associée à une craniosténose | 99,86 % | Syndrome rare à base génétique probable, aucun mécanisme plausible |
| 5 | Cataracte mature | 99,86 % | Opacité structurelle établie, réversion pharmacologique peu plausible |
| 6 | Cataracte nucléaire sénile | 99,85 % | Stress oxydatif et agrégation des cristallines, sans lien démontré |
| 7 | Cataracte corticale | 99,85 % | Piste théorique : homéostasie ionique et hydrique de l'épithélium |
| 8 | Cataracte sénile | 99,84 % | Les analogues de prostaglandines oculaires agissent sur les récepteurs FP, un mécanisme différent |
| 9 | Cataracte diabétique | 99,82 % | Voie des polyols et stress oxydatif sans lien démontré |
| 10 | Rétinopathie diabétique | 99,67 % | Hypothèse la plus plausible biologiquement, mais le sens de l'effet d'un agoniste EP1/EP3 est incertain et pourrait être délétère |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61722693 | NALADOR 500 microgrammes, lyophilisat pour usage parentéral (TEOFARMA) | Lyophilisat pour usage parentéral | Texte d'indication non renseigné |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Un point d'attention ressort néanmoins de l'analyse de plausibilité : la sulprostone administrée par voie systémique est associée à un risque cardiovasculaire (par exemple vasospasme coronarien). Cela serait un obstacle important pour une population diabétique chronique.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5). Aucun essai, aucune publication et aucun mécanisme documenté ne la soutiennent, et les données de sécurité de la notice ANSM sont manquantes. Le profil systémique de la voie parentérale est de plus peu compatible avec des affections oculaires chroniques.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications), une étape bloquante pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (MOA) via DrugBank
- Documenter l'indication originale approuvée du produit NALADOR
- Réaliser une revue de littérature préclinique sur la signalisation EP1/EP3 dans le cristallin et la rétine
- Évaluer la compatibilité de la voie d'administration (parentérale) avec une utilisation oculaire, ou envisager une voie locale
- Envisager d'abord la rétinopathie diabétique comme hypothèse prioritaire pour des travaux précliniques uniquement

*Les résultats de ce rapport sont fournis à titre de référence pour la recherche et ne constituent pas un avis médical. Tout candidat au repositionnement doit faire l'objet d'une validation clinique avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

