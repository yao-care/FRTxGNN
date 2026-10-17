---
layout: default
title: Dipyridamole
parent: Preuves modérées (L3-L4)
nav_order: 249
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Dipyridamole : nouvelle indication prédite, Prinzmetal angina (angine de Prinzmetal) (niveau de preuve L4). Indication d'origine : Fibrillation atriale"
monitor_inn: "DIPYRIDAMOLE"
predicted_indications: ["stroke disorder", "thrombotic disease", "sick sinus syndrome 2, autosomal dominant", "transient ischemic attack (disease)", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "cavernous sinus thrombosis", "lateral sinus thrombosis"]
---

# Dipyridamole
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
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

# Dipyridamole : De la fibrillation atriale à la Prinzmetal angina

## Résumé en Une Phrase

Le dipyridamole est un antiagrégant plaquettaire et vasodilatateur, associé dans les données compilées à la fibrillation atriale comme indication d'origine.
Le modèle TxGNN prédit comme première piste la **angine de Prinzmetal** (score très élevé), mais cette prédiction n'est soutenue par **aucun essai clinique** et par **10 publications** seulement, qui décrivent surtout le dipyridamole comme agent de test diagnostique (et non comme traitement). Une piste mieux documentée, l'**accident vasculaire cérébral (AVC)**, est présentée en complément dans ce rapport.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Fibrillation atriale (selon le graphe de connaissances ; aucun texte d'indication n'est renseigné dans les AMM françaises) |
| Nouvelle Indication Prédite | Prinzmetal angina (angine de Prinzmetal) |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations pharmacologiques connues, le dipyridamole bloque la recapture de l'adénosine et inhibe des phosphodiestérases (PDE), ce qui augmente l'adénosine extracellulaire et les nucléotides cycliques (AMPc/GMPc). Il en résulte une vasodilatation coronaire et une inhibition de l'agrégation plaquettaire.

La relation avec l'angine de Prinzmetal (angor vasospastique) reste toutefois **peu convaincante**. La littérature associe surtout le dipyridamole à cette maladie comme agent de **stress diagnostique**. Une étude de 1988 rapporte même que l'arrêt du test au dipyridamole par l'aminophylline peut déclencher un vasospasme coronaire chez des patients atteints d'angor variant. Cela suggère un potentiel de **nuisance** plutôt qu'un bénéfice thérapeutique. Un risque théorique de « vol coronaire » lié à l'adénosine est également évoqué. Aucun mécanisme thérapeutique sur le vasospasme n'est établi.

