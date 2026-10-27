---
layout: default
title: Propranolol
parent: Prédiction du modèle uniquement (L5)
nav_order: 637
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Propranolol : nouvelle indication prédite, Myopathie distale de type Tateyama (niveau de preuve L5). Indication d'origine : Non renseignée dans les AMM françaises"
monitor_inn: "PROPRANOLOL"
predicted_indications: ["distal myopathy, Tateyama type", "congenital myopathy with excess of thin filaments", "chondroma", "cirrhotic cardiomyopathy"]
---

# Propranolol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Propranolol : De l'hypertension artérielle à la myopathie distale de type Tateyama
{: .text-alpha }

## Résumé en Une Phrase

Le propranolol est un bêtabloquant non sélectif, utilisé à l'origine pour traiter l'hypertension artérielle, les troubles du rythme et la cardiomyopathie hypertrophique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **myopathie distale de type Tateyama** (score de 99,40 %), mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction.
Les indications suivantes du classement disposent de peu de données : la **cardiomyopathie cirrhotique** (3 publications) et la **cardiomyopathie** en général (20 publications, surtout sur la cardiomyopathie hypertrophique, déjà une indication connue).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM françaises ; les indications issues du graphe de connaissances incluent l'hypertension, la fibrillation atriale et la cardiomyopathie hypertrophique |
| Nouvelle Indication Prédite | Myopathie distale de type Tateyama |
| Score de Prédiction TxGNN | 99,40 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le propranolol est un bêtabloquant non sélectif (non cardiosélectif), sans activité sympathomimétique intrinsèque, dont l'efficacité a été établie dans l'hypertension, les arythmies et la cardiomyopathie hypertrophique, par réduction de la fréquence cardiaque, de la contractilité et de la consommation d'oxygène du myocarde.

Pour la myopathie distale de type Tateyama, **aucun lien mécanistique n'est soutenu par les données compilées**. Cette maladie musculaire rare n'a pas de relation évidente avec le blocage bêta-adrénergique. Le score élevé du modèle reste donc une sortie algorithmique, sans étude de soutien. À noter aussi que le graphe de connaissances signale des maladies musculaires (myopathie, maladie du muscle squelettique) parmi les contre-indications du propranolol, ce qui appelle à la prudence.

Parmi les autres prédictions, deux présentent un lien plus plausible :
- **Cardiomyopathie cirrhotique** (score 99,12 %) : le propranolol est largement utilisé dans la cirrhose pour l'hypertension portale. Une publication de 2024 suggère qu'il pourrait corriger l'allongement de l'intervalle QT. D'autres travaux indiquent toutefois des effets cardiovasculaires atténués et une possible altération de la fonction circulatoire et rénale en cas d'ascite réfractaire. Le rapport bénéfice/risque est donc incertain.
- **Cardiomyopathie** (score 99,12 %) : les études concernent surtout la cardiomyopathie hypertrophique, déjà couverte par l'usage établi, donc l'apport pour de nouveaux sous-types est indirect.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la myopathie distale de type Tateyama.

À titre indicatif, voici les publications les plus pertinentes pour les autres indications prédites (la nature exacte des études n'est pas vérifiable à partir des seuls titres et résumés fournis) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38738176](https://pubmed.ncbi.nlm.nih.gov/38738176/) | 2024 | Étude clinique (type non précisé) | Front Pharmacol | Le propranolol pourrait corriger l'allongement de l'intervalle QT chez les patients cirrhotiques (cardiomyopathie cirrhotique) |
| [35763518](https://pubmed.ncbi.nlm.nih.gov/35763518/) | 2022 | Étude clinique ou revue | PLoS One | Effets cardiovasculaires atténués des bêtabloquants selon la gravité de la cirrhose, évalués par perfusion de propranolol |
| [32446716](https://pubmed.ncbi.nlm.nih.gov/32446716/) | 2020 | Étude clinique | J Hepatol | Les bêtabloquants non sélectifs altèrent l'homéostasie circulatoire et la fonction rénale en cas d'ascite réfractaire |
| [6686544](https://pubmed.ncbi.nlm.nih.gov/6686544/) | 1983 | Étude de physiologie clinique | Eur Heart J | Effets du propranolol et du vérapamil sur la rigidité diastolique dans la cardiomyopathie hypertrophique |
| [7191199](https://pubmed.ncbi.nlm.nih.gov/7191199/) | 1980 | Étude clinique | Am J Cardiol | Propranolol et arythmie dans la cardiomyopathie hypertrophique |
| [7200796](https://pubmed.ncbi.nlm.nih.gov/7200796/) | 1982 | Étude hémodynamique | Br Heart J | Effets hémodynamiques de la nifédipine et du propranolol, seuls ou combinés, dans la cardiomyopathie hypertrophique obstructive (12 patients) |
| [28431779](https://pubmed.ncbi.nlm.nih.gov/28431779/) | 2017 | Monographie | Profiles Drug Subst Excip Relat Methodol | Monographie du propranolol : usages, propriétés pharmacologiques |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65667550 | Propranolol Teva L.P. 80 mg (annulée) | Gélule à libération prolongée | Non renseignée |
| 66415335 | Propranolol EG 40 mg (annulée) | Comprimé | Non renseignée |
| 63077978 | Propranolol Teva L.P. 160 mg (annulée) | Gélule à libération prolongée | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : bronchite, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, pancréatite, diabète et acidocétose diabétique, lupus érythémateux systémique, myopathie et maladies musculaires, myasthénie, paralysie périodique familiale, goutte, hyperparathyroïdie, hypercalcémie, anurie, encéphalopathie hépatique, troubles anxieux, entre autres.
- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - Majeure : épinéphrine.
  - Modérées : corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), anticholinergiques (atropine, hyoscyamine, méthscopolamine), bupropion, morphine, lorcasérine, canagliflozine, chlorpropamide, cimétidine, sels de calcium.
  - Mineures : acide ascorbique, acide acétylsalicylique, oxyde de magnésium.

Les mises en garde et contre-indications issues de la notice officielle ne sont pas disponibles : veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la myopathie distale de type Tateyama repose uniquement sur le modèle (niveau L5), sans essai ni publication, sans lien mécanistique plausible, et avec des maladies musculaires signalées parmi les contre-indications du propranolol. Toutes les AMM françaises sont par ailleurs annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données de sécurité de la notice officielle (ANSM), actuellement bloquantes pour le dépistage de sécurité.
- Les données détaillées sur le mécanisme d'action (DrugBank).
- Une justification biologique reliant le blocage bêta-adrénergique à la myopathie distale de type Tateyama, ou des données précliniques.
- Pour la cardiomyopathie cirrhotique, qui est la piste la plus étayée (question de recherche, niveau L4), des études contrôlées précisant le rapport bénéfice/risque selon la gravité de la cirrhose.
- Une clarification du statut commercial en France, puisque seules des AMM annulées sont recensées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

