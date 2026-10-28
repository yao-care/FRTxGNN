---
layout: default
title: Cholecalciferol
parent: Prédiction du modèle uniquement (L5)
nav_order: 166
evidence_level: L5
indication_count: 4
monitor_inn: "cholecalciferol"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "renal osteodystrophy", "renal tubular acidosis"]
last_modified_at: 2026-10-23
description: "Cholecalciferol : nouvelle indication prédite, Dysplasie acromésomélique de type Campailla-Martinelli (niveau de preuve L5). Indication d'origine : Le texte d'indication n'est pas renseigné dans les …"
---

# Cholecalciferol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

## Cholécalciférol : Des usages liés à la vitamine D à la dysplasie acromésomélique de type Campailla-Martinelli
{: .text-alpha }

## Résumé en Une Phrase

Le cholécalciférol (vitamine D3) est commercialisé en France sous forme de compléments médicamenteux de vitamine D.
Le modèle TxGNN prédit qu'il pourrait être utile dans la **dysplasie acromésomélique de type Campailla-Martinelli**, une maladie osseuse génétique rare. **Aucun essai clinique et aucune publication** ne soutiennent actuellement cette prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Le texte d'indication n'est pas renseigné dans les AMM compilées. Le graphe de connaissances enregistre des relations avec l'ostéoporose, le rachitisme, l'ostéomalacie et la carence en vitamine D. Il ne s'agit pas d'indications approuvées. |
| Nouvelle Indication Prédite | Dysplasie acromésomélique de type Campailla-Martinelli |
| Score de Prédiction TxGNN | 0,9978 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | Au moins 20 AMM (la liste peut être partielle) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Le cholécalciférol est un précurseur de la vitamine D active. Il est converti dans l'organisme en dérivés qui régulent l'absorption du calcium et du phosphore et la minéralisation osseuse.

La prédiction est issue du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre des maladies apparentées, et non une preuve biologique. Le score très élevé (0,9978) est une sortie de modèle, pas une preuve clinique.

La dysplasie acromésomélique est une maladie génétique rare du développement du squelette. Son origine génétique n'est pas corrigée par un apport en vitamine D. Les données compilées ne soutiennent aucun lien mécanistique propre à cette maladie, et cette prédiction reste donc spéculative.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement.

---

## Informations de Marché en France

Le cholécalciférol est commercialisé en France. Les données compilées recensent au moins 20 AMM de médicaments à base de cholécalciférol seul, et la liste peut être partielle. Le texte d'indication approuvée n'est pas renseigné dans ces données. Les 5 premières AMM sont présentées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 62028825 | CHOLECALCIFEROL EG 100 000 UI | Solution buvable en ampoule | EG LABO |
| 68992798 | KIPOS 100 000 UI | Capsule molle | SUBSTIPHARM |
| 67075736 | CHOLECALCIFEROL SUBSTIPHARM 80 000 UI | Solution buvable en ampoule | SUBSTIPHARM |
| 62176845 | CHOLECALCIFEROL EVOLUGEN 100 000 UI | Solution buvable en ampoule | EVOLUPHARM |
| 63312942 | CHOLECALCIFEROL ZENTIVA 100 000 UI | Solution buvable en ampoule | ZENTIVA FRANCE |

Les autres présentations comprennent des gouttes buvables (ZYMAD 10 000 UI/ml) et une solution injectable intramusculaire (VITAMINE D3 BON 200 000 U.I./1 ml).

---

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Relations de contre-indication dans le graphe de connaissances** (elles ne proviennent pas du texte de la notice) : hypercalcémie, néphrocalcinose, hyperparathyroïdie, sarcoïdose, maladie rénale, maladie hépatique, hypertension, diabète, fibrillation auriculaire, hyperoxalurie primaire, maladie de Wilson, hémochromatose, hyperlipidémie, cancer de la prostate et carcinome mammaire féminin, entre autres.
- **Interactions médicamenteuses** : 56 interactions sont recensées.
  - Interactions majeures : autres dérivés de la vitamine D (calcifédiol, calcitriol, dihydrotachystérol, doxercalciférol), avec un risque de surdosage et d'hypercalcémie.
  - Interactions modérées, notamment : barbituriques, carbamazépine, diurétiques thiazidiques (bendroflumethiazide, chlorothiazide, chlortalidone), digoxine et digitoxine, résines chélatrices (cholestyramine, colestipol, colesevelam).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique documenté avec cette maladie génétique rare.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données détaillées sur le mécanisme d'action.
- Une revue de la littérature ciblée sur la dysplasie acromésomélique, pour établir si un lien biologique existe.
- La notice de l'ANSM (mises en garde et contre-indications), indispensable avant toute évaluation de sécurité.
- Une réorientation possible vers d'autres prédictions mieux documentées pour ce médicament. L'ostéodystrophie rénale dispose par exemple d'un essai de phase 3 en population apparentée (statut inconnu, résultats non disponibles) et de plusieurs publications.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

