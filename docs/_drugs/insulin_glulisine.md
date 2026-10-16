---
layout: default
title: Insulin Glulisine
parent: Preuves élevées (L1-L2)
nav_order: 403
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Insulin Glulisine : nouvelle indication prédite, Diabète de type 1 (niveau de preuve L1). Indication d'origine : Diabète sucré"
monitor_inn: "insulin glulisine"
predicted_indications: ["type 1 diabetes mellitus", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "autoimmune oophoritis", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
---

# Insulin Glulisine
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

# Insuline glulisine : Du diabète sucré au diabète de type 1

## Résumé en Une Phrase

L'insuline glulisine est un analogue de l'insuline à action rapide, initialement utilisé pour le traitement du diabète sucré et de l'acidocétose diabétique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **diabète de type 1**, avec **28 essais cliniques** et **19 publications** soutenant actuellement cette direction.
Il faut noter qu'il s'agit ici moins d'un véritable repositionnement que de la confirmation d'une indication existante, le diabète de type 1 relevant du diabète sucré.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Diabète sucré ; acidocétose diabétique (source : graphe de connaissances, le texte d'indication des AMM n'étant pas renseigné) |
| Nouvelle Indication Prédite | Diabète de type 1 |
| Score de Prédiction TxGNN | 99,55 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances pharmacologiques générales, l'insuline glulisine est un analogue de l'insuline humaine à action rapide : elle se lie au récepteur de l'insuline et abaisse la glycémie, avec un début d'action plus rapide et une durée plus courte que l'insuline humaine ordinaire.

Le diabète de type 1 est caractérisé par une carence en insuline. Le remplacement par une insuline prandiale est donc le fondement du traitement. L'indication prédite est ainsi une sous-catégorie directe de l'indication d'origine (diabète sucré), ce qui explique le score très élevé du modèle.

Un point pratique important : toutes les AMM françaises identifiées sont annulées. La disponibilité du produit constitue donc une contrainte pratique, et non une lacune de preuves.

---

## Preuves d'Essais Cliniques

Les 10 essais les plus pertinents sont présentés ci-dessous (sur 28 essais recensés). Les essais de phase 3 contrôlés et ceux jugés directement pertinents ont été privilégiés.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00115570](https://clinicaltrials.gov/study/NCT00115570) | Phase 3 | Terminé | 572 | Glulisine vs lispro chez l'enfant et l'adolescent atteints de diabète de type 1, sur 26 semaines (objectif : efficacité et sécurité comparables) |
| [NCT00290979](https://clinicaltrials.gov/study/NCT00290979) | Phase 3 | Terminé | 250 | Étude de non-infériorité vs lispro sur 28 semaines dans le diabète de type 1 (variation de l'HbA1c) |
| [NCT00467376](https://clinicaltrials.gov/study/NCT00467376) | Phase 3 | Terminé | 485 | Glulisine vs lispro sur 12 semaines, associées à la glargine, dans le diabète de type 1 ou 2 |
| [NCT00397553](https://clinicaltrials.gov/study/NCT00397553) | Phase 3 | Terminé | 104 | Efficacité et sécurité de la glulisine avec la glargine dans le diabète de type 1 (étude non randomisée) |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Phase 3 | Terminé | 59 | Sécurité de la glulisine vs insuline asparte en pompe (CSII) : occlusions de cathéter, HbA1c, hypoglycémies |
| [NCT07070752](https://clinicaltrials.gov/study/NCT07070752) | Phase 3 | Terminé | 224 | Non-infériorité immunogénique de GP40321 vs Apidra SoloStar dans le diabète de type 1 |
| [NCT00607087](https://clinicaltrials.gov/study/NCT00607087) | Phase 4 | Terminé | 289 | Glulisine vs asparte et lispro en pompe : hyperglycémies inexpliquées et occlusions de cathéter |
| [NCT01621776](https://clinicaltrials.gov/study/NCT01621776) | Non applicable | Terminé | 107 | Comparaison randomisée glulisine vs lispro sur l'hyperglycémie postprandiale en conditions réelles |
| [NCT01204593](https://clinicaltrials.gov/study/NCT01204593) | Phase 4 | Terminé | 206 | Schéma basal-bolus glargine + glulisine dans le diabète de type 1 préalablement non contrôlé (variation de l'HbA1c à 24 semaines) |
| [NCT00964574](https://clinicaltrials.gov/study/NCT00964574) | Phase 4 | Terminé | 68 | Efficacité et sécurité de la glulisine avec la glargine dans le diabète de type 1 (étude non randomisée) |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | ECR | Horm Metab Res | Glulisine vs lispro chez l'adulte atteint de diabète de type 1 (683 patients randomisés) : étude multicentrique, ouverte, en groupes parallèles |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | Essai clinique | Diabetes Obes Metab | Efficacité et sécurité de la glulisine vs lispro chez des patients japonais atteints de diabète de type 1, avec glargine en insuline basale |
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Étude clinique | Acta Diabetol | Comparaison glulisine, lispro et asparte en pompe dans le diabète de type 1 (HbA1c, glycémie à jeun, hypoglycémies, acidocétose) |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Étude clinique | Pediatr Int | Glulisine en perfusion sous-cutanée continue chez 20 enfants : amélioration des glycémies postprandiales après 1 an |
| [20150026](https://pubmed.ncbi.nlm.nih.gov/20150026/) | 2010 | Revue | Endocr Pract | Analogues d'insuline rapides vs insuline humaine ordinaire en schéma basal-bolus dans le diabète de type 1 |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Revue | Drugs Today | Analogues de l'insuline dans le diabète de type 1 de l'enfant et de l'adolescent |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Revue | Drugs | Revue de l'usage de la glulisine : efficacité comparable au lispro, non-infériorité vis-à-vis d'autres insulines rapides |
| [16706558](https://pubmed.ncbi.nlm.nih.gov/16706558/) | 2006 | Revue | Drugs | Début d'action plus rapide que l'insuline humaine ordinaire, contrôle glycémique similaire dans le diabète de type 1 |
| [18076215](https://pubmed.ncbi.nlm.nih.gov/18076215/) | 2008 | Pharmacocinétique | Clin Pharmacokinet | Pharmacocinétique et pharmacodynamie de la glulisine : absorption plus rapide et durée d'action plus courte |
| [25865292](https://pubmed.ncbi.nlm.nih.gov/25865292/) | 2016 | Revue | Diabetes Metab Res Rev | Perfusion sous-cutanée continue d'insuline : populations, sécurité, efficacité et pharmacoéconomie |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 64684582 | APIDRA SOLOSTAR 100 unités/ml, stylo prérempli | Solution injectable | Non renseignée | Annulée |
| 62679768 | APIDRA 100 Unités/ml, cartouche | Solution injectable | Non renseignée | Annulée |
| 65554613 | APIDRA 100 Unités/ml, flacon | Solution injectable | Non renseignée | Annulée |

Les trois AMM sont détenues par SANOFI AVENTIS (Allemagne).

---

## Considérations de Sécurité

- **Interactions médicamenteuses** : 353 interactions sont recensées. Parmi les exemples les plus notables, de niveau modéré :
  - agents sympathomimétiques et bêta-agonistes (phényléphrine, épinéphrine, pseudoéphédrine, salbutamol, formotérol) ;
  - autres antidiabétiques (metformine, pioglitazone, alogliptine, albiglutide) ;
  - bêtabloquants (acébutolol), hydrochlorothiazide, acétazolamide, corticoïdes (hydrocortisone), œstrogènes (estradiol, éthinylestradiol), doxycycline, éthanol, alpélisib.

  Des interactions de niveau mineur concernent les corticoïdes topiques (hydrocortisone, alclométasone).

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations, notamment pour le risque d'hypoglycémie.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 3 comparant la glulisine au lispro ou à l'asparte dans le diabète de type 1, ainsi que des ECR publiés, soutiennent l'efficacité et la sécurité (niveau L1). Il s'agit toutefois d'une confirmation d'indication existante, non d'un véritable repositionnement.
- Toutes les AMM françaises sont annulées, et les données de sécurité de la notice sont absentes ; ces points justifient des garde-fous.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde, contre-indications) auprès de l'ANSM.
- Compléter les données sur le mécanisme d'action via DrugBank.
- Clarifier les raisons de l'annulation des AMM et la disponibilité réelle du produit en France.
- Définir un plan de surveillance de l'hypoglycémie et des interactions médicamenteuses pertinentes.

---

## Autres Indications Prédites (Information Complémentaire)

Les neuf autres indications prédites ne reposent sur aucun essai clinique ni publication. Elles sont à considérer comme de simples prédictions informatiques (**Hold**).

| Rang | Indication | Score TxGNN | Niveau de Preuve | Commentaire |
|------|------|------|------|------|
| 2 | Syndrome de dysfonctionnement répondant à la thiamine | 99,47 % | L5 | Probable proximité avec des nœuds liés au diabète |
| 3 | Opsismodysplasie | 99,46 % | L5 | Aucun mécanisme plausible ; probable artefact du graphe |
| 4 | Syndrome de la personne raide classique | 99,46 % | L5 | Probable comorbidité auto-immune avec le diabète de type 1 (anticorps anti-GAD) |
| 5 | Syndrome du membre raide focal | 99,46 % | L5 | Même origine probable que le précédent |
| 6 | Ovarite auto-immune | 99,37 % | L5 | Association auto-immune avec le diabète de type 1 |
| 7 | Agénésie du pancréas | 99,17 % | L4 | Substitution insulinique plausible pour le diabète qui en résulte, sans donnée spécifique à la glulisine |
| 8 | Lipodystrophie localisée d'origine médicamenteuse | 99,15 % | L5 | L'insuline est une cause connue, non un traitement |
| 9 | Lipodystrophie centrifuge | 99,11 % | L5 | Aucune justification thérapeutique |
| 10 | Lipoatrophie localisée induite par la pression | 99,10 % | L5 | L'insuline peut provoquer la lipoatrophie, non la traiter |
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

