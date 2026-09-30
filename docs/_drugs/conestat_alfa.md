---
layout: default
title: Conestat Alfa
parent: Preuves élevées (L1-L2)
nav_order: 91
evidence_level: L1
indication_count: 10
---

# Conestat Alfa
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

# Conestat alfa : Déficit en inhibiteur de C1, une prédiction qui correspond à l'indication déjà commercialisée

## Résumé en Une Phrase

Conestat alfa (Ruconest) est un inhibiteur de la C1 estérase humain recombinant, produit chez le lapin transgénique. Il est déjà utilisé pour traiter les crises aiguës d'angiœdème héréditaire (AOH).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **déficit en inhibiteur de C1**, avec **41 essais cliniques** et **20 publications** à l'appui. Il s'agit ici d'un usage conforme à l'indication existante, et non d'un repositionnement au sens strict.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Déficit en inhibiteur de C1 (correspond à l'indication déjà commercialisée) |
| Score de Prédiction TxGNN | 99,999 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Dans le déficit en inhibiteur de C1, la protéine SERPING1 manque ou est non fonctionnelle. Cette protéine freine le complément (C1r/C1s) ainsi que les voies de contact du kallikréine et du facteur XIIa. Sans ce frein, la bradykinine est produite en excès, ce qui provoque les crises d'œdème. Conestat alfa remplace directement la protéine manquante et limite ainsi la production de bradykinine.

L'alignement entre le médicament et la maladie est donc direct. Les données détaillées de mécanisme d'action de DrugBank ne sont pas disponibles, mais ce mécanisme est bien décrit dans la littérature.

Le score très élevé du modèle est cohérent avec cette situation, puisque l'indication est déjà exploitée. Les autres prédictions du modèle (autres maladies) ne reposent en revanche sur aucun essai ni publication.

## Preuves d'Essais Cliniques

Sélection des 10 essais les plus pertinents, sur un total de 41 associés à cette prédiction.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00262301](https://clinicaltrials.gov/study/NCT00262301) | Phase 3 | Terminé | 75 | C1-INH recombinant vs placebo, double aveugle, traitement des crises aiguës d'AOH |
| [NCT01188564](https://clinicaltrials.gov/study/NCT01188564) | Phase 3 | Terminé | 75 | Étude de confirmation randomisée contre placebo, avec extension ouverte (50 U/kg), efficacité et immunogénicité |
| [NCT00225147](https://clinicaltrials.gov/study/NCT00225147) | Phase 2/3 | Terminé | 77 | C1-INH recombinant vs placebo, sécurité, efficacité et pharmacocinétique dans les crises aiguës |
| [NCT02247739](https://clinicaltrials.gov/study/NCT02247739) | Phase 2 | Terminé | 32 | Prophylaxie des crises, randomisée, en double aveugle, croisée sur 3 périodes |
| [NCT00851409](https://clinicaltrials.gov/study/NCT00851409) | Phase 2 | Terminé | 25 | Administrations répétées de C1-INH recombinant : sécurité, immunogénicité, effet prophylactique |
| [NCT01359969](https://clinicaltrials.gov/study/NCT01359969) | Phase 2 | Terminé | 57 | Enfants de 2 à 13 ans, étude ouverte à un seul bras (Ruconest 50 U/kg) |
| [NCT00262288](https://clinicaltrials.gov/study/NCT00262288) | Phase 2/3 | Terminé | 14 | Efficacité, sécurité et pharmacocinétique dans les crises aiguës |
| [NCT06690047](https://clinicaltrials.gov/study/NCT06690047) | Phase 4 | Terminé | 5 | Ruconest dans le prodrome de l'AOH pour éviter l'évolution vers une crise (échantillon très limité) |
| [NCT03697187](https://clinicaltrials.gov/study/NCT03697187) | Non applicable | Terminé | 152 | Registre observationnel de sécurité en vie réelle de Ruconest |
| [NCT01397864](https://clinicaltrials.gov/study/NCT01397864) | Non applicable | Terminé | 181 | Registre de sécurité et de profil immunologique après administrations uniques et répétées |

Plusieurs autres essais portent sur des C1-INH d'origine plasmatique (Berinert, Cinryze). Ils soutiennent l'approche par classe, mais pas spécifiquement conestat alfa.

## Preuves de la Littérature

Sélection de 10 publications sur 20. Les essais randomisés sont classés en premier.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [28754491](https://pubmed.ncbi.nlm.nih.gov/28754491/) | 2017 | ECR (phase 2, croisé) | Lancet | Efficacité du C1-INH recombinant en prophylaxie des crises d'AOH |
| [30021471](https://pubmed.ncbi.nlm.nih.gov/30021471/) | 2018 | Revue (classé ECR par le pack) | Expert Rev Clin Immunol | Conestat alfa en prophylaxie chez l'adulte et l'adolescent ; enregistré pour les crises aiguës en Europe et en Amérique |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Revue systématique | Pneumonol Alergol Pol | Comparaison de l'efficacité de conestat alfa, du C1-INH humain et de l'icatibant dans les crises aiguës |
| [22946752](https://pubmed.ncbi.nlm.nih.gov/22946752/) | 2012 | Revue | BioDrugs | Efficacité évaluée dans deux essais similaires randomisés contre placebo (Amérique du Nord et Europe) |
| [24801469](https://pubmed.ncbi.nlm.nih.gov/24801469/) | 2014 | Cohorte | Allergy Asthma Proc | Traitement à domicile de 65 épisodes chez 2 patientes, évaluation de l'efficacité et de la sécurité en vie réelle |
| [31982824](https://pubmed.ncbi.nlm.nih.gov/31982824/) | 2020 | Cohorte | Int Immunopharmacol | Traitement à domicile des crises et prophylaxie de courte durée : efficacité et sécurité |
| [22171564](https://pubmed.ncbi.nlm.nih.gov/22171564/) | 2012 | Cohorte | BioDrugs | Effets sur la coagulation et la fibrinolyse (risque thromboembolique des C1-INH) ; résultats non disponibles dans l'extrait |
| [26250409](https://pubmed.ncbi.nlm.nih.gov/26250409/) | 2015 | Revue | Immunotherapy | Traitement substitutif recombinant dans le déficit en C1-INH |
| [24556385](https://pubmed.ncbi.nlm.nih.gov/24556385/) | 2014 | Série de cas | Eur J Dermatol | Utilisation dans les crises résistantes ou fréquentes d'angiœdème héréditaire ou acquis |
| [39675680](https://pubmed.ncbi.nlm.nih.gov/39675680/) | 2025 | Étude clinique | J Allergy Clin Immunol | Réponse clinique et voies transcriptomiques sanguines avant et après traitement des prodromes d'AOH |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 61253153 | RUCONEST 2100 U, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Pharming Group (Pays-Bas) |
| 60634703 | RUCONEST 2100 U, poudre pour solution injectable | Poudre pour solution injectable | Pharming Group (Pays-Bas) |

## Considérations de Sécurité

Points de vigilance issus de l'analyse de repositionnement (et non de la notice ANSM) :

- **Contre-indication attendue** : allergie au lapin, car le produit est dérivé du lapin.
- **Risque thromboembolique** : à surveiller, comme pour les autres C1-INH.
- **Immunogénicité** : suivre l'apparition d'anticorps dirigés contre les protéines de l'hôte.

Les mises en garde et contre-indications officielles de l'ANSM n'ont pas pu être exploitées. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- L'indication prédite correspond à l'usage déjà commercialisé, avec plusieurs essais de phase 3 sur le C1-INH recombinant et un essai randomisé publié.
- Les preuves sont plus faibles pour la prophylaxie et l'usage pédiatrique, et la sécurité reste à confirmer sur la notice officielle.

**Pour avancer, les éléments suivants sont nécessaires :**
- Extraire et analyser la notice ANSM (mises en garde et contre-indications) : élément bloquant pour le criblage de sécurité.
- Compléter les données de mécanisme d'action depuis DrugBank.
- Vérifier l'identité du produit dans les essais classés « niveau classe » (C1-INH plasmatique ou non confirmé).
- Renseigner le texte des indications approuvées des deux AMM.

Les neuf autres prédictions du modèle (dont le serpinopathies à polymérisation toxique, la maladie de Glanzmann et le syndrome de Scott) restent en **Hold** : niveau L5, sans essai ni publication, et sans lien mécanistique plausible.

*Ces résultats sont fournis à titre de recherche et ne constituent pas un avis médical.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

