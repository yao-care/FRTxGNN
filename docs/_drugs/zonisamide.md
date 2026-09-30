---
layout: default
title: Zonisamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
---

# Zonisamide
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

# Zonisamide : De l'Épilepsie au Syndrome de Gilles de la Tourette

## Résumé en Une Phrase

Le zonisamide est un médicament antiépileptique. La littérature le décrit comme traitement adjuvant des crises partielles, mais le texte d'indication des AMM françaises est vide dans les données reçues.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de Gilles de la Tourette**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM (texte d'indication vide) ; décrit comme antiépileptique dans la littérature |
| Nouvelle Indication Prédite | Syndrome de Gilles de la Tourette |
| Score de Prédiction TxGNN | 99,85 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les informations connues, le zonisamide bloque les canaux sodiques et les canaux calciques de type T, et pourrait moduler les systèmes GABA et glutamate.

Le lien avec les circuits impliqués dans les tics reste **spéculatif**. La prédiction repose uniquement sur le modèle (score élevé, mais rang 1615 seulement). Aucune donnée expérimentale ou clinique ne la confirme.

Une revue pragmatique (PMID 36005856) rapporte que des médicaments antiépileptiques peuvent induire des troubles obsessionnels-compulsifs et des tics. Pour cette indication, il s'agit donc plutôt d'un **signal de sécurité possible** que d'un argument en faveur de l'efficacité.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Cinq des 20 AMM sont présentées ci-dessous. Le texte de l'indication approuvée est vide dans les données reçues.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|------|
| 64122807 | ZONEGRAN 100 mg, gélule | Gélule | AMDIPHARM |
| 63127527 | ZONISAMIDE SANDOZ 25 mg, gélule | Gélule | SANDOZ |
| 62540779 | ZONISAMIDE TEVA 25 mg, gélule | Gélule | TEVA SANTE |
| 61247321 | ZONISAMIDE ARROW 50 mg, gélule | Gélule | ARROW GENERIQUES |
| 69552780 | ZONISAMIDE NEURAXPHARM 200 mg, comprimé sécable | Comprimé sécable | NEURAXPHARM FRANCE |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données.

Seul signal disponible : une revue (PMID 36005856) décrit des TOC et des tics induits par des antiépileptiques, ce qui appelle à la prudence pour une indication de type tics.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et le seul élément de littérature pertinent évoque un risque plutôt qu'un bénéfice.
- Les données de sécurité de la notice ANSM manquent (lacune bloquante), ce qui empêche toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde et contre-indications).
- Obtenir les données sur le mécanisme d'action via DrugBank.
- Faire une recherche bibliographique ciblée sur le zonisamide dans les tics et le syndrome de Gilles de la Tourette.
- Pour information, d'autres candidats de ce dossier disposent de davantage de preuves : l'**épilepsie-absence** (niveau L3, séries de cas publiées et mécanisme plausible via les canaux calciques de type T) et la **manie bipolaire** (niveau L2, un essai randomisé contre placebo publié). Ils méritent d'être examinés en priorité.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

