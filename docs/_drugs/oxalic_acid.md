---
layout: default
title: Oxalic Acid
parent: Prédiction du modèle uniquement (L5)
nav_order: 563
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Oxalic Acid : nouvelle indication prédite, Rétinopathie diabétique non proliférante sévère (niveau de preuve L5). Indication d'origine : Non renseignée dans les AMM"
monitor_inn: "oxalic acid"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "antithrombin deficiency type 2", "hemoglobinopathy", "factor 5 excess with spontaneous thrombosis", "heparin cofactor 2 deficiency", "thrombophilia", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hyperthyroidism"]
---

# Oxalic Acid
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

## Acide oxalique : De l'absence d'indication documentée à la rétinopathie diabétique non proliférante sévère
{: .text-alpha }

## Résumé en Une Phrase

L'acide oxalique est présent en France dans des préparations homéopathiques (Oxalicum acidum Boiron et Lehning, Berberis complexe n°83), dont les trois autorisations sont aujourd'hui annulées et ne mentionnent aucune indication approuvée.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **rétinopathie diabétique non proliférante sévère**, mais **aucun essai clinique** et **aucune publication** ne soutiennent cette direction.
Les données compilées indiquent plutôt un signal de toxicité de l'oxalate pour la rétine.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM |
| Nouvelle Indication Prédite | Rétinopathie diabétique non proliférante sévère |
| Score de Prédiction TxGNN | 0,9973 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. L'acide oxalique est un acide dicarboxylique, produit terminal du métabolisme, toxique à forte concentration en raison du dépôt d'oxalate de calcium. Aucune indication d'origine n'est documentée dans les autorisations françaises.

Aucun lien mécanistique n'a été identifié avec la rétinopathie diabétique. Le score élevé provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. Un rôle thérapeutique dans la microangiopathie rétinienne est jugé peu plausible.

Les autres prédictions du modèle TxGNN (deep learning) ne sont pas non plus étayées. Les plus proches sont la rétinopathie diabétique (0,9965), le déficit en antithrombine de type 2 (0,9954), l'hémoglobinopathie (0,9951) et la thrombophilie (0,9940). Les déficits de la coagulation semblent résulter de similarités apprises par le modèle entre maladies apparentées (l'oxalate chélate le calcium in vitro), sans pertinence thérapeutique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée à la rétinopathie diabétique non proliférante sévère n'est disponible actuellement.

Pour la rétinopathie diabétique (prédiction de rang 2), la seule publication retrouvée est un cas clinique qui va à l'encontre d'un usage thérapeutique :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [41073327](https://pubmed.ncbi.nlm.nih.gov/41073327/) | 2025 | Cas clinique | Zhonghua Yan Ke Za Zhi | Rétinopathie oxalique bilatérale chez un patient atteint d'hyperoxalurie primaire : dépôts cristallins rétiniens et baisse de l'acuité visuelle. L'oxalate est nocif pour la rétine. |

Pour les autres indications prédites, les publications retrouvées (études métaboliques ou méthodologiques anciennes, séries de cas d'oxalose rénale) décrivent le métabolisme ou la toxicité de l'oxalate et ne démontrent aucun bénéfice thérapeutique.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64922966 | Oxalicum acidum Boiron, dilution 2CH à 30CH ou 4DH à 60DH | Comprimé, solution, granules, poudre et pommade | Non renseignée (AMM active) |
| 62743726 | Oxalicum acidum Lehning, dilution 2CH à 30CH ou 4DH à 60DH | Comprimé, solution, granules, poudre et pommade | Non renseignée (AMM active) |
| 62153864 | Berberis complexe n°83, solution buvable en gouttes | Solution buvable en gouttes | Non renseignée (AMM active) |

---

## Considérations de Sécurité

- **Signal de toxicité rétinienne** : un cas de rétinopathie oxalique (dépôts cristallins) a été rapporté dans le contexte d'une hyperoxalurie primaire, ce qui plaide contre un repositionnement.
- **Toxicité de l'oxalate** : à forte concentration, l'oxalate provoque des dépôts d'oxalate de calcium. Une série de cas ancienne documente une insuffisance rénale terminale liée à l'oxalose.
- **Interactions médicamenteuses** : aucune interaction trouvée dans les données consultées.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est élevé, mais il n'est soutenu par aucun essai clinique, aucune publication pertinente ni aucun mécanisme plausible. Les données disponibles suggèrent plutôt une toxicité rétinienne de l'oxalate. Les trois AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour l'étape de criblage de sécurité)
- Les données sur le mécanisme d'action, à interroger dans DrugBank
- Des données précliniques démontrant un effet bénéfique plausible sur la microvascularisation rétinienne
- Une évaluation de la compatibilité des voies d'administration, de la similarité avec l'indication d'origine et de la pertinence de la littérature (en attente)
- Une analyse de sécurité spécifique au risque de toxicité rétinienne et rénale de l'oxalate
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

