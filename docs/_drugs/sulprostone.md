---
layout: default
title: Sulprostone
parent: 僅模型預測 (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
---

# Sulprostone
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

# Sulprostone : De la Contraction Utérine à la Cataracte Tétanique

## Résumé en Une Phrase

Sulprostone est un analogue de la prostaglandine E2 (PGE2), utilisé à l'origine comme utérotonique pour la contraction utérine et l'induction du travail (information tirée du rationnel mécanistique du dossier, le champ MOA formel étant lui-même une lacune de données). Le modèle TxGNN prédit un score élevé (**99.86%**) pour la **cataracte tétanique** (tetanic cataract), mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction — le rationnel associé indique lui-même qu'il s'agit d'un terme d'ontologie non standard, sans hypothèse mécanistique établie.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Contraction utérine / Induction du travail (utérotonique) — déduit du rationnel mécanistique, non confirmé par un champ d'indication officiel |
| Nouvelle Indication Prédite | Cataracte tétanique (tetanic cataract) |
| Score de Prédiction TxGNN | 99.86% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles formellement (lacune de données signalée comme bloquante). Sur la base des informations présentes dans le dossier de preuves, sulprostone est décrit comme un agoniste de la prostaglandine E2 (récepteur EP), dont l'efficacité dans la contraction utérine et l'induction du travail est bien établie.

Cependant, le rationnel mécanistique associé à chacune des indications prédites (cataracte sous ses diverses formes, rétinopathie diabétique) indique explicitement l'**absence de lien mécanistique connu** entre la signalisation PGE2/EP et la pathologie du cristallin — que ce soit via le métabolisme du cristallin, la voie des polyols (aldose réductase) ou la glycation des protéines cristalliniennes. Pour la rétinopathie diabétique (rang 10), le dossier note une plausibilité mécanistique légèrement supérieure, la signalisation PGE2 ayant un lien indirect théorique avec l'inflammation et l'angiogenèse (VEGF), mais sans aucune donnée préclinique ou clinique pour l'étayer.

Un point de vigilance supplémentaire : les scores TxGNN des indications classées 1 à 5 sont strictement identiques (0.9986011385917664), ce qui suggère un artefact de regroupement topologique dans le graphe de connaissances plutôt qu'un signal différencié et fiable pour chaque indication.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement

---

## Informations de Marché en France

Aucune AMM enregistrée en France (statut : non commercialisé, 0 licence recensée).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Toutes les indications prédites (10/10) sont classées niveau de preuve L5 — prédiction du modèle uniquement, sans essai clinique ni publication à l'appui, et le rationnel mécanistique du dossier lui-même conteste la plausibilité biologique des principales candidates (cataracte).
- Une lacune de données bloquante (DG001 — mises en garde/contre-indications TFDA) empêche toute évaluation de sécurité S1, indépendamment de la force de la prédiction.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice officielle et les mises en garde/contre-indications (DG001, bloquant)
- Obtenir des données de mécanisme d'action détaillées via DrugBank ou littérature primaire (DG002)
- Clarifier la terminologie d'ontologie non standard des indications prédites (ex. « tetanic cataract », « craniostenosis cataract ») avant toute analyse supplémentaire
- Rechercher un signal préclinique ou clinique réel, en priorité pour la rétinopathie diabétique, seule candidate avec un rationnel mécanistique partiellement défendable

*Note : 9 autres indications candidates (variantes de cataracte et rétinopathie diabétique, scores 99.67–99.86%) partagent le même profil — niveau L5, aucun essai ni littérature, recommandation Hold.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

