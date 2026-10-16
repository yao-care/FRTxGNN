---
layout: default
title: Minocycline
parent: Prédiction du modèle uniquement (L5)
nav_order: 502
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Minocycline : nouvelle indication prédite, Kératoconjonctivite épithéliale ponctuée (niveau de preuve L5). Indication d'origine : Infections bactériennes (infection urinaire, bronchite, acné…"
monitor_inn: "MINOCYCLINE"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis"]
---

# Minocycline
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Minocycline : Des Infections Bactériennes à la Kératoconjonctivite Épithéliale Ponctuée

## Résumé en Une Phrase

Minocycline est un antibiotique de la famille des tétracyclines, initialement utilisé pour traiter des infections bactériennes (infections urinaires, bronchite, acné, gonorrhée, parodontite, entre autres).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **kératoconjonctivite épithéliale ponctuée**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infections bactériennes (infection urinaire, bronchite, acné, gonorrhée, parodontite, etc.) d'après le graphe de connaissances ; le texte d'indication de l'AMM française n'est pas renseigné |
| Nouvelle Indication Prédite | Kératoconjonctivite épithéliale ponctuée |
| Score de Prédiction TxGNN | 99,63 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la minocycline appartient à la classe des tétracyclines. Son efficacité antibactérienne est établie dans les indications d'origine, et elle pourrait mécanistiquement être applicable à certaines atteintes de la surface oculaire.

Au-delà de son activité antibactérienne, la minocycline est décrite comme ayant des propriétés anti-inflammatoires, inhibitrices des métalloprotéinases matricielles (MMP) et anti-apoptotiques. Ces effets pourraient être pertinents pour l'inflammation de la surface oculaire. Par analogie, d'autres tétracyclines (comme la doxycycline) sont utilisées dans des atteintes de la surface oculaire telles que le dysfonctionnement des glandes de Meibomius et la blépharite.

Ce lien est cependant **déduit et non démontré** par les données compilées pour ce rapport. Le mécanisme ne peut pas être recoupé avec la pharmacologie documentée du médicament. Une seconde prédiction du modèle, la **kératite d'exposition** (score de 99,20 %), repose sur le même raisonnement spéculatif (inhibition de MMP-9, effets anti-inflammatoires). Elle est également de niveau L5 avec une recommandation Hold, car sa prise en charge repose avant tout sur la lubrification et le traitement de la cause de l'exposition.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60929447 (annulée) | MYNOCINE 100 mg, gélule (LABORATOIRE XO) | Gélule | Non renseignée |

Cette unique AMM étant annulée, le médicament n'a actuellement aucune AMM valide dans les données compilées, ce qui peut limiter sa disponibilité pratique. De plus, la forme disponible est une gélule orale : la compatibilité avec une voie d'administration oculaire n'a pas été évaluée.

## Considérations de Sécurité

- **Maladies associées à des contre-indications (graphe de connaissances, hors texte de la notice)** : maladie rénale, pyo-uretère, maladie hépatique, maladie de la vésicule biliaire, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, pseudotumeur cérébrale, hypertension intracrânienne, dyskinésie de l'œsophage.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi celles listées :
  - **Majeures** : isotrétinoïne, acitrétine (risque notamment lié à l'hypertension intracrânienne).
  - **Modérées** : éthinylestradiol, amoxicilline, ampicilline, acide aminolévulinique (topique), citrate de sodium, asparaginases, balsalazide, citrate de bismuth potassique, phosphate et acétate de calcium, brentuximab védotine, calaspargase pégol, cannabidiol.
  - **Mineures** : acétazolamide, hydrochlorothiazide, amiloride, bumétanide.

Les mises en garde et contre-indications issues de la notice n'ont pas pu être consultées. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (99,63 %), sans aucun essai clinique ni publication. Le niveau de preuve est L5.
- Les données de sécurité issues de la notice sont manquantes (lacune bloquante), le mécanisme d'action n'est pas documenté, et la seule AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications) pour permettre le dépistage de sécurité.
- Obtenir les données de mécanisme d'action (par exemple via DrugBank).
- Réaliser une revue systématique de la littérature et des registres d'essais sur la minocycline dans les atteintes de la surface oculaire.
- Évaluer la compatibilité de la voie d'administration (orale actuelle vs oculaire) et la disponibilité réelle du produit en France.
- Démontrer la pertinence préclinique de l'effet anti-MMP et anti-inflammatoire dans la kératoconjonctivite épithéliale ponctuée.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

