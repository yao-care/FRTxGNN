---
layout: default
title: Hydroxocobalamin
parent: Prédiction du modèle uniquement (L5)
nav_order: 382
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
monitor_inn: "hydroxocobalamin"
predicted_indications: ["esophageal varices without bleeding", "esophageal varices with bleeding"]
description: "Hydroxocobalamin : nouvelle indication prédite, Varices œsophagiennes sans saignement (niveau de preuve L5). Indication d'origine : Carence en vitamine B12, intoxication au cyanure, anémie pernicieus"
---

# Hydroxocobalamin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Hydroxocobalamine : De la carence en vitamine B12 à la varice œsophagienne sans saignement
{: .text-alpha }

## Résumé en Une Phrase

L'hydroxocobalamine est une forme de vitamine B12, initialement utilisée pour traiter la carence en vitamine B12, l'intoxication au cyanure et l'anémie de Biermer (anémie pernicieuse).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour les **varices œsophagiennes sans saignement**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carence en vitamine B12, intoxication au cyanure, anémie pernicieuse (le texte d'indication des AMM n'est pas renseigné ; ces indications proviennent du graphe de connaissances) |
| Nouvelle Indication Prédite | Varices œsophagiennes sans saignement |
| Score de Prédiction TxGNN | 99,23 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'hydroxocobalamine est une forme de vitamine B12, dont l'efficacité dans la carence en B12 et l'intoxication au cyanure est établie. Aucun lien mécanistique avec les varices œsophagiennes n'est établi dans les données compilées pour ce rapport.

Une hypothèse purement théorique serait que l'hydroxocobalamine puisse piéger le monoxyde d'azote (NO) et le sulfure d'hydrogène. Cela pourrait influencer la vasodilatation splanchnique et l'hypertension portale, qui sous-tendent les varices œsophagiennes. Cette hypothèse est spéculative et n'est étayée par aucune donnée fournie.

Le score élevé de TxGNN (99,23 %) résulte d'une prédiction informatique uniquement. La même prédiction existe pour les varices avec saignement (même score), mais l'hémorragie variqueuse aiguë est une urgence vitale disposant de traitements de référence bien établis (vasoactifs, ligature endoscopique, antibioprophylaxie) ; il n'y a aucune base pour envisager ce médicament dans ce contexte. La propriété de piégeage du NO s'accompagne en outre d'un risque connu d'hypertension transitoire.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60232334 | CYANOKIT 5 g, poudre pour solution pour perfusion (SERB) | Poudre pour solution pour perfusion | Non renseignée (AMM annulée) |
| 62597431 | DODECAVIT 0,5 mg/ml, solution injectable IM (SERB) | Solution injectable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension et troubles hypertensifs. Ce point est cohérent avec le risque d'élévation transitoire de la pression artérielle liée au piégeage du NO.
- **Interactions médicamenteuses** : 32 interactions ont été recensées. Parmi celles détaillées, quatre sont de niveau modéré : trioxyde d'arsenic, chloramphénicol, iodure I-131 et iodure I-123. Les autres (par exemple oméprazole, lansoprazole, simvastatine, prednisolone, acide acétylsalicylique, valsartan, ramipril, citalopram, lévothyroxine) sont de niveau non précisé.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et le mécanisme d'action est inconnu dans les données disponibles.
- Les deux AMM françaises sont annulées, et une contre-indication hypertensive est signalée, ce qui est un point de vigilance dans l'hypertension portale et les contextes hémorragiques.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) auprès de l'ANSM, élément bloquant pour le criblage de sécurité.
- Compléter les données sur le mécanisme d'action (par exemple via DrugBank).
- Mener une revue de la littérature sur le piégeage du NO/H₂S et l'hypertension portale, puis des études précliniques si elle est concluante.
- Évaluer la compatibilité des voies d'administration et la pertinence par rapport aux traitements de référence.
- Clarifier la situation réglementaire, toutes les AMM étant annulées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

