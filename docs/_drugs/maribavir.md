---
layout: default
title: Maribavir
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 0
---

# Maribavir
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

# MARIBAVIR : De l'Infection à CMV au Repositionnement — Évaluation Préliminaire

## Résumé en Une Phrase

Maribavir (Livtencity®) est un antiviral ciblant la kinase UL97 du cytomégalovirus (CMV), approuvé par la FDA en 2021 pour le traitement des infections à CMV réfractaires ou résistantes chez les patients transplantés.
Le modèle TxGNN **n'a pas encore généré de prédictions d'indications** pour cette molécule dans la version actuelle du pipeline.
L'évaluation de repositionnement ne peut être complétée sans données de prédiction ni données de sécurité validées.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Infection/maladie à CMV post-transplantation réfractaire (FDA 2021) |
| Nouvelle Indication Prédite | Aucune prédiction TxGNN disponible |
| Score de Prédiction TxGNN | N/A |
| Niveau de Preuve | L5 (modèle sans prédiction — données insuffisantes) |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le mécanisme d'action détaillé de Maribavir est classé comme **[Data Gap]** dans le pack d'évidence actuel. Sur la base des informations publiques connues, Maribavir est un inhibiteur de la protéine kinase UL97 du CMV. Cette kinase virale joue un rôle essentiel dans la réplication de l'ADN viral et l'export nucléaire des capsides virales. En bloquant UL97, Maribavir interrompt le cycle réplicatif du CMV à des stades multiples, ce qui le distingue mécanistiquement des antiviraux classiques (ganciclovir, foscarnet, cidofovir) ciblant l'ADN polymérase.

La pertinence d'un repositionnement vers d'autres indications (autres infections virales à herpèsvirus, immunosuppression post-greffe, ou pathologies liées à des kinases homologues) est mécanistiquement plausible mais **ne peut être évaluée** en l'absence de prédictions TxGNN et de données MOA complètes dans le système.

> Actuellement, aucune prédiction d'indication n'est disponible dans `predicted_indications`. La section d'analyse de repositionnement est suspendue jusqu'à l'exécution complète du pipeline TxGNN.

---

## Preuves d'Essais Cliniques

Aucune prédiction d'indication disponible — tableau d'essais cliniques non applicable dans cette version.

---

## Preuves de la Littérature

Aucune prédiction d'indication disponible — tableau de littérature non applicable dans cette version.

---

## Informations de Marché en France

Maribavir n'a **aucune AMM enregistrée en France** dans les données actuelles. Il n'est pas commercialisé sur le territoire français. À noter qu'une autorisation FDA (États-Unis) existe sous le nom Livtencity® depuis novembre 2021, et une autorisation EMA a été accordée (Livtencity®, indication CMV réfractaire post-transplantation), mais ces autorisations ne sont pas reflétées dans les données réglementaires françaises de ce pack.

---

## Cytotoxicité

Cette section n'est pas applicable. Maribavir est un antiviral et n'appartient pas à la classe des médicaments antinéoplasiques/cytotoxiques.

---

## Considérations de Sécurité

Les données de sécurité spécifiques (mises en garde, contre-indications, interactions médicamenteuses) n'ont pas été récupérées dans ce pack d'évidence. Deux lacunes bloquantes ont été identifiées :

- **DG001 (Bloquant)** : Données de la notice réglementaire (ANSM/TFDA) absentes — impossible de compléter l'évaluation de sécurité initiale S1.
- **DG002 (Élevé)** : Mécanisme d'action non renseigné — impact sur l'analyse mécanistique de repositionnement.

> Veuillez consulter la notice officielle et le résumé des caractéristiques du produit (RCP EMA) pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Ce dossier présente deux lacunes bloquantes (DG001, DG002) et une absence totale de prédictions TxGNN, rendant toute évaluation de repositionnement prématurée. Le profil mécanistique de Maribavir est scientifiquement intéressant, mais aucune direction de repositionnement ne peut être validée sans les sorties du modèle.

**Pour avancer, les éléments suivants sont nécessaires :**

1. **Exécuter le pipeline TxGNN** pour générer les `predicted_indications` (score, rang, preuves associées)
2. **Récupérer la notice ANSM/EMA** (RCP Livtencity®) pour combler DG001 — mises en garde, contre-indications, interactions
3. **Interroger l'API DrugBank** (DB06234) pour obtenir le MOA structuré (DG002)
4. **Vérifier le statut EMA** : Livtencity® dispose d'une AMM européenne — vérifier si la France est incluse dans la distribution effective
5. **Relancer l'évaluation complète** une fois les données ci-dessus intégrées dans le pack v5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

