---
layout: default
title: Anagrelide
parent: Prédiction du modèle uniquement (L5)
nav_order: 65
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Anagrelide : nouvelle indication prédite, Thrombocytose réactive (niveau de preuve L5). Indication d'origine : Thrombocythémie…"
monitor_inn: "anagrelide"
predicted_indications: ["reactive thrombocytosis", "inverse Klippel-Trenaunay syndrome"]
---

# Anagrelide
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

## Anagrélide : De la thrombocythémie à la thrombocytose réactive
{: .text-alpha }

## Résumé en Une Phrase

L'anagrélide est un médicament qui réduit le nombre de plaquettes, initialement utilisé pour traiter la thrombocythémie et la thrombocytose familiale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **thrombocytose réactive**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** n'est enregistré et les **10 publications** identifiées portent surtout sur la thrombocythémie essentielle (forme clonale), non sur la thrombocytose réactive.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Thrombocythémie, thrombocytose familiale (texte d'indication de l'AMM non disponible) |
| Nouvelle Indication Prédite | Thrombocytose réactive |
| Score de Prédiction TxGNN | 99,83 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement, aucun essai clinique ni étude directe sur cette indication) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances publiées, l'anagrélide diminue le nombre de plaquettes en inhibant la maturation des mégacaryocytes, un effet largement documenté dans la thrombocythémie essentielle, un trouble clonal.

La thrombocytose réactive (secondaire) a une origine différente : elle est provoquée par des causes externes telles qu'une inflammation, une carence en fer ou une splénectomie. Elle se traite généralement en prenant en charge la cause sous-jacente, et le risque thrombotique y est habituellement faible. Le mécanisme de baisse des plaquettes est donc biologiquement plausible, mais l'intérêt clinique d'un agent cytoréducteur dans un contexte non clonal est faible.

Le score TxGNN élevé (0,998) reflète très probablement la proximité de cette maladie avec l'indication approuvée (thrombocythémie) dans l'ontologie, plutôt qu'une preuve indépendante. Il doit être interprété avec prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune de ces publications n'évalue directement l'anagrélide dans la thrombocytose réactive ; elles servent surtout de contexte (diagnostic différentiel, thrombocythémie essentielle).

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Revue | Expert Rev Anticancer Ther | Mise à jour sur les mécanismes d'action et le potentiel thérapeutique de l'anagrélide ; la thrombocytose réactive ne nécessite pas de traitement, la forme clonale oui |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Revue | Leuk Lymphoma | Revue critique de l'anagrélide dans la thrombocythémie essentielle ; la thrombocytose réactive est souvent sans conséquence |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Revue | Med J Aust | Prise en charge de la thrombocythémie essentielle ; diagnostic par exclusion des autres syndromes myéloprolifératifs et de la thrombocytose réactive |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Revue | Am J Med Sci | Spectre clinique de la thrombocytose et de la thrombocythémie ; régulation de la production plaquettaire |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Revue | Leuk Res | Rôle de la thrombocytaphérèse dans l'hyperthrombocytose des néoplasies myéloprolifératives |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Revue | Rinsho Ketsueki | Diagnostic et traitement de la thrombocythémie essentielle (busulfan, hydroxyurée, interféron alpha, anagrélide) |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Cohorte rétrospective | Pediatr Blood Cancer | Analyse de 12 cas pédiatriques : thrombocythémie essentielle versus réactive |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Rapport de cas | Eur J Case Rep Intern Med | Infarctus du myocarde aigu chez un patient atteint de thrombocythémie essentielle traité par anagrélide |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Rapport de cas | Srp Arh Celok Lek | Thrombocythémie essentielle associée à une spondylarthrite ankylosante, traitée par anagrélide, DMARD et étanercept |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Rapport de cas | Medicine | Réimplantation de deux doigts chez un patient présentant une thrombocytose après splénectomie |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64599534 | XAGRID 0,5 mg, gélule (Takeda Pharmaceuticals International, Irlande) | Gélule | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Non déterminée (les données sur le mécanisme d'action ne sont pas disponibles) |
| Risque de Myélosuppression | Non documenté dans les données compilées ; l'anagrélide agit sur la lignée plaquettaire |
| Classification d'Émétogénicité | Non documentée |
| Éléments de Surveillance | Numération formule sanguine (plaquettes), fonction hépatique et rénale, surveillance cardiovasculaire |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : insuffisance hépatique, maladie hépatique, maladie rénale, maladie de la vésicule biliaire, thrombocytopénie, trouble de la coagulation, maladie cardiaque, maladie cardiovasculaire, anémie (dont anémie macrocytaire), pneumopathie interstitielle, pneumonie à éosinophiles, éosinophilie pulmonaire, insuffisance cardiaque à haut débit, pyo-uretère.
- **Interactions médicamenteuses** : 376 interactions répertoriées. Parmi les principales, de niveau **majeur** : cisapride, clarithromycine, dolasétron, granisétron, lévofloxacine (risque probable lié à l'allongement de l'intervalle QT). De niveau **modéré** : acide acétylsalicylique, famotidine, cimétidine, aprépitant, alosétron, lopéramide, fenfluramine, ainsi que plusieurs laxatifs (bisacodyl, lactulose, lactitol, glycérine, huile de ricin, citrate et hydroxyde de magnésium).

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle, sans essai clinique ni étude directe ; le rationnel clinique d'un cytoréducteur dans la thrombocytose réactive, généralement bénigne et traitée par sa cause, est faible. Le profil de sécurité (nombreuses contre-indications cardiovasculaires dans le graphe, interactions majeures) et l'AMM française annulée renforcent cette prudence.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice officielle de l'ANSM (mises en garde et contre-indications), indispensable avant tout examen de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Études cliniques ou observationnelles évaluant l'anagrélide spécifiquement dans la thrombocytose réactive
- Justification clinique d'une population cible présentant un risque thrombotique significatif
- Éclaircissement du statut réglementaire en France (AMM annulée)

---

**Note sur la seconde prédiction (syndrome de Klippel-Trenaunay inverse)** : score TxGNN de 99,59 %, niveau de preuve L5, sans essai ni publication, et aucun lien mécanistique établi avec l'anagrélide. Décision : Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

