---
layout: default
title: Miglustat
parent: Prédiction du modèle uniquement (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
---

# Miglustat
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Miglustat : De la maladie de Gaucher de type 1 au syndrome d'ichtyose autosomique à évolution fatale

## Résumé en Une Phrase

Miglustat est un inhibiteur de la glucosylcéramide synthase, initialement développé pour la maladie de Gaucher de type 1 (indication citée par la littérature ; les textes d'indication des AMM françaises ne sont pas renseignés).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome d'ichtyose autosomique à évolution fatale** (score de 99,83 %), mais **aucun essai clinique et aucune publication** ne soutiennent cette prédiction.
Parmi les 10 prédictions, seule la **maladie de Tay-Sachs** (rang 7) dispose de preuves : **5 essais cliniques** et **20 publications**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM ; maladie de Gaucher de type 1 selon la littérature (PMID 12808890) |
| Nouvelle Indication Prédite | Syndrome d'ichtyose autosomique à évolution fatale |
| Score de Prédiction TxGNN | 99,83 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 7 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, miglustat inhibe la glucosylcéramide synthase, première enzyme de la synthèse des glycosphingolipides. Son efficacité dans la maladie de Gaucher de type 1 est reconnue, et cette logique de « réduction de substrat » pourrait s'appliquer à d'autres maladies de surcharge en glycosphingolipides.

Pour le syndrome d'ichtyose autosomique à évolution fatale, le lien est faible. Le métabolisme des céramides de la barrière cutanée n'est que vaguement lié à la cible du médicament. Le libellé de la maladie est en outre peu spécifique. Il s'agit d'une prédiction du modèle, sans aucune donnée clinique ni bibliographique.

Les autres prédictions se répartissent en trois groupes :
- **Lien mécanistique solide, avec des preuves :** la maladie de Tay-Sachs (rang 7, détaillée plus bas).
- **Lien plausible mais non démontré :** la maladie de Krabbe, la leucodystrophie métachromatique, le déficit en prosaposine et la neurodégénérescence associée à l'hydroxylase des acides gras (FAHN).
- **Lien faible ou inexistant :** la maladie de Wolman, la maladie de stockage des esters de cholestérol, l'ichtyose récessive liée à l'X et la tumeur bénigne de la surrénale (probable artefact du graphe de connaissances).

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour le syndrome d'ichtyose autosomique à évolution fatale.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour cette indication.

### Prédiction la mieux documentée : maladie de Tay-Sachs (rang 7)

Score TxGNN : 99,75 %. Niveau de preuve : L2. Recommandation du dossier : question de recherche.

Le mécanisme est cohérent : miglustat réduit la synthèse du ganglioside GM2, qui s'accumule dans les maladies de Tay-Sachs et de Sandhoff à cause du déficit en hexosaminidase A. L'efficacité clinique n'est cependant pas démontrée. L'essai randomisé dans la forme tardive n'a pas montré de bénéfice net sur ses critères principaux, et les études des formes infantiles sont petites, ouvertes et en partie interrompues.

**Essais cliniques**

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Phase 2 | Terminé | 5 | Pharmacocinétique et tolérance de Zavesca dans la gangliosidose à GM2 juvénile (doses uniques et répétées) |
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Phase 3 | Terminé | 10 | Pharmacocinétique, sécurité et tolérance dans la gangliosidose à GM2 infantile (Tay-Sachs classique, Sandhoff infantile) |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Phase 3 | Interrompu | 30 | Effets de miglustat sur les symptômes neurologiques et systémiques des formes infantiles de Sandhoff et Tay-Sachs |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Phase 4 | Interrompu | 16 | Syner-G : miglustat associé à un régime cétogène dans les gangliosidoses ; l'association empêche d'attribuer l'effet à miglustat seul |
| [NCT07399704](https://clinicaltrials.gov/study/NCT07399704) | Phase 2 | En recrutement | 21 | Étude ouverte à long terme du nizubaglustat (AZ-3102) dans la gangliosidose à GM2 ou la maladie de Niemann-Pick C. Il s'agit probablement d'un autre agent que miglustat (soutien indirect, à vérifier) |

**Littérature**

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | ECR | Genet Med | Étude randomisée de 12 mois, suivie de 24 mois de traitement prolongé, de miglustat dans la maladie de Tay-Sachs tardive (sécurité et efficacité) |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Revue systématique | Eur J Neurol | Efficacité et sécurité de miglustat dans la gangliosidose à GM2, après des résultats antérieurs jugés incohérents |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Rapport de cas | Neurology | Deux patients avec Tay-Sachs infantile : la détérioration neurologique n'a pas été arrêtée, mais miglustat a été détecté dans le LCR et la macrocéphalie a été évitée |
| [32867370](https://pubmed.ncbi.nlm.nih.gov/32867370/) | 2020 | Revue | Int J Mol Sci | Tableau clinique, physiopathologie et thérapies actuelles des gangliosidoses à GM2 |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Revue | Front Physiol | Nouvelles approches thérapeutiques de la maladie de Tay-Sachs |
| [30743792](https://pubmed.ncbi.nlm.nih.gov/30743792/) | 2009 | Revue (non classée) | Expert Rev Endocrinol Metab | Thérapie par réduction de substrat avec miglustat dans les maladies à surcharge en glycosphingolipides touchant le cerveau |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Revue | Curr Opin Investig Drugs | Développement de miglustat : approuvé dans l'UE pour la maladie de Gaucher, en développement pour Tay-Sachs, Fabry et Niemann-Pick C |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Cohorte | Mol Genet Metab | Chronologie des changements cliniques dans les gangliosidoses infantiles ; miglustat limité par ses effets digestifs |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Cohorte | J Inherit Metab Dis | Étude pilote de tests neurocognitifs dans Tay-Sachs tardive, pour évaluer un futur critère de jugement |
| [9103204](https://pubmed.ncbi.nlm.nih.gov/9103204/) | 1997 | Préclinique (souris) | Science | Chez la souris Tay-Sachs, le N-butyldésoxynojirimycine (NB-DNJ), composé apparenté à miglustat, a empêché l'accumulation de GM2 dans le cerveau |

## Informations de Marché en France

7 AMM sont recensées ; les 5 premières sont listées ci-dessous. Le texte de l'indication approuvée n'est pas renseigné dans les données.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 65793983 | ZAVESCA 100 mg | Gélule | Janssen-Cilag International NV |
| 66036869 | MIGLUSTAT ACCORD 100 mg | Gélule | Accord Healthcare France |
| 61255179 | MIGLUSTAT GEN.ORPH 100 mg | Gélule | Gen.Orph |
| 64394668 | MIGLUSTAT BLUEFISH 100 mg | Gélule | Bluefish Pharmaceuticals (Suède) |
| 62931799 | MIGLUSTAT DIPHARMA 100 mg | Gélule | Dipharma Arzneimittel (Allemagne) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour l'indication prédite en premier rang (ichtyose autosomique à évolution fatale), il n'existe ni essai ni publication, et le lien mécanistique est faible : le niveau de preuve est L5.
- La maladie de Tay-Sachs est la seule prédiction avec des preuves (niveau L2), mais l'efficacité clinique n'est pas démontrée. Elle relève d'une recherche ciblée, pas d'une recommandation.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité).
- Les données détaillées sur le mécanisme d'action (MOA), à obtenir via DrugBank.
- Les textes d'indication approuvée des AMM françaises.
- Une vérification de l'ECR de Tay-Sachs tardive (PMID 19346952) et de la revue systématique de 2023 (PMID 37209042) pour juger du bénéfice réel.
- Une vérification que NCT07399704 concerne bien un autre agent (nizubaglustat).
- Une clarification du libellé de la maladie « ichtyose autosomique à évolution fatale » avant toute recherche.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

