---
layout: default
title: Nadolol
parent: Prédiction du modèle uniquement (L5)
nav_order: 208
evidence_level: L5
indication_count: 5
---

# Nadolol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Nadolol : D'une indication d'origine non renseignée à l'hypertension rénovasculaire maligne

## Résumé en Une Phrase

Le nadolol est un bêtabloquant non sélectif, commercialisé en France sous le nom CORGARD 80 mg. Le texte de son indication d'origine n'est pas renseigné dans les données reçues.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension rénovasculaire maligne**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée (texte d'indication vide dans l'AMM) |
| Nouvelle Indication Prédite | Hypertension rénovasculaire maligne |
| Score de Prédiction TxGNN | 99,59 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le nadolol est un bêtabloquant non sélectif. Il pourrait être mécanistiquement applicable à l'hypertension rénovasculaire, mais aucune donnée ne le confirme.

Le blocage des récepteurs bêta-1 rénaux réduit la libération de rénine. Cela est plausible dans une hypertension dépendante de la rénine, comme l'hypertension rénovasculaire. Comme l'indication d'origine n'est pas renseignée, on ne peut pas comparer les deux indications.

Plusieurs réserves s'imposent :
- L'hypertension maligne est une urgence hypertensive, généralement prise en charge par des agents intraveineux titrables. Le nadolol oral est peu susceptible d'être un traitement de première intention.
- Le score TxGNN (0,996) est une prédiction du modèle, sans preuve clinique directe ni indirecte.
- La prédiction voisine « maladie rénale hypertensive maligne » a exactement le même score (0,99587). Les deux prédictions partagent probablement les mêmes voisins dans le graphe et ne constituent pas des signaux indépendants.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

Note : des publications ont été récupérées pour une autre prédiction, l'hypertension pulmonaire liée à une maladie pulmonaire ou à l'hypoxie. Ce sont des revues générales de biologie de l'hypoxie (vieillissement cérébral, HIF dans le cancer, altitude), et aucune ne mentionne le nadolol ni le blocage bêta dans l'hypertension pulmonaire. Elles ne sont donc pas retenues comme preuves.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62092895 | CORGARD 80 mg, comprimé sécable (CHEPLAPHARM FRANCE) | Comprimé sécable | Texte d'indication non fourni |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication pertinente. Les données de sécurité de la notice ANSM manquent et bloquent toute évaluation de sécurité. Les quatre autres prédictions (maladie rénale hypertensive maligne, deux formes d'hypertension pulmonaire, syndrome de Braddock) sont aussi de niveau L5 et en Hold.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde et contre-indications), élément bloquant pour le criblage de sécurité
- Données sur le mécanisme d'action, à obtenir via DrugBank
- Indication d'origine autorisée du CORGARD, actuellement absente
- Recherche ciblée d'essais et de publications associant nadolol et hypertension rénovasculaire maligne
- Pour l'hypertension pulmonaire, évaluation de la sécurité (bronchospasme, baisse du débit cardiaque, dépression du ventricule droit)
- En cas d'insuffisance rénale, prise en compte de l'élimination rénale du nadolol pour l'ajustement de dose
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

