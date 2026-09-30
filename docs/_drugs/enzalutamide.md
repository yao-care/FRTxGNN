---
layout: default
title: Enzalutamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 119
evidence_level: L5
indication_count: 7
---

# Enzalutamide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Enzalutamide : Du Cancer de la Prostate à la Prédisposition Génétique au Cancer de la Prostate/du Cerveau

## Résumé en Une Phrase

Enzalutamide est un inhibiteur du récepteur des androgènes, utilisé en pratique dans le cancer de la prostate (le texte d'indication de l'AMM n'est pas renseigné dans les données reçues et doit être vérifié).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **prédisposition génétique au cancer de la prostate/du cerveau**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Prédisposition génétique au cancer de la prostate/du cerveau (prostate cancer/brain cancer susceptibility) |
| Score de Prédiction TxGNN | 99,71 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, l'enzalutamide est un antagoniste du récepteur des androgènes, et son efficacité dans le cancer de la prostate est documentée par de nombreux essais. Mécanistiquement, il pourrait donc être lié à des maladies proches de la prostate.

La « nouvelle indication » prédite est toutefois un nœud d'ontologie de susceptibilité génétique, et non une maladie traitable en clinique. Le score élevé reflète très probablement la proximité, dans le graphe de connaissances, avec le cancer de la prostate, pour lequel l'enzalutamide est déjà utilisé. Il ne s'agit pas d'un signal de repositionnement exploitable.

Aucun essai ni aucune publication ne permet d'évaluer ce lien. La prédiction reste donc purement algorithmique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64093355 | XTANDI 40 mg, comprimé pelliculé (ASTELLAS PHARMA EUROPE, Pays-Bas) | Comprimé pelliculé | Non précisée dans les données reçues |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (hormonothérapie, inhibiteur du récepteur des androgènes) |
| Risque de Myélosuppression, Émétogénicité, Éléments de Surveillance, Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction porte sur un nœud de susceptibilité génétique, sans essai ni publication, avec un niveau de preuve L5. Le score TxGNN élevé s'explique surtout par la proximité avec le cancer de la prostate dans le graphe.
- À titre d'information, le terme parent « cancer des organes reproducteurs masculins » (rang 6) atteint le niveau L2 grâce à l'essai randomisé de phase 2 NCT01288911 (enzalutamide vs bicalutamide, 375 patients). Il correspond cependant à une utilisation déjà conforme à l'indication connue (cancer de la prostate), et non à un véritable repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante : le criblage de sécurité S1 est impossible sans elles)
- Le texte de l'indication de l'AMM 64093355 et l'indication originale, pour vérifier ce qui relève réellement d'un repositionnement
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Le choix d'une indication cliniquement traitable, à la place du nœud de susceptibilité génétique, avant toute évaluation supplémentaire
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

