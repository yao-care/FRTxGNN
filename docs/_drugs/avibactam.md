---
layout: default
title: Avibactam
parent: Prédiction du modèle uniquement (L5)
nav_order: 84
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Avibactam : nouvelle indication prédite, Pneumonie à streptocoque (niveau de preuve L5). Indication d'origine : Pyélonéphrite"
monitor_inn: "avibactam"
predicted_indications: ["influenza, severe, susceptibility to", "ureter tuberculosis", "urinary schistosomiasis", "polyclonal hyperviscosity syndrome", "hyperamylasemia"]
---

# Avibactam
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Avibactam : De la pyélonéphrite à la pneumonie à streptocoque

## Résumé en Une Phrase

Avibactam est un inhibiteur de bêta-lactamases (de type diazabicyclooctane), initialement utilisé pour le traitement de la pyélonéphrite, toujours en association avec un bêta-lactame partenaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pneumonie à streptocoque**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Pyélonéphrite (selon le graphe de connaissances TxGNN ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Pneumonie à streptocoque |
| Score de Prédiction TxGNN | 99,70 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'avibactam est un inhibiteur de bêta-lactamases non bêta-lactame, sans activité antibactérienne propre notable. Il n'est utilisé qu'avec un bêta-lactame partenaire (par exemple la ceftazidime), dont il protège l'activité contre les bactéries productrices de bêta-lactamases.

Sur le plan mécanistique, le lien avec la pneumonie à streptocoque est **faible**. La résistance de *Streptococcus pneumoniae* aux bêta-lactames repose principalement sur des modifications des protéines de liaison aux pénicillines, et non sur la production de bêta-lactamases. Inhiber ces enzymes offre donc peu de bénéfice plausible.

Le score élevé (99,70 %) provient d'une prédiction fondée sur le graphe de connaissances, sans essai clinique ni littérature à l'appui. Il doit être interprété avec une grande prudence.

### Autres prédictions du modèle

Les autres indications prédites présentent également un niveau de preuve L5 et une recommandation Hold :

| Indication prédite | Score TxGNN | Lien mécanistique |
|------|------|------|
| Sensibilité à la grippe sévère | 99,28 % | Aucun mécanisme direct plausible ; il s'agit d'un trait de susceptibilité de l'hôte, non d'une infection traitable |
| Tuberculose de l'uretère | 99,11 % | Lien faible et hypothétique : inhibition in vitro de la bêta-lactamase BlaC de *M. tuberculosis*, sans donnée clinique ; proximité avec l'indication d'origine seulement anatomique |
| Schistosomiase urinaire | 99,06 % | Aucune activité antiparasitaire ; la prédiction reflète probablement la proximité dans le réseau avec les maladies urinaires |
| Syndrome d'hyperviscosité polyclonale | 99,01 % | Aucun lien identifiable ; probable artefact de prédiction |
| Hyperamylasémie | 99,01 % | Aucun lien identifiable ; anomalie biologique plutôt que cible thérapeutique |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 69979273 | ZAVICEFTA 2 g/0,5 g | Poudre pour solution à diluer pour perfusion | Non renseignée | Annulée |
| 68544663 | EMBLAVEO 1,5 g/0,5 g | Poudre pour solution à diluer pour perfusion | Non renseignée | Annulée |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les mises en garde et contre-indications issues de la notice n'ont pas pu être compilées, et aucune interaction médicamenteuse n'a été retrouvée dans les données compilées pour ce rapport.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et le lien mécanistique avec la pneumonie à streptocoque est peu plausible, la résistance de ce germe ne reposant pas sur les bêta-lactamases.
- Les deux AMM françaises sont annulées, et les données de sécurité de la notice sont manquantes, ce qui empêche toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice de l'ANSM afin de compiler les mises en garde et contre-indications (lacune bloquante)
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank
- Réaliser une recherche ciblée d'études précliniques ou cliniques sur l'association avibactam + bêta-lactame dans les infections concernées
- Si une piste est retenue, examiner en priorité l'hypothèse la moins improbable (tuberculose urogénitale via l'inhibition de BlaC) par des études in vitro avant tout développement clinique
- Clarifier le statut réglementaire actuel des produits contenant de l'avibactam en France (AMM annulées) ainsi que les indications approuvées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

