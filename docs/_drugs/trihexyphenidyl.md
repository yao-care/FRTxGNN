---
layout: default
title: Trihexyphenidyl
parent: Preuves modérées (L3-L4)
nav_order: 789
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Trihexyphenidyl : nouvelle indication prédite, Trouble déficitaire de l'attention avec hyperactivité (TDAH) (niveau de preuve L4). Indication d'origine : Maladie de Parkinson et syndromes parkinsonie…"
monitor_inn: "trihexyphenidyl"
predicted_indications: ["attention deficit-hyperactivity disorder", "faciodigitogenital syndrome", "attention deficit hyperactivity disorder, inattentive type", "Rasmussen subacute encephalitis", "PLA2G6-associated neurodegeneration", "congenital disorder of glycosylation with defective fucosylation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "retinal dystrophy with or without extraocular anomalies", "myelitis", "Charcot-Marie-Tooth disease, demyelinating, type 1G"]
---

# Trihexyphenidyl
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

# Trihexyphénidyle : De la maladie de Parkinson au trouble déficitaire de l'attention avec hyperactivité (TDAH)

## Résumé en Une Phrase

Le trihexyphénidyle est un anticholinergique central, initialement utilisé dans le traitement de la maladie de Parkinson et des syndromes parkinsoniens.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble déficitaire de l'attention avec hyperactivité (TDAH)**,
mais **aucun essai clinique** et **une seule publication indirecte** (une série clinique sur les tics associés à une dystonie) soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Parkinson et syndromes parkinsoniens (le texte d'indication des AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Trouble déficitaire de l'attention avec hyperactivité (TDAH) |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, le trihexyphénidyle est un antagoniste muscarinique central à préférence M1, qui module l'équilibre cholinergique-dopaminergique dans les noyaux gris centraux. C'est ce mécanisme qui explique son usage dans la maladie de Parkinson et les dystonies.

Le TDAH implique une dérégulation des signaux dopaminergiques et cholinergiques dans les circuits fronto-striataux ; un lien théorique existe donc. Toutefois, il reste purement hypothétique : la seule publication retrouvée porte sur des tics associés à une dystonie, un phénotype voisin mais distinct, et ne fournit aucune preuve directe d'efficacité dans le TDAH.

Il faut aussi souligner un argument défavorable : la charge anticholinergique (troubles cognitifs, inattention, agitation) pourrait aggraver les symptômes du TDAH. Le score élevé de TxGNN (0,999) reste une simple prédiction.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Cohorte | Movement Disorders | Série clinique de patients présentant des tics et une dystonie persistante, visant à déterminer la prévalence et les caractéristiques de ce syndrome. Aucune donnée sur le trihexyphénidyle ni sur le TDAH. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68401010 | PARKINANE LP 2 mg, gélule à libération prolongée (annulée) | Gélule à libération prolongée | Non renseignée |
| 69806741 | TRIHEXY 5 mg RICHARD, comprimé (annulée) | Comprimé | Non renseignée |
| 66377201 | TRIHEXY 2 mg RICHARD, comprimé (annulée) | Comprimé | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : glaucome à angle ouvert et à angle fermé, hypertrophie bénigne de la prostate, iléus paralytique, achalasie, hernie hiatale, myasthénie et maladies de la jonction neuromusculaire, maladies inflammatoires de l'intestin (dont rectocolite ulcéro-hémorragique), colite à *Clostridium difficile*, entérocolite nécrosante périnatale, maladie coronarienne, troubles de la conduction cardiaque, arrêt cardiaque, hypertension, hypotension, bronchopneumopathie chronique obstructive, ulcère gastrique, maladie rénale, maladie hépatique et maladie de la vésicule biliaire.
- **Interactions médicamenteuses** : 107 interactions recensées. Parmi les plus notables :
  - **Majeures** : chlorure de potassium et citrate de potassium.
  - **Modérées** : autres anticholinergiques (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium, propanthéline, méthscopolamine, mépenzolate), morphine, lopéramide, métoclopramide, dronabinol, nabilone, éluxadoline, pramlintide, prucalopride, hydroxyde de magnésium.
- Pour le TDAH, les effets anticholinergiques sur la cognition et l'attention constituent une préoccupation spécifique.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être obtenues.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune preuve clinique directe : zéro essai et une seule publication indirecte. La prédiction repose uniquement sur le modèle, et le profil cognitif des anticholinergiques va plutôt à l'encontre d'un bénéfice dans le TDAH.
- Toutes les AMM françaises sont annulées, et les données de sécurité officielles sont manquantes (blocage pour le criblage de sécurité).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice officielle de l'ANSM (mises en garde et contre-indications).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Réaliser une recherche ciblée de la littérature sur le trihexyphénidyle dans le TDAH, puis des études précliniques ou pilotes si des signaux apparaissent.
- Évaluer le risque cognitif anticholinergique, notamment chez l'enfant.

**Note sur les autres candidats :** parmi les neuf autres indications prédites, la **neurodégénérescence associée à PLA2G6** (score 99,58 %, niveau L4) est la plus cohérente biologiquement, en raison de ses phénotypes de dystonie-parkinsonisme. Les preuves se limitent toutefois à un cas clinique et le bénéfice serait uniquement symptomatique ; elle relève d'une question de recherche. Les autres candidats (syndrome faciodigitogénital, TDAH de type inattentif, encéphalite de Rasmussen, déficit de glycosylation, polymicrogyrie, dystrophie rétinienne, myélite, maladie de Charcot-Marie-Tooth 1G) ne disposent d'aucune preuve directe ou plausible et restent en Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

