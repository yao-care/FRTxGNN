---
layout: default
title: Ketoconazole
parent: Preuves modérées (L3-L4)
nav_order: 423
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Ketoconazole : nouvelle indication prédite, Acné (niveau de preuve L4). Indication d'origine : Données d'indication non renseignées dans les AMM"
---

# Ketoconazole
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **1** 
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

# Kétoconazole : Des Mycoses Cutanées à l'Acné

## Résumé en Une Phrase

Le kétoconazole est un antifongique imidazolé, utilisé à l'origine pour traiter les mycoses cutanées (teigne du pied, pityriasis versicolor, candidoses cutanées) et la dermite séborrhéique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**acné**, mais cette prédiction repose pour l'instant surtout sur le modèle : **1 essai clinique** (non randomisé en phase, de petite taille, sans résultats) et des publications indirectes, dont des études in vitro, soutiennent cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Données d'indication non renseignées dans les AMM ; le graphe de connaissances cite notamment la teigne du pied, la dermite séborrhéique, le pityriasis versicolor et les candidoses cutanées |
| Nouvelle Indication Prédite | Acné |
| Score de Prédiction TxGNN | 99,80 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le kétoconazole inhibe la CYP51 fongique (lanostérol 14-alpha-déméthylase), ce qui explique son activité antifongique. À des expositions plus élevées, il inhibe aussi des enzymes humaines de la stéroïdogenèse (CYP17A1, CYP11A1) et peut ainsi diminuer la synthèse d'androgènes. Les données compilées pour ce rapport ne contiennent pas de description détaillée du mécanisme d'action ; cette analyse repose sur les connaissances pharmacologiques générales et sur le raisonnement mécanistique associé à la prédiction.

Le lien avec l'acné est plausible sur deux plans. D'une part, une baisse des androgènes pourrait réduire la production de sébum, moteur de l'acné, y compris dans les contextes hyperandrogéniques comme le SOPK. D'autre part, l'application topique pourrait diminuer la colonisation par *Malassezia* (*Pityrosporum*), associée à l'inflammation folliculaire et aux éruptions acnéiformes (folliculite à Malassezia, pustulose céphalique néonatale). Deux études in vitro suggèrent en outre une activité contre *Propionibacterium acnes* (inhibition de sa lipase et de sa croissance).

Il faut rester prudent : le score TxGNN est une prédiction computationnelle, non une preuve clinique. La voie topique est la plus plausible, car l'usage systémique est difficilement justifiable au vu des risques d'hépatotoxicité et de suppression surrénalienne.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | Non applicable | Actif, ne recrute plus | 52 | Comparaison randomisée de la crème de kétoconazole 2 % et de la crème d'adapalène 2 % dans l'acné comédonienne et papulo-pustuleuse légère, sur 12 semaines ; aucun résultat disponible |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | Étude in vitro | Microbiol Immunol | Le kétoconazole inhibe l'activité de la lipase de *P. acnes* et pourrait être une alternative dans l'acné |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | Étude in vitro | Biol Pharm Bull | Activité in vitro des azolés contre *P. acnes* issus de patients acnéiques |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Série clinique | Clin Exp Dermatol | Folliculite à *Pityrosporum* souvent confondue avec l'acné ; essais thérapeutiques chez 62 patients |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Rapport de cas | Arch Dermatol | Association entre éruption papulo-pustuleuse néonatale et infection à *Malassezia furfur* |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Revue | Keio J Med | *Pityrosporum ovale* impliqué dans plusieurs dermatoses (pityriasis versicolor, folliculite, dermite séborrhéique) |
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Revue | Dermatology | Mise à jour sur les traitements systémiques de l'acné |
| [32872149](https://pubmed.ncbi.nlm.nih.gov/32872149/) | 2020 | Revue | Pharmaceuticals (Basel) | Potentiel thérapeutique de l'adapalène (comparateur de l'essai), traitement de première ligne de l'acné |

Aucun essai randomisé ni revue systématique évaluant directement le kétoconazole dans l'acné n'a été identifié. Les autres références recensées sont peu pertinentes (SOPK, syndrome de Cushing, dermatologie générale).

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60557096 | KETODERM 2 %, crème | Crème | Non renseignée (AMM annulée) |
| 60347710 | KETOCONAZOLE VIATRIS 2 %, crème | Crème | Non renseignée (AMM annulée) |
| 61393881 | KETOCONAZOLE ZYDUS 2 %, gel en sachet-dose | Gel | Non renseignée (AMM annulée) |
| 60502840 | KETOCONAZOLE EG 2 %, gel en récipient-unidose | Gel | Non renseignée (AMM annulée) |
| 69406163 | KETOCONAZOLE ESTEVE 200 mg, comprimé | Comprimé | Non renseignée (AMM annulée) |

Au total, 20 AMM sont recensées, toutes annulées, aucune n'étant valide actuellement.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : syndrome du QT long (y compris familial), torsades de pointes, maladie du foie, maladie de la vésicule biliaire, insuffisance corticosurrénale (maladie d'Addison), atrophie cutanée, télangiectasies (dont la maladie de Rendu-Osler), maladies capillaires, maladie vasculaire périphérique (claudication intermittente, artériopathie), achlorhydrie.
- **Interactions médicamenteuses** : 658 interactions recensées. Parmi les principales de niveau **majeur** : lopéramide, triamcinolone, budésonide. De niveau modéré : famotidine, ranitidine, oméprazole, rabéprazole (antiacides et inhibiteurs de la pompe à protons, dont l'absorption du kétoconazole oral dépend de l'acidité gastrique), hydrocortisone, dexaméthasone, bétaméthasone, pioglitazone, alosétron, aprépitant, atropine, hyoscyamine, méthscopolamine, bisacodyl.
- **Risques systémiques** : le kétoconazole oral comporte des risques graves d'hépatotoxicité et de suppression surrénalienne (mises en garde encadrées). La voie topique est donc la seule envisageable pour l'acné.

Les mises en garde et contre-indications issues des notices ANSM ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est L4 : un seul essai de petite taille, sans résultats, et des données surtout in vitro ou indirectes. De plus, toutes les AMM françaises sont annulées et les données de sécurité de la notice sont absentes, ce qui empêche l'étape de dépistage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Résultats de l'essai NCT07237763 (efficacité et tolérance de la crème 2 % versus adapalène)
- Essais randomisés de phase 2/3 contrôlés par placebo ou comparateur actif sur formulation topique
- Récupération et analyse de la notice ANSM (mises en garde, contre-indications)
- Données détaillées sur le mécanisme d'action (DrugBank)
- Clarification de la voie d'administration et de la disponibilité d'une formulation topique commercialisée en France, compte tenu des AMM annulées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

