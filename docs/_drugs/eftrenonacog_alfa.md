---
layout: default
title: Eftrenonacog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 272
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Eftrenonacog Alfa : nouvelle indication prédite, Pseudo-maladie de von Willebrand (niveau de preuve L5). Indication d'origine : Hémophilie"
monitor_inn: "eftrenonacog alfa"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia"]
---

# Eftrenonacog Alfa
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Eftrenonacog alfa : De l'hémophilie à la pseudo-maladie de von Willebrand

## Résumé en Une Phrase

Eftrenonacog alfa (ALPROLIX) est un facteur IX de coagulation recombinant fusionné à un fragment Fc, initialement utilisé pour le traitement de l'hémophilie, y compris la forme symptomatique chez les porteuses.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pseudo-maladie de von Willebrand**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémophilie (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas disponible) |
| Nouvelle Indication Prédite | Pseudo-maladie de von Willebrand |
| Score de Prédiction TxGNN | 99,48 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 5 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les informations connues, eftrenonacog alfa est un facteur IX recombinant couplé à un fragment Fc (rFIXFc). Il remplace le facteur IX déficient dans la voie intrinsèque de la coagulation, ce qui justifie son usage dans l'hémophilie.

Le lien avec la nouvelle indication est faible. La pseudo-maladie de von Willebrand (de type plaquettaire) est due à des mutations avec gain de fonction de la GPIbα plaquettaire. Celles-ci augmentent la liaison des plaquettes au facteur von Willebrand, entraînent l'élimination des grands multimères de VWF et provoquent des saignements d'origine plaquettaire. Le défaut porte sur l'interaction plaquette-VWF, et non sur un déficit en facteur IX.

Le score élevé du modèle (99,48 %) reflète probablement une proximité dans le réseau des maladies hémorragiques, plutôt qu'une justification mécanistique. Cette prédiction doit donc être considérée avec une grande prudence.

Deux autres prédictions du modèle présentent la même limite : le trouble primaire de la libération plaquettaire (99,42 %) et la thrombasthénie de Glanzmann (99,28 %). Dans les deux cas, le défaut est plaquettaire et se situe en dehors de la voie du facteur IX. Aucun essai ni publication ne les soutient.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66430312 | ALPROLIX 500 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 68071018 | ALPROLIX 1000 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 64611260 | ALPROLIX 250 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 60256036 | ALPROLIX 3000 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 64832013 | ALPROLIX 2000 UI | Poudre et solvant pour solution injectable | Non renseignée |

Les cinq AMM, détenues par Swedish Orphan Biovitrum (Suède), sont annulées.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées pour ce rapport, et aucune interaction médicamenteuse n'a été retrouvée.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication, et le mécanisme du facteur IX ne correspond pas au défaut plaquettaire de la pseudo-maladie de von Willebrand.
- Le produit ne dispose plus d'AMM valide en France et les données de sécurité de la notice sont manquantes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) pour le criblage de sécurité
- Obtenir les données sur le mécanisme d'action via DrugBank
- Rechercher des données précliniques ou cliniques pertinentes pour la pseudo-maladie de von Willebrand
- Clarifier le statut réglementaire du produit en France (AMM annulées) et la voie d'administration
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

