---
layout: default
title: Mepolizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 479
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-12
monitor_inn: "mepolizumab"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets", "pseudo-von Willebrand disease", "autoimmune thrombocytopenic", "Glanzmann thrombasthenia"]
description: "Mepolizumab : nouvelle indication prédite, Thrombopénie due à une destruction immunitaire (thrombocytopenia due to immune destruction) (niveau de preuve L5). Indication d'origine : Non renseignée dan…"
---

# Mepolizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

## Mepolizumab: Thrombopénie due à une destruction immunitaire (thrombocytopenia due to immune destruction)
{: .text-alpha }

## Résumé en Une Phrase

Le mépolizumab (NUCALA) est un anticorps monoclonal anti-IL-5, initialement associé à la pneumonie à éosinophiles et à l'éosinophilie pulmonaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **thrombopénie due à une destruction immunitaire**,
mais cette prédiction ne s'appuie actuellement que sur **1 publication** (un rapport de cas) et **aucun essai clinique**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Thrombopénie due à une destruction immunitaire (thrombocytopenia due to immune destruction) |
| Score de Prédiction TxGNN | 0.9966 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Mepolizumab (traduction non officielle) : « Le mépolizumab est un antagoniste de l'IL-5 (IgG1 kappa). L'IL-5 est la principale cytokine responsable de la croissance et de la différenciation, du recrutement, de l'activation et de la survie des éosinophiles. Le mépolizumab se lie à l'IL-5 avec une constante de dissociation de 100 pM, inhibant l'activité biologique de l'IL-5 en bloquant sa liaison à la chaîne alpha du complexe récepteur de l'IL-5 exprimé à la surface des éosinophiles. » Texte original en anglais : "Mepolizumab is an IL-5 antagonist (IgG1 kappa). IL-5 is the major cytokine responsible for the growth and differentiation, recruitment, activation, and survival of eosinophils. Mepolizumab binds to IL-5 with a dissociation constant of 100 pM, inhibiting the bioactivity of IL-5 by blocking its binding to the alpha chain of the IL-5 receptor complex expressed on the eosinophil cell surface." ([DailyMed: Nucala (mepolizumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fefb887c-e4ac-431e-8893-e9d1a5a63fea), version du 2025-08-06 ; consulté le 2026-11-19). Sur la base des informations connues, le mépolizumab est un anticorps monoclonal anti-IL-5 qui réduit le nombre d'éosinophiles. Son efficacité a été étudiée dans les pathologies à éosinophiles, ce qui correspond à son indication d'origine.

Le lien avec la thrombopénie immunitaire est indirect : une dysrégulation immunitaire liée aux éosinophiles pourrait contribuer à la destruction des plaquettes dans certains contextes d'hyperéosinophilie ou de résistance aux corticoïdes. La seule publication disponible décrit un cas d'hyperéosinophilie résistante aux corticoïdes ayant régressé sous mépolizumab, avec une amélioration d'une microangiopathie thrombotique mixte.

Cette observation ne démontre pas une efficacité dans la thrombopénie immunitaire primaire, et le traitement concomitant constitue un facteur de confusion. Le score élevé de TxGNN reste une prédiction purement computationnelle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Rapport de cas | Blood Cells Mol Dis | Résolution d'un syndrome immunitaire hyperéosinophilique résistant aux corticoïdes sous mépolizumab, avec amélioration concomitante d'une microangiopathie thrombotique mixte (traitements associés) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66719612 | NUCALA 100 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée (AMM active) |
| 63236206 | NUCALA 100 mg, solution injectable en stylo prérempli | Solution injectable | Non renseignée (AMM active) |
| 67361794 | NUCALA 40 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée (AMM active) |
| 65864619 | NUCALA 100 mg, poudre pour solution injectable | Poudre pour solution injectable | Non renseignée (AMM active) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été identifiée dans les données compilées pour ce rapport.

## Autres Prédictions Examinées

| Rang | Maladie prédite | Score TxGNN | Niveau de Preuve | Commentaire |
|------|------|------|------|------|
| 2 | Trouble de la libération plaquettaire primaire | 0,9961 | L5 | Une seule revue sur le syndrome hyperéosinophilique ; aucun lien mécanistique direct |
| 3 | Pseudo-maladie de von Willebrand | 0,9944 | L5 | Défaut génétique de GP1BA ; aucun lien avec l'IL-5 |
| 4 | Thrombopénie auto-immune | 0,9933 | L5 | Voies IL-5/éosinophiles non établies ; chevauche la prédiction n° 1 |
| 5 | Thrombasthénie de Glanzmann | 0,9928 | L5 | Défaut de l'intégrine αIIbβ3 ; probable faux positif |

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose sur un score computationnel élevé et sur un seul rapport de cas confondu par des traitements associés, sans aucun essai clinique. De plus, les 4 AMM françaises du produit sur 4 sont valides, mais les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice ANSM (mises en garde et contre-indications), indispensable avant tout examen de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Études précliniques ou observationnelles sur le rôle de l'IL-5 et des éosinophiles dans la thrombopénie immunitaire
- Clarification du statut réglementaire actuel du produit en France

<!-- review:begin fr-lic-20261106-mepolizumab-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarification du statut réglementaire actuel du produit en France (AMM annulées) » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 4 AMM pour ce médicament, dont 4 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-mepolizumab-1 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « (AMM annulées) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Nucala (mepolizumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fefb887c-e4ac-431e-8893-e9d1a5a63fea) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

