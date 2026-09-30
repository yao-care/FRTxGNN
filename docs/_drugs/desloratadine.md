---
layout: default
title: Desloratadine
parent: Prédiction du modèle uniquement (L5)
nav_order: 102
evidence_level: L5
indication_count: 6
---

# Desloratadine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Desloratadine : D'un antihistaminique H1 à l'urticaire au froid

## Résumé en une phrase

La desloratadine est un antihistaminique H1 de deuxième génération, commercialisé en France (AERIUS et génériques). Les textes d'indication des AMM ne figurent pas dans les données fournies.
Le modèle TxGNN prédit qu'elle pourrait être efficace dans l'**urticaire au froid**, avec **3 essais cliniques** et **7 publications** qui soutiennent actuellement cette direction, dont 2 ECR publiés.

---

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Nouvelle indication prédite | Urticaire au froid (cold urticaria) |
| Score de prédiction TxGNN | 99,94 % |
| Niveau de preuve | L1 (selon l'Evidence Pack : plusieurs essais randomisés de Phase 4 et 2 ECR publiés. Aucun essai de Phase 3 n'est fourni) |
| Statut de marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision recommandée | Proceed with Guardrails |

---

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances pharmacologiques établies, la desloratadine est un agoniste inverse des récepteurs H1, à sélectivité périphérique. Son efficacité dans les affections histaminiques est bien connue.

Dans l'urticaire au froid, les papules résultent de la libération d'histamine par les mastocytes. Le blocage des récepteurs H1 cible donc directement la voie effectrice de la maladie. Les recommandations approuvent l'augmentation de la dose jusqu'à 4 fois la dose standard pour les urticaires physiques.

Le lien mécanistique est donc cohérent. Les essais randomisés testent d'ailleurs le médicament directement dans cette maladie, à 5 mg (dose standard), 10 mg et 20 mg. Les doses supérieures à la dose de l'AMM nécessitent un suivi médical.

---

## Preuves d'essais cliniques

| Numéro d'essai | Phase | Statut | Inscription | Résultats principaux |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Terminé | 30 | Étude multicentrique, en double aveugle, à doses croissantes (5, 10 et 20 mg) dans l'urticaire au froid acquise. Objectif : déterminer la dose qui inhibe les symptômes. |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Terminé | 33 | Étude croisée randomisée, en double aveugle, contre placebo. Compare 5 mg et 20 mg sur les lésions d'urticaire au froid (thermographie, volumétrie, photographie). |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Terminé | 150 | Comparaison de l'effet inhibiteur de 5 antihistaminiques dans l'urticaire. Non limitée à l'urticaire au froid : résultats par sous-type à vérifier. |

---

## Preuves de la littérature

| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | ECR | J Allergy Clin Immunol | Étude croisée randomisée contre placebo : la desloratadine à forte dose réduit le volume des papules et améliore les seuils de provocation au froid par rapport à la dose standard. |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | ECR | Br J Dermatol | Mesure du seuil critique de température dans l'urticaire au froid, avec augmentation de la dose d'antihistaminique H1. |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | Étude clinique | J Dermatol Treat | Desloratadine 5 mg pendant 4 jours, test au glaçon avant et après traitement chez 12 patients atteints d'urticaire au froid. |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Revue | Drugs | Étiologie, prise en charge et options thérapeutiques de l'urticaire chronique. |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Revue | Allergy | Ébastine dans la rhinite allergique et l'urticaire chronique idiopathique (indirect, autre molécule). |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Rapport de cas | Qatar Med J | Urticaire au froid après anaphylaxie due à une piqûre de fourmi noire. |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Rapport de cas | J Allergy Clin Immunol Pract | Urticaire au froid dépendante de l'alimentation, nouvelle variante d'urticaire physique. |

---

## Informations de marché en France

Les textes d'indication approuvée ne sont pas renseignés dans les données. Formes disponibles : comprimé pelliculé et solution buvable.

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 63929363 | DESLORATADINE SANDOZ 5 mg | Comprimé pelliculé | SANDOZ |
| 65723604 | DESLORATADINE ZENTIVA 5 mg | Comprimé pelliculé | ZENTIVA FRANCE |
| 63820969 | DESLORATADINE KRKA 5 mg | Comprimé pelliculé | KRKA (Slovénie) |
| 61223605 | DESLORATADINE BIOGARAN 5 mg | Comprimé pelliculé | BIOGARAN |
| 61833327 | AERIUS 5 mg | Comprimé pelliculé | ORGANON (Hollande) |

---

## Considérations de sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et prochaines étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais randomisés de Phase 4 (augmentation de dose, croisé contre placebo) et 2 ECR publiés testent directement la desloratadine dans l'urticaire au froid, avec un mécanisme H1 cohérent. Aucun essai de Phase 3 n'est disponible, et l'utilisation à des doses supérieures à celles de l'AMM exige une supervision clinique.
- Les autres prédictions sont nettement plus faibles : la « maladie de la cavité nasale » est au niveau L3 (Research Question), et les quatre autres sont au niveau L5 (Hold, prédiction du modèle uniquement).

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications). Ce point est bloquant pour le criblage de sécurité.
- Vérifier le statut d'indication autorisée localement, car les indications d'origine sont absentes des données.
- Compléter les données sur le mécanisme d'action (DrugBank).
- Vérifier dans les fiches complètes le comparateur et la population de NCT00600847, ainsi que les résultats par sous-type de NCT01940393.
- Définir un protocole de suivi clinique pour toute augmentation de dose au-delà de l'AMM.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

