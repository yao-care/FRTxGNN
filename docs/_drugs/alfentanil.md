---
layout: default
title: Alfentanil
parent: Prédiction du modèle uniquement (L5)
nav_order: 35
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Alfentanil : nouvelle indication prédite, Syndrome néphrogénique d'antidiurèse inappropriée (SNAI) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM disponibles"
monitor_inn: "ALFENTANIL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Alfentanil
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Alfentanil : De l'analgésie opioïde au syndrome néphrogénique d'antidiurèse inappropriée
{: .text-alpha }

## Résumé en Une Phrase

Alfentanil est un opioïde de synthèse agoniste des récepteurs mu, commercialisé en France sous le nom de Rapifen (solution injectable). Le texte des indications approuvées n'est pas disponible dans les données compilées pour ce rapport.
Le modèle TxGNN le prédit comme potentiellement efficace pour le **syndrome néphrogénique d'antidiurèse inappropriée (SNAI)**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM disponibles |
| Nouvelle Indication Prédite | Syndrome néphrogénique d'antidiurèse inappropriée (SNAI) |
| Score de Prédiction TxGNN | 0,9951 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales, l'alfentanil est un agoniste des récepteurs opioïdes mu, utilisé en anesthésie et en analgésie.

**La prédiction ne repose sur aucun lien mécanistique plausible.** Le SNAI est causé par des mutations de gain de fonction du récepteur V2 de la vasopressine (AVPR2), qui entraînent une rétention d'eau malgré une vasopressine indétectable. Les opioïdes peuvent stimuler la libération de vasopressine et favoriser l'antidiurèse par des mécanismes centraux et rénaux. On s'attendrait donc plutôt à une aggravation de la rétention d'eau et de l'hyponatrémie qu'à une amélioration.

Le score élevé de TxGNN (0,9951) provient uniquement d'une prédiction du modèle TxGNN (apprentissage profond). Il n'est pas étayé par un raisonnement pharmacologique, et la similarité avec l'indication originale n'a pas pu être évaluée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 68622560 | RAPIFEN 1 mg (0,5 mg/ml), solution injectable | Solution injectable | Active |
| 63670722 | RAPIFEN 5 mg (0,5 mg/ml), solution injectable | Solution injectable | Active |

Le texte des indications approuvées n'est pas renseigné pour ces deux AMM. Le titulaire est Piramal Critical Care (Pays-Bas).

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie de PrimeKG, et non texte de la notice) : maladie rénale, pyo-uretère, maladie hépatique, maladie de la vésicule biliaire, trouble hypotensif, pseudotumeur cérébrale, hypertension intracrânienne.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les 20 premières :
  - **Majeures** : aprépitant, bupropion, clarithromycine, clotrimazole, dexfenfluramine, dolasétron, fenfluramine, granisétron, lorcasérine.
  - **Modérées** : atropine, cimétidine, clidinium, dexaméthasone, dicyclomine, dronabinol, éluxadoline, phénylbutyrate de glycérol, glycopyrronium, hyoscyamine, mazindol.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Le mécanisme connu des opioïdes (stimulation de la libération de vasopressine) irait plutôt à l'encontre de l'effet recherché dans le SNAI.
- Les AMM françaises sont toutes annulées et le profil d'interactions est chargé (100 interactions), ce qui limite la faisabilité pratique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité).
- Les données détaillées sur le mécanisme d'action, à obtenir via DrugBank.
- Une justification pharmacologique plausible, ou des données précliniques, démontrant un effet bénéfique dans le SNAI.
- Une évaluation de la compatibilité des voies d'administration et de la similarité avec l'indication originale.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

