---
layout: default
title: Flucytosine
parent: Prédiction du modèle uniquement (L5)
nav_order: 332
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Flucytosine : nouvelle indication prédite, Maladie osseuse de Paget (bone Paget disease) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées"
monitor_inn: "FLUCYTOSINE"
predicted_indications: ["bone Paget disease"]
---

# Flucytosine
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

## Flucytosine : De l'antifongique à la Maladie osseuse de Paget (bone Paget disease)
{: .text-alpha }

## Résumé en Une Phrase

La flucytosine est un antimycosique de la famille des pyrimidines fluorées, commercialisée en France sous le nom d'Ancotil.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie osseuse de Paget**,
mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette prédiction, qui repose uniquement sur le score du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Maladie osseuse de Paget (bone Paget disease) |
| Score de Prédiction TxGNN | 99,04 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances générales, la flucytosine est un antimycosique qui est converti par la cytosine désaminase des champignons en 5-fluorouracile, lequel perturbe la synthèse de l'ARN et de l'ADN fongiques.

La maladie osseuse de Paget est un trouble du remodelage osseux lié à une dérégulation de l'activité des ostéoclastes (souvent associée à des variants de SQSTM1). Les cellules humaines étant largement dépourvues de cytosine désaminase, **aucun lien mécanistique évident** n'apparaît entre le mode d'action de la flucytosine et cette maladie.

Le score élevé du modèle (0,990) correspond à un lien purement computationnel issu d'un graphe de connaissances. Il pourrait refléter des artefacts de proximité dans le réseau plutôt qu'une véritable pharmacologie. Cette prédiction doit donc être considérée avec une grande prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67250203 | ANCOTIL 1 POUR CENT, solution pour perfusion (VIATRIS MEDICAL) – annulée | Solution pour perfusion | Non renseignée |
| 68758674 | ANCOTIL 500 mg, comprimé (VIATRIS MEDICAL) – annulée | Comprimé | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie du graphe PrimeKG, et non texte de la notice) : maladie rénale, maladie hépatique, maladie de la vésicule biliaire, pyo-uretère, déficit en potassium, thrombopénie, leucopénie, agranulocytose, neutropénie (y compris formes congénitales et idiopathiques de l'adulte), syndrome de Kostmann, hématopoïèse cyclique, anémie aplasique (acquise et autres formes).
- **Interactions médicamenteuses** : 85 interactions recensées. Principales :
  - **Majeure** : déférasirox n'est pas concerné ; la déféripone présente une interaction de niveau **majeur**.
  - **Modérée** : amphotéricine B (formes conventionnelle, lipidique, liposomale et sulfate de cholestéryle), mésalazine, balsalazide, olsalazine, sulfasalazine, vancomycine, kanamycine, néomycine, streptomycine, polymyxine B, bacitracine, déférasirox, pentamidine, ibuprofène, iobenguane (I-131), chlorure de strontium Sr-89.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible. De plus, les AMM françaises sont toutes annulées et le profil hématologique, rénal et hépatique du médicament appelle à la prudence.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank) et hypothèse biologique reliant la flucytosine à la maladie de Paget
- Notice officielle de l'ANSM (mises en garde et contre-indications), indispensable avant tout examen de sécurité
- Études précliniques ou revue de la littérature apportant un premier signal d'efficacité
- Clarification de l'indication d'origine et de la situation réglementaire actuelle (AMM annulées)
- Évaluation de la compatibilité des voies d'administration pour la nouvelle indication
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

