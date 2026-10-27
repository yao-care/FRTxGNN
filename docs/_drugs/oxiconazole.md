---
layout: default
title: Oxiconazole
parent: Preuves modérées (L3-L4)
nav_order: 567
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-14
description: "Oxiconazole : nouvelle indication prédite, Candidose cutanée (niveau de preuve L3). Indication d'origine : Non renseignée dans le texte de l'AMM"
---

# Oxiconazole
{: .fs-9 }

Niveau de preuve: **L3** | Indications prédites: **1** 
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

## Oxiconazole : Des Mycoses Cutanées Superficielles à la Candidose Cutanée
{: .text-alpha }

## Resume en Une Phrase

Oxiconazole est un antifongique imidazole à usage topique, initialement utilisé pour traiter les dermatophytoses (pied d'athlète, teigne du corps) et le pityriasis versicolor.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **candidose cutanée**, avec un score de **99,81 %**.
Aucun essai clinique n'est enregistré, et **5 publications** (principalement des revues) soutiennent indirectement cette direction.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignée dans le texte de l'AMM ; la base de connaissances mentionne : pied d'athlète, teigne du corps, pityriasis versicolor, dermatophytose de l'aine et de la région périanale |
| Nouvelle Indication Predite | Candidose cutanée |
| Score de Prediction TxGNN | 99,81 % |
| Niveau de Preuve | L3 |
| Statut de Marche en France | Annulée uniquement (AMM retirée) |
| Nombre d'AMM | 1 |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action de ce médicament ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances sur la classe, oxiconazole fait partie des antifongiques imidazolés. Cette classe inhibe la lanostérol 14-alpha-déméthylase (CYP51), enzyme fongique, ce qui bloque la synthèse de l'ergostérol et fragilise la membrane de la cellule fongique.

Les espèces de *Candida* sont sensibles à ce mécanisme. Une activité contre la candidose cutanée est donc biologiquement plausible, et cohérente avec les indications d'origine (dermatophytoses et pityriasis versicolor), qui sont aussi des infections fongiques superficielles de la peau.

Le score élevé de TxGNN (99,81 %) va dans le même sens, mais il s'agit d'une prédiction de modèle et non d'une preuve clinique. Le raisonnement repose ici sur des connaissances de classe, et non sur des données propres à oxiconazole.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [6382000](https://pubmed.ncbi.nlm.nih.gov/6382000/) | 1984 | Étude clinique comparative | Mykosen | Comparaison d'oxiconazole et d'éconazole dans les dermatomycoses (résumé non disponible ; plan d'étude et randomisation non confirmés) |
| [24196340](https://pubmed.ncbi.nlm.nih.gov/24196340/) | 2013 | Revue | J Drugs Dermatol | Optimisation du traitement antifongique topique des infections cutanées superficielles ; la plupart peuvent être traitées par voie topique |
| [7501581](https://pubmed.ncbi.nlm.nih.gov/7501581/) | 1995 | Revue | Postgrad Med | Vue d'ensemble des infections fongiques superficielles ; teignes, candidose cutanée et pityriasis versicolor peuvent être traités par de nombreux antifongiques topiques |
| [10439936](https://pubmed.ncbi.nlm.nih.gov/10439936/) | 1999 | Revue | Drugs | Terbinafine dans les mycoses superficielles (autre médicament, preuve indirecte) |
| [2670516](https://pubmed.ncbi.nlm.nih.gov/2670516/) | 1989 | Revue | Drugs | Bifonazole dans les mycoses superficielles (autre médicament, preuve indirecte) |

Aucune de ces publications ne porte directement sur oxiconazole dans la candidose cutanée. La seule étude concernant oxiconazole date de 1984 et traite des dermatomycoses en général.

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 60797376 | FONX 1 %, crème en tube (KARO PHARMA, Suède) | Crème | Non renseignée (AMM annulée) |

## Considerations de Securite

- **Contre-indication issue de la base de connaissances** : dermatite (relation médicament-maladie du graphe de connaissances, et non texte de la notice).
- **Interactions médicamenteuses** : aucune interaction retrouvée dans les données consultées.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prédiction est plausible sur le plan mécanistique (classe des imidazoles), mais elle ne repose que sur le modèle et sur des revues indirectes, sans essai clinique. Le niveau de preuve est L3 au mieux.
- L'unique AMM française est annulée et les informations de sécurité officielles manquent, ce qui bloque le passage à l'évaluation de sécurité.

**Pour avancer, les elements suivants sont necessaires :**
- Récupérer et analyser la notice officielle de l'ANSM (mises en garde et contre-indications)
- Obtenir les données détaillées sur le mécanisme d'action d'oxiconazole (DrugBank)
- Rechercher des études directes d'oxiconazole dans la candidose cutanée (activité in vitro, essais comparatifs)
- Vérifier la disponibilité actuelle d'une formulation topique en France, l'AMM étant annulée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

