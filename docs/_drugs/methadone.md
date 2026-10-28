---
layout: default
title: Methadone
parent: Preuves modérées (L3-L4)
nav_order: 484
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-28
description: "Methadone : nouvelle indication prédite, Syndrome de Gilles de la Tourette (niveau de preuve L4). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "methadone"
predicted_indications: ["Tourette syndrome", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "headache disorder", "manic bipolar affective disorder", "trigeminal autonomic cephalalgia", "common cold"]
---

# Methadone
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **7** 
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

## Méthadone : De l'indication originale non renseignée au Syndrome de Gilles de la Tourette
{: .text-alpha }

## Résumé en Une Phrase

La méthadone est un agoniste opioïde puissant, commercialisé en France sous forme de sirop et de gélules par l'AP-HP. Le texte de l'indication approuvée n'est pas renseigné dans les données compilées pour ce rapport, et les deux AMM sont aujourd'hui annulées.
Le modèle TxGNN la prédit comme potentiellement efficace pour le **Syndrome de Gilles de la Tourette**, mais **aucun essai clinique** n'est enregistré et seule **une publication ancienne (1992)** décrit directement cet usage.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Syndrome de Gilles de la Tourette |
| Score de Prédiction TxGNN | 0,9976 |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances pharmacologiques générales, la méthadone est un agoniste des récepteurs opioïdes mu et un antagoniste des récepteurs NMDA. Ce profil est utilisé en pratique dans le traitement de la dépendance aux opioïdes et dans la prise en charge de la douleur.

La modulation opioïde des circuits dopaminergiques et striataux a été proposée comme pouvant influencer les tics. Un rapport de 1992 (PMID 1728167) décrit un traitement par méthadone d'un trouble de Gilles de la Tourette. Une revue de 2007 mentionne également que des opiacés sont efficaces dans le syndrome de Gilles de la Tourette et le TOC réfractaires.

Cette prédiction reste toutefois fragile : elle repose sur un seul rapport ancien et de petite taille, sans essai enregistré. Les autres publications associées (chorée, douleur neuropathique du cancer, TOC) sont indirectes.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [1728167](https://pubmed.ncbi.nlm.nih.gov/1728167/) | 1992 | Rapport de cas / petite série clinique | Am J Psychiatry | Traitement par méthadone d'un trouble de Gilles de la Tourette (résumé non disponible) |
| [17102981](https://pubmed.ncbi.nlm.nih.gov/17102981/) | 2007 | Préclinique / Revue | Psychopharmacology | Rôle des opiacés atypiques dans le TOC ; les opiacés sont mentionnés comme efficaces dans le TOC réfractaire et le syndrome de Gilles de la Tourette |
| [15247538](https://pubmed.ncbi.nlm.nih.gov/15247538/) | 2004 | Revue | Curr Opin Neurol | Causes non génétiques de chorée ; lien indirect |
| [39086469](https://pubmed.ncbi.nlm.nih.gov/39086469/) | 2024 | Revue | Palliat Care Soc Pract | Nouveaux traitements de la douleur neuropathique dans le cancer avancé ; lien indirect |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67255773 | METHADONE AP-HP 1,33 mg/ml, sirop | Sirop | Non renseignée (AMM active) |
| 68726979 | METHADONE AP-HP 5 mg, gélule | Gélule | Non renseignée (AMM active) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : syndrome du QT long (y compris familial), torsades de pointes, arrêt cardiaque soudain, maladie de la conduction cardiaque, insuffisance respiratoire, asthme, épilepsie, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, hypothyroïdie et myxœdème, maladie inflammatoire chronique de l'intestin, iléus paralytique, occlusion intestinale, hypertrophie bénigne de la prostate, sténose urétrale, hypotension, hypertension intracrânienne, troubles liés à l'usage de substances.
- **Interactions médicamenteuses** : 267 interactions recensées. Parmi les interactions de niveau majeur : alvimopan, bupropion, morphine, dexaméthasone, clarithromycine, cisapride, acide picosulfurique, polyéthylène glycol (3350 avec électrolytes). Parmi les interactions de niveau modéré : famotidine, hyoscyamine, lopéramide, aprépitant, atropine, cimétidine, glycopyrronium, dicyclomine.
- Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un seul rapport ancien (1992) sans essai clinique enregistré (niveau L4). Les deux AMM françaises sont annulées, et le profil de sécurité (risque cardiaque lié à l'allongement du QT, dépression respiratoire, nombreuses interactions) est exigeant pour une indication neuropsychiatrique non validée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde, contre-indications), étape bloquante pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Réaliser une revue systématique de la littérature sur les opioïdes dans le syndrome de Gilles de la Tourette, puis, si elle est favorable, un essai exploratoire avec surveillance de l'ECG (QT)
- Clarifier le statut réglementaire, 2 AMM valides sur 2 existant actuellement pour ces présentations commercialisées

**Remarque sur les autres indications prédites :** le trouble bipolaire maniaque (L3, étude de 1982 sur de petits effectifs, non confirmatoire) reste une question de recherche. Les céphalées (L4), l'autre candidat céphalalgique (céphalée trigémino-autonomique, L4, signal de **risque** d'aggravation) et le rhume banal (L5, sans lien) sont à mettre en attente. Le syndrome néphrogénique d'antidiurèse inappropriée et la trichotillomanie (L5, aucune donnée, mécanisme opposé à celui des antagonistes opioïdes) ne sont soutenus par aucune preuve.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

