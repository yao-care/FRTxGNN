---
layout: default
title: Fenoterol
parent: Prédiction du modèle uniquement (L5)
nav_order: 322
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Fenoterol : nouvelle indication prédite, Atrophie multisystématisée (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM (usage connu : bronchodilatateu…"
monitor_inn: "fenoterol"
predicted_indications: ["multiple system atrophy", "postural orthostatic tachycardia syndrome", "variably protease-sensitive prionopathy", "open-angle glaucoma", "Raynaud disease", "primary hereditary glaucoma", "sinoatrial block", "sinoatrial node disease"]
---

# Fenoterol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Fénotérol : D'un bronchodilatateur à l'Atrophie Multisystématisée
{: .text-alpha }

## Résumé en Une Phrase

Le fénotérol est un agoniste bêta-2 adrénergique à action courte, utilisé comme bronchodilatateur (il peut aussi servir à freiner le travail prématuré). Le modèle TxGNN le prédit comme potentiellement efficace pour l'**atrophie multisystématisée**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM (usage connu : bronchodilatateur) |
| Nouvelle Indication Prédite | Atrophie multisystématisée |
| Score de Prédiction TxGNN | 99,70 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulé |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le fénotérol est un agoniste bêta-2 adrénergique à action courte. Son usage bronchodilatateur est établi, et il agit sur les récepteurs bêta-adrénergiques (β1, β2 et β3 d'après les données de pharmacologie compilées).

Le lien mécanistique possible est une modulation sympathique et une vasodilatation médiée par le récepteur bêta-2, pouvant influencer la dysautonomie de l'atrophie multisystématisée. Toutefois, cette vasodilatation pourrait aggraver l'hypotension orthostatique neurogène, symptôme central de cette maladie. La plausibilité biologique est donc faible et ambivalente.

Les autres prédictions du modèle sont du même ordre et ne reposent sur aucune preuve : syndrome de tachycardie orthostatique posturale (mécanisme jugé incohérent, la stimulation bêta-2 risquant d'aggraver les symptômes), prionopathie sensible aux protéases de façon variable (aucun lien identifiable, probable artefact du graphe de connaissances), glaucome à angle ouvert et glaucome héréditaire primitif (lien de classe plausible via l'humeur aqueuse, mais sans donnée propre au fénotérol), maladie de Raynaud (vasodilatation périphérique plausible, mais effets cardiovasculaires limitants), ainsi que bloc sino-atrial et dysfonction sinusale (effet chronotrope théorique, mais risque pro-arythmique et alternatives bien supérieures).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62652340 | BRONCHODUAL 50 microgrammes/20 microgrammes/dose, solution pour inhalation en flacon pressurisé (Boehringer Ingelheim France) | Solution pour inhalation | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Interactions et cibles pharmacologiques** : le fénotérol agit sur les récepteurs bêta-1 (ADRB1), bêta-2 (ADRB2) et bêta-3 (ADRB3) adrénergiques. Aucune interaction médicamenteuse avec un autre médicament n'est documentée dans les données compilées.
- **Points d'attention issus de l'analyse des prédictions** : risques cardiovasculaires (tachycardie, palpitations), arythmies, hypokaliémie et effets sur l'intervalle QT, en particulier à dose élevée ; risque d'aggravation de l'hypotension orthostatique ou de la tachycardie selon l'indication visée.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le mécanisme est ambivalent, voire défavorable : la vasodilatation bêta-2 pourrait aggraver l'hypotension orthostatique. L'AMM française est annulée, ce qui limite la faisabilité pratique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles issues de la notice de l'ANSM (données actuellement manquantes, bloquant l'étape de criblage de sécurité)
- Les données détaillées sur le mécanisme d'action
- Une revue de la littérature préclinique et clinique sur le fénotérol dans l'atrophie multisystématisée
- Une évaluation de la compatibilité de la voie d'administration (inhalée uniquement à ce jour) avec l'indication visée
- Une analyse comparative de la sécurité cardiovasculaire dans cette population
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

