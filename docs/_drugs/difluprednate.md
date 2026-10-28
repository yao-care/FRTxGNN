---
layout: default
title: Difluprednate
parent: Prédiction du modèle uniquement (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "DIFLUPREDNATE"
predicted_indications: ["familial adrenal hypoplasia with absent pituitary luteinizing hormone", "seborrheic keratosis", "PAGOD syndrome", "vulvar inverted follicular keratosis", "adrenocortical insufficiency", "seborrheic dermatitis", "46,XY disorder of sex development", "necrobiosis lipoidica", "nephrotic syndrome", "iris disease"]
description: "Difluprednate : nouvelle indication prédite, Familial adrenal hypoplasia with absent pituitary luteinizing hormone (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locale"
---

# Difluprednate
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

## Difluprednate: Familial adrenal hypoplasia with absent pituitary luteinizing hormone
{: .text-alpha }

## Résumé en Une Phrase

Le difluprednate est un corticoïde de synthèse puissant, utilisé en ophtalmologie pour traiter l'inflammation et la douleur après chirurgie oculaire ainsi que l'uvéite antérieure. La seule AMM française recensée (une crème dermatologique) est aujourd'hui annulée et ne mentionne aucune indication.
Le modèle TxGNN place en tête de classement la **forme familiale d'hypoplasie surrénalienne avec absence de LH hypophysaire** (score de 0,9996), mais cette prédiction n'est soutenue par aucune donnée clinique. La piste la plus plausible sur le plan biologique est la **maladie de l'iris**, soutenue par **0 essai clinique** et **1 publication** préclinique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Familial adrenal hypoplasia with absent pituitary luteinizing hormone |
| Score de Prédiction TxGNN | 0.9996 |
| Niveau de Preuve | L5 (rang 1) ; L4 (maladie de l'iris) |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold (rang 1) ; question de recherche pour la maladie de l'iris |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Le difluprednate est toutefois un agoniste du récepteur des glucocorticoïdes (NR3C1), avec une affinité très élevée rapportée (Ki de 0,78 nM). Son effet anti-inflammatoire de classe est bien établi.

**Rang 1 (hypoplasie surrénalienne familiale).** Une logique de substitution en glucocorticoïdes pourrait être avancée. Elle est cependant faible : la maladie résulte d'un défaut congénital du développement (par exemple NR0B1/DAX-1) qu'un corticoïde topique ne corrige pas. Le difluprednate n'a aucun usage de substitution systémique établi.

**Maladie de l'iris (rang 10).** C'est le lien le plus cohérent. Le difluprednate en émulsion ophtalmique est utilisé contre l'inflammation du segment antérieur (uvéite antérieure), étroitement liée aux atteintes de l'iris (iritis, iridocyclite). La seule publication disponible est une étude pharmacocinétique chez le lapin : elle soutient la plausibilité biologique, mais pas l'efficacité clinique. La définition de cette indication reste par ailleurs imprécise.

**Autres prédictions.** Les indications de rang 2 à 9 relèvent soit d'une logique de classe des corticoïdes (dermatite séborrhéique, nécrobiose lipoïdique, syndrome néphrotique, insuffisance surrénalienne), soit d'un lien mécanistique très faible (kératose séborrhéique, syndrome PAGOD, kératose folliculaire inversée vulvaire, trouble du développement sexuel 46,XY). Aucune n'est étayée par des données propres au difluprednate.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [21182429](https://pubmed.ncbi.nlm.nih.gov/21182429/) | 2011 | Étude préclinique (pharmacocinétique, lapin) | J Ocul Pharmacol Ther | Évaluation des caractéristiques pharmacocinétiques et pharmacodynamiques du difluprednate en émulsion ophtalmique, comparé à d'autres agents ophtalmiques, par dosage de liaison au récepteur des glucocorticoïdes |

Cette publication concerne la maladie de l'iris (rang 10). Aucune littérature n'est disponible pour les autres indications prédites.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63588061 | EPITOPIC 0,05 POUR CENT, crème (ETHYX PHARMACEUTICALS) | Crème | Non renseignée (AMM active) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie du graphe PrimeKG, et non texte de notice) : hypertension oculaire, kératite herpétique (virus HSV), tuberculose oculaire, ulcère cornéen mycosique.
- **Interactions médicamenteuses** : aucune interaction médicament-médicament identifiée. La seule entrée concerne la cible pharmacologique du produit, le récepteur des glucocorticoïdes (agoniste).

Les mises en garde et contre-indications de la notice n'ont pas pu être obtenues. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold** (pour l'ensemble des indications prédites ; la maladie de l'iris peut être retenue comme question de recherche)

**Justification :**
- Toutes les prédictions reposent sur le score du modèle seul (L5), sauf la maladie de l'iris (L4) qui ne dispose que d'une étude préclinique chez l'animal. Aucun essai clinique n'existe, et le produit n'est plus commercialisé en France (AMM annulée).
- Les données de sécurité de la notice manquent, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Définir précisément l'indication « maladie de l'iris » et rechercher des données cliniques sur l'uvéite antérieure ou l'iridocyclite avec le difluprednate.
- Vérifier la compatibilité des voies d'administration (formulation ophtalmique contre voie requise pour chaque indication).
- Pour les indications systémiques (insuffisance surrénalienne, syndrome néphrotique), comparer aux traitements établis, car le difluprednate ne dispose d'aucune donnée de dosage systémique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

