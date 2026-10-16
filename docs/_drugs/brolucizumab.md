---
layout: default
title: Brolucizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 118
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Brolucizumab : nouvelle indication prédite, Trouble de la phosphorylation oxydative mitochondriale dû à des anoma… (niveau de preuve L5). Indication d'origine : Dégénérescence maculaire (texte d'indi…"
monitor_inn: "BROLUCIZUMAB"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "esophageal varices with bleeding", "esophageal varices without bleeding", "exocrine pancreatic insufficiency"]
---

# Brolucizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

# Brolucizumab : De la dégénérescence maculaire à un trouble de la phosphorylation oxydative mitochondriale (ADN nucléaire)

## Résumé en Une Phrase

Brolucizumab est un fragment d'anticorps à chaîne unique anti-VEGF-A, initialement utilisé pour le traitement de la dégénérescence maculaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble de la phosphorylation oxydative mitochondriale dû à des anomalies de l'ADN nucléaire**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dégénérescence maculaire (texte d'indication de l'AMM non renseigné) |
| Nouvelle Indication Prédite | Trouble de la phosphorylation oxydative mitochondriale dû à des anomalies de l'ADN nucléaire |
| Score de Prédiction TxGNN | 99,67 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulée (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le brolucizumab est un inhibiteur du VEGF-A de type fragment d'anticorps à chaîne unique, dont l'usage est établi dans la dégénérescence maculaire.

Aucun lien mécanistique plausible n'est établi avec les défauts de phosphorylation oxydative d'origine nucléaire. Les maladies mitochondriales peuvent comporter une atteinte rétinienne et une signalisation VEGF liée à l'hypoxie, mais cette hypothèse reste spéculative.

Le score élevé de TxGNN (0,997) provient d'une prédiction fondée sur le graphe de connaissances. Il n'est étayé par aucun essai clinique ni aucune publication dans les données compilées pour ce rapport, et doit donc être interprété avec une grande prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65607585 | BEOVU 120 mg/ml, solution injectable en seringue préremplie (statut : annulée) | Solution injectable | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie du graphe, et non texte de la notice) : uvéite, maladie de l'iris, maladie du corps ciliaire, panuvéite, maladie infectieuse oculaire, conjonctivite.

Pour les mises en garde, contre-indications officielles et interactions médicamenteuses, veuillez consulter la notice.

## Autres Indications Prédites (pour information)

| Rang | Indication Prédite | Score TxGNN | Niveau de Preuve | Commentaire |
|------|------|------|------|------|
| 2 | Varices œsophagiennes avec saignement | 99,12 % | L5 | Rationnel théorique (angiogenèse dépendante du VEGF, hypertension portale). Produit intravitréen, non conçu pour une voie systémique. Risque hémorragique et thromboembolique préoccupant en contexte de saignement actif. |
| 3 | Varices œsophagiennes sans saignement | 99,12 % | L5 | Même rationnel et mêmes réserves. Score identique à la forme hémorragique, ce qui suggère des nœuds proches dans le graphe plutôt qu'une preuve indépendante. |
| 4 | Insuffisance pancréatique exocrine | 99,07 % | L5 | Aucun lien mécanistique clair. Prise en charge par substitution enzymatique. Score probablement un artefact du graphe. |

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique établi.
- L'AMM française est annulée, et les données de sécurité officielles sont absentes. Il n'est pas possible de passer à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (analyse du PDF de la notice).
- Obtenir les données sur le mécanisme d'action via DrugBank.
- Mener une revue de la littérature et des registres d'essais sur les maladies mitochondriales et le VEGF.
- Évaluer la compatibilité de la voie d'administration (produit intravitréen) avec l'indication visée.
- Clarifier la situation réglementaire de la spécialité (AMM annulée).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

