---
layout: default
title: Pegaspargase
parent: Preuves élevées (L1-L2)
nav_order: 582
evidence_level: L1
indication_count: 10
---

# Pegaspargase
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

# Pegaspargase : De la leucémie lymphoblastique aiguë au lymphome/leucémie lymphoblastique à précurseurs

## Résumé en Une Phrase

Pegaspargase est une forme pégylée de la L-asparaginase, initialement utilisée pour traiter la leucémie lymphoblastique aiguë (LAL).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **lymphome/leucémie lymphoblastique à précurseurs**, une entité très proche de l'indication d'origine, avec **35 essais cliniques** et **19 publications** soutenant actuellement cette direction.
Il s'agit en pratique d'une indication déjà établie ou très voisine, et non d'un repositionnement au sens strict.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie lymphoblastique aiguë (indication d'origine du graphe de connaissances ; le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Lymphome/leucémie lymphoblastique à précurseurs |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Retiré (AMM annulée uniquement) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les sources compilées. Sur la base des informations connues, pegaspargase est une L-asparaginase d'*Escherichia coli* conjuguée au polyéthylène glycol. Elle dégrade l'asparagine circulante. Les lymphoblastes expriment peu d'asparagine synthétase et dépendent de l'asparagine extérieure : sa déplétion bloque la synthèse protéique et induit l'apoptose.

C'est le même mécanisme que celui de l'indication d'origine (LAL). Le lymphome et la leucémie lymphoblastiques à précurseurs sont deux expressions d'une même maladie. Les protocoles de LAL sont d'ailleurs appliqués au lymphome lymphoblastique. Le score très élevé du modèle (0,9996) est cohérent avec les données cliniques existantes.

## Preuves d'Essais Cliniques

