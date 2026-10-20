---
layout: default
title: Fluvoxamine
parent: Preuves élevées (L1-L2)
nav_order: 344
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Fluvoxamine : nouvelle indication prédite, Trouble anxieux (classe en 5e position de la liste des predictions (niveau de preuve L1). Indication d'origine : Phobie sociale, trouble phobique, trouble o…"
monitor_inn: "FLUVOXAMINE"
predicted_indications: ["schizotypal personality disorder", "schizoid personality disorder", "histrionic personality disorder (disease)", "paranoid personality disorder", "anxiety disorder", "agoraphobia", "benign paroxysmal torticollis of infancy", "dependent personality disorder", "narcissistic personality disorder", "endogenous depression"]
---

# Fluvoxamine
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

# Fluvoxamine : De la phobie sociale et du trouble obsessionnel-compulsif au trouble anxieux

## Resume en Une Phrase

La fluvoxamine est un inhibiteur selectif de la recapture de la serotonine (ISRS), initialement utilise pour traiter la phobie sociale, les troubles phobiques et le trouble obsessionnel-compulsif (TOC).
Le modele TxGNN predit qu'elle pourrait etre efficace pour le **trouble anxieux** (indication la mieux documentee parmi les 10 candidates), avec **13 essais cliniques** et **20 publications** soutenant actuellement cette direction.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Phobie sociale, trouble phobique, trouble obsessionnel-compulsif (source : graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigne) |
| Nouvelle Indication Predite | Trouble anxieux (classe en 5e position de la liste des predictions ; voir la remarque ci-dessous) |
| Score de Prediction TxGNN | 99.97 % |
| Niveau de Preuve | L1 |
| Statut de Marche en France | Annule uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulee) |
| Decision Recommandee | Proceed with Guardrails |

**Remarque sur le choix de l'indication :** les quatre premieres predictions (troubles de la personnalite schizotypique, schizoide, histrionique et paranoiaque) ont un score un peu plus eleve (99.997 %) mais reposent sur des preuves tres faibles (niveaux L4-L5, aucun essai clinique, decision « Hold »). Ce rapport retient donc le trouble anxieux, premier candidat disposant de preuves substantielles. Le trouble anxieux recoupe largement les indications deja connues (phobie sociale, TOC) : il s'agit surtout d'une extension du cadre existant plutot que d'un repositionnement au sens strict. L'agoraphobie (L1) et la depression endogene (L2) constituent d'autres pistes credibles.

## Pourquoi Cette Prediction est-elle Raisonnable ?

Les donnees detaillees sur le mecanisme d'action ne sont pas disponibles dans les informations compilees pour ce rapport. D'apres les connaissances etablies, la fluvoxamine est un ISRS qui est aussi un agoniste puissant du recepteur sigma-1. La modulation serotoninergique des circuits de la peur et de l'anxiete explique son efficacite dans la phobie sociale et le TOC.

Le trouble anxieux englobe notamment le trouble panique, l'anxiete generalisee et l'anxiete sociale, ainsi que, selon les classifications, le TOC. L'indication originale (phobie sociale, TOC) appartient donc deja a ce spectre. Le mecanisme serotoninergique est ainsi applicable a l'ensemble de la categorie, ce que soutiennent les revues de la classe des ISRS et les meta-analyses en reseau.

