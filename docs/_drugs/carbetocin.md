---
layout: default
title: Carbetocin
parent: Prédiction du modèle uniquement (L5)
nav_order: 139
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Carbetocin : nouvelle indication prédite, Syndrome pseudo-isotrétinoïne (niveau de preuve L5). Indication d'origine : Syndrome de Prader-Willi, syndrome de Noonan"
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

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Carbétocine : Du Syndrome de Prader-Willi au Syndrome pseudo-isotrétinoïne

## Résumé en Une Phrase

La carbétocine est un analogue peptidique de l'ocytocine, connu pour la prévention de l'hémorragie du post-partum par atonie utérine. Elle a aussi été explorée dans le syndrome de Prader-Willi et le syndrome de Noonan (indications issues du graphe de connaissances).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome pseudo-isotrétinoïne**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Syndrome de Prader-Willi, syndrome de Noonan (graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Syndrome pseudo-isotrétinoïne |
| Score de Prédiction TxGNN | 99,15 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Annulé uniquement (aucune AMM valide) |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les informations pharmacologiques connues, la carbétocine est un agoniste du récepteur de l'ocytocine (OXTR). Elle est utilisée pour prévenir l'hémorragie du post-partum, et une formulation intranasale (LV-101) a été développée pour le syndrome de Prader-Willi, afin de réduire la faim extrême à l'origine de l'hyperphagie.

Le syndrome pseudo-isotrétinoïne est un phénotype malformatif congénital proche de l'embryopathie à l'acide rétinoïque. Le lien avec les indications d'origine (syndromes développementaux) provient probablement de voisins communs dans le graphe de connaissances, et non d'une justification biologique démontrée.

**Il faut donc rester prudent :** la modulation de la voie de l'ocytocine ne peut raisonnablement pas corriger des malformations structurelles congénitales. La prédiction repose uniquement sur le score du modèle. Une seconde prédiction du même type (syndrome de Goodman, score 99,06 %) présente les mêmes limites et n'est pas développée ici.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68795345 | CARBETOCINE AGUETTANT 100 microgrammes/ml, solution injectable en seringue pré-remplie | Solution injectable | Non renseignée |
| 62023123 | PABAL 100 microgrammes/ml, solution injectable | Solution injectable | Non renseignée |

Les deux AMM (titulaires : AGUETTANT et FERRING France) sont annulées ; aucune AMM n'est actuellement valide.

## Considérations de Sécurité

**Interactions et pharmacologie :** la carbétocine agit sur le récepteur de l'ocytocine (OXTR). Aucune interaction médicamenteuse cliniquement classée n'a été identifiée dans les données compilées.

Veuillez consulter la notice pour les informations de mises en garde et de contre-indications, qui ne sont pas disponibles ici.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur un score élevé du modèle (niveau L5), sans essai clinique, sans publication et sans mécanisme plausible. De plus, aucune AMM française n'est actuellement valide.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Établir une justification biologique reliant la voie de l'ocytocine au syndrome pseudo-isotrétinoïne
- Mener une revue de littérature et de registres d'essais pour détecter toute preuve préclinique ou clinique
- Évaluer la compatibilité des voies d'administration (voie injectable seule disponible) et clarifier le statut réglementaire
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

