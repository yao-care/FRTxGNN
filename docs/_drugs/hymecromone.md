---
layout: default
title: Hymecromone
parent: Prédiction du modèle uniquement (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "hymecromone"
predicted_indications: ["diabetic nephropathy", "brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "allergic asthma", "intrinsic asthma", "gout", "hemoglobinopathy", "type 1 diabetes mellitus", "bronchitis", "partial deletion of the short arm of chromosome 16"]
description: "Hymecromone : nouvelle indication prédite, Diabetic nephropathy (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Hymecromone
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

## Hymecromone: Diabetic nephropathy
{: .text-alpha }

## Résumé en Une Phrase

L'hymécromone (CANTABILINE 400 mg, comprimé) est un médicament dont l'indication d'origine n'est pas renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **néphropathie diabétique**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Diabetic nephropathy |
| Score de Prédiction TxGNN | 0.9985 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, l'hymécromone (4-méthylumbelliférone) est décrite comme un inhibiteur de la synthèse de l'acide hyaluronique. Le texte de l'AMM ne mentionne aucune indication, ce qui empêche d'établir un lien avec l'indication d'origine.

L'hypothèse mécanistique est que l'accumulation d'acide hyaluronique est impliquée, dans la littérature préclinique, dans la fibrose rénale et les lésions rénales diabétiques. Ce lien reste toutefois spéculatif : aucun essai ni publication n'a été fourni pour l'étayer.


### Autres prédictions du modèle

Les autres indications prédites sont toutes au niveau L5 (aucune preuve clinique), avec une recommandation Hold :

| Rang | Maladie prédite | Score TxGNN | Plausibilité mécanistique |
|---|---|---|---|
| 2 | Maladie des petits vaisseaux cérébraux de type 1 (avec ou sans anomalies oculaires) | 0,9985 | Aucun lien clair (trouble monogénique rare lié à COL4A1) |
| 3 | Syndrome familial autosomique dominant d'hématurie, tortuosité artériolaire rétinienne et contractures | 0,9985 | Aucun lien étayé (trouble COL4A1 de la membrane basale) |
| 4 | Asthme allergique | 0,9980 | Hypothèse plausible mais non vérifiée (inflammation et remodelage des voies aériennes) |
| 5 | Asthme intrinsèque | 0,9979 | Même hypothèse que l'asthme allergique, prédiction probablement corrélée |
| 6 | Goutte | 0,9973 | Aucun lien évident |
| 7 | Hémoglobinopathie | 0,9957 | Aucun mécanisme étayé |
| 8 | Diabète de type 1 | 0,9954 | Données précliniques suggérant une modulation de l'auto-immunité des îlots, non étayées ici |
| 9 | Bronchite | 0,9946 | Lien faible et spéculatif |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61974317 | CANTABILINE 400 mg, comprimé (DB PHARMA) | Comprimé | Non renseignée (AMM active) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées, et aucune contre-indication issue du graphe de connaissances n'est répertoriée.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Toutes les prédictions reposent uniquement sur le modèle (niveau L5), sans essai clinique ni publication. L'AMM française est annulée et les données de sécurité de la notice sont manquantes, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), point bloquant
- Obtenir les données sur le mécanisme d'action via DrugBank
- Clarifier l'indication d'origine du médicament et les raisons de l'annulation de l'AMM
- Mener une revue de la littérature préclinique sur l'inhibition de l'acide hyaluronique dans la néphropathie diabétique
- Évaluer la compatibilité des voies d'administration (actuellement en attente)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

