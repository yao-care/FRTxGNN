---
layout: default
title: Lonafarnib
parent: Prédiction du modèle uniquement (L5)
nav_order: 458
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Lonafarnib : nouvelle indication prédite, Lèpre (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "LONAFARNIB"
predicted_indications: ["leprosy"]
---

# Lonafarnib
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

# Lonafarnib : Du Syndrome de progéria à la Lèpre

## Résumé en Une Phrase

Lonafarnib est un inhibiteur de la farnésyltransférase dont l'indication d'origine n'est pas renseignée dans les données d'AMM compilées pour ce rapport (le produit est connu sous le nom de marque Zokinvy).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **lèpre**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Lèpre |
| Score de Prédiction TxGNN | 99,14 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, lonafarnib est un inhibiteur de la farnésyltransférase : il bloque la prénylation des protéines. Il est utilisé dans le syndrome de progéria de Hutchinson-Gilford et dans les laminopathies progéroïdes.

Le lien avec la lèpre reste **spéculatif**. *Mycobacterium leprae* survit dans les macrophages et les cellules de Schwann de l'hôte. Or, les petites GTPases prénylées de l'hôte (Ras, Rho, Rab) interviennent dans la maturation des phagosomes, le trafic intracellulaire et la signalisation inflammatoire. Inhiber la prénylation pourrait, en théorie, modifier ces processus.

Aucune donnée directe ou indirecte ne soutient ce lien. Le score TxGNN est très élevé (99,14 %), mais il s'agit d'une prédiction de modèle qui ne peut être validée ici, faute d'essais et de publications.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61837140 | ZOKINVY 75 mg, gélule (annulée) | Gélule | Non renseignée |
| 66601425 | ZOKINVY 50 mg, gélule (annulée) | Gélule | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de la farnésyltransférase) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

**Interactions médicamenteuses** : 100 interactions ont été recensées. Parmi les premières listées, les interactions de niveau **majeur** concernent :
- Lopéramide
- Aprépitant
- Triamcinolone
- Dexaméthasone
- Budésonide
- Cimétidine
- Clarithromycine
- Éliglustat
- Naloxégol

Des interactions de niveau **modéré** figurent notamment avec l'hydrocortisone, l'oméprazole, la bétaméthasone, le chlorpropamide, la saxagliptine, l'empagliflozine, l'oxandrolone et la naldémédine.

Ces interactions suggèrent une vigilance particulière vis-à-vis des médicaments métabolisés par les mêmes voies enzymatiques, en particulier les corticoïdes et les inhibiteurs enzymatiques (clarithromycine, cimétidine).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. De plus, les AMM françaises sont toutes annulées et les données de sécurité issues de la notice sont absentes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) auprès de l'ANSM
- Compléter les données sur le mécanisme d'action (DrugBank)
- Mener une revue de la littérature préclinique sur la prénylation et l'infection par *M. leprae*
- Établir la compatibilité de voie d'administration et la similarité avec l'indication d'origine, actuellement non évaluées
- Fournir des données précliniques ou des essais exploratoires validant le lien avec la lèpre
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

