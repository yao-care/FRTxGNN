---
layout: default
title: Paroxetine
parent: Prédiction du modèle uniquement (L5)
nav_order: 580
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Paroxetine : nouvelle indication prédite, Syndrome d'Ohdo et ses variants (niveau de preuve L5). Indication d'origine : Données non disponibles dans le texte réglementaire français"
monitor_inn: "paroxetine"
predicted_indications: ["Ohdo syndrome and variants"]
---

# Paroxetine
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

## Paroxétine : De la dépression et des troubles anxieux au syndrome d'Ohdo et ses variants
{: .text-alpha }

## Résumé en Une Phrase

La paroxétine est un inhibiteur sélectif de la recapture de la sérotonine (ISRS), initialement utilisé pour traiter la dépression, les troubles anxieux, le trouble obsessionnel-compulsif, le trouble de stress post-traumatique et la phobie sociale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome d'Ohdo et ses variants**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit uniquement d'une prédiction du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Données non disponibles dans le texte réglementaire français (les indications connues dans le graphe de connaissances incluent la dépression majeure, le trouble anxieux, le TOC, le TSPT et la phobie sociale) |
| Nouvelle Indication Prédite | Syndrome d'Ohdo et ses variants |
| Score de Prédiction TxGNN | 99,11 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement AMM annulée (non commercialisé) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la paroxétine appartient à la classe des ISRS. Son efficacité dans la dépression et les troubles anxieux est établie, mais son lien mécanistique avec le syndrome d'Ohdo n'est pas démontré.

Le syndrome d'Ohdo (y compris la variante Say-Barber-Biesecker-Young-Simpson) est une maladie génétique rare, couramment associée à des mutations de *KAT6B*, caractérisée par une déficience intellectuelle, un blépharophimosis et une hypotonie. Sa physiopathologie relève de mécanismes épigénétiques et développementaux, sans lien évident avec la pharmacologie sérotoninergique de la paroxétine.

Un lien éventuel serait indirect, par exemple le traitement symptomatique d'une anxiété, d'une dépression ou de troubles du comportement associés. Cette hypothèse reste spéculative. Le score élevé reflète probablement une proximité dans le graphe de connaissances (phénotypes neuropsychiatriques ou développementaux partagés) plutôt qu'un véritable mécanisme thérapeutique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68085224 | DIVARIUS 20 mg, comprimé pelliculé sécable (CHIESI) | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : épilepsie, trouble bipolaire, trouble affectif majeur, maladie du foie, maladie de la vésicule biliaire, troubles de la coagulation sanguine, syndrome malin des neuroleptiques, syndrome de sécrétion inappropriée d'ADH, syndrome néphrogénique d'antidiurèse inappropriée, syndrome sérotoninergique, akathisie d'origine médicamenteuse.
- **Interactions médicamenteuses** : 327 interactions recensées. Parmi celles retrouvées, les interactions **majeures** concernent le bupropion, la lorcasérine, la diéthylpropione, le dolasétron, l'eliglustat, le palonosétron et la phentermine. Des interactions **modérées** concernent notamment la morphine, l'acide acétylsalicylique (risque hémorragique), la chlorpropamide, la cimétidine, la clarithromycine, le dronabinol, l'éluxadoline, le glimépiride, le répaglinide et certains laxatifs de préparation colique. L'interaction avec l'aprépitant est mineure.

Les mises en garde et contre-indications de la notice officielle n'ont pas pu être consultées. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication et sans mécanisme plausible clairement identifié. De plus, l'AMM française est annulée et les données de sécurité de la notice manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), qui est une lacune bloquante pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Rechercher d'éventuelles preuves précliniques ou cliniques liant la paroxétine au syndrome d'Ohdo, ou à ses symptômes neuropsychiatriques associés
- Évaluer la pertinence d'une voie d'administration et d'une population cible (compatibilité de voie non encore évaluée)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

