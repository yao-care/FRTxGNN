---
layout: default
title: Calcitriol
parent: Prédiction du modèle uniquement (L5)
nav_order: 131
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Calcitriol : nouvelle indication prédite, Carence en vitamine D (entrée obsolète) (niveau de preuve L5). Indication d'origine : Hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore…"
monitor_inn: "CALCITRIOL"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hereditary hypophosphatemic rickets"]
---

# Calcitriol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Calcitriol : Des troubles du métabolisme phosphocalcique à la carence en vitamine D (entrée obsolète)

## Résumé en Une Phrase

Le calcitriol est la forme active de la vitamine D. Il est classiquement associé à des troubles du métabolisme calcique et phosphoré, comme l'hypoparathyroïdie, l'hypophosphatémie et l'ostéodystrophie rénale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **carence en vitamine D** (entrée de maladie désormais obsolète dans l'ontologie utilisée).
Cette prédiction repose uniquement sur le modèle : **0 essai clinique** et **0 publication** la soutiennent actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore, hypophosphatémie, hypoparathyroïdie, ostéodystrophie rénale (d'après le graphe de connaissances, le texte d'indication des AMM françaises n'étant pas renseigné) |
| Nouvelle Indication Prédite | Carence en vitamine D (entrée obsolète) |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM abrogées |
| Nombre d'AMM | 2 (toutes deux abrogées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le calcitriol est la forme active de la vitamine D. Son rôle dans la régulation du calcium et du phosphore est établi, et il est utilisé dans des maladies du métabolisme phosphocalcique. Mécanistiquement, il pourrait donc être applicable à une situation de carence en vitamine D.

Sur le plan conceptuel, remplacer une vitamine D déficitaire par sa forme active est cohérent. Le score très élevé du modèle reflète probablement la proximité, dans le graphe de connaissances, entre cette entrée et les indications existantes liées à la vitamine D. Il ne constitue pas une preuve clinique.

Deux réserves importantes s'imposent. D'abord, l'entrée de maladie est obsolète, ce qui limite l'interprétation de la prédiction. Ensuite, le traitement substitutif d'une carence en vitamine D se fait habituellement avec la vitamine D native (cholécalciférol ou ergocalciférol), et non avec le calcitriol.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|------|
| 61847953 | ROCALTROL 0,25 microgramme, capsule molle | Capsule molle (voie orale) | Abrogée |
| 62597239 | SILKIS 3 microgrammes/g, pommade | Pommade | Abrogée |

Le texte des indications approuvées n'est pas disponible pour ces deux AMM. Aucune AMM n'est actuellement valide en France pour le calcitriol seul ou en association.

## Considérations de Sécurité

- **Maladies pour lesquelles le calcitriol est signalé comme contre-indiqué** (d'après le graphe de connaissances, et non d'après le texte d'une notice) : maladie rénale, pyo-uretère, sarcoïdose, hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore, susceptibilité à la lithiase rénale liée à SLC26A1, lithiase rénale, néphropathie urique aiguë, hyperphosphatémie, hypervitaminose, artériosclérose oblitérante.
- **Interactions médicamenteuses** : 100 interactions sont recensées, dont 20 consultées pour ce rapport.
  - Interactions majeures : cholécalciférol, calcifédiol, burosumab (cumul d'effets vitaminiques D et risque d'hypercalcémie ou d'hyperphosphatémie).
  - Interactions modérées : diurétiques thiazidiques (hydrochlorothiazide, bendrofluméthiazide, benzthiazide, chlorothiazide, chlortalidone), anticonvulsivants et barbituriques (fosphénytoïne, carbamazépine, amobarbital, butalbital, butabarbital), chélateurs des acides biliaires (cholestyramine, colesevelam, colestipol), hydroxyde d'aluminium, calcipotriol topique, digitoxine et digoxine.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication. L'entrée de maladie est obsolète, et la substitution dans la carence en vitamine D relève habituellement de la vitamine D native. Aucune AMM n'est valide en France actuellement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Faire correspondre l'entrée obsolète à une entité de maladie actuelle, afin de redéfinir précisément l'indication visée.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Récupérer et analyser la notice officielle de l'ANSM (mises en garde et contre-indications), indispensable pour l'évaluation de sécurité.
- Réaliser une recherche ciblée de littérature et d'essais pour l'indication reformulée.

**Autres indications prédites, à titre d'information :**
- **Rachitisme hypophosphatémique héréditaire** (score TxGNN 99,28 %) : c'est la piste la mieux documentée. Les données compilées lui attribuent un niveau L2 et la recommandation « Proceed with Guardrails ».
  - Essais : [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) (phase 1 précoce, terminé, 16 participants, calcitriol en monothérapie dans l'hypophosphatémie liée à l'X) et [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) (phase 4, statut inconnu, 100 participants, fortes versus faibles doses de vitamine D active avec phosphate neutre).
  - Aucun essai de phase 3 terminé n'a été identifié. Une surveillance de l'hypercalciurie, de la néphrocalcinose et de l'hyperparathyroïdie est nécessaire. Le burosumab est une alternative.
- **Hypoparathyroïdie familiale isolée** (99,81 %) : rationnel mécanistique solide, déduit de l'indication d'origine, mais sans preuve directe (L5).
- **Acidose tubulaire rénale** (99,93 %) : littérature composée surtout de cas cliniques et d'études physiologiques (L4), le calcitriol agissant sur les complications osseuses plutôt que sur l'acidose.
- **Dysplasie acromésomélique de type Campailla-Martinelli, conodysplasie craniofaciale et syndrome de Dahlberg-Borer-Newcomer** : aucun lien mécanistique établi ni preuve spécifique (L5).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

