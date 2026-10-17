---
layout: default
title: Clomipramine
parent: Prédiction du modèle uniquement (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Clomipramine : nouvelle indication prédite, Trouble anxieux (niveau de preuve L5). Indication d'origine : Trouble obsessionnel compulsif"
monitor_inn: "CLOMIPRAMINE"
predicted_indications: ["benign paroxysmal torticollis of infancy", "histrionic personality disorder (disease)", "schizoid personality disorder", "paranoid personality disorder", "schizotypal personality disorder", "agoraphobia", "attention deficit-hyperactivity disorder"]
---

# Clomipramine
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

# Clomipramine : Du Trouble Obsessionnel Compulsif au Trouble Anxieux

## Resume en Une Phrase

Clomipramine est un antidepresseur tricyclique, initialement utilise pour le traitement du trouble obsessionnel compulsif (TOC).
Le modele TxGNN predit qu'il pourrait etre efficace pour le **trouble anxieux** (en pratique, surtout le trouble panique et l'agoraphobie),
avec **8 essais cliniques** et **20 publications** retenus dans les donnees compilees pour cette indication. Ces essais portent presque exclusivement sur le TOC et non sur les troubles anxieux eux-memes.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Trouble obsessionnel compulsif (source : graphe de connaissances ; le texte d'indication des AMM n'est pas renseigne) |
| Nouvelle Indication Predite | Trouble anxieux |
| Score de Prediction TxGNN | 99,93 % |
| Niveau de Preuve | L1 (selon l'evaluation des donnees compilees ; a nuancer, voir ci-dessous) |
| Statut de Marche en France | Toutes les AMM sont annulees (aucune AMM valide) |
| Nombre d'AMM | 3 |
| Decision Recommandee | Proceed with Guardrails |

**Nuance sur le niveau de preuve :** le niveau L1 est attribue dans les donnees compilees, mais les essais listes sont majoritairement centres sur le TOC, et la plupart ne sont pas des essais directs dans les troubles anxieux. Le soutien le plus solide provient de meta-analyses et de recommandations portant sur le trouble panique. Une lecture prudente situerait la preuve directe entre L2 et L3.

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles dans les donnees compilees. Sur la base des informations connues, la clomipramine est un puissant inhibiteur de la recapture de la serotonine, avec une activite noradrenergique via son metabolite actif, la desmethylclomipramine. Son efficacite dans le TOC est etablie.

Le TOC a longtemps ete classe parmi les troubles anxieux, et il partage avec le trouble panique et l'agoraphobie des voies serotoninergiques et noradrenergiques. Le transfert du TOC vers les troubles anxieux est donc mecanistiquement plausible. Des reseaux de meta-analyses et les recommandations de la WFSBP placent la clomipramine parmi les agents efficaces dans le trouble panique.

Deux limites : les essais enregistres utilisent surtout la clomipramine comme comparateur ou comme base d'augmentation dans le TOC, et la tolerance (effets anticholinergiques, conduction cardiaque, seuil convulsif) la place derriere les ISRS.

Parmi les autres predictions, **l'agoraphobie** (niveau L2, etudes anciennes et de petite taille, dont un essai en medecine generale contre diazepam et des essais dans le trouble panique) et la **depression majeure** (niveau L1, meta-analyses) sont les mieux soutenues. Les predictions pour les troubles de la personnalite (histrionique, schizoide, paranoide, schizotypique) et la torticolis paroxystique benin du nourrisson ne reposent que sur le modele (L4-L5, decision Hold). Pour le TDAH, la question reste a l'etude (niveau L3).

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT00466609](https://clinicaltrials.gov/study/NCT00466609) | Phase 4 | Termine | 54 | Strategies d'augmentation dans le TOC non repondeur : fluoxetine seule, fluoxetine + quetiapine, fluoxetine + clomipramine |
| [NCT00004310](https://clinicaltrials.gov/study/NCT00004310) | Phase 2 | Inconnu | 76 | Clomipramine intraveineuse vs orale dans le TOC |
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Phase 4 | Termine | 21 | Augmentation par quetiapine vs clomipramine des ISRS dans le TOC resistant |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Termine | 124 | TCC associee a un inhibiteur de la recapture de la serotonine dans le TOC pediatrique (reponse partielle) |
| [NCT05737511](https://clinicaltrials.gov/study/NCT05737511) | Phase 4 | Pas encore en recrutement | 80 | Hydroxyzine vs traitement habituel dans le trouble panique (essai pilote) |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | Non applicable | Termine | 26 | Prediction de la reponse clomipramine vs escitalopram dans le TOC |
| [NCT00254735](https://clinicaltrials.gov/study/NCT00254735) | Phase 3 | Termine | 44 | Augmentation par quetiapine dans le TOC severe (sur fond ISRS/clomipramine) |
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | Termine prematurement | 407 | Pharmacovigilance en gerontopsychiatrie ; contexte de securite uniquement |

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Meta-analyse en reseau | Cochrane Database Syst Rev | Traitements pharmacologiques du trouble panique de l'adulte |
| [40788541](https://pubmed.ncbi.nlm.nih.gov/40788541/) | 2026 | Meta-analyse en reseau | Eur Arch Psychiatry Clin Neurosci | Efficacite et acceptabilite comparees des anxiolytiques |
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2026 | Revue systematique | Psychother Psychosom | Options therapeutiques dans les troubles anxieux resistants |
| [35900217](https://pubmed.ncbi.nlm.nih.gov/35900217/) | 2023 | Recommandations | World J Biol Psychiatry | Recommandations WFSBP pour l'anxiete, le TOC et le TSPT |
| [6373161](https://pubmed.ncbi.nlm.nih.gov/6373161/) | 1984 | ECR | Curr Med Res Opin | Clomipramine vs diazepam dans l'agoraphobie et la phobie sociale en medecine generale (33 patients analyses) |
| [22290995](https://pubmed.ncbi.nlm.nih.gov/22290995/) | 1993 | ECR | J Psychopharmacol | Effets psychomoteurs et cognitifs de la clomipramine, imipramine et placebo actif dans le trouble panique (54 patients) |
| [2651491](https://pubmed.ncbi.nlm.nih.gov/2651491/) | 1989 | Cohorte (essai ouvert) | J Clin Psychopharmacol | Clomipramine a faible dose : arret complet des attaques de panique chez 13 patients sur 17 |
| [11277602](https://pubmed.ncbi.nlm.nih.gov/11277602/) | 2001 | Etude de recherche de dose | J Psychopharmacol | Remission complete chez 70,3 % des 81 patients ; aucune rechute pendant l'entretien |
| [9585709](https://pubmed.ncbi.nlm.nih.gov/9585709/) | 1998 | Essai controle | Am J Psychiatry | Exercice aerobie, clomipramine et placebo dans le trouble panique |
| [18849910](https://pubmed.ncbi.nlm.nih.gov/18849910/) | 2008 | Revue | CNS Spectrums | Traitement medical du TOC et de l'anxiete ; clomipramine efficace mais plus d'effets indesirables |

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 69281119 | ANAFRANIL 25 mg/2 ml, solution injectable (ALFASIGMA FRANCE) | Solution injectable | Non renseignee (AMM annulee) |
| 69273510 | ANAFRANIL 10 mg, comprime enrobe (ALFASIGMA FRANCE) | Comprime enrobe | Non renseignee (AMM annulee) |
| 61426025 | ANAFRANIL 75 mg, comprime pelliculé secable (ALFASIGMA FRANCE) | Comprime pelliculé secable | Non renseignee (AMM annulee) |

## Considerations de Securite

Les informations de la notice (mises en garde, contre-indications) ne sont pas disponibles dans les donnees compilees. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : epilepsie, trouble bipolaire de type maniaque, maladie hepatique, maladie de la vesicule biliaire, abus ou dependance a des substances, hyperthermie maligne, phaeochromocytome, paragangliome sympathique, cancers (duodenum, intestin grele, coeur, surrenale), neuroblastome, glaucome, hyperthyroidie (maladie de Basedow, thyreotoxicose).
- **Interactions medicamenteuses** : 100 interactions recensees. Interactions majeures notamment avec l'epinephrine, le bupropion, la lorcaserine, le citrate de potassium et le cisapride. Interactions moderees avec, entre autres, la famotidine, la cimetidine, la clarithromycine, la morphine, l'acide acetylsalicylique, ainsi que des anticholinergiques (atropine, hyoscyamine, glycopyrronium, clidinium) et le lopéramide.
- **Points de vigilance rapportes dans la litterature** : effets anticholinergiques, effets cardiaques, abaissement du seuil convulsif, dysfonction sexuelle, rare toxicite hematologique (pancytopenie), toxicite en cas de surdosage et risque suicidaire chez les sujets jeunes. Une initiation a faible dose et une titration lente sont recommandees en raison de l'agitation initiale.

## Conclusion et Prochaines Etapes

**Decision : Proceed with Guardrails**

**Justification :**
- Les meta-analyses et recommandations dans le trouble panique, ainsi que plusieurs etudes cliniques anciennes dans le trouble panique et l'agoraphobie, soutiennent un benefice plausible. Toutefois, les essais enregistres sont centres sur le TOC, et les AMM francaises sont toutes annulees. Le niveau L1 est donc a interpreter avec prudence.

**Pour avancer, les elements suivants sont necessaires :**
- Les mises en garde et contre-indications officielles de la notice ANSM (lacune bloquante pour le criblage de securite)
- Les donnees detaillees sur le mecanisme d'action (DrugBank)
- Des essais controles contemporains de la clomipramine dans les troubles anxieux (trouble panique), versus ISRS
- Verification du statut reglementaire en France, toutes les AMM etant annulees, y compris la voie d'acces possible
- Un plan de surveillance cardiaque, hematologique et du risque suicidaire, avec precaution pour les patients presentant les contre-indications listees
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

