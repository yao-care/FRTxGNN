---
layout: default
title: Desloratadine
parent: Preuves élevées (L1-L2)
nav_order: 225
evidence_level: L1
indication_count: 6
last_modified_at: 2026-10-14
description: "Desloratadine : nouvelle indication prédite, Urticaire au froid (niveau de preuve L1). Indication d'origine : Rhinite allergique"
monitor_inn: "DESLORATADINE"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic"]
---

# Desloratadine
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **6** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

# Desloratadine : De la rhinite allergique à l'urticaire au froid

## Résumé en Une Phrase

Desloratadine est un antihistaminique H1 de seconde génération, initialement utilisé pour la rhinite allergique, l'urticaire idiopathique et allergique, ainsi que d'autres affections allergiques ou rhinitiques.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**urticaire au froid**,
avec **2 essais cliniques** et **6 publications** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Rhinite allergique (d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Urticaire au froid |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la desloratadine est un antagoniste (agoniste inverse) sélectif des récepteurs H1 périphériques. Son efficacité dans la rhinite allergique et l'urticaire est établie.

L'urticaire au froid est une urticaire physique médiée par l'histamine, due à la dégranulation des mastocytes lors de l'exposition au froid. Le blocage des récepteurs H1 limite la papule et l'érythème, ce qui offre un mécanisme direct et plausible.

Cette indication est très proche des urticaires déjà associées au médicament (idiopathique et allergique) : il s'agit d'une extension au sein d'une même famille de maladies plutôt que d'un repositionnement éloigné. Les recommandations préconisent d'augmenter la dose (jusqu'à 4 fois la dose standard) lorsque la dose habituelle est insuffisante.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Terminé | 30 | Étude multicentrique en double aveugle, avec escalade de dose (5, 10 et 20 mg), visant à déterminer la dose de desloratadine suffisante pour inhiber les symptômes de l'urticaire au froid acquise |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Terminé | 33 | Étude croisée randomisée, en double aveugle, contre placebo, comparant 5 mg et 20 mg sur les lésions d'urticaire au froid induites expérimentalement |

Les deux essais sont de petite taille et classés en Phase 4, et non en Phase 3.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | ECR | J Allergy Clin Immunol | La desloratadine à forte dose réduit le volume des papules et améliore les seuils de provocation au froid par rapport à la dose standard (étude croisée contre placebo) |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | ECR | Br J Dermatol | Mesure du seuil critique de température dans l'urticaire au froid ; essai contrôlé sur l'escalade de dose d'un antihistaminique H1 |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | Étude clinique | J Dermatol Treat | Desloratadine 5 mg pendant 4 jours testée par application de glaçons chez 12 patients atteints d'urticaire au froid |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Revue | Drugs | Étiologie, prise en charge et options thérapeutiques de l'urticaire chronique |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Revue | Allergy | Revue sur l'ébastine dans la rhinite allergique et l'urticaire chronique idiopathique (autre antihistaminique) |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Cas clinique | Qatar Med J | Urticaire au froid apparue après une anaphylaxie due à une morsure de fourmi noire |

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées ; aucune n'est actuellement valide. Le texte de l'indication approuvée n'est pas renseigné. Les 5 premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63929363 | Desloratadine Sandoz 5 mg | Comprimé pelliculé | Non renseignée |
| 65723604 | Desloratadine Zentiva 5 mg | Comprimé pelliculé | Non renseignée |
| 63820969 | Desloratadine Krka 5 mg | Comprimé pelliculé | Non renseignée |
| 61223605 | Desloratadine Biogaran 5 mg | Comprimé pelliculé | Non renseignée |
| 61833327 | Aerius 5 mg | Comprimé pelliculé | Non renseignée |

Les formes disponibles dans l'ensemble des AMM sont le comprimé pelliculé (5 mg) et la solution buvable (0,5 mg/ml).

## Considérations de Sécurité

**Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : hypertension, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, diabète et acidocétose diabétique, hyperplasie bénigne de la prostate, maladie coronarienne et athérosclérose, glaucome à angle fermé, hyperthyroïdie (maladie de Basedow, thyrotoxicose), pyoureter.

**Interactions médicamenteuses** : 100 interactions sont recensées, mais leur niveau de gravité est classé « inconnu ». Parmi les médicaments concernés : calcitriol, phentermine, pantoprazole, doxycycline, clotrimazole, morphine, metformine, oméprazole, rosiglitazone, lansoprazole, cimétidine, vancomycine, lactulose, nizatidine, triamcinolone, prednisone, simvastatine, épinéphrine, hydrocortisone, chlorure de potassium.

Les mises en garde et contre-indications de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité. L'utilisation de doses supérieures à la dose standard (hors AMM) nécessite une attention particulière.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Deux ECR (2009 et 2012) et deux essais de Phase 4 terminés soutiennent l'efficacité de la desloratadine, notamment à forte dose, dans l'urticaire au froid, avec un mécanisme H1 plausible. Les échantillons sont petits, les essais sont de Phase 4, et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde, contre-indications) auprès de l'ANSM, ce qui bloque actuellement l'étape de sécurité
- Compléter les données sur le mécanisme d'action via DrugBank
- Vérifier la disponibilité et la formulation du produit en France, puisque toutes les AMM sont annulées
- Définir un plan de sécurité pour l'escalade de dose (jusqu'à 4 fois la dose standard) et pour les populations à risque (insuffisance rénale ou hépatique, maladies cardiovasculaires)

**Autres indications prédites (preuves insuffisantes, décision : Hold)** : maladie de la cavité nasale (99,87 %), laryngopharyngite aiguë (99,85 %), dermatite atopique récalcitrante (99,75 %), réactivité IgE atopique (99,64 %) et conjonctivite de la rosacée (99,40 %). Elles reposent uniquement sur la prédiction du modèle (L5), sans essai clinique et avec une littérature préclinique non spécifique à la desloratadine, ou sans aucune littérature.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

