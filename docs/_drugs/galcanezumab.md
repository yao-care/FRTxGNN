---
layout: default
title: Galcanezumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 355
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Galcanezumab : nouvelle indication prédite, Déficit en cofacteur II de l'héparine (niveau de preuve L5). Indication d'origine : Migraine (avec ou sans aura)"
monitor_inn: "galcanezumab"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
---

# Galcanezumab
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

# Galcanezumab : De la migraine au déficit en cofacteur II de l'héparine

## Résumé en Une Phrase

Galcanezumab est un anticorps monoclonal qui neutralise le peptide lié au gène de la calcitonine (CGRP). Il était initialement utilisé pour le traitement de la migraine (avec ou sans aura).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **déficit en cofacteur II de l'héparine**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction. Elle repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Migraine (avec ou sans aura) |
| Nouvelle Indication Prédite | Déficit en cofacteur II de l'héparine |
| Score de Prédiction TxGNN | 99,50 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, galcanezumab est un anticorps monoclonal dirigé contre le CGRP, dont l'efficacité dans la migraine passe par la voie trigémino-vasculaire.

**Cette prédiction n'est pas étayée sur le plan mécanistique.** Le déficit en cofacteur II de l'héparine est une thrombophilie héréditaire, liée à une inhibition réduite de la thrombine par le cofacteur II de l'héparine (SERPIND1). La signalisation du CGRP n'est pas connue pour réguler ce cofacteur ni la cascade de coagulation.

Le score élevé (0,995) semble être un artefact du graphe de connaissances, probablement dû à la proximité de nœuds vasculaires ou liés à la coagulation, plutôt qu'à une justification biologique. Les deux autres prédictions les mieux classées (déficit en antithrombine de type 2, excès de facteur V avec thrombose spontanée) sont aussi des thrombophilies avec des scores quasi identiques (0,994). Cela suggère un artefact systématique de regroupement plutôt qu'un signal indépendant.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69972332 | EMGALITY 120 mg, solution injectable en stylo prérempli (statut : annulée) | Solution injectable | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Remarque : les données compilées pour ce rapport n'incluent aucune interaction médicamenteuse recensée. Cela ne signifie pas l'absence d'interactions. Dans un contexte de risque thrombotique, la prudence s'impose, car les médicaments agissant sur la voie du CGRP ont fait l'objet de signalements d'événements vasculaires (hypertension, événements de type Raynaud) après commercialisation.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Aucun lien mécanistique crédible n'a été identifié entre le blocage du CGRP et la coagulation.
- Le score élevé est vraisemblablement un artefact de graphe, et la seule AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données sur le mécanisme d'action, afin de confirmer l'absence de lien avec la voie de la coagulation
- Les mises en garde et contre-indications de la notice de l'ANSM (données bloquantes pour le criblage de sécurité)
- Une revue de la littérature et des registres d'essais, pour confirmer l'absence de signal
- Une évaluation de l'artefact de regroupement des thrombophilies dans le graphe, avant d'envisager toute étude
- Une réévaluation des indications prédites alternatives, ayant une plausibilité biologique plus forte
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

