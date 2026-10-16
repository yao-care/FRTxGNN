---
layout: default
title: Miglustat
parent: Prédiction du modèle uniquement (L5)
nav_order: 500
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Miglustat : nouvelle indication prédite, Maladie de Tay-Sachs (niveau de preuve L5). Indication d'origine : Maladie de Gaucher"
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

# Miglustat : De la maladie de Gaucher à la maladie de Tay-Sachs

## Résumé en Une Phrase

Miglustat est un inhibiteur de la glucosylcéramide synthase, initialement utilisé pour le traitement de la maladie de Gaucher et de la maladie de Niemann-Pick.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie de Tay-Sachs** (la prédiction la mieux étayée parmi les dix candidates), avec **4 essais cliniques** et **11 publications** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Gaucher ; maladie de Niemann-Pick (selon le graphe de connaissances) |
| Nouvelle Indication Prédite | Maladie de Tay-Sachs |
| Score de Prédiction TxGNN | 99,75 % |
| Niveau de Preuve | L1 (selon la grille du dossier ; à nuancer, voir ci-dessous) |
| Statut de Marché en France | Toutes les AMM sont annulées |
| Nombre d'AMM | 7 (0 valide, 7 annulées) |
| Décision Recommandée | Hold |

> **Note sur le choix de l'indication :** la première indication prédite par le modèle (ichtyose autosomique, score 99,83 %) ne dispose d'aucune preuve clinique ni bibliographique. La maladie de Tay-Sachs, 7ᵉ du classement, est la seule candidate pour laquelle des données réelles existent ; elle est donc retenue pour ce rapport. Les autres prédictions sont résumées plus bas.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, miglustat inhibe la glucosylcéramide synthase (gène UGCG), enzyme clé de la synthèse des glycosphingolipides. Son efficacité dans la maladie de Gaucher de type 1 est établie. C'est le principe de la thérapie par réduction de substrat.

Dans la maladie de Tay-Sachs, un déficit en hexosaminidase A provoque l'accumulation du ganglioside GM2 dans les neurones. En réduisant la synthèse en amont des glycosphingolipides, miglustat pourrait diminuer la quantité de substrat à dégrader. Il traverse aussi la barrière hémato-encéphalique, ce qui est pertinent pour une maladie neuronopathique. La logique mécanistique est donc cohérente avec l'indication d'origine.

