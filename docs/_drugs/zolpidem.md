---
layout: default
title: Zolpidem
parent: Prédiction du modèle uniquement (L5)
nav_order: 831
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Zolpidem : nouvelle indication prédite, Trouble du sommeil (initiation et maintien du sommeil) (niveau de preuve L5). Indication d'origine : Insomnie"
monitor_inn: "zolpidem"
predicted_indications: ["sleep disorder, initiating and maintaining sleep", "benign paroxysmal torticollis of infancy", "agoraphobia"]
---

# Zolpidem
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Zolpidem : De l'insomnie au trouble du sommeil (initiation et maintien du sommeil)

## Resume en Une Phrase

Zolpidem est un hypnotique non benzodiazepinique, initialement utilise pour le traitement de l'insomnie.
Le modele TxGNN predit qu'il pourrait etre efficace pour le **trouble du sommeil (initiation et maintien du sommeil)**, une indication qui correspond en pratique a son indication d'origine : il ne s'agit donc pas d'un repositionnement au sens strict.
Cette direction est soutenue par **18 publications** (dont 1 recommandation de pratique clinique, 2 meta-analyses en reseau et 1 essai randomise de phase 3 utilisant le zolpidem comme comparateur), mais **aucun essai clinique enregistre**.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Insomnie (source : graphe de connaissances TxGNN ; le texte d'indication des AMM n'est pas renseigne) |
| Nouvelle Indication Predite | Trouble du sommeil (initiation et maintien du sommeil) |
| Score de Prediction TxGNN | 99.87% |
| Niveau de Preuve | L1 (selon le classement des donnees compilees ; voir la remarque ci-dessous) |
| Statut de Marche en France | Uniquement annule |
| Nombre d'AMM | 11 (toutes annulees) |
| Decision Recommandee | Proceed with Guardrails |

**Remarque sur le niveau de preuve :** aucun essai de phase 3 portant sur le zolpidem seul n'est enregistre dans les donnees compilees. Le niveau L1 repose sur des recommandations de pratique clinique, des meta-analyses en reseau et un essai de phase 3 avec comparateur actif. Il refletait surtout la solidite de l'usage historique dans l'indication d'origine, et non une preuve nouvelle de repositionnement.

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles dans les donnees compilees. Sur la base des connaissances pharmacologiques generales, le zolpidem est un modulateur allosterique positif des recepteurs GABA-A, avec une selectivite pour la sous-unite alpha-1, ce qui favorise l'endormissement.

