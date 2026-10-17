---
layout: default
title: Dihydrocodeine
parent: Prédiction du modèle uniquement (L5)
nav_order: 243
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Dihydrocodeine : nouvelle indication prédite, Maladie de la cavité nasale (niveau de preuve L5). Indication d'origine : Rhinite allergique, rhinite vasomotrice, pharyngite, rhume, rhinite…"
monitor_inn: "dihydrocodeine"
predicted_indications: ["acute laryngopharyngitis", "allergic urticaria", "papillary conjunctivitis", "faucial diphtheria", "cervical disc degenerative disorder", "headache disorder", "cold urticaria", "trigeminal autonomic cephalalgia"]
---

# Dihydrocodeine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Dihydrocodéine : De la rhinite allergique à la maladie de la cavité nasale

## Résumé en Une Phrase

La dihydrocodéine est un opioïde utilisé comme antalgique et antitussif, associé dans les données compilées à des indications touchant les voies respiratoires supérieures (rhinite allergique, rhinite vasomotrice, pharyngite, rhume, nasopharyngite).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie de la cavité nasale**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.
Cette prédiction repose uniquement sur le calcul du modèle (niveau de preuve L5).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Rhinite allergique, rhinite vasomotrice, pharyngite, rhume, rhinite, nasopharyngite (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Maladie de la cavité nasale |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la dihydrocodéine est un opioïde à visée antalgique et antitussive. Les indications d'origine (rhinite, nasopharyngite, rhume) concernent des affections des voies respiratoires supérieures, et la maladie de la cavité nasale appartient à la même région anatomique.

Le lien est toutefois **faible et indirect**. Aucune donnée mécanistique ne permet d'expliquer en quoi un opioïde agirait sur une pathologie nasale. Le score élevé du modèle (99,99 %) correspond vraisemblablement à la proximité avec les indications existantes, plutôt qu'à un véritable signal de repositionnement.

Les autres prédictions du modèle sont du même ordre : laryngopharyngite aiguë (99,99 %, probablement un chevauchement avec les indications existantes), urticaire allergique, conjonctivite papillaire, diphtérie fauciale, discopathie cervicale dégénérative, céphalées (seule piste avec deux publications indirectes), urticaire au froid et céphalalgie trigémino-autonomique. Aucune ne dispose d'essai clinique. Pour les urticaires, la libération d'histamine induite par les opioïdes pourrait même aggraver la maladie.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la maladie de la cavité nasale.

À titre indicatif, deux publications indirectes ont été identifiées pour une autre indication prédite (céphalées) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [28521551](https://pubmed.ncbi.nlm.nih.gov/28521551/) | 2017 | Revue | Journal of Pain & Palliative Care Pharmacotherapy | Synthèse des revues Cochrane publiées de janvier à mars 2017 ; aucune donnée spécifique à la dihydrocodéine confirmée |
| [11915306](https://pubmed.ncbi.nlm.nih.gov/11915306/) | 2002 | Étude clinique / cas d'abus | Nihon Arukoru Yakubutsu Igakkai Zasshi | Trois cas d'abus d'un sirop antitussif ; signal de mésusage et de dépendance, et non preuve d'efficacité |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67482372 | DICODIN L.P. 60 mg, comprimé à libération prolongée | Comprimé à libération prolongée | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

Les données issues de la notice (mises en garde, contre-indications) ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité.

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, insuffisance hépatique, épilepsie, insomnie, bronchopneumopathie chronique obstructive, maladie rénale, pancréatite, maladie de la vésicule biliaire, thrombopénie, hypothyroïdie, ulcère gastroduodénal, maladie inflammatoire de l'intestin, diabète et acidocétose diabétique, hypertrophie bénigne de la prostate, hypotension, goutte, abus ou dépendance aux substances, hémophilie, maladie coronarienne et infarctus du myocarde, hémoglobinopathie.
- **Interactions médicamenteuses** : 119 interactions recensées. Parmi celles listées :
  - **Majeures** : alvimopan, bupropion.
  - **Modérées** : aprépitant, atropine, attapulgite, cimétidine, clidinium, dexaméthasone, dexfenfluramine, dicyclomine, dolasétron, dronabinol, éluxadoline, fenfluramine, glycopyrronium, granisétron, hyoscyamine, kaolin, lopéramide, mépenzolate.
- **Risque lié à la classe** : les opioïdes comportent un risque de dépendance, de dépression respiratoire et de céphalées par abus médicamenteux. Le signal d'abus relevé dans la littérature va dans le même sens.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication directe, avec un lien mécanistique faible. De plus, la seule AMM française est annulée et les données de sécurité de la notice sont absentes, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) pour le criblage de sécurité.
- Obtenir les données sur le mécanisme d'action (par exemple via DrugBank).
- Mener une recherche bibliographique ciblée sur la dihydrocodéine dans les pathologies nasales.
- Évaluer la compatibilité des voies d'administration (actuellement non évaluée) ainsi que le rapport bénéfice/risque, compte tenu du risque de dépendance et des nombreuses contre-indications.
- Si une piste doit être retenue, la prédiction « céphalées » (L4) est la seule disposant de publications, mais celles-ci sont indirectes et défavorables à un usage des opioïdes.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

