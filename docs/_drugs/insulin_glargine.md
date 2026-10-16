---
layout: default
title: Insulin Glargine
parent: Prédiction du modèle uniquement (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Insulin Glargine : nouvelle indication prédite, Ovarite auto-immune (niveau de preuve L5). Indication d'origine : Diabète de type 2, diabète de type 1, acidocétose diabétique"
---

# Insulin Glargine
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

# Insuline glargine : Du diabète de type 1 et 2 à l'ovarite auto-immune

## Résumé en Une Phrase

L'insuline glargine est une insuline basale à action prolongée, initialement utilisée pour le traitement du diabète (de type 1 et de type 2) et de l'acidocétose diabétique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**ovarite auto-immune**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction : elle repose uniquement sur le score du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Diabète de type 2, diabète de type 1, acidocétose diabétique (texte d'indication de l'AMM non disponible ; indications issues du graphe de connaissances) |
| Nouvelle Indication Prédite | Ovarite auto-immune |
| Score de Prédiction TxGNN | 99,88 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 8 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'insuline glargine est un analogue de l'insuline humaine à action prolongée, dont l'efficacité dans le diabète est établie.

Le lien avec l'ovarite auto-immune est probablement indirect. Cette maladie est souvent associée à des syndromes polyendocriniens auto-immuns, qui incluent un diabète auto-immun. Le score élevé reflète donc vraisemblablement une proximité dans le réseau de maladies, et non un effet thérapeutique sur l'ovarite elle-même. L'insuline traiterait tout au plus un diabète associé.

Cette hypothèse n'est étayée par aucune étude et doit être considérée comme une prédiction purement computationnelle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'ovarite auto-immune.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61404477 | LANTUS 100 unités/ml, cartouche | Solution injectable | Non renseignée (AMM annulée) |
| 62030744 | TOUJEO 300 unités/ml DoubleStar, stylo prérempli | Solution injectable | Non renseignée (AMM annulée) |
| 68378405 | TOUJEO 300 unités/ml SoloStar, stylo prérempli | Solution injectable | Non renseignée (AMM annulée) |
| 64332894 | ABASAGLAR 100 unités/ml, stylo prérempli | Solution injectable | Non renseignée (AMM annulée) |
| 60408661 | SEMGLEE 100 unités/ml, stylo prérempli | Solution injectable | Non renseignée (AMM annulée) |

Trois autres AMM annulées existent (LANTUS en flacon, LANTUS SOLOSTAR, ABASAGLAR en cartouche).

## Considérations de Sécurité

- **Interactions médicamenteuses** : 352 interactions recensées. Les principales, de niveau modéré, concernent :
  - d'autres antidiabétiques (metformine, pioglitazone, alogliptine, albiglutide) ;
  - des sympathomimétiques et bêta-agonistes (épinéphrine, salbutamol, formotérol, phényléphrine, pseudoéphédrine) ;
  - des corticoïdes (hydrocortisone) ;
  - des œstrogènes (estradiol, éthinylestradiol) ;
  - l'acébutolol, l'acétazolamide, l'hydrochlorothiazide, la doxycycline, l'alpélisib et l'éthanol.

  Quelques interactions mineures concernent des corticoïdes topiques (hydrocortisone, alclométasone).

Les mises en garde et contre-indications de la notice n'ont pas pu être compilées. Veuillez consulter la notice pour ces informations.

## Autres Prédictions Examinées

Les autres prédictions du modèle ne changent pas cette évaluation :

- **Syndrome de dysfonctionnement répondant à la thiamine, syndrome de la personne raide classique, syndrome du membre raide focal** : la prédiction reflète vraisemblablement un diabète associé. L'insuline traiterait ce diabète, non la maladie sous-jacente (niveau L5, Hold).
- **Opsismodysplasie** : lien spéculatif via INPPL1/SHIP2 dans la signalisation de l'insuline, sans aucune donnée (L5, Hold).
- **Agénésie pancréatique** : l'insuline basale est cohérente sur le plan mécanistique, mais il s'agit en pratique de l'indication d'origine (diabète insulinopénique). La littérature trouvée est indirecte (revues générales, étude vétérinaire chez le chat, cas de MODY5 traité par un agoniste du GLP-1) (niveau L4, question de recherche).
- **Lipodystrophies localisées** (médicamenteuse, centrifuge, induite par la pression, idiopathique) : les injections d'insuline peuvent elles-mêmes provoquer une lipodystrophie localisée. Ce signal est à lire comme une considération de sécurité, non comme une opportunité thérapeutique (L5, Hold).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction pour l'ovarite auto-immune repose uniquement sur le score du modèle (L5), sans essai ni publication. Le lien plausible passe par un diabète auto-immun associé et non par un effet de l'insuline glargine sur la maladie. De plus, toutes les AMM françaises sont annulées et les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données de mécanisme d'action (DrugBank)
- Les mises en garde et contre-indications de la notice (site de l'ANSM)
- Une recherche ciblée de la littérature et des essais sur l'ovarite auto-immune
- Une clarification du statut réglementaire actuel, toutes les AMM listées étant annulées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

