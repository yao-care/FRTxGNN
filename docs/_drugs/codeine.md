---
layout: default
title: Codeine
parent: Prédiction du modèle uniquement (L5)
nav_order: 195
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
monitor_inn: "codeine"
predicted_indications: ["nasal cavity disease", "trigeminal autonomic cephalalgia", "allergic urticaria"]
description: "Codeine : nouvelle indication prédite, Maladie de la cavité nasale (nasal cavity disease) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Codeine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Codeine: Maladie de la cavité nasale (nasal cavity disease)
{: .text-alpha }

## Résumé en Une Phrase

La codéine est un opioïde antalgique et antitussif, initialement utilisé dans la rhinite, la pharyngite, le rhume et les céphalées.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie de la cavité nasale**, mais **aucun essai clinique** et **une seule publication** (un rapport de cas sans valeur thérapeutique) soutiennent cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Maladie de la cavité nasale (nasal cavity disease) |
| Score de Prédiction TxGNN | 0.9993 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 19) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Il est toutefois connu que la codéine est une prodrogue agoniste des récepteurs opioïdes mu, transformée en morphine par le CYP2D6. Elle est utilisée pour soulager la toux et la douleur.

Le score très élevé (0,9993) reflète probablement la proximité, dans le réseau de connaissances, avec les indications d'origine (rhinite, rhinopharyngite, rhume). Ces indications sont symptomatiques (toux, congestion) et non modificatrices de la maladie.

La seule publication retrouvée décrit une rhinolithiase causée par un corps étranger contenant de la codéine et de l'opium (un « opiome »). Il s'agit d'une forme pharmaceutique logée dans la cavité nasale, et non d'un effet thérapeutique. **Aucun mécanisme de repositionnement plausible n'est étayé.**

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Rapport de cas | Ear, Nose & Throat Journal | Rhinolithe inhabituel formé autour d'un corps étranger (mélange durci de codéine et d'opium) chez un homme de 21 ans ; extraction sous anesthésie locale. Aucun effet thérapeutique rapporté. |

## Informations de Marché en France

19 AMM valides ; le texte d'indication approuvée n'est pas disponible. Les 5 premières sont listées :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60811833 | PADERYL 19,5 mg, comprimé enrobé | Comprimé enrobé | Non renseignée |
| 62582924 | PADERYL 0,1 POUR CENT, sirop | Sirop | Non renseignée |
| 69458587 | PARACETAMOL/CODEINE BIOGARAN 500 mg/30 mg | Comprimé | Non renseignée |
| 60206154 | PULMOSERUM, solution buvable | Solution buvable | Non renseignée |
| 66384797 | PARACETAMOL/CODEINE VIATRIS 500 mg/30 mg | Comprimé | Non renseignée |

## Considérations de Sécurité

- **Contre-indications (issues du graphe de connaissances, non du texte de la notice)** : hypertension, insuffisance hépatique, maladie hépatique, maladie rénale, épilepsie, insomnie, bronchopneumopathie chronique obstructive, troubles anxieux, porphyries, pancréatite, maladie de la vésicule biliaire, thrombocytopénie, hypothyroïdie, ulcère gastroduodénal, maladies inflammatoires de l'intestin, gastrite, troubles psychotiques et autres troubles mentaux, dermatite herpétiforme.
- **Interactions Médicamenteuses** : 449 interactions recensées. Parmi les principales, deux de niveau majeur : **alvimopan** et **bupropion**. Des interactions de niveau modéré existent notamment avec l'atropine, la cimétidine, la dexaméthasone, le lopéramide, le granisétron, le dolasétron, le dronabinol, l'éluxadoline, le glycopyrronium et l'hyoscyamine.

Veuillez consulter la notice pour les mises en garde officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle, sans essai clinique, et la seule publication est un rapport de cas non thérapeutique. Par ailleurs, le médicament est commercialisé en France (19 AMM valides).

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action et sur les mises en garde et contre-indications officielles issues de la notice
- Preuves cliniques directes d'un bénéfice dans une maladie de la cavité nasale
- Clarification du statut réglementaire actuel des produits à base de codéine

---

### Note sur les autres prédictions du modèle

Les trois autres prédictions n'appuient pas non plus un repositionnement :
- Hold.
- **Céphalée autonomique trigéminale** (0.9943, L4) : les deux publications ne montrent aucun bénéfice de la codéine. Les opioïdes sont généralement déconseillés dans ces céphalées (efficacité limitée, céphalée par abus médicamenteux, dépendance). Hold.
- **Urticaire allergique** (0.9937, L4) : la littérature montre que la codéine **provoque** l'urticaire en libérant l'histamine des mastocytes, et sert de témoin positif dans les tests cutanés. Son usage dans cette indication est mécanistiquement contre-indiqué. Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

