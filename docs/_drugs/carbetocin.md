---
layout: default
title: Carbetocin
parent: Prédiction du modèle uniquement (L5)
nav_order: 139
evidence_level: L5
indication_count: 2
monitor_inn: "carbetocin"
predicted_indications: ["isotretinoin-like syndrome", "Goodman syndrome"]
last_modified_at: 2026-11-20
description: "Carbetocin : nouvelle indication prédite, Syndrome pseudo-isotrétinoïne (isotretinoin-like syndrome) (niveau de preuve L5). En France, AMM dans la BDPM : 2 (valides : 2)"
---

# Carbetocin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Carbétocine : agoniste du récepteur de l'ocytocine → syndrome pseudo-isotrétinoïne (isotretinoin-like syndrome)
{: .text-alpha }

## Résumé en Une Phrase

La carbétocine est un analogue de l'ocytocine, qui agit sur le récepteur de l'ocytocine et est utilisé pour prévenir l'hémorragie du post-partum liée à l'atonie utérine.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome pseudo-isotrétinoïne (isotretinoin-like syndrome)**,
mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Syndrome pseudo-isotrétinoïne (isotretinoin-like syndrome) |
| Score de Prédiction TxGNN | 0,9915 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon ChEMBL (EMBL-EBI), le mécanisme d'action enregistré pour Carbetocin est (traduction non officielle) : « Agoniste des récepteurs de l'ocytocine ». Texte original en anglais : "Oxytocin receptor agonist" ([ChEMBL CHEMBL3301668 (carbetocin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3301668), CC BY-SA 3.0 ; consulté le 2026-11-19). Ce que l'on sait, c'est que la carbétocine est un agoniste du récepteur de l'ocytocine (gène OXTR). Une formulation intranasale est par ailleurs en développement dans le syndrome de Prader-Willi, pour réduire la sensation de faim extrême.

Le lien avec le syndrome pseudo-isotrétinoïne repose uniquement sur un score de prédiction élevé du modèle. Ce syndrome correspond à un phénotype de malformations congénitales proche de l'embryopathie rétinoïque. La connexion probable passe par des éléments voisins partagés dans le modèle, sans fondement biologique démontré ici.

Il est peu vraisemblable qu'une modulation de la voie de l'ocytocine puisse corriger des malformations congénitales structurelles. La prédiction doit donc être considérée comme une hypothèse purement computationnelle, sans justification mécanistique vérifiable.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

La carbétocine est commercialisée en France. Les données compilées recensent 2 AMM, présentées sous forme de solution injectable :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 68795345 | CARBETOCINE AGUETTANT 100 microgrammes/ml, solution injectable en seringue pré-remplie | Solution injectable |
| 62023123 | PABAL 100 microgrammes/ml, solution injectable | Solution injectable |

## Considérations de Sécurité

**Interactions et pharmacologie :** une seule entrée est recensée, la cible pharmacologique de la carbétocine, le récepteur de l'ocytocine (OXTR). Aucune interaction médicamenteuse cliniquement caractérisée n'est disponible.

Veuillez consulter la notice pour les mises en garde et contre-indications.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau de preuve L5), sans essai clinique, sans publication et sans mécanisme plausible. La plausibilité biologique est faible.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action de la carbétocine
- Justification biologique d'un lien entre la voie de l'ocytocine et le syndrome pseudo-isotrétinoïne
- Études précliniques ou cliniques portant directement sur cette maladie
- Récupération et analyse de la notice (mises en garde et contre-indications) pour le dépistage de sécurité

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé (révisé le 2026-11-20 ; version antérieure conservée dans le journal) | [ChEMBL CHEMBL3301668 (carbetocin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3301668) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

