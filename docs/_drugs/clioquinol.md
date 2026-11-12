---
layout: default
title: Clioquinol
parent: Prédiction du modèle uniquement (L5)
nav_order: 180
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
monitor_inn: "CLIOQUINOL"
predicted_indications: ["ectothrix infectious disease", "endothrix infectious disease"]
description: "Clioquinol : nouvelle indication prédite, Ectothrix infectious disease (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Clioquinol
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

## Clioquinol: Ectothrix infectious disease
{: .text-alpha }

## Résumé en Une Phrase

Le clioquinol est une hydroxyquinoléine halogénée, initialement utilisée contre les dermatophyties cutanées (pied d'athlète, teigne du corps, atteinte de l'aine et de la région périanale).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **candidose cutanée**,
mais **aucun essai clinique** et seulement **1 publication**, ancienne et indirecte, soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Ectothrix infectious disease |
| Score de Prédiction TxGNN | 0.9926 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le clioquinol est une hydroxyquinoléine halogénée chélatrice de métaux (cuivre, zinc, fer), dotée d'une activité antifongique et antibactérienne. Son efficacité dans les dermatophyties est reconnue et, sur le plan mécanistique, il pourrait être applicable à la candidose cutanée.

La perturbation de l'homéostasie des métaux dans la cellule fongique pourrait s'étendre aux levures du genre *Candida*. Les dermatophyties et la candidose cutanée sont deux mycoses superficielles de la peau, ce qui rend l'extension plausible.

Cette hypothèse reste toutefois théorique : l'unique article retrouvé (1988, prévention de l'infection professionnelle à *Candida albicans* par des additifs de savons) est indirect, et son titre ne montre pas que le clioquinol ait été testé.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [2978600](https://pubmed.ncbi.nlm.nih.gov/2978600/) | 1988 | Rapport de santé préventive/professionnelle | Przeglad dermatologiczny | Étude *in vitro* d'additifs de savons de toilette sur des souches de *C. albicans* de patients ; effet fongicide en solution fortement alcaline. Le clioquinol n'est pas clairement évalué. |

Pour une autre indication prédite, la mycose superficielle, une étude préclinique de 2021 ([33772895](https://pubmed.ncbi.nlm.nih.gov/33772895/), *Mycoses*) a évalué l'association du clioquinol avec le ciclopirox et la terbinafine dans des modèles alternatifs de dermatophytose (activité et toxicité). Elle suggère une synergie antifongique, mais ne constitue pas une preuve d'efficacité clinique.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64835493 | TRUE TEST 36, patch pour test épicutané | Patch | Non renseignée (AMM active) |

Ce produit est un patch de test épicutané (diagnostic allergologique) fabriqué par SmartPractice Denmark, et non un antifongique thérapeutique.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance corticosurrénale, maladie d'Addison, atrophie cutanée, télangiectasies, maladies capillaires, maladie de Rendu-Osler, maladie vasculaire périphérique, claudication intermittente, artériopathie périphérique.
- **Autres points** : l'historique de sécurité du clioquinol (neurotoxicité en cas d'exposition systémique) impose la prudence. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

Veuillez consulter la notice pour les informations de sécurité complètes : les mises en garde et contre-indications officielles ne sont pas disponibles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est mécanistiquement plausible, mais elle ne repose que sur le modèle et sur une publication ancienne et indirecte, sans essai clinique.

<!-- review:begin fr-lic-20261106-clioquinol-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La prédiction est mécanistiquement plausible, mais elle ne repose que sur le modèle et sur une publication ancienne et indirecte, sans essai clinique. De plus, l'autorisation française est annulée et les données de sécurité officielles sont absentes. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-clioquinol-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) auprès de l'ANSM, étape bloquante pour le criblage de sécurité
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Générer des données *in vitro* directes sur les espèces de *Candida*, puis des données précliniques cutanées
- Vérifier la compatibilité de la voie d'administration (topique) et la faisabilité réglementaire
- Évaluer le risque de neurotoxicité et d'absorption systémique pour une formulation topique

<!-- review:begin fr-lic-20261106-clioquinol-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Vérifier la compatibilité de la voie d'administration (topique) et la faisabilité réglementaire, l'AMM étant annulée » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-clioquinol-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « De plus, l'autorisation française est annulée et les données de sécurité officielles sont absentes » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « l'AMM étant annulée » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

