---
layout: default
title: Mannitol
parent: Prédiction du modèle uniquement (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Mannitol : Du diurétique osmotique au syndrome néphrogénique d'antidiurèse inappropriée

## Résumé en Une Phrase

Le mannitol est un diurétique osmotique, commercialisé en France sous forme de solutions pour perfusion.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome néphrogénique d'antidiurèse inappropriée (SNAI)**, mais **aucun essai clinique** ne soutient cette direction et la seule publication associée est une revue générale sur l'hyponatrémie, sans lien thérapeutique direct.
Cette prédiction repose donc uniquement sur la proximité du médicament et de la maladie dans le graphe de connaissances.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Syndrome néphrogénique d'antidiurèse inappropriée |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L5 (le jeu de données indiquait L4, mais la seule publication ne teste pas le mannitol dans cette indication) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 9 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Le mannitol est un diurétique osmotique : il augmente l'osmolarité plasmatique et tubulaire, ce qui entraîne une diurèse osmotique. L'indication originale n'est pas renseignée dans les AMM françaises fournies.

Le lien avec le SNAI est faible. Cette maladie est causée par un gain de fonction du récepteur V2 de la vasopressine, un mécanisme sur lequel le mannitol n'agit pas. Son seul point commun avec le SNAI est d'apparaître dans les discussions de diagnostic différentiel de l'hyponatrémie. Le score élevé reflète très probablement une proximité dans le graphe autour de l'équilibre hydro-électrolytique, et non une activité pharmacologique démontrée.

Les autres prédictions du même rang (pathologies pulmonaires, hyperthermie maligne, paralysies périodiques, myopathies liées à RYR1, diabète insipide néphrogénique) sont également non étayées. Plusieurs sont des artéfacts de formulation. Par exemple, les formes intraveineuses du dantrolène contiennent du mannitol comme excipient. Pour le diabète insipide néphrogénique, le mannitol aggraverait plutôt la polyurie.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Revue | Eur J Intern Med | Dix pièges courants dans l'évaluation de l'hyponatrémie. Aborde le diagnostic et la prise en charge, sans démontrer d'effet thérapeutique du mannitol sur le SNAI. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 62126714 | Mannitol 10 % Aguettant | Solution pour perfusion | Aguettant |
| 68274328 | Mannitol B. Braun 10 pour cent | Solution pour perfusion | B. Braun Medical |
| 66972245 | Mannitol Lavoisier 20 pour cent | Solution pour perfusion | Laboratoires Chaix et du Marais |
| 62093602 | Mannitol 20 pour cent B. Braun | Solution injectable hypertonique pour perfusion | B. Braun Medical |
| 69361469 | Mannitol Biosedra 10 pour cent | Solution pour perfusion | Fresenius Kabi France |

Le texte des indications approuvées n'est pas renseigné dans les données reçues.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Il n'existe ni essai clinique ni donnée thérapeutique directe pour le mannitol dans le SNAI. Le mécanisme connu du mannitol (diurèse osmotique) n'a pas de lien avec un gain de fonction du récepteur V2. La prédiction résulte d'une inférence du graphe de connaissances.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde et contre-indications), indispensable pour le criblage de sécurité
- Données détaillées sur le mécanisme d'action (via l'API DrugBank)
- Indications approuvées des AMM françaises
- Une justification pharmacologique explicite reliant le mannitol au SNAI, avant toute étude
- Une revue experte des prédictions du même rang, pour confirmer qu'il s'agit d'artéfacts du graphe

*Ces résultats sont fournis à titre de recherche et ne constituent pas un avis médical. Toute piste de repositionnement doit être validée cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

