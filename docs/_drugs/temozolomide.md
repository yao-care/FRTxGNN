---
layout: default
title: Temozolomide
parent: Prédiction du modèle uniquement (L5)
nav_order: 735
evidence_level: L5
indication_count: 1
monitor_inn: "temozolomide"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-11-20
description: "Temozolomide : nouvelle indication prédite, Néoplasme de la queue de cheval (cauda equina neoplasm) (niveau de preuve L5). En France, AMM dans la BDPM : au moins 20"
---

# Temozolomide
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

## Temozolomide: Néoplasme de la queue de cheval (cauda equina neoplasm)
{: .text-alpha }

## Résumé en Une Phrase

Le témozolomide est un agent alkylant oral, initialement utilisé pour traiter les tumeurs cérébrales gliales (astrocytome anaplasique, astrocytome hors glioblastome, glioblastome cérébral).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **néoplasme de la queue de cheval**, mais les preuves se limitent à **une seule publication pertinente (un rapport de cas)** et **aucun essai clinique**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Néoplasme de la queue de cheval (cauda equina neoplasm) |
| Score de Prédiction TxGNN | 0.9930 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Temozolomide (traduction non officielle) : « Le témozolomide n'est pas directement actif mais subit une conversion non enzymatique rapide au pH physiologique en composé réactif, le 5-(3-méthyltriazén-1-yl)-imidazole-4-carboxamide (MTIC). La cytotoxicité du MTIC serait principalement due à l'alkylation de l'ADN, essentiellement aux positions O 6 et N 7 de la guanine, qui provoque des cassures double brin de l'ADN et entraîne une mort cellulaire programmée. » Texte original en anglais : "Temozolomide is not directly active but undergoes rapid nonenzymatic conversion at physiologic pH to the reactive compound 5-(3-methyltriazen-1-yl)-imidazole-4-carboxamide (MTIC). The cytotoxicity of MTIC is thought to be primarily due to DNA alkylation, mainly at the O 6 and N 7 positions of guanine, which causes DNA double strand breaks and results in programmed cell death." ([DailyMed: Temodar (temozolomide) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=046a9011-3911-4d3f-a15f-fbb56d5aad56), version du 2026-02-20 ; consulté le 2026-11-19). D'après les connaissances pharmacologiques générales, le témozolomide est un agent alkylant oral qui méthyle l'ADN (positions O6 et N7 de la guanine, N3 de l'adénine). Ces lésions sont cytotoxiques et entraînent l'apoptose des cellules tumorales, surtout lorsque l'expression de MGMT est faible. Il traverse la barrière hémato-encéphalique et diffuse dans le liquide céphalorachidien.

Le score provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. La queue de cheval fait partie du système nerveux central bas, et certaines tumeurs de cette région, comme l'épendymome myxopapillaire, sont des tumeurs primitives du système nerveux central. Un effet sur ces tumeurs est donc plausible sur le plan biologique.

Cette plausibilité reste toutefois théorique : le statut du promoteur de MGMT dans les tumeurs de la queue de cheval n'est pas établi dans les données disponibles, et le score élevé du modèle est une prédiction computationnelle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [29270703](https://pubmed.ncbi.nlm.nih.gov/29270703/) | 2018 | Rapport de cas | Eur Spine J | Efficacité remarquable du témozolomide dans un épendymome myxopapillaire spinal en rechute, avec récidives multiples et dissémination dans le liquide céphalorachidien |
| [42760727](https://pubmed.ncbi.nlm.nih.gov/42760727/) | 2026 | Rapport de cas | Medicine | Carcinome NUT nasal avec réponses répétées sous prise en charge multimodale incluant la radiothérapie (lien indirect avec la queue de cheval) |
| [18706663](https://pubmed.ncbi.nlm.nih.gov/18706663/) | 2009 | Rapport de cas | Neuro-Chirurgie | Cryptococcose neuroméningée atypique chez un enfant traité pour un gliome pontique (lien indirect, non pertinent pour l'efficacité) |

Seul le premier rapport de cas concerne une tumeur de la région de la queue de cheval. Il s'agit d'un cas isolé, de faible niveau de preuve.

## Informations de Marché en France

Le témozolomide est commercialisé en France. Au moins 20 AMM valides sont recensées (liste possiblement partielle). Le texte de l'indication approuvée n'est pas renseigné dans les données compilées. Voici cinq AMM :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60691017 | TEMOZOLOMIDE ACCORD 250 mg | Gélule | Non renseignée |
| 66186993 | TEMOZOLOMIDE VIATRIS 140 mg | Gélule | Non renseignée |
| 68196114 | TEMODAL 140 mg | Gélule | Non renseignée |
| 61710965 | TEMODAL 2,5 mg/ml | Poudre pour solution pour perfusion | Non renseignée |
| 65421470 | TEMOZOLOMIDE SUN 5 mg | Gélule | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (agent alkylant) |
| Risque de Myélosuppression | Élevé à moyen. Les relations recensées dans le graphe de connaissances signalent des contre-indications liées à des atteintes hématologiques (thrombopénie, neutropénie, pancytopénie, anémie aplasique, etc.) |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | NFS (avec différentielle), fonction hépatique et rénale |
| Protection de Manipulation | Suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

- **Contre-indications recensées dans le graphe de connaissances** (relations du graphe, et non texte de la notice) : insuffisance hépatique, thrombopénie, neutropénie, agranulocytose, anémie (dont anémie macrocytaire), pneumocystose, pancytopénie, lymphopénie, syndrome myélodysplasique, anémie aplasique idiopathique, anémie aplasique.
- **Interactions médicamenteuses** : 320 interactions recensées. Parmi les principales :
  - Modérée : naltrexone
  - Mineure : lévofloxacine
  - Niveau non précisé : calcitriol, pantoprazole, doxycycline, clotrimazole, morphine, metformine, oméprazole, lansoprazole, prednisone, hydrocortisone, amphotéricine B, entre autres

Les mises en garde et contre-indications issues de la notice ANSM ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un score élevé du modèle et sur un seul rapport de cas, sans essai clinique. Aucune étude ne porte directement sur un néoplasme de la queue de cheval au sens large, d'où un niveau de preuve L5. Les données de sécurité de la notice font défaut.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, indications approuvées)
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Réaliser une revue systématique de la littérature sur les tumeurs de la queue de cheval (épendymome myxopapillaire notamment)
- Établir le statut du promoteur de MGMT dans ces tumeurs
- Si pertinent, planifier une étude observationnelle ou un essai de phase 2

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Temodar (temozolomide) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=046a9011-3911-4d3f-a15f-fbb56d5aad56) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

