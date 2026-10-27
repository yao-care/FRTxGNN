---
layout: default
title: Mepolizumab
parent: Preuves modérées (L3-L4)
nav_order: 479
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Mepolizumab : nouvelle indication prédite, Thrombopénie due à une destruction immunitaire (niveau de preuve L4). Indication d'origine : Pneumonie à éosinophiles"
monitor_inn: "mepolizumab"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets", "pseudo-von Willebrand disease", "autoimmune thrombocytopenic", "Glanzmann thrombasthenia"]
---

# Mepolizumab
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **5** 
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

## Mépolizumab : De la pneumonie à éosinophiles à la thrombopénie d'origine immunitaire
{: .text-alpha }

## Résumé en Une Phrase

Le mépolizumab (NUCALA) est un anticorps monoclonal anti-IL-5, initialement associé à la pneumonie à éosinophiles et à l'éosinophilie pulmonaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **thrombopénie due à une destruction immunitaire**,
mais cette prédiction ne s'appuie actuellement que sur **1 publication** (un rapport de cas) et **aucun essai clinique**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Pneumonie à éosinophiles ; éosinophilie pulmonaire (issues du graphe de connaissances, aucun texte d'indication dans les AMM) |
| Nouvelle Indication Prédite | Thrombopénie due à une destruction immunitaire |
| Score de Prédiction TxGNN | 99,66 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le mépolizumab est un anticorps monoclonal anti-IL-5 qui réduit le nombre d'éosinophiles. Son efficacité a été étudiée dans les pathologies à éosinophiles, ce qui correspond à son indication d'origine.

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
| 66719612 | NUCALA 100 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée (AMM annulée) |
| 63236206 | NUCALA 100 mg, solution injectable en stylo prérempli | Solution injectable | Non renseignée (AMM annulée) |
| 67361794 | NUCALA 40 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée (AMM annulée) |
| 65864619 | NUCALA 100 mg, poudre pour solution injectable | Poudre pour solution injectable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été identifiée dans les données compilées pour ce rapport.

## Autres Prédictions Examinées

| Rang | Maladie prédite | Score TxGNN | Niveau de Preuve | Commentaire |
|------|------|------|------|------|
| 2 | Trouble de la libération plaquettaire primaire | 99,61 % | L4 | Une seule revue sur le syndrome hyperéosinophilique ; aucun lien mécanistique direct |
| 3 | Pseudo-maladie de von Willebrand | 99,44 % | L5 | Défaut génétique de GP1BA ; aucun lien avec l'IL-5 |
| 4 | Thrombopénie auto-immune | 99,33 % | L5 | Voies IL-5/éosinophiles non établies ; chevauche la prédiction n° 1 |
| 5 | Thrombasthénie de Glanzmann | 99,28 % | L5 | Défaut de l'intégrine αIIbβ3 ; probable faux positif |

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose sur un score computationnel élevé et sur un seul rapport de cas confondu par des traitements associés, sans aucun essai clinique. De plus, toutes les AMM françaises du produit sont annulées et les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice ANSM (mises en garde et contre-indications), indispensable avant tout examen de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Études précliniques ou observationnelles sur le rôle de l'IL-5 et des éosinophiles dans la thrombopénie immunitaire
- Clarification du statut réglementaire actuel du produit en France (AMM annulées)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

