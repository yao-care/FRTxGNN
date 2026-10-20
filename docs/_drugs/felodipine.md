---
layout: default
title: Felodipine
parent: Prédiction du modèle uniquement (L5)
nav_order: 319
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Felodipine : nouvelle indication prédite, Angor de Prinzmetal (niveau de preuve L5). Indication d'origine : Hypertension artérielle (le texte d'indication des AMM n'est pas rens…"
monitor_inn: "felodipine"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease"]
---

# Felodipine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Félodipine : De l'Hypertension à l'Angor de Prinzmetal

## Résumé en Une Phrase

La félodipine est un inhibiteur calcique de type dihydropyridine, initialement utilisé pour traiter l'hypertension artérielle.
Le modèle TxGNN la prédit comme potentiellement efficace pour l'**angor de Prinzmetal** (angor vasospastique), avec **0 essai clinique enregistré** mais **7 publications** (dont plusieurs études cliniques anciennes et petites) soutenant cette direction.

Remarque : le premier résultat du modèle est l'hypertension pulmonaire d'origine multifactorielle peu claire. Cette indication ne repose que sur la prédiction du modèle (niveau L5). L'indication de l'angor de Prinzmetal est retenue ici dans le titre, car c'est la mieux documentée parmi les prédictions.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Angor de Prinzmetal |
| Score de Prédiction TxGNN | 99,07 % |
| Niveau de Preuve | L2 (les études sont petites, anciennes, et non de phase 3 confirmée) |
| Statut de Marché en France | Toutes les AMM sont annulées (aucun produit commercialisé) |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances pharmacologiques générales, la félodipine est un inhibiteur des canaux calciques de type L, de la classe des dihydropyridines. Elle relâche le muscle lisse vasculaire et réduit ainsi les résistances périphériques, ce qui explique son effet antihypertenseur.

L'angor de Prinzmetal est causé par un spasme des artères coronaires. Le même mécanisme de relaxation du muscle lisse vasculaire s'applique, et les inhibiteurs calciques sont une classe thérapeutique établie pour cette maladie. Plusieurs études cliniques de 1989 à 1995 ont testé directement la félodipine dans l'angor variant.

La question ouverte n'est donc pas l'intérêt de la classe, mais le bénéfice propre à la félodipine par rapport aux autres inhibiteurs calciques. Les études disponibles sont de petite taille et anciennes.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [7744087](https://pubmed.ncbi.nlm.nih.gov/7744087/) | 1995 | ECR (double aveugle, croisé, 43 patients) | Eur Heart J | Félodipine ER 10 mg et nifédipine SR améliorent la durée d'effort vs placebo dans l'angor stable d'effort (indication voisine, non spécifique à Prinzmetal) |
| [1746458](https://pubmed.ncbi.nlm.nih.gov/1746458/) | 1991 | Essai clinique comparatif | Am J Cardiol | Félodipine 1 prise/jour vs nifédipine 4 prises/jour chez 30 patients avec angor de Prinzmetal, évaluation par Holter de 24 h |
| [8013514](https://pubmed.ncbi.nlm.nih.gov/8013514/) | 1994 | Essai clinique (provocation à l'ergonovine) | Eur Heart J | Félodipine à libération prolongée 20 mg/jour évaluée pour prévenir l'ischémie induite par l'ergonovine chez 14 patients |
| [2909138](https://pubmed.ncbi.nlm.nih.gov/2909138/) | 1989 | Étude clinique | Am J Cardiol | Effet de la félodipine sur les crises ischémiques induites par l'hyperventilation dans l'angor variant (résumé non disponible) |
| [7728649](https://pubmed.ncbi.nlm.nih.gov/7728649/) | 1995 | Revue | Can J Cardiol | Les inhibiteurs calciques sont le traitement de première intention de l'angor de Prinzmetal, avec un focus sur la félodipine |
| [14689111](https://pubmed.ncbi.nlm.nih.gov/14689111/) | 2003 | Revue | Herz | Revue du traitement différencié par les inhibiteurs calciques |
| [15222138](https://pubmed.ncbi.nlm.nih.gov/15222138/) | 2004 | Cas clinique | Orvosi Hetilap | Angor de Prinzmetal induit par la nicergoline (lien tangentiel avec la félodipine) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67139288 | FELODIPINE ZENTIVA L.P. 5 mg | Comprimé pelliculé à libération prolongée | Non renseignée (AMM annulée) |
| 69149683 | FLODIL L.P. 5 mg | Comprimé enrobé à libération prolongée | Non renseignée (AMM annulée) |
| 69451322 | FELODIPINE SANDOZ L.P. 5 mg | Comprimé pelliculé à libération prolongée | Non renseignée (AMM annulée) |
| 61950444 | LOGIMAX 5 mg/47,5 mg | Comprimé pelliculé à libération prolongée | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : maladie rénale, maladie hépatique, maladie de la vésicule biliaire, angiœdème (dont héréditaire et acquis), neutropénie, agranulocytose, sténose aortique, hypotension, cardiomyopathie hypertrophique, infarctus du myocarde, coronaropathie et athérosclérose, obstruction de l'artère rénale, hémoglobinopathie, maladies du tissu conjonctif, des os et du cartilage. Ces éléments sont indicatifs et doivent être vérifiés avec la notice officielle. Notamment, la présence de la coronaropathie et de l'infarctus du myocarde dans cette liste mérite une attention particulière pour l'indication envisagée.
- **Interactions médicamenteuses** : 246 interactions sont recensées. Une interaction de niveau majeur concerne la **dolasétron**. Les interactions de niveau modéré incluent notamment : corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide), bupropion, aprépitant, morphine, acide acétylsalicylique, cimétidine, clarithromycine, inhibiteurs du SGLT2 (canagliflozine, dapagliflozine, empagliflozine), sels de calcium, sulfate de magnésium, dronabinol et nabilone.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L2 : les études sur l'angor de Prinzmetal sont petites, anciennes (1989-1995), sans essai de phase 3 confirmé ni essai enregistré. Toutes les AMM françaises sont annulées, et les données de sécurité issues de la notice manquent (lacune bloquante pour le dépistage de sécurité).
- Les autres indications prédites (hypertension pulmonaire, atteintes rénales hypertensives malignes, syndrome de Braddock, cœur pulmonaire chronique) reposent sur la seule prédiction du modèle ou sur des preuves indirectes ou précliniques (L4-L5), et ne justifient pas d'avancer.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Lire les textes complets des études sur l'angor de Prinzmetal (tailles d'échantillon, critères de jugement) et comparer la félodipine aux autres inhibiteurs calciques
- Évaluer la disponibilité pratique du produit, les AMM étant toutes annulées
- Évaluer le risque lié à la coronaropathie et à l'infarctus du myocarde signalés dans le graphe de connaissances
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

