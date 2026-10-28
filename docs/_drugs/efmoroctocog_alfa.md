---
layout: default
title: Efmoroctocog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 271
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Efmoroctocog Alfa : nouvelle indication prédite, Pseudo-maladie de von Willebrand (niveau de preuve L5). Indication d'origine : Hémophilie (forme symptomatique de l'hémophilie chez les porteuses)"
monitor_inn: "EFMOROCTOCOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "thrombotic thrombocytopenic purpura"]
---

# Efmoroctocog Alfa
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

## Efmoroctocog alfa : De l'hémophilie à la pseudo-maladie de von Willebrand
{: .text-alpha }

## Résumé en Une Phrase

Efmoroctocog alfa est un facteur VIII de coagulation recombinant fusionné à un fragment Fc (rFVIII-Fc), initialement utilisé pour le traitement de l'hémophilie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pseudo-maladie de von Willebrand** (de type plaquettaire), mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.
La prédiction repose uniquement sur le modèle, et le lien mécanistique est jugé faible.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémophilie (forme symptomatique de l'hémophilie chez les porteuses) |
| Nouvelle Indication Prédite | Pseudo-maladie de von Willebrand |
| Score de Prédiction TxGNN | 1,0000 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 8 sur 8) |
| Nombre d'AMM | 8 (valides : 8) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, efmoroctocog alfa est un facteur VIII recombinant fusionné à un fragment Fc, qui remplace le facteur VIII déficient dans l'hémophilie. Le fragment Fc prolonge sa demi-vie dans la circulation.

La pseudo-maladie de von Willebrand (de type plaquettaire) est causée par un gain de fonction du récepteur plaquettaire GPIbα, qui entraîne la perte des multimères de haut poids moléculaire du facteur von Willebrand (VWF). Le remplacement du facteur VIII ne corrige pas ce défaut du récepteur plaquettaire : le lien mécanistique est donc **faible**.

Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, telles que les troubles hémorragiques liés au VWF et au FVIII, et non une preuve biologique.

### Autres indications prédites (pour information)

| Rang | Maladie | Score | Plausibilité mécanistique | Recommandation |
|---|---|---|---|---|
| 2 | Trouble de la libération plaquettaire primaire | 1,0000 | Absente (défaut de sécrétion des granules) | Hold |
| 3 | Thrombasthénie de Glanzmann | 1,0000 | Absente (défaut de l'intégrine αIIbβ3) | Hold |
| 4 | Syndrome de Scott | 0,9997 | Spéculative (défaut TMEM16F/ANO6) | Hold |
| 5 | Déficit acquis en facteur de coagulation | 0,9995 | La plus plausible (ex. hémophilie acquise), limitée par les inhibiteurs | Research Question |
| 6 | Diathèse hémorragique par défaut de récepteur du collagène | 0,9992 | Absente | Hold |
| 7 | Trouble hémorragique par thrombopénie constitutionnelle | 0,9992 | Absente | Hold |
| 8 | Thrombopénie alloimmune fœtale et néonatale | 0,9984 | Absente | Hold |
| 10 | Purpura thrombotique thrombocytopénique | 0,9972 | Absente, risque théorique d'aggravation prothrombotique | Hold |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 8 autorisations, toutes détenues par Swedish Orphan Biovitrum International (Suède), sont **valides**. Le texte des indications approuvées n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 69349794 | ELOCTA 1500 UI | Poudre et solvant pour solution injectable | Active |
| 60602449 | ELOCTA 750 UI | Poudre et solvant pour solution injectable | Active |
| 68853909 | ELOCTA 2000 UI | Poudre et solvant pour solution injectable | Active |
| 69009069 | ELOCTA 1000 UI | Poudre et solvant pour solution injectable | Active |
| 64440763 | ELOCTA 250 UI | Poudre et solvant pour solution injectable | Active |

*Trois autres AMM (500, 3000 et 4000 UI) sont également annulées.*

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées. Dans le cas du purpura thrombotique thrombocytopénique, un risque théorique d'aggravation de l'état prothrombotique est signalé.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la pseudo-maladie de von Willebrand repose uniquement sur le modèle (niveau L5), sans essai ni publication, et le mécanisme du facteur VIII ne répond pas au défaut plaquettaire en cause.
- Les 8 AMM françaises sont valides et le médicament est commercialisé.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le dépistage de sécurité)
- Les données détaillées sur le mécanisme d'action (via DrugBank)
- Une revue de la littérature et des registres d'essais pour les indications les plus plausibles (déficit acquis en facteur de coagulation, hémophilie A avec anomalie vasculaire)
- Une clarification de la situation réglementaire (raisons de l'annulation des AMM, disponibilité éventuelle du produit)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

