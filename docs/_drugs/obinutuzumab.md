---
layout: default
title: Obinutuzumab
parent: Preuves élevées (L1-L2)
nav_order: 219
evidence_level: L1
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **3** 
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

# Obinutuzumab : Du Ciblage Anti-CD20 au Lymphome Folliculaire

## Résumé en Une Phrase

L'obinutuzumab est un anticorps monoclonal anti-CD20 glycoingénieré de type II. Les données fournies ne renseignent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace dans le **lymphome folliculaire**,
avec **50 essais cliniques** et **20 publications** soutenant actuellement cette direction, dont deux essais de Phase 3 terminés.

> **Note de périmètre :** les deux prédictions les mieux classées portent sur des sous-types de leucémie lymphoïde chronique/lymphome lymphocytique (LLC/LL). Elles n'ont aucun essai ni publication dans les données fournies (niveau L5, décision Hold). Ce rapport se concentre sur le lymphome folliculaire (rang 3), seule prédiction disposant de preuves cliniques.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Lymphome folliculaire (rang 3 des prédictions) |
| Score de Prédiction TxGNN | 99,18 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les informations connues, l'obinutuzumab est un anticorps anti-CD20 de type II, glycoingénieré pour renforcer la cytotoxicité cellulaire dépendante des anticorps (ADCC) et l'induction directe de la mort cellulaire.

Les cellules B du lymphome folliculaire expriment le CD20, cible de l'obinutuzumab. Le lien mécanistique est donc plausible. L'obinutuzumab est étudié avec une chimiothérapie, ou comme partenaire d'agents ciblés : polatuzumab vedotin, vénétoclax, lénalidomide, zanubrutinib, glofitamab.

Comme l'indication d'origine n'est pas renseignée, la proximité avec l'indication initiale n'a pas pu être évaluée. Le niveau L1 repose sur les essais de Phase 3 ci-dessous, et non sur la seule prédiction du modèle.

## Preuves d'Essais Cliniques

