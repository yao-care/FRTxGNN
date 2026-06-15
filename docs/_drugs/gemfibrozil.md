---
layout: default
title: Gemfibrozil
parent: 僅模型預測 (L5)
nav_order: 135
evidence_level: L5
indication_count: 10
---

# Gemfibrozil
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

# Gemfibrozil : De l'Hypertriglycéridémie à la Polyarthrite Rhumatoïde

## Résumé en Une Phrase

Gemfibrozil est un agent hypolipémiant de la classe des fibrates (dérivé de l'acide fibrique), traditionnellement utilisé pour le traitement de l'hypertriglycéridémie et des dyslipidémies mixtes.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Polyarthrite Rhumatoïde**,
avec **0 essai clinique dédié** et **4 publications** soutenant actuellement cette direction.
La rationale mécanistique via la voie PPARα/NF-κB est biologiquement plausible, mais les preuves cliniques humaines font entièrement défaut.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertriglycéridémie / Dyslipidémie (aucune AMM France disponible) |
| Nouvelle Indication Prédite | Polyarthrite Rhumatoïde |
| Score de Prédiction TxGNN | 99.90% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le pack actuel. Sur la base des informations connues, Gemfibrozil est un agoniste des récepteurs PPARα (Peroxisome Proliferator-Activated Receptor alpha), appartenant à la classe pharmacologique des fibrates. Son mécanisme lipidique principal implique l'activation de la lipoprotéine lipase (LPL), conduisant à une réduction des triglycérides (−40 à 50 %) et à une augmentation du HDL-cholestérol (+10 à 15 %).

Au-delà de son rôle lipidique, la voie PPARα présente un intérêt anti-inflammatoire important : l'activation de PPARα peut inhiber le facteur de transcription NF-κB, réduire la production de cytokines pro-inflammatoires (IL-6, TNF-α), et moduler l'équilibre Treg/Th17. Ces mécanismes sont directement pertinents dans la physiopathologie de la polyarthrite rhumatoïde (PR), maladie auto-immune chronique médiée par ces mêmes voies inflammatoires.

La preuve de concept la plus directe provient de PMID 30074417, qui démontre que l'association gemfibrozil + prednisolone à dose réduite présente une efficacité comparable à la prednisolone à pleine dose dans un modèle animal d'arthrite adjuvante (AIA), suggérant une synergie anti-inflammatoire réelle. Par extension, PMID 41207105 confirme que la classe fibrate (via PPAR-γ notamment) exerce un effet protecteur mesurable dans des modèles expérimentaux de PR. Cependant, aucun essai clinique humain n'a encore été conduit pour cette indication.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [30074417](https://pubmed.ncbi.nlm.nih.gov/30074417/) | 2019 | Étude expérimentale (animal) | Modern Rheumatology | Gemfibrozil (30 mg/kg) + prednisolone à dose réduite équivalent à prednisolone pleine dose dans le modèle AIA chez le rat ; synergie anti-inflammatoire confirmée via PPARα |
| [41207105](https://pubmed.ncbi.nlm.nih.gov/41207105/) | 2026 | Étude animale | International Immunopharmacology | Bezafibrate (pan-PPAR) atténue la PR expérimentale via PPAR-γ, utilisant une approche de repositionnement par docking moléculaire ; soutient l'effet de classe des fibrates sur la voie PPAR dans la PR |
| [20083653](https://pubmed.ncbi.nlm.nih.gov/20083653/) | 2010 | Étude mécanistique | Journal of Immunology | Régulation de Foxp3/Treg par le NO dans les maladies auto-immunes ; fournit un contexte mécanistique sur la balance Treg/Th17, pertinente pour la PR |
| [18039017](https://pubmed.ncbi.nlm.nih.gov/18039017/) | 2007 | Revue / Rapport de cas | Am J Clin Dermatol | Érythème palmaire comme marqueur de la PR et d'autres états systémiques ; pertinence clinique indirecte, non spécifique à gemfibrozil |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Les preuves actuelles se limitent à des études animales et mécanistiques, sans aucun essai clinique humain dédié à la polyarthrite rhumatoïde. Malgré une rationale mécanistique plausible via l'axe PPARα → inhibition NF-κB → réduction des cytokines pro-inflammatoires, le niveau de preuve L3 issu uniquement de modèles précliniques est insuffisant pour recommander un développement clinique immédiat dans cette indication.

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmation complète du mécanisme d'action (MOA) via DrugBank et littérature primaire
- Obtention des données de sécurité complètes (mises en garde, contre-indications, profil DDI — notamment le risque de myopathie documenté avec les fibrates)
- Conduite d'une étude préclinique ciblée dans des modèles humanisés de PR (ex. modèle collagène-induced arthritis CIA) avec gemfibrozil en monothérapie
- Revue systématique de la classe fibrate dans les maladies auto-immunes pour consolider l'effet de classe
- Évaluation du statut réglementaire en France : gemfibrozil n'étant pas commercialisé, tout essai clinique nécessite une autorisation d'importation ou une demande d'autorisation temporaire d'utilisation (ATU/AAP)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

