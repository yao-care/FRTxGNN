---
layout: default
title: Tetrabenazine
parent: Prédiction du modèle uniquement (L5)
nav_order: 748
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tetrabenazine : nouvelle indication prédite, Maladie rénale polykystique de type 3 (avec ou sans maladie polykysti… (niveau de preuve L5). Indication d'origine : Maladie de Huntington"
---

# Tetrabenazine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Tétrabénazine : De la maladie de Huntington à la maladie rénale polykystique de type 3 (avec ou sans maladie polykystique du foie)

## Résumé en Une Phrase

La tétrabénazine est un médicament initialement utilisé pour traiter les mouvements anormaux de la maladie de Huntington et de syndromes apparentés.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie rénale polykystique de type 3 (avec ou sans maladie polykystique du foie)**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Huntington (et syndromes apparentés, selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Maladie rénale polykystique de type 3 (avec ou sans maladie polykystique du foie) |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (non commercialisé) |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, la tétrabénazine est un inhibiteur réversible du transporteur vésiculaire des monoamines de type 2 (VMAT2) : elle déplète les monoamines présynaptiques (dopamine notamment) et soulage ainsi de façon symptomatique les mouvements hyperkinétiques.

La relation entre l'indication originale (trouble moteur neurologique) et la nouvelle indication (maladie rénale/hépatique kystique d'origine génétique, de type ciliopathie) n'est pas évidente. Aucun lien mécanistique plausible entre l'inhibition de VMAT2 et la physiopathologie de la polykystose rénale n'a été identifié.

Le score élevé de TxGNN (99,90 %) reflète une proximité dans le graphe de connaissances, et non une preuve biologique ou clinique. Cette prédiction doit donc être considérée avec une grande prudence. Les autres prédictions du même classement (dysplasie rénale-hépatique-pancréatique, syndrome de Joubert avec atteinte rénale, néphrite interstitielle karyomégalique, etc.) présentent le même profil : niveau L5, sans essai ni publication pertinente.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour cette indication.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 64487229 | TETMODIS 25 mg, comprimé sécable | Comprimé sécable | Non renseignée | Annulée |
| 62463044 | XENAZINE 25 mg, comprimé sécable | Comprimé sécable | Non renseignée | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, hypotension orthostatique et troubles hypotensifs, syndrome du QT long (y compris familial) et torsades de pointes, troubles anxieux, troubles névrotiques et dysthymie, maladie hépatique, maladie de la vésicule biliaire, dyskinésie tardive et dyskinésie linguo-faciale-buccale, syndrome parkinsonien et maladie de Parkinson, akathisie induite par les médicaments, hyperprolactinémie (y compris familiale ou acquise) et tumeur hypophysaire sécrétant de la prolactine.
- **Interactions médicamenteuses** : 168 interactions recensées. Parmi les principales :
  - Majeures : bupropion, dolasétron, métoclopramide
  - Modérées : famotidine, lopéramide, morphine, lorcasérine, clarithromycine, lévofloxacine, dronabinol, éliglustat, palonosétron, nabilone, diphénoxylate, difénoxine, ainsi que plusieurs laxatifs/préparations de lavage intestinal (bisacodyl, acide picosulfurique, polyéthylène glycol avec électrolytes, sulfate de sodium)
  - Mineure : métronidazole

Veuillez consulter la notice pour les informations de sécurité détaillées (mises en garde et contre-indications officielles non disponibles dans les données compilées).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et aucun lien mécanistique plausible n'existe entre l'inhibition de VMAT2 et la polykystose rénale. De plus, le médicament n'a actuellement plus d'AMM valide en France, et son profil de sécurité (dépression, QT long, contre-indication en cas de maladie hépatique) est préoccupant.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (MOA) détaillé, afin d'évaluer un éventuel lien mécanistique
- Mises en garde et contre-indications officielles issues de la notice de l'ANSM
- Données précliniques (modèles de ciliopathie ou de polykystose) justifiant un intérêt biologique
- Clarification du statut réglementaire (AMM annulées) et de la voie d'accès éventuelle
- Évaluation du rapport bénéfice/risque dans une population à atteinte rénale et/ou hépatique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

