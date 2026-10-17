---
layout: default
title: Eltrombopag
parent: Prédiction du modèle uniquement (L5)
nav_order: 277
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Eltrombopag : nouvelle indication prédite, Infection par le VIH (niveau de preuve L5). Indication d'origine : Thrombopénie auto-immune"
monitor_inn: "eltrombopag"
predicted_indications: ["HIV infectious disease"]
---

# Eltrombopag
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

# Eltrombopag : De la thrombopénie auto-immune à l'infection par le VIH

## Résumé en Une Phrase

Eltrombopag est un agoniste du récepteur de la thrombopoïétine, initialement utilisé pour la thrombopénie auto-immune.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection par le VIH**, avec **1 essai clinique** enregistré (Phase 3, arrêté prématurément) et **aucune publication** associée dans les données compilées pour ce rapport.
Cette prédiction doit être interprétée avec prudence : elle concerne vraisemblablement la thrombopénie associée au VIH (une complication) et non l'infection virale elle-même.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Thrombopénie auto-immune (source : graphe de connaissances ; aucun texte d'indication AMM disponible) |
| Nouvelle Indication Prédite | Infection par le VIH |
| Score de Prédiction TxGNN | 99,26 % |
| Niveau de Preuve | L1 selon le classement automatique (à relativiser, voir ci-dessous) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. Sur la base des connaissances générales sur la classe, l'eltrombopag est un agoniste du récepteur de la thrombopoïétine (TPO-R) : il stimule la prolifération et la différenciation des mégacaryocytes et augmente ainsi la production de plaquettes. Son efficacité dans la thrombopénie auto-immune est la base de son indication d'origine.

Dans l'infection par le VIH, la thrombopénie est une complication fréquente. Elle résulte d'une destruction plaquettaire immuno-médiée, d'une altération de la mégacaryopoïèse par effet viral direct sur les progéniteurs, et de comorbidités (atteinte hépatique liée au VHC, myélosuppression due aux traitements antiviraux). Comme le TPO-R agit sur le déficit de production quelle que soit la cause, le lien mécanistique est plausible pour la **thrombopénie associée au VIH**.

Le score TxGNN très élevé (0,99) est un signal computationnel. Il ne traduit pas une activité antivirale de l'eltrombopag. Le lien mécanistique ci-dessus repose sur des connaissances générales de la classe, non sur des données de mécanisme vérifiées.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00678587](https://clinicaltrials.gov/study/NCT00678587) | Phase 3 | Arrêté | 292 | Étude randomisée, en double aveugle, contrôlée par placebo, visant à évaluer si l'eltrombopag réduit le besoin de transfusions plaquettaires chez des patients thrombopéniques atteints d'une hépatopathie chronique subissant des actes invasifs programmés |

**Réserves importantes :**
- Le titre et le résumé de cet essai portent sur la thrombopénie liée à une hépatopathie chronique, et non explicitement sur le VIH. Le lien avec le VIH n'est pas confirmé par les données disponibles.
- L'essai a été arrêté (2008-06 à 2009-10) ; le motif d'arrêt n'est pas indiqué et doit être vérifié sur ClinicalTrials.gov.
- La pertinence a été évaluée au grade B : l'arrêt prématuré limite la confiance dans les critères d'efficacité et de sécurité.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées ; aucune AMM valide n'est actuellement enregistrée. Aucun texte d'indication approuvée n'est disponible. Les 5 premières AMM sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64581657 | ELTROMBOPAG VIATRIS 25 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 65670831 | ELTROMBOPAG EG 50 mg, comprimé pelliculé sécable | Comprimé pelliculé sécable | Non renseignée |
| 61951699 | REVOLADE 75 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 64570543 | ELTROMBOPAG EG 75 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 65801736 | ELTROMBOPAG KRKA 50 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : maladie rénale, pyourétère, maladie hépatique, maladie de la vésicule biliaire, insuffisance hépatique aiguë, hépatite, anémie, anémie macrocytaire, hyperbilirubinémie (dont héréditaire), syndrome de Gilbert, leucopénie, syndrome myélodysplasique, thrombocytose, thrombose des veines hépatiques, syndrome de Budd-Chiari.
- **Interactions médicamenteuses** : 135 interactions recensées. Principales :
  - **Majeure** : éluxadoline.
  - **Modérées** : sels de calcium (phosphate, acétate, carbonate, citrate, gluconate, lactate, glubionate), sels et antiacides à base de magnésium et d'aluminium (oxyde, carbonate, chlorure, citrate, gluconate, hydroxyde, magaldrate, hydroxyde d'aluminium), attapulgite, kaolin, fer, glibenclamide. Les cations polyvalents peuvent notamment réduire l'absorption de l'eltrombopag.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau L1 attribué automatiquement repose sur un seul essai de Phase 3 arrêté prématurément, dont le lien avec le VIH n'est pas confirmé ; il n'existe aucune publication associée. Toutes les AMM françaises sont annulées et les données de sécurité de la notice sont absentes (lacune bloquante), ce qui empêche de poursuivre le criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications).
- Obtenir les données sur le mécanisme d'action via DrugBank.
- Vérifier sur ClinicalTrials.gov la population, le critère principal et le motif d'arrêt de NCT00678587.
- Rechercher des essais et publications spécifiques à la thrombopénie associée au VIH, et préciser si l'indication visée est la complication hématologique plutôt que l'infection.
- Clarifier les raisons de l'annulation des AMM et la situation réglementaire actuelle de l'eltrombopag en France.
- Évaluer, pour une population VIH, les contre-indications issues du graphe (notamment atteinte hépatique et thromboses) et les interactions avec les traitements antirétroviraux.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

