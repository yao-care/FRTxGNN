---
layout: default
title: Tolcapone
parent: Prédiction du modèle uniquement (L5)
nav_order: 771
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "TOLCAPONE"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "transaldolase deficiency", "fructose-1,6-bisphosphatase deficiency", "Lewy body dementia", "X-linked intellectual disability-ataxia-apraxia syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "X-linked intellectual disability-cerebellar hypoplasia syndrome", "paralysis agitans, juvenile, of Hunt"]
description: "Tolcapone : nouvelle indication prédite, Encéphalite subaiguë de Rasmussen (Rasmussen subacute encephalitis) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Tolcapone
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

## Tolcapone: Encéphalite subaiguë de Rasmussen (Rasmussen subacute encephalitis)
{: .text-alpha }

## Résumé en Une Phrase

Tolcapone est un inhibiteur de la COMT (catéchol-O-méthyltransférase), initialement utilisé dans le traitement de la **maladie de Parkinson**.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**encéphalite subaiguë de Rasmussen**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Encéphalite subaiguë de Rasmussen (Rasmussen subacute encephalitis) |
| Score de Prédiction TxGNN | 0.9993 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, tolcapone est un inhibiteur de la COMT, enzyme qui dégrade les catécholamines dont la lévodopa. Son efficacité dans la maladie de Parkinson repose sur le prolongement de l'action de la dopamine.

Pour l'encéphalite de Rasmussen, aucun lien mécanistique n'est étayé. Cette maladie est une encéphalite focale chronique à médiation immunitaire, et l'inhibition de la COMT n'y a pas de rôle établi. Le score élevé du modèle reflète une prédiction computationnelle, non une preuve biologique ou clinique.

Il convient de noter que d'autres candidats de la liste de prédictions sont plus plausibles sur le plan biologique, notamment la **démence à corps de Lewy** (rang 6), qui partage avec la maladie de Parkinson le dysfonctionnement dopaminergique et la pathologie de l'α-synucléine, ainsi que le **parkinsonisme juvénile de Hunt** (rang 10), terme historique qui recoupe probablement les indications parkinsoniennes déjà connues plutôt qu'un véritable signal de repositionnement.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'encéphalite de Rasmussen.

À titre informatif, une seule publication a été retrouvée pour un autre candidat (démence à corps de Lewy) : il s'agit d'un modèle préclinique in vitro, sans valeur de preuve clinique pour tolcapone.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | Préclinique (organoïdes dérivés d'iPSC) | Science Advances | Modélisation de la maladie à corps de Lewy avec des organoïdes corticaux porteurs d'une triplication de SNCA et identification de médicaments thérapeutiques candidats |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67077388 | TASMAR 100 mg, comprimé pelliculé (VIATRIS HEALTHCARE, Irlande) | Comprimé pelliculé | Non renseignée (AMM active) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie du foie, maladie de la vésicule biliaire, mélanome, troubles hypotensifs, rhabdomyolyse, fasciite nodulaire, dyskinésie tardive, dyskinésie linguo-faciale-buccale.
- **Hépatotoxicité** : elle est à l'origine de l'usage restreint du médicament et doit être prise en compte dans toute étude ultérieure.
- **Interactions médicamenteuses** : 65 interactions recensées. Principales :
  - **Majeure** : bleu de méthylène.
  - **Modérées** : épinéphrine (y compris ophtalmique et topique), morphine (y compris liposomale), codéine, opium, dronabinol, nabilone, naltrexone, métoclopramide, prométhazine, chlorphéniramine, cétirizine, dextrométhorphane, éthanol.
  - **Mineures** : warfarine, dicoumarol.
  - **Niveau inconnu** : oméprazole.

Les mises en garde et contre-indications issues de la notice n'ont pas pu être obtenues ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, sans lien mécanistique plausible, et le produit n'est plus commercialisé en France (AMM annulée) avec un risque hépatique connu.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications), qui bloque actuellement le criblage de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (via DrugBank).
- Justifier un rationnel biologique reliant l'inhibition de la COMT à l'encéphalite de Rasmussen, ou réorienter l'évaluation vers un candidat plus plausible, comme la démence à corps de Lewy.
- Réaliser une revue de la littérature ciblée et évaluer le rapport bénéfice/risque hépatique avant toute étude.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

