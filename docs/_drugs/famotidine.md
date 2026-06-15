---
layout: default
title: Famotidine
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Famotidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Famotidine : De l'Ulcère Peptique au Reflux Duodéno-gastrique

## Résumé en Une Phrase

La famotidine est un antagoniste des récepteurs H2 de l'histamine, reconnu mondialement pour le traitement des maladies acido-dépendantes (ulcère gastroduodénal, reflux gastro-œsophagien), bien qu'elle ne dispose d'aucune AMM enregistrée en France dans cette base de données.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **Reflux Duodéno-gastrique**,
avec **0 essai clinique** et **2 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Non enregistrée en France (usage mondial établi : ulcère gastroduodénal, RGO) |
| Nouvelle Indication Prédite | Reflux Duodéno-gastrique |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations connues, la famotidine appartient à la classe des antagonistes des récepteurs H2 de l'histamine. Elle agit en bloquant sélectivement les récepteurs H2 sur les cellules pariétales gastriques, ce qui diminue la production d'AMPc intracellulaire et réduit ainsi la sécrétion acide gastrique — basale comme stimulée. Son efficacité dans la maladie ulcéro-peptique est soutenue par un corpus clinique abondant (voir indications 3 et 8 du pipeline TxGNN).

Dans le contexte du reflux duodéno-gastrique, la famotidine pourrait théoriquement atténuer les dommages muqueux causés par la composante acide du contenu refluant. En abaissant le pH gastrique, elle réduit l'agression chimique sur la muqueuse exposée aux sécrétions duodénales à la fois acides et biliaires.

Cependant, cette prédiction comporte une limite mécanistique importante : le reflux duodéno-gastrique implique principalement des sels biliaires et des enzymes pancréatiques — composantes non acides —, sur lesquelles la famotidine n'exerce aucune action directe. Le lien mécanistique relève donc d'une inférence raisonnée (réduction de la co-agression acide) plutôt que d'un ciblage pharmacologique direct, ce qui explique le niveau de preuve L4 malgré un score algorithmique élevé.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [12532466](https://pubmed.ncbi.nlm.nih.gov/12532466/) | 2003 | Observationnelle Prospective | World Journal of Gastroenterology | Évaluation prospective de l'effet de la famotidine sur le reflux gastro-œsophagien (GER) et duodéno-gastro-œsophagien (DGER) chez des patients en soins intensifs ; exploration des facteurs associés au reflux |
| [16259441](https://pubmed.ncbi.nlm.nih.gov/16259441/) | 2004 | Revue Clinique | Experimental & Clinical Gastroenterology | Efficacité de la famotidine 20 mg deux fois par jour aux stades précoces de la maladie de reflux gastroduodénal (grades 0 et 1 sur l'échelle de Savary-Miller modifiée), évaluée par critères cliniques et endoscopiques |

---

## Informations de Marché en France

La famotidine ne dispose d'aucune Autorisation de Mise sur le Marché (AMM) dans la base réglementaire consultée pour la France. Le médicament est néanmoins largement disponible sous des appellations commerciales reconnues (ex. Pepcid®, Famotidine générique) dans de nombreux pays (États-Unis, Japon, Royaume-Uni, etc.), où il est approuvé pour l'ulcère gastroduodénal, le RGO et les états d'hypersécrétion acide.

---

## Considérations de Sécurité

Veuillez consulter la notice officielle pour les informations de sécurité (mises en garde, contre-indications, interactions médicamenteuses).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le score TxGNN de 99,99 % reflète une pertinence algorithmique élevée, mais le reflux duodéno-gastrique est principalement médié par des composantes biliaires et enzymatiques non acides sur lesquelles la famotidine n'a pas d'action pharmacologique directe. L'absence totale d'essais cliniques dédiés à cette indication et la disponibilité de seulement 2 publications de niveau L4 (dont aucun ECR) ne justifient pas une progression clinique sans investigations complémentaires préalables.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération des données de mécanisme d'action (MOA) complètes via DrugBank (DB00927) pour affiner l'analyse de pertinence mécanistique
- Données de sécurité officielles (contre-indications, avertissements principaux, interactions médicamenteuses) issues de la notice ANSM/EMA ou de la fiche DrugBank
- Études précliniques ou mécanistiques explorant spécifiquement l'effet de la suppression acide sur la muqueuse soumise au reflux biliaire
- Évaluation comparative avec des agents mécanistiquement plus adaptés au reflux duodéno-gastrique pur (agents cytoprotecteurs comme le sucralfate, pro-cinétiques, acide ursodésoxycholique)
- Vérification du statut réglementaire AMM en France via le site de l'ANSM pour confirmer ou infirmer l'absence de commercialisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

