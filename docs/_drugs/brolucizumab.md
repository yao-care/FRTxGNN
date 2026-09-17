---
layout: default
title: Brolucizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 61
evidence_level: L5
indication_count: 4
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

En me basant sur l'Evidence Pack fourni, voici le rapport d'évaluation :

---

# Brolucizumab : De la Dégénérescence Maculaire Néovasculaire au Trouble de la Phosphorylation Oxydative Mitochondriale

## Résumé en Une Phrase

Brolucizumab est un fragment d'anticorps anti-VEGF-A à chaîne unique humanisé, approuvé à l'international (notamment sous la marque Beovu®) pour la dégénérescence maculaire liée à l'âge néovasculaire (DMLA humide) et l'œdème maculaire diabétique, mais actuellement **non commercialisé en France**.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Trouble de la Phosphorylation Oxydative Mitochondriale due à des Anomalies de l'ADN Nucléaire**, avec **aucun essai clinique** et **aucune publication** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Dégénérescence maculaire liée à l'âge néovasculaire (approbation hors France) |
| Nouvelle Indication Prédite | Trouble de la phosphorylation oxydative mitochondriale due à des anomalies de l'ADN nucléaire |
| Score de Prédiction TxGNN | 99,67% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action de brolucizumab ne sont pas disponibles dans les données réglementaires françaises (médicament non commercialisé en France). Sur la base des informations connues à l'international, brolucizumab appartient à la classe des inhibiteurs du VEGF-A : il bloque la liaison du VEGF-A à ses récepteurs (VEGFR-1 et VEGFR-2), inhibant ainsi l'angiogenèse pathologique et la perméabilité vasculaire, principalement dans le contexte des maladies rétiniennes néovasculaires.

Le lien biologique entre l'inhibition du VEGF-A et le trouble de la phosphorylation oxydative mitochondriale causé par des anomalies de l'ADN nucléaire est **hautement indirect et mécanistiquement contradictoire**. Si le VEGF-A exerce une influence modulatrice sur la biogenèse mitochondriale via l'axe PGC-1α, brolucizumab agit précisément comme un antagoniste — c'est-à-dire qu'il *bloque* cette voie plutôt que de la potentialiser. Or, les dysfonctionnements de la chaîne respiratoire mitochondriale d'origine génétique (mutations de l'ADN nucléaire) requièrent des approches correctives ou substitutives de la fonction enzymatique, non une inhibition vasculaire.

L'analyse de la rationalité du repositionnement indique que ce signal TxGNN est vraisemblablement un **artefact de similarité topologique** dans le graphe de connaissances biomédicales, et non le reflet d'une logique mécanistique actionnable. La probabilité de faux positif est jugée élevée par le pipeline d'évaluation.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le niveau de preuve est L5 (prédiction du modèle uniquement, sans aucune étude clinique, préclinique ou publication disponible), et l'analyse mécanistique révèle une direction biologique contradictoire : bloquer le VEGF-A ne constitue pas un mécanisme réparateur pour des défauts génétiques de la chaîne respiratoire mitochondriale. Le signal TxGNN est considéré comme un faux positif topologique à haut risque.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données précliniques in vitro et in vivo démontrant un effet biologique de brolucizumab sur des cellules présentant un déficit de phosphorylation oxydative mitochondriale
- Clarification du mécanisme d'action complet (MOA), notamment les effets biologiques hors-cible documentés
- Données de sécurité complètes (notice EMA / TFDA)
- Réévaluation indépendante du signal TxGNN par un expert en médecine mitochondriale afin de confirmer ou infirmer la pertinence biologique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

