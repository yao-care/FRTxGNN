---
layout: default
title: Dexchlorpheniramine
parent: Preuves modérées (L3-L4)
nav_order: 230
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-14
description: "Dexchlorpheniramine : nouvelle indication prédite, Urticaire allergique (niveau de preuve L4). Indication d'origine : Rhinite allergique"
monitor_inn: "dexchlorpheniramine"
predicted_indications: ["allergic urticaria", "cold urticaria"]
---

# Dexchlorpheniramine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **2** 
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

# Dexchlorphéniramine : De la rhinite allergique à l'urticaire allergique

## Résumé en Une Phrase

La dexchlorphéniramine est un antihistaminique H1 de première génération, initialement utilisé pour traiter les rhinites allergiques, les conjonctivites allergiques, l'urticaire et l'angio-œdème.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**urticaire allergique**, mais cette indication recoupe largement ses usages d'origine.
Les données compilées pour ce rapport ne contiennent **aucun essai clinique** et **3 publications**, dont une seule (étude pharmacodynamique) est directement liée au médicament.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Rhinite allergique (les textes d'indication des AMM ne sont pas renseignés ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Urticaire allergique |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées (non commercialisé) |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la dexchlorphéniramine appartient à la classe des antihistaminiques H1 de première génération (antagonistes/agonistes inverses du récepteur H1). Son efficacité dans les affections allergiques est établie, et elle est mécanistiquement applicable à l'urticaire.

L'urticaire allergique est provoquée par la libération d'histamine par les mastocytes, qui agit sur les récepteurs H1 cutanés et produit la papule et l'érythème. Le blocage H1 est donc un mécanisme direct. L'urticaire et l'angio-œdème figurent déjà parmi les indications d'origine du médicament : l'urticaire allergique en est un sous-type. Cette prédiction ne représente donc pas une véritable opportunité de repositionnement, et le score élevé reflète surtout un effet de classe déjà connu.

La seconde prédiction, l'**urticaire au froid** (score 99,61 %), suit la même logique : urticaire physique dans laquelle l'histamine est un médiateur majeur, mais aucune donnée spécifique à la dexchlorphéniramine n'a été fournie (niveau L5).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Essai randomisé de phase I (pharmacodynamique) | Eur J Pharm Sci | Comparaison de l'inhibition de la papule et de l'érythème induits par l'histamine entre la bilastine orale, la dexchlorphéniramine parentérale et une nouvelle formulation parentérale de bilastine ; la dexchlorphéniramine sert de comparateur |
| [29723372](https://pubmed.ncbi.nlm.nih.gov/29723372/) | 2018 | Étude pharmacodynamique (test cutané) | An Bras Dermatol | Suppression de la papule et de l'érythème par les principaux antihistaminiques H1 commercialisés au Brésil |
| [39803](https://pubmed.ncbi.nlm.nih.gov/39803/) | 1979 | Étude clinique et immunologique (cas) | Dermatologica | Cas d'urticaire de contact à la chaleur acquise ; non spécifique à la dexchlorphéniramine, non contrôlé |

Ces publications sont des études pharmacodynamiques ou un cas isolé : elles ne constituent pas des preuves d'efficacité clinique dans l'urticaire allergique.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65570749 | POLARAMINE 2 mg, comprimé sécable (BAYER HEALTHCARE) | Comprimé sécable | Non renseignée (AMM annulée) |
| 65227405 | POLARAMINE 5 mg/1 ml, solution injectable (LABORATORIOS FARMACEUTICOS ROVI) | Solution injectable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : hypertension et troubles hypertensifs, insuffisance hépatique et maladie du foie, épilepsie, ulcère gastrique ou peptique, maladie rénale, pancréatite, maladie de la vésicule biliaire, hypothyroïdie (dont myxœdème et hypothyroïdie congénitale), maladie inflammatoire chronique de l'intestin, diabète et acidocétose diabétique, hypertrophie bénigne de la prostate, hypotension, abus ou dépendance à des substances, maladie coronarienne, infarctus du myocarde, athérosclérose, hémoglobinopathie, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, hypertension oculaire.

Ces éléments doivent être confirmés par la notice officielle. Veuillez consulter la notice pour les mises en garde et les interactions médicamenteuses.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est mécanistiquement plausible mais recoupe les indications d'origine (urticaire, angio-œdème) ; elle n'apporte pas de nouveauté thérapeutique. Aucun essai clinique n'est disponible, les preuves sont de niveau L4 (L5 pour l'urticaire au froid), et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le dépistage de sécurité)
- Les données sur le mécanisme d'action, à partir de DrugBank
- Des études cliniques spécifiques à la dexchlorphéniramine dans l'urticaire (y compris l'urticaire au froid)
- Une clarification de l'intérêt du repositionnement, compte tenu du recoupement avec les indications existantes, et de la disponibilité des voies d'administration, le médicament n'étant plus commercialisé en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

