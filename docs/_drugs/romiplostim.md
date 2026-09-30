---
layout: default
title: Romiplostim
parent: Preuves modérées (L3-L4)
nav_order: 271
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

# Romiplostim : De la Thrombopénie Immunologique à un Trouble de la Libération Plaquettaire Primaire

## Résumé en Une Phrase

Romiplostim (Nplate) est un agoniste du récepteur de la thrombopoïétine (TPO), qui stimule la production de plaquettes. Les données de l'ANSM fournies ne précisent pas son indication d'origine, mais ce médicament est connu pour traiter la thrombopénie immunologique (PTI).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble primaire de la libération plaquettaire**.
Cette direction n'est soutenue que par **1 essai clinique observationnel** et **2 publications** (une revue et une étude in vitro), toutes indirectes.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM fournies (thrombopénie immunologique d'après les connaissances générales sur Nplate) |
| Nouvelle Indication Prédite | Trouble primaire de la libération plaquettaire (*primary release disorder of platelets*) |
| Score de Prédiction TxGNN | 99,9998 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, le romiplostim est un agoniste du récepteur de la TPO. Il stimule les mégacaryocytes de la moelle osseuse et augmente ainsi le nombre de plaquettes circulantes.

Le lien avec la nouvelle indication est faible. Un trouble de la libération (sécrétion) plaquettaire est un défaut **qualitatif** : les plaquettes sont présentes mais fonctionnent mal. Or le romiplostim agit sur la **quantité** de plaquettes. Augmenter leur nombre ne corrige pas a priori un défaut de sécrétion.

Le seul appui disponible est indirect et provient de la biologie de la PTI. La revue sur la mégacaryopoïèse décrit le rôle central de la TPO dans la production plaquettaire. L'étude in vitro montre que les autoanticorps de la PTI freinent la formation de proplaquettes. Aucune de ces sources ne concerne le trouble de libération plaquettaire lui-même. Le score TxGNN élevé reflète donc surtout une proximité dans le graphe de connaissances, pas une justification mécanistique démontrée.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03820960](https://clinicaltrials.gov/study/NCT03820960) | N/A (observationnelle) | Terminé | 10 039 | Facteurs de risque de thrombose dans la thrombopénie immunologique. Ce n'est pas un essai d'efficacité du romiplostim et il ne porte pas sur les troubles de libération plaquettaire. |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23594368](https://pubmed.ncbi.nlm.nih.gov/23594368/) | 2013 | Revue | British Journal of Haematology | Synthèse des avancées sur la mégacaryopoïèse et la thrombopoïèse, avec la TPO comme principal facteur de croissance de la lignée mégacaryocytaire |
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Préclinique / in vitro | Haematologica | Les autoanticorps antiplaquettes de patients atteints de PTI inhibent la formation de proplaquettes par les mégacaryocytes et altèrent la production plaquettaire in vitro |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64313253 | NPLATE 250 microgrammes | Poudre et solvant pour solution injectable | Non précisée dans les données fournies |
| 66384249 | NPLATE 125 microgrammes | Poudre pour solution injectable | Non précisée dans les données fournies |
| 68638461 | NPLATE 500 microgrammes | Poudre et solvant pour solution injectable | Non précisée dans les données fournies |

Le titulaire des trois AMM est AMGEN EUROPE.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L4. Le seul essai associé est observationnel et sans lien avec l'efficacité du romiplostim, et les deux publications sont indirectes.
- Le mécanisme (augmentation du nombre de plaquettes) ne correspond pas à un défaut qualitatif de libération plaquettaire. Le score TxGNN élevé ne suffit pas à compenser ce manque.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM, dont l'absence bloque toute évaluation de sécurité.
- Les données détaillées sur le mécanisme d'action (DrugBank).
- L'indication approuvée de chaque AMM, à extraire de la notice ANSM.
- Une justification mécanistique ou des données précliniques montrant qu'un agoniste du récepteur de la TPO peut avoir un effet dans les troubles de libération plaquettaire.
- Pour le même médicament, une autre prédiction (« trouble hémorragique de type plaquettaire », rang 8) dispose d'un essai de phase 3 randomisé (RECITE, NCT03362177), mais dans la thrombopénie induite par la chimiothérapie. Elle mérite une analyse séparée, sans être transposée à la présente indication.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

