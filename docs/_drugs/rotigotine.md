---
layout: default
title: Rotigotine
parent: Prédiction du modèle uniquement (L5)
nav_order: 682
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "ROTIGOTINE"
predicted_indications: ["attention deficit-hyperactivity disorder", "schizophrenia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "faciodigitogenital syndrome", "congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "myopia X-linked", "atypical glycine encephalopathy", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited"]
description: "Rotigotine : nouvelle indication prédite, Attention deficit-hyperactivity disorder (niveau de preuve L5). En France, AMM dans la BDPM : 4 (valides : 4)"
---

# Rotigotine
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

## Rotigotine: Attention deficit-hyperactivity disorder
{: .text-alpha }

## Résumé en Une Phrase

Rotigotine est un agoniste dopaminergique, initialement utilisé pour traiter la maladie de Parkinson et le syndrome des jambes sans repos.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble du déficit de l'attention avec hyperactivité (TDAH)**, mais **aucun essai clinique** n'est enregistré et **3 publications** seulement (revues et étude mécanistique, sans preuve d'efficacité dans le TDAH) sont associées à cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Attention deficit-hyperactivity disorder |
| Score de Prédiction TxGNN | 1.0000 |
| Niveau de Preuve | L5 (prédiction du modèle, aucune étude clinique ; la littérature disponible est de nature mécanistique ou de revue) |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Rotigotine (traduction non officielle) : « La rotigotine est un agoniste dopaminergique non ergoté. Le mécanisme d’action précis de la rotigotine dans le traitement de la maladie de Parkinson est inconnu, bien qu’on pense qu’il soit lié à sa capacité à stimuler les récepteurs dopaminergiques au sein du noyau caudé-putamen dans le cerveau. » Texte original en anglais : "Rotigotine is a non-ergoline dopamine agonist. The precise mechanism of action of rotigotine as a treatment for Parkinson's disease is unknown, although it is thought to be related to its ability to stimulate dopamine receptors within the caudate-putamen in the brain." ([DailyMed: Neupro (rotigotine) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=939e28c5-f3a9-42c0-9a2d-8d471d82a6e0), version du 2026-11-11 ; consulté le 2026-11-19). Sur la base des connaissances pharmacologiques générales, la rotigotine est un agoniste dopaminergique à large spectre (récepteurs D1 à D5, avec une activité notable sur D3, D2 et D1), qui agit aussi sur les récepteurs adrénergiques alpha-2B et sérotoninergiques 5-HT1A. Son efficacité dans la maladie de Parkinson et le syndrome des jambes sans repos repose sur cette stimulation dopaminergique.

Le TDAH implique un dérèglement des systèmes dopaminergique et noradrénergique. Des polymorphismes du récepteur D4 et l'hétéromérisation entre ce récepteur et le récepteur adrénergique α2A ont été associés au trouble (PMID 34182128). Cela offre un lien plausible, mais indirect.

Il faut rester prudent : les publications sur le syndrome des jambes sans repos chez l'enfant reflètent la comorbidité et des mécanismes dopaminergiques partagés avec le TDAH, et non une preuve d'efficacité de la rotigotine dans le TDAH. Le score élevé du modèle reste une prédiction purement computationnelle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Revue | Revue neurologique | Revue du syndrome des jambes sans repos (2 à 3 % de la population occidentale) ; pas de donnée d'efficacité dans le TDAH |
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Revue | Current pharmaceutical design | Options pharmacologiques du syndrome des jambes sans repos chez l'enfant ; reflète la comorbidité avec le TDAH |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Préclinique/mécanistique | Pharmacological research | Hétéromérisation entre récepteurs α2A et variants du récepteur D4 ; implications pour les troubles du contrôle des impulsions |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66662951 | NEUPRO 4 mg/24 h, dispositif transdermique (active) | Dispositif | Non renseignée |
| 61578613 | NEUPRO 8 mg/24 h, dispositif transdermique (active) | Dispositif | Non renseignée |
| 69741731 | NEUPRO 2 mg/24 h, dispositif transdermique (active) | Dispositif | Non renseignée |
| 60200500 | NEUPRO 6 mg/24 h, dispositif transdermique (active) | Dispositif | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie, hors texte de notice) : hypertension / trouble hypertensif, atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, hypotension orthostatique, dyskinésie d'origine médicamenteuse.
- **Interactions médicamenteuses** : 51 interactions recensées, dont celles de niveau modéré avec les opioïdes (morphine, codéine, opium, diphénoxylate, difénoxine), les cannabinoïdes (dronabinol, nabilone), le métoclopramide, la prométhazine, plusieurs antihistaminiques (chlorphéniramine, cétirizine, brompheniramine, carbinoxamine, clémastine, azélastine nasale), le dextrométhorphane, la sibutramine, l'éthanol et l'ioflupane I-123.
- **Point d'attention propre à l'indication** : les agonistes dopaminergiques peuvent provoquer des effets indésirables psychiatriques (psychose, troubles du contrôle des impulsions), ce qui appelle une vigilance particulière dans une population pédiatrique ou psychiatrique.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucun essai clinique, et une littérature limitée à des revues et à de la pharmacologie mécanistique. Les 4 AMM françaises sont valides (4 sur 4), mais les données de sécurité de la notice manquent, ce qui bloque le dépistage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications)
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Mener une revue ciblée de la littérature sur les agonistes dopaminergiques dans le TDAH, puis des études précliniques ou cliniques exploratoires
- Évaluer la faisabilité de la voie d'administration (dispositif transdermique) pour la population cible et clarifier la situation réglementaire en France

**Autres prédictions (rang 2 à 10) :** schizophrénie (Hold ; un agoniste dopaminergique pourrait aggraver les symptômes positifs, et la méta-analyse disponible sur les médicaments pro-dopaminergiques concerne les symptômes négatifs sans être spécifique à la rotigotine), puis huit maladies rares (polymicrogyrie, syndrome faciodigitogénital, trouble congénital de la glycosylation, dystrophie rétinienne, deux formes de myopie liée à l'X, encéphalopathie glycinique atypique, maladie de Charcot-Marie-Tooth 1G) toutes de niveau L5 sans lien mécanistique identifié ni donnée de soutien : Hold.

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Neupro (rotigotine) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=939e28c5-f3a9-42c0-9a2d-8d471d82a6e0) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

