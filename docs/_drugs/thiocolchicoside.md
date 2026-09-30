---
layout: default
title: Thiocolchicoside
parent: Prédiction du modèle uniquement (L5)
nav_order: 306
evidence_level: L5
indication_count: 2
---

# Thiocolchicoside
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

# Thiocolchicoside : De l'Indication Originale Non Documentée à l'Insomnie

## Résumé en Une Phrase

Le thiocolchicoside est commercialisé en France (9 AMM), mais les données réglementaires reçues ne précisent pas son indication originale.
Le modèle TxGNN le prédit comme potentiellement efficace pour l'**insomnie**, avec un score très élevé (99,89 %). Cependant, **aucune publication** ne soutient cette prédiction, et le seul essai clinique associé (**1 essai**) ne porte pas sur l'insomnie.
Cette prédiction repose donc uniquement sur le modèle (niveau de preuve L5) et elle est **en contradiction apparente avec la pharmacologie connue** du médicament.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM reçues |
| Nouvelle Indication Prédite | Insomnie |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 9 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances pharmacologiques générales (et non d'après les données fournies), le thiocolchicoside est décrit comme un myorelaxant agissant comme antagoniste compétitif des récepteurs GABA-A, avec un effet sur les récepteurs de la glycine.

Sur cette base, le lien mécanistique avec l'insomnie est **faible, voire défavorable** : antagoniser la signalisation GABAergique inhibitrice tendrait plutôt à favoriser l'éveil ou à abaisser le seuil convulsif qu'à traiter l'insomnie. Un bénéfice ne pourrait être qu'indirect, par exemple un meilleur sommeil grâce au soulagement de spasmes musculaires douloureux.

Le score TxGNN élevé (0,999) est une prédiction issue d'un graphe de connaissances. Aucune donnée clinique ou mécanistique du dossier ne vient la confirmer.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT06791434](https://clinicaltrials.gov/study/NCT06791434) | Phase 4 | Terminé | 156 | Aiguilletage sec en complément du traitement conventionnel de la lombalgie myofasciale. Pertinence faible (grade C) : l'insomnie n'est pas la pathologie étudiée et le thiocolchicoside n'est pas l'intervention testée. Au mieux, le bras conventionnel peut inclure un myorelaxant. |

Cet essai ne fournit aucune preuve directe pour l'insomnie.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69999429 | THIOCOLCHICOSIDE EG 4 mg | Comprimé sécable | Non renseignée |
| 63646098 | THIOCOLCHICOSIDE ZENTIVA 4 mg | Comprimé | Non renseignée |
| 68086109 | THIOCOLCHICOSIDE CRISTERS 4 mg | Comprimé | Non renseignée |
| 65617572 | MIOREL 4 mg | Gélule | Non renseignée |
| 67136662 | THIOCOLCHICOSIDE BIOGARAN 4 mg | Comprimé | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication pertinents, et le mécanisme connu (antagonisme GABA-A) va à l'encontre d'un effet bénéfique dans l'insomnie.
- Les informations de sécurité de la notice ANSM manquent, ce qui bloque l'étape de criblage de sécurité.

La seconde prédiction, le **delirium tremens (sevrage alcoolique)**, a un score de 99,21 % mais aucune preuve clinique. L'antagonisme GABAergique s'oppose au traitement standard par benzodiazépines, et le risque convulsif signalé pour ce médicament pourrait aggraver l'évolution dans ce contexte. Elle est également en **Hold**.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde et contre-indications, en particulier le risque convulsif).
- Obtenir les données de mécanisme d'action depuis DrugBank pour l'analyse du lien mécanistique.
- Identifier l'indication originale approuvée pour chaque AMM.
- Rechercher des études cliniques ou précliniques directement liées à l'insomnie ; sinon, envisager d'abandonner cette piste.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

