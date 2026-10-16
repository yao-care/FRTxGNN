---
layout: default
title: Codeine
parent: Preuves modérées (L3-L4)
nav_order: 195
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-14
description: "Codeine : nouvelle indication prédite, Maladie de la cavité nasale (niveau de preuve L4). Indication d'origine : Rhinite allergique, rhinite vasomotrice, pharyngite, rhume…"
monitor_inn: "codeine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "trigeminal autonomic cephalalgia", "allergic urticaria"]
---

# Codeine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **4** 
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

# Codéine : Des affections des voies respiratoires supérieures et des céphalées à la maladie de la cavité nasale

## Résumé en Une Phrase

La codéine est un opioïde antalgique et antitussif, initialement utilisé dans la rhinite, la pharyngite, le rhume et les céphalées.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie de la cavité nasale**, mais **aucun essai clinique** et **une seule publication** (un rapport de cas sans valeur thérapeutique) soutiennent cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Rhinite allergique, rhinite vasomotrice, pharyngite, rhume, rhinopharyngite, céphalées (le texte d'indication des AMM n'est pas renseigné ; indications issues du graphe de connaissances) |
| Nouvelle Indication Prédite | Maladie de la cavité nasale |
| Score de Prédiction TxGNN | 99,93 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Il est toutefois connu que la codéine est une prodrogue agoniste des récepteurs opioïdes mu, transformée en morphine par le CYP2D6. Elle est utilisée pour soulager la toux et la douleur.

Le score très élevé (99,93 %) reflète probablement la proximité, dans le réseau de connaissances, avec les indications d'origine (rhinite, rhinopharyngite, rhume). Ces indications sont symptomatiques (toux, congestion) et non modificatrices de la maladie.

La seule publication retrouvée décrit une rhinolithiase causée par un corps étranger contenant de la codéine et de l'opium (un « opiome »). Il s'agit d'une forme pharmaceutique logée dans la cavité nasale, et non d'un effet thérapeutique. **Aucun mécanisme de repositionnement plausible n'est étayé.**

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Rapport de cas | Ear, Nose & Throat Journal | Rhinolithe inhabituel formé autour d'un corps étranger (mélange durci de codéine et d'opium) chez un homme de 21 ans ; extraction sous anesthésie locale. Aucun effet thérapeutique rapporté. |

## Informations de Marché en France

Toutes les AMM sont annulées ; le texte d'indication approuvée n'est pas disponible. Les 5 premières sont listées :

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
- La prédiction repose uniquement sur le modèle, sans essai clinique, et la seule publication est un rapport de cas non thérapeutique. De plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action et sur les mises en garde et contre-indications officielles issues de la notice
- Preuves cliniques directes d'un bénéfice dans une maladie de la cavité nasale
- Clarification du statut réglementaire actuel des produits à base de codéine

---

### Note sur les autres prédictions du modèle

Les trois autres prédictions n'appuient pas non plus un repositionnement :
- **Laryngopharyngite aiguë** (99,92 %, L5) : aucun essai ni publication ; elle recoupe l'indication d'origine de pharyngite. Hold.
- **Céphalée autonomique trigéminale** (99,43 %, L4) : les deux publications ne montrent aucun bénéfice de la codéine. Les opioïdes sont généralement déconseillés dans ces céphalées (efficacité limitée, céphalée par abus médicamenteux, dépendance). Hold.
- **Urticaire allergique** (99,37 %, L4) : la littérature montre que la codéine **provoque** l'urticaire en libérant l'histamine des mastocytes, et sert de témoin positif dans les tests cutanés. Son usage dans cette indication est mécanistiquement contre-indiqué. Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

