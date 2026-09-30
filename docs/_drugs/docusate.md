---
layout: default
title: Docusate
parent: Prédiction du modèle uniquement (L5)
nav_order: 110
evidence_level: L5
indication_count: 2
---

# Docusate
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

# Docusate : Du Laxatif Émollient au Syndrome de Plummer-Vinson

## Résumé en Une Phrase

Docusate est un tensioactif anionique utilisé comme laxatif émollient (ramollissement des selles). Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de Plummer-Vinson**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette prédiction (0 et 0).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Syndrome de Plummer-Vinson |
| Score de Prédiction TxGNN | 99,18 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, docusate agit localement dans la lumière intestinale comme tensioactif pour ramollir les selles, avec une absorption systémique minime.

Le syndrome de Plummer-Vinson associe une anémie ferriprive, une dysphagie et des membranes œsophagiennes. Sa prise en charge repose sur la supplémentation en fer et la dilatation endoscopique. Rien dans la pharmacologie connue de docusate n'agit sur le statut en fer ni sur la pathologie des membranes œsophagiennes.

**Aucun lien mécanistique crédible n'a été identifié.** Le score élevé de TxGNN (0,992) est une prédiction issue du graphe de connaissances. Il s'agit probablement d'un artefact de topologie du graphe et non d'une preuve biologique. Il ne doit pas être interprété comme un signe d'efficacité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69281980 | NORGALAX, gel rectal en récipient unidose (ESSENTIAL PHARMA, Malte) | Gel | Non précisée dans les données disponibles |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et aucun lien mécanistique plausible n'a été identifié avec le syndrome de Plummer-Vinson.
- La seconde prédiction du modèle (anémie mégaloblastique constitutionnelle indépendante de la vitamine B12 et des folates, score 99,15 %) est dans la même situation : pas de lien mécanistique, aucune preuve.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) pour permettre le criblage de sécurité. Ce point est bloquant.
- Obtenir le mécanisme d'action détaillé via DrugBank.
- Évaluer la compatibilité de voie d'administration : le seul produit en France est un gel rectal, alors que la maladie prédite relève d'une prise en charge systémique et œsophagienne.
- Rechercher une éventuelle preuve biologique ou clinique indépendante avant toute réévaluation.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat de repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

