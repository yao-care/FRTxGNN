---
layout: default
title: Dihydroergotamine
parent: Prédiction du modèle uniquement (L5)
nav_order: 244
evidence_level: L5
indication_count: 1
---

# Dihydroergotamine
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

# Dihydroergotamine : De la migraine à la migraine avec aura du tronc cérébral

## Résumé en Une Phrase

La dihydroergotamine (DHE) est utilisée à l'origine dans le traitement de la migraine (avec ou sans aura) et de l'algie vasculaire de la face.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **migraine avec aura du tronc cérébral**,
mais **aucun essai clinique** n'est enregistré pour cette indication précise ; la littérature disponible (**20 publications**) concerne surtout la migraine en général.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Migraine (avec ou sans aura), algie vasculaire de la face, hémicrânie paroxystique, hémicrânie continue (indication AMM non renseignée dans les données) |
| Nouvelle Indication Prédite | Migraine avec aura du tronc cérébral |
| Score de Prédiction TxGNN | 99,37 % |
| Niveau de Preuve | L5 (prédiction du modèle, aucune étude clinique directe ; le dossier source indique L4) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances pharmacologiques générales, la DHE est un agoniste des récepteurs 5-HT1B/1D, avec une activité additionnelle sur d'autres récepteurs sérotoninergiques, adrénergiques et dopaminergiques. Elle provoque une vasoconstriction crânienne et inhibe la libération de CGRP et d'autres neuropeptides par les terminaisons du nerf trijumeau.

La migraine avec aura du tronc cérébral est un sous-type de migraine avec aura. Or la migraine, avec ou sans aura, figure déjà parmi les indications d'origine du médicament. Le score élevé du modèle reflète très probablement cette proximité dans l'ontologie des maladies, plutôt qu'une preuve indépendante.

Une réserve importante s'impose : les agents vasoconstricteurs ont été historiquement évités dans certaines formes de migraine à aura du tronc cérébral ou hémiplégique, en raison d'un risque ischémique théorique. Une publication de 2010 (PMID 20533960) rappelle d'ailleurs que la DHE est classiquement contre-indiquée dans la migraine hémiplégique et la migraine de type basilaire. Le mécanisme ne soutient donc pas un usage sans réserve.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Les publications ci-dessous portent sur la DHE dans la migraine en général ; aucune ne teste spécifiquement la migraine avec aura du tronc cérébral, hormis celle de 2010 sur les symptômes de la fosse postérieure. Les études citées sont majoritairement des revues.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [20533960](https://pubmed.ncbi.nlm.nih.gov/20533960/) | 2010 | Revue | Headache | Usage de la DHE dans la migraine avec symptômes de la fosse postérieure ; contre-indication classique dans la migraine hémiplégique et de type basilaire |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Revue | Headache | Évaluation par l'American Headache Society des preuves des traitements de la crise migraineuse chez l'adulte |
| [22211870](https://pubmed.ncbi.nlm.nih.gov/22211870/) | 2012 | Revue | Headache | Traitement de secours de la migraine aiguë : triptans, DHE et magnésium |
| [39373843](https://pubmed.ncbi.nlm.nih.gov/39373843/) | 2024 | Étude de phase 3 ouverte | CNS Drugs | Sécurité et tolérance à 12 mois de STS101 (poudre nasale de DHE) dans la migraine aiguë |
| [41186275](https://pubmed.ncbi.nlm.nih.gov/41186275/) | 2026 | Étude ouverte | Headache | Satisfaction des participants avec STS101 (étude ASCEND) |
| [42217235](https://pubmed.ncbi.nlm.nih.gov/42217235/) | 2026 | Revue | Expert Rev Neurother | STS101 comme nouvelle option pour la migraine aiguë avec ou sans aura |
| [8262792](https://pubmed.ncbi.nlm.nih.gov/8262792/) | 1993 | Étude ouverte | Headache | Efficacité et sécurité de la DHE (D.H.E. 45) en consultation, 311 patients migraineux |
| [9100396](https://pubmed.ncbi.nlm.nih.gov/9100396/) | 1997 | Série rétrospective | Headache | DHE intraveineuse continue dans 171 céphalées réfractaires |
| [19708964](https://pubmed.ncbi.nlm.nih.gov/19708964/) | 2009 | Recommandations | Eur J Neurol | Recommandations de l'EFNS sur le traitement médicamenteux de la migraine |
| [27837002](https://pubmed.ncbi.nlm.nih.gov/27837002/) | 2016 | Étude clinique | Neurology | Sécurité de la dompéridone contre les nausées liées à la perfusion de DHE |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62455371 | DIERGOSPRAY 4 mg/ml, solution pour pulvérisation nasale (AMDIPHARM) | Solution pour pulvérisation | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications (associations médicament–maladie du graphe de connaissances, hors texte de la notice)** : hypertension artérielle, insuffisance hépatique, porphyries (porphyrie héréditaire et troubles du métabolisme des porphyrines), maladie coronarienne, angor de Prinzmetal, artériopathie périphérique, claudication intermittente.
- **Interactions Médicamenteuses** : 117 interactions recensées. Parmi les interactions majeures figurent l'isométheptène, l'épinéphrine (y compris formes ophtalmique et topique), l'éphédrine (y compris nasale), la lorcasérine, la dexfenfluramine, la fenfluramine et la clarithromycine. Parmi les interactions modérées : doxycycline, tétracycline, aprépitant, dexaméthasone, cimétidine, clotrimazole, miconazole, éluxadoline, phénylbutyrate de glycérol et métréleptine.
- **Point d'attention propre à l'indication** : risque ischémique théorique des vasoconstricteurs dans la migraine avec aura du tronc cérébral.

Les mises en garde et contre-indications de la notice ANSM ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose essentiellement sur la proximité avec l'indication d'origine (migraine) ; aucun essai clinique ne cible la migraine avec aura du tronc cérébral. La DHE est de plus classiquement contre-indiquée dans les formes basilaire et hémiplégique, et l'unique AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications de la notice ANSM (blocage pour le criblage de sécurité)
- Données détaillées sur le mécanisme d'action (par ex. via DrugBank)
- Évaluation spécifique du risque ischémique dans la migraine avec aura du tronc cérébral, avec revue des cas publiés
- Données cliniques (cas, séries ou essais) dans cette sous-population
- Clarification du statut réglementaire en France (AMM annulée) et de la disponibilité de formes administrables
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

