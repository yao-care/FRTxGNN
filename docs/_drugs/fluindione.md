---
layout: default
title: Fluindione
parent: Prédiction du modèle uniquement (L5)
nav_order: 134
evidence_level: L5
indication_count: 2
---

# Fluindione
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Fluindione : D'un Anticoagulant Antivitamine K (Indication Originale Non Précisée) à la Polyarthrite Rhumatoïde

## Résumé en Une Phrase

La fluindione est un anticoagulant antivitamine K (inhibition de VKORC1), commercialisé en France sous le nom PREVISCAN. Les données fournies ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **polyarthrite rhumatoïde**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **1 publication** (non pertinente pour cette indication) sont disponibles.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données ANSM |
| Nouvelle Indication Prédite | Polyarthrite rhumatoïde |
| Score de Prédiction TxGNN | 99,34 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

La fluindione est un antagoniste de la vitamine K : elle inhibe VKORC1 et réduit la synthèse hépatique des facteurs de coagulation dépendants de la vitamine K. Les données détaillées sur son mécanisme d'action et son indication d'origine ne figurent pas dans le dossier.

Aucun lien mécanistique établi ne relie l'antagonisme de la vitamine K à la physiopathologie de la polyarthrite rhumatoïde, maladie auto-immune inflammatoire des articulations. Le score élevé de TxGNN (0,993) est une prédiction issue du graphe de connaissances. Il ne constitue pas une preuve spécifique au médicament, et la plausibilité biologique reste à démontrer.

La seule publication retrouvée porte sur la calciphylaxie. Les antivitamines K étant un facteur de risque reconnu de calciphylaxie, elle relève au mieux d'un signal de sécurité, pas d'un argument d'efficacité dans la polyarthrite rhumatoïde.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38169875](https://pubmed.ncbi.nlm.nih.gov/38169875/) | 2023 | Série de cas | Clinical Nephrology. Case Studies | Deux cas atypiques de calciphylaxie avec atteinte ischémique oculaire, sans manifestations cutanées. Aucun lien avec l'efficacité dans la polyarthrite rhumatoïde ; signal de sécurité éventuel |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68133651 | PREVISCAN 20 mg, comprimé quadrisécable (MERCK SANTE) | Comprimé quadrisécable | Non précisée dans les données |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Les données de sécurité de l'ANSM (mises en garde, contre-indications, interactions) ne sont pas disponibles. Seul un signal indirect ressort de la littérature récupérée : les antivitamines K sont un facteur de risque de calciphylaxie.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique, sans mécanisme plausible et sans littérature pertinente.
- Les données de sécurité de la notice ANSM manquent, et le risque hémorragique d'un anticoagulant est un frein majeur à tout usage hors indication.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications, indication approuvée), ce qui bloque le criblage de sécurité
- Compléter les données sur le mécanisme d'action (DrugBank)
- Mener une recherche bibliographique ciblée « antivitamine K / warfarine et polyarthrite rhumatoïde »
- Évaluer un rationnel biologique reliant la voie de la vitamine K à l'inflammation articulaire avant tout travail préclinique

*Note : une seconde prédiction (migraine, score 99,23 %) présente le même niveau de preuve L5 et la même décision Hold. Sa littérature porte sur la génétique de l'épilepsie et de la migraine, sans rapport avec la fluindione.*

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

