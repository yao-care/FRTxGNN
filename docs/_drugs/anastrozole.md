---
layout: default
title: Anastrozole
parent: Preuves élevées (L1-L2)
nav_order: 67
evidence_level: L1
indication_count: 6
---

# Anastrozole
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **6** 
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

# Anastrozole : De l'indication originale à l'adénocarcinome mammaire féminin (indication déjà établie)

## Résumé en Une Phrase

L'anastrozole est un inhibiteur non stéroïdien de l'aromatase de troisième génération. Les données de l'ANSM compilées pour ce rapport ne précisent pas son indication d'origine.
Le modèle TxGNN le prédit comme potentiellement efficace pour le **carcinome mammaire féminin**, avec **29 essais cliniques** et **20 publications** à l'appui. Il s'agit en réalité d'une indication déjà bien établie, et non d'un repositionnement nouveau.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données réglementaires compilées |
| Nouvelle Indication Prédite | Carcinome mammaire féminin |
| Score de Prédiction TxGNN | 99,68 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Autorisations toutes annulées |
| Nombre d'AMM | 18 (0 valide, 18 annulées) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base compilée. D'après les connaissances pharmacologiques et les éléments de littérature fournis, l'anastrozole est un inhibiteur non stéroïdien de l'aromatase. Il bloque la synthèse périphérique des œstrogènes chez la femme ménopausée et prive ainsi les tumeurs mammaires à récepteurs hormonaux positifs du signal de croissance œstrogéno-dépendant.

L'indication prédite correspond donc au cœur d'usage connu du médicament. Le score TxGNN élevé est cohérent avec ce mécanisme et avec l'abondance de données de phase 3. Les champs « indication originale » et « mécanisme d'action » sont vides dans les données sources et devraient être corrigés.

Les autres indications prédites (neuroblastome, ganglioneuroblastome, tumeur rétropéritonéale, leucémie monocytaire, syndrome rare avec anomalies vertébrales et dysfonction endocrinienne et des lymphocytes T) n'ont aucune justification mécanistique claire. Elles reposent uniquement sur la prédiction informatique, sans essai ni littérature pertinente. Elles sont classées « Hold ».

## Preuves d'Essais Cliniques

