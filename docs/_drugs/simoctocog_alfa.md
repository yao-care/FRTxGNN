---
layout: default
title: Simoctocog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 705
evidence_level: L5
indication_count: 10
---

# Simoctocog Alfa
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

# Simoctocog alfa : De l'hémophilie à la pseudo-maladie de von Willebrand

## Résumé en Une Phrase

Simoctocog alfa est un facteur VIII de coagulation humain recombinant (délété du domaine B), initialement utilisé dans le traitement de l'hémophilie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pseudo-maladie de von Willebrand**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémophilie (source : graphe de connaissances TxGNN ; le texte des indications des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Pseudo-maladie de von Willebrand |
| Score de Prédiction TxGNN | 99,997 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 8 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, simoctocog alfa est un facteur VIII recombinant. Son efficacité dans l'hémophilie A repose sur le remplacement du facteur VIII déficient.

**En réalité, la prédiction est peu plausible sur le plan mécanistique.** La pseudo-maladie de von Willebrand est un trouble plaquettaire causé par un gain de fonction de la GPIb-alpha, qui augmente la liaison au facteur de von Willebrand (VWF). Un apport de facteur VIII ne corrige pas ce défaut du récepteur plaquettaire. Le score élevé reflète très probablement une proximité dans le graphe de connaissances (nœuds communs aux troubles hémorragiques), et non une justification biologique.

### Autres indications prédites

Les neuf autres prédictions du modèle ne disposent pas non plus d'essais ni de publications :

| Rang | Maladie prédite | Score TxGNN | Niveau | Évaluation |
|---|---|---|---|---|
| 2 | Trouble de la libération plaquettaire primaire | 99,997 % | L5 | Défaut de sécrétion plaquettaire, indépendant du FVIII |
| 3 | Thrombasthénie de Glanzmann | 99,995 % | L5 | Défaut de l'intégrine αIIbβ3 ; traitement standard : transfusion plaquettaire ou FVIIa recombinant |
| 4 | Syndrome de Scott | 99,969 % | L5 | Lien théorique lointain (FVIII, cofacteur de la ténase), mais la surface phospholipidique manquante n'est pas restaurée |
| 5 | Déficit acquis en facteur de coagulation | 99,952 % | L5 | Lien le plus plausible (ex. hémophilie A acquise), mais les inhibiteurs neutraliseraient le produit ; les agents de contournement sont la norme |
| 6 | Diathèse hémorragique par défaut d'un récepteur du collagène | 99,921 % | L5 | Sans rapport avec le FVIII |
| 7 | Syndrome hémorragique par thrombopénie constitutionnelle | 99,917 % | L5 | Le FVIII ne corrige ni le nombre ni la fonction des plaquettes |
| 8 | Thrombopénie alloimmune fœtale et néonatale | 99,845 % | L5 | Mécanisme immunitaire ; prise en charge par IgIV, corticoïdes, transfusion plaquettaire |
| 9 | Hémophilie A avec anomalie vasculaire | 99,779 % | L4 | Proche de l'indication originale, mais l'anomalie vasculaire n'est pas corrigée ; à traiter comme question de recherche |
| 10 | Purpura thrombotique thrombocytopénique | 99,724 % | L5 | Déficit en ADAMTS13 ; risque théorique d'aggravation de l'état prothrombotique |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 8 AMM, toutes de la gamme NUWIQ (Octapharma, Suède), sont annulées. Aucune n'est actuellement valide.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66102792 | NUWIQ 1000 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 69144152 | NUWIQ 4000 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 63023286 | NUWIQ 250 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 63383804 | NUWIQ 1500 UI | Poudre et solvant pour solution injectable | Non renseignée |
| 67351693 | NUWIQ 500 UI | Poudre et solvant pour solution injectable | Non renseignée |

Trois autres AMM annulées existent (NUWIQ 2500, 3000 et 2000 UI) et ne sont pas détaillées ici.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées pour ce rapport. Une préoccupation théorique est toutefois soulevée pour le purpura thrombotique thrombocytopénique : l'apport de FVIII pourrait aggraver l'état prothrombotique, le FVIII élevé étant un facteur de risque thrombotique.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les dix indications prédites reposent uniquement sur le modèle (niveau L5, sauf une en L4), sans essai ni publication, et la plupart relèvent de défauts plaquettaires ou immunitaires sans lien mécanistique avec le FVIII.
- Toutes les AMM françaises sont annulées, ce qui limite la disponibilité pratique, et les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice (mises en garde et contre-indications) sur le site de l'ANSM, étape bloquante pour le criblage de sécurité
- Données sur le mécanisme d'action depuis DrugBank
- Revue de la littérature et des registres d'essais pour les indications prédites
- Si une piste est poursuivie, priorité à l'hémophilie A acquise (rang 5) et à l'hémophilie A avec anomalie vasculaire (rang 9), comme questions de recherche et non comme candidats au repositionnement
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

