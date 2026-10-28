---
layout: default
title: Pitavastatin
parent: Prédiction du modèle uniquement (L5)
nav_order: 612
evidence_level: L5
indication_count: 4
monitor_inn: "pitavastatin"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome"]
last_modified_at: 2026-10-28
description: "Pitavastatin : nouvelle indication prédite, Déficience en protéine de transfert des esters de cholestérol (niveau de preuve L5). Indication d'origine : Hyperlipidémie combinée familiale"
---

# Pitavastatin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

## Pitavastatine : De l'hyperlipidémie combinée familiale à la déficience en protéine de transfert des esters de cholestérol
{: .text-alpha }

## Résumé en Une Phrase

La pitavastatine est une statine, enregistrée dans le graphe de connaissances pour l'hyperlipidémie combinée familiale (forme désormais considérée comme obsolète).
Le modèle TxGNN prédit qu'elle pourrait être utile pour la **déficience en protéine de transfert des esters de cholestérol (CETP)**,
mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hyperlipidémie combinée familiale (relation enregistrée dans le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Déficience en protéine de transfert des esters de cholestérol |
| Score de Prédiction TxGNN | 0,9998 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 6 sur 6) |
| Nombre d'AMM | 6 (valides : 6) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. D'après les connaissances générales, la pitavastatine est un inhibiteur de l'HMG-CoA réductase, qui réduit le LDL-cholestérol et tend à augmenter le HDL-cholestérol.

La déficience en CETP se caractérise par un HDL-cholestérol très élevé et un métabolisme lipoprotéique modifié. Il existe donc un lien plausible avec la voie des lipides. Cependant, cette maladie s'accompagne typiquement d'un HDL élevé, et le traitement par statine n'y est pas un besoin établi.

Le score élevé de TxGNN reste une prédiction du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. Sans essai, sans publication et sans données de mécanisme validées, le lien ne peut pas être confirmé.

## Preuves d'Essais Cliniques

Aucun essai clinique associé à la déficience en CETP n'est enregistré actuellement.

*Remarque : pour une autre indication prédite (infection par le VIH, rang 2), un essai de phase 3/4 (NCT06317051, 300 participants, actif non recrutant) compare notamment la rosuvastatine/ézétimibe à la pitavastatine chez des personnes vivant avec le VIH. Il porte sur le risque cardiométabolique, et non sur la déficience en CETP.*

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69233925 | LIPPIZA 2 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 64164770 | TROLISE 2 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 65203831 | TROLISE 4 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 62771736 | TROLISE 1 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 64358832 | LIPPIZA 1 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |

Une 6e AMM (LIPPIZA 4 mg, n° 63270518) existe également. Toutes sont détenues par KOWA Pharmaceutical Europe.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations du graphe, et non texte de notice) : maladie du foie, maladie de la vésicule biliaire, hypothyroïdie (dont myxœdème et hypothyroïdie congénitale), myopathie et maladies musculaires, paralysie périodique familiale, hypotension, rhabdomyolyse, fasciite nodulaire, insuffisance rénale, traumatisme.
- **Interactions médicamenteuses** : 86 interactions recensées. Parmi les principales : **majeure** avec l'érythromycine ; **modérées** avec la rosuvastatine, la simvastatine, le cobicistat, l'eltrombopag, la chloroquine, l'hydroxychloroquine, le métronidazole, le disulfirame et l'éthanol ; **mineures** avec la warfarine et le dicoumarol.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai ni publication n'étudie la déficience en CETP avec la pitavastatine, et la pertinence clinique est discutable puisque cette condition s'accompagne déjà d'un HDL élevé.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (à compléter)
- Revue de la littérature sur les statines dans la déficience en CETP
- Texte de la notice (mises en garde et contre-indications) via l'ANSM
- Évaluation de la pertinence clinique et des besoins thérapeutiques réels dans cette maladie rare
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

