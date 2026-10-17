---
layout: default
title: Teriparatide
parent: Prédiction du modèle uniquement (L5)
nav_order: 745
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Teriparatide : nouvelle indication prédite, Ulcère duodénal (niveau de preuve L5). Indication d'origine : Ostéoporose post-ménopausique"
monitor_inn: "teriparatide"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
---

# Teriparatide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Tériparatide : De l'ostéoporose post-ménopausique à l'ulcère duodénal

## Résumé en Une Phrase

Le tériparatide est un analogue de l'hormone parathyroïdienne (PTH 1-34), initialement utilisé pour traiter l'ostéoporose post-ménopausique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**ulcère duodénal**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette prédiction, qui reste purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Ostéoporose post-ménopausique (d'après le graphe de connaissances, le texte d'indication des AMM n'étant pas renseigné) |
| Nouvelle Indication Prédite | Ulcère duodénal |
| Score de Prédiction TxGNN | 99,86 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 8 (dont 8 annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. On sait toutefois que le tériparatide est un fragment actif de la PTH humaine, qui se lie au récepteur PTH1R (et, dans les bases pharmacologiques, au PTH2R). Administré de façon intermittente, il stimule la formation osseuse. C'est ce qui justifie son usage dans l'ostéoporose chez les patients à haut risque de fracture.

Ce mécanisme est centré sur le remodelage osseux. Aucun lien mécanistique plausible n'a été identifié avec l'ulcère duodénal, qui relève de l'agression de la muqueuse gastro-duodénale (acidité, *Helicobacter pylori*, anti-inflammatoires), et non du métabolisme osseux. Le score élevé du modèle reflète des proximités dans le graphe de connaissances, sans fondement clinique ou biologique démontré.

La prédiction est donc à considérer avec grande prudence. Elle n'est étayée par aucune donnée expérimentale ou clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 8 AMM recensées sont toutes annulées. Le texte de l'indication approuvée n'est pas renseigné pour ces autorisations. Les 5 premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|---------|------|------|------|------|
| 68877066 | Teriparatide Teva 20 µg/80 µL, stylo prérempli | Solution injectable | Teva (Pays-Bas) | Annulée |
| 67114096 | Movymia 20 µg/80 µL | Solution injectable | Stada Arzneimittel AG | Annulée |
| 66987514 | Teriparatide Biogaran 20 µg/80 µL, stylo prérempli | Solution injectable | Biogaran | Annulée |
| 68681263 | Terrosa 20 µg/80 µL | Solution injectable | Gedeon Richter | Annulée |
| 64408915 | Sondelbay 20 µg/80 µL, stylo prérempli | Solution injectable | Accord Healthcare (Espagne) | Annulée |

## Considérations de Sécurité

- **Maladies en contre-indication (graphe de connaissances, et non texte de notice)** : hypercalcémie, hyperparathyroïdie, néphrocalcinose, lithiase urinaire, ostéosarcome, maladie de Paget osseuse (y compris juvénile), ostéomalacie, rachitisme, ostéodystrophie rénale, ostéite fibreuse, troubles du métabolisme du phosphore, hypotension.
- **Interactions médicamenteuses** (8 entrées, dont 6 interactions médicamenteuses) :
  - Modérées : digoxine, digitoxine, calcitriol (topique), calcipotriol (topique).
  - Mineures : hydrochlorothiazide, furosémide.

Les mises en garde et contre-indications issues de la notice officielle ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour l'ulcère duodénal repose uniquement sur le modèle (niveau L5). Elle n'a ni essai clinique, ni publication, ni lien mécanistique plausible avec l'action osseuse du tériparatide.
- Toutes les AMM françaises sont annulées, ce qui limite aussi la faisabilité d'un développement local.

**Pour avancer, les éléments suivants sont nécessaires :**
- Un rationnel biologique crédible reliant l'agonisme PTH1R à la physiopathologie de l'ulcère duodénal, ainsi que des données précliniques.
- Les données détaillées sur le mécanisme d'action.
- Les mises en garde et contre-indications de la notice ANSM, à télécharger depuis le site de l'ANSM.
- La vérification du statut réglementaire actuel du tériparatide en France (toutes les AMM listées sont annulées).

**Piste à évaluer séparément :** parmi les autres prédictions du modèle, l'**ostéoporose associée à la grossesse et à la lactation** (score 99,55 %) est la mieux étayée. Elle repose sur environ 20 publications, essentiellement des séries de cas, des cohortes, une revue systématique avec méta-analyse et des revues, sans essai randomisé identifié (niveau L3). Elle prolonge l'indication originale dans le spectre de l'ostéoporose, mais le tériparatide est déconseillé pendant la grossesse. Cette piste mériterait une évaluation dédiée.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

