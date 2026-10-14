---
layout: default
title: Tiagabine
parent: Prédiction du modèle uniquement (L5)
nav_order: 758
evidence_level: L5
indication_count: 1
---

# Tiagabine
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

# Tiagabine : De l'Épilepsie Partielle à l'Épilepsie Visuelle

## Résumé en Une Phrase

Tiagabine est un antiépileptique inhibiteur de la recapture du GABA, initialement utilisé pour le traitement de l'épilepsie partielle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**épilepsie visuelle**, mais aucun essai clinique n'est enregistré à ce jour. Parmi les **16 publications** retrouvées, aucune n'évalue spécifiquement cette indication.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Épilepsie partielle |
| Nouvelle Indication Prédite | Épilepsie visuelle |
| Score de Prédiction TxGNN | 99,25 % |
| Niveau de Preuve | L5 (prédiction du modèle, sans étude directe sur cette indication) |
| Statut de Marché en France | AMM annulée uniquement (non commercialisé) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Selon la littérature retrouvée, la tiagabine bloque la recapture du GABA (transporteur GAT-1) par les neurones et les cellules gliales, ce qui renforce l'inhibition synaptique. Ce mécanisme est décrit comme spécifique parmi les antiépileptiques. Elle est efficace en traitement additionnel des crises partielles.

L'épilepsie visuelle (par exemple épilepsie du lobe occipital ou épilepsie photosensible) est une forme focale ou réflexe de crises. Un effet antiépileptique de type GABAergique est donc plausible, et le score élevé du modèle reflète probablement la proximité phénotypique avec l'épilepsie partielle. Il s'agit davantage d'une extension au sein d'une même famille de maladies que d'un véritable repositionnement.

Point de vigilance : la littérature signale des déficits du champ visuel avec les antiépileptiques GABAergiques (vigabatrine, tiagabine). C'est une considération importante pour une population dont la pathologie touche le système visuel.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune publication ne teste la tiagabine dans l'épilepsie visuelle. Les références ci-dessous apportent un contexte sur le mécanisme, l'efficacité générale et la sécurité visuelle.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Recommandation | Neurology | Mise à jour des recommandations AAN/AES sur les nouveaux antiépileptiques dans l'épilepsie nouvellement diagnostiquée |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Revue | Neuropharmacology | Mécanismes d'action des antiépileptiques actuellement utilisés |
| [12588906](https://pubmed.ncbi.nlm.nih.gov/12588906/) | 2003 | Revue | J Neurol Neurosurg Psychiatry | Vigabatrine, tiagabine et champs visuels (résumé non disponible) |
| [10530690](https://pubmed.ncbi.nlm.nih.gov/10530690/) | 1999 | Revue | Epilepsia | Tiagabine : inhibition de la recapture du GABA, efficace en traitement additionnel des crises partielles, sans effet notable sur le métabolisme hépatique des autres antiépileptiques |
| [9097364](https://pubmed.ncbi.nlm.nih.gov/9097364/) | 1997 | Revue | Semin Pediatr Neurol | Efficacité contre les crises partielles chez l'adulte et l'adolescent ; données pédiatriques préliminaires encourageantes |
| [15094857](https://pubmed.ncbi.nlm.nih.gov/15094857/) | 1998 | Revue | Drugs Today (Barc) | Mécanisme spécifique ; pas de tératogénicité, cancérogénicité ni mutagénicité notables chez l'animal |
| [8039477](https://pubmed.ncbi.nlm.nih.gov/8039477/) | 1994 | Revue | Epilepsia | Inhibiteur spécifique de la recapture du GABA ; effets anticonvulsivants dans les modèles animaux et dans un essai contrôlé contre placebo (crises partielles complexes) |
| [17560495](https://pubmed.ncbi.nlm.nih.gov/17560495/) | 2007 | Revue | Pediatr Neurol | Antiépileptiques et fonction visuelle : troubles du champ visuel et de la vision des couleurs |
| [11520315](https://pubmed.ncbi.nlm.nih.gov/11520315/) | 2001 | Revue | Epilepsia | Mécanismes GABAergiques dans l'épilepsie |
| [26210064](https://pubmed.ncbi.nlm.nih.gov/26210064/) | 2015 | Revue | Epilepsy Behav | États de mal épileptiques d'origine médicamenteuse ; certains antiépileptiques GABAergiques peuvent aggraver les crises |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61089729 | GABITRIL 15 mg, comprimé pelliculé (TEVA PHARMA, Pays-Bas) | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (et non du texte de la notice)** : trouble anxieux, trouble névrotique, trouble dysthymique, maladie hépatique, maladie de la vésicule biliaire.
- **Interactions médicamenteuses** : 97 interactions recensées. Celles de niveau modéré incluent aprépitant, morphine (y compris liposomale), dronabinol, nabilone, métoclopramide et opium. Plusieurs autres (pantoprazole, doxycycline, metformine, oméprazole, lansoprazole, prednisone, chlorure de potassium, ranitidine, ondansétron, sucralfate, rosiglitazone, simvastatine, tégasérod) ont un niveau non précisé.
- **Sécurité visuelle** : la littérature rapporte des anomalies du champ visuel avec les antiépileptiques GABAergiques. Elles sont à considérer avec une attention particulière dans cette population.

Les mises en garde et contre-indications de la notice officielle n'ont pas pu être consultées. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (L5). Aucun essai clinique ni étude spécifique à l'épilepsie visuelle n'a été identifié. L'AMM française est annulée, et les données de sécurité de la notice sont manquantes, ce qui bloque l'évaluation de sécurité. Le risque de troubles du champ visuel pose en outre une question particulière pour cette population.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice de l'ANSM (mises en garde et contre-indications)
- Obtenir des données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Rechercher des études cliniques ou observationnelles de la tiagabine dans l'épilepsie occipitale, photosensible ou réflexe
- Évaluer le risque d'atteinte du champ visuel et prévoir une surveillance ophtalmologique si une étude est envisagée
- Clarifier la disponibilité du produit en France, l'AMM étant annulée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

