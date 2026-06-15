---
layout: default
title: Clotrimazole
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 3
---

# Clotrimazole
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

# Clotrimazole : Des Infections Fongiques à l'Acné

## Résumé en Une Phrase

Clotrimazole est un antifongique azolé à large spectre, utilisé mondialement pour le traitement des infections à *Candida* (candidose vaginale, oropharyngée) et des dermatophyties (tinea pedis, tinea corporis) — bien qu'aucune AMM française ne soit enregistrée dans ce système.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Acné**, mais cette direction n'est soutenue que par **1 essai clinique suspendu** et **aucune publication dédiée**.
La base de preuves actuelle est insuffisante pour justifier un développement clinique dans cette indication.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Infections fongiques / Candidose (non approuvé en France — données AMM indisponibles) |
| Nouvelle Indication Prédite | Acné |
| Score de Prédiction TxGNN | 99,86 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de Clotrimazole ne sont pas disponibles dans ce système. D'après les données de la littérature (PMID 24863842), Clotrimazole est un antifongique azolé synthétique qui inhibe l'enzyme CYP51 (14α-déméthylase), bloquant ainsi la biosynthèse de l'ergostérol — constituant essentiel de la membrane fongique. L'accumulation de précurseurs toxiques entraîne l'altération membranaire et la mort cellulaire fongique.

La relation entre ce mécanisme antifongique et l'acné est indirecte et hypothétique. L'acné typique est d'étiologie bactérienne (*Cutibacterium acnes*) et hormonale, deux cibles sur lesquelles Clotrimazole n'exerce pas d'action directe. Le seul lien mécanistique plausible concerne la **folliculite à *Malassezia***, infection fongique des follicules pileux qui peut cliniquement mimer l'acné — et pour laquelle un antifongique azolé serait pertinent. Par ailleurs, certains azolés présentent des propriétés anti-inflammatoires accessoires, mais cet effet n'a pas été validé dans des modèles d'acné.

Le score TxGNN élevé (99,86 %) reflète probablement des connexions non spécifiques entre nœuds de maladies cutanées et agents antimicrobiens dans le graphe de connaissances, plutôt qu'une spécificité mécanistique réelle pour l'acné. L'absence totale de publications scientifiques ciblant cette association renforce cette interprétation.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | ⚠️ Suspendu | 80 | Évaluation de l'efficacité comparative d'une combinaison **Beclométhasone 0,025 % + Gentamicine 0,1 % + Clotrimazole 1 %** chez des patients avec dermatose infectée à lésions symétriques bilatérales. L'essai n'a pas été mené à terme, et Clotrimazole est co-formulé avec un corticostéroïde et un antibiotique — sa contribution individuelle à l'acné ne peut pas être isolée. |

---

## Preuves de la Littérature

Aucune littérature associant Clotrimazole spécifiquement à l'acné n'est disponible actuellement.

---

## Informations de Marché en France

Aucune AMM pour Clotrimazole n'est enregistrée en France dans ce système de données (statut : non commercialisé).

> **Note clinique :** À l'échelle mondiale, Clotrimazole est commercialisé depuis les années 1970 sous de nombreuses marques (Canesten®, Empecid®, etc.) pour les indications fongiques topiques et vaginales. L'absence de données AMM françaises dans ce système est vraisemblablement liée à un périmètre de collecte limité.

---

## Considérations de Sécurité

Veuillez consulter la notice officielle du fabricant pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
L'unique essai clinique identifié est suspendu avant complétion et évalue une combinaison tri-médicamenteuse, rendant impossible toute conclusion sur la contribution isolée de Clotrimazole dans l'acné. Aucune publication scientifique ne soutient cette direction, et le lien mécanistique avec l'acné bactérienne classique est structurellement faible. Le score TxGNN élevé est probablement un artéfact de connectivité dans le graphe de connaissances.

**Pour avancer, les éléments suivants sont nécessaires :**

- Données sur le mécanisme d'action complet (MOA) de Clotrimazole, notamment ses effets anti-inflammatoires potentiels
- Clarification diagnostique de la cible : **acné bactérienne** (*C. acnes*) versus **folliculite fongique à *Malassezia*** — distinction clinique et histologique indispensable avant tout essai
- Études précliniques *in vitro* / *in vivo* sur des modèles de folliculite à *Malassezia* versus acné bactérienne
- Essais cliniques en monothérapie Clotrimazole topique dans l'indication précisément définie

---

> **Note sur les autres indications prédites :** Le modèle TxGNN a également prédit **Vulvovaginite** (rang 2, score 99,59 %, niveau L1 — 22 essais cliniques, 20 publications) et **Vaginite atrophique post-ménopausique** (rang 3, score 99,46 %, niveau L5). La vulvovaginite correspond à l'indication mondiale établie de Clotrimazole (non un repositionnement) ; la vaginite atrophique ne dispose d'aucun mécanisme pertinent ni d'aucune preuve clinique.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

