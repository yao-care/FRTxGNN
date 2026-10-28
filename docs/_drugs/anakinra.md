---
layout: default
title: Anakinra
parent: Prédiction du modèle uniquement (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Anakinra : nouvelle indication prédite, Mastocytome extracutané (niveau de preuve L3). Indication d'origine : Polyarthrite rhumatoïde…"
monitor_inn: "ANAKINRA"
predicted_indications: ["extracutaneous mastocytoma", "hepatic infarction", "autosomal recessive familial Mediterranean fever", "aggressive systemic mastocytosis", "hepatic veno-occlusive disease", "peliosis hepatis", "oligoarticular juvenile idiopathic arthritis with anti-nuclear antibodies", "oligoarticular juvenile idiopathic arthritis without anti-nuclear antibodies", "pyogenic autoinflammatory syndrome", "unclassified autoinflammatory syndrome"]
---

# Anakinra
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Anakinra : De la polyarthrite rhumatoïde au mastocytome extracutané
{: .text-alpha }

## Résumé en Une Phrase

Anakinra est un antagoniste du récepteur de l'interleukine-1, initialement utilisé dans la polyarthrite rhumatoïde et les syndromes périodiques associés à la cryopyrine (dont le syndrome CINCA).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **fièvre méditerranéenne familiale autosomique récessive**,
avec **0 essai clinique** enregistré et **20 publications** associées (principalement des revues, séries et cas cliniques) dans les données compilées pour ce rapport.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde, syndromes périodiques associés à la cryopyrine (CAPS), syndrome CINCA |
| Nouvelle Indication Prédite | Fièvre méditerranéenne familiale autosomique récessive |
| Score de Prédiction TxGNN | 0,9993 (indication de rang 1 : mastocytome extracutané, 0,9993 ; fièvre méditerranéenne familiale retenue ici car mieux documentée, 0,9989) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Proceed with Guardrails |

> Note : le score affiché ci-dessus pour la fièvre méditerranéenne familiale est de **0,9989** ; la mention entre parenthèses précise que le candidat classé premier par TxGNN (mastocytome extracutané, 0,9993) ne dispose d'aucune preuve et n'a donc pas été retenu.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, anakinra est une forme recombinante de l'antagoniste du récepteur de l'IL-1 : il bloque la fixation de l'IL-1 (α et β) sur son récepteur. Son efficacité dans la polyarthrite rhumatoïde et les syndromes liés à la cryopyrine (CAPS) repose sur ce blocage.

La fièvre méditerranéenne familiale (FMF) est causée par des mutations du gène MEFV (pyrine), qui entraînent une activation excessive de l'inflammasome et une surproduction d'IL-1β. Elle appartient à la même famille de maladies auto-inflammatoires que les CAPS : la voie physiopathologique ciblée est donc la même que pour l'indication déjà reconnue.

La littérature fournie soutient l'inhibition de l'IL-1 comme classe thérapeutique dans la FMF, notamment chez les patients résistants ou intolérants à la colchicine. Aucun essai randomisé d'anakinra dans cette maladie n'apparaît toutefois dans les données.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucun essai randomisé n'est disponible. Les publications les plus pertinentes (études sur l'IL-1 et l'anakinra, puis revues) sont listées ci-dessous.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [21277619](https://pubmed.ncbi.nlm.nih.gov/21277619/) | 2011 | Série de cas / Revue | Semin Arthritis Rheum | Évaluation des traitements ciblant l'IL-1 dans la FMF ; la pyrine intervient dans la maturation de l'IL-1, ce qui justifie cette approche |
| [34550430](https://pubmed.ncbi.nlm.nih.gov/34550430/) | 2022 | Cohorte | Rheumatol Int | Canakinumab (anti-IL-1β) efficace dans la FMF résistante ou intolérante à la colchicine et/ou à l'anakinra |
| [19033248](https://pubmed.ncbi.nlm.nih.gov/19033248/) | 2009 | Cas clinique | Nephrol Dial Transplant | Traitement réussi par anakinra d'une FMF et évolution après transplantation rénale |
| [21931121](https://pubmed.ncbi.nlm.nih.gov/21931121/) | 2012 | Cas cliniques | Nephrol Dial Transplant | Effet bénéfique marqué des inhibiteurs de l'IL-1 en cas de FMF compliquée d'amylose et d'insuffisance rénale |
| [20386914](https://pubmed.ncbi.nlm.nih.gov/20386914/) | 2012 | Cas clinique | Rheumatol Int | Efficacité de l'anakinra chez un patient atteint de FMF résistante à la colchicine, avec amylose secondaire |
| [23928237](https://pubmed.ncbi.nlm.nih.gov/23928237/) | 2013 | Cas clinique | Joint Bone Spine | Myosite chez un patient avec FMF et spondyloarthrite traitée avec succès par anakinra |
| [28585601](https://pubmed.ncbi.nlm.nih.gov/28585601/) | 2017 | Cas cliniques | JPMA | Anakinra et canakinumab chez quatre patients résistants à la colchicine, traités avec succès |
| [32655029](https://pubmed.ncbi.nlm.nih.gov/32655029/) | 2020 | Cas clinique | Iran J Kidney Dis | Rejet cellulaire aigu tardif après anakinra chez un transplanté rénal avec FMF (lien causal incertain) |
| [23322405](https://pubmed.ncbi.nlm.nih.gov/23322405/) | 2013 | Revue | Clin Rev Allergy Immunol | Revue du traitement biologique anti-IL-1β de la FMF |
| [26572612](https://pubmed.ncbi.nlm.nih.gov/26572612/) | 2016 | Revue | Curr Med Chem | Colchicine, agents biologiques et autres options thérapeutiques dans la FMF |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60663231 | KINERET 100 mg/0,67 mL, solution injectable en seringue préremplie (statut : active) | Solution injectable | Non renseignée |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions sont recensées dans les données compilées. Les principales :
  - **Majeure** : défériprone.
  - **Modérée** : corticoïdes (hydrocortisone, bétaméthasone, budésonide, dexaméthasone, prednisolone, prednisone, triamcinolone), simvastatine, anticoagulants (apixaban, dicoumarol, rivaroxaban), produits radiopharmaceutiques ou apparentés (ibritumomab tiuxétan, iobenguane I-131, tositumomab).
  - **Mineure** : sels de zinc (acétate, gluconate, sulfate).

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le mécanisme (blocage de l'IL-1) est cohérent avec la physiopathologie de la FMF et identique à celui de l'indication CAPS ; la littérature (cas cliniques, séries, revues) est concordante, mais elle ne comporte ni essai randomisé ni essai enregistré (niveau L3).
- Les autres prédictions (mastocytome extracutané, infarctus hépatique, maladie veino-occlusive hépatique, péliose hépatique) n'ont aucune preuve (L5) ; la mastocytose systémique agressive repose sur des cas de syndrome de Schnitzler hors sujet. Les formes de PAPA/PSTPIP1 (L3) et le syndrome auto-inflammatoire non classé (L3) sont des pistes de recherche secondaires.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications), actuellement indisponible, ce qui bloque l'évaluation de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Clarifier le statut réglementaire : la seule AMM française est annulée, sans indication renseignée.
- Rechercher ou mettre en place un essai contrôlé d'anakinra dans la FMF résistante à la colchicine, et analyser les revues systématiques existantes.
- Définir un plan de surveillance pour les populations à risque (insuffisance rénale, transplantés, patients sous corticoïdes ou anticoagulants).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

