---
layout: default
title: Lomustine
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Lomustine
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

# LOMUSTINE : Évaluation de Repositionnement — Données Insuffisantes

## Résumé en Une Phrase

LOMUSTINE est un agent alkylant de la classe des nitrosourées, reconnu pour sa capacité à franchir la barrière hémato-encéphalique et historiquement indiqué dans le traitement des tumeurs cérébrales et de la maladie de Hodgkin.
Le pack de données actuel **ne contient aucune prédiction TxGNN** pour ce médicament, ce qui empêche toute évaluation formelle de repositionnement.
Des lacunes critiques (indications prédites, mécanisme d'action, données de sécurité) doivent être comblées avant de poursuivre l'analyse.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Non renseignée dans ce pack |
| Nouvelle Indication Prédite | Aucune prédiction TxGNN disponible |
| Score de Prédiction TxGNN | — |
| Niveau de Preuve | L5 — données manquantes, évaluation impossible |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce pack. Sur la base des informations publiques connues, LOMUSTINE appartient à la classe des nitrosourées — agents alkylants capables de former des liaisons croisées avec l'ADN et de traverser la barrière hémato-encéphalique. Cette propriété pharmacocinétique distinctive le distingue de la majorité des chimiothérapies et constitue sa valeur clinique principale dans les tumeurs du système nerveux central.

Aucune indication prédite par TxGNN n'étant présente dans le pack actuel, il n'est pas possible de fournir d'analyse sur la relation mécanistique entre l'indication d'origine et une cible thérapeutique potentielle. Cette section sera complétée dès que les prédictions TxGNN seront disponibles pour DB01206.

---

## Cytotoxicité

LOMUSTINE est un médicament antinéoplasique cytotoxique de la famille des nitrosourées, utilisé en chimiothérapie systémique.

| Élément | Contenu |
|---|---|
| Classification de Cytotoxicité | Cytotoxique conventionnel — classe Nitrosourée (agent alkylant) |
| Risque de Myélosuppression | **Élevé** — myélosuppression retardée et cumulative, caractéristique pharmacologique propre aux nitrosourées (nadir leucocytaire à ~5–6 semaines) |
| Classification d'Émétogénicité | **Élevée** — LOMUSTINE est une forme orale hautement émétogène |
| Éléments de Surveillance | NFS avec différentielle toutes les 6 semaines, plaquettes, fonction hépatique et rénale |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques (préparation sous hotte, équipements de protection individuelle) |

---

## Considérations de Sécurité

Veuillez consulter la notice officielle pour les informations de sécurité complètes (avertissements, contre-indications et interactions médicamenteuses non disponibles dans ce pack).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le pack de données actuel ne contient aucune indication prédite par TxGNN pour LOMUSTINE (DB01206), et l'ensemble des données de sécurité (avertissements principaux, contre-indications) sont manquantes. En l'absence de ces éléments fondamentaux, il est impossible de conduire une évaluation de repositionnement fiable.

**Pour avancer, les éléments suivants sont nécessaires :**

- **Prédictions TxGNN** : Générer les scores d'indication pour DB01206 (LOMUSTINE) via le pipeline TxGNN
- **Mécanisme d'action (MOA)** : Consulter l'API DrugBank pour DB01206 afin d'obtenir les données de mécanisme détaillées
- **Avertissements et contre-indications** : Télécharger et analyser la notice officielle (ANSM ou EMA) — statut identifié comme lacune bloquante (DG001)
- **Statut réglementaire européen** : Vérifier la présence d'une AMM EMA ou dans des pays membres (LOMUSTINE est commercialisé dans plusieurs pays européens sous des dénominations locales)
- **Indications approuvées** : Renseigner `original_indications` à partir des données DrugBank ou de l'étiquetage EMA
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

