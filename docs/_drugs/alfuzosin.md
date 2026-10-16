---
layout: default
title: Alfuzosin
parent: Prédiction du modèle uniquement (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Alfuzosin : nouvelle indication prédite, Hypertrichose congénitale universelle de type Ambras (niveau de preuve L5). Indication d'origine : Hyperplasie bénigne de la prostate"
---

# Alfuzosin
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

# Alfuzosine : De l'Hyperplasie Bénigne de la Prostate à l'Hypertrichose Congénitale Universelle de type Ambras

## Résumé en Une Phrase

Alfuzosine est un antagoniste des récepteurs alpha-1 adrénergiques, initialement utilisé pour le traitement de l'hyperplasie bénigne de la prostate.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertrichose congénitale universelle de type Ambras**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hyperplasie bénigne de la prostate (d'après le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Hypertrichose congénitale universelle de type Ambras |
| Score de Prédiction TxGNN | 99,999 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (non commercialisé) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'alfuzosine est un antagoniste alpha-1 adrénergique, dont l'efficacité symptomatique dans l'hyperplasie bénigne de la prostate repose sur la relaxation du muscle lisse prostatique et cervical vésical.

**Il n'existe pas de lien mécanistique établi** avec la nouvelle indication. Le syndrome d'Ambras est une maladie génétique rare, associée à des remaniements du chromosome 8q affectant la régulation de TRPS1, sans voie adrénergique connue. Le score élevé (99,999 %) reflète vraisemblablement la proximité, dans le graphe de connaissances, de maladies partageant un phénotype pileux, plutôt qu'une base biologique.

Les autres prédictions du modèle vont dans le même sens : hypertrichose (direction de l'effet incertaine, certains vasodilatateurs comme le minoxidil *provoquant* une hypertrichose), anomalies de la tige pilaire, hypotrichoses, syndromes malformatifs (dentaires, Dandy-Walker). L'urticaire allergique est l'indication la plus plausible sur le plan biologique, mais reste sans aucune preuve, des traitements établis existant déjà (antihistaminiques anti-H1, omalizumab). Dans le syndrome de circulation fœtale persistante, l'hypotension systémique induite par un alpha-bloquant pourrait aggraver le shunt droite-gauche.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64068708 | XATRAL 2,5 mg, comprimé pelliculé (SANOFI WINTHROP INDUSTRIE) | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, hypotension orthostatique, troubles hypotensifs, syndrome du QT long (y compris familial), torsades de pointes, insuffisance hépatique, maladie hépatique, maladie de la vésicule biliaire, syndrome de l'iris hypotonique peropératoire.
- **Interactions médicamenteuses** : 198 interactions recensées. Parmi celles affichées :
  - **Majeures** : cisapride, clarithromycine, dolasétron (risque lié à l'allongement de l'intervalle QT et/ou à l'inhibition du CYP3A4).
  - **Modérées** : famotidine, aprépitant, bisacodyl, bupropion, canagliflozine, dapagliflozine, empagliflozine, ertugliflozine, clotrimazole, dronabinol, granisétron, lévofloxacine, ricin (huile), glycérine, lactitol, lactulose.
  - **Mineure** : cimétidine.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible ; le profil de sécurité (hypotension, allongement du QT) est défavorable pour des indications bénignes ou génétiques. Le produit n'est en outre plus commercialisé en France (AMM annulée).

**Pour avancer, les éléments suivants sont nécessaires :**
- Mise à disposition des mises en garde et contre-indications de la notice (ANSM), actuellement bloquante pour l'évaluation de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Données précliniques ou mécanistiques justifiant un lien entre la voie adrénergique et la pathologie visée
- Réévaluation de l'ordre de priorité des indications prédites (en particulier l'urticaire allergique, la plus plausible biologiquement) avant tout investissement
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

