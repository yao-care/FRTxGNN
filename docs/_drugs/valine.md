---
layout: default
title: Valine
parent: Preuves modérées (L3-L4)
nav_order: 801
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-31
description: "Valine : nouvelle indication prédite, Cholangite sclérosante (niveau de preuve L4). Indication d'origine : Non précisée dans les données compilées (texte d'indication vide pour…"
monitor_inn: "VALINE"
predicted_indications: ["sclerosing cholangitis", "angle-closure glaucoma", "hyperthyroidism", "aqueous misdirection", "traumatic glaucoma", "neovascular glaucoma", "glaucomatous atrophy of optic disc", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "obsolete bundle branch block", "hyperthyroxinemia"]
---

# Valine
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

## Valine : D'un acide aminé nutritionnel à la cholangite sclérosante
{: .text-alpha }

## Résumé en Une Phrase

La valine est un acide aminé à chaîne ramifiée (BCAA), présent dans de nombreuses solutions de nutrition parentérale et entérale. Le modèle TxGNN prédit qu'elle pourrait être utile dans la **cholangite sclérosante**, mais aucun essai clinique n'étaye cette direction et seules **2 publications** indirectes (étude de cohorte et randomisation mendélienne) existent. Il s'agit d'associations métaboliques, non d'une preuve thérapeutique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données compilées (texte d'indication vide pour toutes les AMM) |
| Nouvelle Indication Prédite | Cholangite sclérosante |
| Score de Prédiction TxGNN | 0,9942 |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 19) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la valine est un acide aminé essentiel de la famille des BCAA, utilisé comme composant de solutions d'acides aminés pour la nutrition. Son rôle est nutritionnel et non ciblé sur une maladie hépatique précise.

Le lien avec la cholangite sclérosante reste indirect. Une étude de cohorte a examiné les profils d'acides aminés plasmatiques et la fatigue dans la cholangite biliaire primitive et la cholangite sclérosante primitive (accent sur la tyrosine). Une étude de randomisation mendélienne a exploré l'effet causal de métabolites sanguins sur ces maladies cholestatiques. Ces travaux montrent que le métabolisme des acides aminés est perturbé dans ces maladies, mais **rien n'indique qu'une supplémentation en valine les traite**.

Le score élevé du modèle doit donc être interprété avec prudence : il provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, non une preuve biologique ni une efficacité démontrée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39015781](https://pubmed.ncbi.nlm.nih.gov/39015781/) | 2024 | Randomisation mendélienne | Frontiers in Medicine | Étude de la relation causale entre métabolites sanguins et risque de cholangite biliaire primitive et de cholangite sclérosante primitive |
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohorte | BMC Gastroenterology | Recherche d'anomalies des acides aminés plasmatiques (notamment la tyrosine) et de leur lien avec la fatigue dans ces deux maladies |

---

## Informations de Marché en France

Le médicament est commercialisé ; 19 AMM sont actuellement valides. Le texte d'indication approuvée n'est pas disponible. Principales AMM (5 sur 20) :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63363997 | REVITALOSE SANS SUCRE, solution buvable édulcorée au sorbitol | Solution buvable | Non renseignée |
| 61960303 | AMINOVEN 10 POUR CENT, solution pour perfusion | Solution pour perfusion | Non renseignée |
| 69667989 | AMINOVEN 5 POUR CENT, solution pour perfusion | Solution pour perfusion | Non renseignée |
| 63183821 | AMINOPLASMAL 8, solution pour perfusion | Solution pour perfusion | Non renseignée |
| 61786735 | AMINOMIX 500, solution pour perfusion | Solution pour perfusion | Non renseignée |

Les autres AMM concernent des produits de nutrition parentérale similaires (Aminoplasmal, Olimel, SmofKabiven, Clinimix, Primene, Nutrineal, etc.).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur le modèle et sur des associations métaboliques indirectes (cohorte, génétique). Aucun essai clinique ni preuve thérapeutique n'existe, et le produit n'a plus d'AMM valide en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action de la valine et son lien plausible avec la physiopathologie de la cholangite sclérosante
- Informations de sécurité issues des notices (mises en garde, contre-indications), actuellement manquantes
- Texte des indications approuvées des anciennes AMM
- Études précliniques, puis cliniques, évaluant un effet thérapeutique de la valine dans cette maladie
- Évaluation de la compatibilité des voies d'administration avec l'usage envisagé

**Note sur les autres prédictions :** les autres indications prédites (glaucomes, hyperthyroïdie, résistance aux hormones thyroïdiennes, hyperthyroxinémie, etc.) ne disposent d'aucune preuve thérapeutique. Pour l'hyperthyroïdie et les maladies thyroïdiennes apparentées, la littérature porte surtout sur des mutations de récepteurs où « Val » désigne une substitution d'acide aminé, ce qui relève très probablement d'artefacts de correspondance de noms.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

