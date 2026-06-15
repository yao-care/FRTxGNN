---
layout: default
title: Doravirine
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 3
---

# Doravirine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Doravirine : De l'Infection à VIH-1 à l'Infection à Virus de l'Immunodéficience Simienne

## Résumé en Une Phrase

Doravirine est un inhibiteur non nucléosidique de la transcriptase inverse (NNRTI), cliniquement approuvé pour le traitement de l'infection à VIH-1 chez l'adulte (commercialisé sous le nom Pifeltro® dans d'autres pays).
Le modèle TxGNN prédit qu'il pourrait être efficace contre l'**infection à Virus de l'Immunodéficience Simienne (SIV)**,
avec **0 essai clinique** et **1 publication indirecte** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Infection à VIH-1 (NNRTI — inhibiteur non nucléosidique de la transcriptase inverse) |
| Nouvelle Indication Prédite | Infection à Virus de l'Immunodéficience Simienne (SIV) |
| Score de Prédiction TxGNN | 99.93% |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la fiche. Sur la base des informations connues, Doravirine est un NNRTI qui se lie de manière non compétitive à la poche hydrophobe de la transcriptase inverse (NNBP, *Non-Nucleoside Binding Pocket*). Il inhibe ainsi la réplication virale en bloquant l'activité polymérase de la RT. Son efficacité dans le traitement de l'infection à VIH-1 est cliniquement établie.

Le SIV (*Simian Immunodeficiency Virus*) et le VIH-1 appartiennent tous deux au genre des lentivirus de primates et partagent une homologie structurelle élevée au niveau de la transcriptase inverse — en particulier au niveau du NNBP, la poche de liaison de Doravirine. Les résidus clés de cette poche sont hautement conservés entre les deux virus, ce qui constitue une base mécanistique rationnelle pour envisager une activité anti-SIV.

Cependant, la prédiction reste au stade de l'analogie mécanistique. Aucune donnée d'activité directe de Doravirine sur des isolats de SIV — que ce soit in vitro ou in vivo — n'est actuellement disponible. La haute probabilité attribuée par TxGNN reflète vraisemblablement la forte conservation structurale SIV/VIH-1 dans le graphe de connaissances biomédicales, et non une preuve clinique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Revue / Résumé Phase 1-2 | *Current Opinion in HIV and AIDS* | Discussion du rôle potentiel de l'islatravir (inhibiteur de translocation de la RT) dans le traitement et la prévention du VIH-1 — référence mécanistique indirecte pour la classe des inhibiteurs de la RT |

> **Note :** Cette publication porte sur l'islatravir, non sur Doravirine, et ne concerne pas directement le SIV. Elle est incluse comme contexte mécanistique pour la classe NNRTI/RT-inhibiteurs.

---

## Informations de Marché en France

Doravirine ne dispose d'aucune AMM en France. Aucune donnée d'enregistrement disponible dans cette base.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose exclusivement sur une analogie mécanistique (homologie de la NNBP entre SIV RT et VIH-1 RT), sans aucun essai clinique ni étude d'activité directe sur le SIV. Le niveau de preuve L4 est insuffisant pour justifier une progression vers des études cliniques à ce stade.

**Pour avancer, les éléments suivants sont nécessaires :**
- Études in vitro de l'activité antivirale de Doravirine sur des isolats de SIV (IC₅₀, index de résistance)
- Données complètes sur le mécanisme d'action (MOA) et le profil de sélectivité de la NNBP (source : DrugBank API ou littérature primaire)
- Profil de sécurité complet : avertissements, contre-indications, interactions médicamenteuses (source : notice TFDA/EMA)
- Évaluation du statut réglementaire en France via EMA/ANSM pour tout usage potentiel
- Clarification du contexte de recherche : application vétérinaire (primates non humains) ou modèle préclinique pour l'infection à VIH-1 humain
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

