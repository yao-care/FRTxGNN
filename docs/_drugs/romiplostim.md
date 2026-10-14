---
layout: default
title: Romiplostim
parent: Preuves modérées (L3-L4)
nav_order: 678
evidence_level: L4
indication_count: 10
---

# Romiplostim
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
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

# Romiplostim : Du Purpura Thrombopénique Auto-immun au Trouble de Libération Plaquettaire Primaire

## Résumé en Une Phrase

Romiplostim est un agoniste du récepteur de la thrombopoïétine (MPL), initialement utilisé pour le traitement du purpura thrombopénique auto-immun (PTI) et de l'anémie aplasique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble de libération plaquettaire primaire**, mais cette prédiction ne repose actuellement que sur **0 essai clinique** et **1 publication** de nature mécanistique indirecte.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Purpura thrombopénique auto-immun, anémie aplasique (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Trouble de libération plaquettaire primaire (primary release disorder of platelets) |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. D'après les connaissances pharmacologiques, romiplostim est un agoniste du récepteur de la thrombopoïétine (MPL) : il stimule la prolifération des mégacaryocytes et augmente la production de plaquettes. Son efficacité dans le PTI chronique est établie.

La prédiction du modèle repose sur la proximité, dans le graphe de connaissances, entre les pathologies plaquettaires. Cependant, le mécanisme est ici peu convaincant : un trouble de libération plaquettaire est un défaut **fonctionnel** (sécrétion des granules), et non un déficit numérique. Augmenter le nombre de plaquettes ne corrigerait vraisemblablement pas ce défaut.

La seule publication disponible (PMID 25682608) porte sur l'inhibition, par des auto-anticorps, de la formation des proplaquettes dans le PTI. Elle soutient le mécanisme du PTI, et non celui de la nouvelle indication prédite.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Étude fondamentale/mécanistique | Haematologica | Dans le PTI, les auto-anticorps antiplaquettaires inhibent in vitro la formation des proplaquettes par les mégacaryocytes et altèrent la production plaquettaire. Lien indirect avec l'indication prédite. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64313253 | NPLATE 250 microgrammes, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Non renseignée (AMM annulée) |
| 66384249 | NPLATE 125 microgrammes, poudre pour solution injectable | Poudre pour solution injectable | Non renseignée (AMM annulée) |
| 68638461 | NPLATE 500 microgrammes, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Interactions médicamenteuses** :
  - **Carfilzomib** : interaction de niveau **majeur** (source : DDInter).
  - Cible pharmacologique : récepteur de la thrombopoïétine (MPL), ce qui correspond à son mécanisme d'agoniste et non à une interaction cliniquement évaluée.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un score élevé du modèle, mais le niveau de preuve est faible (L4) : aucun essai clinique, une seule étude mécanistique indirecte. Le défaut est fonctionnel, donc l'augmentation du nombre de plaquettes est peu susceptible d'être bénéfique. En outre, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action et sa pertinence pour un défaut fonctionnel plaquettaire.
- Notice de l'ANSM (mises en garde et contre-indications), indispensable avant toute évaluation de sécurité.
- Données précliniques ou cliniques spécifiques au trouble de libération plaquettaire.
- Clarification de la situation réglementaire (AMM annulées) et de la disponibilité du produit en France.

**Note complémentaire :** parmi les autres indications prédites, la thrombopénie alloimmune fœto-néonatale (niveau L4, « question de recherche »), les thrombopénies constitutionnelles et les macrothrombopénies autosomiques dominantes sont mécanistiquement plus plausibles, car il s'agit de déficits quantitatifs en plaquettes. Les preuves restent toutefois indirectes (principalement issues du PTI) ou inexistantes, et la sécurité pendant la grossesse reste à établir.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