La nouvelle indication predite (difficultes d'initiation et de maintien du sommeil) est essentiellement la meme que l'indication d'origine, l'insomnie. La prediction du modele est donc coherente, mais elle ne constitue pas une veritable decouverte de repositionnement.

La litterature confirme que le zolpidem est un traitement et un comparateur reconnu : l'essai de phase 3 sur le lemborexant utilise le zolpidem a liberation prolongee comme controle actif chez des adultes ages, et plusieurs recommandations le citent parmi les « Z-drugs ».

Les deux autres predictions (torticolis paroxystique benin du nourrisson, score 99.26 % ; agoraphobie, score 99.25 %) ne reposent que sur le score du modele, sans essai ni publication. Elles ne presentent pas de justification mecanistique plausible : le torticolis paroxystique benin est un trouble pediatrique rare, pour lequel le zolpidem n'est pas adapte chez le nourrisson ; pour l'agoraphobie, l'activite anxiolytique du zolpidem est minime et les risques de dependance pesent contre son usage. Ces predictions sont classees L5 avec une decision « Hold ».

---

## Preuves d'Essais Cliniques

Aucun essai clinique associe enregistre actuellement.

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Meta-analyse en reseau | Lancet | Comparaison de l'efficacite des traitements pharmacologiques de l'insomnie chez l'adulte, a court et long terme |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Recommandation de pratique clinique | J Clin Sleep Med | Recommandations de l'AASM sur le traitement pharmacologique de l'insomnie chronique, medicament par medicament |
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | ECR (phase 3) | JAMA Netw Open | Lemborexant compare au placebo et au zolpidem a liberation prolongee chez des adultes ages insomniaques |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Meta-analyse en reseau | J Manag Care Spec Pharm | Efficacite et securite comparees du lemborexant et d'autres traitements de l'insomnie |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Revue | Pharmacol Rev | Medicaments de l'insomnie au-dela des benzodiazepines ; effets indesirables des Z-drugs (troubles cognitifs, tolerance, insomnie de rebond, chutes, dependance) |
| [39923608](https://pubmed.ncbi.nlm.nih.gov/39923608/) | 2025 | Consensus d'experts | Sleep Med | Recommandations europeennes pour le changement ou l'arret des hypnotiques dans l'insomnie chronique |
| [41187937](https://pubmed.ncbi.nlm.nih.gov/41187937/) | 2025 | Recommandation clinique | Arq Neuropsiquiatr | Abus et dependance aux Z-drugs ; usage recommande pour quatre semaines au maximum |
| [34210446](https://pubmed.ncbi.nlm.nih.gov/34210446/) | 2021 | Revue | Clin Geriatr Med | Traitement pharmacologique de l'insomnie du sujet age ; risques de chutes et de mortalite avec les Z-drugs |
| [28671376](https://pubmed.ncbi.nlm.nih.gov/28671376/) | 2017 | Revue | Am Fam Physician | Chez le sujet age, melatonine a liberation prolongee et doxepine en premiere intention ; Z-drugs en reserve |
| [22424586](https://pubmed.ncbi.nlm.nih.gov/22424586/) | 2012 | Revue | Expert Opin Pharmacother | Zolpidem, agoniste des recepteurs aux benzodiazepines, hypnotique le plus prescrit aux Etats-Unis |

---

## Informations de Marche en France

Les 11 AMM sont toutes annulees ; aucune n'est actuellement valide. Le texte de l'indication approuvee n'est pas renseigne.

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 61705683 | ZOLPIDEM ALMUS 10 mg (BIOGARAN) | Comprime pellicule secable | Annulee |
| 62969974 | ZOLPIDEM BIOGARAN 10 mg | Comprime pellicule secable | Annulee |
| 61843104 | ZOLPIDEM ZYDUS 10 mg | Comprime pellicule secable | Annulee |
| 63179285 | STILNOX 10 mg (SANOFI WINTHROP) | Comprime pellicule secable | Annulee |
| 69329603 | ZOLPIDEM CRISTERS 10 mg | Comprime pellicule secable | Annulee |

---

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : trouble anxieux, trouble nevrotique, trouble dysthymique, maladie hepatique, maladie de la vesicule biliaire, syndrome d'apnees obstructives du sommeil et autres syndromes d'apnee du sommeil, syndrome d'hypoventilation centrale congenitale, troubles amnesiques et amnesie retrograde, troubles lies a l'usage de substances, abus ou dependance, trouble deficitaire de l'attention avec hyperactivite.
- **Interactions medicamenteuses** : 274 interactions recensees. Interactions majeures notamment avec la morphine et la morphine liposomale (risque de depression du systeme nerveux central). Interactions moderees avec, entre autres, le bupropion, l'aprepitant, la dexamethasone, la cimetidine, la clarithromycine, le dronabinol, la nabilone, le metoclopramide, le miconazole, le clotrimazole, l'opium et la sibutramine.
- **Points de vigilance issus de la litterature** : alteration cognitive, tolerance, insomnie de rebond, chutes et accidents (surtout chez le sujet age), abus et dependance.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu etre recuperees ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Etapes

**Decision : Proceed with Guardrails** (pour l'indication « trouble du sommeil, initiation et maintien du sommeil »)

**Justification :**
- L'indication predite est equivalente a l'indication d'origine, et la litterature (recommandations, meta-analyses, essai de phase 3 avec comparateur) soutient l'usage du zolpidem dans l'insomnie. Toutefois, les 11 AMM francaises sont toutes annulees et le profil de risque (dependance, troubles du comportement complexes du sommeil, altération du lendemain, sujets ages) exige des garde-fous.
- Les predictions pour le torticolis paroxystique benin du nourrisson et l'agoraphobie restent en **Hold** (niveau L5, sans preuve).

**Pour avancer, les elements suivants sont necessaires :**
- Recuperer la notice officielle de l'ANSM (mises en garde, contre-indications, indication approuvee) : donnee bloquante pour le screening de securite.
- Obtenir les donnees sur le mecanisme d'action depuis DrugBank.
- Verifier la disponibilite reelle d'une formulation commercialisee en France, puisque toutes les AMM sont annulees.
- Definir un plan de gestion des co-medications depressives du systeme nerveux central (notamment les opioides) et de surveillance de l'alteration du lendemain, des comportements complexes du sommeil et de l'usage chez le sujet age.
- Ne pas poursuivre les predictions L5 (torticolis du nourrisson, agoraphobie) sans preuve mecanistique et clinique nouvelle.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

