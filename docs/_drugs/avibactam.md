---
layout: default
title: Avibactam
parent: Prédiction du modèle uniquement (L5)
nav_order: 84
evidence_level: L5
indication_count: 4
monitor_inn: "avibactam"
predicted_indications: ["ureter tuberculosis", "urinary schistosomiasis", "polyclonal hyperviscosity syndrome", "hyperamylasemia"]
last_modified_at: 2026-10-23
description: "Avibactam : nouvelle indication prédite, Tuberculose de l'uretère (niveau de preuve L5). Indication d'origine : Pyélonéphrite"
---

# Avibactam
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

## Avibactam : De la pyélonéphrite à la tuberculose de l'uretère
{: .text-alpha }

## Résumé en Une Phrase

Avibactam est un inhibiteur de bêta-lactamases, dont l'usage connu dans la base de connaissances concerne la **pyélonéphrite**.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **tuberculose de l'uretère**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Pyélonéphrite (relation recorded dans le graphe de connaissances ; le texte des AMM ne contient pas d'indication renseignée) |
| Nouvelle Indication Prédite | Tuberculose de l'uretère |
| Score de Prédiction TxGNN | 0,9911 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, l'avibactam est un inhibiteur de bêta-lactamases non bêta-lactamine (de type diazabicyclooctane), commercialisé en association avec un antibiotique bêta-lactamine. Seul, il n'a pas d'activité antibactérienne notable.

Le lien avec la tuberculose est plausible mais indirect : *Mycobacterium tuberculosis* produit une bêta-lactamase de classe A (BlaC), que l'avibactam inhibe in vitro, et l'association avec des bêta-lactamines a montré une activité in vitro contre ce germe. La localisation urinaire est en outre proche de l'usage connu (pyélonéphrite).

Il faut toutefois rester prudent : le score élevé est une prédiction de modèle, sans essai ni publication à l'appui. Tout bénéfice dépendrait d'une bêta-lactamine partenaire, et la tuberculose rénale ou urétérale requiert des schémas antituberculeux standards à plusieurs médicaments.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69979273 | ZAVICEFTA 2 g/0,5 g | Poudre pour solution à diluer pour perfusion | Non renseignée dans les données compilées |
| 68544663 | EMBLAVEO 1,5 g/0,5 g | Poudre pour solution à diluer pour perfusion | Non renseignée dans les données compilées |

Ces deux produits sont des spécialités contenant l'avibactam, et sont commercialisés en France.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai clinique ni publication ne porte sur la tuberculose de l'uretère. Les données de sécurité de la notice sont aussi absentes, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM
- Obtenir les données sur le mécanisme d'action
- Rassembler des données précliniques (activité in vitro avec bêta-lactamine partenaire sur *M. tuberculosis*) puis des études cliniques ciblées
- Évaluer la place d'une telle association par rapport aux schémas antituberculeux standards

*Note : les autres prédictions (schistosomiase urinaire, syndrome d'hyperviscosité polyclonale, hyperamylasémie) n'ont aucun lien mécanistique plausible ni aucune preuve clinique, et sont également classées L5 / Hold.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

