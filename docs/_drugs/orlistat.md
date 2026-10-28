---
layout: default
title: Orlistat
parent: Prédiction du modèle uniquement (L5)
nav_order: 561
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "ORLISTAT"
predicted_indications: ["hypervitaminosis"]
description: "Orlistat : nouvelle indication prédite, Hypervitaminose (hypervitaminosis) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Orlistat
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Orlistat: Hypervitaminose (hypervitaminosis)
{: .text-alpha }

## Résumé en Une Phrase

Orlistat est un inhibiteur des lipases gastrique et pancréatique, initialement utilisé pour le traitement de l'obésité (y compris l'obésité monogénique).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypervitaminose**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hypervitaminose (hypervitaminosis) |
| Score de Prédiction TxGNN | 0.9942 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action issues des bases curatées ne sont pas disponibles. Sur la base des informations connues, l'orlistat est un inhibiteur des lipases gastrique et pancréatique : il réduit d'environ 30 % l'absorption des graisses alimentaires, ce qui explique son usage dans l'obésité.

Les vitamines liposolubles (A, D, E, K) sont absorbées avec les graisses alimentaires. En théorie, en diminuant cette absorption, l'orlistat pourrait réduire les taux de ces vitamines en cas d'hypervitaminose due à un excès d'apport. Ce lien est plausible, mais **spéculatif**.

Cette propriété est aussi un effet indésirable connu de l'orlistat (carence en vitamines liposolubles). Toute utilisation dans cette optique exigerait donc une surveillance étroite. Le score élevé de TxGNN (0,9942) reste une prédiction du modèle, sans appui clinique ni bibliographique, et le mécanisme n'a pas pu être recoupé avec des données curatées.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 65715632 | XENICAL 120 mg, gélule | Gélule | Non renseignée | Active |
| 65734134 | ORLISTAT EG 120 mg, gélule | Gélule | Non renseignée | Active |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie, et non texte de la notice) : insuffisance hépatique, hyperoxalurie primaire, anorexie mentale, boulimie, carence vitaminique, cholestase (y compris cholestase intrahépatique récurrente bénigne et familiale), atteinte hépatique d'origine médicamenteuse.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les premières listées :
  - Modérées : abacavir, lamivudine, emtricitabine, atazanavir, acarbose, albiglutide, alogliptine, canagliflozine, metformine, chlorpropamide, amiodarone, cannabidiol, asparaginase (E. coli et Erwinia), calaspargase pegol, brentuximab vedotin, clofarabine.
  - Mineures : cholécalciférol, calcifédiol, calcitriol (vitamines D, particulièrement pertinentes ici).

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication. Le mécanisme proposé est spéculatif et recoupe un effet indésirable connu de l'orlistat (carence en vitamines liposolubles). De plus, le médicament est commercialisé en France, avec 2 AMM valides sur 2.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications), car cette lacune bloque l'étape de criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Mener une revue de la littérature et des registres d'essais sur l'orlistat et l'hypervitaminose
- Évaluer la pertinence clinique : type de vitamine concerné, alternatives existantes (arrêt de la supplémentation, traitements spécifiques) et rapport bénéfice/risque
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

