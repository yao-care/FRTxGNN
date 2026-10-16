---
layout: default
title: Olsalazine
parent: Prédiction du modèle uniquement (L5)
nav_order: 558
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Olsalazine : nouvelle indication prédite, Syndrome myélodysplasique (niveau de preuve L5). Indication d'origine : Non précisée dans les AMM (texte d'indication vide)"
---

# Olsalazine
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

# Olsalazine : De la rectocolite hémorragique au syndrome myélodysplasique

## Résumé en une phrase

Olsalazine est un dimère prodrogue de l'acide 5-aminosalicylique (5-ASA, mésalazine), connu pour son usage dans la rectocolite hémorragique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome myélodysplasique**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

---

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non précisée dans les AMM (texte d'indication vide) ; usage connu : rectocolite hémorragique |
| Nouvelle indication prédite | Syndrome myélodysplasique |
| Score de prédiction TxGNN | 99,91 % |
| Niveau de preuve | L5 |
| Statut de marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision recommandée | Hold |

---

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'olsalazine est un dimère de 5-ASA, majoritairement retenu dans le côlon avec une faible exposition systémique. Le 5-ASA a une activité anti-inflammatoire (modulation de NF-kB et de PPAR-gamma, notamment).

Le lien avec une maladie clonale de la moelle osseuse comme le syndrome myélodysplasique reste **spéculatif**. Le score élevé (0,999) reflète vraisemblablement une proximité dans le graphe de connaissances plutôt qu'une justification mécanistique démontrée.

Les autres prédictions du classement posent les mêmes limites : syndrome myélodysplasique non classé, cytopénie réfractaire de l'enfant, délétion partielle du bras long du chromosome 5 (anomalie cytogénétique plutôt qu'indication thérapeutique) et anémies rares sont fortement corrélés au premier résultat et ne constituent pas des preuves indépendantes. Les prédictions pour l'hypotrichose, l'alopécie et l'alopécie areata sont également sans données à l'appui. Pour l'anémie arégénérative, une mise en garde s'impose : les médicaments de la classe sulfasalazine/5-ASA ont de rares signalements de suppression médullaire ou d'anémie aplasique, ce qui plaide contre un bénéfice.

---

## Preuves d'essais cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la littérature

Aucune littérature associée disponible actuellement.

---

## Informations de marché en France

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Indication approuvée | Statut |
|---------|------|------|-----------|------|
| 64457645 | DIPENTUM 500 mg, comprimé | Comprimé | Non renseignée | Annulée |
| 63634128 | DIPENTUM 250 mg, gélule | Gélule | Non renseignée | Annulée |

Titulaire : ATNAHS PHARMA NETHERLANDS (Pays-Bas).

---

## Considérations de sécurité

- **Interactions médicamenteuses** : 105 interactions recensées. Parmi les principales :
  - **Majeures** : immunoglobuline G humaine (intraveineuse), immunoglobuline humaine anti-neurotoxine botulique A/B, cidofovir, acide iothalamique.
  - **Modérées** : kétorolac, ibuprofène, diclofénac, célécoxib, aciclovir, amphotéricine B (y compris complexe lipidique), amikacine, azathioprine, bacitracine, ibandronate, capréomycine, chlorpropamide, cisplatine, clofarabine, colistiméthate.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations de sécurité.

---

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, avec un lien mécanistique spéculatif et une exposition systémique faible de l'olsalazine. De plus, les deux AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice (ANSM), actuellement manquantes et bloquantes pour le criblage de sécurité
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Une revue de la littérature précise et des registres d'essais pour le syndrome myélodysplasique
- Des données précliniques montrant un effet du 5-ASA sur les cellules hématopoïétiques
- Une évaluation de la compatibilité de la voie d'administration et de l'exposition systémique pour l'indication visée
- Une analyse du risque hématologique (myélosuppression rapportée avec les médicaments de cette classe)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

