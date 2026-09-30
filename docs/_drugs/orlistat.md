---
layout: default
title: Orlistat
parent: Prédiction du modèle uniquement (L5)
nav_order: 224
evidence_level: L5
indication_count: 1
---

# Orlistat
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

# Orlistat : D'une Indication Originale Non Renseignée à l'Hypervitaminose

## Résumé en Une Phrase

Orlistat est un inhibiteur des lipases gastriques et pancréatiques, commercialisé en France (Xenical et un générique). Son indication originale ne figure pas dans les données d'AMM disponibles.
Le modèle TxGNN prédit qu'il pourrait être utile dans l'**hypervitaminose**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette piste : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les textes d'AMM disponibles |
| Nouvelle Indication Prédite | Hypervitaminose |
| Score de Prédiction TxGNN | 99,42 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de référence. Sur la base des informations connues, l'orlistat inhibe les lipases gastriques et pancréatiques, ce qui réduit d'environ 30 % l'absorption des graisses alimentaires.

Cette réduction diminue aussi l'absorption des vitamines liposolubles (A, D, E, K). Le risque de carence en ces vitamines est d'ailleurs signalé dans l'information réglementaire du produit. Sur le plan mécanistique, une absorption réduite pourrait donc être utile en cas d'excès de vitamines liposolubles d'origine orale (par exemple hypervitaminose A ou D).

**Limites importantes :**
- Ce lien est déduit d'un effet indésirable connu et n'est étayé par aucune donnée clinique.
- Il ne s'appliquerait pas aux hypervitaminoses d'origine non alimentaire (voie parentérale, surproduction endogène).
- Le score élevé de TxGNN (0,994) reste une prédiction du modèle. La similarité avec l'indication originale n'a pas encore pu être évaluée, et la compatibilité des voies d'administration est en attente.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 65715632 | XENICAL 120 mg, gélule | Gélule | CHEPLAPHARM ARZNEIMITTEL (Allemagne) |
| 65734134 | ORLISTAT EG 120 mg, gélule | Gélule | EG LABO - Laboratoires Eurogenerics |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle TxGNN (niveau L5), sans essai clinique ni publication. Le lien mécanistique est déduit d'un effet indésirable connu, et les données de sécurité de la notice ne sont pas encore disponibles pour l'évaluation.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice de l'ANSM (mises en garde et contre-indications), étape bloquante avant tout criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (MOA) via DrugBank
- Confirmer l'indication originale dans les textes d'AMM
- Effectuer une recherche systématique de la littérature et des essais sur l'hypervitaminose (A, D, E, K)
- Évaluer la similarité avec l'indication originale et la compatibilité des voies d'administration
- Évaluer le rapport bénéfice/risque, l'orlistat pouvant provoquer des carences en vitamines liposolubles
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