Il faut garder a l'esprit que le score tres eleve du modele reflete en grande partie la proximite de ce trouble avec les indications existantes dans le graphe de connaissances. La plausibilite est bonne, mais la nouveaute therapeutique est limitee.

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT01933919](https://clinicaltrials.gov/study/NCT01933919) | Phase 3 | Termine | 38 | Fluvoxamine (SME3110) vs placebo dans le TOC pediatrique/adolescent ; efficacite et securite a long terme |
| [NCT00000389](https://clinicaltrials.gov/study/NCT00000389) | Phase 3 | Termine | Non renseigne | Etude RUPP : fluvoxamine dans les troubles anxieux de l'enfant |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Termine | 124 | TCC associee aux inhibiteurs de la recapture de la serotonine dans le TOC pediatrique (reponse partielle) ; non specifique a la fluvoxamine |
| [NCT00352768](https://clinicaltrials.gov/study/NCT00352768) | Phase 4 | Arrete | 20 | Etude post-commercialisation de SME3110 dans le TOC de l'enfant et de l'adolescent ; limitee par la petite taille et l'arret precoce |
| [NCT02022709](https://clinicaltrials.gov/study/NCT02022709) | Phase 4 | Termine | 78 | Exposition avec prevention de la reponse (ERP) et ISRS dans le TOC ; non specifique a la fluvoxamine |
| [NCT00012584](https://clinicaltrials.gov/study/NCT00012584) | Non applicable | Termine | 120 | Stimulant seul ou avec fluvoxamine chez des jeunes avec TDAH et troubles anxieux comorbides |
| [NCT02194075](https://clinicaltrials.gov/study/NCT02194075) | Phase 4 | Termine | 60 | Methylphenidate a liberation prolongee en appoint a la fluvoxamine dans le TOC |
| [NCT04539951](https://clinicaltrials.gov/study/NCT04539951) | Phase 2 | En recrutement | 1600 | Strategies de changement ou d'augmentation apres echec du traitement initial du TOC |
| [NCT02285699](https://clinicaltrials.gov/study/NCT02285699) | Non applicable | Termine | 43 | Microbiote intestinal dans le TOC avant et apres 12 semaines d'ISRS ; n'evalue pas l'efficacite de la fluvoxamine |
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | Arrete | 407 | Pharmacovigilance des traitements psychotropes chez des patients gerontopsychiatriques |

Plusieurs autres essais enregistres (par exemple NCT03179839, NCT05737511, NCT02739061, NCT07025590) concernent des interventions non medicamenteuses ou d'autres molecules et sont peu pertinents pour la fluvoxamine.

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [40143130](https://pubmed.ncbi.nlm.nih.gov/40143130/) | 2025 | Synthese de revues systematiques et meta-analyses | Pharmaceuticals | Efficacite de la fluvoxamine dans le trouble anxieux generalise, l'anxiete sociale, le trouble panique et le TOC |
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Meta-analyse en reseau | Cochrane Database Syst Rev | Traitements pharmacologiques du trouble panique chez l'adulte |
| [27318812](https://pubmed.ncbi.nlm.nih.gov/27318812/) | 2016 | Revue systematique / meta-analyse en reseau | Lancet Psychiatry | Comparaison des interventions medicamenteuses et psychotherapeutiques dans le TOC de l'adulte |
| [32039743](https://pubmed.ncbi.nlm.nih.gov/32039743/) | 2020 | Revue systematique / meta-analyse en reseau | Acta Neuropsychiatrica | Traitements pharmacologiques de l'anxiete sociale chez l'adulte |
| [29995828](https://pubmed.ncbi.nlm.nih.gov/29995828/) | 2018 | Meta-analyse | Medicine | Efficacite et tolerance de la fluvoxamine dans l'anxiete sociale de l'adulte |
| [18408531](https://pubmed.ncbi.nlm.nih.gov/18408531/) | 2008 | Revue systematique / meta-analyse | Int Clin Psychopharmacol | Efficacite et tolerance des antidepresseurs de seconde generation dans l'anxiete sociale |
| [37032427](https://pubmed.ncbi.nlm.nih.gov/37032427/) | 2023 | Recommandation (CPIC) | Clin Pharmacol Ther | Dosage guide par la pharmacogenetique (CYP2D6, CYP2C19) pour les antidepresseurs serotoninergiques |
| [24923349](https://pubmed.ncbi.nlm.nih.gov/24923349/) | 2014 | Revue | CNS Neurol Disord Drug Targets | Efficacite etablie de plusieurs ISRS, dont la fluvoxamine, dans le trouble panique |
| [19198698](https://pubmed.ncbi.nlm.nih.gov/19198698/) | 2008 | Revue | Drugs Today | Fluvoxamine a liberation controlee dans le TOC et la phobie sociale (trois etudes controlees de 12 semaines) |
| [11825104](https://pubmed.ncbi.nlm.nih.gov/11825104/) | 2002 | Revue | CNS Drugs | Fluvoxamine dans les troubles anxieux de l'enfant et de l'adolescent |

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 65470567 (annulee) | FLOXYFRAL 50 mg, comprime pellicule secable | Comprime pellicule | Non renseignee |

Aucune AMM valide n'est actuellement recensee : la seule autorisation connue (Viatris Medical) est annulee.

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (relations medicament-maladie, et non texte de la notice) : epilepsie, trouble bipolaire, trouble affectif majeur, maladie hepatique, maladie de la vesicule biliaire, trouble de la coagulation, syndrome malin des neuroleptiques, syndrome de secretion inappropriee d'ADH (y compris sa forme nephrogenique) et syndrome serotoninergique.
- **Interactions medicamenteuses** : 100 interactions recensees. Parmi celles listees, les interactions de niveau **majeur** concernent l'alosetron, la diethylpropion, le dolasetron et le bupropion. Des interactions de niveau modere sont notees, entre autres, avec l'acide acetylsalicylique, la clarithromycine, la morphine, la pioglitazone, l'aprepitant, la dexamethasone, l'hydrocortisone et le chlorpropamide.
- **Points d'attention issus de la litterature** : inhibition forte du CYP1A2 et du CYP2C19, variabilite pharmacogenetique (CYP2D6/CYP2C19), risque de convulsions en association avec certaines phenothiazines, suicidalite chez l'enfant et l'adolescent, sudation, effets digestifs et dysfonctions sexuelles.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles : veuillez consulter la notice pour les informations de securite completes.

## Conclusion et Prochaines Etapes

**Decision : Proceed with Guardrails**

**Justification :**
- Le trouble anxieux est soutenu par des essais de Phase 3 termines (TOC pediatrique, troubles anxieux de l'enfant) et par de nombreuses meta-analyses, mais il recoupe largement les indications deja connues ; il s'agit d'une extension plus que d'un veritable repositionnement.
- Le statut de marche (AMM annulee uniquement) limite la disponibilite, et les donnees de securite officielles sont manquantes.

**Pour avancer, les elements suivants sont necessaires :**
- Recuperer la notice officielle (mises en garde, contre-indications) aupres de l'ANSM, etape bloquante pour le criblage de securite.
- Obtenir les donnees detaillees sur le mecanisme d'action (DrugBank).
- Clarifier la disponibilite en France (autres specialites ou importation) compte tenu de l'AMM annulee.
- Mettre en place un dosage guide par le genotype (CYP2D6/CYP2C19) et un criblage systematique des interactions.
- Verifier les resultats d'essais recents ; les Phases 3 identifiees portent surtout sur des populations pediatriques.
- Pour les autres candidates : agoraphobie (L1) et depression endogene (L2, essai NCT04160377 de statut inconnu) meritent un suivi ; les troubles de la personnalite et la torticolis paroxystique benin du nourrisson restent en « Hold » faute de preuves.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

