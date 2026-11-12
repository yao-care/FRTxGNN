---
layout: default
title: Oxitriptan
parent: Prédiction du modèle uniquement (L5)
nav_order: 568
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Oxitriptan : nouvelle indication prédite, Insomnie (niveau de preuve L5). Indication d'origine : Non renseignée (le texte d'indication de l'AMM est vide)"
monitor_inn: "OXITRIPTAN"
predicted_indications: ["insomnia (disease)"]
---

# Oxitriptan
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

## Oxitriptan : D'une indication non documentée à l'Insomnie
{: .text-alpha }

## Résumé en Une Phrase

Oxitriptan (5-hydroxytryptophane, 5-HTP) est le précurseur biosynthétique immédiat de la sérotonine ; son indication d'origine n'est pas renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**insomnie**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : la prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée (le texte d'indication de l'AMM est vide) |
| Nouvelle Indication Prédite | Insomnie |
| Score de Prédiction TxGNN | 0,9989 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'oxitriptan est un intermédiaire métabolique entre le tryptophane et la sérotonine. Son indication d'origine n'étant pas documentée, aucune comparaison directe avec la nouvelle indication n'est possible.

D'un point de vue biologique, la sérotonine est elle-même un précurseur de la mélatonine, qui régule le cycle veille-sommeil. Cela offre une justification plausible d'un rôle dans la régulation du sommeil.

Cette justification reste toutefois théorique. Elle repose uniquement sur le score du modèle TxGNN et sur un raisonnement pharmacologique général, et non sur des données cliniques ou bibliographiques. La similarité avec l'indication d'origine n'a pas pu être évaluée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62469022 | LEVOTONINE, gélule (PANPHARMA) | Gélule | Non renseignée (AMM active) |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 17 interactions sont recensées (source : DDInter).
  - **Majeures (10)** : lorcasérine, dolasétron, palonosétron, ondansétron, fenfluramine, granisétron, sibutramine, bleu de méthylène, doxépine (y compris sa forme topique) et procarbazine. Beaucoup concernent des agents sérotoninergiques, avec un risque de syndrome sérotoninergique.
  - **Modérées (7)** : morphine, codéine, hydrocodone, cyproheptadine, ozanimod et ifosfamide.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction (score de 0,9989) n'est étayée par aucun essai clinique ni aucune publication (niveau L5). Ses indications sont vides, et les données de sécurité propres au produit sont manquantes alors que les interactions médicamenteuses sont nombreuses.

<!-- review:begin fr-lic-20261106-oxitriptan-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « L'unique AMM française est annulée et ses indications sont vides, et les données de sécurité propres au produit sont manquantes alors que les interactions médicamenteuses sont nombreuses. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-oxitriptan-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Obtenir les données sur le mécanisme d'action (par exemple via DrugBank)
- Rechercher et évaluer les essais cliniques et publications sur l'oxitriptan dans l'insomnie
- Documenter l'indication d'origine et la similarité avec la nouvelle indication
- Examiner en détail le risque de syndrome sérotoninergique et les interactions majeures
- Évaluer la compatibilité des voies d'administration

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « L'unique AMM française est annulée et s » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

