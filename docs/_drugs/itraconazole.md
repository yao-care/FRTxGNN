---
layout: default
title: Itraconazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 161
evidence_level: L5
indication_count: 1
---

# Itraconazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Itraconazole : De l'Antifongique Azolé à la Pneumocystose

## Résumé en Une Phrase

L'itraconazole est un antifongique azolé commercialisé en France (5 AMM), mais les textes d'indication de ces AMM ne sont pas renseignés dans les données disponibles.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **pneumocystose**, avec un score très élevé, mais **aucun essai clinique** n'est enregistré et aucune des **20 publications** identifiées ne démontre directement une efficacité contre *Pneumocystis*.
Cette prédiction est mécanistiquement peu soutenue et doit être considérée avec prudence.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Pneumocystose |
| Score de Prédiction TxGNN | 99,34 % |
| Niveau de Preuve | L5 (prédiction du modèle, sans étude réelle testant l'itraconazole dans la pneumocystose ; le dossier source indiquait L4) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 5 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances pharmacologiques générales, l'itraconazole inhibe la CYP51 fongique (lanostérol 14-alpha-déméthylase) et bloque ainsi la synthèse de l'ergostérol, composant essentiel de la membrane des champignons.

Le lien prédit avec la pneumocystose n'est **pas** soutenu par ce mécanisme. La membrane de *Pneumocystis jirovecii* contient très peu d'ergostérol (le cholestérol y prédomine), et les azolés ne sont pas établis comme efficaces contre ce pathogène. Le traitement de référence reste le triméthoprime-sulfaméthoxazole.

La prédiction du graphe reflète probablement l'association fréquente de l'itraconazole avec les infections fongiques opportunistes chez les patients immunodéprimés (VIH, greffe, granulomatose septique chronique), plutôt qu'une activité réelle contre *Pneumocystis*. L'indication d'origine et le MOA n'étant pas renseignés, la prédiction ne peut pas être recoupée avec eux.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Les 20 publications identifiées portent surtout sur les infections opportunistes en général, et non sur l'itraconazole dans la pneumocystose. Voici les 10 plus pertinentes, par ordre de priorité de type d'étude.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | ECR (phase III, double aveugle) | HIV Medicine | Prophylaxie par itraconazole des infections fongiques profondes chez des patients VIH immunodéprimés ; l'extrait disponible ne mentionne pas de résultat sur la pneumocystose |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohorte rétrospective | Transplantation Proceedings | Infections fongiques invasives après greffe rénale, associées à une mortalité et à une dysfonction du greffon accrues |
| [17594870](https://pubmed.ncbi.nlm.nih.gov/17594870/) | 2007 | Cohorte rétrospective | Allergologia et Immunopathologia | Granulomatose septique chronique pédiatrique sur 25 ans ; itraconazole utilisé en prophylaxie antifongique |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Observationnelle | Indian J Med Microbiol | Profil des pathogènes fongiques respiratoires chez les hôtes immunocompétents et immunodéprimés, selon le taux de CD4 |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Rapport de cas | Frontiers in Immunology | Co-infection *Talaromyces marneffei* et *P. jirovecii* chez un enfant avec mutation STAT1 ; l'itraconazole a probablement traité *Talaromyces*, pas *Pneumocystis* |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Revue | BMJ Clinical Evidence | Prophylaxie primaire et secondaire des infections opportunistes chez les patients VIH |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Revue (pharmacocinétique) | Clinical Pharmacokinetics | Pénétration des anti-infectieux, dont les antifongiques, dans le liquide épithélial pulmonaire |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Revue | Drugs | Traitement et prophylaxie des infections systémiques à protozoaires, dont *Pneumocystis carinii* |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Revue | Current Clinical Topics in Infectious Diseases | Prophylaxie et traitement des infections chez les receveurs de greffe de moelle osseuse |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Revue | Seminars in Respiratory Infections | Infections après greffe pulmonaire |

---

## Informations de Marché en France

Les textes d'indication approuvée ne sont pas renseignés pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 60738303 | ITRACONAZOLE VIATRIS 100 mg, gélule | Gélule | VIATRIS SANTE |
| 69662344 | ITRACONAZOLE TEVA 100 mg, gélule | Gélule | TEVA SANTE |
| 69998156 | SPORANOX 10 mg/mL, solution buvable | Solution buvable | JANSSEN CILAG |
| 62469613 | SPORANOX 100 mg, gélule | Gélule | JANSSEN CILAG |
| 66188581 | ITRACONAZOLE SANDOZ 100 mg, gélule | Gélule | SANDOZ |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé (99,34 %), mais il n'existe ni essai clinique ni étude démontrant une efficacité de l'itraconazole contre *Pneumocystis*, et le mécanisme (faible teneur en ergostérol du pathogène) va à l'encontre de la prédiction.
- Les informations de sécurité de la notice ANSM sont absentes, ce qui bloque toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications, interactions médicamenteuses), point bloquant
- Obtenir les données de mécanisme d'action (DrugBank) et les indications approuvées des AMM
- Rechercher des données précliniques ou cliniques spécifiques à l'itraconazole dans la pneumocystose
- Comparer avec le traitement de référence (triméthoprime-sulfaméthoxazole) avant tout autre investissement

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

