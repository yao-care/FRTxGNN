---
layout: default
title: Prasugrel
parent: Prédiction du modèle uniquement (L5)
nav_order: 622
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Prasugrel : nouvelle indication prédite, Trouble migraineux (rang 2 (niveau de preuve L5). Indication d'origine : Syndrome coronarien aigu"
monitor_inn: "PRASUGREL"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura", "kyphoscoliotic heart disease", "rheumatoid arthritis", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "migraine with or without aura, susceptibility to", "brachydactyly-syndactyly syndrome", "leprosy"]
---

# Prasugrel
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

## Prasugrel : Du Syndrome Coronarien Aigu au Trouble Migraineux
{: .text-alpha }

## Resume en Une Phrase

Prasugrel est un antiagregant plaquettaire (inhibiteur du recepteur P2Y12), initialement utilise dans le traitement du syndrome coronarien aigu.
Le modele TxGNN predit qu'il pourrait etre efficace pour l'**hypertension pulmonaire** (prediction classee en premier), mais les preuves disponibles sont tres faibles : aucun essai clinique, et seulement 2 publications sans rapport direct avec cette indication.
Ce rapport retient donc comme piste la mieux documentee le **trouble migraineux**, soutenu par **2 essais cliniques** (indirects) et **2 publications** de petite taille.

> Note de lecture : la prediction de rang 1 (hypertension pulmonaire) est quasi sans preuve. La migraine (rang 2, score quasi identique) est la seule indication avec un corpus de preuves exploitable. Le titre et les sections de preuves portent sur la migraine.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Syndrome coronarien aigu (source : graphe de connaissances ; les textes d'indication des AMM sont vides) |
| Nouvelle Indication Predite | Trouble migraineux (rang 2 ; rang 1 : hypertension pulmonaire, niveau L5) |
| Score de Prediction TxGNN | 99,88 % (hypertension pulmonaire : 99,88 %) |
| Niveau de Preuve | L3 (migraine) |
| Statut de Marche en France | Toutes les AMM sont annulees (aucune AMM valide) |
| Nombre d'AMM | 4 (toutes annulees) |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles dans les donnees compilees pour ce rapport. Sur la base des informations connues, prasugrel est une thienopyridine antagoniste du recepteur plaquettaire P2Y12 ; il inhibe l'agregation plaquettaire et son efficacite dans le syndrome coronarien aigu est etablie.

Dans la migraine, l'hypothese avancee est la suivante : chez les patients migraineux porteurs d'un foramen ovale perméable (FOP), le passage paradoxal de substances activant les plaquettes ou vasoactives (par exemple la serotonine) pourrait declencher les crises. L'inhibition de P2Y12 par les thienopyridines (clopidogrel, prasugrel) ou par le ticagrelor pourrait attenuer cet effet. Le lien avec l'indication originale est donc indirect : il s'agit du meme mecanisme antiplaquettaire, applique a un contexte different, et uniquement dans une population selectionnee (migraine avec FOP).

Cette hypothese reste a confirmer : les essais retrouves testent la fermeture du FOP par dispositif, et non prasugrel lui-meme. Pour l'hypertension pulmonaire, le lien (role des plaquettes dans le remodelage vasculaire) est plausible mais non demontre.

---

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT07629635](https://clinicaltrials.gov/study/NCT07629635) | Phase 3 | En recrutement | 32 | Traitement oriente vers le FOP dans la migraine (fermeture du FOP ou prasugrel mentionne dans le contexte) ; preuve indirecte, pas encore de resultats |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | Non applicable | Termine prematurement | 7 | Occluseur septal GORE CARDIOFORM contre placebo/simulacre dans la migraine ; essai de dispositif, faible valeur pour prasugrel |

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Etude de cohorte retrospective | Neurology | Revue de l'usage hors AMM des thienopyridines chez des migraineux avec FOP |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Etude pilote ouverte (ticagrelor) | Neurology | Etude pilote avec un inhibiteur P2Y12 apparente, faisant suite a l'observation d'une reduction des migraines sous clopidogrel et prasugrel chez certains patients avec FOP |
| [42722054](https://pubmed.ncbi.nlm.nih.gov/42722054/) | 2026 | Preclinique (souris) | European Journal of Pharmacology | Effet neuroprotecteur de prasugrel dans un modele d'epilepsie par kindling ; maladie differente, pertinence faible pour la migraine |

---

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 63610757 | PRASUGREL KRKA 10 mg (annulee) | Comprime pellicule | Non renseignee |
| 67461428 | PRASUGREL EG 10 mg (annulee) | Comprime pellicule | Non renseignee |
| 64503651 | PRASUGREL BGR 10 mg (annulee) | Comprime pellicule | Non renseignee |
| 65916489 | EFIENT 10 mg (annulee) | Comprime pellicule | Non renseignee |

---

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hepatique, trouble hypotensif, maladie de la coagulation, accident vasculaire cerebral, trouble cerebrovasculaire, infarctus cerebral, traumatisme, purpura thrombocytopenique, hemorragie intracranienne, accident ischemique transitoire, insuffisance vertebrobasilaire.
- **Interactions medicamenteuses** (100 interactions repertoriees) :
  - Majeures : deferasirox, ibritumomab tiuxetan.
  - Moderees : acide acetylsalicylique, morphine, opium, fenfluramine, dexfenfluramine, sibutramine.
  - Mineures : antagonistes H2 (famotidine, ranitidine, cimetidine, nizatidine) et inhibiteurs de la pompe a protons (omeprazole, esomeprazole, pantoprazole, lansoprazole, dexlansoprazole, rabeprazole), bupropion.

Les mises en garde et contre-indications issues de la notice de l'ANSM n'ont pas pu etre recuperees ; veuillez consulter la notice pour les informations de securite completes. Le risque hemorragique inherent a la classe est a considerer avec une attention particuliere.

---

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- Le niveau de preuve est L3 pour la migraine (etudes observationnelles et pilote sur des molecules apparentees) et L5 pour l'hypertension pulmonaire. Aucun essai randomise n'a evalue prasugrel lui-meme, toutes les AMM francaises sont annulees et les donnees de securite de la notice manquent, ce qui empeche le passage au criblage de securite.

**Pour avancer, les elements suivants sont necessaires :**
- Recuperer la notice de l'ANSM (mises en garde et contre-indications) pour realiser le criblage de securite.
- Obtenir les donnees detaillees sur le mecanisme d'action (DrugBank).
- Definir une population cible (migraine avec FOP) et evaluer le rapport benefice/risque hemorragique, notamment au regard des contre-indications cerebrovasculaires.
- Disposer d'un essai randomise testant directement prasugrel dans la migraine avec FOP ; suivre les resultats de NCT07629635.
- Clarifier le statut reglementaire en France (AMM annulees) avant toute perspective d'usage.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

