---
layout: default
title: Thiocolchicoside
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 2
---

# Thiocolchicoside
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Thiocolchicoside : Des Spasmes Musculaires a l'Insomnie

## Resume en Une Phrase

Thiocolchicoside est un relaxant musculaire central utilise pour les spasmes et douleurs musculaires, agissant comme antagoniste des recepteurs GABA-A et glycine.
Le modele TxGNN predit qu'il pourrait etre efficace pour l'**Insomnie**,
mais cette direction n'est soutenue actuellement que par **1 essai clinique de pertinence faible (grade C)** et **aucune publication**.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Spasmes musculaires (relaxant musculaire central) — donnee officielle TFDA non disponible |
| Nouvelle Indication Predite | Insomnie |
| Score de Prediction TxGNN | 99.89% |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Les donnees detaillees sur le mecanisme d'action officiel (MOA) ne sont pas disponibles dans DrugBank pour cette evaluation. Sur la base des informations disponibles dans l'analyse de repositionnement, le thiocolchicoside agit pharmacologiquement comme **antagoniste des recepteurs GABA-A et glycine**, ce qui en fait un relaxant musculaire central utilise pour les spasmes et douleurs musculaires.

Cependant, cette direction pharmacologique pose un probleme mecanistique majeur pour l'indication predite : le traitement de l'insomnie repose typiquement sur des **agonistes** GABA-A (benzodiazepines, Z-drugs) qui augmentent l'inhibition centrale, alors que le thiocolchicoside, en **bloquant** ces memes recepteurs, va dans le sens oppose — une augmentation de l'excitabilite centrale, avec un risque connu de convulsions (l'EMA a d'ailleurs restreint sa dose et sa duree d'utilisation pour cette raison).

Le meme raisonnement s'applique a la deuxieme indication predite par le modele, le delirium de sevrage alcoolique (score TxGNN 99.21%) : cette condition necessite egalement une potentialisation GABA-A (benzodiazepines), une direction contraire au mecanisme antagoniste du thiocolchicoside. La prediction TxGNN, bien que numeriquement elevee, est donc mecanistiquement discordante pour les deux indications identifiees et doit etre interpretee avec prudence.

---

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT06791434](https://clinicaltrials.gov/study/NCT06791434) | Phase 4 | Termine | 156 | Etude sur l'aiguilletage a sec (dry needling) en complement du traitement conventionnel de la lombalgie myofasciale ; le thiocolchicoside n'y figure que comme composant possible du traitement de fond, sans evaluation d'un critere lie a l'insomnie (pertinence : grade C, faible) |

---

## Preuves de la Litterature

Aucune litterature associee disponible actuellement.

---

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
Le seul essai clinique identifie n'evalue pas l'insomnie comme critere et presente une pertinence faible (grade C), et aucune litterature ne soutient cette indication. De plus, le mecanisme antagoniste GABA-A/glycine du thiocolchicoside est pharmacologiquement contradictoire avec l'effet recherche dans le traitement de l'insomnie, ce qui constitue un signal d'alerte plutot qu'un support mecanistique.

**Pour avancer, les elements suivants sont necessaires :**
- Notice/mises en garde TFDA (donnee bloquante actuellement manquante, empeche toute evaluation de securite initiale S1)
- Donnees detaillees sur le mecanisme d'action (MOA) via l'API DrugBank
- Essais cliniques ou etudes mecanistiques evaluant specifiquement le thiocolchicoside dans l'insomnie
- Reevaluation de la coherence mecanistique de la prediction TxGNN avant toute progression
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

