---
layout: default
title: Hesperidin
parent: Prédiction du modèle uniquement (L5)
nav_order: 378
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Hesperidin : nouvelle indication prédite, Néoplasie myéloproliférative (niveau de preuve L5). Indication d'origine : Non renseignée dans les données compilées"
---

# Hesperidin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Hespéridine : D'une indication non documentée à la néoplasie myéloproliférative

## Résumé en Une Phrase

L'hespéridine est un flavonoïde (flavanone glycosylée) commercialisé en France sous forme de comprimés pelliculés (FLAVONOIDES ZENTIVA CONSEIL). Les données compilées ne précisent aucune indication d'origine, et ces autorisations sont aujourd'hui annulées.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **néoplasie myéloproliférative**, mais **aucun essai clinique** et **une seule publication** (étude in silico) soutiennent actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données compilées |
| Nouvelle Indication Prédite | Néoplasie myéloproliférative |
| Score de Prédiction TxGNN | 99,47 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisations annulées uniquement |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'hespéridine est un flavonoïde de la classe des flavanones glycosylées. Son indication d'origine n'est pas renseignée dans les autorisations françaises compilées, et l'applicabilité mécanistique à la nouvelle indication reste à démontrer.

La seule publication associée est une étude de docking moléculaire *in silico* (2019) portant sur le domaine kinase de BCR-ABL dans la leucémie myéloïde chronique (LMC), une néoplasie myéloproliférative apparentée mais distincte. Elle suggère un possible effet inhibiteur de kinase, sans aucune validation expérimentale ou clinique.

Il faut aussi relever une limite pharmacologique : l'hespéridine a une faible biodisponibilité orale, de sorte qu'atteindre des concentrations systémiques efficaces au niveau d'une cible kinase est incertain. Le score élevé de TxGNN (0,995) reste une prédiction de modèle, non corroborée par des preuves réelles.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31759365](https://pubmed.ncbi.nlm.nih.gov/31759365/) | 2019 | Étude in silico | Asian Pacific Journal of Cancer Prevention | Repositionnement de médicaments par méthodes informatiques pour cibler le domaine kinase de BCR dans la LMC, afin de contourner la résistance aux inhibiteurs de tyrosine kinase via Grb-2 |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69840366 | FLAVONOIDES ZENTIVA CONSEIL 500 mg, comprimé pelliculé (annulée) | Comprimé pelliculé | Non renseignée |
| 66701450 | FLAVONOIDES ZENTIVA CONSEIL 1000 mg, comprimé pelliculé (annulée) | Comprimé pelliculé | Non renseignée |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle TxGNN (niveau L5) et sur une seule étude in silico, sans essai clinique. Les autorisations françaises sont annulées et les informations de sécurité sont absentes, ce qui empêche de passer au criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), point bloquant
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Obtenir une validation expérimentale *in vitro* sur des modèles de néoplasie myéloproliférative
- Évaluer la biodisponibilité et la faisabilité d'atteindre des concentrations efficaces par voie orale
- Clarifier l'indication d'origine et la raison de l'annulation des AMM
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

