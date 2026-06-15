---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

# Guselkumab : Du Psoriasis à l'Ostéoporose Induite par les Médicaments

## Résumé en Une Phrase

Guselkumab est un anticorps monoclonal humain ciblant spécifiquement la sous-unité p19 de l'interleukine-23 (IL-23), approuvé à l'international pour le traitement du psoriasis en plaques modéré à sévère, de l'arthrite psoriasique et de la rectocolite hémorragique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Ostéoporose Induite par les Médicaments**,
avec **0 essai clinique** et **0 publication** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Psoriasis en plaques modéré à sévère (approuvé FDA/EMA ; aucune AMM locale enregistrée) |
| Nouvelle Indication Prédite | Ostéoporose Induite par les Médicaments |
| Score de Prédiction TxGNN | 99.84% |
| Niveau de Preuve | L5 |
| Statut de Marché | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Guselkumab est un inhibiteur sélectif de l'IL-23 ciblant la sous-unité p19 — ce qui le distingue des inhibiteurs non sélectifs de p40 (tels qu'ustekinumab) qui bloquent simultanément IL-12 et IL-23. En interrompant le signal IL-23, guselkumab empêche la différenciation des cellules T naïves en lymphocytes Th17, réduisant ainsi la sécrétion d'IL-17A, IL-17F et IL-22. Les données détaillées sur le mécanisme d'action ne sont actuellement pas disponibles dans l'Evidence Pack ; ces informations s'appuient sur la pharmacologie établie de cette classe thérapeutique.

La plausibilité théorique pour l'ostéoporose induite par les médicaments repose sur le rôle régulateur des cellules Th17 dans le remodelage osseux : ces cellules surexpriment RANKL tout en supprimant OPG, favorisant ainsi la différenciation des ostéoclastes et la résorption osseuse. Un inhibiteur de l'IL-23 pourrait donc, en théorie, atténuer cette composante inflammatoire de la perte osseuse.

Cependant, cette connexion mécanistique est **extrêmement faible et indirecte**. Le mécanisme central de l'ostéoporose induite par les médicaments — notamment la toxicité directe des glucocorticoïdes sur les ostéoblastes, la suppression de la formation osseuse et l'accélération de l'apoptose ostéocytaire — est indépendant de l'axe IL-23/Th17. La prédiction TxGNN reflète vraisemblablement une proximité topologique dans le graphe de connaissances biologiques plutôt qu'une plausibilité clinique directe.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction TxGNN pour l'ostéoporose induite par les médicaments est classée L5 — prédiction du modèle uniquement, sans aucune étude réelle pour l'étayer. La connexion mécanistique avec l'axe IL-23/Th17 est indirecte et insuffisante pour justifier un développement actif dans cette indication en l'état actuel des données.

**Pour avancer, les éléments suivants sont nécessaires :**
- Études précliniques démontrant l'effet de l'inhibition de l'IL-23 sur la densité minérale osseuse dans un modèle d'ostéoporose médicamenteuse
- Analyse rétrospective des marqueurs osseux (DMO, biomarqueurs de remodelage osseux : CTX, P1NP) dans les cohortes des essais cliniques existants de guselkumab
- Données de mécanisme d'action complètes (actuellement non disponibles dans l'Evidence Pack)
- Clarification du statut réglementaire local et obtention des données de sécurité issues de la notice officielle

---

> **Note sur le portefeuille de repositionnement :** L'Evidence Pack contient deux indications avec un niveau de preuve L1 bien établi — le **psoriasis** (rang 3, score 99.75%, ≥10 ECR de Phase 3 complétés, décision : Proceed with Guardrails) et la **rectocolite hémorragique** (rang 6, score 99.70%, programme QUASAR Phase 3 avec approbation FDA 2024/5, décision : Proceed with Guardrails). Ces deux indications méritent une évaluation prioritaire séparée.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

