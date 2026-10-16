---
layout: default
title: Vonicog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 820
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vonicog Alfa : nouvelle indication prédite, Trouble de la libération plaquettaire primaire (rang 1) (niveau de preuve L5). Indication d'origine : Maladie de von Willebrand héréditaire"
---

# Vonicog Alfa
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

# Vonicog alfa : Du Syndrome de Willebrand à l'Hémophilie

## Résumé en Une Phrase

Vonicog alfa est un facteur de von Willebrand recombinant (rVWF), initialement utilisé pour le traitement de la **maladie de von Willebrand** (héréditaire ou acquise).
Le modèle TxGNN prédit qu'il pourrait être efficace pour plusieurs affections hémorragiques, dont l'**hémophilie** (seule prédiction étayée par de la littérature indirecte). La prédiction de rang 1 est le **trouble de la libération plaquettaire primaire**, sans aucun élément de preuve.
Au total, **aucun essai clinique** et **4 publications indirectes** (toutes sur la maladie de von Willebrand, non sur l'hémophilie) sont disponibles.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de von Willebrand héréditaire (texte d'indication des AMM non disponible ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Trouble de la libération plaquettaire primaire (rang 1) ; hémophilie (rang 4, seule avec littérature indirecte) |
| Score de Prédiction TxGNN | 99,98 % (rang 1) ; 99,95 % (hémophilie) |
| Niveau de Preuve | L5 (rang 1) ; L4 (hémophilie) |
| Statut de Marché en France | Uniquement annulé |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, vonicog alfa est du facteur de von Willebrand recombinant : il favorise l'adhésion et l'agrégation plaquettaires et transporte le facteur VIII, qu'il stabilise dans la circulation.

Pour le **trouble de la libération plaquettaire primaire**, il s'agit d'un défaut intrinsèque des plaquettes (sécrétion des granules). Un apport de VWF ne pourrait offrir qu'un soutien hémostatique partiel et indirect. Le score élevé reste une prédiction purement computationnelle.

Pour l'**hémophilie**, le lien est plausible mais indirect : le VWF stabilise le facteur VIII endogène, mais ne remplace pas le facteur VIII manquant. Les autres prédictions présentent des liens plus faibles : thrombasthénie de Glanzmann (défaut du récepteur GPIIb/IIIa, en aval du VWF), pseudo-maladie de von Willebrand (défaut du récepteur plaquettaire, où l'ajout de VWF pourrait aggraver l'agglutination), syndrome de Scott, défaut du récepteur du collagène et thrombopénie constitutionnelle. La « forme liée à l'X de la maladie de von Willebrand » est une variante ontologique très proche de l'indication d'origine, probablement un chevauchement de nomenclature plutôt qu'une réelle opportunité de repositionnement. Le terme « flood factor deficiency » semble être un artefact d'ontologie sans mécanisme défini.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Publications retrouvées pour l'hémophilie (preuve indirecte uniquement, aucune ne porte sur l'hémophilie) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35439298](https://pubmed.ncbi.nlm.nih.gov/35439298/) | 2022 | Essai clinique de phase 3 | Blood | Prophylaxie par rVWF chez des adultes atteints de maladie de von Willebrand sévère, visant à réduire les saignements spontanés traités |
| [37332615](https://pubmed.ncbi.nlm.nih.gov/37332615/) | 2023 | Étude pharmacocinétique/pharmacodynamique | Journal of Blood Medicine | Comparaison du rVWF et du VWF d'origine plasmatique chez des patients atteints de maladie de von Willebrand de type 3 |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Revue narrative | Current Pharmaceutical Design | Agents hémostatiques nouveaux et renouvelés : considérations anesthésiques périopératoires |
| [37926687](https://pubmed.ncbi.nlm.nih.gov/37926687/) | 2024 | Étude de laboratoire in vitro et enquête | Haemophilia | Méthodes de dosage du VWF recombinant et plasmatique dans les laboratoires d'hémostase |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65346733 | VEYVONDI 650 UI poudre et solvant pour solution injectable (statut : annulée) | Poudre et solvant pour solution injectable | Non renseignée |
| 69749137 | VEYVONDI 1 300 UI poudre et solvant pour solution injectable (statut : annulée) | Poudre et solvant pour solution injectable | Non renseignée |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées pour ce rapport, et aucune contre-indication n'est issue du graphe de connaissances.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les 10 prédictions reposent sur le seul modèle (L5), à l'exception de l'hémophilie (L4), dont les publications concernent la maladie de von Willebrand et non l'hémophilie. Aucun essai clinique n'est enregistré, les deux AMM françaises sont annulées et les données de sécurité de la notice sont manquantes (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications) afin de pouvoir réaliser le premier criblage de sécurité
- Obtenir les données sur le mécanisme d'action (par ex. via DrugBank)
- Clarifier les raisons de l'annulation des AMM et la disponibilité actuelle du produit en France
- Rechercher des données cliniques directes sur l'hémophilie (et, si pertinent, sur le trouble de la libération plaquettaire), ou un avis d'expert sur la pertinence biologique
- Écarter les prédictions de faible plausibilité (« flood factor deficiency », forme liée à l'X redondante avec l'indication d'origine)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

