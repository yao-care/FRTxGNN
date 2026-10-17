---
layout: default
title: Bromocriptine
parent: Prédiction du modèle uniquement (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bromocriptine : nouvelle indication prédite, Schizophrénie (candidat retenu pour l'évaluation… (niveau de preuve L5). Indication d'origine : Maladie de Parkinson, hyperprolactinémie, acromégalie"
monitor_inn: "bromocriptine"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "retinal dystrophy with or without extraocular anomalies", "atypical glycine encephalopathy", "myopia 26, X-linked, female-limited", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "schizophrenia", "syndromic myopia"]
---

# Bromocriptine
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

# Bromocriptine : De la maladie de Parkinson et de l'hyperprolactinémie à la schizophrénie

## Résumé en Une Phrase

La bromocriptine est un agoniste dopaminergique D2, initialement utilisé dans la maladie de Parkinson, l'hyperprolactinémie (y compris les tumeurs hypophysaires sécrétant de la prolactine) et l'acromégalie.
Le modèle TxGNN prédit qu'elle pourrait être utile dans la **schizophrénie** (la première prédiction du classement, une maladie génétique rare de la glycosylation, ne repose sur aucune donnée), avec **1 essai clinique** et **20 publications** associés, dont aucune ne démontre une efficacité.
Le niveau de preuve reste faible : il s'agit d'une piste de recherche, non d'une indication étayée.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Parkinson, hyperprolactinémie, acromégalie (le texte d'indication des AMM n'est pas renseigné ; indications issues du graphe de connaissances) |
| Nouvelle Indication Prédite | Schizophrénie (candidat retenu pour l'évaluation, car il est le seul à disposer de données ; la prédiction n° 1 est un trouble congénital de la glycosylation avec défaut de fucosylation) |
| Score de Prédiction TxGNN | 99,73 % (schizophrénie) ; 99,83 % pour la prédiction n° 1 |
| Niveau de Preuve | L4 (schizophrénie) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold (question de recherche) |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la bromocriptine est un agoniste des récepteurs dopaminergiques D2/D3 (avec une activité sérotoninergique 5-HT2C mentionnée dans la description de l'essai), dont l'efficacité est établie dans la maladie de Parkinson et dans les états d'hyperprolactinémie.

La schizophrénie est associée à une dysrégulation dopaminergique, ce qui crée un lien pharmacologique avec la bromocriptine. Ce lien est toutefois ambigu : un agoniste D2 risque plutôt d'aggraver la psychose, et un cas de schizophrénie induite par la bromocriptine a été publié (PMID 8120934). L'intérêt potentiel se situerait davantage dans un rôle adjuvant, pour les troubles métaboliques (prédiabète, insulinorésistance) associés aux antipsychotiques, ou pour l'hyperprolactinémie qu'ils provoquent, plutôt que pour les symptômes psychotiques centraux.

Les autres prédictions du classement (myopies, rétinopathie, hydranencéphalie, neuropathie de Charcot-Marie-Tooth, etc.) n'ont pas de lien mécanistique identifié. Seule une hypothèse théorique faible existe pour les myopies, via le rôle de la dopamine rétinienne. Elles restent au stade de simples prédictions du modèle.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03575000](https://clinicaltrials.gov/study/NCT03575000) | Phase 4 | Pas encore en recrutement | 15 | Étude pilote ouverte, multicentrique, à dose flexible : bromocriptine en traitement adjuvant chez des patients schizophrènes avec prédiabète, pour évaluer la sécurité et la tolérance sur l'intolérance au glucose/insulinorésistance induite par les antipsychotiques. Aucun résultat d'efficacité disponible. |

---

## Preuves de la Littérature

Parmi les 20 publications associées, voici les plus pertinentes. Aucun essai randomisé n'est présent.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8120934](https://pubmed.ncbi.nlm.nih.gov/8120934/) | 1993 | Rapport de cas | J Natl Med Assoc | Schizophrénie apparue 4 jours après le début de la bromocriptine à faible dose chez un homme de 53 ans sans antécédent psychotique ; retour à la normale 5 jours après l'arrêt. |
| [6574535](https://pubmed.ncbi.nlm.nih.gov/6574535/) | 1983 | Étude clinique (10 patients) | Psychiatry Res | Bromocriptine à doses croissantes (jusqu'à 40 mg) chez 10 patients schizophrènes chroniques, avec évaluation des symptômes, du sommeil et de la réponse de la prolactine. |
| [39265262](https://pubmed.ncbi.nlm.nih.gov/39265262/) | 2024 | Revue systématique | Schizophr Res | L'insulinorésistance est une voie modifiable de la dysfonction cognitive dans la schizophrénie (contexte du rationnel métabolique). |
| [22713195](https://pubmed.ncbi.nlm.nih.gov/22713195/) | 2011 | Revue | Acta Med Port | Hyperprolactinémie fréquente sous antipsychotiques chez les patients schizophrènes. |
| [30805732](https://pubmed.ncbi.nlm.nih.gov/30805732/) | 2019 | Revue | J Neural Transm | Revue des agonistes dopaminergiques classiques, dont la bromocriptine. |
| [33571431](https://pubmed.ncbi.nlm.nih.gov/33571431/) | 2021 | Science fondamentale | Cell | Structures cryo-EM des complexes de signalisation des récepteurs D1 et D2. |
| [15711437](https://pubmed.ncbi.nlm.nih.gov/15711437/) | 2005 | Série de cas | Clin Neuropharmacol | Revue des agents adjuvants dans la schizophrénie résistante à la clozapine. |

Remarque : la publication [29546691](https://pubmed.ncbi.nlm.nih.gov/29546691/) (cabergoline versus bromocriptine dans les prolactinomes géants, revue systématique de 2018) est rattachée à une autre prédiction (hydranencéphalie). Elle concerne l'indication d'origine du médicament et correspond vraisemblablement à une association sans pertinence.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63369053 | PARLODEL 2,5 mg, comprimé sécable (annulée) | Comprimé sécable | Non renseignée |
| 64141483 | PARLODEL 5 mg, gélule (annulée) | Gélule | Non renseignée |
| 66729097 | PARLODEL 10 mg, gélule (annulée) | Gélule | Non renseignée |

Les trois AMM, détenues par EXELTIS SANTE, sont annulées : aucune présentation n'est actuellement commercialisée sous ce nom en France.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : hypertension, maladie hépatique, maladie de la vésicule biliaire, maladie coronarienne, accident vasculaire cérébral et troubles cérébrovasculaires (dont infarctus cérébral), prééclampsie (légère et sévère) et syndrome HELLP.
- **Interactions médicamenteuses** : 87 interactions recensées. Parmi les principales :
  - Majeures : isométheptène, lorcasérine.
  - Modérées : morphine (y compris liposomale), clarithromycine, dronabinol, nabilone, lansoprazole, métoclopramide, prométhazine, éthanol, opium, diphénoxylate, difénoxine, déférasirox, nitisinone, troglitazone, nitrite d'amyle, fostamatinib, ioflupane I-123.
- **Point d'attention spécifique** : en tant qu'agoniste D2, la bromocriptine peut exacerber ou induire des symptômes psychotiques (cas publié), ce qui est critique dans la schizophrénie. Les interactions avec les antagonistes dopaminergiques (métoclopramide, prométhazine, antipsychotiques) doivent aussi être examinées.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles : les données issues de la notice ANSM ne sont pas disponibles.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un score de modèle élevé, mais le seul essai disponible est une petite étude pilote ouverte (n = 15) non encore en recrutement, centrée sur un critère métabolique et sans donnée d'efficacité. La littérature comprend surtout des revues de pharmacologie et un cas rapportant une psychose induite, et aucun essai randomisé. Les autres prédictions n'ont aucun soutien clinique ni mécanistique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications), donnée bloquante pour le criblage de sécurité.
- Compléter les données sur le mécanisme d'action (via DrugBank).
- Attendre ou obtenir les résultats de l'essai NCT03575000, puis envisager un essai contrôlé randomisé sur l'indication adjuvante métabolique ou sur l'hyperprolactinémie induite par les antipsychotiques.
- Évaluer le risque d'aggravation psychotique et le profil d'interactions avec les antipsychotiques.
- Clarifier le statut réglementaire, toutes les AMM françaises étant annulées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

