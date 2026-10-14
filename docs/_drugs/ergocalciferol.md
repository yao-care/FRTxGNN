---
layout: default
title: Ergocalciferol
parent: Prédiction du modèle uniquement (L5)
nav_order: 294
evidence_level: L5
indication_count: 10
---

# Ergocalciferol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Ergocalciferol : De l'ostéoporose et des carences en vitamine D à l'hypoparathyroïdie isolée familiale (sécrétion de PTH altérée)

## Résumé en Une Phrase

L'ergocalciférol (vitamine D2) est utilisé à l'origine pour traiter les carences en vitamine D et les maladies osseuses et minérales associées (ostéoporose, rachitisme, ostéomalacie, hypoparathyroïdie).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypoparathyroïdie isolée familiale par altération de la sécrétion de PTH**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction précise : elle repose uniquement sur le modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Ostéoporose, ostéoporose post-ménopausique, carence en vitamine D, rachitisme, ostéomalacie, hypoparathyroïdie (texte d'indication des AMM non disponible) |
| Nouvelle Indication Prédite | Hypoparathyroïdie isolée familiale par altération de la sécrétion de PTH |
| Score de Prédiction TxGNN | 99,85 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 7 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'ergocalciférol est une forme native de la vitamine D : elle est convertie dans le foie en 25-hydroxyvitamine D, puis dans le rein en forme active (1,25-dihydroxyvitamine D), qui favorise l'absorption intestinale du calcium et du phosphore.

L'hypoparathyroïdie figure déjà parmi les indications d'origine du médicament, ce qui rend le lien biologique plausible. Toutefois, dans les états de déficit en PTH, la conversion rénale de l'ergocalciférol en forme active (1-alpha-hydroxylation) dépend de la PTH. Les analogues déjà activés sont donc généralement préférés.

La prédiction n'est ainsi pas soutenue par des preuves directes pour cette forme familiale précise. Elle doit être considérée comme une hypothèse de travail.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 7 AMM identifiées sont toutes annulées ; aucune n'est actuellement valide. Le texte de l'indication approuvée n'est pas renseigné dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 69719090 | STEROGYL 15 "H" 600 000 UI/1,5 ml (DESMA PHARMA) | Solution injectable | Annulée |
| 62457493 | STEROGYL 2 000 000 UI/100 ml (DESMA PHARMA) | Solution buvable en gouttes | Annulée |
| 69443489 | STEROGYL 15 "A" 600 000 UI/1,5 ml (DESMA PHARMA) | Solution buvable | Annulée |
| 64639110 | VITALIPIDE ADULTES (FRESENIUS KABI FRANCE) | Émulsion injectable pour perfusion | Annulée |
| 64023481 | VITALIPIDE ENFANTS (FRESENIUS KABI FRANCE) | Émulsion injectable pour perfusion | Annulée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de notice) : hypercalcémie, néphrocalcinose, hyperparathyroïdie, sarcoïdose, maladie rénale, maladie hépatique, hypertension, diabète, fibrillation auriculaire, troubles du métabolisme du phosphore, hyperoxalurie primaire, hémochromatose, maladie de Wilson, hyperlipidémie, cancer de la prostate et carcinome mammaire féminin, entre autres.
- **Interactions médicamenteuses** (55 interactions recensées) :
  - *Majeures* : cholécalciférol, calcifédiol, calcitriol, doxercalciférol (risque d'effet additif de la vitamine D et d'hypercalcémie).
  - *Modérées* : diurétiques thiazidiques (hydrochlorothiazide, chlorothiazide, chlorthalidone), digoxine, barbituriques (amobarbital, butalbital), carbamazépine, rifabutine, résines chélatrices (cholestyramine, colesevelam, colestipol), sévélamer, oxyde de magnésium, formes topiques de calcipotriol et de calcitriol.
  - *Mineure* : cimétidine.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de securite complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication spécifique. Le mécanisme est en outre contesté, car la conversion en forme active dépend de la PTH, alors que celle-ci est déficiente dans cette maladie. Par ailleurs, toutes les AMM françaises sont annulées et les données de sécurité de la notice sont absentes (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice auprès de l'ANSM (lacune bloquante pour le criblage de sécurité).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Réaliser une revue ciblée de la littérature sur la vitamine D native dans l'hypoparathyroïdie familiale, et la comparer aux analogues activés (calcitriol, alfacalcidol).
- Clarifier la disponibilité réelle d'une formulation commercialisée en France, puisque toutes les AMM sont annulées.

---

### Note sur les autres indications prédites

Les autres prédictions du modèle ne sont pas non plus étayées par des preuves solides :

| Rang | Indication prédite | Niveau de preuve | Remarque |
|---|---|---|---|
| 7 | Ostéodystrophie rénale | L3 | Un essai de phase 4 (NCT01799317, statut inconnu, 60 patients) et des études comparant l'ergocalciférol au calcitriol ; la piste la plus étayée. |
| 8 | Rachitisme hypophosphatémique | L3 | Chevauche une indication d'origine ; pas un signal de repositionnement nouveau. |
| 6 | Hypophosphatémie | L4 | Preuves indirectes (cas cliniques). |
| 10 | Rachitisme vitamino-dépendant | L4 | Revues et cas anciens ; non recommandé en première ligne. |
| 3 | Acidose tubulaire rénale | L4 | Deux cas cliniques, aucun ne teste l'ergocalciférol. |
| 9 | Syndrome des buveurs de lait et d'alcalins | L5 | Probablement nocif (risque d'hypercalcémie). |
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

