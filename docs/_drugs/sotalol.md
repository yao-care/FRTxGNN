---
layout: default
title: Sotalol
parent: 僅模型預測 (L5)
nav_order: 283
evidence_level: L5
indication_count: 7
---

# Sotalol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Sotalol : Du Contrôle du Rythme Cardiaque (Fibrillation/Flutter Auriculaire) au Syndrome du Sinus Malade de Type 2

## Résumé en Une Phrase

Le sotalol est cliniquement connu comme antiarythmique de classe III à action bêta-bloquante, utilisé notamment pour le contrôle du rythme dans la fibrillation/flutter auriculaire (les indications d'origine ne sont pas formellement documentées dans le dossier source ; cette information provient du contexte pharmacologique fourni dans l'Evidence Pack). Le modèle TxGNN prédit avec le score le plus élevé (**99.76 %**) une association avec la **Maladie du Sinus de Type 2 (Autosomique Dominante)**, mais cette prédiction est en réalité jugée **mécanistiquement contre-indiquée** plutôt que thérapeutique, sans aucun essai clinique ni publication pour la soutenir (**niveau de preuve L5**). Parmi les 7 candidats évalués, seule l'indication de rang 4 (« trouble d'AVC », en lien avec le contrôle du rythme dans la fibrillation auriculaire) dispose d'un support réel (**22 essais cliniques identifiés, 20 publications, niveau L2**).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée dans les données disponibles (médicament non commercialisé en France ; rôle pharmacologique connu : antiarythmique de classe III / bêta-bloquant, utilisé pour le contrôle du rythme dans la fibrillation/flutter auriculaire) |
| Nouvelle Indication Prédite | Maladie du Sinus de Type 2, Autosomique Dominante (*sick sinus syndrome 2, autosomal dominant*) |
| Score de Prédiction TxGNN | 99.76 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier source (Data Gap). Sur la base des informations contenues dans l'Evidence Pack, le sotalol combine un blocage bêta-adrénergique non sélectif et un blocage des canaux potassiques (effet de classe III), ce qui lui confère un effet chronotrope négatif — il ralentit la fréquence cardiaque et l'automaticité du nœud sinusal.

**Cette prédiction n'est pas mécanistiquement raisonnable.** Le syndrome du sinus malade se caractérise précisément par une défaillance de l'automaticité du nœud sinusal et une bradycardie. L'effet pharmacologique du sotalol va donc dans le sens **opposé** au besoin thérapeutique : au lieu de corriger la dysfonction sinusale, il risquerait de l'aggraver. L'évaluation associée à cette prédiction indique explicitement qu'il s'agit probablement d'un **signal faussement positif**, généré par une proximité topologique dans le réseau maladie-médicament de TxGNN plutôt que par une logique pharmacologique réelle.

À titre de comparaison, la prédiction de rang 4 (« trouble d'AVC ») repose sur un mécanisme beaucoup plus plausible : en maintenant le rythme sinusal chez les patients en fibrillation/flutter auriculaire, le sotalol pourrait réduire indirectement le risque d'AVC cardio-embolique — un usage qui prolonge une indication pharmacologique déjà connue plutôt qu'un véritable repositionnement.

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
- Le lien mécanistique entre le sotalol et la Maladie du Sinus de Type 2 est **contre-indiqué** plutôt que thérapeutique (effet bradycardisant du médicament sur une pathologie de bradycardie du nœud sinusal), et aucun essai clinique ni publication ne soutient cette direction (niveau de preuve L5).
- Le score TxGNN élevé (99.76 %) reflète très probablement une proximité de réseau maladie-médicament plutôt qu'une hypothèse pharmacologique valide.
- Le seul candidat parmi les 7 prédictions ayant un support de preuve substantiel est le rang 4 (« trouble d'AVC », L2, Research Question), mais il correspond à une extension du rôle antiarythmique déjà connu du sotalol dans la fibrillation auriculaire, plutôt qu'à un nouveau repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA) du sotalol (DG002, actuellement Data Gap)
- Mises en garde et contre-indications officielles de la notice / TFDA-équivalent français (DG001, bloquant pour l'évaluation de sécurité S1)
- Si l'indication « trouble d'AVC » est retenue pour investigation, une revue qualitative des essais de grade A/B (notamment NCT00007605, NCT05279833) et une clarification du critère d'évaluation (maintien du rythme sinusal vs réduction directe de l'AVC)
- Confirmation qu'aucun développement clinique ne doit être engagé sur la piste « Maladie du Sinus de Type 2 » compte tenu du signal contre-indicatoire identifié
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

