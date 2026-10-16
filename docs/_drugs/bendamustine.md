---
layout: default
title: Bendamustine
parent: Preuves élevées (L1-L2)
nav_order: 94
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Bendamustine : nouvelle indication prédite, Lymphome du manteau (niveau de preuve L1). Indication d'origine : Lymphome folliculaire"
monitor_inn: "BENDAMUSTINE"
predicted_indications: ["mantle cell lymphoma", "chronic myelogenous leukemia, BCR-ABL1 positive", "Hodgkins lymphoma", "small intestinal Burkitt lymphoma", "small intestinal mucosa-associated lymphoid tissue lymphoma", "thyroid gland mucosa-associated lymphoid tissue lymphoma", "breast mucosa-associated lymphoid tissue lymphoma", "tonsillar lymphoma", "MALT lymphoma", "relapsing-remitting multiple sclerosis"]
---

# Bendamustine
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

# Bendamustine : Du Lymphome Folliculaire au Lymphome du Manteau

## Resume en Une Phrase

Bendamustine est un agent alkylant initialement utilise pour traiter le lymphome folliculaire, les neoplasmes des cellules B matures, la leucemie lymphoblastique aigue et le syndrome de Richter.
Le modele TxGNN predit qu'il pourrait etre efficace pour le **Lymphome du Manteau**,
avec **39 essais cliniques** et **20 publications** soutenant actuellement cette direction, dont plusieurs essais randomises de Phase 3.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Lymphome folliculaire (les textes d'indication des AMM francaises ne sont pas renseignes ; indication issue du graphe de connaissances) |
| Nouvelle Indication Predite | Lymphome du manteau |
| Score de Prediction TxGNN | 99,63 % |
| Niveau de Preuve | L1 |
| Statut de Marche en France | Annule uniquement (aucune AMM valide) |
| Nombre d'AMM | 2 (toutes deux annulees) |
| Decision Recommandee | Proceed with Guardrails |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles. Sur la base des informations connues, la bendamustine est un agent alkylant possedant aussi des proprietes proches des analogues puriques, actif contre les hemopathies malignes a cellules B.

Le lymphome du manteau est un neoplasme des cellules B matures, tres proche des indications d'origine (lymphome folliculaire, neoplasmes des cellules B matures). Le mecanisme commun, a savoir les lesions de l'ADN dans les cellules B malignes, est donc directement transposable.

Cette plausibilite est renforcee par la litterature : l'association bendamustine-rituximab (BR) est un schema de reference, utilise comme base dans de nombreux essais recents associant des inhibiteurs de BTK (ibrutinib, acalabrutinib, orelabrutinib).

## Preuves d'Essais Cliniques

Le tableau presente les 10 essais les plus pertinents parmi ceux compiles. Plusieurs autres essais de Phase 2 completes existent, notamment NCT00891839 (BR en rechute/refractaire, n=45) et NCT01737177 (R2-B, n=42).

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT00991211](https://clinicaltrials.gov/study/NCT00991211) | Phase 3 | Termine | 549 | BR vs R-CHOP en premiere ligne dans les lymphomes indolents et du manteau (non-inferiorite sur la survie sans progression) |
| [NCT00877006](https://clinicaltrials.gov/study/NCT00877006) | Phase 3 | Termine | 447 | Etude BRIGHT : BR vs R-CVP ou R-CHOP en premiere ligne (lymphome indolent ou du manteau) |
| [NCT01776840](https://clinicaltrials.gov/study/NCT01776840) | Phase 3 | Termine | 523 | Ibrutinib + BR vs placebo + BR chez les patients de 65 ans et plus nouvellement diagnostiques |
| [NCT02972840](https://clinicaltrials.gov/study/NCT02972840) | Phase 3 | Actif, hors recrutement | 635 | Acalabrutinib + BR vs placebo + BR, lymphome du manteau non traite |
| [NCT06363994](https://clinicaltrials.gov/study/NCT06363994) | Phase 3 | En recrutement | 476 | Orelabrutinib + BR vs BR, lymphome du manteau non traite |
| [NCT06084936](https://clinicaltrials.gov/study/NCT06084936) | Phase 3 | En recrutement | 182 | Glofitamab vs choix de l'investigateur (dont BR) en rechute/refractaire |
| [NCT01073163](https://clinicaltrials.gov/study/NCT01073163) | Phase 3 | Termine | 54 | Effet de BR sur l'intervalle QT |
| [NCT00891839](https://clinicaltrials.gov/study/NCT00891839) | Phase 2 | Termine | 45 | BR en lymphome du manteau en rechute/refractaire |
| [NCT04115631](https://clinicaltrials.gov/study/NCT04115631) | Phase 2 | Actif, hors recrutement | 360 | Trois schemas a base de BR, avec ou sans cytarabine a haute dose et acalabrutinib, chez les patients de 70 ans et moins |
| [NCT03834688](https://clinicaltrials.gov/study/NCT03834688) | Phase 2 | Termine | 33 | Venetoclax + BR chez les patients de plus de 60 ans non traites |

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [23433739](https://pubmed.ncbi.nlm.nih.gov/23433739/) | 2013 | ECR (Phase 3) | Lancet | BR comparee a R-CHOP en premiere ligne dans les lymphomes indolents et du manteau (non-inferiorite) |
| [24591201](https://pubmed.ncbi.nlm.nih.gov/24591201/) | 2014 | ECR (Phase 3) | Blood | Etude BRIGHT : BR comparee a R-CHOP/R-CVP chez les patients naifs de traitement |
| [30811293](https://pubmed.ncbi.nlm.nih.gov/30811293/) | 2019 | Cohorte | J Clin Oncol | Suivi a 5 ans de l'etude BRIGHT |
| [35657079](https://pubmed.ncbi.nlm.nih.gov/35657079/) | 2022 | ECR | N Engl J Med | Ibrutinib + BR dans le lymphome du manteau non traite |
| [40311141](https://pubmed.ncbi.nlm.nih.gov/40311141/) | 2025 | ECR | J Clin Oncol | Acalabrutinib + BR dans le lymphome du manteau non traite |
| [41052510](https://pubmed.ncbi.nlm.nih.gov/41052510/) | 2025 | ECR (Phase 2/3) | Lancet | Etude ENRICH : ibrutinib-rituximab vs immunochimiotherapie (R-CHOP ou BR) chez les patients de 60 ans et plus |
| [32126141](https://pubmed.ncbi.nlm.nih.gov/32126141/) | 2020 | Analyse groupee d'essais de Phase 2 | Blood Adv | Induction rituximab/bendamustine puis rituximab/cytarabine avant autogreffe |
| [40975105](https://pubmed.ncbi.nlm.nih.gov/40975105/) | 2025 | Phase 2 mono-bras | Lancet Haematol | R-BAC puis venetoclax chez les patients ages a haut risque |
| [41132246](https://pubmed.ncbi.nlm.nih.gov/41132246/) | 2025 | Recommandations | HemaSphere | Recommandations EHA-EU MCL network pour le diagnostic et le traitement |
| [42034605](https://pubmed.ncbi.nlm.nih.gov/42034605/) | 2026 | Cohorte multicentrique (755 patients) | Blood Cancer J | Evolution apres BR en premiere ligne puis inhibiteur de BTK en deuxieme ligne |

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 64457346 | BENDAMUSTINE MEDAC 2,5 mg/mL | Poudre pour solution a diluer pour perfusion | Non renseignee (AMM annulee) |
| 61826343 | BENDAMUSTINE ARROW 2,5 mg/mL | Poudre pour solution a diluer pour perfusion | Non renseignee (AMM annulee) |

## Cytotoxicite

| Element | Contenu |
|------|------|
| Classification de Cytotoxicite | Cytotoxique conventionnel (agent alkylant) |
| Risque de Myelosuppression | Eleve : les contre-indications du graphe de connaissances incluent thrombopenie, neutropenie, agranulocytose et anemie |
| Classification d'Emetogenicite | Moyenne a faible (selon la classe ; a confirmer dans la notice) |
| Elements de Surveillance | NFS avec formule (neutrophiles, plaquettes, hemoglobine), fonction hepatique et renale |
| Protection de Manipulation | Doit suivre les reglementations de manipulation des medicaments cytotoxiques |

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : insuffisance hepatique, maladie renale, pyoureter, maladie hepatique, maladie de la vesicule biliaire, thrombopenie, neutropenie, agranulocytose, anemie, anemie macrocytaire.
- **Interactions medicamenteuses** : 100 interactions repertoriees. Les plus notables sont de niveau **majeur** : deferiprone et samarium (153Sm) lexidronam (risque probable de toxicite hematologique additive). Interactions de niveau modere, entre autres : omeprazole, esomeprazole, cimetidine, caffeine, deferasirox, mercaptopurine, ticlopidine, chloramphenicol, roflumilast, osilodrostat, acide obeticholique.

Les mises en garde et contre-indications de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de securite.

## Conclusion et Prochaines Etapes

**Decision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais randomises de Phase 3 completes (dont NCT00991211 et NCT00877006) et des publications de haut niveau (Lancet, NEJM, J Clin Oncol) soutiennent l'usage de la bendamustine associee au rituximab dans le lymphome du manteau. Le niveau de preuve est L1.
- Cependant, aucune AMM francaise n'est actuellement valide, les donnees de securite issues de la notice sont absentes et le profil hematologique est a risque.

**Pour avancer, les elements suivants sont necessaires :**
- Recuperer la notice de l'ANSM (mises en garde, contre-indications) pour lever le point bloquant de securite
- Obtenir les donnees detaillees sur le mecanisme d'action (DrugBank)
- Clarifier le statut reglementaire francais (AMM annulees, alternatives commercialisees)
- Definir un plan de surveillance hematologique et des ajustements posologiques (insuffisance hepatique ou renale, personnes agees)

### Autres indications predites (a titre informatif)

- **Lymphome MALT** (99,21 %) : L2, Proceed with Guardrails ; Phase 2 dediee (NCT01015248, n=60) et series retrospectives, sans Phase 3 specifique.
- **Lymphome de Hodgkin** (99,55 %) : L2, question de recherche ; donnees limitees a de petites etudes de Phase 1/2.
- **Lymphome de Burkitt de l'intestin grele** et **lymphome MALT de l'intestin grele** : L3, question de recherche.
- **Leucemie myeloide chronique BCR-ABL1 positive**, **lymphomes MALT thyroidien et mammaire**, **lymphome amygdalien** : L4 a L5, Hold.
- **Sclerose en plaques remittente-recurrente** (99,21 %) : L5, Hold ; aucune donnee, profil de securite preoccupant.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

