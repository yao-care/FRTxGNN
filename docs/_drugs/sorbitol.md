---
layout: default
title: Sorbitol
parent: 僅模型預測 (L5)
nav_order: 282
evidence_level: L5
indication_count: 1
---

# Sorbitol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Sorbitol : De l'Usage Osmotique (Laxatif/Diurétique) à l'Hyperthermie Maligne d'Effort

## Résumé en Une Phrase

Sorbitol est pharmacologiquement connu comme agent osmotique (laxatif/diurétique osmotique), mais son indication d'origine formelle et son mécanisme d'action détaillé ne sont pas documentés dans ce pack de preuves. Le modèle TxGNN prédit qu'il pourrait être associé à l'**hyperthermie maligne d'effort**, avec un score de similarité de **99,40%**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée dans ce pack (aucune AMM en France ; usage pharmacologique connu : agent osmotique) |
| Nouvelle Indication Prédite | Hyperthermie maligne d'effort (exercise-induced malignant hyperthermia) |
| Score de Prédiction TxGNN | 99,40% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action de sorbitol ne sont pas disponibles. Sur la base des informations pharmacologiques connues, sorbitol agit comme agent osmotique non absorbé, utilisé comme laxatif ou diurétique osmotique — aucune donnée ne relie ce mode d'action au récepteur RYR1, à la régulation du canal calcique du muscle squelettique, ou à la voie d'excitation-contraction impliquée dans l'hyperthermie maligne.

L'hyperthermie maligne d'effort est une pathologie pharmacogénétique rare, liée à des mutations des gènes *RYR1*/*CACNA1S*. Aucun lien biologique identifiable n'existe entre cette voie et l'action métabolique connue du sorbitol (activité osmotique, polyol non métabolisé).

Cette prédiction repose uniquement sur une similarité d'embedding du modèle TxGNN (score 0,994), sans support mécanistique. Elle doit être considérée comme une association pilotée par les données, à faible degré de confiance, et ne peut être exclue d'être un artefact du modèle ou une association indirecte liée à une comorbidité plutôt qu'à une relation causale.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le niveau de preuve est L5 (prédiction du modèle seule, sans essai clinique ni littérature), et le mécanisme d'action proposé par le modèle n'a aucun support biologique identifiable — le pack de preuves qualifie lui-même ce lien de faible crédibilité, potentiellement du bruit de modèle. Aucune donnée de sécurité (mises en garde, contre-indications, DDI) n'est disponible, ce qui empêche toute évaluation de sécurité initiale (S1).

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications TFDA (lacune bloquante DG001) — nécessaires avant toute évaluation de sécurité S1
- Mécanisme d'action (MOA) détaillé de sorbitol (lacune DG002), pour évaluer la plausibilité mécanistique de la piste
- Indication(s) d'origine formellement documentée(s), actuellement absentes du pack
- Étude préclinique ou mécanistique indépendante testant un lien entre sorbitol et la voie RYR1/hyperthermie maligne, avant d'envisager tout essai clinique
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

