---
layout: default
title: Clotiazepam
parent: Prédiction du modèle uniquement (L5)
nav_order: 190
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Clotiazepam : nouvelle indication prédite, Insomnie (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "clotiazepam"
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium"]
---

# Clotiazepam
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Clotiazépam : Du Statut d'Anxiolytique (Indication Non Renseignée) à l'Insomnie
{: .text-alpha }

## Résumé en Une Phrase

Clotiazépam est une thiénodiazépine, de la classe des benzodiazépines, commercialisée en France sous le nom VERATRAN, dont l'indication originale n'est pas renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**insomnie**,
mais **aucun essai clinique** n'est enregistré et **1 publication** de portée générale (revue sur la pharmacocinétique des anxiolytiques) est disponible.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Insomnie |
| Score de Prédiction TxGNN | 0,9989 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le clotiazépam fait partie de la classe des benzodiazépines (thiénodiazépine) et agit comme modulateur allostérique positif des récepteurs GABA-A. Ce renforcement de l'inhibition GABAergique produit des effets sédatifs et hypnotiques, ce qui constitue un mécanisme biologiquement plausible pour l'insomnie.

Cette lecture repose sur la connaissance de la classe pharmacologique et non sur le dossier propre au médicament. Le score TxGNN est très élevé (0,9989), mais il s'agit d'une prédiction de modèle, et non d'une preuve clinique.

Une seconde indication prédite, le **delirium de sevrage alcoolique** (score 0,9933), est également plausible par effet de classe : les benzodiazépines compensent la perte de la potentialisation GABA-A induite par l'alcool. Elle ne repose toutefois sur aucune donnée spécifique au clotiazépam (niveau L5, aucun essai ni publication).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Revue | Expert Opin Drug Metab Toxicol | Revue de la pharmacocinétique des médicaments anxiolytiques, rappelant que les troubles anxieux sont les plus fréquents des troubles mentaux et que les anxiolytiques figurent parmi les psychotropes les plus prescrits. Elle ne porte pas spécifiquement sur le clotiazépam dans l'insomnie. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65558647 | VERATRAN 5 mg, comprimé | Comprimé | Non renseignée (AMM active) |
| 68771419 | VERATRAN 10 mg, comprimé sécable | Comprimé sécable | Non renseignée (AMM active) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le soutien repose essentiellement sur la prédiction du modèle et sur l'effet de classe des benzodiazépines : aucun essai clinique et une seule revue générale sont disponibles (niveau L4).
- Les données de sécurité sont absentes, ce qui empêche toute évaluation de sécurité préalable.

<!-- review:begin fr-lic-20261106-clotiazepam-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les deux AMM françaises sont annulées et les données de sécurité sont absentes, ce qui empêche toute évaluation de sécurité préalable. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 2 AMM pour ce médicament, dont 2 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-clotiazepam-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications), élément bloquant pour l'évaluation de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Rechercher des études cliniques ou observationnelles spécifiques au clotiazépam dans l'insomnie
- Évaluer les risques propres à la classe des benzodiazépines (dépendance, sédation, usage prolongé) et la compatibilité des voies d'administration

<!-- review:begin fr-lic-20261106-clotiazepam-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Rechercher des études cliniques ou observationnelles spécifiques au clotiazépam dans l'insomnie / Clarifier les raisons de l'annulation des AMM et l'indication originale autorisée » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 2 AMM pour ce médicament, dont 2 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-clotiazepam-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « es deux AMM françaises sont annulées et l » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « Clarifier les raisons de l'annulation des AMM et l'indication originale autorisée » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

