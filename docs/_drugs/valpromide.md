---
layout: default
title: Valpromide
parent: Prédiction du modèle uniquement (L5)
nav_order: 802
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "VALPROMIDE"
predicted_indications: ["insomnia (disease)"]
description: "Valpromide : nouvelle indication prédite, Insomnie (insomnia (disease)) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Valpromide
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

## Valpromide: Insomnie (insomnia (disease))
{: .text-alpha }

## Résumé en Une Phrase

Valpromide est un dérivé amide de l'acide valproïque, commercialisé en France sous le nom de Depamide. Son indication d'origine n'est pas renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**insomnie**, mais seule **1 publication** (une série de cas de 1999) et **aucun essai clinique** soutiennent actuellement cette direction.

<!-- review:begin fr-lic-20261106-valpromide-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Valpromide est un dérivé amide de l'acide valproïque, commercialisé en France sous le nom de Depamide (autorisation aujourd'hui annulée). » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-valpromide-1 -->

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Insomnie (insomnia (disease)) |
| Score de Prédiction TxGNN | 0.9979 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

*Remarque sur le niveau de preuve : selon la grille de lecture, une simple série de cas relèverait plutôt du niveau L3 (observationnel) ou L5 (prédiction seule). Le niveau L4 retenu dans les données compilées est conservé ici, par prudence, car la seule publication disponible est très limitée.*

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, valpromide est un dérivé amide de l'acide valproïque (valproate), un anticonvulsivant. Son efficacité dans son indication d'origine n'est pas documentée dans les données disponibles.

Par analogie avec le valproate, deux mécanismes sont plausibles : le renforcement de la transmission GABAergique (inhibition de la GABA transaminase, augmentation de la disponibilité du GABA) et la modulation des canaux sodiques voltage-dépendants. Ces effets pourraient théoriquement réduire l'hyperexcitabilité neuronale et favoriser le sommeil.

Ce lien est toutefois déduit d'un composé apparenté et n'a pas été démontré pour valpromide dans l'insomnie. Le score très élevé de TxGNN (0,9979) est une prédiction informatique, et non une preuve clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [10370890](https://pubmed.ncbi.nlm.nih.gov/10370890/) | 1999 | Série de cas | L'Encéphale | Huit cas de patients déments présentant agitation, agressivité et insomnie avec anxiété généralisée. Les anticonvulsivants (valpromide et carbamazépine) sont évoqués comme alternative aux neuroleptiques, dont l'usage est souvent compliqué par somnolence et confusion. |

Cette publication porte sur l'agitation et les troubles du comportement dans la démence ; l'insomnie n'y est qu'un symptôme associé. Elle ne constitue donc pas une preuve directe dans l'insomnie primaire.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63737879 (annulée) | DEPAMIDE 300 mg, comprimé pelliculé gastro-résistant (SANOFI WINTHROP INDUSTRIE) | Comprimé pelliculé gastro-résistant | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un score de modèle élevé, mais les preuves réelles se limitent à une série de cas ancienne, indirecte et sans essai clinique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le dépistage de sécurité)
- Obtenir les données sur le mécanisme d'action de valpromide (par exemple via DrugBank)
- Clarifier l'indication d'origine historique de Depamide
- Rechercher des études cliniques spécifiques à l'insomnie (essais contrôlés, polysomnographie)
- Évaluer la compatibilité des voies d'administration et la similarité avec l'indication d'origine

<!-- review:begin fr-lic-20261106-valpromide-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarifier l'indication d'origine historique de Depamide et les raisons de l'annulation de l'AMM » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-valpromide-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « (autorisation aujourd'hui annulée) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « et les raisons de l'annulation de l'AMM » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

