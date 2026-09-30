---
layout: default
title: Alglucosidase Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Alglucosidase Alfa
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

# Alglucosidase alfa : De la maladie de Pompe à la maladie à corps de polyglucosanes de l'adulte

## Résumé en Une Phrase

Alglucosidase alfa est une enzyme recombinante (alpha-glucosidase acide humaine), utilisée en thérapie enzymatique substitutive dans la maladie de Pompe (glycogénose de type II).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie à corps de polyglucosanes de l'adulte**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Pompe (glycogénose de type II). Le texte d'indication de l'AMM n'est pas renseigné dans les données fournies. |
| Nouvelle Indication Prédite | Maladie à corps de polyglucosanes de l'adulte (adult polyglucosan body disease) |
| Score de Prédiction TxGNN | 99,47 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de référence. Sur la base des informations connues, l'alglucosidase alfa est une alpha-glucosidase acide recombinante. Elle hydrolyse les liaisons glycosidiques alpha-1,4 et alpha-1,6 du glycogène lysosomal, et son efficacité a été établie dans la maladie de Pompe.

La maladie à corps de polyglucosanes de l'adulte est causée par un déficit en enzyme branchante du glycogène (GBE1). Elle entraîne l'accumulation d'un glycogène mal ramifié (polyglucosane). Le seul point commun est donc le thème général du métabolisme du glycogène.

Le lien reste **plausible mais faible**, pour deux raisons :
- Le polyglucosane s'accumule surtout dans le cytosol des neurones et des axones, alors que l'enzyme agit dans les lysosomes et y accède mal.
- Pour atteindre le système nerveux, le médicament devrait franchir la barrière hémato-encéphalique.

Le score élevé du modèle TxGNN reste une prédiction et ne remplace pas une preuve biologique ou clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61065137 | MYOZYME 50 mg, poudre pour solution à diluer pour perfusion (SANOFI, Pays-Bas) | Poudre pour solution à diluer pour perfusion | Non précisée dans les données disponibles |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été trouvée dans les données interrogées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L5 : il n'existe ni essai ni publication, et le lien mécanistique est faible (enzyme lysosomale face à une accumulation cytosolique, avec passage de la barrière hémato-encéphalique nécessaire).
- Les autres prédictions du classement présentent le même niveau de preuve. Deux formes de glycogénose par déficit en enzyme branchante ont un lien tout aussi faible, car l'enzyme ne corrige pas le déficit de ramification. Les prédictions ophtalmologiques (entropion, ectropion, syndrome de Horner congénital, etc.) n'ont aucun mécanisme plausible et sont probablement des artefacts du graphe de connaissances.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour tout passage à l'étape de criblage de sécurité).
- Les données détaillées sur le mécanisme d'action (DrugBank).
- Des données précliniques montrant que l'enzyme atteint le polyglucosane neuronal, avec une stratégie de passage de la barrière hémato-encéphalique.
- Une revue de la littérature sur les approches de thérapie enzymatique dans les déficits en GBE1.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

