---
layout: default
title: Glucarpidase
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
---

# Glucarpidase
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

# Glucarpidase : De la Toxicité au Méthotrexate au Cataracte Diabétique

## Résumé en Une Phrase

Glucarpidase est une carboxypeptidase recombinante utilisée pour neutraliser la toxicité du méthotrexate (MTX) à haute dose chez les patients en insuffisance rénale, en hydrolysant le MTX en métabolites inactifs.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Cataracte Diabétique**,
avec **0 essai clinique** et **0 publication** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Non disponible (aucune AMM enregistrée dans le dossier) |
| Nouvelle Indication Prédite | Cataracte Diabétique |
| Score de Prédiction TxGNN | 99,85% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations connues, glucarpidase est une enzyme de la classe des carboxypeptidases, spécifiquement conçue pour hydrolyser le méthotrexate (MTX) en ses métabolites inactifs (DAMPA et glutamate). Son activité pharmacologique est ainsi entièrement centrée sur la voie de détoxification du folate/MTX, et non sur un effet thérapeutique direct propre.

La cataracte diabétique résulte principalement de l'activation de l'aldose réductase par l'hyperglycémie chronique, entraînant une accumulation de sorbitol dans le cristallin et des dommages osmotiques progressifs. Ce mécanisme pathologique est totalement indépendant de la voie métabolique folate/MTX sur laquelle opère glucarpidase. Les analyses mécanistiques figurant dans le dossier confirment l'absence de lien biologique direct : aucun point d'intersection n'a été identifié entre l'action enzymatique de glucarpidase et la physiopathologie du cristallin diabétique.

Il convient de souligner que les 10 prédictions de rang le plus élevé concernent toutes des formes de cataracte ou de pathologie oculaire diabétique. Cette concentration atypique sur un seul domaine nosologique suggère un probable artefact de regroupement dans le graphe de connaissances (Knowledge Graph) du modèle TxGNN — lié à la densité de connectivité des nœuds de cataracte dans le graphe — plutôt qu'un signal pharmacologique réel.

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
L'absence totale de preuves cliniques et de littérature (niveau L5), l'inexistence de mécanisme biologique plausible reliant glucarpidase à la pathologie du cristallin, et la distribution anormale des prédictions TxGNN (concentration sur les cataractes) indiquent un artefact de modélisation et ne justifient pas la poursuite de cette piste de repositionnement en l'état.

**Pour avancer, les éléments suivants sont nécessaires :**

- Obtention des données complètes de mécanisme d'action (MOA) via DrugBank — actuellement manquantes (DG002)
- Récupération des informations de sécurité et des contre-indications depuis la notice officielle — actuellement manquantes (DG001)
- Analyse critique de l'artefact de regroupement dans le graphe de connaissances TxGNN concernant les nœuds de type cataracte
- Identification d'un mécanisme biologique crédible reliant la voie folate/MTX aux pathologies oculaires avant toute évaluation clinique
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

