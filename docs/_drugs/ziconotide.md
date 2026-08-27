---
layout: default
title: Ziconotide
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
---

# Ziconotide
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

# Ziconotide : De la Douleur Chronique Sévère à la Migraine

## Résumé en Une Phrase

Ziconotide (DrugBank DB06283) est un bloqueur des canaux calciques de type N (Cav2.2), utilisé en administration intrathécale pour la douleur chronique sévère réfractaire. Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Migraine**, mais cette direction n'est actuellement soutenue que par **1 publication** (un rapport de cas), sans aucun essai clinique enregistré.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Douleur chronique sévère nécessitant une analgésie intrathécale *(mentionnée dans la littérature du dossier ; aucune donnée d'AMM disponible — voir ci-dessous)* |
| Nouvelle Indication Prédite | Migraine |
| Score de Prédiction TxGNN | 99.92 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

> Note sur l'indication originale : le champ réglementaire `taiwan_regulatory.licenses` est vide (le produit n'est pas commercialisé en France, 0 AMM), et `drug.original_indications` n'est pas renseigné dans ce dossier. La mention "douleur chronique sévère" provient du contexte de la publication associée à la prédiction n°1 (PMID 26392785), pas d'un document réglementaire.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le champ de mécanisme d'action officiel (`original_moa`) est marqué comme donnée manquante (DG002 — sévérité High). Sur la base des informations disponibles dans la littérature et l'analyse de rationnel du modèle, le ziconotide est un bloqueur des canaux calciques voltage-dépendants de type N (Cav2.2), agissant au niveau présynaptique de la corne dorsale de la moelle épinière pour inhiber la libération de neurotransmetteurs pronociceptifs comme la substance P et le CGRP.

Le lien avec la migraine repose sur le fait que la voie du CGRP est un mécanisme central de la physiopathologie migraineuse : en théorie, un blocage en amont de la libération de CGRP pourrait avoir un effet pertinent. Cependant, le ziconotide est administré exclusivement par voie intrathécale, un mode d'administration très différent des traitements anti-migraineux usuels (voie orale, sous-cutanée), avec une fenêtre de sécurité étroite (effets psychiatriques et cognitifs documentés dans son usage actuel).

À ce stade, la seule preuve directe est un rapport de cas isolé décrivant une résolution de migraine chronique réfractaire sous ziconotide intrathécal — un signal exploratoire, non une démonstration causale.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26392785](https://pubmed.ncbi.nlm.nih.gov/26392785/) | 2015 | Rapport de cas | Journal of Pain Research | Résolution de céphalées migraineuses chroniques chez un patient sous ziconotide intrathécal ; le ziconotide y est décrit comme un bloqueur calcique utilisé pour la douleur chronique sévère sans tolérance/dépendance associée aux opioïdes |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

> À noter : le dossier signale un écart de données bloquant (DG001, sévérité *Blocking*) concernant les mises en garde et contre-indications TFDA — cette lacune empêche à elle seule le passage à l'étape d'évaluation de sécurité S1.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La preuve disponible se limite à un seul rapport de cas (niveau L4, étape S1 « Research Question »), sans aucun essai clinique enregistré. Le médicament n'est pas commercialisé en France (0 AMM) et les données de sécurité réglementaires (mises en garde, contre-indications TFDA) sont totalement manquantes avec une sévérité bloquante. La voie d'administration intrathécale limite en outre fortement la transposabilité vers une population migraineuse ambulatoire.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice/RCP TFDA (mises en garde, contre-indications) — DG001, bloquant
- Confirmer le mécanisme d'action formel via DrugBank ou une autre source structurée — DG002
- Identifier ou initier une étude contrôlée (au moins Phase 2) évaluant le ziconotide dans la migraine chronique réfractaire
- Évaluer la faisabilité clinique et le rapport bénéfice/risque de la voie intrathécale dans cette indication, en particulier au vu des autres signaux du même dossier (ex. syndrome de la queue de cheval, rang 3) qui suggèrent une possible confusion entre association thérapeutique et association liée à la voie d'administration elle-même
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

