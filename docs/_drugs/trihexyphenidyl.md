---
layout: default
title: Trihexyphenidyl
parent: Prédiction du modèle uniquement (L5)
nav_order: 789
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "trihexyphenidyl"
predicted_indications: ["attention deficit-hyperactivity disorder", "faciodigitogenital syndrome", "attention deficit hyperactivity disorder, inattentive type", "Rasmussen subacute encephalitis", "PLA2G6-associated neurodegeneration", "congenital disorder of glycosylation with defective fucosylation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "retinal dystrophy with or without extraocular anomalies", "myelitis", "Charcot-Marie-Tooth disease, demyelinating, type 1G"]
description: "Trihexyphenidyl : nouvelle indication prédite, Trouble déficitaire de l'attention avec hyperactivité (attention deficit-hyperactivity disorder) (niveau de preuve L5). Indication d'origine : Non rense…"
---

# Trihexyphenidyl
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Trihexyphenidyl: Trouble déficitaire de l'attention avec hyperactivité (attention deficit-hyperactivity disorder)
{: .text-alpha }

## Résumé en Une Phrase

Le trihexyphénidyle est un anticholinergique central, initialement utilisé dans le traitement de la maladie de Parkinson et des syndromes parkinsoniens.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble déficitaire de l'attention avec hyperactivité (TDAH)**,
mais **aucun essai clinique** et **une seule publication indirecte** (une série clinique sur les tics associés à une dystonie) soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Trouble déficitaire de l'attention avec hyperactivité (attention deficit-hyperactivity disorder) |
| Score de Prédiction TxGNN | 0.9992 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 7 sur 7) |
| Nombre d'AMM | 7 (valides : 7) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Trihexyphenidyl (traduction non officielle) : « Le chlorhydrate de trihexyphénidyle est le sel de pipéridine substitué, chlorhydrate de 3-(1-pipéridyl)- 1-phénylcyclohexyl-1-propanol, qui exerce un effet inhibiteur direct sur le système nerveux parasympathique. Il a également un effet relaxant sur la musculature lisse, exercé à la fois directement sur le tissu musculaire lui-même et indirectement par un effet inhibiteur sur le système nerveux parasympathique. » Texte original en anglais : "Trihexyphenidyl Hydrochloride is the substituted piperidine salt, 3-(1-piperidyl)- 1-phenylcyclohexyl-1-propanol hydrochloride, which exerts a direct inhibitory effect upon the parasympathetic nervous system. It also has a relaxing effect on smooth musculature; exerted both directly upon the muscle tissue itself and indirectly through an inhibitory effect upon the parasympathetic nervous system." ([DailyMed: trihexyphenidyl hydrochloride prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b60ef86c-b8b6-4530-baaf-d4671ce961af), version du 2026-07-23 ; consulté le 2026-11-19). D'après les connaissances générales, le trihexyphénidyle est un antagoniste muscarinique central à préférence M1, qui module l'équilibre cholinergique-dopaminergique dans les noyaux gris centraux. C'est ce mécanisme qui explique son usage dans la maladie de Parkinson et les dystonies.

Le TDAH implique une dérégulation des signaux dopaminergiques et cholinergiques dans les circuits fronto-striataux ; un lien théorique existe donc. Toutefois, il reste purement hypothétique : la seule publication retrouvée porte sur des tics associés à une dystonie, un phénotype voisin mais distinct, et ne fournit aucune preuve directe d'efficacité dans le TDAH.

Il faut aussi souligner un argument défavorable : la charge anticholinergique (troubles cognitifs, inattention, agitation) pourrait aggraver les symptômes du TDAH. Le score élevé de TxGNN (0,9992) reste une simple prédiction.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Cohorte | Movement Disorders | Série clinique de patients présentant des tics et une dystonie persistante, visant à déterminer la prévalence et les caractéristiques de ce syndrome. Aucune donnée sur le trihexyphénidyle ni sur le TDAH. |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 68401010 | PARKINANE LP 2 mg, gélule à libération prolongée | Gélule à libération prolongée | CNX THERAPEUTICS FRANCE | Active |
| 69806741 | TRIHEXY 5 mg RICHARD, comprimé | Comprimé | RICHARD | Active |
| 66377201 | TRIHEXY 2 mg RICHARD, comprimé | Comprimé | RICHARD | Active |
| 60379544 | ARTANE 2 mg, comprimé | Comprimé | NEURAXPHARM FRANCE | Active |
| 65387616 | ARTANE 5 mg, comprimé | Comprimé | NEURAXPHARM FRANCE | Active |
| 66238671 | PARKINANE LP 5 mg, gélule à libération prolongée | Gélule à libération prolongée | CNX THERAPEUTICS FRANCE | Active |
| 67900409 | ARTANE 0,4 POUR CENT, solution buvable en gouttes | Solution buvable gouttes | NEURAXPHARM FRANCE | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

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
- Le médicament dispose d'AMM valides en France (statut des AMM : voir l'Aperçu rapide), et les données de sécurité officielles sont manquantes (blocage pour le criblage de sécurité).

<!-- review:begin fr-lic-20261124-trihexyphenidyl-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les 3 AMM françaises sont valides (3 sur 3) » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans l'Aperçu rapide. Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés : le nombre et le statut à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché, générés à partir des données BDPM. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-trihexyphenidyl-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice officielle de l'ANSM (mises en garde et contre-indications).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Réaliser une recherche ciblée de la littérature sur le trihexyphénidyle dans le TDAH, puis des études précliniques ou pilotes si des signaux apparaissent.
- Évaluer le risque cognitif anticholinergique, notamment chez l'enfant.

**Note sur les autres candidats :** parmi les neuf autres indications prédites, la **neurodégénérescence associée à PLA2G6** (score 0,9958, niveau L4) est la plus cohérente biologiquement, en raison de ses phénotypes de dystonie-parkinsonisme. Les preuves se limitent toutefois à un cas clinique et le bénéfice serait uniquement symptomatique ; elle relève d'une question de recherche. Les autres candidats (syndrome faciodigitogénital, TDAH de type inattentif, encéphalite de Rasmussen, déficit de glycosylation, polymicrogyrie, dystrophie rétinienne, myélite, maladie de Charcot-Marie-Tooth 1G) ne disposent d'aucune preuve directe ou plausible et restent en Hold.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: trihexyphenidyl hydrochloride prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b60ef86c-b8b6-4530-baaf-d4671ce961af) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