Les données disponibles tempèrent toutefois cet espoir. Une étude de cas de deux patients atteints de la forme infantile n'a pas montré d'arrêt de la détérioration neurologique, malgré une concentration significative du médicament dans le liquide céphalorachidien. Une revue de 2026 évoque d'ailleurs les « limites du repositionnement ».

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Phase 3 | Terminé | 10 | Pharmacocinétique, sécurité et tolérance dans la gangliosidose à GM2 infantile ; étude centrée sur la faisabilité, non sur l'efficacité |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Phase 3 | Arrêté | 30 | Effets de miglustat sur les symptômes neurologiques et systémiques des formes infantiles de Sandhoff et Tay-Sachs ; arrêt précoce |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Phase 4 | Arrêté | 16 | Schéma entéral synergique (miglustat + régime cétogène) dans les gangliosidoses ; l'apport de miglustat seul ne peut être isolé |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Phase 2 | Terminé | 5 | Pharmacocinétique et tolérance dans la gangliosidose à GM2 juvénile ; effectif très faible |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | ECR | Genetics in Medicine | Étude randomisée de 12 mois (suivi prolongé de 24 mois) sur la sécurité et l'efficacité de miglustat dans la maladie de Tay-Sachs à début tardif |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Revue systématique | European Journal of Neurology | Évaluation de l'efficacité et de la sécurité de miglustat dans la gangliosidose à GM2, les études antérieures étant jugées incohérentes |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Série de cas | Neurology | Deux patients infantiles : pas d'arrêt de la détérioration neurologique, mais concentration notable dans le LCR et prévention de la macrocéphalie |
| [42794762](https://pubmed.ncbi.nlm.nih.gov/42794762/) | 2026 | Revue | Int J Mol Sci | Justification biologique, preuves cliniques et limites du repositionnement de miglustat dans les maladies lysosomales neuronopathiques |
| [30743792](https://pubmed.ncbi.nlm.nih.gov/30743792/) | 2009 | Revue | Expert Rev Endocrinol Metab | Thérapie par réduction de substrat dans les maladies à stockage de glycosphingolipides cérébraux |
| [16763917](https://pubmed.ncbi.nlm.nih.gov/16763917/) | 2006 | Revue | J Inherit Metab Dis | Thérapie par réduction de substrat des maladies à stockage de glycosphingolipides, à partir de l'expérience dans la maladie de Gaucher |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Revue | Frontiers in Physiology | Nouvelles approches thérapeutiques dans la maladie de Tay-Sachs |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Étude pilote (cohorte) | J Inherit Metab Dis | Tests neurocognitifs dans la forme tardive, pour évaluer un critère de jugement utilisable en essai thérapeutique |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Revue d'histoire naturelle | Mol Genet Metab | Chronologie clinique des gangliosidoses infantiles ; la réduction de substrat par miglustat est limitée par les effets digestifs |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Profil de médicament | Curr Opin Investig Drugs | Développement de miglustat, notamment dans Tay-Sachs, Fabry et Niemann-Pick de type C |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65793983 | ZAVESCA 100 mg | Gélule | Non renseignée (AMM annulée) |
| 61255179 | MIGLUSTAT GEN.ORPH 100 mg | Gélule | Non renseignée (AMM annulée) |
| 64394668 | MIGLUSTAT BLUEFISH 100 mg | Gélule | Non renseignée (AMM annulée) |
| 62931799 | MIGLUSTAT DIPHARMA 100 mg | Gélule | Non renseignée (AMM annulée) |
| 66036869 | MIGLUSTAT ACCORD 100 mg | Gélule | Non renseignée (AMM annulée) |

Deux autres AMM annulées existent (OPFOLDA 65 mg, YARGESA 100 mg). Aucune AMM n'est actuellement valide.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie du système nerveux périphérique, neuropathie périphérique, insuffisance rénale.
- **Interactions médicamenteuses** : 2 interactions recensées. L'imiglucérase présente une interaction de niveau modéré. L'autre entrée correspond à la cible pharmacologique de miglustat (glucosylcéramide synthase, UGCG), et non à une interaction médicamenteuse cliniquement documentée.
- **Tolérance digestive** : la littérature signale des effets indésirables gastro-intestinaux limitant l'usage chez les nourrissons.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

## Autres Prédictions du Modèle (sans preuve clinique)

Les neuf autres candidates n'ont ni essai clinique ni publication associés (niveau L5, recommandation Hold).

| Maladie prédite | Score TxGNN | Plausibilité mécanistique |
|------|------|------|
| Ichtyose autosomique syndromique à évolution fatale | 99,83 % | Hypothétique (métabolisme des céramides épidermiques) |
| Maladie de stockage des esters de cholestérol | 99,82 % | Faible (substrats non glycosphingolipidiques) |
| Maladie de Krabbe | 99,78 % | Plausible (réduction de substrat) |
| Leucodystrophie métachromatique | 99,77 % | Plausible (voie des glycosphingolipides) |
| Maladie de Wolman | 99,76 % | Faible |
| Encéphalopathie par déficit en prosaposine | 99,75 % | Plausible |
| Tumeur bénigne de la surrénale | 99,74 % | Aucune justification claire |
| Ichtyose récessive liée à l'X | 99,73 % | Indirecte et spéculative |
| Neurodégénérescence associée à la FA2H | 99,72 % | Voie liée, sens du bénéfice incertain |

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour la maladie de Tay-Sachs, la justification mécanistique est solide et un programme clinique existe. Toutefois, les essais sont petits (5 à 30 patients), centrés sur la pharmacocinétique et la tolérance, ou arrêtés précocement. Les données de cas disponibles ne montrent pas d'arrêt de la progression neurologique. Le niveau L1 attribué par la grille repose sur la présence d'un essai de phase 3 terminé, mais cet essai n'est pas confirmatoire ; le niveau de preuve réel est inférieur.
- Les 7 AMM françaises sont toutes annulées, et la sécurité n'a pas pu être évaluée à partir de la notice (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération des mises en garde et contre-indications officielles (notice ANSM)
- Données détaillées sur le mécanisme d'action (DrugBank)
- Analyse des résultats de l'ECR de 2009 et de la revue systématique de 2023 sur l'efficacité réelle dans les gangliosidoses à GM2
- Clarification du statut réglementaire en France (raisons des annulations d'AMM, accès éventuel par autorisation d'accès compassionnel)
- Évaluation du profil de tolérance (effets digestifs, neuropathie périphérique, fonction rénale) dans les populations pédiatriques ciblées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

