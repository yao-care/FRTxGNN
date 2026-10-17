---
layout: default
title: Zuclopenthixol
parent: Prédiction du modèle uniquement (L5)
nav_order: 833
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Zuclopenthixol : nouvelle indication prédite, Dystrophie rétinienne avec ou sans anomalies extra-oculaires (niveau de preuve L5). Indication d'origine : Schizophrénie"
monitor_inn: "ZUCLOPENTHIXOL"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia X-linked", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "syndromic myopia", "myopia 26, X-linked, female-limited", "atypical glycine encephalopathy"]
---

# Zuclopenthixol
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

# Zuclopenthixol : De la Schizophrénie à la Dystrophie Rétinienne

## Résumé en Une Phrase

Le zuclopenthixol est un antipsychotique de la famille des thioxanthènes, initialement utilisé pour le traitement de la **schizophrénie**.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dystrophie rétinienne (avec ou sans anomalies extra-oculaires)**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Schizophrénie (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Dystrophie rétinienne avec ou sans anomalies extra-oculaires |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 6 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le zuclopenthixol fait partie des thioxanthènes, antipsychotiques antagonistes des récepteurs dopaminergiques D1/D2. Son efficacité dans la schizophrénie est établie, mais aucun élément fourni ne relie le blocage dopaminergique à la dystrophie rétinienne.

La dystrophie rétinienne est un groupe de maladies génétiquement hétérogènes, dont la physiopathologie (dégénérescence des photorécepteurs ou de l'épithélium pigmentaire) n'a pas de lien démontré avec la neurotransmission dopaminergique ciblée par le médicament. Le score élevé de TxGNN (99,99 %) reflète une proximité dans le graphe de connaissances, pas une preuve biologique ou clinique.

En conséquence, la plausibilité mécanistique doit être considérée comme **non étayée** à ce stade. La prédiction reste une hypothèse à documenter avant toute poursuite.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les six AMM identifiées sont toutes annulées ; aucune n'est actuellement valide.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 68072846 | Clopixol Action Prolongée 200 mg/1 ml (BB Farma, Italie) | Solution injectable | Annulée |
| 62788550 | Clopixol Action Prolongée 200 mg/1 ml (Lundbeck SAS) | Solution injectable | Annulée |
| 61323662 | Clopixol 10 mg (Lundbeck SAS) | Comprimé pelliculé | Annulée |
| 63744998 | Clopixol A Action Semi-Prolongée 50 mg/ml (Lundbeck SAS) | Solution injectable | Annulée |
| 69974746 | Clopixol 25 mg (Lundbeck SAS) | Comprimé pelliculé | Annulée |

Une sixième AMM annulée existe (n° 69902540, Clopixol Action Prolongée 200 mg/1 ml, Difarmed, Espagne). Le texte d'indication approuvée n'est pas renseigné pour ces AMM.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées pour ce rapport, et aucune contre-indication issue du graphe de connaissances n'est répertoriée. Cela ne vaut pas absence de risque : le texte des mises en garde et contre-indications de l'ANSM n'a pas pu être exploité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, avec un lien mécanistique non étayé. De plus, toutes les AMM françaises sont annulées et les données de sécurité de la notice sont manquantes, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), élément bloquant
- Obtenir les données de mécanisme d'action depuis DrugBank
- Mener une revue de littérature ciblée sur la dopamine rétinienne et les dystrophies rétiniennes
- Évaluer la pertinence de la voie d'administration et le profil de risque neurologique (effets extrapyramidaux) pour cette population
- Réexaminer les autres indications prédites (myopie, etc.), qui présentent aussi un niveau de preuve L5, et noter que l'antagonisme dopaminergique irait probablement dans le sens défavorable
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

