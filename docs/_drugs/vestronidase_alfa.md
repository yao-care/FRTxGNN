---
layout: default
title: Vestronidase Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 334
evidence_level: L5
indication_count: 9
---

# Vestronidase Alfa
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Vestronidase alfa : De la mucopolysaccharidose de type VII (MPS VII) au syndrome de Scheie

## Résumé en Une Phrase

Vestronidase alfa est une enzyme recombinante (β-glucuronidase humaine, GUSB), initialement utilisée pour traiter la mucopolysaccharidose de type VII (MPS VII).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome de Scheie** (MPS I atténuée), mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.
L'analyse mécanistique est même défavorable : la GUSB ne peut pas remplacer l'enzyme déficiente dans cette maladie (IDUA).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | MPS VII (le texte d'indication de l'AMM n'est pas renseigné dans la base) |
| Nouvelle Indication Prédite | Syndrome de Scheie |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, vestronidase alfa est une enzymothérapie substitutive (ERT) par β-glucuronidase recombinante. Son efficacité dans la MPS VII a été démontrée, et elle agit sur le catabolisme lysosomal des glycosaminoglycanes (GAG).

Le syndrome de Scheie est dû à un déficit en alpha-L-iduronidase (IDUA). La GUSB retire les résidus d'acide glucuronique terminaux, alors que l'IDUA retire les résidus d'acide iduronique terminaux. La GUSB ne peut donc pas se substituer à l'IDUA. Le lien n'existe qu'au niveau de la classe (voie de dégradation lysosomale des GAG). Une ERT spécifique à base d'IDUA (laronidase) existe déjà pour cette maladie.

Le score TxGNN très élevé reflète probablement la proximité des maladies MPS dans le graphe de connaissances, et non une cible enzymatique commune. Cette prédiction doit donc être considérée comme un signal de classe, pas comme une hypothèse thérapeutique solide.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour le syndrome de Scheie.

À titre d'information, l'essai de Phase 1 [NCT04532047](https://clinicaltrials.gov/study/NCT04532047) (PEARL, ERT prénatale dans les maladies lysosomales, n=10, en recrutement) est lié à une autre prédiction, le syndrome de Hurler. Il s'agit d'une plateforme multi-maladies, et rien ne confirme que vestronidase alfa y soit utilisée. Il n'apporte donc aucun soutien au syndrome de Scheie.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour le syndrome de Scheie.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61759695 | MEPSEVII 2 mg/ml, solution à diluer pour perfusion (ULTRAGENYX GERMANY) | Solution à diluer pour perfusion | Texte non renseigné dans la base |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication. L'argument enzymatique est défavorable, car la GUSB ne peut pas remplacer l'IDUA. Un traitement spécifique (laronidase) est déjà disponible.
- Les autres prédictions du dossier ne changent pas cette conclusion. Celles pour le syndrome de Hurler et le syndrome de Sanfilippo relèvent de la simple question de recherche (L4) : elles ne reposent que sur une plateforme d'essai non spécifique et sur des publications portant sur la MPS VII. Le reste des prédictions ne présente aucun lien plausible.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde, contre-indications), étape bloquante pour tout criblage de sécurité
- Obtenir les données de mécanisme d'action depuis DrugBank
- Obtenir le texte d'indication de l'AMM 61759695 pour confirmer l'indication originale
- Justifier, par des données précliniques, une activité de la GUSB sur les substrats de l'IDUA. Sans cela, il n'y a pas de raison d'engager une étude clinique dans le syndrome de Scheie.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

