---
layout: default
title: Ciclesonide
parent: Prédiction du modèle uniquement (L5)
nav_order: 167
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Ciclesonide : nouvelle indication prédite, Eczéma atopique (niveau de preuve L5). Indication d'origine : Asthme, asthme allergique, rhinite allergique"
monitor_inn: "ciclesonide"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis", "asthma-related traits, susceptibility to"]
---

# Ciclesonide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Ciclésonide : De l'asthme à l'eczéma atopique

## Résumé en Une Phrase

Le ciclésonide est un corticoïde inhalé, initialement utilisé pour le traitement de l'asthme et de la rhinite allergique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**eczéma atopique**, mais **aucun essai clinique** ni **aucune publication** directement liée à cette indication ne soutient actuellement cette prédiction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Asthme, asthme allergique, rhinite allergique (d'après le graphe de connaissances ; le texte de l'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Eczéma atopique |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Retiré du marché (AMM annulées uniquement) |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le ciclésonide est une prodrogue corticoïde inhalée, activée par des estérases en désisobutyryl-ciclésonide, un agoniste du récepteur des glucocorticoïdes à activité anti-inflammatoire.

Les corticoïdes topiques ou systémiques sont un traitement établi de l'eczéma atopique. L'action anti-inflammatoire du ciclésonide dans les maladies allergiques des voies respiratoires (asthme, rhinite allergique) est donc mécanistiquement cohérente avec une application à une dermatose inflammatoire atopique.

Une réserve importante : le ciclésonide est formulé pour l'inhalation, il n'est pas commercialisé pour un usage dermatologique et ses AMM sont toutes annulées. Une nouvelle formulation serait nécessaire. La compatibilité des voies d'administration n'a pas encore été évaluée. Par ailleurs, les entrées « eczéma atopique » et « dermatite atopique » (rang 3) désignent le même concept et devraient être fusionnées.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'eczéma atopique.

À titre indicatif, pour d'autres indications prédites :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Revue (lignes directrices) | Basic & Clinical Pharmacology & Toxicology | Lignes directrices finlandaises sur le diagnostic et le traitement de la BPCO stable ; preuve indirecte pour la bronchite, sans données spécifiques au ciclésonide |
| [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/) | 2012 | Rapport de cas | Contact Dermatitis | Dermatite allergique systémique due au budésonide inhalé, avec réactivité croisée au ciclésonide aux tests épicutanés ; signal de sécurité, non d'efficacité |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63599556 | ALVESCO 80 microgrammes/dose, solution pour inhalation en flacon pressurisé | Solution pour inhalation | Non renseignée (AMM annulée) |
| 66052179 | ALVESCO 160 microgrammes/dose, solution pour inhalation en flacon pressurisé | Solution pour inhalation | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de notice) : kératite herpétique, insuffisance surrénalienne, maladie d'Addison, ostéoporose (dont post-ménopausique), infections fongiques, dermatophytose, hypertension oculaire, glaucome, infections parasitaires.
- **Interactions médicamenteuses** : 63 interactions recensées. Principales :
  - **Majeure** : cladribine.
  - **Modérée** : clarithromycine, miconazole, cobicistat, atazanavir, fosamprénavir, amprénavir, bocéprévir, cératinib (ceritinib), conivaptan, fostamatinib, insuline humaine inhalée, abamétapir (topique). Plusieurs sont des inhibiteurs du CYP3A4, susceptibles d'augmenter l'exposition systémique au corticoïde.
  - **Mineure** : formotérol, salbutamol, arformotérol.
- **Alerte de sécurité** : le rapport de cas (PMID 22957490) signale un risque d'hypersensibilité et de réactivité croisée entre corticoïdes, pertinent pour un usage dermatologique.

Les mises en garde et contre-indications de la notice ne sont pas disponibles ; veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé (99,96 %), mais il n'existe aucun essai clinique ni publication pour l'eczéma atopique (niveau L5). Le produit n'est plus commercialisé en France et sa forme inhalée n'est pas adaptée à l'usage dermatologique.
- Les données de sécurité de la notice, nécessaires au criblage de sécurité, sont manquantes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications).
- Obtenir les données sur le mécanisme d'action depuis DrugBank.
- Réaliser une revue de la littérature ciblée sur le ciclésonide dans l'eczéma atopique, et comparer avec les corticoïdes topiques déjà autorisés.
- Évaluer la faisabilité d'une formulation adaptée (voie cutanée) et la compatibilité des voies d'administration.
- Fusionner les entrées « eczéma atopique » et « dermatite atopique » pour la revue suivante.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