Cette prédiction à score élevé doit donc être interprétée comme un signal informatique, non comme une hypothèse thérapeutique étayée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour l'angine de Prinzmetal.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Revue / pharmacologie clinique | Japanese Circulation Journal | Effet de plusieurs médicaments (propranolol, diltiazem, dipyridamole, atropine, phénoxybenzamine) sur les crises d'angor de repos, dont 13 patients avec angor de Prinzmetal ; le propranolol était inefficace voire aggravant |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Série de cas | American Journal of Cardiology | L'arrêt du test au dipyridamole par l'aminophylline peut déclencher un vasospasme coronaire dans l'angor variant |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Cohorte | British Heart Journal | Reproductibilité du test d'effort chez des patients avec sus-décalage du segment ST et réponses variables au test au dipyridamole |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | Cohorte | Zhonghua Xin Xue Guan Bing Za Zhi | Caractéristiques cliniques du spasme coronaire atypique comparé au spasme typique |
| [14060538](https://pubmed.ncbi.nlm.nih.gov/14060538/) | 1963 | Rapport de cas | Naika | Cas d'une forme variante d'angine de poitrine |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | Non classé | Japanese Circulation Journal | Scintigraphie au thallium-201 avec dipyridamole pour la détection de la maladie coronaire (précision diagnostique de 66 %) |
| [2022043](https://pubmed.ncbi.nlm.nih.gov/2022043/) | 1991 | Non classé | Circulation | Bases physiopathologiques de l'évaluation fonctionnelle non invasive des sténoses coronaires |
| [8417062](https://pubmed.ncbi.nlm.nih.gov/8417062/) | 1993 | Non classé | J Am Coll Cardiol | Augmentation de l'échodensité du myocarde transitoirement asynergique comme signe d'ischémie |
| [7628141](https://pubmed.ncbi.nlm.nih.gov/7628141/) | 1995 | Non classé | Clinical Nuclear Medicine | Discussion d'un cas de « migraine cardiaque » chez un patient avec angor variant |
| [8634169](https://pubmed.ncbi.nlm.nih.gov/8634169/) | 1996 | Non classé | Revista Portuguesa de Cardiologia | Pronostic à 3 ans après scintigraphie thallium-dipyridamole normale |

Aucune de ces publications n'est un essai randomisé démontrant un bénéfice thérapeutique du dipyridamole dans l'angine de Prinzmetal.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60021216 | PERSANTINE 75 mg, comprimé enrobé | Comprimé enrobé | Non renseignée (AMM annulée) |
| 68572748 | PERSANTINE 10 mg/2 mL, solution injectable, ampoule | Solution injectable | Non renseignée (AMM annulée) |

Les deux AMM, détenues par Glenwood GmbH Pharmazeutische Erzeugnisse, sont annulées : aucune présentation n'est actuellement autorisée en France selon les données compilées.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : insuffisance rénale, maladie hépatique, maladie de la vésicule biliaire, thrombopénie, ulcère gastroduodénal (dont actif), gastrite, hypotension, goutte, infarctus du myocarde, syndrome coronarien aigu, hémophilie, anémie, purpura thrombopénique, déficit congénital en prothrombine, maladie hémorragique par déficit en vitamine K, syndrome de Reye, maladie d'Alzheimer, maladie de Pick, polypes nasaux, troubles du métabolisme du phosphore ou du calcium, déficit en potassium, abus de substances, hémoglobinopathies.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les principales, de niveau **modéré** : dexfenfluramine, sibutramine, fenfluramine. D'autres interactions, de niveau non précisé, concernent notamment l'acide acétylsalicylique, la cimétidine, la metformine, le glimépiride, la morphine, la simvastatine, la prednisone, l'oméprazole, le pantoprazole, le lansoprazole et la vancomycine.

Veuillez consulter la notice pour les mises en garde officielles, qui n'ont pas pu être obtenues.

---

## Conclusion et Prochaines Étapes

**Décision : Hold** (pour l'angine de Prinzmetal)

**Justification :**
- La prédiction repose sur un score informatique élevé, mais les preuves réelles sont de niveau L4 : aucun essai, et une littérature qui décrit surtout un usage diagnostique, avec un signal possible de nuisance (vasospasme).
- Les AMM françaises sont toutes annulées, ce qui limite la disponibilité.

**Piste complémentaire (hors indication première) :** pour l'**AVC** et l'**accident ischémique transitoire**, les données compilées montrent un niveau de preuve L1 (décision « Proceed with Guardrails »), avec l'essai ESPRIT (4 500 patients, aspirine avec ou sans dipyridamole), plusieurs méta-analyses et revues Cochrane. Il s'agit toutefois surtout de la confirmation d'un usage établi (association aspirine + dipyridamole à libération prolongée) plutôt que d'un véritable repositionnement. Les points de vigilance sont les céphalées, l'hypotension, le risque hémorragique avec d'autres antithrombotiques et la charge d'interactions. La « maladie thrombotique » (L3) reste une question de recherche, car la catégorie est trop large et une partie de la littérature est hors sujet. Les autres prédictions (L5) n'ont aucun support.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles (notice ANSM), manquantes et bloquantes pour toute évaluation de sécurité
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Pour l'angine de Prinzmetal : des études cliniques de pharmacologie montrant un bénéfice thérapeutique et une évaluation du risque de vasospasme
- La clarification du statut réglementaire et de la disponibilité des formulations en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

