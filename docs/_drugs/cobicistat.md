---
layout: default
title: Cobicistat
parent: Prédiction du modèle uniquement (L5)
nav_order: 193
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Cobicistat : nouvelle indication prédite, Syndrome d'immunodéficience acquise féline (niveau de preuve L5). Indication d'origine : Infection par le VIH, SIDA"
monitor_inn: "COBICISTAT"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Cobicistat
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Cobicistat : Du VIH/SIDA au Syndrome d'Immunodéficience Acquise Féline
{: .text-alpha }

## Résumé en Une Phrase

Cobicistat est un agent « booster » pharmacocinétique (inhibiteur du CYP3A), initialement utilisé dans le traitement de l'infection par le VIH et du SIDA.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome d'immunodéficience acquise féline**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection par le VIH, SIDA (selon le graphe de connaissances TxGNN ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Syndrome d'immunodéficience acquise féline |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le cobicistat est un inhibiteur du CYP3A sans activité antirétrovirale propre. Il sert de booster pharmacocinétique pour d'autres agents (elvitégravir, atazanavir, darunavir), dont il augmente l'exposition.

Le syndrome d'immunodéficience acquise féline est causé par le virus de l'immunodéficience féline (FIV), un lentivirus apparenté au VIH. Le score élevé (99,92 %) reflète vraisemblablement la proximité dans le réseau de connaissances avec les indications VIH/SIDA d'origine, plutôt qu'un mécanisme distinct.

Tout bénéfice dépendrait de la co-administration avec un antirétroviral actif contre le FIV, et aucune association de ce type n'est étayée par les données disponibles. Le statut commercial (AMM annulées) et les 100 interactions médicamenteuses recensées compliquent en outre tout usage vétérinaire.

**Autres prédictions du modèle (même niveau de preuve L5) :**
- **Infection par le virus de l'immunodéficience simienne** (score 99,92 %) : le SIV est un modèle primate non humain du VIH. Le cobicistat n'aurait d'intérêt que comme composant d'un schéma combiné, et seulement comme piste de recherche préclinique pharmacocinétique.
- **Trouble neurodéveloppemental avec démarche ataxique, absence de parole et diminution de la substance blanche corticale** (score 99,91 %) : aucun lien mécanistique plausible ; il s'agit probablement d'un artefact du graphe de connaissances.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 65768058 | STRIBILD 150 mg/150 mg/200 mg/245 mg | Comprimé pelliculé | Annulée |
| 65453475 | GENVOYA 150 mg/150 mg/200 mg/10 mg | Comprimé pelliculé | Annulée |

Les deux AMM sont détenues par Gilead Sciences Ireland UC (Irlande). Le texte de l'indication approuvée n'est pas renseigné dans les données compilées.

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions sont recensées. Parmi les 20 premières examinées :
  - **Majeures** : lopéramide, triamcinolone, cisapride, budésonide.
  - **Modérées** : hydrocortisone, aprépitant, bétaméthasone, clotrimazole, dexaméthasone (y compris formes nasale et ophtalmique), dexfenfluramine, fenfluramine, métoclopramide, prednisolone (ophtalmique), répaglinide, hydrocortisone (ophtalmique), budésonide (nasal), clarithromycine.
  - **Mineure** : prucalopride.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le cobicistat n'a pas d'activité antivirale propre, et ses AMM françaises sont toutes annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action, à compléter via DrugBank.
- Mises en garde et contre-indications issues de la notice ANSM (données bloquantes pour le criblage de sécurité).
- Justification biologique de l'association avec un antirétroviral actif contre le FIV.
- Études précliniques pharmacocinétiques (par exemple en modèle primate SIV) avant toute considération clinique.
- Évaluation de la faisabilité vétérinaire (voies d'administration, formes disponibles), actuellement non déterminée.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

