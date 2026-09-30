---
layout: default
title: Pipobroman
parent: Prédiction du modèle uniquement (L5)
nav_order: 239
evidence_level: L5
indication_count: 1
---

# Pipobroman
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

# Pipobroman : De l'Indication Originale Non Documentée à la Cataracte Diabétique

## Résumé en Une Phrase

Le pipobroman (DrugBank DB00236) est commercialisé en France sous le nom VERCYTE 25 mg, comprimé. Son indication originale n'est pas renseignée dans les données disponibles, mais il est généralement décrit comme un antinéoplasique cytotoxique de type alkylant.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **cataracte diabétique**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Cataracte diabétique |
| Score de Prédiction TxGNN | 99,01 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Aucune indication originale n'est renseignée non plus. Il n'est donc pas possible de comparer la prédiction à une justification pharmacologique connue.

Le seul élément en faveur de la prédiction est le score TxGNN de 0,99. Il s'agit d'une sortie de modèle, pas d'une preuve clinique. Le pipobroman est généralement décrit comme un agent cytotoxique de type alkylant, ce qui ne correspond pas évidemment à la cataracte diabétique. Celle-ci est habituellement attribuée au flux de la voie des polyols (aldose réductase), au stress oxydatif et à la glycation des protéines. Aucun lien entre ces voies et le pipobroman n'est démontré par les données fournies.

Un agent cytotoxique soulève en outre des préoccupations de sécurité pour une indication oculaire chronique non oncologique. Ce score élevé doit donc être traité comme un signal générateur d'hypothèses, à valider sur le plan mécanistique avant tout travail supplémentaire.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 60195398 | VERCYTE 25 mg, comprimé | Comprimé | Laboratoires Delbert |

Le texte de l'indication approuvée n'est pas renseigné pour cette AMM.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (agent de type alkylant, selon la description générale du pipobroman ; catégories DrugBank non fournies) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | À traiter comme un médicament cytotoxique, selon la réglementation de manipulation applicable, dans l'attente de la notice |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication ni lien mécanistique démontré.
- La nature cytotoxique du médicament pose une question de rapport bénéfice/risque pour une indication oculaire chronique non oncologique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications), qui bloque le passage au criblage de sécurité S1.
- Obtenir les données sur le mécanisme d'action (par exemple via l'API DrugBank).
- Documenter l'indication originale et le texte d'indication de l'AMM.
- Rechercher des preuves précliniques ou mécanistiques reliant le pipobroman aux voies de la cataracte diabétique (polyols, stress oxydatif, glycation).
- Évaluer la compatibilité de la voie d'administration (orale actuellement) avec une indication oculaire.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

