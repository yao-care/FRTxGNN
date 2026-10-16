---
layout: default
title: Regadenoson
parent: Prédiction du modèle uniquement (L5)
nav_order: 656
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Regadenoson : nouvelle indication prédite, Anaphylaxie (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM (usage connu : agent de stress…"
monitor_inn: "regadenoson"
predicted_indications: ["anaphylaxis", "food-dependent exercise-induced anaphylaxis", "esotropia", "pseudoallergy"]
---

# Regadenoson
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

# Regadénoson : D'agent de stress pharmacologique pour l'imagerie myocardique à l'anaphylaxie

## Résumé en Une Phrase

Le régadénoson est un agoniste sélectif du récepteur A2A de l'adénosine, utilisé comme agent diagnostique pour l'imagerie de perfusion myocardique (scintigraphie).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**anaphylaxie**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM (usage connu : agent de stress pour l'imagerie de perfusion myocardique) |
| Nouvelle Indication Prédite | Anaphylaxie |
| Score de Prédiction TxGNN | 99,85 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de référence. Les données de pharmacologie indiquent toutefois que le régadénoson se lie aux récepteurs de l'adénosine A1, A2A, A2B et A3, et qu'il est utilisé comme agent diagnostique pour l'imagerie de perfusion myocardique. Il est décrit comme un agoniste sélectif du récepteur A2A.

Le lien mécanistique théorique est le suivant : la signalisation A2A peut freiner la dégranulation des mastocytes et la libération de médiateurs inflammatoires dans des modèles précliniques. Cela offrirait une piste plausible, mais non validée, vers l'anaphylaxie. Le même raisonnement vaut, de façon plus hypothétique encore, pour la pseudo-allergie (activation mastocytaire non médiée par les IgE).

Cette hypothèse se heurte à un problème de sécurité majeur : le régadénoson provoque une vasodilatation et une hypotension, alors que le traitement de première intention de l'anaphylaxie (l'adrénaline) agit par des effets hémodynamiques opposés. Le score élevé de TxGNN est une prédiction purement computationnelle. La similarité avec l'indication originale n'a pas pu être évaluée.

Autres prédictions du modèle, toutes de niveau L5 et en statut « Hold » :

| Rang | Indication prédite | Score TxGNN | Commentaire |
|------|------|------|------|
| 2 | Anaphylaxie d'effort dépendante de l'alimentation | 99,74 % | Même hypothèse mastocytaire ; bolus IV unique mal adapté à la prévention d'événements épisodiques ; risque hémodynamique à l'effort |
| 3 | Ésotropie | 99,12 % | Aucun lien mécanistique identifié ; probable artefact du graphe de connaissances |
| 4 | Pseudo-allergie | 99,12 % | Rationnel théorique uniquement ; le régadénoson peut lui-même provoquer des réactions de type hypersensibilité |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69075222 | RAPISCAN 400 microgrammes, solution injectable (GE Healthcare, Norvège) | Solution injectable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie du graphe PrimeKG, et non texte de notice) :
  - Cardiovasculaires : hypertension, hypotension, sténose aortique et maladies de la valve aortique, sténose mitrale, bloc auriculo-ventriculaire, maladie du sinus, maladie coronarienne, péricardite, épanchement péricardique, hémopéricarde, sténose carotidienne, thrombose de l'artère carotide, accident ischémique transitoire, insuffisance vertébro-basilaire.
  - Respiratoires : asthme (y compris intrinsèque et allergique), bronchopneumopathie chronique obstructive (y compris forme sévère à début précoce), maladie bronchique.
  - Neurologiques et autres : épilepsie, maladie du système nerveux autonome, syndrome de Horner.
- **Interactions médicamenteuses** (10 signalées, 6 de niveau modéré) : caféine, dipyridamole, dyphylline, théophylline, aminophylline, oxtriphylline. Les méthylxanthines et le dipyridamole modifient la signalisation de l'adénosine et peuvent donc moduler l'effet du régadénoson.
- **Sécurité spécifique à la prédiction** : l'effet vasodilatateur et hypotenseur est contraire à la prise en charge hémodynamique de l'anaphylaxie. Plusieurs contre-indications du graphe (asthme, hypotension, maladies cardiovasculaires) recoupent des comorbidités fréquentes chez les patients à risque anaphylactique.

Les mises en garde et contre-indications issues de la notice ANSM n'ont pas pu être obtenues ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Le profil hémodynamique du régadénoson va à l'encontre de la prise en charge de l'anaphylaxie, et le seul produit français est annulé.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mécanisme d'action détaillé (DrugBank) et analyse du lien mécanistique.
- Mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité).
- Données précliniques montrant un effet de l'agonisme A2A sur la dégranulation mastocytaire dans des modèles d'anaphylaxie, avec évaluation du risque hypotenseur.
- Évaluation de la compatibilité de voie d'administration (bolus IV unique vs besoin thérapeutique) et de la similarité avec l'indication originale.
- Revue de la littérature et des registres d'essais pour confirmer l'absence ou l'existence de preuves.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