Les 10 essais les plus pertinents sur 50 sont listés ci-dessous.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01332968](https://clinicaltrials.gov/study/NCT01332968) | Phase 3 | Terminé | 1401 | Chimiothérapie + obinutuzumab vs chimiothérapie + rituximab, suivie d'un traitement d'entretien, chez des patients atteints de lymphome non hodgkinien indolent avancé non traité (étude pivot) |
| [NCT01059630](https://clinicaltrials.gov/study/NCT01059630) | Phase 3 | Terminé | 413 | Bendamustine seule vs bendamustine + obinutuzumab, puis entretien, dans le LNH indolent réfractaire au rituximab |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Phase 2 | Terminé | 217 | Zanubrutinib + obinutuzumab vs obinutuzumab seul dans le lymphome folliculaire en rechute ou réfractaire |
| [NCT05058404](https://clinicaltrials.gov/study/NCT05058404) | Phase 3 | Actif, non en recrutement | 605 | Chimiothérapie raccourcie vs standard associée à l'immunothérapie dans le lymphome folliculaire à forte masse tumorale |
| [NCT05045664](https://clinicaltrials.gov/study/NCT05045664) | Phase 3 | En recrutement | 100 | Radiothérapie associée à un anticorps anti-CD20 dans le lymphome folliculaire de stade précoce |
| [NCT02611323](https://clinicaltrials.gov/study/NCT02611323) | Phase 1/2 | Terminé | 133 | Obinutuzumab + polatuzumab vedotin + vénétoclax en rechute ou réfractaire |
| [NCT02600897](https://clinicaltrials.gov/study/NCT02600897) | Phase 1/2 | Terminé | 114 | Obinutuzumab + polatuzumab vedotin + lénalidomide en rechute ou réfractaire |
| [NCT03113422](https://clinicaltrials.gov/study/NCT03113422) | Phase 2 | Terminé | 56 | Vénétoclax + obinutuzumab + bendamustine en première ligne, forte masse tumorale (bras unique) |
| [NCT05783596](https://clinicaltrials.gov/study/NCT05783596) | Phase 2 | Actif, non en recrutement | 47 | Glofitamab + obinutuzumab en première ligne (lymphome folliculaire et de la zone marginale) |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Phase 4 | Terminé | 114 | Sécurité de la perfusion courte d'obinutuzumab (90 min) en première ligne |

Plusieurs études de combinaison sont de phase précoce, terminées prématurément ou retirées (par exemple NCT04796922, retiré, 0 patient). Elles ne doivent pas être surinterprétées.

## Preuves de la Littérature

Les 10 publications les plus pertinentes sur 20 sont listées ci-dessous. Les résumés du jeu de données sont tronqués et les tailles d'effet n'ont pas été vérifiées.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | ECR | J Clin Oncol | GALLIUM : l'obinutuzumab prolonge la survie sans progression vs rituximab en première ligne ; analyse de l'influence du schéma de chimiothérapie sur l'efficacité et la sécurité |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | Non classé | HemaSphere | Analyse finale de GALLIUM (Phase 3), obinutuzumab vs rituximab en immunochimiothérapie |
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | Classé « revue » dans les données | N Engl J Med | Comparaison de la chimiothérapie à base de rituximab et à base d'obinutuzumab dans le lymphome folliculaire avancé non traité |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | ECR | J Clin Oncol | ROSEWOOD (Phase 2) : zanubrutinib + obinutuzumab vs obinutuzumab seul en rechute ou réfractaire |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | Phase 2, bras unique | Lancet Haematol | GALEN : obinutuzumab + lénalidomide en rechute ou réfractaire |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Revue rapide | Front Pharmacol | Efficacité, sécurité et coût-efficacité de l'obinutuzumab dans le lymphome folliculaire |
| [37767550](https://pubmed.ncbi.nlm.nih.gov/37767550/) | 2024 | Phase 2 | Haematologica | Polatuzumab vedotin + bendamustine + rituximab ou obinutuzumab (Phase Ib/II) |
| [40355425](https://pubmed.ncbi.nlm.nih.gov/40355425/) | 2025 | Non classé | Blood Cancer J | PrE0403 : vénétoclax intermittent + obinutuzumab + bendamustine en première ligne à haut risque |
| [28324270](https://pubmed.ncbi.nlm.nih.gov/28324270/) | 2017 | Revue | Target Oncol | Revue de l'obinutuzumab dans le lymphome folliculaire réfractaire ou en rechute après rituximab |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Revue | Blood Lymphat Cancer | Impact de l'obinutuzumab seul ou en association dans le lymphome folliculaire |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 61042996 | GAZYVARO 1000 mg, solution à diluer pour perfusion | Solution à diluer pour perfusion | ROCHE REGISTRATION |

Le texte de l'indication approuvée n'est pas fourni dans les données.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée / immunothérapie (anticorps monoclonal anti-CD20), et non cytotoxique conventionnel |
| Risque de Myélosuppression | Des cytopénies sont signalées comme point de surveillance ; détails à consulter dans la notice |
| Éléments de Surveillance | Numération formule sanguine (NFS), réactions à la perfusion, infections, réactivation du VHB |

Pour la classification d'émétogénicité et la protection de manipulation, veuillez consulter les mises en garde et précautions de la notice.

## Considérations de Sécurité

- **Points de surveillance signalés dans l'analyse :** réactions à la perfusion, cytopénies, infections et réactivation du VHB. Une surveillance standard est requise.

Les interactions médicamenteuses n'ont pas été retrouvées dans les données. Veuillez consulter la notice ANSM pour les mises en garde, contre-indications et interactions.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails** (lymphome folliculaire)

**Justification :**
- Deux essais de Phase 3 terminés (NCT01332968 et NCT01059630), dont une publication ECR correspondante (PMID 29856692), soutiennent le niveau L1, avec de nombreux essais de combinaison complémentaires.
- Les deux prédictions de LLC/LL, mieux classées, n'ont aucune preuve clinique dans les données : elles restent en **Hold** (L5). Leurs scores identiques (99,21 %) indiquent des nœuds d'ontologie proches, pas des preuves indépendantes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (RCP) : indications autorisées, mises en garde et contre-indications (lacune bloquante pour le criblage de sécurité)
- Vérification du statut d'autorisation dans le lymphome folliculaire selon l'étiquetage actuel, l'indication d'origine étant vide
- Données sur le mécanisme d'action (DrugBank)
- Vérification des critères principaux et des tailles d'effet dans les publications complètes, les résumés étant tronqués
- Compatibilité de voie d'administration, non évaluée

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

