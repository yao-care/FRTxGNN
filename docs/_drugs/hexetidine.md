---
layout: default
title: Hexetidine
parent: Prédiction du modèle uniquement (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Hexetidine : nouvelle indication prédite, Anévrisme du septum interventriculaire (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM (antiseptique buccal local)"
monitor_inn: "hexetidine"
predicted_indications: ["interventricular septum aneurysm", "pulmonary valve disease", "orofacial clefting syndrome", "Laubry-Pezzi syndrome", "genetic syndromic Pierre Robin syndrome", "disorder of fucoglycosan synthesis", "partial deletion of the long arm of chromosome 22", "Pierre Robin syndrome associated with a chromosomal anomaly", "partial deletion of the long arm of chromosome 7", "Jeune syndrome situs inversus"]
---

# Hexetidine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Hexétidine : D'un antiseptique buccal à l'anévrisme du septum interventriculaire

## Résumé en Une Phrase

L'hexétidine est un antiseptique local utilisé en bain de bouche et en pâte dentifrice pour l'hygiène buccale. L'indication d'origine n'est pas renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**anévrisme du septum interventriculaire**, mais **aucun essai clinique** et **aucune publication** pertinente ne soutiennent cette prédiction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM (antiseptique buccal local) |
| Nouvelle Indication Prédite | Anévrisme du septum interventriculaire |
| Score de Prédiction TxGNN | 99,16 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Uniquement des AMM annulées |
| Nombre d'AMM | 7 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'hexétidine est un antiseptique/antimicrobien à usage local (bain de bouche, pâte dentifrice), destiné à l'hygiène buccale.

**Cette prédiction n'apparaît pas plausible sur le plan biologique.** L'anévrisme du septum interventriculaire est une anomalie structurelle du cœur, alors que l'hexétidine agit localement dans la cavité buccale. Aucun lien mécanistique crédible n'a été identifié : le score élevé semble être un artefact de la prédiction fondée sur le graphe de connaissances.

Les autres prédictions du modèle (valvulopathie pulmonaire, fente orofaciale, syndrome de Laubry-Pezzi, syndrome de Pierre Robin, délétions chromosomiques, etc.) présentent la même absence de justification pharmacologique. Elles sont toutes au niveau L5, sans essai clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'anévrisme du septum interventriculaire.

À titre indicatif, une seule publication a été retrouvée pour une autre prédiction du modèle (trouble de la synthèse des fucoglycanes). Il s'agit d'une revue générale sur les agents antiplaque, sans lien avec cette maladie :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [12974527](https://pubmed.ncbi.nlm.nih.gov/12974527/) | 2003 | Revue | Oral Diseases | Revue des agents antiplaque dans la prévention des maladies buccales liées au biofilm (caries, maladies parodontales) ; usage en hygiène buccale, sans rapport avec l'indication prédite |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62906059 | Hexetidine Biogaran Conseil 0,1 % | Solution pour bain de bouche | Non renseignée (AMM annulée) |
| 67768847 | Hextril Menthe 0,1 pour cent | Solution pour bain de bouche | Non renseignée (AMM annulée) |
| 61455112 | Hexetidine EG Labo Conseil 0,1 % | Solution pour bain de bouche | Non renseignée (AMM annulée) |
| 67376038 | Hextril 0,1 pour cent | Bain de bouche, flacon | Non renseignée (AMM annulée) |
| 66929112 | Hexetidine Viatris Conseil 0,1 % | Solution pour bain de bouche | Non renseignée (AMM annulée) |

Deux autres AMM annulées existent au total (7 au total), dont Hextril 0,1 pour cent en pâte dentifrice et Hexetidine Teva Conseil 0,1 %.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication pertinente, et sans lien mécanistique plausible entre un antiseptique buccal local et une anomalie structurelle cardiaque.
- Toutes les AMM françaises sont annulées et les données de sécurité de la notice sont absentes, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice de l'ANSM (mises en garde et contre-indications)
- Données détaillées sur le mécanisme d'action (DrugBank)
- Démonstration d'un lien biologique plausible et d'une compatibilité de voie d'administration (usage local vs systémique) avant toute étude préclinique
- Éventuellement, examen d'indications plus cohérentes avec le profil antiseptique buccal du médicament
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

