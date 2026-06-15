---
layout: default
title: Atropine
parent: 僅模型預測 (L5)
nav_order: 46
evidence_level: L5
indication_count: 2
---

# Atropine
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

# Atropine : De l'Anticholinergique Classique au Trouble Migraineux

## Résumé en Une Phrase

L'atropine est un antagoniste muscarinique non sélectif classiquement utilisé pour le traitement de la bradycardie, de l'intoxication aux organophosphorés et en prémédication anesthésique. Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **trouble migraineux** (migraine disorder), avec **0 essai clinique** et **13 publications** orientant actuellement cette direction de recherche. Les preuves disponibles sont essentiellement mécanistiques et précliniques, imposant une phase d'investigation fondamentale avant tout développement clinique.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Anticholinergique (bradycardie, intoxication aux organophosphorés, prémédication anesthésique) |
| Nouvelle Indication Prédite | Trouble migraineux (Migraine disorder) |
| Score de Prédiction TxGNN | 99.56% |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

L'atropine est un antagoniste muscarinique non sélectif bloquant les récepteurs M1 à M5 dans le système nerveux périphérique et central. Bien que les données formelles sur le mécanisme d'action ne soient pas disponibles dans la base de données réglementaire consultée, la pharmacologie de l'atropine est bien caractérisée dans la littérature scientifique mondiale. Sur la base de ces données, l'atropine appartient à la classe des anticholinergiques et son action antimuscarinique constitue le fondement du lien mécanistique exploré ici.

Le rationnel de repositionnement repose sur le **réflexe trigémino-autonomique**, pilier central de la physiopathologie de la migraine : l'activation du nerf trijumeau déclenche une décharge parasympathique via le ganglion sphénopalatin (SPG), entraînant une inflammation neurogène de la dure-mère et une extravasation de protéines plasmatiques (PMID 9344563). L'atropine, en bloquant les récepteurs muscariniques, pourrait théoriquement interrompre cette voie, inhibant la sortie parasympathique du SPG et l'activation des mastocytes méningés impliquée dans la cascade inflammatoire migraineuse (PMID 36485173).

Cependant, une complexité théorique majeure tempère cette hypothèse : le système cholinergique dans la migraine est **bidirectionnel**. Si l'activation parasympathique périphérique peut amplifier l'inflammation méningée, les récepteurs muscariniques centraux participent également à la nociception analgésique endogène — le blocage cholinergique central antagonise l'antinociception induite par le sumatriptan (PMID 8930196), suggérant que l'atropine pourrait simultanément réduire l'inflammation et contrecarrer des mécanismes analgésiques intrinsèques. L'effet net in vivo demeure donc imprévisible en l'absence de données cliniques dédiées.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Mécanistique / In vitro | European Journal of Neuroscience | Les mastocytes méningés modulent la neuroinflammation cholinergique dans un modèle de migraine à la nitroglycérine ; les antagonistes muscariniques modifient la libération de médiateurs inflammatoires et l'activation des fibres C |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Étude animale (rat) | Experimental Neurology | La stimulation parasympathique du SPG induit une extravasation protéique dans la dure-mère, soutenant directement le rôle de la voie cholinergique dans la neuroinflammation méningée migraineuse |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Étude animale | J Pharmacology & Experimental Therapeutics | Le système cholinergique central contribue à l'antinociception induite par le sumatriptan ; l'atropine antagonise cet effet, démontrant une interaction complexe entre blocage muscarinique et analgésie |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Observation clinique / Revue | Cephalalgia | Chez des patients atteints d'hémicranie paroxystique chronique, l'atropine systémique réduit significativement la sudation, le larmoiement et la sécrétion nasale lors des crises — première évidence clinique d'un rôle cholinergique dans les céphalées autonomiques |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | Étude pharmacologique (ex vivo) | British Journal of Pharmacology | L'atropine (3 µM) utilisée comme outil de blocage muscarinique dans l'étude de la relaxation nicotinique de l'artère basilaire ; pertinence pour la vasomotricité dans la migraine |
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Revue | Journal of Applied Toxicology | L'anisodamine, dérivé naturel de l'atropine, présente un profil anticholinergique similaire avec moindre toxicité SNC ; revue comparative utile pour évaluer la classe des dérivés tropaniques |
| [15882801](https://pubmed.ncbi.nlm.nih.gov/15882801/) | 2005 | Étude pharmacologique | Neuroscience Letters | Le CGRP et les récepteurs nicotiniques médient les modifications du flux sanguin facial lors des crises migraineuses par voie trigéminale centrale ; contexte du rôle des voies autonomiques |
| [1786517](https://pubmed.ncbi.nlm.nih.gov/1786517/) | 1991 | Étude pharmacologique | British Journal of Pharmacology | L'ergotamine et la DHE agissent sur les récepteurs 5-HT1C dans le plexus choroïde ; contexte pharmacologique des traitements antimigraineux et de leurs interactions potentielles |
| [18091300](https://pubmed.ncbi.nlm.nih.gov/18091300/) | 2007 | Série de cas cliniques | Optometry and Vision Science | Effets oculaires indésirables du topiramate (prophylactique migraineux) : myopie aiguë et hypertension intraoculaire — pertinent pour la surveillance ophtalmologique si repositionnement anticholinergique |
| [21252](https://pubmed.ncbi.nlm.nih.gov/21252/) | 1977 | Étude pharmacologique | Journal of Pharmacy and Pharmacology | Mécanisme d'action possible de la bêta-phényléthylamine dans la migraine ; contexte des médiateurs impliqués dans la physiopathologie migraineuse |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Les preuves disponibles sont exclusivement mécanistiques et précliniques (niveau L4), sans aucun essai clinique enregistré. La dualité du système cholinergique dans la migraine — à la fois pro-inflammatoire en périphérie et analgésique en central — crée une incertitude théorique fondamentale qui empêche toute recommandation de développement sans données précliniques dédiées résolvant cette ambivalence.

> **Note sur la 2ème indication prédite — Migraine avec aura du tronc cérébral (score 99.42%, L5) :** Cette indication est classée **Hold** avec une réserve plus forte. Les données disponibles (PMID 31945385) suggèrent que l'activation cholinergique *inhibe* la dépression corticale envahissante (CSD) qui initie l'aura — l'effet antagoniste de l'atropine irait donc à l'encontre du mécanisme thérapeutique visé. Cette piste n'est pas prioritaire en l'état.

**Pour avancer, les éléments suivants sont nécessaires :**

- **Données MOA formelles** : consultation de la base DrugBank complète pour le profil pharmacologique détaillé de l'atropine (DB00572)
- **Informations de sécurité** : récupération des contre-indications, mises en garde et interactions médicamenteuses depuis la notice ANSM ou équivalente
- **Étude préclinique dédiée** : évaluation de l'effet net de l'atropine (centrale vs. périphérique) dans un modèle de migraine validé (ex. modèle nitroglycérine chez le rat) pour trancher l'ambivalence bidirectionnelle
- **Définition de la fenêtre thérapeutique** : identification d'une voie d'administration adaptée (intranasal, IV, SC) permettant une action ciblée sur le SPG sans passage central significatif
- **Revue systématique clinique** : analyse exhaustive des cas documentant un effet de l'atropine sur les symptômes autonomiques migraineux (en prolongement de PMID 2943405)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

