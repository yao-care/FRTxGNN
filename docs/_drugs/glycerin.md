---
layout: default
title: Glycerin
parent: Prédiction du modèle uniquement (L5)
nav_order: 368
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Glycerin : nouvelle indication prédite, Syndrome de la queue de cheval (niveau de preuve L5). Indication d'origine : Constipation"
---

# Glycerin
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

# Glycérine : De la constipation au syndrome de la queue de cheval

## Résumé en une phrase

La glycérine est un agent osmotique, initialement utilisée pour traiter la constipation.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome de la queue de cheval**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction issue uniquement du modèle.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Constipation (source : graphe de connaissances ; le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle indication prédite | Syndrome de la queue de cheval |
| Score de prédiction TxGNN | 99,60 % |
| Niveau de preuve | L5 |
| Statut de marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la glycérine est un laxatif osmotique : son efficacité dans la constipation repose sur l'appel d'eau dans la lumière intestinale.

Pour le syndrome de la queue de cheval (atteinte compressive ou inflammatoire des racines nerveuses lombo-sacrées), aucun mécanisme plausible n'est établi pour la glycérine administrée par voie orale ou rectale. La glycérine a été utilisée historiquement comme agent neurolytique intrathécal (par exemple dans la névralgie du trijumeau), mais cela ne constitue pas un lien thérapeutique avec cette pathologie.

Le score élevé du modèle reflète donc une association dans le graphe de connaissances et non une justification pharmacologique. Cette prédiction doit être considérée comme une hypothèse non étayée.

## Preuves d'essais cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la littérature

Aucune littérature associée n'est disponible actuellement.

## Informations de marché en France

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Indication approuvée |
|---------|------|------|-----------|
| 61749306 | GLYCERINUM BOIRON, degré de dilution compris entre 2CH et 30CH ou entre 4DH et 60DH (BOIRON) | Comprimé, solution, granules, poudre et pommade | Non renseignée (AMM annulée) |

## Considérations de sécurité

- **Interactions médicamenteuses** : 220 interactions sont recensées. Parmi les 20 premières, la grande majorité sont de niveau modéré, une seule étant mineure (doxycycline). Exemples d'interactions modérées : abiratérone, tramadol, acétazolamide, hydrocortisone, salbutamol, alfuzosine, hydrochlorothiazide, amiloride, amiodarone, amisulpride, bénazépril, anagrélide, propofol, apalutamide, apomorphine, triamcinolone, trioxyde d'arsenic, luméfantrine, asénapine.

Les mises en garde et contre-indications de la notice n'ont pas pu être obtenues. Veuillez consulter la notice pour ces informations de sécurité.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication, et sans mécanisme plausible pour la voie d'administration usuelle. Le seul produit autorisé en France est une AMM annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action de la glycérine, afin d'analyser tout lien mécanistique
- Mises en garde et contre-indications issues de la notice ANSM (lacune bloquante pour l'évaluation de sécurité)
- Preuves précliniques ou cliniques spécifiques au syndrome de la queue de cheval
- Évaluation de la compatibilité des voies d'administration

**Remarque sur les autres indications prédites :** le glaucome à angle ouvert (rang 2, niveau L4) repose sur un effet osmotique transitoire sur la pression intraoculaire. Il s'agit d'un lien plausible mais indirect, surtout pertinent pour le glaucome aigu par fermeture de l'angle et non pour la prise en charge chronique ; les publications retrouvées ne fournissent pas de preuve directe. Le syndrome de l'intestin irritable (rang 6) est mécanistiquement proche de l'indication d'origine, mais reste sans preuve (L5). Toutes les autres prédictions classées (glaucome héréditaire primaire, alopécies, hypotrichoses, migraines) restent au niveau L5 ou sans évidence d'efficacité, avec une recommandation Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

