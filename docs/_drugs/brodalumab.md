---
layout: default
title: Brodalumab
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Brodalumab
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

# Brodalumab : Du Psoriasis en Plaques à la Strongyloïdose

## Résumé en Une Phrase

Brodalumab est un anticorps monoclonal antagoniste du récepteur IL-17RA, indiqué dans plusieurs pays pour le traitement du psoriasis en plaques modéré à sévère, mais non commercialisé en France à ce jour. Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Strongyloïdose** (*strongyloidiasis*), bien que la rationalité biologique soulève des interrogations fondamentales sur la direction de l'effet attendu. Actuellement, **aucun essai clinique ni aucune publication** ne soutient directement cette indication prédite.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Non répertoriée (aucune AMM en France) |
| Nouvelle Indication Prédite | Strongyloïdose (*Strongyloidiasis*) |
| Score de Prédiction TxGNN | 99,84 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action (MOA) issues de DrugBank ne sont pas disponibles dans cet Evidence Pack. Sur la base des informations connues, Brodalumab est un anticorps monoclonal humain ciblant le récepteur IL-17RA, inhibant ainsi la signalisation de plusieurs membres de la famille IL-17 (IL-17A, IL-17C, IL-17F et IL-17E). Cette inhibition réduit la cascade inflammatoire médiée par les lymphocytes Th17, ce qui a démontré son efficacité dans le psoriasis en plaques. Il est commercialisé sous les noms **Siliq®** (États-Unis) et **Kyntheum®** (Europe, approbation EMA 2017) pour cette indication.

Concernant la strongyloïdose, la rationalité biologique de cette prédiction suscite des réserves importantes. L'IL-17 joue un rôle de molécule effectrice clé dans la défense immunitaire de l'hôte contre les parasites helminthes tels que *Strongyloides stercoralis*. En théorie, l'inhibition de la signalisation IL-17RA par Brodalumab devrait **affaiblir** l'immunité anti-parasitaire et **aggraver** l'infection, plutôt que l'améliorer. Cette contradiction biologique directe remet en question la pertinence clinique de cette piste de repositionnement.

Le score TxGNN élevé (99,84 %) reflète très probablement la proximité topologique entre le nœud « voie IL-17 » et le nœud « strongyloïdose » dans le graphe de connaissances, sans nécessairement capturer la **direction** de l'effet biologique. Cette distinction entre association topologique et causalité directionnelle est une limitation connue des modèles de graphe pour les maladies parasitaires helminthiques.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Brodalumab ne dispose d'aucune autorisation de mise sur le marché en France. Le médicament a obtenu une approbation EMA (Kyntheum®) pour le psoriasis en plaques, mais il n'est pas référencé par l'ANSM ni commercialisé sur le territoire français à la date de cet Evidence Pack (2026-06-06).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

> **Note de risque spécifique au repositionnement :** Dans le contexte d'une potentielle utilisation en zone endémique de *Strongyloides stercoralis*, l'inhibition de la signalisation IL-17 est un facteur aggravant connu pour les infections parasitaires. Les patients immunosupprimés traités par anti-IL-17 présentent un risque accru de strongyloïdose hyperinfectieuse, avec potentiel d'évolution systémique fatale.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
L'inhibition de IL-17RA par Brodalumab est biologiquement contre-productive pour la strongyloïdose — l'IL-17 étant un médiateur central de l'immunité anti-helminthique, son blocage risque d'aggraver l'infection parasitaire plutôt que de la traiter. En l'absence de toute preuve clinique ou préclinique directe (niveau L5) et face à une rationalité mécanistique inversée, la poursuite de cette piste n'est pas recommandée dans l'état actuel des connaissances.

**Pour avancer sur d'autres pistes, les éléments suivants sont nécessaires :**

- Données complètes sur le mécanisme d'action (MOA) via DrugBank API (Data Gap DG002)
- Informations réglementaires ANSM complètes, notamment mises en garde et contre-indications de la notice (Data Gap DG001)
- **Évaluation prioritaire de l'indication de rang 2 (Eye disease / L4)**, qui présente une rationalité biologique cohérente avec le profil anti-IL-17 de Brodalumab (uvéite, kératite, inflammation oculaire de type Th17) et dispose d'au moins une étude observationnelle et une revue narrative comme points de départ
- Revue de la littérature sur les autres indications du spectre inflammatoire oculaire (rangs 5–10) pour identifier si un sous-groupe (ex. uvéite antérieure associée à la spondyloarthrite) pourrait bénéficier d'un rationnel mécanistique solide
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

