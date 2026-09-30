---
layout: default
title: Brolucizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 63
evidence_level: L5
indication_count: 4
---

# Brolucizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

# Brolucizumab : De la DMLA néovasculaire au Trouble de la phosphorylation oxydative mitochondriale (ADN nucléaire)

## Résumé en Une Phrase

Brolucizumab est un fragment d'anticorps anti-VEGF-A administré par voie intravitréenne. Les données d'AMM fournies ne précisent pas son indication, mais il est connu pour le traitement de la DMLA néovasculaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble de la phosphorylation oxydative mitochondriale dû à des anomalies de l'ADN nucléaire**, avec un score très élevé.
Cette prédiction repose uniquement sur le modèle : **0 essai clinique** et **0 publication** la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM (la DMLA néovasculaire est l'indication connue du produit, hors données fournies) |
| Nouvelle Indication Prédite | Trouble de la phosphorylation oxydative mitochondriale dû à des anomalies de l'ADN nucléaire |
| Score de Prédiction TxGNN | 99,67 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Concrètement, elle ne l'est pas, ou très peu. Le brolucizumab est un fragment d'anticorps à chaîne unique (scFv) qui neutralise le VEGF-A. Il est administré par injection dans l'œil. Les données détaillées sur le mécanisme d'action issues de DrugBank ne sont pas disponibles, mais cette description suffit pour l'analyse.

Les maladies de la phosphorylation oxydative liées à l'ADN nucléaire proviennent de défauts d'assemblage ou de fonctionnement de la chaîne respiratoire mitochondriale. Elles ne relèvent pas de la signalisation du VEGF. Aucun lien mécanistique crédible n'a donc été identifié entre l'action anti-VEGF et cette maladie.

Le score TxGNN de 0,997 est une prédiction issue d'un graphe de connaissances. Aucune donnée biologique, aucun essai et aucune publication ne l'appuie. Il ne doit pas être interprété comme un signal d'efficacité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65607585 | BEOVU 120 mg/ml, solution injectable en seringue préremplie (NOVARTIS EUROPHARM, Irlande) | Solution injectable | Non renseignée dans les données fournies |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données disponibles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est de niveau L5 : aucun essai, aucune publication et aucun lien mécanistique plausible. La voie intravitréenne et la faible exposition systémique rendent l'atteinte d'une cible dans une maladie mitochondriale peu vraisemblable.
- Les autres prédictions du modèle sont aussi à mettre en attente (Hold), pour les mêmes raisons :
  - Varices œsophagiennes avec et sans saignement (score 99,12 %) : le lien avec l'angiogenèse est faible et indirect, et le blocage systémique du VEGF pose un risque hémorragique. Les deux entrées ont un score identique et semblent être des doublons.
  - Insuffisance pancréatique exocrine (99,07 %) : aucun lien mécanistique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM, actuellement manquantes et bloquantes pour le criblage de sécurité
- L'indication approuvée du produit, absente du texte d'AMM fourni
- Les données de mécanisme d'action de DrugBank
- Un lien biologique plausible entre le blocage du VEGF-A et la pathologie visée, avant tout travail préclinique

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

