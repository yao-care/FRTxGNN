---
layout: default
title: Glucarpidase
parent: Prédiction du modèle uniquement (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Glucarpidase : nouvelle indication prédite, Cataracte diabétique (niveau de preuve L5). Indication d'origine : Non renseignée dans les données disponibles"
monitor_inn: "GLUCARPIDASE"
predicted_indications: ["diabetic cataract", "diabetic retinopathy", "craniostenosis cataract", "mature cataract", "tetanic cataract", "diabetes mellitus type 2 associated cataract", "immature cataract", "cortical cataract", "nuclear senile cataract", "senile cataract"]
---

# Glucarpidase
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

## Glucarpidase : D'une indication non documentée à la Cataracte diabétique
{: .text-alpha }

## Résumé en Une Phrase

Glucarpidase est une enzyme recombinante (carboxypeptidase G2) qui hydrolyse le méthotrexate et d'autres folates en métabolites inactifs. Son indication d'origine n'est pas renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **cataracte diabétique**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données disponibles |
| Nouvelle Indication Prédite | Cataracte diabétique |
| Score de Prédiction TxGNN | 99,85 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Retiré (AMM annulée uniquement) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales, le glucarpidase est une enzyme bactérienne recombinante qui dégrade le méthotrexate extracellulaire et les folates. Elle est administrée par voie intraveineuse.

**Cette prédiction n'est pas étayée sur le plan mécanistique.** Le glucarpidase n'a aucune action connue sur la voie des polyols, l'aldose réductase, la glycation ni l'opacification du cristallin. Sa taille (grosse enzyme) et sa voie systémique rendent par ailleurs une pénétration oculaire peu plausible.

Le score élevé (99,85 %) est à interpréter avec prudence. Plusieurs sous-types de cataracte (mature, immature, tétanique, associée au diabète de type 2, etc.) reçoivent des scores quasi identiques (≈ 99,83 %), ce qui suggère un artefact de structure du graphe de connaissances plutôt qu'un signal spécifique à la maladie. Les autres prédictions du classement (rétinopathie diabétique, cataractes sénile, corticale, nucléaire, craniosténose avec cataracte) souffrent des mêmes limites : aucun lien mécanistique ni donnée clinique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60176597 | VORAXAZE 1000 unités, poudre pour solution injectable (SERB) | Poudre pour solution injectable | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 8 interactions de niveau modéré identifiées (source : DDInter) :
  - Proguanil
  - Triméthoprime
  - Lévoleucovorine
  - Pémétrexed
  - Pralatrexate
  - Pyriméthamine
  - Leucovorine (acide folinique)
  - Triméthrexate

  Ces interactions concernent principalement des médicaments liés au métabolisme des folates (antifolates et folates).

Veuillez consulter la notice pour les mises en garde et contre-indications.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible. De plus, l'AMM française est annulée et les données de sécurité issues de la notice sont manquantes, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde, contre-indications, indication approuvée)
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Identifier un lien biologique plausible entre l'activité enzymatique et la physiopathologie de la cataracte, avec des études précliniques (niveau L4) avant toute considération clinique
- Évaluer la faisabilité d'une voie d'administration oculaire, la voie intraveineuse actuelle étant peu compatible avec l'indication visée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

