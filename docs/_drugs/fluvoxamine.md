---
layout: default
title: Fluvoxamine
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Fluvoxamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Fluvoxamine : Du Trouble Obsessionnel-Compulsif au Trouble de Personnalité Schizotypique

## Résumé en Une Phrase

Fluvoxamine est un inhibiteur sélectif de la recapture de la sérotonine (ISRS), utilisé dans de nombreux pays pour le traitement du trouble obsessionnel-compulsif (TOC), des troubles anxieux et de la dépression — mais non commercialisé en France à ce jour.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Trouble de Personnalité Schizotypique**,
avec **0 essai clinique** et **6 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | TOC, troubles anxieux et dépression (usages hors France — aucune AMM française disponible) |
| Nouvelle Indication Prédite | Trouble de personnalité schizotypique |
| Score de Prédiction TxGNN | 99,997 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de fluvoxamine ne sont pas disponibles dans les sources interrogées. Sur la base des informations issues de la littérature clinique, fluvoxamine inhibe puissamment et sélectivement le transporteur de sérotonine (SERT), augmentant ainsi la concentration synaptique de 5-HT. À la différence des autres ISRS, il possède également une activité agoniste sur le récepteur sigma-1, qui module l'axe HPA et la réactivité amygdalienne — propriété pertinente dans les états d'anxiété chronique et de décompensation émotionnelle.

Le trouble de personnalité schizotypique se caractérise par des idées de référence, une pensée magique, une méfiance interpersonnelle et des éléments obsessionnels-compulsifs du spectre anxieux. Cette proximité avec le TOC et les troubles anxieux sociaux constitue le point d'ancrage mécanique de la prédiction TxGNN : le modèle de graphe inférerait que si fluvoxamine est efficace dans le TOC et l'anxiété sociale, il pourrait s'étendre à d'autres conditions présentant un profil obsessionnel-anxieux similaire.

Cependant, les 6 publications disponibles ne ciblent pas directement le trouble schizotypique comme population d'étude principale. Elles portent essentiellement sur des patients TOC réfractaires à fluvoxamine chez qui une comorbidité schizotypique était associée à une meilleure réponse lors de l'ajout d'un antipsychotique. Ce lien demeure indirect et ne permet pas d'établir un rationnel mécanistique robuste pour une utilisation de fluvoxamine en monothérapie dans le trouble schizotypique isolé.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [1970224](https://pubmed.ncbi.nlm.nih.gov/1970224/) | 1990 | Série de cas (augmentation) | Am J Psychiatry | 9/17 patients TOC répondeurs à l'ajout d'un neuroleptique à fluvoxamine ; la comorbidité schizotypique et tic spectrum étaient associées à la réponse ; anomalies de la dopamine et sérotonine évoquées |
| [11063782](https://pubmed.ncbi.nlm.nih.gov/11063782/) | 2000 | Essai ouvert 12 semaines | Psychiatry Research | Augmentation par olanzapine chez 23 patients TOC réfractaires à fluvoxamine ; la comorbidité schizotypique concomitante était associée à la réponse thérapeutique |
| [16146185](https://pubmed.ncbi.nlm.nih.gov/16146185/) | 2005 | Rapport de cas | Psychiatria et Neurologia Japonica | Amélioration du TOC par fluvoxamine après arrêt des neuroleptiques chez un patient schizophrène avec personnalité schizotypique sous-jacente |
| [14999178](https://pubmed.ncbi.nlm.nih.gov/14999178/) | 2004 | Rapport de cas | CNS Spectrums | Patient avec accumulation compulsive, TDAH et trouble schizotypique traité par association fluvoxamine + sels d'amphétamine + rispéridone avec amélioration comportementale |
| [20414175](https://pubmed.ncbi.nlm.nih.gov/20414175/) | 2010 | Série clinique | CNS Spectrums | Étude du profil d'accumulation compulsive dans le TOC japonais ; nature hétérogène des réponses aux traitements dont fluvoxamine |
| [8473723](https://pubmed.ncbi.nlm.nih.gov/8473723/) | 1993 | Rapport de cas | Int Clin Psychopharmacol | Signal de sécurité : crises convulsives induites par l'association lévopromazine-fluvoxamine ; pertinence pour les co-prescriptions avec phénothiazines |

---

## Informations de Marché en France

Fluvoxamine ne dispose d'aucune autorisation de mise sur le marché (AMM) en France. Aucune donnée de licence ANSM n'est disponible dans les sources interrogées.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Aucune étude ne cible directement le trouble de personnalité schizotypique comme population principale ; les 6 publications disponibles fournissent des données indirectes issues d'études sur le TOC avec comorbidité schizotypique. La prédiction TxGNN repose sur une inférence par proximité topologique dans le graphe de connaissances, sans base clinique directe suffisante pour justifier une progression.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données complètes sur le mécanisme d'action de fluvoxamine (interrogation DrugBank API — gap DG002)
- Informations de sécurité ANSM : mises en garde, contre-indications, interactions médicamenteuses (gap DG001)
- Revue de la neurobiologie sérotoninergique spécifique au trouble de personnalité schizotypique
- Étude pilote prospective ciblant le trouble schizotypique comme indication principale (aucun essai enregistré à ce jour)
- Évaluation du statut réglementaire dans les pays où fluvoxamine est commercialisé (ex. Japon, États-Unis) pour identifier d'éventuelles approbations pertinentes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

