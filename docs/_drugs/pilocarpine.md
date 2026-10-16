---
layout: default
title: Pilocarpine
parent: Prédiction du modèle uniquement (L5)
nav_order: 603
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Pilocarpine : nouvelle indication prédite, Glaucome héréditaire primaire (niveau de preuve L5). Indication d'origine : Glaucome à angle ouvert…"
monitor_inn: "PILOCARPINE"
predicted_indications: ["primary hereditary glaucoma"]
---

# Pilocarpine
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

# Pilocarpine : Du Glaucome à Angle Ouvert au Glaucome Héréditaire Primaire

## Résumé en Une Phrase

La pilocarpine est un agoniste muscarinique, initialement utilisé pour le traitement du glaucome à angle ouvert et de l'hypertension oculaire.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **glaucome héréditaire primaire**.
Cependant, **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Glaucome à angle ouvert, hypertension oculaire (le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Glaucome héréditaire primaire |
| Score de Prédiction TxGNN | 99,83 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances pharmacologiques générales, la pilocarpine est un agoniste muscarinique (récepteur M3). Elle provoque la contraction du muscle ciliaire et augmente l'écoulement de l'humeur aqueuse par le trabéculum, ce qui abaisse la pression intraoculaire. C'est le mécanisme établi pour ses indications d'origine.

Le glaucome héréditaire primaire appartient à la même famille de maladies que le glaucome à angle ouvert, ce qui explique probablement le score TxGNN très élevé (proximité avec les indications existantes). Un abaissement de la pression intraoculaire est donc, en théorie, pertinent.

Toutefois, les formes héréditaires (par exemple congénitales ou juvéniles, liées à des variants de CYP1B1 ou MYOC) impliquent souvent une anomalie structurelle du trabéculum ou de l'angle irido-cornéen. Les myotiques y sont probablement moins efficaces, et la chirurgie reste généralement le traitement de première intention. Cette analyse repose sur des connaissances générales et non sur les données fournies.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66997501 | ISOPTO PILOCARPINE 2 POUR CENT, collyre (NOVARTIS PHARMA) | Collyre en solution | Non renseignée ; AMM annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non le texte de la notice) : glaucome à angle fermé, asthme, bronchopneumopathie chronique obstructive (BPCO), uvéite, iritis, iridocyclite, kératite, kératoconjonctivite, décollement de la rétine, lithiase rénale (néphrolithiase), néphropathie urique aiguë, insuffisance hépatique, lithiase biliaire (cholélithiase, cholécystolithiase, choledocholithiase), cholécystite, maladie des voies biliaires, ictère obstructif et maladie bronchique.
- **Interactions médicamenteuses** : 100 interactions recensées, dont 13 de niveau modéré, toutes avec des anticholinergiques (effet pharmacologique opposé) : hyoscyamine, atropine (y compris ophtalmique), glycopyrronium (y compris topique), clidinium, dicyclomine, mépenzolate, méthscopolamine, propanthéline, scopolamine (y compris ophtalmique) et trospium. Des interactions de niveau inconnu figurent aussi avec le pantoprazole, le clotrimazole, la morphine, la metformine, l'oméprazole, le lansoprazole et l'épinéphrine.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le mécanisme est plausible, mais les formes héréditaires de glaucome relèvent souvent d'anomalies structurelles peu sensibles aux myotiques. Le seul produit français est en outre annulé, et les données de sécurité issues de la notice manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles de la notice (ANSM), nécessaires au dépistage de sécurité
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Une recherche bibliographique et d'essais cliniques ciblée sur la pilocarpine dans les glaucomes héréditaires, congénitaux et juvéniles
- Une évaluation de la compatibilité de la voie d'administration (collyre) avec la population visée, notamment pédiatrique
- Une clarification du statut réglementaire actuel, aucune AMM n'étant en vigueur en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

