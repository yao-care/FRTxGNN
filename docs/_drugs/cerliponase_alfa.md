---
layout: default
title: Cerliponase Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 155
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Cerliponase Alfa : nouvelle indication prédite, Syndrome de Scheie (niveau de preuve L5). Indication d'origine : Lipofuscinose neuronale céroïde (dont la forme infantile)"
monitor_inn: "CERLIPONASE ALFA"
predicted_indications: ["Scheie syndrome", "Hurler syndrome", "lysosomal storage disease with skeletal involvement", "cholesteryl ester storage disease", "Gaucher disease", "familial encephalopathy with neuroserpin inclusion bodies", "Wolman disease with hypolipoproteinemia and acanthocytosis", "proximal myopathy with extrapyramidal signs", "autosomal ichthyosis syndrome with fatal disease course"]
---

# Cerliponase Alfa
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

## Cerliponase alfa : De la lipofuscinose neuronale céroïde au syndrome de Scheie
{: .text-alpha }

## Résumé en une phrase

Cerliponase alfa est une enzyme recombinante (tripeptidyl peptidase 1, TPP1) administrée par voie intracérébroventriculaire, initialement utilisée pour la lipofuscinose neuronale céroïde, notamment sa forme infantile.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de Scheie**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.
Cette prédiction repose uniquement sur le modèle, et son lien biologique est jugé faible.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Lipofuscinose neuronale céroïde (dont la forme infantile) |
| Nouvelle indication prédite | Syndrome de Scheie |
| Score de prédiction TxGNN | 0,9998 |
| Niveau de preuve | L5 |
| Statut de marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, cerliponase alfa est une enzymothérapie substitutive qui remplace la TPP1, enzyme lysosomale déficiente dans la forme CLN2 de la lipofuscinose neuronale céroïde.

Le syndrome de Scheie (forme atténuée de la mucopolysaccharidose de type I) est lui aussi une maladie de surcharge lysosomale, mais il est dû à un déficit en alpha-L-iduronidase, une enzyme différente, avec accumulation de glycosaminoglycanes. La TPP1 n'agit pas sur ce substrat, et aucun recoupement mécanistique direct n'est établi.

Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités que le modèle a apprises entre maladies lysosomales apparentées, et non une preuve biologique spécifique. Il existe déjà un traitement substitutif adapté pour la MPS I (laronidase).

Les autres prédictions du modèle (syndrome de Hurler, maladie de Gaucher, maladie de surcharge en esters de cholestérol, maladie de Wolman, etc.) appellent les mêmes réserves : absence de lien mécanistique démontré et absence d'essais cliniques. Pour la maladie de Gaucher, une seule publication de cartographie de l'histoire naturelle a été retrouvée ; elle n'évalue pas cerliponase alfa.

## Preuves d'essais cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la littérature

Aucune littérature associée au syndrome de Scheie n'est disponible actuellement.

## Informations de marché en France

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Indication approuvée |
|---------|------|------|-----------|
| 65808346 | BRINEURA 150 mg, solution pour perfusion | Solution pour perfusion | Non renseignée (AMM active) |

## Considérations de sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et sans lien mécanistique plausible entre la TPP1 et le déficit en alpha-L-iduronidase.
- Le seul produit autorisé en France (Brineura) a une AMM annulée, et les données de sécurité de la notice ne sont pas disponibles.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications) afin de permettre une évaluation de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Démontrer, par des études précliniques, un effet de la TPP1 sur la pathologie de la MPS I
- Évaluer la compatibilité de la voie d'administration intracérébroventriculaire avec la maladie visée
- Comparer avec les traitements déjà disponibles, comme la laronidase
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