Parmi les essais compilés, voici les plus pertinents :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00784680](https://clinicaltrials.gov/study/NCT00784680) | Phase 3 | Terminé | 308 | Qualité de vie sous Arimidex seul, tamoxifène seul ou association, en adjuvant chez la femme ménopausée |
| [NCT00327769](https://clinicaltrials.gov/study/NCT00327769) | Phase 3 | Terminé | 234 | Fulvestrant 250 mg vs Arimidex 1 mg en deuxième ligne, cancer avancé RE+ |
| [NCT00143390](https://clinicaltrials.gov/study/NCT00143390) | Phase 3 | Terminé | 298 | Exémestane vs anastrozole en première ligne hormonale, cancer avancé ou récidivant (non-infériorité sur le temps jusqu'à progression) |
| [NCT00301457](https://clinicaltrials.gov/study/NCT00301457) | Phase 3 | Terminé | 1914 | 6 ans vs 3 ans d'anastrozole après 2 à 3 ans de tamoxifène en adjuvant |
| [NCT00300508](https://clinicaltrials.gov/study/NCT00300508) | Phase 3 | Terminé | 856 | 3 ans d'anastrozole supplémentaires vs absence de traitement après 5 ans d'hormonothérapie adjuvante |
| [NCT03425838](https://clinicaltrials.gov/study/NCT03425838) | Phase 3 | Actif, non en recrutement | 1050 | Étude SONIA : inhibiteur de l'aromatase + inhibiteur CDK4/6 en première ou deuxième ligne |
| [NCT02246621](https://clinicaltrials.gov/study/NCT02246621) | Phase 3 | Actif, non en recrutement | 493 | Inhibiteur non stéroïdien de l'aromatase (anastrozole ou létrozole) + abémaciclib vs placebo, cancer avancé RH+/HER2- |
| [NCT00256217](https://clinicaltrials.gov/study/NCT00256217) | Phase 2 | Terminé | 42 | Chimioprévention par anastrozole dans le CCIS et le cancer invasif précoce |
| [NCT04272801](https://clinicaltrials.gov/study/NCT04272801) | Phase 2 | Actif, non en recrutement | 84 | Hormonothérapie préopératoire chez les femmes âgées pour guider la décision de radiothérapie |
| [NCT01723774](https://clinicaltrials.gov/study/NCT01723774) | Phase 2 | Actif, non en recrutement | 84 | Palbociclib + anastrozole en néoadjuvant, cancer de stade 2-3 RE+/HER2- |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | ECR | Lancet | Essai ATAC : après 5 ans, l'anastrozole prolonge significativement la survie sans maladie par rapport au tamoxifène (9366 femmes ménopausées) |
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | ECR | Lancet | IBIS-II : résultats à long terme de l'anastrozole en prévention du cancer du sein chez les femmes à haut risque |
| [27908454](https://pubmed.ncbi.nlm.nih.gov/27908454/) | 2016 | ECR | Lancet | FALCON : fulvestrant 500 mg vs anastrozole 1 mg, cancer avancé RH+ (survie sans progression) |
| [26686960](https://pubmed.ncbi.nlm.nih.gov/26686960/) | 2016 | ECR | Lancet | NSABP B-35 : résultats rapportés par les patientes, anastrozole vs tamoxifène dans le CCIS |
| [31615937](https://pubmed.ncbi.nlm.nih.gov/31615937/) | 2020 | Étude clinique | Clin Cancer Res | neoMONARCH : abémaciclib + anastrozole en néoadjuvant, forte inhibition du cycle cellulaire |
| [41632158](https://pubmed.ncbi.nlm.nih.gov/41632158/) | 2025 | Cohorte | JAMA Netw Open | Comparaison en pratique réelle de l'anastrozole, du létrozole et de l'exémestane |
| [20923259](https://pubmed.ncbi.nlm.nih.gov/20923259/) | 2010 | Revue | Expert Opin Drug Saf | Anastrozole en adjuvant : efficacité supérieure au tamoxifène dans plusieurs essais |
| [28614542](https://pubmed.ncbi.nlm.nih.gov/28614542/) | 2017 | Revue | Rev Assoc Med Bras | Anastrozole en chimioprévention et en traitement du cancer du sein |
| [17033446](https://pubmed.ncbi.nlm.nih.gov/17033446/) | 2006 | Rapport de cas | Eur J Gastroenterol Hepatol | Premier cas rapporté d'hépatotoxicité induite par l'anastrozole |
| [30851629](https://pubmed.ncbi.nlm.nih.gov/30851629/) | 2019 | In vitro | Thromb Res | Activation plaquettaire induite par les cellules tumorales, majorée par le tamoxifène et l'anastrozole |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62303214 | ARIMIDEX 1 mg (Laboratoires Juvisé Pharmaceuticals), annulée | Comprimé pelliculé | Non renseignée |
| 68676387 | ARIMIDEX 1 mg (Difarmed, Espagne), annulée | Comprimé pelliculé | Non renseignée |
| 69997905 | ANASTROZOLE ARROW 1 mg, annulée | Comprimé pelliculé | Non renseignée |
| 68434537 | ANASTROZOLE BIOGARAN 1 mg, annulée | Comprimé pelliculé | Non renseignée |
| 65664198 | ANASTROZOLE SANDOZ 1 mg, annulée | Comprimé pelliculé | Non renseignée |

Au total, 18 AMM sont recensées, toutes annulées. Seules cinq sont listées ici.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Hormonothérapie antinéoplasique (inhibiteur de l'aromatase), non cytotoxique conventionnel |
| Risque de Myélosuppression | Faible (aucune donnée de toxicité hématologique dans les données compilées) |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | Fonction hépatique (un cas d'hépatotoxicité rapporté), densité minérale osseuse, bilan lipidique et risque cardiovasculaire |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, hors texte de notice) : ischémie myocardique, maladie coronarienne.
- **Interactions médicamenteuses** : 100 interactions recensées dans la base DDInter, toutes de niveau de gravité non précisé. Parmi elles : bupropion, pantoprazole, glimépiride, morphine, metformine, oméprazole, rosiglitazone, prednisone, simvastatine, hydrocortisone, acide acétylsalicylique, glibenclamide, glipizide.
- **Signaux issus de la littérature** : un cas d'hépatotoxicité, des effets osseux (perte de densité minérale) étudiés dans plusieurs essais, et un risque thromboembolique évoqué par des travaux in vitro.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, non disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le carcinome mammaire RH+ chez la femme ménopausée est une indication solidement établie, avec plusieurs essais de phase 3 terminés (ATAC, FALCON, IBIS-II, NSABP B-35) : le niveau de preuve est L1. La décision est assortie de garde-fous car les AMM françaises sont toutes annulées et les données de sécurité de la notice manquent.
- Les autres prédictions (neuroblastome, ganglioneuroblastome, leucémie monocytaire, tumeur rétropéritonéale, syndrome rare) restent en « Hold » : niveau L4 à L5, sans justification mécanistique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), une lacune bloquante pour l'étape de sécurité.
- Compléter le mécanisme d'action et l'indication d'origine dans les données sources (DrugBank).
- Clarifier la raison de l'annulation des 18 AMM et la disponibilité effective du produit en France (autres procédures d'autorisation, importation).
- Qualifier le niveau de gravité des interactions médicamenteuses, en particulier avec les médicaments cardiovasculaires, vu les contre-indications du graphe de connaissances (ischémie myocardique, maladie coronarienne).
- Établir un plan de surveillance osseuse, hépatique et cardiovasculaire.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

