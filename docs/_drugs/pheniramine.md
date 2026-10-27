---
layout: default
title: Pheniramine
parent: Preuves modérées (L3-L4)
nav_order: 594
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Pheniramine : nouvelle indication prédite, Urticaire allergique (niveau de preuve L4). Indication d'origine : Rhinite allergique, rhinite vasomotrice, pharyngite, rhume, urticaire…"
monitor_inn: "pheniramine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis"]
---

# Pheniramine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **3** 
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

## Phéniramine : Du traitement des rhinites et états grippaux à l'urticaire allergique
{: .text-alpha }

## Résumé en Une Phrase

La phéniramine est un antihistaminique H1 de première génération, initialement utilisé dans la rhinite allergique, la rhinite vasomotrice, la pharyngite, le rhume et l'urticaire.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**urticaire allergique**, mais **aucun essai clinique** n'est enregistré et les **4 publications** retrouvées (3 rapports de cas et 1 revue ancienne) ne fournissent pas de preuve d'efficacité.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Rhinite allergique, rhinite vasomotrice, pharyngite, rhume, urticaire, angioedème (d'après le graphe de connaissances ; aucun texte d'indication AMM disponible) |
| Nouvelle Indication Prédite | Urticaire allergique |
| Score de Prédiction TxGNN | 99,67 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 9 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la phéniramine appartient à la classe des antihistaminiques H1 de première génération. Son action repose sur le blocage des récepteurs H1 de l'histamine, avec des effets anticholinergiques et sédatifs habituels dans cette classe.

L'urticaire et l'angioedème figurent déjà parmi les indications d'origine du médicament. L'urticaire allergique est donc mécanistiquement cohérente avec le blocage H1 connu. Le score TxGNN élevé reflète surtout ce chevauchement avec des indications existantes, et non un véritable signal de repositionnement.

Deux autres prédictions vont dans le même sens : « maladie de la cavité nasale » (99,28 %), catégorie très large qui recouvre les rhinites déjà connues, et « laryngopharyngite aiguë » (99,25 %), plausible pour un soulagement symptomatique (rhinorrhée, écoulement postérieur). Ces deux prédictions ne reposent sur aucun essai ni publication.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [40324831](https://pubmed.ncbi.nlm.nih.gov/40324831/) | 2025 | Rapport de cas | Indian J Pharmacol | Perte de connaissance après administration concomitante de phéniramine IV et d'hydrocortisone lors d'une réaction anaphylactique : événement indésirable grave |
| [40125237](https://pubmed.ncbi.nlm.nih.gov/40125237/) | 2025 | Rapport de cas | Cureus | Réaction d'hypersensibilité immédiate à la phéniramine dans un syndrome d'hypersensibilité médicamenteuse multiple |
| [16854350](https://pubmed.ncbi.nlm.nih.gov/16854350/) | 2006 | Rapport de cas | Allergol Immunopathol | Œdème facial menaçant le pronostic vital après ingestion d'une chenille processionnaire du pin, mimant une réaction allergique |
| [2859711](https://pubmed.ncbi.nlm.nih.gov/2859711/) | 1985 | Revue | Z Hautkr | Revue mondiale de l'astémizole, comparé à des antihistaminiques classiques dont la phéniramine ; ne concerne pas directement la phéniramine |

Ces publications ne documentent pas l'efficacité de la phéniramine dans l'urticaire allergique : trois portent sur des événements indésirables ou des cas atypiques.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60759678 | Paracétamol/Vitamine C/Phéniramine Viatris Conseil sans sucre 500 mg/200 mg/25 mg | Poudre pour solution buvable | Non précisée (AMM annulée) |
| 69329731 | Fervex Adultes | Granulés pour solution buvable | Non précisée (AMM annulée) |
| 69738404 | Fervex Adultes Framboise | Granulés pour solution buvable | Non précisée (AMM annulée) |
| 66238760 | Rhinofébral sans sucre | Poudre pour solution buvable | Non précisée (AMM annulée) |
| 61697350 | Humexlib État Grippal sans sucre | Poudre pour solution buvable | Non précisée (AMM annulée) |

Au total, 9 AMM sont recensées et toutes sont annulées. Il s'agit exclusivement d'associations fixes (paracétamol, vitamine C, phéniramine) destinées à l'état grippal. Aucune AMM en monothérapie n'est valide.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : hypertension, insuffisance hépatique et maladies hépatiques, maladie rénale, épilepsie, insomnie, BPCO, bronchite, ulcère gastrique ou peptique, gastrite, pancréatite, maladies de la vésicule biliaire, thrombocytopénie, hyperglycémie, diabète et acidocétose diabétique, hypothyroïdie et myxœdème, maladie inflammatoire de l'intestin, troubles psychotiques et autres troubles mentaux, hypertrophie bénigne de la prostate, dermatite herpétiforme.
- **Interactions médicamenteuses** : aucune interaction retrouvée dans la base consultée.
- **Alerte issue de la littérature** : des cas de réaction d'hypersensibilité à la phéniramine et d'événement indésirable grave (perte de connaissance après administration intraveineuse) sont rapportés.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être récupérées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est essentiellement redondante avec des indications existantes (urticaire, angioedème) et n'est étayée par aucun essai clinique ni publication d'efficacité (niveau L4 ; L5 pour les deux autres prédictions).
- Toutes les AMM françaises sont annulées et les données de sécurité officielles sont manquantes, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (analyse du PDF).
- Obtenir les données de mécanisme d'action (par exemple via DrugBank).
- Rechercher des essais contrôlés ou des revues systématiques de la phéniramine dans l'urticaire allergique.
- Clarifier les raisons de l'annulation des AMM et vérifier la disponibilité de formes (notamment injectables ou orales en monothérapie) compatibles avec l'usage visé.
- Évaluer si l'indication présente un intérêt réel au-delà des indications déjà connues.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

