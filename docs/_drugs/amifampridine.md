---
layout: default
title: Amifampridine
parent: Prédiction du modèle uniquement (L5)
nav_order: 54
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Amifampridine : nouvelle indication prédite, Glaucome (niveau de preuve L5). Indication d'origine : Syndrome myasthénique de Lambert-Eaton"
---

# Amifampridine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Amifampridine : Du Syndrome Myasthénique de Lambert-Eaton au Glaucome

## Résumé en Une Phrase

L'amifampridine (3,4-diaminopyridine) est un bloqueur des canaux potassiques, initialement utilisé pour le traitement du syndrome myasthénique de Lambert-Eaton.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **glaucome**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Syndrome myasthénique de Lambert-Eaton (selon le graphe de connaissances TxGNN ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Glaucome |
| Score de Prédiction TxGNN | 99,71 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 3 (0 valide, 3 annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, l'amifampridine bloque les canaux potassiques voltage-dépendants, ce qui prolonge la dépolarisation présynaptique et favorise la libération de neurotransmetteurs dépendante du calcium. Son efficacité dans le syndrome de Lambert-Eaton repose sur ce mécanisme.

Le lien avec le glaucome est **spéculatif**. La modulation des canaux potassiques a été évoquée en relation avec l'excitabilité des cellules ganglionnaires rétiniennes et la dynamique de l'humeur aqueuse, mais aucune donnée directe ne relie l'amifampridine à la pression intraoculaire ou à la neuropathie optique.

Le score élevé de TxGNN (0,997) reste une prédiction du modèle, sans aucun essai ni publication pour la corroborer. Par ailleurs, le blocage systémique des canaux potassiques soulève des préoccupations de sécurité (notamment le risque de convulsions) qu'il faudrait mettre en balance avec un éventuel bénéfice oculaire.

Une seconde prédiction, la **porphyrie aiguë intermittente** (score 99,32 %), figure également dans les données. Elle ne présente pas de lien mécanistique clair avec l'amifampridine, n'est étayée par aucune donnée clinique, et le risque de convulsions est là aussi un sujet de préoccupation. Elle est également classée L5 et Hold.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65825598 | AMIFAMPRIDINE SUBSTIPHARM 10 mg, comprimé sécable (AXUNIO PHARMA) | Comprimé sécable | Non renseignée (AMM annulée) |
| 69785998 | AMIFAMPRIDINE SERB 10 mg, comprimé (SERB) | Comprimé | Non renseignée (AMM annulée) |
| 69935992 | FIRDAPSE 10 mg, comprimé (SERB) | Comprimé | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 68 interactions recensées au total. Parmi celles présentées :
  - **Majeure** : bupropion
  - **Modérées** : corticoïdes (hydrocortisone, bétaméthasone, dexaméthasone, prednisolone, prednisone) ; anorexigènes et sympathomimétiques (dexfenfluramine, diéthylpropion, fenfluramine, mazindol, phentermine, sibutramine, éphédrine) ; dronabinol ; lévofloxacine ; métoclopramide ; opioïdes (morphine, morphine liposomale, opium) ; polyéthylène glycol 3350 avec électrolytes
- **Point d'attention général** : l'amifampridine abaisse le seuil épileptogène. Plusieurs interactions listées (bupropion, lévofloxacine, métoclopramide) relèvent également de ce risque, ce qui est à considérer en cas d'association.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le lien mécanistique avec le glaucome est spéculatif, et le profil de sécurité (risque de convulsions) est préoccupant.
- Toutes les AMM françaises sont annulées, et les données de sécurité issues de la notice sont manquantes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice auprès de l'ANSM (élément bloquant)
- Obtenir les données détaillées sur le mécanisme d'action via DrugBank
- Mener une revue de la littérature préclinique sur les canaux potassiques et la pression intraoculaire / neuroprotection rétinienne
- Évaluer la compatibilité de la voie d'administration (voie orale systémique vs voie oculaire) et le rapport bénéfice/risque
- Clarifier la situation réglementaire (raisons de l'annulation des AMM)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

