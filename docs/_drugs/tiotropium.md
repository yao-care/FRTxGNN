---
layout: default
title: Tiotropium
parent: Prédiction du modèle uniquement (L5)
nav_order: 765
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-03
monitor_inn: "TIOTROPIUM"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "hyperlucent lung", "tracheal stenosis"]
description: "Tiotropium : nouvelle indication prédite, Malformation respiratoire (respiratory malformation) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Tiotropium
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

## Tiotropium: Malformation respiratoire (respiratory malformation)
{: .text-alpha }

## Résumé en Une Phrase

Le tiotropium est un bronchodilatateur anticholinergique de longue durée d'action, administré par inhalation.
Le modèle TxGNN prédit qu'il pourrait être utile pour la **malformation respiratoire (respiratory malformation)**.
Les **3 essais cliniques** et **5 publications** compilés pour ce rapport ne portent pas directement sur cette maladie : les essais concernent la mucoviscidose, et la littérature est indirecte.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Malformation respiratoire (respiratory malformation) |
| Score de Prédiction TxGNN | 0.9995 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les informations connues, le tiotropium est un anticholinergique (antagoniste muscarinique) à action prolongée, qui détend la musculature bronchique. Son effet est donc symptomatique, sur le calibre des voies aériennes.

Une malformation respiratoire est un défaut structurel des voies aériennes ou du poumon. Un bronchodilatateur ne corrige pas ce défaut. Il pourrait au mieux soulager une composante de rétrécissement bronchique réversible associée.

Le score TxGNN est très élevé (0,9995), mais il s'agit d'un résultat de calcul. Aucune étude citée ne teste le tiotropium dans la malformation respiratoire elle-même. Le lien mécanistique reste donc une hypothèse non démontrée.

## Preuves d'Essais Cliniques

Les trois essais ci-dessous portent sur des patients atteints de mucoviscidose, et non sur des malformations respiratoires. Leur pertinence pour la prédiction est faible.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01179347](https://clinicaltrials.gov/study/NCT01179347) | Phase 3 | Terminé | 464 | Tiotropium 5 µg une fois par jour (Respimat®) contre placebo pendant 12 semaines dans la mucoviscidose : efficacité et sécurité |
| [NCT00737100](https://clinicaltrials.gov/study/NCT00737100) | Phase 2 | Terminé | 510 | Deux doses de tiotropium (2,5 et 5 µg) contre placebo pendant 12 semaines dans la mucoviscidose : effet sur la fonction pulmonaire, choix de la dose |
| [NCT02172534](https://clinicaltrials.gov/study/NCT02172534) | Phase 1 | Terminé | 113 | Sécurité, tolérance et pharmacocinétique de doses uniques et répétées (28 jours) chez l'enfant et l'adulte atteints de mucoviscidose |

## Preuves de la Littérature

Aucune de ces publications n'étudie directement l'effet du tiotropium sur les malformations respiratoires.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31522031](https://pubmed.ncbi.nlm.nih.gov/31522031/) | 2019 | Étude de physiologie clinique | Respiratory Medicine | Effets de la déflation pulmonaire induite par tiotropium/olodatérol sur les réponses cardiocirculatoires à l'effort |
| [33787023](https://pubmed.ncbi.nlm.nih.gov/33787023/) | 2021 | Rapport de cas | Rev Fac Cien Med (Córdoba) | Infection COVID-19 chez un jeune patient avec pectus excavatum (déformation thoracique) : évolution potentiellement grave |
| [40850565](https://pubmed.ncbi.nlm.nih.gov/40850565/) | 2025 | Préclinique / mécanistique | Chemico-Biological Interactions | Mécanismes du dysfonctionnement ventilatoire chez la souris exposée à un agent neurotoxique organophosphoré (dérégulation cholinergique) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60363967 | SPIRIVA 18 microgrammes, poudre pour inhalation en gélule (statut : active) | Poudre pour inhalation en gélule | Texte de l'indication non renseigné |

## Considérations de Sécurité

Les mises en garde et les contre-indications de la notice ne figurent pas dans les données compilées pour ce rapport. Veuillez consulter la notice pour ces informations.

**Interactions médicamenteuses** : 100 interactions sont recensées. Les principales sont de niveau modéré et concernent d'autres médicaments à action anticholinergique, avec un risque de cumul des effets :
- Hyoscyamine, atropine, scopolamine
- Glycopyrronium (y compris la forme topique), clidinium, dicyclomine
- Trospium, mépenzolate, méthscopolamine, propanthéline
- Élubroxadoline (éluxadoline) et prucalopride, également de niveau modéré
- Insuline humaine inhalée à action rapide, de niveau modéré

La cimétidine est de niveau mineur. Plusieurs autres associations (calcitriol, pantoprazole, glimépiride, mésalazine, doxycycline) sont de niveau inconnu.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé (0,9995), mais aucun essai ni aucune publication ne porte directement sur la malformation respiratoire. Le niveau de preuve est donc L5.
- Le tiotropium agit sur le tonus bronchique et ne peut pas corriger un défaut structurel.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des études ciblant directement les patients atteints de malformation respiratoire, avec une population et un critère de jugement clairement définis.
- Les données sur le mécanisme d'action, afin d'analyser le lien mécanistique.
- Les mises en garde et contre-indications de la notice, pour l'évaluation de sécurité.
- Une vérification de la compatibilité de la voie d'administration (inhalation) avec la population visée, notamment les jeunes enfants.

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

