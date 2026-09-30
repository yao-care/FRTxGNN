---
layout: default
title: Glucarpidase
parent: Prédiction du modèle uniquement (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Glucarpidase
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

# Glucarpidase : De la Toxicité du Méthotrexate à la Cataracte Diabétique

## Résumé en Une Phrase

La glucarpidase est une enzyme recombinante utilisée à l'origine pour hydrolyser le méthotrexate présent en excès dans le sang. Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **cataracte diabétique**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette prédiction, qui repose uniquement sur un calcul du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Le texte d'indication n'est pas renseigné dans l'AMM. Usage connu : élimination du méthotrexate extracellulaire (d'après la description du mécanisme) |
| Nouvelle Indication Prédite | Cataracte diabétique |
| Score de Prédiction TxGNN | 99,85 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations connues, la glucarpidase est une carboxypeptidase G2 recombinante. Elle hydrolyse le méthotrexate extracellulaire et d'autres substrats contenant du glutamate.

**En pratique, cette prédiction n'est pas plausible sur le plan mécanistique.** La glucarpidase est une grosse protéine qui agit sur le méthotrexate dans le plasma. Rien n'indique qu'elle agisse sur le cristallin, la voie des polyols, la glycation, le stress oxydatif du cristallin ou les voies vasculaires et inflammatoires de la rétine. Administrée par voie systémique, elle devrait aussi pénétrer très peu dans l'œil.

Le score élevé (99,85 %) reflète vraisemblablement des voisins communs dans le graphe de connaissances, notamment autour des pathologies de la cataracte. Il ne traduit pas une biologie commune avec le médicament.

Les neuf autres prédictions du modèle vont dans le même sens :
- rétinopathie diabétique ;
- cataracte craniosténotique ;
- cataracte mature ;
- cataracte tétanique ;
- cataracte associée au diabète de type 2 ;
- cataracte immature ;
- cataracte corticale ;
- cataracte sénile nucléaire ;
- cataracte sénile.

Toutes ont des scores compris entre 99,82 % et 99,84 %, sont classées L5 et n'ont ni essai ni publication associés. Aucun lien mécanistique n'a été identifié pour aucune d'entre elles.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 60176597 | VORAXAZE 1000 unités, poudre pour solution injectable (SERB) | Poudre pour solution injectable |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction relève uniquement du modèle (L5), sans essai clinique ni publication.
- Elle ne repose sur aucun mécanisme plausible : la glucarpidase agit sur le méthotrexate plasmatique, et sa pénétration oculaire attendue est faible.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM, à récupérer et analyser (obstacle bloquant pour le criblage de sécurité).
- Les données détaillées sur le mécanisme d'action (MOA), à obtenir via DrugBank.
- Des études précliniques ou mécanistiques montrant un effet sur le cristallin ou la rétine.
- Une évaluation de la faisabilité d'une voie d'administration oculaire, la voie systémique étant peu adaptée.

*Ces résultats sont fournis à titre de référence pour la recherche et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

