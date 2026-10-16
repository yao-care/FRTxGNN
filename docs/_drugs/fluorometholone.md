---
layout: default
title: Fluorometholone
parent: Prédiction du modèle uniquement (L5)
nav_order: 338
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fluorometholone : nouvelle indication prédite, Vascularite post-infectieuse (niveau de preuve L5). Indication d'origine : Uvéite, iridocyclite, conjonctivites allergiques (atopique…"
monitor_inn: "fluorometholone"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "infective urethral stricture", "post-infectious syndrome", "punctate epithelial keratoconjunctivitis", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy", "lens-induced iridocyclitis", "glaucomatocyclitic crisis"]
---

# Fluorometholone
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

# Fluorométholone : De l'uvéite à la kératoconjonctivite ponctuée épithéliale

## Résumé en Une Phrase

Le fluorométholone est un corticoïde topique ophtalmique, initialement utilisé pour traiter les inflammations du segment antérieur de l'œil (uvéite, iridocyclite, conjonctivites allergiques, etc.).
Le modèle TxGNN le prédit comme potentiellement efficace pour la **postinfectious vasculitis** (vascularite post-infectieuse, première prédiction du classement), mais cette piste n'est étayée par **aucun essai clinique** ni **aucune publication**. La piste la plus plausible sur le plan biologique est la **kératoconjonctivite ponctuée épithéliale**, pour laquelle seules **2 publications** de contexte indirect sont disponibles.

> Remarque : le titre reprend l'indication prédite la plus plausible (kératoconjonctivite ponctuée épithéliale, rang 6) plutôt que la première du classement, car cette dernière est mécanistiquement peu crédible pour une forme ophtalmique topique. La section « Aperçu Rapide » détaille les deux.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Uvéite, iridocyclite, conjonctivites allergiques (atopique, printanière, papillaire), ulcère de la cornée, etc. (le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite (rang 1 TxGNN) | Vascularite post-infectieuse |
| Nouvelle Indication Prédite la plus plausible (rang 6) | Kératoconjonctivite ponctuée épithéliale |
| Score de Prédiction TxGNN | 99,91 % (rang 1) ; 99,89 % (rang 6) |
| Niveau de Preuve | L5 (rang 1) ; L4 (rang 6) |
| Statut de Marché en France | Autorisation annulée uniquement |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold (rang 1) ; Research Question (rang 6) |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le fluorométholone est un corticoïde synthétique qui se lie au récepteur des glucocorticoïdes (NR3C1) et exerce un effet anti-inflammatoire et immunosuppresseur. Son efficacité dans les inflammations oculaires antérieures est reconnue.

Pour la **kératoconjonctivite ponctuée épithéliale**, la proximité avec les indications d'origine est élevée : il s'agit d'une inflammation de la surface oculaire, et les corticoïdes sont utilisés pour les infiltrats sous-épithéliaux et les séquelles inflammatoires des kératoconjonctivites adénovirales (épidémiques) et microsporidiennes. Toutefois, les deux publications retrouvées portent sur la prise en charge des séquelles et sur le suivi par OCT du segment antérieur : il s'agit d'un contexte indirect, non de données d'efficacité propres au fluorométholone. Les corticoïdes dans les kératoconjonctivites infectieuses comportent aussi des risques (excrétion virale prolongée, élévation de la pression intraoculaire, aggravation de l'infection).

Pour la **vascularite post-infectieuse** (rang 1), un mécanisme glucocorticoïde est plausible, la maladie étant à médiation immunitaire. Mais le fluorométholone est un agent ophtalmique topique à exposition systémique limitée : une indication systémique est mal soutenue. Le score TxGNN est le seul élément en faveur de cette prédiction.

Deux autres pistes proches des indications d'origine sont à signaler (niveau L4, sans essai ni publication spécifiques) : l'**iridocyclite induite par le cristallin** (traitement définitif généralement chirurgical, corticoïdes en appoint) et la **crise glaucomato-cyclitique** (syndrome de Posner-Schlossman, uvéite antérieure récidivante avec hypertonie oculaire, pour laquelle la moindre tendance du fluorométholone à élever la PIO est un avantage théorique).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Pour la kératoconjonctivite ponctuée épithéliale :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34011737](https://pubmed.ncbi.nlm.nih.gov/34011737/) | 2021 | Revue | Indian J Ophthalmol | Caractérisation des séquelles de la kératoconjonctivite microsporidienne et de sa prise en charge |
| [35128186](https://pubmed.ncbi.nlm.nih.gov/35128186/) | 2021 | Revue | J Curr Ophthalmol | Rôle de l'OCT du segment antérieur dans le suivi de la kératoconjonctivite épidémique et effet des corticoïdes topiques sur son évolution |

Aucune littérature associée disponible pour les autres indications prédites.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68728453 | FLUCON, collyre (IMMEDICA PHARMA, Suède) | Collyre | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : kératite à herpès simplex, glaucome à angle ouvert, hypertonie oculaire, infections oculaires (infectieuses, fongiques, virales, tuberculose oculaire), conjonctivite, pigmentation cornéenne, diabète et acidocétose diabétique, porphyries, déficit en G6PD, glycogénose, cystinurie, galactosémie.
- **Interactions médicamenteuses** : 11 interactions recensées (doxycycline, salbutamol, ciclosporine, paracétamol, digoxine, brimonidine, céphalexine, acide alendronique, aciclovir, diazépam, fénofibrate), toutes de niveau de gravité non précisé. Le récepteur des glucocorticoïdes est par ailleurs la cible pharmacologique identifiée.
- **Points d'attention propres aux nouvelles indications** : risque d'élévation de la PIO et d'aggravation d'infection dans les kératoconjonctivites infectieuses ; risque de réactivation parasitaire sous immunosuppression dans la cardiomyopathie de Chagas.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être obtenues.

## Conclusion et Prochaines Étapes

**Décision : Hold** (vascularite post-infectieuse et autres prédictions systémiques ou non spécifiques) ; **Research Question** pour la kératoconjonctivite ponctuée épithéliale, l'iridocyclite induite par le cristallin et la crise glaucomato-cyclitique.

**Justification :**
- Les prédictions de rang 1 à 5 et 7 à 8 reposent uniquement sur le score du modèle, sans essai ni publication, et plusieurs sont peu crédibles pour un collyre à faible exposition systémique. Les pistes ophtalmiques sont plus plausibles mais ne disposent que de preuves indirectes. De plus, l'unique AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications officielles issues de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Données détaillées sur le mécanisme d'action (DrugBank)
- Études spécifiques au fluorométholone dans la kératoconjonctivite (essais ou séries comparatives)
- Évaluation de la compatibilité de voie d'administration et de formulation pour chaque indication envisagée
- Clarification du statut réglementaire (AMM annulée) et de la disponibilité du produit en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

