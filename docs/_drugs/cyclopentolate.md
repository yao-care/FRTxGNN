---
layout: default
title: Cyclopentolate
parent: Prédiction du modèle uniquement (L5)
nav_order: 202
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Cyclopentolate : nouvelle indication prédite, Syndrome de la queue de cheval (niveau de preuve L5). Indication d'origine : Cycloplégie"
monitor_inn: "CYCLOPENTOLATE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
---

# Cyclopentolate
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Cyclopentolate : De la cycloplégie au syndrome de la queue de cheval
{: .text-alpha }

## Résumé en Une Phrase

Le cyclopentolate est un anticholinergique (antagoniste muscarinique) utilisé en collyre, initialement indiqué pour obtenir une cycloplégie (paralysie de l'accommodation).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de la queue de cheval**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cycloplégie (source : graphe de connaissances TxGNN ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Syndrome de la queue de cheval |
| Score de Prédiction TxGNN | 99,54 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (non commercialisé) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le cyclopentolate fait partie de la classe des antagonistes muscariniques. Son efficacité dans la cycloplégie et la mydriase par voie ophtalmique est établie.

Un raisonnement théorique est possible : le syndrome de la queue de cheval provoque souvent des troubles vésicaux, et le blocage des récepteurs muscariniques pourrait réduire l'hyperactivité du détrusor. Cependant, cette hypothèse reste fragile : le cyclopentolate est un agent ophtalmique sans usage systémique ou urologique établi, et il n'agit pas sur la pathologie sous-jacente, qui est une compression neurologique.

Le score élevé (0,995) reflète une prédiction du modèle uniquement, sans aucune preuve clinique ou bibliographique.

### Autres indications prédites (pour information)

| Rang | Indication prédite | Score TxGNN | Niveau de preuve | Commentaire |
|------|------|------|------|------|
| 2 | Vessie neurogène (terme obsolète dans l'ontologie) | 99,40 % | L5 | Les antimuscariniques (oxybutynine, toltérodine) sont un traitement établi de l'hyperactivité neurogène du détrusor, d'où une plausibilité au niveau de la classe. Aucune donnée sur l'exposition systémique ou la sécurité du cyclopentolate. Le terme devrait être reclassé vers « hyperactivité neurogène du détrusor ». |
| 3 | Syndrome de l'intestin irritable | 99,27 % | L5 | Les antispasmodiques anticholinergiques (dicyclomine, hyoscyamine) sont utilisés pour les douleurs abdominales. Aucun développement oral ou digestif du cyclopentolate ; effets anticholinergiques systémiques problématiques possibles (constipation, effets centraux). |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69255195 | SKIACOL 0,5 POUR CENT, collyre (Laboratoires Alcon) | Collyre en solution | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie du graphe, et non texte de la notice) : hypertension, diabète et acidocétose diabétique, hyperplasie bénigne de la prostate, maladies cardiovasculaires (cardiopathie, maladie coronarienne, arrêt cardiaque soudain, troubles de la conduction cardiaque, artériosclérose, athérosclérose), glaucome à angle fermé, hyperthyroïdie (maladie de Basedow, thyrotoxicose), lésions ou maladies cérébrales, syndrome de Down.
- **Interactions médicamenteuses** : aucune interaction retrouvée dans les données compilées.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être compilées. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai, aucune publication, et le produit n'est plus commercialisé en France (AMM annulée). Le rationnel mécanistique reste théorique pour un collyre sans usage systémique, et les contre-indications du graphe sont nombreuses.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Compléter les données sur le mécanisme d'action (DrugBank)
- Rechercher des essais cliniques et des publications sur les trois indications prédites
- Reclasser le terme obsolète « vessie neurogène » vers « hyperactivité neurogène du détrusor » avant toute évaluation
- Évaluer la compatibilité de voie d'administration (collyre vs voie systémique) et l'exposition systémique requise
- Comparer avec les antimuscariniques déjà établis (oxybutynine, toltérodine, dicyclomine) pour juger de l'intérêt réel
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

