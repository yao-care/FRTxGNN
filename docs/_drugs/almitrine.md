---
layout: default
title: Almitrine
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 1
---

# Almitrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Now I have the research needed. Here is the full report:

---

# Almitrine : Stimulant Respiratoire — Aucune Nouvelle Indication Prédite

## Résumé en Une Phrase

Almitrine (bismésilate) est un agoniste périphérique des chémorécepteurs carotidiens, historiquement utilisé pour améliorer l'oxygénation artérielle dans l'insuffisance respiratoire chronique liée à la BPCO. Le modèle TxGNN **n'a identifié aucune nouvelle indication candidate** pour ce médicament. De plus, Almitrine n'est **pas commercialisé en France** (0 AMM), ce qui limite considérablement les possibilités de repositionnement dans ce territoire.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Insuffisance respiratoire chronique liée à la BPCO (hypoxémie chronique) |
| Nouvelle Indication Prédite | **Aucune** — le modèle TxGNN n'a retourné aucune prédiction |
| Score de Prédiction TxGNN | N/A |
| Niveau de Preuve | **L5** — Aucune étude associée à une nouvelle indication |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Aucune Prédiction n'a Été Générée ?

Almitrine est un **agoniste des chémorécepteurs périphériques** (corps carotidiens). Son mécanisme d'action est hautement spécialisé : il augmente la sensibilité des chémorécepteurs à l'hypoxie et à l'hypercapnie, stimulant ainsi la ventilation alvéolaire et améliorant le rapport ventilation/perfusion (V/Q) par potentialisation de la vasoconstriction pulmonaire hypoxique. Ce mécanisme très ciblé sur la physiologie respiratoire réduit naturellement le champ des indications transposables identifiées par les algorithmes de prédiction sur graphe de connaissances.

Par ailleurs, Almitrine présente un profil de sécurité contraignant, avec un risque bien documenté de **neuropathie périphérique** dose-dépendante, qui a conduit au retrait progressif du marché dans plusieurs pays (dont la France, où la combinaison Duxil a été retirée vers 2011-2013 par décision de l'ANSM en raison d'un rapport bénéfice/risque défavorable). Ce contexte réglementaire défavorable contribue également à l'absence de signaux de repositionnement.

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas renseignées dans l'Evidence Pack (Data Gap identifié). Néanmoins, sur la base des connaissances publiées, Almitrine appartient à la classe des stimulants respiratoires (code ATC : R07AB07, dérivé de pipérazine-triazine) développé par Servier sous le nom de marque **Vectarion**.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé à une nouvelle indication n'est enregistré actuellement.

> **Note :** Un regain d'intérêt transitoire pour Almitrine a été observé pendant la pandémie de COVID-19 (2020-2021) pour son potentiel à améliorer le mismatch V/Q dans le SDRA lié au COVID-19, mais cela n'a pas abouti à de nouvelles approbations.

---

## Preuves de la Littérature

Aucune littérature associée à une nouvelle indication n'est disponible actuellement.

---

## Informations de Marché en France

Almitrine n'est **pas commercialisé en France**. Aucune Autorisation de Mise sur le Marché (AMM) active n'a été identifiée.

| Élément | Détail |
|------|------|
| Statut | Non commercialisé (0 AMM) |
| Historique | Le produit combiné Duxil (almitrine + raubasine) a été retiré du marché français vers 2011-2013 suite à une réévaluation défavorable du rapport bénéfice/risque par l'ANSM |
| Motif de retrait | Neuropathie périphérique dose-dépendante, profil de sécurité défavorable |

---

## Considérations de Sécurité

> Les données de sécurité ne sont pas renseignées dans l'Evidence Pack actuel (Data Gap — Sévérité : Blocking).

Néanmoins, sur la base de la littérature publiée, les éléments de sécurité connus sont les suivants :

- **Mises en Garde Principales** :
  - **Neuropathie périphérique** : effet indésirable majeur, dose-dépendant, survenant surtout à des posologies >100 mg/jour ou lors d'un usage prolongé. Généralement réversible à l'arrêt, mais peut être sévère.
  - **Perte de poids** fréquente sous traitement.
  - **Hypertension artérielle pulmonaire** possible lors d'un usage prolongé.
  - Surveillance neurologique périodique recommandée (études de conduction nerveuse).
  - Le traitement doit être intermittent (cycles de 2 mois avec 1 mois de pause) pour réduire le risque de neuropathie.

- **Contre-indications** :
  - Insuffisance hépatique sévère
  - Neuropathie périphérique préexistante
  - Hypersensibilité connue à l'almitrine ou à ses excipients
  - Grossesse et allaitement

- **Interactions Médicamenteuses** : Aucune interaction identifiée dans l'Evidence Pack (requête DDI : not_found).

---

## Lacunes de Données Identifiées

| ID | Catégorie | Élément Manquant | Sévérité | Impact |
|----|-----------|------------------|----------|--------|
| DG001 | Niveau Médicament | Mises en garde / Contre-indications officielles (notice) | **Blocking** | Impossible d'entrer en évaluation de sécurité S1 |
| DG002 | Niveau Médicament | Mécanisme d'action (MOA) | Élevée | Affecte l'analyse de relation mécanistique |

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le modèle TxGNN n'a identifié aucune nouvelle indication candidate pour Almitrine. De plus, le médicament n'est pas commercialisé en France (0 AMM), a été retiré du marché français en raison d'un rapport bénéfice/risque défavorable (neuropathie périphérique), et présente des lacunes de données bloquantes (DG001). L'ensemble de ces facteurs ne justifie pas la poursuite de l'évaluation de repositionnement à ce stade.

**Pour reconsidérer cette décision, les éléments suivants seraient nécessaires :**
- Résolution de la lacune DG001 : obtention et analyse de la notice officielle (mises en garde, contre-indications)
- Résolution de la lacune DG002 : données MOA complètes via DrugBank API
- Identification d'un signal de repositionnement par un modèle alternatif ou par la littérature émergente
- Réévaluation du profil de sécurité dans le contexte d'une indication spécifique où le rapport bénéfice/risque pourrait être favorable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

