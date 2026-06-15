---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 4
---

# Darunavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Darunavir : De l'Infection à VIH à l'Infection par le Virus de l'Immunodéficience Simienne

## Résumé en Une Phrase

Darunavir est un inhibiteur de protéase du VIH non peptidique, utilisé en association avec un agent de potentialisation pharmacocinétique pour le traitement de l'infection à VIH-1.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Infection par le Virus de l'Immunodéficience Simienne (SIV)**,
avec **0 essai clinique** et **4 publications scientifiques** (études sur primates non humains) soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Infection à VIH-1 (contexte connu ; non enregistré à Taïwan) |
| Nouvelle Indication Prédite | Infection par le Virus de l'Immunodéficience Simienne (SIV) |
| Score de Prédiction TxGNN | 99.97% |
| Niveau de Preuve | L3 |
| Statut de Marché | ✗ Non commercialisé (Taïwan) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans cette fiche. Sur la base des informations connues, le Darunavir appartient à la classe des inhibiteurs de protéase (IP) du VIH — il se lie au site actif de la protéase virale et bloque le clivage des polyprotéines précurseurs du VIH, empêchant ainsi la formation de virions matures et infectieux.

La prédiction repose sur une homologie structurelle et fonctionnelle entre la protéase du SIV et celle du VIH-1/VIH-2 : les deux enzymes partagent environ 50 à 60 % de similarité de séquence et appartiennent à la même superfamille de protéases virales. Le site actif de la protéase du SIV est suffisamment similaire à celui du VIH-1 pour que le Darunavir puisse s'y lier et inhiber la maturation virale — mécanisme expérimentalement validé dans des modèles primates non humains (PNH) où il est intégré à des protocoles de cART.

Toutefois, il convient de souligner une limite fondamentale : le SIV est un pathogène exclusivement simien, sans application clinique directe chez l'humain. La pertinence de repositionnement dans un cadre thérapeutique humain est donc structurellement limitée — cette prédiction est davantage utile comme modèle préclinique de validation que comme cible d'indication clinique autonome.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour cette indication.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Étude animale (PNH) | PLoS Pathogens | Un régime ART hautement intensifié (incluant darunavir) induit une suppression virale durable et une restriction significative du réservoir viral chez des macaques rhésus infectés par SIVmac251 |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Étude animale (PNH) | PLoS ONE | Évaluation de cART combiné à l'inhibiteur HDAC SAHA chez des macaques rhésus (origine chinoise) infectés par le SIV ; le protocole incluant darunavir supprime efficacement la virémie et réduit les réservoirs viraux |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Étude animale (PNH) | AIDS Res Hum Retroviruses | Évaluation comparative de deux régimes cART co-formulés injectables chez des macaques rhésus infectés par SIVmac239 ; suppression virale atteignant des seuils cliniquement pertinents |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Étude animale (PNH) | AIDS (London) | L'auranofine combinée à un cART (incluant darunavir) limite le réservoir viral dans un modèle de SIDA simien et induit un contrôle de la charge virale après suspension du traitement |

> ⚠️ **Note méthodologique :** L'ensemble des publications identifiées correspond à des études précliniques sur primates non humains (Tier 3). Aucune donnée clinique humaine ni revue systématique n'est disponible pour cette indication spécifique.

---

## Informations de Marché à Taïwan

Aucune autorisation de mise sur le marché enregistrée pour le Darunavir à Taïwan.

---

## Considérations de Sécurité

Veuillez consulter la notice officielle (FDA/EMA) pour les informations complètes de sécurité, mises en garde et contre-indications.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le lien mécanistique entre le Darunavir et l'infection à SIV est scientifiquement plausible (homologie protéase SIV/VIH 50–60 %), soutenu par 4 études animales PNH de qualité modérée. Cependant, le SIV est un pathogène exclusivement simien — il n'existe pas d'indication clinique humaine directement dérivable de cette prédiction, ce qui limite structurellement son intérêt de repositionnement dans un cadre thérapeutique humain.

**Pour avancer, les éléments suivants sont nécessaires :**
- Clarifier l'objectif stratégique : si la cible est un modèle préclinique pour l'éradication du VIH, cette indication est pertinente ; si la cible est une nouvelle indication humaine, il convient de rediriger l'analyse vers d'autres prédictions
- Récupérer les données complètes de mécanisme d'action via DrugBank API (DG002)
- Obtenir les notices TFDA/FDA/EMA pour les informations de sécurité (DG001)
- Examiner les prédictions alternatives de rang 2–4 pour identifier une cible à plus forte valeur clinique humaine (en particulier, écarter la prédiction « feline AIDS » — artefact de mapping pipeline — et investiguer les liens métaboliques avec la dyslipidémie)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

