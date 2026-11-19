---
layout: default
title: Ioversol
parent: Prédiction du modèle uniquement (L5)
nav_order: 409
evidence_level: L5
indication_count: 9
monitor_inn: "IOVERSOL"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "alopecia"]
last_modified_at: 2026-11-20
description: "Ioversol : nouvelle indication prédite, Arthrose (niveau de preuve L5). Indication d'origine : Non précisée dans les données compilées (les textes d'indication des…"
---

# Ioversol
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

## Ioversol : D'un produit de contraste iodé à l'arthrose (prédiction du modèle)
{: .text-alpha }

## Résumé en une phrase

Ioversol est un produit de contraste iodé utilisé en imagerie radiologique, commercialisé en France sous les noms OPTIRAY et OPTIJECT.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**arthrose**, mais la seule publication retrouvée porte sur une procédure d'embolisation (et non sur l'ioversol lui-même) : **aucun essai clinique** et **1 publication indirecte** soutiennent actuellement cette prédiction.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non précisée dans les données compilées (les textes d'indication des AMM sont vides) |
| Nouvelle indication prédite | Arthrose |
| Score de prédiction TxGNN | 0,9963 |
| Niveau de preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Ioversol (traduction non officielle) : « L'injection intravasculaire d'ioversol opacifie les vaisseaux situés sur le trajet du flux du produit de contraste, permettant la visualisation radiographique des structures internes jusqu'à ce qu'une hémodilution significative se produise. L'ioversol peut être visualisé dans le parenchyme rénal dans les 30 à 60 secondes suivant une injection intraveineuse rapide. » Texte original en anglais : "Intravascular injection of ioversol opacifies those vessels in the path of the flow of the contrast medium, permitting radiographic visualization of the internal structures until significant hemodilution occurs. Ioversol may be visualized in the renal parenchyma within 30 to 60 seconds following rapid intravenous injection." ([DailyMed: Optiray 320 (ioversol) prescribing information, Liebel-Flarsheim Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6cb6ca5f-b249-49b0-a9eb-8aa583da7c74), version du 2025-12-29 ; consulté le 2026-11-19). Ioversol est un produit de contraste radiographique iodé, destiné à rendre visibles les structures corporelles lors d'examens d'imagerie. Il n'a pas de mécanisme pharmacologique connu contre l'arthrose.

La seule publication retrouvée (essai LipioJoint-1) évalue une embolisation des artères géniculaires dans l'arthrose du genou, réalisée avec une émulsion à base d'huile iodée éthiodisée. L'effet observé est attribuable à la procédure d'embolisation, pas à l'ioversol. Le score élevé provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

Cette publication ne portant pas sur l'ioversol, aucune étude citée n'examine directement ce médicament dans l'arthrose. Le niveau de preuve est donc plafonné à L5. Les autres prédictions du modèle (polyarthrite rhumatoïde, brachyolmie, hémoglobinopathie, alopécie, etc.) ne reposent sur aucune preuve clinique et n'ont pas de justification mécanistique plausible.

## Preuves d'essais cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la littérature

| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Essai clinique (bras unique, procédural) | Diagnostic and Interventional Imaging | Évaluation de la sécurité et de l'efficacité de l'embolisation transitoire des artères géniculaires avec une émulsion d'huile éthiodisée dans l'arthrose du genou. L'étude ne porte pas sur l'ioversol. |

## Informations de marché en France

Ioversol est commercialisé en France ; les 4 AMM ci-dessous sont valides (produits à un seul principe actif, titulaire GUERBET). Les textes d'indication ne figurent pas dans les données compilées.

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Indication approuvée |
|---------|------|------|-----------|
| 65772900 | OPTIRAY 350 (350 mg I/mL), solution injectable en flacon | Solution injectable | Non renseignée |
| 67470459 | OPTIJECT 300 mg d'I/mL, solution injectable ou pour perfusion | Solution injectable ou pour perfusion | Non renseignée |
| 62823503 | OPTIJECT 350 mg d'I/mL, solution injectable ou pour perfusion | Solution injectable ou pour perfusion | Non renseignée |
| 67722465 | OPTIRAY 300 (300 mg I/mL), solution injectable en flacon | Solution injectable | Non renseignée |

## Considérations de sécurité

- **Interactions médicamenteuses** : 100 interactions ont été recensées. Les principales, de niveau majeur, concernent :
  - la metformine ;
  - l'amphotéricine B (y compris ses formes lipidique, liposomale et au sulfate de cholestéryle) ;
  - la mésalazine, le balsalazide, l'olsalazine et la sulfasalazine ;
  - la vancomycine ;
  - des aminosides et apparentés (kanamycine, néomycine, streptomycine) ;
  - la polymyxine B.

  Le mannitol présente une interaction de niveau modéré. L'atropine, la famotidine, l'acide acétylsalicylique, la morphine et l'oméprazole ont des interactions de niveau inconnu.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- Aucune étude citée n'examine l'ioversol dans l'arthrose ; la seule publication concerne une procédure d'embolisation avec un autre agent. La prédiction repose uniquement sur le modèle (L5) et n'a pas de plausibilité mécanistique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action de l'ioversol
- Mises en garde et contre-indications issues de la notice ANSM (lacune bloquante pour l'évaluation de sécurité)
- Textes d'indication des AMM françaises
- Toute étude préclinique ou clinique évaluant directement l'ioversol dans l'arthrose, en l'absence de laquelle la prédiction ne devrait pas être poursuivie

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Optiray 320 (ioversol) prescribing information, Liebel-Flarsheim Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6cb6ca5f-b249-49b0-a9eb-8aa583da7c74) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

