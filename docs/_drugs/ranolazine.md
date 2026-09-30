---
layout: default
title: Ranolazine
parent: Prédiction du modèle uniquement (L5)
nav_order: 260
evidence_level: L5
indication_count: 1
---

# Ranolazine
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

# Ranolazine : De l'Indication d'Origine (non renseignée) au Syndrome néphrogénique d'antidiurèse inappropriée

## Résumé en Une Phrase

La ranolazine est commercialisée en France sous le nom RANEXA (comprimés à libération prolongée), mais les données disponibles ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome néphrogénique d'antidiurèse inappropriée (NSIAD)**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée (aucun texte d'indication dans les AMM) |
| Nouvelle Indication Prédite | Syndrome néphrogénique d'antidiurèse inappropriée (NSIAD) |
| Score de Prédiction TxGNN | 99,65 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances générales, la ranolazine est un inhibiteur du courant sodique tardif (INaL), avec un effet partiel sur l'oxydation des acides gras. Ces informations ne proviennent pas du dossier d'évidence et doivent être confirmées.

Le NSIAD est causé, dans la plupart des cas, par des variants à gain de fonction du gène *AVPR2*. Le récepteur V2 est alors activé en permanence, ce qui entraîne une rétention d'eau via la voie AMPc/AQP2 et une hyponatrémie, malgré une vasopressine effacée. Aucune des deux actions connues de la ranolazine ne cible plausiblement la signalisation du récepteur V2 ni le trafic de l'AQP2.

**Aucun lien mécanistique établi n'est donc soutenu par les données fournies.** Le score de 0,996 est une prédiction issue d'un graphe de connaissances, sans corroboration par un essai, une publication ou une étude de mécanisme. Un éventuel lien (par exemple via des voisins communs dans le réseau) reste hypothétique et nécessite une validation indépendante.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63170891 | RANEXA 375 mg | Comprimé à libération prolongée | Non renseignée dans les données |
| 64679592 | RANEXA 500 mg | Comprimé à libération prolongée | Non renseignée dans les données |

Les deux AMM sont détenues par MENARINI INTERNATIONAL OPERATIONS LUXEMBOURG.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai, publication ni lien mécanistique plausible avec la physiopathologie du NSIAD.
- Les données de sécurité (mises en garde, contre-indications) et l'indication d'origine manquent, ce qui empêche de passer à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, indication approuvée), lacune bloquante.
- Compléter les données de mécanisme d'action via DrugBank.
- Rechercher des études précliniques ou de mécanisme reliant la ranolazine à la voie AVPR2/AMPc/AQP2.
- Valider indépendamment la prédiction, par exemple en analysant les voisins du réseau qui ont conduit au score.
- Évaluer la compatibilité des voies d'administration (statut actuellement en attente).

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

