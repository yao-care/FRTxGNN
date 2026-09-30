---
layout: default
title: Calcitriol
parent: Prédiction du modèle uniquement (L5)
nav_order: 67
evidence_level: L5
indication_count: 7
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

# Calcitriol : De la Vitamine D Active à la Carence en Vitamine D (terme obsolète)

## Résumé en Une Phrase

Calcitriol est la forme active de la vitamine D, commercialisée en France en capsule molle (Rocaltrol) et en pommade (Silkis).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **carence en vitamine D (terme d'ontologie signalé comme obsolète)**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction précise.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Carence en vitamine D (terme obsolète) |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le calcitriol est la forme active de la vitamine D. Le lien biologique avec une carence en vitamine D est donc plausible, puisque le médicament apporte directement l'hormone active.

Cependant, le terme de maladie est signalé comme « obsolète », c'est-à-dire qu'il s'agit d'une entrée dépréciée de l'ontologie. Le score très élevé du modèle reflète probablement l'association avec la classe pharmacologique (vitamine D) plutôt qu'un véritable signal de repositionnement. Il faut donc l'interpréter avec prudence.

Aucun essai clinique ni aucune publication ne figurent dans les données fournies pour cette indication. La prédiction repose uniquement sur le modèle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 61847953 | ROCALTROL 0,25 microgramme, capsule molle | Capsule molle (voie orale) | ATNAHS PHARMA NETHERLANDS (Pays-Bas) |
| 62597239 | SILKIS 3 microgrammes/g, pommade | Pommade | GALDERMA INTERNATIONAL |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est de niveau L5 (modèle seul), sans essai ni publication. De plus, le terme de maladie est obsolète, ce qui affaiblit la portée du score élevé.
- Pour information, une autre indication prédite pour ce médicament, le **rachitisme hypophosphatémique héréditaire**, dispose de davantage de preuves (niveau L3, essais directs sur le calcitriol dans l'hypophosphatémie liée à l'X). Elle est classée « Proceed with Guardrails » et mérite une évaluation séparée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Remplacer le terme obsolète par l'entrée actuelle de l'ontologie, puis relancer l'évaluation.
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications), car ces données de sécurité bloquent le passage au criblage de sécurité S1.
- Obtenir les données de mécanisme d'action depuis DrugBank.
- Effectuer une recherche ciblée d'essais et de littérature sur le calcitriol dans la carence en vitamine D.
- Vérifier la compatibilité des voies d'administration : la capsule orale est a priori la forme pertinente pour une carence systémique, la pommade étant une forme cutanée.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

