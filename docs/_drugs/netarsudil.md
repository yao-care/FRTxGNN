---
layout: default
title: Netarsudil
parent: Prédiction du modèle uniquement (L5)
nav_order: 532
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Netarsudil : nouvelle indication prédite, Glaucome héréditaire primitif (niveau de preuve L5). Indication d'origine : Glaucome à angle ouvert"
monitor_inn: "netarsudil"
predicted_indications: ["primary hereditary glaucoma"]
---

# Netarsudil
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Nétarsudil : Du Glaucome à Angle Ouvert au Glaucome Héréditaire Primitif

## Résumé en Une Phrase

Le nétarsudil est un collyre inhibiteur de la Rho kinase (ROCK), initialement utilisé pour traiter le glaucome à angle ouvert et l'hypertension oculaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **glaucome héréditaire primitif**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique ni aucune publication** ne la soutient actuellement pour cette indication précise.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Glaucome à angle ouvert ; hypertension oculaire |
| Nouvelle Indication Prédite | Glaucome héréditaire primitif |
| Score de Prédiction TxGNN | 99,50 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisation annulée uniquement |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. Les données pharmacologiques montrent toutefois que le nétarsudil inhibe les kinases ROCK1 et ROCK2. D'après les connaissances générales, il inhibe aussi le transporteur de la noradrénaline. Ces actions augmentent l'écoulement de l'humeur aqueuse par le trabéculum et réduisent la pression veineuse épisclérale, ce qui fait baisser la pression intraoculaire (PIO).

Les glaucomes héréditaires (congénitaux ou juvéniles) impliquent une altération de l'écoulement trabéculaire. Un lien conceptuel existe donc avec le mécanisme du médicament, qui agit déjà sur cette voie dans le glaucome à angle ouvert. Ce lien reste théorique : le score très élevé du modèle ne remplace pas des données cliniques, et aucune étude fournie ne porte spécifiquement sur la forme héréditaire.

À titre de contexte, l'indication plus large « glaucome » (second résultat de la prédiction) est, elle, largement documentée. Elle compte de nombreux essais de phase 3 (par exemple NCT02558374, NCT02674854, NCT02207491) et un essai de phase 3 comparant le nétarsudil au ripasudil (PMID 37603205). Elle recoupe toutefois fortement l'indication d'origine : il s'agit d'une confirmation de l'usage approuvé, non d'un véritable repositionnement.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour le glaucome héréditaire primitif.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour cette indication.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64224662 | ROCLANDA 50 microgrammes/mL + 200 microgrammes/mL, collyre en solution (SANTEN OY) | Collyre en solution | Non précisée (AMM annulée) |

## Considérations de Sécurité

- **Interactions médicamenteuses** : aucune interaction médicamenteuse cliniquement documentée n'a été identifiée. Les données disponibles concernent uniquement les cibles pharmacologiques du nétarsudil (ROCK1 et ROCK2).
- **Effets indésirables oculaires rapportés dans la littérature** (surtout en cas de glaucome à angle ouvert) :
  - verticillata cornéenne ;
  - kératopathie épithéliale ;
  - œdème épithélial réticulaire ;
  - fragilité conjonctivale ;
  - sténose ou fermeture ponctuelle ;
  - hypertrophie en nid d'abeille.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour le glaucome héréditaire primitif repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication spécifique.
- L'AMM française est annulée, ce qui limite aussi la faisabilité à court terme.

**Pour avancer, les éléments suivants sont nécessaires :**
- Études précliniques ou cliniques ciblant les formes héréditaires (congénitales ou juvéniles) de glaucome.
- Données détaillées sur le mécanisme d'action (MOA).
- Mises en garde et contre-indications issues de la notice officielle de l'ANSM.
- Vérification du statut réglementaire (l'annulation concerne peut-être uniquement cette présentation) et des voies d'administration compatibles.
- Si le glaucome au sens large est visé, une réévaluation distincte, qui pourrait justifier « Proceed with Guardrails » (niveau L1), avec surveillance des effets indésirables oculaires.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

