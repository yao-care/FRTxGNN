---
layout: default
title: Dimercaprol
parent: Prédiction du modèle uniquement (L5)
nav_order: 247
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Dimercaprol : nouvelle indication prédite, Bronchite (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées (chélation des métaux…"
---

# Dimercaprol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Dimercaprol : Du traitement des intoxications aux métaux lourds à la bronchite

## Résumé en Une Phrase

Le dimercaprol (British Anti-Lewisite) est un agent chélateur dithiol, utilisé à l'origine pour traiter les intoxications par les métaux lourds (arsenic, mercure, plomb).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **bronchite**, mais cette prédiction repose sur **aucun essai clinique** et **une seule publication** (un rapport de cas de 1963 sur une bronchite due à l'inhalation aiguë de vapeurs de mercure).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées (chélation des métaux lourds d'après les connaissances pharmacologiques établies) |
| Nouvelle Indication Prédite | Bronchite |
| Score de Prédiction TxGNN | 99,54 % |
| Niveau de Preuve | L5 (prédiction du modèle, seul un rapport de cas isolé et ancien est disponible) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances pharmacologiques établies, le dimercaprol est un chélateur dithiol : ses groupements sulfhydryles se lient aux métaux lourds (mercure, arsenic, plomb) et favorisent leur élimination.

Le seul lien plausible avec la bronchite est indirect. Le rapport de cas de 1963 décrit une bronchite causée par l'inhalation aiguë de mercure. Dans ce contexte précis, chélater le mercure pourrait traiter la toxicité sous-jacente. Ce bénéfice potentiel serait donc limité aux bronchites d'origine toxique par métaux, et ne s'étendrait pas aux bronchites infectieuses, allergiques ou obstructives chroniques.

Le score TxGNN très élevé (99,54 %) reflète probablement la proximité dans le réseau de connaissances entre le dimercaprol et les intoxications aux métaux lourds avec atteinte respiratoire. Il s'agit d'une prédiction de modèle et non d'une preuve clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [14068440](https://pubmed.ncbi.nlm.nih.gov/14068440/) | 1963 | Rapport de cas | The American Review of Respiratory Disease | Deux cas de bronchite due à l'inhalation aiguë de mercure (résumé non disponible ; le titre ne permet pas de conclure sur l'effet du dimercaprol) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62727889 | B.A.L., solution injectable I.M. (SERB), AMM annulée | Solution injectable | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie de PrimeKG, et non texte de notice) : hypertension / trouble hypertensif, maladie du foie, maladie de la vésicule biliaire, déficit en G6PD, glycogénose, cystinurie, galactosémie.
- **Interactions médicamenteuses** : 15 interactions de niveau majeur identifiées, principalement avec le fer sous toutes ses formes : fer, ferrique carboxymaltose, citrate ferrique, dérisomaltose ferrique, fumarate ferreux, gluconate ferreux, sulfate ferreux, ferumoxides, ferumoxsil, ferumoxytol, fer dextran, succinylate de protéine de fer, fer saccharose, complexe de gluconate ferrique sodique. Une interaction majeure est aussi signalée avec le sélénium. Le dimercaprol formant des complexes avec les métaux, l'association avec le fer est à éviter.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un seul rapport de cas de 1963, sans essai clinique, et le bénéfice plausible se limiterait aux bronchites d'origine toxique par métaux lourds.
- Le produit n'a plus d'AMM valide en France et les données de sécurité de la notice sont absentes, ce qui bloque le criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde, contre-indications) auprès de l'ANSM
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Définir précisément la population cible (bronchite d'origine toxique par métaux lourds) et rechercher des études complémentaires
- Clarifier le statut réglementaire et la disponibilité du produit en France après l'annulation de l'AMM
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

