---
layout: default
title: Fluvoxamine
parent: Prédiction du modèle uniquement (L5)
nav_order: 344
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-03
monitor_inn: "FLUVOXAMINE"
predicted_indications: ["schizotypal personality disorder", "schizoid personality disorder", "histrionic personality disorder (disease)", "paranoid personality disorder", "anxiety disorder", "agoraphobia", "benign paroxysmal torticollis of infancy", "dependent personality disorder", "narcissistic personality disorder"]
description: "Fluvoxamine : nouvelle indication prédite, Trouble de la personnalité schizotypique (schizotypal personality disorder) (niveau de preuve L5)."
---

# Fluvoxamine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Fluvoxamine: Trouble de la personnalité schizotypique (schizotypal personality disorder)
{: .text-alpha }

## Résumé en Une Phrase

La fluvoxamine est un antidépresseur de la classe des inhibiteurs sélectifs de la recapture de la sérotonine.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **trouble de la personnalité schizotypique (schizotypal personality disorder)**, mais les données compilées pour ce rapport ne contiennent **aucun essai clinique** et seulement **5 publications** indirectes (séries et rapports de cas), qui portent sur le TOC avec traits schizotypiques et non sur ce trouble lui-même.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Trouble de la personnalité schizotypique (schizotypal personality disorder) |
| Score de Prédiction TxGNN | 1.0000 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, la fluvoxamine appartient à la classe des ISRS, et sa modulation de la transmission sérotoninergique pourrait, en théorie, être pertinente pour des troubles psychiatriques impliquant des circuits de l'anxiété et des comportements compulsifs.

Le lien avec le trouble de la personnalité schizotypique reste toutefois indirect. Les publications retrouvées décrivent l'ajout d'un neuroleptique chez des patients atteints de TOC résistant à la fluvoxamine, où la présence de traits schizotypiques était associée à la réponse, ainsi que quelques cas cliniques. Elles ne testent pas la fluvoxamine dans le trouble schizotypique lui-même. Le score très élevé du modèle semble refléter une proximité dans le réseau avec le TOC et la classe des ISRS plutôt qu'une preuve clinique.

Aucune étude citée n'étudiant directement cette maladie, le niveau de preuve est plafonné à L5 : la prédiction repose uniquement sur le modèle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [1970224](https://pubmed.ncbi.nlm.nih.gov/1970224/) | 1990 | Série de cas | Am J Psychiatry | Chez 17 patients avec TOC résistant à la fluvoxamine, 9 ont répondu à l'ajout d'un neuroleptique ; la présence de tics ou d'un trouble schizotypique était associée à la réponse |
| [11063782](https://pubmed.ncbi.nlm.nih.gov/11063782/) | 2000 | Essai ouvert | Psychiatry Res | Ajout d'olanzapine pendant 12 semaines dans le TOC résistant à la fluvoxamine ; évaluation du rôle des tics et du trouble schizotypique comme facteurs de réponse |
| [14999178](https://pubmed.ncbi.nlm.nih.gov/14999178/) | 2004 | Rapport de cas | CNS Spectrums | Patient avec syllogomanie, TDAH et trouble schizotypique, traité par fluvoxamine, amphétamines et rispéridone avec thérapie comportementale |
| [16146185](https://pubmed.ncbi.nlm.nih.gov/16146185/) | 2005 | Rapport de cas | Seishin Shinkeigaku Zasshi | TOC avec syndrome déficitaire induit par les neuroleptiques, amélioré après arrêt des neuroleptiques puis introduction de fluvoxamine |
| [8473723](https://pubmed.ncbi.nlm.nih.gov/8473723/) | 1993 | Rapport de cas | Int Clin Psychopharmacol | Crises convulsives lors de l'association lévomépromazine-fluvoxamine (signal de sécurité) |

## Informations de Marché en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 65470567 | FLOXYFRAL 50 mg, comprime pellicule secable | Comprime pellicule | Non renseignee |

La fluvoxamine est commercialisée en France (1 AMM valide dans les données compilées).

## Considérations de Sécurité

- **Contre-indications ou situations à risque à examiner** (relations de contre-indication recensées dans les données compilées, ne provenant pas du texte de la notice) : épilepsie, trouble bipolaire, trouble affectif majeur, maladie du foie, maladie de la vésicule biliaire, trouble de la coagulation, syndrome malin des neuroleptiques, syndrome de sécrétion inappropriée d'ADH, syndrome néphrogénique d'antidiurèse inappropriée, syndrome sérotoninergique.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les interactions majeures : alosétron, diéthylpropione, dolasétron, bupropion. Parmi les interactions modérées : rabéprazole, hydrocortisone, aprépitant, acide acétylsalicylique, clarithromycine, morphine, dexaméthasone, pioglitazone, entre autres.
- Un cas de crises convulsives a été rapporté avec l'association à une phénothiazine (lévomépromazine), ce qui est pertinent car les neuroleptiques sont souvent associés dans les situations cliniques étudiées.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle : aucun essai clinique et aucune étude ne testent la fluvoxamine dans le trouble de la personnalité schizotypique lui-même. Les publications disponibles concernent le TOC avec traits schizotypiques.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action et sur les mises en garde et contre-indications de la notice
- Études cliniques contrôlées de la fluvoxamine spécifiquement dans le trouble de la personnalité schizotypique
- Évaluation du profil d'interactions (CYP1A2, CYP2C19) et de la sécurité chez les patients recevant des neuroleptiques

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

