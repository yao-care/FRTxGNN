---
layout: default
title: Alfentanil
parent: Prédiction du modèle uniquement (L5)
nav_order: 22
evidence_level: L5
indication_count: 1
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

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Alfentanil : D'un adjuvant anesthésique (indication d'AMM non renseignée) au syndrome néphrogénique d'antidiurèse inappropriée

## Résumé en Une Phrase

Alfentanil est un agoniste opioïde µ de courte durée d'action, utilisé en contexte d'anesthésie et de soins aigus. Les données réglementaires disponibles ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome néphrogénique d'antidiurèse inappropriée (NSIAD)**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée (texte d'indication vide dans les AMM) |
| Nouvelle Indication Prédite | Syndrome néphrogénique d'antidiurèse inappropriée (NSIAD) |
| Score de Prédiction TxGNN | 99,51 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier, et DrugBank ne liste aucune indication d'origine. Alfentanil est un agoniste des récepteurs opioïdes µ, à action courte. Ses effets passent principalement par la signalisation opioïde centrale.

**Cette prédiction ne repose sur aucun lien mécanistique étayé.** Le NSIAD est causé par des variants activateurs (gain de fonction) du gène *AVPR2*, qui codent le récepteur V2 de la vasopressine. Ce récepteur est activé indépendamment de l'hormone, avec une vasopressine (AVP) indétectable. L'agonisme µ-opioïde est plutôt associé à une libération d'AVP, ce qui n'a pas de pertinence quand le défaut est un récepteur constitutivement actif, en aval de l'AVP.

Une voie thérapeutique plausible passerait par un antagonisme du récepteur V2 ou par un autre effet sur la réabsorption rénale de l'eau. Aucune action de ce type n'est documentée pour l'alfentanil. Ce médicament est par ailleurs un adjuvant anesthésique d'usage aigu, ce qui rend peu vraisemblable son emploi dans une maladie génétique chronique. Le score élevé est probablement un artefact du graphe de connaissances et ne doit pas être considéré comme une preuve.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68622560 | RAPIFEN 1 mg (0,5 mg/ml), solution injectable | Solution injectable | Non renseignée |
| 63670722 | RAPIFEN 5 mg (0,5 mg/ml), solution injectable | Solution injectable | Non renseignée |

Les deux AMM appartiennent à PIRAMAL CRITICAL CARE (Pays-Bas).

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai ni publication. Le mécanisme connu de l'alfentanil (agonisme µ-opioïde) ne rejoint pas la physiopathologie du NSIAD (récepteur V2 activé de façon constitutive).

**Pour avancer, les éléments suivants sont nécessaires :**
- La notice ANSM (mises en garde et contre-indications), indispensable au criblage de sécurité initial. Cette lacune est bloquante.
- Les données sur le mécanisme d'action, à interroger via l'API DrugBank.
- Les indications d'origine des deux AMM, absentes du dossier.
- Un lien mécanistique documenté avec la voie AVPR2 / réabsorption rénale de l'eau, ou des données précliniques qui le soutiennent.
- Une évaluation de la compatibilité de la voie d'administration (statut actuellement en attente), l'alfentanil n'existant ici qu'en solution injectable.

*Les résultats de ce rapport sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

