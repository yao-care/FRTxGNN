---
layout: default
title: Insulin Detemir
parent: Prédiction du modèle uniquement (L5)
nav_order: 401
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "insulin detemir"
predicted_indications: ["autoimmune oophoritis", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
description: "Insulin Detemir : nouvelle indication prédite, Autoimmune oophoritis (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Insulin Detemir
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Insulin Detemir: Autoimmune oophoritis
{: .text-alpha }

## Résumé en Une Phrase

L'insuline détémir est un analogue de l'insuline basale à action prolongée, initialement utilisé pour le traitement du diabète sucré et de l'acidocétose diabétique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **diabète de type 1**, avec **40 essais cliniques** et **20 publications** soutenant actuellement cette direction.
Il s'agit toutefois d'une indication déjà établie : ce n'est pas un véritable repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Autoimmune oophoritis |
| Score de Prédiction TxGNN | 0.9967 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les informations connues, l'insuline détémir est un analogue de l'insuline humaine à action prolongée, acylé par un acide gras en C14 (acide myristique). Cette modification lui permet de se lier de façon réversible à l'albumine, ce qui ralentit son absorption et prolonge son effet métabolique jusqu'à 24 heures.

Dans le diabète de type 1, le pancréas ne produit plus assez d'insuline. L'insuline basale remplace cette insuline manquante en se fixant sur le récepteur de l'insuline. Le diabète de type 1 relève donc directement de l'indication d'origine (diabète sucré) : la prédiction du modèle reflète un usage déjà établi, et non une nouvelle piste thérapeutique.

Les autres indications prédites (par exemple l'ovarite auto-immune, l'opsismodysplasie, le syndrome de la personne raide ou les lipodystrophies localisées) ne disposent d'aucun essai clinique ni d'aucune publication. Les lipodystrophies localisées correspondent en réalité à un effet indésirable connu des injections d'insuline, et non à un bénéfice thérapeutique.

---

## Preuves d'Essais Cliniques

Parmi les essais compilés, voici les plus pertinents (essais de phase 3 randomisés en priorité, puis études observationnelles de grande taille).

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Phase 3 | Terminé | 114 | Détémir + asparte vs NPH + asparte chez l'adulte avec diabète de type 1 : comparaison de l'efficacité et de la sécurité sur le contrôle glycémique |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Phase 3 | Terminé | 330 | Comparaison en double aveugle sur 12 mois de la détémir issue de deux procédés de fabrication (NN729 vs actuel), en schéma basal-bolus |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Phase 3 | Terminé | 347 | Détémir vs NPH chez l'enfant et l'adolescent avec diabète de type 1, en association à l'insuline asparte |
| [NCT00184639](https://clinicaltrials.gov/study/NCT00184639) | Phase 3 | Terminé | 71 | Détémir vs insuline Semilente MC sur 32 semaines chez l'enfant, l'adolescent et le jeune adulte |
| [NCT00117780](https://clinicaltrials.gov/study/NCT00117780) | Phase 4 | Terminé | 520 | Détémir en une ou deux injections par jour en schéma basal-bolus avec asparte (HbA1c, hypoglycémies, poids) |
| [NCT00978627](https://clinicaltrials.gov/study/NCT00978627) | Phase 3 | Terminé | 548 | Insuline dégludec/asparte vs détémir + asparte dans le diabète de type 1 (la détémir sert de comparateur) |
| [NCT01542463](https://clinicaltrials.gov/study/NCT01542463) | N/A | Terminé | 4 464 | Étude non interventionnelle européenne sur la sécurité, le contrôle glycémique et le poids sous détémir (diabète de type 1 ou 2) |
| [NCT01709929](https://clinicaltrials.gov/study/NCT01709929) | Phase 3 | Terminé | 2 287 | Étude de sécurité ouverte, non randomisée, de la détémir en Amérique du Nord (diabète de type 1 ou 2) |
| [NCT00440439](https://clinicaltrials.gov/study/NCT01440439) | Phase 4 | Statut inconnu | 30 | Détémir vs glargine : contrôle glycémique et métabolisme pendant l'exercice dans le diabète de type 1 |
| [NCT00322257](https://clinicaltrials.gov/study/NCT00322257) | Phase 3 | Arrêté | 596 | Insuline inhalée aux repas vs asparte injectée, la détémir servant d'insuline basale de fond (preuve indirecte) |

*Remarque : au total, 40 essais sont associés à cette indication ; seuls 10 sont présentés ici. Les essais de phase 1 et les études observationnelles supplémentaires ne sont pas détaillés.*

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | ECR | Lancet Diabetes Endocrinol | Essai EXPECT : dégludec vs détémir (avec asparte) chez la femme enceinte avec diabète de type 1, étude de non-infériorité |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | Revue systématique / méta-analyse | Cochrane Database Syst Rev | Analogues d'insuline (ultra-)longue durée d'action dans le diabète de type 1 : bénéfices sur les complications et les hypoglycémies |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Revue systématique / méta-analyse | Drugs Today (Barc) | Analogues de l'insuline chez l'enfant et l'adolescent avec diabète de type 1 |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Revue systématique / méta-analyse | Pol Arch Med Wewn | Détémir vs NPH dans le diabète de type 1 : amélioration du contrôle glycémique non confirmée par tous les investigateurs |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Revue systématique / méta-analyse en réseau | Value Health | Efficacité et sécurité relatives des schémas d'insuline basale chez l'adulte avec diabète de type 1 |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Revue | Vasc Health Risk Manag | Profil pharmacocinétique moins variable que la NPH ; réduction du risque d'hypoglycémie (surtout nocturne) |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Revue | Drugs | Effet plus prévisible et plus constant que la NPH, avec moindre variabilité intra-individuelle |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Revue | Vasc Health Risk Manag | Mise à jour sur la détémir : taux d'hypoglycémie plus faible, HbA1c comparable |
| [17881328](https://pubmed.ncbi.nlm.nih.gov/17881328/) | 2007 | Revue | Endocrinol Metab Clin North Am | Pharmacologie de la détémir : propriétés moléculaires et pharmacodynamie |
| [17881330](https://pubmed.ncbi.nlm.nih.gov/17881330/) | 2007 | Revue | Endocrinol Metab Clin North Am | Traitement intensif du diabète et poids corporel : moindre prise de poids avec la détémir |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66688750 | LEVEMIR PENFILL 100 Unités/mL, solution injectable en cartouche | Solution injectable | Non renseignée (AMM active) |
| 66481292 | LEVEMIR INNOLET 100 Unités/mL, solution injectable en stylo prérempli | Solution injectable | Non renseignée (AMM active) |
| 64529525 | LEVEMIR FLEXPEN 100 Unités/mL, solution injectable en stylo prérempli | Solution injectable | Non renseignée (AMM active) |

Les trois AMM sont annulées, ce qui limite la disponibilité pratique du produit en France.

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 353 interactions sont répertoriées. Les principales, de niveau modéré, concernent :
  - les agents sympathomimétiques et bêta-2 mimétiques (phényléphrine, épinéphrine, pseudoéphédrine, salbutamol, formotérol) ;
  - le bêtabloquant acébutolol ;
  - les corticoïdes (hydrocortisone) ;
  - les œstrogènes (éthinylestradiol, estradiol) ;
  - les autres antidiabétiques (metformine, pioglitazone, alogliptine, albiglutide) ;
  - l'acétazolamide, l'hydrochlorothiazide, la doxycycline, l'alpélisib et l'éthanol.

  Quelques interactions mineures concernent des corticoïdes topiques (hydrocortisone, alclométasone).

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 3 terminés et des méta-analyses soutiennent l'efficacité et la sécurité de l'insuline détémir dans le diabète de type 1. Il s'agit toutefois d'un usage déjà établi et non d'un repositionnement.
- Les autres indications prédites (rangs 2 à 10) sont recommandées en « Hold » ou « Research Question » : aucune preuve clinique ni mécanistique. La prédiction de lipodystrophie correspond à un signal de sécurité, non à un bénéfice.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action
- Mises en garde et contre-indications issues de la notice officielle (ANSM)
- Clarification de la raison du retrait des AMM et de l'existence d'alternatives commercialisées (autres insulines basales)
- Plan de surveillance de l'hypoglycémie et des interactions médicamenteuses, notamment avec les antidiabétiques et les sympathomimétiques
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

