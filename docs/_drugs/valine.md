---
layout: default
title: Valine
parent: Prédiction du modèle uniquement (L5)
nav_order: 330
evidence_level: L5
indication_count: 10
---

# Valine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Valine : De l'apport nutritionnel en acides aminés (indication non documentée) à la Cholangite sclérosante

## Résumé en Une Phrase

La valine est un acide aminé à chaîne ramifiée (BCAA). Elle est commercialisée en France dans des solutions de nutrition orale et parentérale, mais le texte de l'indication approuvée n'est pas renseigné dans les données.
Le modèle TxGNN prédit qu'elle pourrait être utile dans la **cholangite sclérosante**.
Cette prédiction repose sur **0 essai clinique** et **2 publications**, toutes deux indirectes et sans lien démontré avec un bénéfice de la valine.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données réglementaires (les produits sont des solutions d'acides aminés pour voie orale ou perfusion) |
| Nouvelle Indication Prédite | Cholangite sclérosante |
| Score de Prédiction TxGNN | 99,42 % |
| Niveau de Preuve | L4 (études indirectes, sans essai clinique) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la valine est un acide aminé essentiel de la famille des BCAA. Elle entre dans la composition de solutions de nutrition (Revitalose, Aminoven, Aminoplasmal, Aminomix). Son usage en nutrition est établi, mais son efficacité dans la cholangite sclérosante n'a pas été démontrée.

Le lien avec la nouvelle indication reste hypothétique. Les maladies hépatiques chroniques s'accompagnent souvent d'anomalies du métabolisme des acides aminés, et les BCAA y jouent un rôle connu. Aucune étude ne montre pourtant qu'une supplémentation en valine améliore la cholangite sclérosante. Les deux publications retrouvées apportent seulement un contexte métabolique indirect : l'une porte sur les taux plasmatiques de tyrosine et la fatigue dans les maladies cholestatiques, l'autre sur des associations entre métabolites sanguins et risque de maladies cholestatiques.

Le score TxGNN (0,994) provient uniquement d'un graphe de connaissances. Il doit être considéré comme une hypothèse de recherche, non comme une preuve d'efficacité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohorte | BMC Gastroenterology | Étude de la relation entre la tyrosine plasmatique et la fatigue dans la cirrhose biliaire primitive et la cholangite sclérosante primitive. Elle porte sur la tyrosine, pas sur la valine. |
| [39015781](https://pubmed.ncbi.nlm.nih.gov/39015781/) | 2024 | Randomisation mendélienne | Frontiers in Medicine | Analyse causale entre métabolites sanguins et risque de cholangite biliaire primitive et de cholangite sclérosante primitive. Contexte métabolique seulement. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63363997 | REVITALOSE SANS SUCRE, solution buvable édulcorée au sorbitol | Solution buvable | Non renseignée |
| 61960303 | AMINOVEN 10 POUR CENT, solution pour perfusion | Solution pour perfusion | Non renseignée |
| 69667989 | AMINOVEN 5 POUR CENT, solution pour perfusion | Solution pour perfusion | Non renseignée |
| 63183821 | AMINOPLASMAL 8, solution pour perfusion | Solution pour perfusion | Non renseignée |
| 61786735 | AMINOMIX 500, solution pour perfusion | Solution pour perfusion | Non renseignée |

Au total, 20 AMM sont recensées. Seules les 5 premières sont listées ici.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Il n'existe aucun essai clinique et aucune publication montrant un effet de la valine dans la cholangite sclérosante. Les deux articles retrouvés sont indirects, et la prédiction repose sur le seul score du graphe de connaissances.
- Les données de sécurité de la notice ANSM manquent, ce qui bloque le passage à l'évaluation de sécurité.
- Les autres indications prédites (glaucomes, hyperthyroïdie, résistance aux hormones thyroïdiennes, hyperthyroxinémie) sont encore plus faibles. Les publications associées sont des faux positifs liés à la nomenclature des acides aminés (« Val ») ou à des médicaments au nom proche, comme le valsartan.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications).
- Obtenir les données de mécanisme d'action depuis DrugBank.
- Renseigner l'indication approuvée de chaque AMM pour établir l'indication d'origine.
- Mener une revue ciblée de la littérature sur les BCAA et la valine dans les maladies cholestatiques.
- Formuler une hypothèse mécanistique testable avant toute étude préclinique ou clinique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

