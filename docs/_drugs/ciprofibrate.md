---
layout: default
title: Ciprofibrate
parent: Prédiction du modèle uniquement (L5)
nav_order: 172
evidence_level: L5
indication_count: 2
monitor_inn: "CIPROFIBRATE"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "fibroma of prostate"]
last_modified_at: 2026-10-23
description: "Ciprofibrate : nouvelle indication prédite, Déficience en protéine de transfert des esters de cholestérol (cholesterol-ester transfer protein deficiency) (niveau de preuve L5). Indication d'origine :…"
---

# Ciprofibrate
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Ciprofibrate: Déficience en protéine de transfert des esters de cholestérol (cholesterol-ester transfer protein deficiency)
{: .text-alpha }

## Résumé en Une Phrase

Le ciprofibrate est un fibrate, initialement utilisé pour traiter l'hypertriglycéridémie et les hyperlipidémies familiales combinées (relations enregistrées dans le graphe de connaissances).
Le modèle TxGNN prédit qu'il pourrait être utile pour la **déficience en protéine de transfert des esters de cholestérol (CETP)**,
mais cette direction ne repose que sur **1 publication préclinique** (modèle animal) et **aucun essai clinique**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Déficience en protéine de transfert des esters de cholestérol (cholesterol-ester transfer protein deficiency) |
| Score de Prédiction TxGNN | 0.9991 |
| Niveau de Preuve | L5 (aucune étude ne porte directement sur cette maladie) |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les informations pharmacologiques connues, le ciprofibrate est un agoniste du récepteur PPAR-alpha (PPARA) qui réduit les triglycérides et module le métabolisme des lipoprotéines.

La déficience en CETP se caractérise par un HDL-cholestérol très élevé et un remodelage anormal des lipoprotéines. Un lien plausible existe donc par le métabolisme lipidique. Toutefois, ce lien reste théorique : la seule publication disponible (2003) est une étude chez la souris déficiente en apolipoprotéine E, montrant que le ciprofibrate aggrave l'hypercholestérolémie, effet corrigé par la surexpression de SR-BI.

Cette preuve est indirecte et ne concerne ni la déficience en CETP, ni l'humain. Comme cette maladie se manifeste par un HDL-C élevé, il n'est pas non plus certain que réduire les lipides par un fibrate constitue un objectif clinique pertinent. Le score élevé de TxGNN reste une prédiction informatique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [14570884](https://pubmed.ncbi.nlm.nih.gov/14570884/) | 2003 | Préclinique (modèle animal, transfert de gène par adénovirus) | J Biol Chem | Chez la souris déficiente en apoE, le ciprofibrate aggrave l'hypercholestérolémie ; la surexpression de SR-BI inverse cet effet. Étude indirecte, sans lien démontré avec la déficience en CETP. |

## Informations de Marché en France

Le ciprofibrate est commercialisé en France. Les trois AMM sont des spécialités à substance unique, valides. Le texte d'indication approuvée n'est pas renseigné dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66475325 | LIPANOR 100 mg, gélule (Sanofi Winthrop Industrie) | Gélule | Non renseignée |
| 66866758 | CIPROFIBRATE BIOGARAN 100 mg, gélule | Gélule | Non renseignée |
| 62938313 | CIPROFIBRATE ARROW 100 mg, gélule (Arrow Génériques) | Gélule | Non renseignée |

## Considérations de Sécurité

**Interactions médicamenteuses :** la seule entrée disponible concerne la cible pharmacologique du ciprofibrate, le récepteur PPAR-alpha (PPARA), et non une interaction avec un autre médicament. Aucun niveau de gravité n'est précisé.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune étude clinique ni publication ne porte directement sur la déficience en CETP ; la seule référence est préclinique et indirecte. Le niveau de preuve est donc L5, et le score TxGNN seul ne suffit pas.
- Les informations de sécurité issues de la notice sont manquantes, ce qui bloque toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, indications approuvées)
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Établir si une réduction lipidique par fibrate est cliniquement pertinente dans la déficience en CETP
- Rechercher des études cliniques ou observationnelles chez des patients atteints de cette maladie

**Note sur la seconde prédiction (fibrome de la prostate, score 0,9971) :** aucun essai ni publication n'a été identifié (niveau L5), et aucun lien mécanistique crédible n'apparaît entre un agoniste PPAR-alpha et cette lésion bénigne. Il peut s'agir d'un artefact de correspondance d'ontologie ; une validation du terme est nécessaire avant toute investigation.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

