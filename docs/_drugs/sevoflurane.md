---
layout: default
title: Sevoflurane
parent: Prédiction du modèle uniquement (L5)
nav_order: 702
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sevoflurane : nouvelle indication prédite, Angor de Prinzmetal (niveau de preuve L5). Indication d'origine : Non renseignée dans l'AMM (anesthésie générale par inhalation d'après…"
monitor_inn: "sevoflurane"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "fibromyalgia", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "migraine disorder", "inclusion body myositis"]
---

# Sevoflurane
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Sévoflurane : De l'anesthésie générale à l'angor de Prinzmetal
{: .text-alpha }

## Résumé en Une Phrase

Le sévoflurane est un anesthésique halogéné administré par inhalation. Il est utilisé en anesthésie générale, mais aucun texte d'indication n'est renseigné dans l'AMM française recensée.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**angor de Prinzmetal**, mais **aucun essai clinique** ni **aucune publication** ne soutient cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans l'AMM (anesthésie générale par inhalation d'après la nature du produit) |
| Nouvelle Indication Prédite | Angor de Prinzmetal |
| Score de Prédiction TxGNN | 99,78 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulée (AMM non valide) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le sévoflurane est un anesthésique volatil, dont l'effet repose notamment sur la modulation de canaux ioniques, en particulier les récepteurs GABA-A.

Le sévoflurane exerce un effet vasodilatateur sur le muscle lisse vasculaire, ce qui pourrait, en théorie, être lié au vasospasme coronarien à l'origine de l'angor de Prinzmetal. Ce lien reste toutefois **spéculatif** : aucune donnée fournie ne l'établit, et le score élevé du modèle ne constitue pas une preuve.

Par ailleurs, un anesthésique volatil est peu adapté à la prise en charge chronique d'une maladie telle que l'angor de Prinzmetal.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour l'angor de Prinzmetal.

À titre d'information, pour d'autres indications prédites, seuls des articles indirects (gestion anesthésique, études périopératoires) ont été identifiés. Ils ne démontrent aucun bénéfice thérapeutique : fibromyalgie (1 cas clinique), tendinite (9 publications d'anesthésie périopératoire), migraine (1 série rétrospective d'IRM pédiatrique) et myosite à inclusions (1 cas clinique).

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 67329056 | SEVOFLURANE BAXTER 1 ml/ml, liquide pour inhalation par vapeur | Liquide pour inhalation par vapeur | Non renseignée | Annulée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie de PrimeKG, et non texte de notice) : épilepsie, maladie rénale, pyo-uretère, maladie hépatique, maladie de la vésicule biliaire, troubles hypotensifs, hyperthermie maligne de l'anesthésie, hyperthermie maligne d'effort, pseudotumeur cérébrale, hypertension intracrânienne, dystrophie musculaire de Duchenne, dystrophie musculaire (dont Becker) et protéinurie.
- **Interactions médicamenteuses** : 146 interactions recensées. Parmi celles analysées, les interactions de niveau **majeur** concernent :
  - l'épinéphrine
  - le dolasétron
  - le cisapride

  Des interactions de niveau modéré figurent également (famotidine, morphine, clarithromycine, lévofloxacine, ondansétron, palonosétron, exénatide, laxatifs, etc.) ainsi qu'une interaction mineure (métronidazole).

Les mises en garde et contre-indications issues de la notice ANSM n'ont pas pu être récupérées. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle, sans essai clinique ni publication directe, et sans mécanisme établi ; l'AMM française est annulée.
- Un anesthésique volatil est impraticable pour un traitement chronique, et plusieurs contre-indications issues du graphe (dont l'hypotension) sont préoccupantes dans un contexte cardiovasculaire.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), élément bloquant pour le criblage de sécurité
- Obtenir les données sur le mécanisme d'action (via DrugBank)
- Études précliniques ou de mécanisme sur le vasospasme coronarien
- Évaluer la compatibilité de la voie d'administration avec l'indication visée
- Clarifier le statut réglementaire (AMM annulée) et l'indication d'origine
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

