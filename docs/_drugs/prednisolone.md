---
layout: default
title: Prednisolone
parent: Prédiction du modèle uniquement (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
---

# Prednisolone
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

# Prednisolone : Vers la Pelade (Alopecia Areata)

## Résumé en Une Phrase

Prednisolone est un corticoïde systémique commercialisé en France (5 AMM), mais l'indication d'origine n'est pas renseignée dans les données reçues.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pelade (alopecia areata)**.
Cette piste s'appuie sur **3 essais cliniques pertinents** (sur 18 récupérés, dont la plupart concernent le lupus) et sur **20 publications**, dont un ECR contrôlé versus placebo, une revue systématique et une méta-analyse en réseau Cochrane.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Pelade (alopecia areata) |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L3 (voir la note ci-dessous) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 5 |
| Décision Recommandée | Proceed with Guardrails |

**Note sur le niveau de preuve :** le dossier source attribue L2. Cependant, la phase de l'unique ECR prednisolone contre placebo (PMID 15692475) n'est pas précisée et son effectif est faible. Le critère L2 (1 ECR de Phase 2/3 complet) n'est donc pas vérifié. Les revues systématiques disponibles correspondent au niveau L3, qui est retenu ici. Le critère L1 (≥2 ECR de Phase 3) n'est pas atteint.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des connaissances générales, la prednisolone est un glucocorticoïde. Cette classe inhibe la transcription de cytokines pro-inflammatoires et freine l'activité des lymphocytes T.

La pelade est une maladie auto-immune médiée par les lymphocytes T, qui s'attaquent au follicule pileux après perte de son privilège immunitaire. L'action immunosuppressive des corticoïdes correspond donc à cette physiopathologie. Une étude mécanistique (PMID 30294905) suggère aussi que les corticoïdes oraux en pulse agiraient en modifiant les taux de TNF-α.

Cette piste est cependant limitée sur deux points :
- La rechute à l'arrêt du traitement est fréquente, et la toxicité cumulée des corticoïdes restreint l'usage prolongé.
- Les inhibiteurs de JAK disposent désormais de données de Phase 3 et constituent l'alternative de référence.

## Preuves d'Essais Cliniques

Trois essais sont réellement liés à la pelade. Les 15 autres, qui portent principalement sur le lupus érythémateux systémique, la néphropathie, la migraine ou le cancer de la prostate, ne sont pas pertinents et ne sont pas listés.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Terminé | 42 | Méthylprednisolone orale en méga-pulse dans la pelade sévère résistante. Corticoïde proche, mais pas la prednisolone elle-même. Résultats non détaillés dans le résumé. |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | Non applicable (observationnelle) | Terminé | 296 | Sécurité et efficacité du tofacitinib dans l'alopécie, avec ou sans prednisolone en appoint. Le médicament évalué est le tofacitinib. |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | Non applicable | Inconnu | 20 | Comparaison d'un injecteur sans aiguille (DERMOJET) et d'une seringue classique pour l'injection intralésionnelle de stéroïdes dans la pelade. Il s'agit d'une étude sur le mode d'administration. |

Aucun essai contrôlé de Phase 2/3 évaluant directement la prednisolone dans la pelade n'est enregistré dans ces données.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | ECR | J Am Acad Dermatol | Prednisolone orale en pulse contre placebo dans la pelade. Il s'agit du seul ECR ciblant la molécule, de petite taille. Le résumé disponible ne donne pas les résultats. |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Méta-analyse en réseau | Cochrane Database Syst Rev | Compare les traitements de la pelade (immunosuppresseurs, stimulants de la pousse, immunothérapie de contact). Les résultats chiffrés ne figurent pas dans l'extrait. |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | Revue systématique | Australas J Dermatol | Évalue les preuves des traitements systémiques de la pelade, de la pelade totale et de la pelade universelle. |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Revue | Dermatol Pract Concept | Efficacité, taux de rechute, effets indésirables et facteurs pronostiques des pulses de corticoïdes. Les résultats des pulses sont variables. |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Revue de la littérature | Pediatr Dermatol | Schémas posologiques et effets indésirables des pulses de corticoïdes chez l'enfant. Ces schémas ne sont pas bien établis. |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | Cohorte | J Dtsch Dermatol Ges | Pelade sévère de l'enfant. Les corticoïdes à haute dose donnent les réponses les plus rapides, mais la rechute est inévitable à l'arrêt. Étude d'un relais à dose plus faible. |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | Étude clinique (type non classé) | Dermato-endocrinology | Prednisolone en pulse à dose moyenne. Elle semble efficace aux stades précoces, mais des effets indésirables importants peuvent conduire à l'arrêt. |
| [30294905](https://pubmed.ncbi.nlm.nih.gov/30294905/) | 2019 | Étude mécanistique | J Cosmet Dermatol | Modification du TNF-α sérique et tissulaire comme mécanisme possible des pulses oraux de corticoïdes. |
| [32779249](https://pubmed.ncbi.nlm.nih.gov/32779249/) | 2020 | Étude rétrospective | J Eur Acad Dermatol Venereol | 138 patients atteints de pelade chronique. Taux de poursuite de l'azathioprine, du méthotrexate et de la ciclosporine comme agents d'épargne cortisonique. |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Cas clinique et revue ciblée | J Dermatol Treat | Rémission durable d'une pelade sévère sous mini-pulse de dexaméthasone lorsque les inhibiteurs de JAK ne sont pas utilisables. |

## Informations de Marché en France

Les textes d'indication approuvée ne sont pas renseignés pour ces 5 AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 62743861 | PREDNISOLONE ZENTIVA 20 mg | Comprimé effervescent sécable |
| 69864424 | PREDNISOLONE SANDOZ 20 mg | Comprimé effervescent sécable |
| 67537107 | PREDNISOLONE VIATRIS 20 mg | Comprimé effervescent sécable |
| 65569519 | DELIPROCT | Suppositoire |
| 69345098 | DERINOX | Solution pour pulvérisation nasale |

Seule la forme orale (comprimé de 20 mg) est compatible avec un usage systémique en pulse dans la pelade.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- La physiopathologie auto-immune de la pelade est cohérente avec l'action des glucocorticoïdes. Un ECR contrôlé versus placebo, des revues systématiques et une méta-analyse Cochrane existent, et la forme orale est commercialisée en France.
- Aucune preuve de Phase 3 ne porte sur la prednisolone elle-même, et la rechute à l'arrêt ainsi que la toxicité cumulée des corticoïdes limitent son usage face aux inhibiteurs de JAK.

**Pour avancer, les éléments suivants sont nécessaires :**
- Intégrer la notice ANSM (mises en garde, contre-indications), ce qui bloque actuellement l'évaluation de sécurité.
- Compléter les données sur le mécanisme d'action depuis DrugBank.
- Vérifier la phase, l'effectif et les résultats de l'ECR de 2005 (PMID 15692475), ainsi que l'indication d'origine, absente des données.
- Définir un cadre de sécurité : durée maximale, schéma dégressif, suivi métabolique, osseux et de la croissance chez l'enfant.
- À noter : parmi les autres prédictions du dossier, le syndrome néphrotique idiopathique corticosensible (rang 10) présente des preuves plus solides (L1), mais il relève déjà du standard de soins.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute utilisation.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

