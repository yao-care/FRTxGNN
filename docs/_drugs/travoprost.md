---
layout: default
title: Travoprost
parent: Prédiction du modèle uniquement (L5)
nav_order: 782
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost : Du Glaucome à Angle Ouvert à la Calciphylaxie Viscérale

## Résumé en Une Phrase

Travoprost est un analogue de la prostaglandine F2-alpha, initialement utilisé pour traiter le glaucome à angle ouvert et l'hypertension oculaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **calciphylaxie viscérale**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Glaucome à angle ouvert, hypertension oculaire (les textes d'indication des AMM ne sont pas renseignés) |
| Nouvelle Indication Prédite | Calciphylaxie viscérale |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 20 (0 valide, 20 annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, travoprost est un agoniste du récepteur FP des prostaglandines. Son efficacité dans le glaucome repose sur la baisse de la pression intraoculaire, principalement par augmentation de l'écoulement uvéoscléral.

Pour la calciphylaxie viscérale, le lien mécanistique reste très spéculatif. Une hypothèse de vasodilatation ou de remodelage vasculaire pourrait être avancée, mais aucune donnée clinique ou bibliographique ne l'étaye. De plus, l'administration oculaire topique est peu susceptible de produire une exposition systémique pertinente.

Le score élevé du modèle doit donc être interprété comme un signal exploratoire, et non comme une preuve d'efficacité. Les autres indications prédites (syndromes du défilé thoracique, angiodysplasie gastrique, syndrome du orteil bleu, lymphangiectasie, dissection coronaire spontanée) présentent le même profil : aucune preuve et un lien mécanistique peu plausible.

## Preuves d'Essais Cliniques

Aucun essai clinique associé à la calciphylaxie viscérale n'est enregistré actuellement.

À titre d'information, pour la prédiction « maladie vasculaire » (rang 5), les essais retrouvés portent sur les indications d'origine ou sur des effets indésirables oculaires, et non sur une maladie vasculaire. Le seul essai touchant à la physiologie vasculaire est [NCT00308945](https://clinicaltrials.gov/study/NCT00308945) (Phase 4, terminé, 20 patients) : comparaison de travoprost et latanoprost sur le diamètre vasculaire rétinien et le flux sanguin choroïdien chez des patients glaucomateux. Il ne fournit qu'une information hémodynamique oculaire indirecte.

## Preuves de la Littérature

Aucune littérature associée à la calciphylaxie viscérale n'est disponible actuellement.

## Informations de Marché en France

Toutes les AMM sont annulées. Les textes d'indication approuvée ne sont pas renseignés dans les données compilées. Principales AMM :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 60670806 | TRAVATAN 40 µg/mL | Collyre en solution | Annulée |
| 63633802 | DUOTRAV 40 µg/mL + 5 mg/mL | Collyre en solution | Annulée |
| 67138300 | VIZITRAV 40 µg/mL | Collyre en solution | Annulée |
| 62332319 | SINETRAV 40 µg/mL | Collyre en solution | Annulée |
| 68058227 | TRAVOPROST ZENTIVA 40 µg/mL | Collyre en solution | Annulée |

Les 15 autres AMM (génériques de travoprost seul ou associés au timolol) sont également annulées.

## Considérations de Sécurité

- **Maladies associées à une contre-indication dans le graphe de connaissances** (et non issues d'une notice) : uvéite, maladie de l'iris, maladie du corps ciliaire, panuvéite, iritis, œdème maculaire cystoïde, œdème rétinien maculaire.
- **Interactions médicamenteuses** : 49 interactions sont répertoriées, toutes de niveau « inconnu » (par exemple calcitriol, pantoprazole, sucralfate, morphine, metformine, oméprazole, prednisone, simvastatine, acide acétylsalicylique). Leur portée clinique n'est pas caractérisée.
- **Signal de sécurité de la littérature** : un cas d'effusion uvéale avec décollement rétinien exsudatif induit par travoprost topique chez un patient atteint du syndrome de Sturge-Weber-Krabbe (PMID [19107053](https://pubmed.ncbi.nlm.nih.gov/19107053/)).
- **Effets indésirables oculaires connus** : l'hyperhémie conjonctivale est fréquemment rapportée avec les analogues de prostaglandines, travoprost compris.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, non disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, avec un lien mécanistique spéculatif et une voie oculaire topique peu compatible avec une indication systémique. Par ailleurs, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action issues de DrugBank, afin d'analyser le lien mécanistique
- Notice officielle de l'ANSM (mises en garde et contre-indications) pour le dépistage de sécurité
- Données précliniques ou mécanistiques reliant l'agonisme du récepteur FP à la calciphylaxie
- Évaluation de la faisabilité d'une voie d'administration permettant une exposition systémique pertinente
- Clarification du statut réglementaire en France (annulation des AMM)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

