---
layout: default
title: Clobazam
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
---

# Clobazam
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

# Clobazam : De l'Épilepsie au Syndrome d'Épilepsie Lié aux Infections Fébriles (FIRES)

## Résumé en Une Phrase

Le clobazam est une 1,5-benzodiazépine à large spectre antiépileptique, approuvée par la FDA pour le traitement adjuvant du syndrome de Lennox-Gastaut, et utilisée dans plusieurs pays pour les épilepsies réfractaires.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Syndrome d'Épilepsie Lié aux Infections Fébriles (FIRES)**, avec **0 essai clinique enregistré** et **2 publications** orientant actuellement cette direction.
Les preuves disponibles portent toutefois sur d'autres agents benzodiazépiniques plutôt que sur le clobazam lui-même.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Épilepsie réfractaire (non commercialisé en France selon les données disponibles) |
| Nouvelle Indication Prédite | Syndrome d'Épilepsie Lié aux Infections Fébriles (FIRES) |
| Score de Prédiction TxGNN | 99.82% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des connaissances établies, le clobazam est une 1,5-benzodiazépine structuralement distincte des benzodiazépines classiques 1,4 (comme le diazépam ou le clonazépam). Il agit comme modulateur allostérique positif des récepteurs GABA-A, amplifiant l'afflux de chlorure et renforçant l'inhibition neuronale corticale — mécanisme qui constitue la base pharmacologique de ses propriétés antiépileptiques.

Le FIRES est un état de mal épileptique fébrile réfractaire survenant chez des enfants précédemment sains, caractérisé par des crises pharmacorésistantes exigeant souvent un coma pharmacologique prolongé. La justification mécanistique est que le renforcement GABAergique pourrait élever le seuil de décharge épileptique lors de la phase aiguë et faciliter le sevrage des anesthésiques généraux. Les benzodiazépines de longue durée d'action — dont font partie les analogues du clobazam — sont précisément explorées dans ce rôle de relais per os après stabilisation par midazolam IV.

Cependant, les preuves publiées identifiées ne portent pas directement sur le clobazam dans le FIRES : elles documentent le lorazépam entéral (PMID 35770765) et le pérampanel (PMID 39958143) dans cette indication. La prédiction du modèle TxGNN reflète vraisemblablement la similarité de classe benzodiazépinique plutôt qu'une évidence clinique propre au clobazam.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Série de cas | Epileptic Disorders | Le lorazépam entéral constitue une stratégie de sevrage prometteuse chez des patients FIRES dépendants au midazolam ; l'approche soutient un relais benzodiazépinique oral après coma pharmacologique |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Rapport de cas | Cureus | Le pérampanel a permis de réduire la dépendance aux barbituriques chez un garçon de 13 ans atteint de FIRES, illustrant l'intérêt des agents adjuvants dans le sevrage des anesthésiques |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les données de contre-indications, mises en garde et interactions médicamenteuses n'ont pas pu être récupérées pour cette évaluation.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Bien que la classe pharmacologique du clobazam (benzodiazépine GABAergique) soit mécanistiquement cohérente avec la prise en charge du FIRES, aucune publication ni essai clinique ne documente directement son utilisation dans cette indication. Les 2 références identifiées concernent d'autres médicaments (lorazépam, pérampanel), sans données comparatives ni spécifiques au clobazam. Le niveau de preuve L5 ne justifie pas d'avancer vers une évaluation clinique formelle à ce stade.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération des données de mécanisme d'action (MOA) via DrugBank (DG002)
- Récupération de la notice officielle pour les mises en garde et contre-indications (DG001)
- Revue bibliographique ciblée sur le clobazam spécifiquement dans le FIRES ou les états de mal épileptiques réfractaires fébriles
- Vérification des registres internationaux (EU-CTR, ISRCTN) pour tout essai émergent sur le clobazam dans le NORSE/FIRES
- Analyse comparative avec le lorazépam et le midazolam entéral dans le contexte de sevrage post-FIRES
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

