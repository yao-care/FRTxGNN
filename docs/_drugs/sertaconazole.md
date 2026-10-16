---
layout: default
title: Sertaconazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 701
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sertaconazole : nouvelle indication prédite, Teigne du corps (tinea corporis) (niveau de preuve L5). Indication d'origine : Teigne du pied (tinea pedis)"
---

# Sertaconazole
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

# Sertaconazole : De la teigne du pied à la teigne du corps (tinea corporis)

## Résumé en Une Phrase

Le sertaconazole est un antifongique imidazolé, initialement utilisé pour le traitement de la teigne du pied (tinea pedis).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **teigne du corps (tinea corporis)**, indication la mieux soutenue parmi les prédictions examinées,
avec **0 essai clinique enregistré** et **20 publications** recensées actuellement, dont plusieurs études comparatives (sertaconazole contre terbinafine, clotrimazole, éberconazole, etc.).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Teigne du pied (tinea pedis) (le texte d'indication des AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Teigne du corps (tinea corporis) |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L2 (attribution prudente : phase et conception des études non confirmées) |
| Statut de Marché en France | Toutes les AMM sont annulées (aucune AMM valide) |
| Nombre d'AMM | 4 |
| Décision Recommandée | Proceed with Guardrails |

Remarque : la première indication prédite par rang TxGNN est la dermatophytose de l'aine et de la région périanale (niveau L4, Hold, aucune littérature spécifique). La teigne du corps a été retenue ici comme indication principale car elle est la mieux documentée.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues dans la littérature, le sertaconazole est un antifongique imidazolé qui inhibe la synthèse de l'ergostérol (via la lanostérol 14-alpha-déméthylase). Son noyau benzothiophène pourrait en outre exercer une action directe sur la membrane fongique, augmentant sa perméabilité et entraînant la mort cellulaire à concentration élevée.

La teigne du pied et la teigne du corps sont toutes deux des dermatophytoses superficielles causées par les mêmes genres de champignons (*Trichophyton*, *Epidermophyton*, *Microsporum*). Des données in vitro montrent une activité fongicide et fongistatique du sertaconazole contre *T. rubrum*, *T. mentagrophytes* et *E. floccosum*. Une revue publiée dans *Drugs* (2009) indique que, dans l'Union européenne, le sertaconazole est indiqué dans les dermatophytoses, y compris la teigne du corps, la teigne de l'aine (tinea cruris) et la teigne du pied.

L'extension vers la teigne du corps est donc très proche de l'indication d'origine, ce qui rend le risque faible. Le score TxGNN élevé reflète cette similarité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Les publications les plus pertinentes pour la teigne du corps (priorité aux études comparatives, puis aux revues) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24249898](https://pubmed.ncbi.nlm.nih.gov/24249898/) | 2013 | ECR comparatif | Indian J Dermatol | Terbinafine 1 % crème contre sertaconazole 2 % crème dans la teigne du corps et la teigne de l'aine |
| [35068526](https://pubmed.ncbi.nlm.nih.gov/35068526/) | 2021 | ECR comparatif | Indian J Dermatol | Efficacité et sécurité de l'éberconazole contre le sertaconazole dans les teignes localisées |
| [28066103](https://pubmed.ncbi.nlm.nih.gov/28066103/) | 2016 | Étude randomisée en aveugle observateur | Indian J Pharmacol | Sertaconazole contre terbinafine topique dans les dermatophytoses localisées (teigne du corps ou de l'aine) |
| [30409926](https://pubmed.ncbi.nlm.nih.gov/30409926/) | 2019 | ECR en double aveugle | Indian J Dermatol Venereol Leprol | Amorolfine 0,25 % contre sertaconazole 2 % dans les dermatophytoses limitées |
| [24249897](https://pubmed.ncbi.nlm.nih.gov/24249897/) | 2013 | Étude randomisée ouverte | Indian J Dermatol | Sertaconazole 2 % contre butenafine 1 % : efficacité, sécurité et coût dans les teignes cutanées |
| [34760651](https://pubmed.ncbi.nlm.nih.gov/34760651/) | 2021 | Étude randomisée ouverte | Perspect Clin Res | Sertaconazole contre luliconazole en crème dans les dermatophytoses |
| [23372210](https://pubmed.ncbi.nlm.nih.gov/23372210/) | 2013 | Étude pilote comparative | Indian J Dermatol | Sertaconazole, terbinafine et luliconazole en crème dans les dermatophytoses |
| [25386455](https://pubmed.ncbi.nlm.nih.gov/25386455/) | 2014 | Étude observationnelle comparative | J Clin Diagn Res | Sertaconazole contre clotrimazole topiques dans la teigne du corps |
| [18039020](https://pubmed.ncbi.nlm.nih.gov/18039020/) | 2007 | Étude clinique comparative | Am J Clin Dermatol | Solution contre crème de sertaconazole 2 % dans la teigne du corps, la teigne interdigitale du pied ou la candidose correspondante |
| [19275277](https://pubmed.ncbi.nlm.nih.gov/19275277/) | 2009 | Revue | Drugs | Utilisation du sertaconazole dans les mycoses superficielles en dermatologie et gynécologie ; indications européennes incluant la teigne du corps |

Ces études sont pour la plupart de petite taille, ouvertes ou régionales ; leur phase et leur conception ne peuvent être confirmées à partir des seuls titres.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63090616 | CANDAZOL 300 mg, ovule (annulée) | Ovule | Non renseignée |
| 66726382 | MONAZOL, ovule (annulée) | Ovule | Non renseignée |
| 66910838 | MONAZOL 2 %, crème (annulée) | Crème | Non renseignée |
| 65436593 | SERTACONAZOLE SUBSTIPHARM 300 mg, ovule (annulée) | Ovule | Non renseignée |

Les quatre AMM sont annulées ; aucun produit n'est actuellement autorisé en France.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- La teigne du corps est une extension étroite de l'indication dermatophytique d'origine, avec plusieurs études comparatives publiées et un mécanisme plausible. Toutefois, aucune AMM n'est valide en France, aucun essai n'est enregistré, et les données de sécurité et de mécanisme ne sont pas disponibles.
- Les autres indications prédites sont moins soutenues : la dermatophytose de l'aine et de la région périanale (L4), la teigne du cuir chevelu ou de la barbe (L4), le pityriasis versicolor (L3, étude de 1992) et les atteintes profondes ou pilaires (ectothrix, endothrix, granulome de Majocchi, tinea profunda : L5, prédiction seule) restent en Hold ou en question de recherche. Ces dernières nécessitent généralement un traitement systémique. La candidose cutanée et les mycoses superficielles (L2) sont en grande partie couvertes par l'indication d'origine et les entités déjà évaluées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice de l'ANSM (mises en garde et contre-indications), indispensable avant tout dépistage de sécurité
- Données détaillées sur le mécanisme d'action
- Confirmation de la phase et de la conception des études comparatives, avec lecture des textes complets
- Clarification du statut réglementaire, puisque toutes les AMM françaises sont annulées, et de la voie d'administration (forme topique crème, les ovules étant destinés à la voie vaginale)
- Données d'interactions médicamenteuses (aucune trouvée à ce jour)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

