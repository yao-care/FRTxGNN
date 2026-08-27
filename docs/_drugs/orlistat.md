---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 1
---

# Orlistat
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

# Orlistat : De l'Obésité à l'Hypervitaminose

## Résumé en Une Phrase

Orlistat est un inhibiteur des lipases pancréatique et gastrique, utilisé à l'origine dans la prise en charge du poids (obésité) en réduisant l'absorption intestinale des graisses alimentaires. Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Hypervitaminose** (excès de vitamines liposolubles), mais cette direction n'est actuellement soutenue par **aucun essai clinique** ni **aucune publication** — la prédiction repose uniquement sur le modèle algorithmique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Obésité / prise en charge du poids (donnée non présente dans le Evidence Pack fourni ; il s'agit d'une connaissance pharmacologique générale, l'indication n'ayant pu être extraite de licences françaises) |
| Nouvelle Indication Prédite | Hypervitaminose |
| Score de Prédiction TxGNN | 99.42% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action original (MOA) ne sont pas disponibles dans ce Evidence Pack (écart de données identifié, sévérité High). Cependant, la fiche de justification mécanistique associée à cette prédiction précise qu'Orlistat est un **inhibiteur de la lipase pancréatique**, qui bloque la digestion et l'absorption intestinale des graisses alimentaires. Cet effet, connu et documenté, réduit secondairement l'absorption des vitamines liposolubles (A, D, E, K) qui dépendent de la digestion lipidique pour être assimilées.

Sur cette base, l'hypothèse de repositionnement propose qu'Orlistat pourrait être utilisé pour limiter l'absorption intestinale de vitamines liposolubles en cas d'hypervitaminose A/D/E/K, en exploitant le même mécanisme que celui responsable de la réduction de l'absorption des graisses.

**Point de vigilance important** : cette prédiction présente une contradiction directionnelle. Dans l'indication d'origine (prise en charge du poids), la réduction de l'absorption des vitamines liposolubles est classiquement considérée comme un **effet indésirable à surveiller** (risque de carence vitaminique), et non comme un bénéfice thérapeutique recherché. L'utilisation du même mécanisme à visée thérapeutique dans l'hypervitaminose reste donc une inférence mécanistique non validée, à interpréter avec prudence.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement

---

## Informations de Marché en France

Orlistat n'est actuellement **pas commercialisé en France** (0 AMM active recensée dans les données disponibles).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Cette prédiction repose uniquement sur le score du modèle TxGNN (niveau de preuve L5), sans aucun essai clinique ni publication à l'appui. De plus, le mécanisme proposé entre en contradiction avec le profil de sécurité connu du médicament dans son indication d'origine, où la réduction de l'absorption des vitamines liposolubles est un effet indésirable et non un bénéfice recherché.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données complètes sur le mécanisme d'action (MOA) via DrugBank/TFDA
- Mises en garde et contre-indications du TFDA (écart de données bloquant, DG001)
- Études précliniques ou de mécanisme confirmant un bénéfice thérapeutique spécifique (et non un simple effet secondaire) dans l'hypervitaminose
- Preuves cliniques réelles (essais ou séries de cas) évaluant Orlistat dans l'hypervitaminose A/D/E/K
- Évaluation de la faisabilité d'une entrée sur le marché français, actuellement absent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

