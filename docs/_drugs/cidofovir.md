---
layout: default
title: Cidofovir
parent: Prédiction du modèle uniquement (L5)
nav_order: 168
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Cidofovir : nouvelle indication prédite, Cholangite sclérosante (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
---

# Cidofovir
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

# Cidofovir : D'une indication non renseignée à la Cholangite sclérosante

## Résumé en Une Phrase

Cidofovir est un analogue nucléotidique antiviral (inhibiteur de l'ADN polymérase) ; l'indication originale n'est pas renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **cholangite sclérosante**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.
La prédiction repose uniquement sur le modèle (niveau de preuve L5).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Cholangite sclérosante |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le cidofovir est un analogue nucléotidique inhibiteur de l'ADN polymérase virale, actif contre des virus à ADN (CMV, adénovirus, HPV). Son indication d'origine n'étant pas renseignée dans les données d'AMM, la relation avec la nouvelle indication ne peut pas être établie à partir de ces données.

Le lien mécanistique avec la cholangite sclérosante n'est pas étayé. Une connexion théorique ténue existe via les cholangiopathies associées au SIDA ou à une infection virale (CMV), mais elle n'est démontrée par aucune donnée fournie. Le score élevé (0,999) est une prédiction de modèle et doit être interprété avec prudence.

Les autres indications prédites sont encore moins soutenues :
- **Polyarthrite rhumatoïde** (score 99,82 %) : 5 publications ont été retrouvées, mais elles concernent le léflunomide dans l'infection à CMV après greffe, la toxicité rétinienne des médicaments et des verrues virales. Elles résultent probablement d'une association par mots-clés et ne prouvent pas que le cidofovir traite la polyarthrite rhumatoïde.
- **Syndrome de microphtalmie colobomateuse-dysplasie rhizomélique** (99,62 %) et **syndrome de brachydactylie-syndactylie** (99,49 %) : aucune justification mécanistique ; il s'agit vraisemblablement d'artefacts du graphe de connaissances.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la cholangite sclérosante.

Pour la polyarthrite rhumatoïde (indication classée 2e), les publications retrouvées ne sont pas pertinentes pour l'efficacité du cidofovir :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31054984](https://pubmed.ncbi.nlm.nih.gov/31054984/) | 2019 | Cohorte/série de cas | Biol Blood Marrow Transplant | Léflunomide dans l'infection à CMV après greffe allogénique de cellules souches |
| [15489872](https://pubmed.ncbi.nlm.nih.gov/15489872/) | 2004 | Rapport de cas | Bone Marrow Transplant | Léflunomide dans une infection à CMV réfractaire après greffe de moelle |
| [16688677](https://pubmed.ncbi.nlm.nih.gov/16688677/) | 2006 | Rapport de cas | Klin Padiatr | Foscarnet + léflunomide dans l'infection à CMV réfractaire après greffe |
| [30888954](https://pubmed.ncbi.nlm.nih.gov/30888954/) | 2019 | Rapport de cas | Skinmed | Radiothérapie et hyperthermie dans des verrues vulgaires récalcitrantes |
| [15155152](https://pubmed.ncbi.nlm.nih.gov/15155152/) | 2004 | Revue | Expert Opin Drug Saf | Toxicité rétinienne des médicaments |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67633828 | CIDOFOVIR TILLOMED 75 mg/mL solution à diluer pour perfusion (Tillomed Pharma, Allemagne) | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |

## Cytotoxicité

Le cidofovir est un antiviral et non un antinéoplasique ; cette section n'est pas applicable.

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : maladie rénale, pyourètre, trouble acidosique, acidose lactique acquise.
- **Interactions médicamenteuses** : 55 interactions recensées. Parmi les principales, de niveau **majeur** :
  - Amphotéricine B (y compris formes lipidique, sulfate de cholestéryle et liposomale)
  - Aminosides et apparentés : kanamycine, néomycine, streptomycine
  - Polymyxine B, vancomycine
  - Dérivés de la mésalazine : mésalazine, balsalazide, olsalazine, sulfasalazine
  - Déférasirox, déféroxamine
  - Produits de contraste et radiopharmaceutiques iodés : diatrizoate, iodipamide, iobenguane (I-131)
  - De niveau **modéré** : exénatide, trospium

Ces interactions évoquent surtout un risque additif de néphrotoxicité, point à vérifier dans la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication pertinente. Le lien mécanistique est non démontré, les données de sécurité de la notice sont manquantes (lacune bloquante) et la seule AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), lacune bloquante pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Clarifier l'indication originale et la raison de l'annulation de l'AMM
- Rechercher des études précliniques ou observationnelles reliant le cidofovir à la cholangite sclérosante (par ex. cholangiopathie virale/CMV)
- Évaluer la compatibilité de la voie d'administration et le risque de néphrotoxicité, compte tenu des contre-indications rénales issues du graphe de connaissances
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

