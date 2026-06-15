---
layout: default
title: Glycine
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 2
---

# Glycine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

Ce skill couvre la gestion du pipeline (entraînement, déploiement) — il ne s'applique pas à la génération de rapport depuis un Evidence Pack. Je procède directement avec le format défini.

---

# Glycine : De Supplément Nutritionnel à Maladie de la Cavité Nasale

## Résumé en Une Phrase

La glycine est un acide aminé non essentiel, utilisé principalement comme supplément nutritionnel et excipient dans diverses formulations pharmaceutiques.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **Maladie de la Cavité Nasale**,
avec **1 essai clinique** et **2 publications** soutenant actuellement cette direction (pertinence indirecte).

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Supplément nutritionnel / Acide aminé non essentiel |
| Nouvelle Indication Prédite | Maladie de la cavité nasale |
| Score de Prédiction TxGNN | 99.85% |
| Niveau de Preuve | L4 |
| Statut de Marché | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la glycine est un acide aminé non essentiel aux fonctions physiologiques multiples, et mécanistiquement pourrait être applicable à la maladie de la cavité nasale par le biais de ses propriétés anti-inflammatoires.

La glycine peut théoriquement exercer un effet anti-inflammatoire en agissant sur les récepteurs glycinergiques (GlyR), inhibant l'activation des neutrophiles et réduisant la sécrétion de cytokines pro-inflammatoires (IL-6, TNF-α). Ce mécanisme pourrait, en théorie, atténuer la réaction inflammatoire de la muqueuse nasale et réduire l'infiltration des cellules immunitaires.

Cependant, ce lien mécanistique reste au stade de la spéculation théorique. L'essai clinique identifié (NCT01806675) utilise la glycine uniquement comme composant structural de la séquence RGD d'un traceur PET diagnostique — et non comme agent thérapeutique direct. Les publications disponibles portent sur des études histochimiques animales et des formulations d'adjuvants vaccinaux, sans lien direct avec un usage thérapeutique dans les pathologies nasales.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1–2 | Terminé | 25 | Imagerie PET/CT avec 18F-FPPRGD2 comme biomarqueur d'angiogenèse dans GBM, cancers gynécologiques et carcinome rénal ; la glycine figure uniquement comme composant structural de la séquence RGD du traceur, sans lien direct avec le traitement des maladies nasales |

> ⚠️ **Note de pertinence (Grade C) :** Cet essai ne teste pas la glycine comme traitement des maladies de la cavité nasale. Il ne constitue pas une preuve thérapeutique directe.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Étude in vitro / Formulation | *Chemical & Pharmaceutical Bulletin* | Oligoarginines conjuguées à des polymères comme adjuvants mucosaux nasaux induisant IgG/IgA ; l'arginine (et non la glycine) constitue le composant actif principal |
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Science fondamentale | *Veterinary Pathology* | Histochimie des glycoconjugués de la muqueuse nasale bovine normale et infectée par herpèsvirus BHV1 ; étude animale sans lien thérapeutique direct avec la glycine |

---

## Informations de Marché

Aucune AMM enregistrée pour la glycine à indication thérapeutique validée.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Les preuves disponibles sont insuffisantes pour soutenir la glycine comme traitement des maladies de la cavité nasale. Le seul essai clinique identifié présente une pertinence indirecte (grade C, usage comme excipient structural), et les deux publications sont des études précliniques sans lien thérapeutique direct. Le niveau de preuve L4 et l'absence totale d'essai clinique direct justifient une décision Hold.

**Pour avancer, les éléments suivants sont nécessaires :**

- Données sur le mécanisme d'action (MOA) détaillé de la glycine via DrugBank
- Profil de sécurité complet (avertissements, contre-indications, interactions médicamenteuses)
- Études précliniques in vivo sur modèles de pathologie nasale (rhinite, sinusite)
- Essais cliniques de Phase 1/2 évaluant directement la glycine dans les maladies de la cavité nasale
- Évaluation de la voie d'administration adaptée (nasale topique, orale, etc.)
- Clarification du statut réglementaire (supplément vs médicament) selon le pays cible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

