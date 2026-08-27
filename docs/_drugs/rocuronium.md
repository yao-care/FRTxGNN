---
layout: default
title: Rocuronium
parent: 僅模型預測 (L5)
nav_order: 266
evidence_level: L5
indication_count: 10
---

# Rocuronium
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

# Rocuronium : De l'Anesthésie Générale (Blocage Neuromusculaire) au Trouble Migraineux

## Résumé en Une Phrase

Rocuronium est un agent bloquant neuromusculaire non dépolarisant, utilisé en anesthésie générale pour faciliter l'intubation et le relâchement musculaire peropératoire — cet usage ressort du contexte des essais cliniques disponibles, aucune fiche d'indication officielle n'ayant été retrouvée dans les sources consultées. Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Trouble Migraineux** (migraine disorder), avec un score de prédiction de **99,90 %**, mais cette direction n'est actuellement soutenue que par **1 essai clinique non pertinent** et **aucune publication scientifique dédiée**.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Blocage neuromusculaire / anesthésie générale (non documenté formellement dans les sources — donnée manquante, cf. DG002) |
| Nouvelle Indication Prédite | Trouble Migraineux (migraine disorder) |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les sources structurées (DrugBank marque ce champ comme donnée manquante à haute priorité, DG002). Sur la base du contexte disponible dans les essais cliniques associés, Rocuronium est un bloqueur neuromusculaire non dépolarisant qui agit sur les récepteurs nicotiniques de l'acétylcholine au niveau de la jonction neuromusculaire du muscle squelettique. Il ne franchit pas la barrière hémato-encéphalique et n'a donc aucune action centrale connue.

Contrairement à l'exemple type de repositionnement, l'analyse mécanistique fournie avec ce dossier conclut elle-même qu'**il n'existe aucun lien mécanistique plausible** entre le blocage neuromusculaire périphérique et le trouble migraineux, dont la physiopathologie repose sur le système trigémino-vasculaire central et la voie du CGRP. L'unique essai clinique relié à cette prédiction (NCT01431326) est une étude pharmacocinétique pédiatrique de « médicaments standards de soins », dans laquelle le rocuronium n'apparaît que comme un des nombreux médicaments surveillés au hasard des protocoles chirurgicaux — il ne s'agit en aucun cas d'un essai interventionnel ciblant la migraine.

Ce profil est cohérent avec un **signal probablement faux positif**, généré par une co-occurrence fortuite dans le graphe de connaissances plutôt que par une réelle proximité pharmacologique. Par comparaison, un signal beaucoup plus modeste mais mécanistiquement plus crédible existe dans ce même dossier : le remplacement de la succinylcholine par le rocuronium (avec réversion par sugammadex) pourrait réduire les myalgies/céphalées post-anesthésiques liées aux fasciculations musculaires (voir « Céphalée » / *headache disorder*, rang 10, niveau de preuve L3) — mais ce mécanisme concerne une céphalée post-procédurale ponctuelle, pas le trouble migraineux chronique visé par la prédiction principale.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Terminé | 3520 | Étude pharmacocinétique observationnelle chez l'enfant, portant sur plusieurs « médicaments peu étudiés » administrés selon les soins standards ; le rocuronium n'y est qu'un des médicaments surveillés (contexte chirurgical/anesthésique général), sans aucune évaluation de la migraine. |

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Aucune AMM enregistrée — selon les données consultées, Rocuronium n'est pas commercialisé en France (0 licence recensée).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction principale (Trouble Migraineux) ne dispose d'aucune preuve clinique ou littéraire pertinente — le seul essai relié est une étude pharmacocinétique pédiatrique sans lien avec la migraine — et l'analyse mécanistique fournie identifie elle-même ce signal comme un probable artefact du graphe de connaissances, en l'absence de toute action centrale connue du rocuronium.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les mises en garde/contre-indications de la notice TFDA/ANSM (donnée bloquante DG001) et les données de mécanisme d'action (DG002) auprès de DrugBank, préalables indispensables avant toute évaluation de sécurité S1
- Clarifier l'indication d'origine officielle du produit (actuellement absente des sources structurées)
- Si une piste de recherche doit être retenue dans ce dossier, envisager plutôt le signal secondaire plus modeste mais mécanistiquement mieux étayé — la réduction des myalgies/céphalées post-anesthésiques via l'usage du rocuronium/sugammadex à la place de la succinylcholine (rang 10, niveau L3, stade S1) — comme question de recherche distincte, ciblée et non extrapolable au trouble migraineux chronique
- Étant donné l'absence de commercialisation en France (0 AMM), toute suite réglementaire nécessiterait une démarche d'enregistrement complète
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

