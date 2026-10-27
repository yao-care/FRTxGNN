---
layout: default
title: Phenylalanine
parent: Preuves modérées (L3-L4)
nav_order: 599
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-14
description: "Phenylalanine : nouvelle indication prédite, Cholangite sclérosante (niveau de preuve L4). Indication d'origine : Non renseignée dans les AMM (texte d'indication vide)"
monitor_inn: "phenylalanine"
predicted_indications: ["sclerosing cholangitis", "congenital prothrombin deficiency"]
---

# Phenylalanine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **2** 
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

## Phénylalanine : De l'usage nutritionnel à la Cholangite Sclérosante
{: .text-alpha }

## Résumé en Une Phrase

La phénylalanine est un acide aminé essentiel, présent dans plusieurs solutions de nutrition parentérale et orale commercialisées en France. Aucune indication d'origine n'est renseignée dans les données compiled for this report.
Le modèle TxGNN prédit qu'elle pourrait être utile pour la **cholangite sclérosante**, mais **aucun essai clinique** n'est enregistré et seules **3 publications indirectes** existent, aucune ne démontrant un effet thérapeutique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM (texte d'indication vide) |
| Nouvelle Indication Prédite | Cholangite sclérosante |
| Score de Prédiction TxGNN | 99,43 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. La phénylalanine est un acide aminé essentiel, constituant de nombreuses solutions nutritionnelles (perfusion, dialyse péritonéale, solution buvable). Son rôle physiologique est bien connu, mais aucun lien mécanistique avec la cholangite sclérosante n'est établi à partir des données disponibles.

Le seul élément de rapprochement est indirect : une étude observationnelle relie la concentration plasmatique de tyrosine (métabolite de la phénylalanine) à la fatigue dans la cirrhose biliaire primitive et la cholangite sclérosante primitive. Cela suggère une altération du métabolisme phénylalanine-tyrosine dans les maladies hépatiques cholestatiques, mais il s'agit d'une association avec un symptôme, non d'une preuve d'effet sur l'évolution de la maladie.

Le score TxGNN, très élevé, reflète une proximité dans le graphe de connaissances et non une justification biologique démontrée. Les variations des taux d'acides aminés pourraient simplement résulter de la maladie et non constituer une cible thérapeutique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Étude observationnelle (conception non confirmée) | BMC Gastroenterology | Relation entre la tyrosine plasmatique et la fatigue dans la cirrhose biliaire primitive et la cholangite sclérosante primitive |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohorte / métabolomique (autre maladie : cholangiocarcinome) | J Clin Exp Hepatol | Profil métabolomique sérique du cholangiocarcinome au Royaume-Uni, à la recherche de biomarqueurs précoces ; non pertinent pour un effet thérapeutique |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Méthodologie de dosage (recherche fondamentale) | J Gastroenterol Hepatol | Dosage radio-immunologique d'un peptide formylé (fMLP) et circulation entéro-hépatique ; ne concerne pas la phénylalanine comme médicament |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63363997 | REVITALOSE SANS SUCRE, solution buvable édulcorée au sorbitol | Solution buvable | Non renseignée (AMM annulée) |
| 61960303 | AMINOVEN 10 POUR CENT, solution pour perfusion | Solution pour perfusion | Non renseignée (AMM annulée) |
| 69667989 | AMINOVEN 5 POUR CENT, solution pour perfusion | Solution pour perfusion | Non renseignée (AMM annulée) |
| 62947013 | AMINOPLASMAL 25, solution pour perfusion | Solution pour perfusion | Non renseignée (AMM annulée) |
| 61786735 | AMINOMIX 500, solution pour perfusion | Solution pour perfusion | Non renseignée (AMM annulée) |

Au total, 20 AMM sont recensées, toutes annulées ; seules les 5 premières sont listées ici.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations du graphe, et non texte de notice) : maladie rénale (dont insuffisance rénale chronique et terminale), néphrolithiase, néphrocalcinose, hypercalcémie, sarcoïdose, maladies cardiovasculaires, fibrillation ventriculaire, intoxication digitalique, **phénylcétonurie** et troubles du métabolisme de la phénylalanine, ainsi que des troubles du métabolisme du phosphore.
- Aucune interaction médicamenteuse n'a été retrouvée dans les données.

Veuillez consulter la notice pour les informations de securité complémentaires (mises en garde et contre-indications officielles non disponibles).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L4 au mieux) : aucun essai clinique, littérature seulement indirecte, mécanisme inconnu, et toutes les AMM françaises sont annulées.
- La seconde indication prédite, le déficit congénital en prothrombine (score 99,26 %, niveau L5), ne dispose d'aucune preuve ni de mécanisme plausible et n'est pas non plus recommandée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (via DrugBank) pour évaluer un lien mécanistique réel
- Notice ANSM (mises en garde et contre-indications) pour permettre l'évaluation de sécurité
- Études précliniques ou observationnelles ciblées montrant un effet de la phénylalanine sur la cholangite sclérosante
- Clarification du statut réglementaire, toutes les AMM étant annulées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

