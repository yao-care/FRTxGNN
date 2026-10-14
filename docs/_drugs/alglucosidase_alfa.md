---
layout: default
title: Alglucosidase Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 37
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

# Alglucosidase alfa : De la maladie de stockage du glycogène à la maladie des corps de polyglucosanes de l'adulte

## Résumé en Une Phrase

Alglucosidase alfa est une enzyme recombinante (alpha-glucosidase acide) initialement utilisée pour le traitement de la maladie de stockage du glycogène.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie des corps de polyglucosanes de l'adulte**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit uniquement d'une prédiction du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de stockage du glycogène (source : graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Maladie des corps de polyglucosanes de l'adulte |
| Score de Prédiction TxGNN | 99,47 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement, aucune étude réelle) |
| Statut de Marché en France | Uniquement annulé (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

> Remarque : les données compilées classent cette prédiction en L4 (« question de recherche »). En l'absence de toute étude préclinique, de mécanisme ou clinique, le niveau L5 est retenu ici selon la grille d'évaluation. Dans tous les cas, la décision recommandée reste prudente.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, l'alglucosidase alfa est une forme recombinante de l'alpha-glucosidase acide (GAA), qui dégrade le glycogène dans les lysosomes. Son efficacité a été établie dans la maladie de stockage du glycogène de type II (maladie de Pompe), et elle pourrait, sur le plan conceptuel, concerner d'autres maladies du métabolisme du glycogène.

La maladie des corps de polyglucosanes de l'adulte est causée par un déficit en enzyme branchante du glycogène (GBE1). Il en résulte une accumulation de polyglucosane mal ramifié et insoluble dans les neurones et d'autres tissus. Le lien avec l'indication d'origine est donc limité au métabolisme commun du glycogène.

La prédiction doit être interprétée avec une grande prudence : le polyglucosane s'accumule dans le cytosol, alors que la GAA agit dans les lysosomes. De plus, une enzyme administrée par voie intraveineuse a peu de chances de franchir la barrière hémato-encéphalique pour atteindre les neurones touchés. Le score élevé reflète la proximité dans le réseau des maladies de stockage du glycogène, et non une efficacité démontrée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61065137 | MYOZYME 50 mg, poudre pour solution à diluer pour perfusion (SANOFI, Pays-Bas) — AMM annulée | Poudre pour solution à diluer pour perfusion | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été identifiée dans les données compilées.

## Autres Prédictions du Modèle

Les autres prédictions les mieux classées ne disposent d'aucune preuve clinique ni bibliographique (niveau L5, décision Hold) :

| Maladie prédite | Score TxGNN | Commentaire |
|------|------|------|
| Déficit en enzyme branchante (forme neuromusculaire congénitale) | 99,32 % | L'enzyme déficiente n'est pas la GAA ; proximité de classification uniquement |
| Déficit en enzyme branchante (forme périnatale fatale) | 99,32 % | Même constat ; absence de données cliniques |
| Entropion congénital | 99,22 % | Malformation palpébrale structurelle ; aucun mécanisme plausible |
| Ectropion congénital | 99,17 % | Prise en charge chirurgicale ; probable artéfact du modèle |
| Syndrome de Horner congénital | 99,17 % | Atteinte de la voie oculosympathique ; aucun lien établi |
| Syndrome ptosis-paralysie des cordes vocales | 99,15 % | Aucun lien mécanistique |
| Camptodactylie, myopie et fibrose du muscle droit médial | 99,11 % | Probable artéfact du modèle |
| Épiblépharon | 99,11 % | Anomalie palpébrale ; aucun mécanisme plausible |
| Syndrome ptosis-strabisme-pupilles ectopiques | 99,10 % | Aucune donnée corroborante |

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur la proximité dans le graphe de connaissances, sans aucun essai clinique ni publication. Le mécanisme (enzyme lysosomale face à une accumulation cytosolique, faible pénétration cérébrale) rend l'efficacité peu plausible.
- L'AMM française est annulée, et les données de sécurité de la notice sont manquantes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications) et analyser son contenu
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Mener des études précliniques (modèles de déficit en GBE1) évaluant l'action de la GAA sur le polyglucosane et sa distribution tissulaire, notamment cérébrale
- Rechercher systématiquement la littérature et les registres d'essais pour confirmer l'absence ou la présence de données
- Vérifier la disponibilité commerciale du produit, l'AMM étant annulée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

