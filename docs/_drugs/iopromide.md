---
layout: default
title: Iopromide
parent: Prédiction du modèle uniquement (L5)
nav_order: 408
evidence_level: L5
indication_count: 9
monitor_inn: "IOPROMIDE"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "alopecia", "myosclerosis", "hemoglobinopathy", "pseudoachondroplasia"]
last_modified_at: 2026-10-23
description: "Iopromide : nouvelle indication prédite, Arthrose (niveau de preuve L5). Indication d'origine : Non précisée dans les données d'AMM compilées (texte d'indication vid…"
---

# Iopromide
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

## Iopromide : D'un produit de contraste iodé à l'arthrose (prédiction non étayée)
{: .text-alpha }

## Résumé en Une Phrase

Iopromide est un produit de contraste iodé non ionique, utilisé en imagerie diagnostique (spécialité Ultravist).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**arthrose**, mais il s'agit d'une prédiction purement informatique :
**aucun essai clinique** et **aucune publication** ne la soutiennent actuellement dans les données compilées pour ce rapport.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données d'AMM compilées (texte d'indication vide) |
| Nouvelle Indication Prédite | Arthrose |
| Score de Prédiction TxGNN | 0,9953 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Iopromide est un agent de contraste iodé non ionique : il sert à rendre visibles les structures anatomiques à l'imagerie et n'a pas d'activité pharmacologique connue sur les maladies articulaires.

Le score élevé du modèle TxGNN (deep learning) (0,9953) provient du modèle et peut refléter des similarités apprises par le modèle entre maladies apparentées (maladies articulaires ou squelettiques), et non une justification biologique. L'usage du produit en arthrographie est un acte diagnostique, pas un effet thérapeutique.

Il n'est donc pas possible, en l'état, d'établir un lien mécanistique entre l'usage d'origine et l'arthrose. Les autres prédictions du modèle présentent la même limite : polyarthrite rhumatoïde (99,37 %), brachyolmie (99,19 %), dysplasie acromésomélique de type Hunter-Thompson (99,14 %), syndrome brachyolmie-amélogenèse imparfaite (99,12 %), alopécie (99,11 %), myosclérose (99,09 %), hémoglobinopathie (99,08 %) et pseudoachondroplasie (99,06 %). Aucune n'a de mécanisme plausible ni de preuve clinique ou bibliographique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68373358 | Ultravist 300 (300 mg d'iode/mL) | Solution injectable | Non renseignée |
| 62729413 | Ultravist 370 (370 mg d'iode/mL) | Solution injectable | Non renseignée |
| 65027575 | Ultravist 370 (370 mg d'iode/mL), seringue préremplie pour injecteur automatique | Solution injectable | Non renseignée |
| 60385522 | Ultravist 300 (300 mg d'iode/mL), seringue préremplie pour injecteur automatique | Solution injectable | Non renseignée |

Les quatre AMM, détenues par Bayer Healthcare, sont valides et concernent le médicament seul.

## Considérations de Sécurité

- **Interactions médicamenteuses** : 100 interactions sont recensées. Parmi les premières, les interactions de niveau majeur concernent notamment :
  - metformine ;
  - amphotéricine B (y compris formes lipidique, sulfate de cholestéryle et liposomale) ;
  - mésalazine, balsalazide, olsalazine et sulfasalazine ;
  - vancomycine ;
  - aminosides (kanamycine, néomycine, streptomycine) ;
  - polymyxine B.

  Le mannitol présente une interaction de niveau modéré. Plusieurs autres (clotrimazole, acide acétylsalicylique, bupropion, dexaméthasone, pantoprazole) sont de niveau non précisé.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai, aucune publication, aucun mécanisme plausible pour l'arthrose ni pour les autres maladies prédites.
- Les données de sécurité de la notice sont absentes, ce qui bloque toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications, indications autorisées).
- Obtenir les données sur le mécanisme d'action (DrugBank).
- Identifier des études précliniques ou cliniques portant directement sur l'arthrose, avant toute réévaluation.
- Évaluer la compatibilité de la voie d'administration (actuellement en attente) avec un usage thérapeutique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

