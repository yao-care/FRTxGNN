---
layout: default
title: Spironolactone
parent: Prédiction du modèle uniquement (L5)
nav_order: 289
evidence_level: L5
indication_count: 2
---

# Spironolactone
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Spironolactone : D'un antagoniste des récepteurs minéralocorticoïdes à l'hypotrichose simple du cuir chevelu

## Résumé en Une Phrase

La spironolactone est un antagoniste de l'aldostérone (récepteur minéralocorticoïde) doté d'une activité antiandrogénique, commercialisé en France sous forme de comprimés. Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypotrichose simple du cuir chevelu**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction. Il s'agit d'une hypothèse purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM fournies (le texte d'indication est vide pour les AMM listées) |
| Nouvelle Indication Prédite | Hypotrichose simple du cuir chevelu |
| Score de Prédiction TxGNN | 99,26 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, la spironolactone bloque le récepteur de l'aldostérone et exerce aussi une action antiandrogénique. Ce second effet explique son usage hors AMM dans les alopécies d'origine androgénique, comme l'alopécie féminine de type androgénétique.

Le modèle s'appuie probablement sur cette proximité entre la spironolactone et les affections du follicule pileux dans le graphe de connaissances. Cette association reste toutefois fragile. L'hypotrichose simple du cuir chevelu est une maladie héréditaire rare, liée à des variants de gènes tels que *CDSN*, *APCDD1* et *SNRPE*. Elle n'est pas principalement dirigée par les androgènes, et le lien mécanistique reste donc spéculatif. Il n'a pas pu être vérifié, faute de mécanisme d'action documenté.

Une seconde prédiction du même type existe : la **milie hypotrichosique congénitale** (score 99,04 %, niveau L5, décision Hold). Aucun mécanisme plausible ne relie le blocage des récepteurs minéralocorticoïdes ou androgéniques à la correction d'un défaut de développement du follicule. Cette prédiction est encore moins convaincante que la première.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69360552 | SPIRONOLACTONE ZYDUS 25 mg | Comprimé pelliculé sécable | Non renseignée |
| 65618628 | SPIRONOLACTONE PFIZER 25 mg | Comprimé sécable | Non renseignée |
| 68800618 | SPIRONOLACTONE TEVA 50 mg | Comprimé pelliculé sécable | Non renseignée |
| 60464076 | SPIRONOLACTONE VIATRIS 25 mg | Comprimé pelliculé sécable | Non renseignée |
| 60337762 | SPIRONOLACTONE TEVA 75 mg | Comprimé pelliculé sécable | Non renseignée |

Ces 5 AMM sont les premières des 20 recensées. Les formes disponibles sont toutes orales (comprimés).

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai ni publication.
- Le mécanisme est peu plausible pour une maladie génétique du follicule, et les données de sécurité de la notice ANSM manquent (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), étape bloquante avant toute évaluation de sécurité.
- Documenter le mécanisme d'action via DrugBank, pour vérifier le lien avec l'hypotrichose.
- Rechercher dans la littérature et les registres d'essais toute étude sur la spironolactone dans les hypotrichoses héréditaires.
- Renseigner les indications approuvées des AMM françaises.
- Évaluer la compatibilité de voie d'administration : les formes disponibles sont orales, et l'adéquation à l'indication prédite reste à établir.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