Les 35 essais sont rattachés à cette prédiction ; les plus pertinents sont listés ci-dessous. Dans la plupart, la pegaspargase est un composant du schéma de chimiothérapie et non la variable testée.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00967057](https://clinicaltrials.gov/study/NCT00967057) | Phase 3 | Terminé | 470 | ALLR3 : chimiothérapie de la LAL en rechute ou réfractaire de l'enfant, avec une base contenant de l'asparaginase |
| [NCT00103285](https://clinicaltrials.gov/study/NCT00103285) | Phase 3 | Terminé | 5377 | Comparaison de schémas de chimiothérapie dans la LAL B à précurseurs de risque standard |
| [NCT00905034](https://clinicaltrials.gov/study/NCT00905034) | Phase 2 | Terminé | 37 | Schéma MOAD (méthotrexate, vincristine, L-asparaginase pégylée, dexaméthasone) dans la LAL en rechute |
| [NCT00890656](https://clinicaltrials.gov/study/NCT00890656) | Phase 2 | Terminé | 90 | Hyper-CVAD augmenté en rattrapage de la LAL |
| [NCT01005914](https://clinicaltrials.gov/study/NCT01005914) | Phase 2 | Arrêté | 11 | Ajout de PEG-asparaginase à l'hyper-CVAD dans la LAL de l'adulte nouvellement diagnostiquée |
| [NCT02003222](https://clinicaltrials.gov/study/NCT02003222) | Phase 3 | Actif, hors recrutement | 488 | Blinatumomab ajouté à la chimiothérapie dans la LAL B de l'adulte (pegaspargase non testée en tant que telle) |
| [NCT05602194](https://clinicaltrials.gov/study/NCT05602194) | Phase 3 | Actif, hors recrutement | 440 | Lévocarnitine pour prévenir l'hépatotoxicité liée à l'asparaginase (volet sécurité) |
| [NCT03643276](https://clinicaltrials.gov/study/NCT03643276) | Phase 3 | En recrutement | 5000 | Protocole AIEOP-BFM ALL 2017 chez l'enfant et l'adolescent |
| [NCT03914625](https://clinicaltrials.gov/study/NCT03914625) | Phase 3 | Actif, hors recrutement | 6720 | Blinatumomab avec chimiothérapie dans la LAL B de risque standard ou le lymphome B lymphoblastique localisé |
| [NCT01190930](https://clinicaltrials.gov/study/NCT01190930) | Phase 3 | Terminé | 9350 | Chimiothérapie adaptée au risque dans la LAL B de risque standard ou le lymphome B lymphoblastique localisé |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | ECR | J Clin Oncol | Essai de phase 3 AALL1231 : bortézomib dans la LAL T et le lymphome T lymphoblastique nouvellement diagnostiqués |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | ECR | J Clin Oncol | Essai de phase 3 AALL0434 : nélarabine dans la LAL T nouvellement diagnostiquée |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | ECR | J Clin Oncol | AALL0232 : dexaméthasone et méthotrexate à haute dose dans la LAL B à haut risque |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Cohorte | Blood Adv | Essai GIMEMA LAL1913 : programme de LAL de l'adulte avec pegaspargase |
| [31030380](https://pubmed.ncbi.nlm.nih.gov/31030380/) | 2019 | Revue | Drugs | Revue de la pegaspargase dans la LAL, indiquée en association chez l'enfant et l'adulte |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Revue | Haematologica | Consensus d'experts sur la prévention et la prise en charge des événements indésirables chez l'adulte |
| [40858769](https://pubmed.ncbi.nlm.nih.gov/40858769/) | 2025 | Cohorte | Ann Hematol | Tolérance de la pegaspargase chez les patients de 55 ans ou plus (programme LAL1913) |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Étude clinique | J Clin Oncol | DFCI 11-001 : efficacité et toxicité de la pegaspargase et de la calaspargase pégol chez l'enfant |
| [40492422](https://pubmed.ncbi.nlm.nih.gov/40492422/) | 2025 | Cohorte | Br J Haematol | Intégration du blinatumomab en consolidation dans le schéma CALGB 10403 |
| [9161659](https://pubmed.ncbi.nlm.nih.gov/9161659/) | 1997 | Revue | Ann Pharmacother | Revue de la chimie, de la pharmacologie et de la clinique de la pegaspargase |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61861579 | ONCASPAR 750 U/ml, poudre pour solution injectable/pour perfusion (Laboratoires Servier) | Poudre pour solution injectable ou pour perfusion | Non renseignée ; AMM annulée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Agent antinéoplasique enzymatique (déplétion de l'asparagine), non cytotoxique conventionnel au sens classique |
| Risque de Myélosuppression | Faible en monothérapie ; le risque dépend surtout des autres agents du schéma. Les données compilées ne le détaillent pas |
| Classification d'Émétogénicité | Faible (selon la classe du médicament ; non précisée dans les données compilées) |
| Éléments de Surveillance | Fonction hépatique, triglycérides, glycémie, lipase/amylase (pancréatite), paramètres de coagulation, signes d'hypersensibilité |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 378 interactions sont recensées. Les 20 premières examinées sont toutes de niveau modéré. Elles concernent notamment :
  - les corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide) ;
  - les antidiabétiques (metformine, acarbose, alogliptine, canagliflozine, dapagliflozine, saxagliptine, albiglutide, dulaglutide, chlorpropamide) ;
  - l'acide acétylsalicylique, la doxycycline, la tétracycline, la clarithromycine, le bupropion et l'acide chénodésoxycholique.
- **Toxicités décrites dans la littérature** : hypersensibilité, pancréatite, hépatotoxicité, thrombose, hypertriglycéridémie et hyperglycémie, plus marquées chez l'adulte plus âgé et le patient obèse.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles : elles ne figurent pas dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Les essais de phase 3 menés dans la LAL, avec des schémas contenant de l'asparaginase, et la littérature clinique abondante soutiennent cette indication. Elle est cependant déjà établie, et non un repositionnement nouveau.
- Le profil de toxicité exige un encadrement strict.
- L'AMM française est annulée, ce qui limite l'accès commercial local.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications officielles de la notice (source ANSM), actuellement manquantes et bloquantes pour l'évaluation de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Clarification du statut réglementaire en France et de la disponibilité du produit après l'annulation de l'AMM
- Plan de surveillance de la sécurité pour les populations à risque (adultes de plus de 40 ans, patients obèses)

**Remarque sur les autres prédictions :** les autres indications prédites sont, pour la plupart, soit l'indication d'origine (LAL, L1), soit sans preuve (leucémie lymphoïde chronique, lymphome folliculaire, déficit en méthylcobalamine cblE : L5, Hold). Le lymphome lymphoïde au sens large et le lymphome de Hodgkin (L3) reposent surtout sur des données de lymphomes NK/T extranodaux, ce qui ne soutient pas directement ces prédictions.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

