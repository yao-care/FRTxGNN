---
layout: default
title: Povidone
parent: Prédiction du modèle uniquement (L5)
nav_order: 619
evidence_level: L5
indication_count: 1
---

# Povidone
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Povidone : Du Syndrome de l'Œil Sec à l'Érythrodermie Ichtyosiforme Congénitale

## Résumé en Une Phrase

Povidone est un polymère hydrophile utilisé comme lubrifiant et humectant dans des collyres, initialement destiné au traitement du syndrome de l'œil sec (xérophtalmie).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**érythrodermie ichtyosiforme congénitale**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Syndrome de l'œil sec, xérophtalmie (les textes d'indication des AMM ne sont pas renseignés ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Érythrodermie ichtyosiforme congénitale |
| Score de Prédiction TxGNN | 99,11 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 7 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la povidone est un polymère hydrophile utilisé comme lubrifiant et humectant dans les produits ophtalmiques. Son utilité dans l'œil sec repose sur sa capacité à retenir l'eau et à former un film protecteur.

L'hypothèse, purement spéculative, est que ces mêmes propriétés pourraient améliorer temporairement l'hydratation de la barrière cutanée dans l'ichtyose, où la couche cornée est sèche et squameuse. Cette idée n'a pas été testée.

Il faut aussi souligner une limite importante : un effet émollient ou humectant ne serait que symptomatique. Il n'agirait pas sur les anomalies génétiques sous-jacentes de la différenciation des kératinocytes et du métabolisme lipidique (par exemple TGM1, ALOXE3, ALOX12B, NIPAL4 et ABCA12). Le lien repose uniquement sur un score élevé du modèle, sans soutien clinique ni bibliographique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Toutes les AMM ci-dessous sont annulées. Les textes d'indication approuvée ne sont pas renseignés dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 69449741 | NUTRIVISC 5 POUR CENT, collyre en solution (Laboratoires Alcon) | Collyre en solution | Annulée |
| 68403812 | DULCILARMES 1,5 %, collyre en solution en récipient unidose (Horus Pharma) | Collyre en solution | Annulée |
| 64035359 | NUTRIVISC 5 POUR CENT (20 mg/0,4 ml), collyre en récipient unidose (Laboratoires Alcon) | Collyre en solution | Annulée |
| 65367581 | UNIFLUID 6 mg/0,4 ml, collyre en récipient unidose (Théa) | Collyre en solution | Annulée |
| 63734630 | DULCILARMES 1,5 %, collyre en solution (Horus Pharma) | Collyre en solution | Annulée |

Deux autres AMM annulées (FLUIDABAK 1,5 % et REFRESH) figurent également dans les données compilées.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie du graphe, et non texte de notice) : épilepsie, maladie hépatique, maladie de la vésicule biliaire, insuffisance respiratoire, dissociation auriculo-ventriculaire, bloc auriculo-ventriculaire, bloc cardiaque. Ces éléments sont à interpréter avec prudence, car ils ne proviennent pas de la notice et semblent peu cohérents avec un usage en collyre.

Aucune interaction médicamenteuse n'a été retrouvée. Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau de preuve L5), sans essai clinique ni publication. Le mécanisme proposé est symptomatique et ne traite pas la cause génétique de la maladie. De plus, toutes les AMM françaises sont annulées et les données de sécurité officielles manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) sur le site de l'ANSM, étape bloquante pour le dépistage de sécurité
- Obtenir les données sur le mécanisme d'action via DrugBank
- Rechercher des études précliniques ou des données de formulation topique cutanée pour la povidone dans l'ichtyose
- Évaluer la compatibilité des voies d'administration, les formes actuelles étant uniquement ophtalmiques
- Clarifier le statut réglementaire, aucune AMM n'étant valide actuellement
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

