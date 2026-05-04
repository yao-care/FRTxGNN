---
layout: default
title: Alizapride
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 0
---

# Alizapride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Alizapride : Rapport d'Évaluation Préliminaire

## Résumé en Une Phrase

Alizapride (DB01425) est un benzamide substitué connu comme antiémétique antagoniste des récepteurs dopaminergiques D2, utilisé dans certains pays européens pour le traitement des nausées et vomissements. Cependant, **aucune nouvelle indication n'a été prédite** par le modèle TxGNN à ce stade, et le médicament ne dispose d'**aucune AMM en France** selon les données réglementaires disponibles. Le dossier présente des **lacunes de données critiques** (mécanisme d'action détaillé, mises en garde, contre-indications) qui empêchent une évaluation complète.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans le dossier |
| Nouvelle Indication Prédite | Aucune prédiction TxGNN disponible |
| Score de Prédiction TxGNN | — |
| Niveau de Preuve | L5 (aucune étude réelle associée) |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Cette Évaluation est-elle Préliminaire ?

Alizapride est un dérivé benzamide, structurellement apparenté au métoclopramide et au sulpiride. Il agit principalement comme **antagoniste des récepteurs dopaminergiques D2**, ce qui explique son activité antiémétique en bloquant la stimulation dopaminergique au niveau de la zone chémoréceptrice (area postrema). Ce mécanisme est bien établi dans la classe des benzamides prokinétiques.

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier fourni (identifié comme lacune de données DG002). Sur la base des informations connues, l'alizapride appartient à la classe des antagonistes dopaminergiques benzamides, dont l'efficacité antiémétique est bien documentée, mais aucune extrapolation vers de nouvelles indications n'a pu être réalisée par le modèle TxGNN.

L'absence totale de prédictions TxGNN (`predicted_indications` vide) peut s'expliquer par plusieurs facteurs : une représentation insuffisante du médicament dans le graphe de connaissances thérapeutiques, un manque de données d'entraînement spécifiques, ou encore l'absence de signaux significatifs reliant ce composé à de nouvelles pathologies au-delà de son utilisation antiémétique établie.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé à une nouvelle indication n'est enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée à une nouvelle indication n'est disponible actuellement.

---

## Informations de Marché en France

Alizapride ne dispose d'**aucune AMM** recensée dans les données réglementaires fournies. Le statut de marché est « Non commercialisé ».

> **Note :** L'alizapride a historiquement été commercialisé dans certains pays européens sous diverses dénominations commerciales (ex. Plitican®), mais aucune licence active n'a été identifiée dans le périmètre de cette évaluation.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

> **Lacune de données critique (DG001)** : Les mises en garde, contre-indications et informations de la notice n'ont pas pu être récupérées. Cette lacune est classée comme **bloquante** et empêche l'entrée en phase d'évaluation initiale de sécurité (S1).

> **Note générale sur la classe** : Les antagonistes dopaminergiques D2 (benzamides) sont associés à des risques connus incluant des effets extrapyramidaux, une hyperprolactinémie, et un allongement de l'intervalle QT. Ces risques de classe doivent être pris en compte dans toute évaluation future.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le dossier d'alizapride présente des lacunes de données majeures à tous les niveaux : aucune prédiction TxGNN, aucune AMM active, aucune donnée de sécurité exploitable, et un mécanisme d'action non documenté dans le dossier. En l'état, il n'existe aucune base suffisante pour avancer vers un repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- ☐ **Résolution de DG001 (Bloquant)** : Récupérer les mises en garde et contre-indications depuis la notice officielle (source : ANSM / bases réglementaires)
- ☐ **Résolution de DG002 (Haute priorité)** : Documenter le mécanisme d'action détaillé via l'API DrugBank
- ☐ **Enrichissement du graphe de connaissances** : Vérifier la représentation d'alizapride dans le graphe TxGNN et relancer la prédiction si le nœud médicament est absent ou sous-connecté
- ☐ **Recherche bibliographique élargie** : Explorer manuellement PubMed pour des signaux de repositionnement hors périmètre TxGNN (ex. propriétés anti-inflammatoires des benzamides, effets sur la motilité gastro-intestinale dans d'autres pathologies)
- ☐ **Évaluation du statut réglementaire** : Confirmer si l'alizapride est toujours commercialisé dans d'autres juridictions (EMA, pays européens individuels)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

