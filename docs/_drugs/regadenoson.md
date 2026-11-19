---
layout: default
title: Regadenoson
parent: Prédiction du modèle uniquement (L5)
nav_order: 656
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-20
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

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Regadénoson : D'agent de stress pharmacologique pour l'imagerie myocardique à l'anaphylaxie
{: .text-alpha }

## Résumé en Une Phrase

Le régadénoson est un agoniste sélectif du récepteur A2A de l'adénosine, utilisé comme agent diagnostique pour l'imagerie de perfusion myocardique (scintigraphie).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**anaphylaxie**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM (usage connu : agent de stress pour l'imagerie de perfusion myocardique) |
| Nouvelle Indication Prédite | Anaphylaxie |
| Score de Prédiction TxGNN | 0,9985 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Regadenoson (traduction non officielle) : « Le régadénoson est un agoniste de faible affinité (K i ≈ 1,3 µM) du récepteur A 2A de l'adénosine, avec une affinité au moins 10 fois plus faible pour le récepteur A 1 de l'adénosine (K i > 16,5 µM), et une affinité faible, voire nulle, pour les récepteurs A 2B et A 3 de l'adénosine. L'activation du récepteur A 2A de l'adénosine par le régadénoson produit une vasodilatation coronaire et augmente le débit sanguin coronaire (DSC). » Texte original en anglais : "Regadenoson is a low affinity agonist (K i ≈ 1.3 µM) for the A 2A adenosine receptor, with at least 10-fold lower affinity for the A 1 adenosine receptor (K i > 16.5 µM), and weak, if any, affinity for the A 2B and A 3 adenosine receptors. Activation of the A 2A adenosine receptor by regadenoson produces coronary vasodilation and increases coronary blood flow (CBF)." ([DailyMed: Lexiscan (regadenoson) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=057289f4-2e18-4c1e-bed4-6c1858e2ef16), version du 2018-12-21 ; consulté le 2026-11-19). Les données de pharmacologie indiquent toutefois que le régadénoson se lie aux récepteurs de l'adénosine A1, A2A, A2B et A3, et qu'il est utilisé comme agent diagnostique pour l'imagerie de perfusion myocardique. Il est décrit comme un agoniste sélectif du récepteur A2A.

Le lien mécanistique théorique est le suivant : la signalisation A2A peut freiner la dégranulation des mastocytes et la libération de médiateurs inflammatoires dans des modèles précliniques. Cela offrirait une piste plausible, mais non validée, vers l'anaphylaxie. Le même raisonnement vaut, de façon plus hypothétique encore, pour la pseudo-allergie (activation mastocytaire non médiée par les IgE).

Cette hypothèse se heurte à un problème de sécurité majeur : le régadénoson provoque une vasodilatation et une hypotension, alors que le traitement de première intention de l'anaphylaxie (l'adrénaline) agit par des effets hémodynamiques opposés. Le score élevé de TxGNN est une prédiction purement computationnelle. La similarité avec l'indication originale n'a pas pu être évaluée.

Autres prédictions du modèle, toutes de niveau L5 et en statut « Hold » :

| Rang | Indication prédite | Score TxGNN | Commentaire |
|------|------|------|------|
| 2 | Anaphylaxie d'effort dépendante de l'alimentation | 0,9974 | Même hypothèse mastocytaire ; bolus IV unique mal adapté à la prévention d'événements épisodiques ; risque hémodynamique à l'effort |
| 3 | Ésotropie | 0,9912 | Aucun lien mécanistique identifié ; le score provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, non une preuve biologique |
| 4 | Pseudo-allergie | 0,9912 | Rationnel théorique uniquement ; le régadénoson peut lui-même provoquer des réactions de type hypersensibilité |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69075222 | RAPISCAN 400 microgrammes, solution injectable (GE Healthcare, Norvège) | Solution injectable | Non renseignée (AMM active) |

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

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Lexiscan (regadenoson) prescribing information, Astellas Pharma US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=057289f4-2e18-4c1e-bed4-6c1858e2ef16) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

