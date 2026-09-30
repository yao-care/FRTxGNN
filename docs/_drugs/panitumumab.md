---
layout: default
title: Panitumumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 230
evidence_level: L5
indication_count: 2
---

# Panitumumab
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

# Panitumumab : D'une Indication Oncologique Non Renseignée à l'Ostéoporose Médicamenteuse

## Résumé en Une Phrase

Panitumumab est un anticorps monoclonal entièrement humain dirigé contre l'EGFR (récepteur du facteur de croissance épidermique). C'est un médicament oncologique administré par voie systémique, et l'indication originale n'est pas renseignée dans les données reçues.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**ostéoporose médicamenteuse**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Ostéoporose médicamenteuse |
| Score de Prédiction TxGNN | 99,13 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, panitumumab est un anticorps monoclonal anti-EGFR entièrement humain. Sa cible pourrait être mécanistiquement liée à l'os, mais cela reste à démontrer.

La signalisation de l'EGFR intervient dans la régulation des ostéoblastes et des ostéoclastes. Un effet osseux est donc biologiquement plausible.

**Le sens de l'effet reste cependant incertain.** L'inhibition de l'EGFR peut provoquer une hypomagnésémie et une hypocalcémie, ce qui pourrait dégrader la santé osseuse au lieu de traiter l'ostéoporose. Le score TxGNN (0,991) provient uniquement d'une prédiction par graphe de connaissances, sans essai ni publication à l'appui dans les données fournies. La compatibilité de la voie d'administration n'a pas non plus été évaluée.

Une seconde indication est prédite : la **rétinopathie diabétique non proliférante sévère** (score 99,05 %, niveau L5, Hold). Le lien mécanistique est concevable, mais le traitement standard cible le VEGF et aucune donnée ne soutient une approche anti-EGFR. Panitumumab a par ailleurs des toxicités oculaires et cutanées connues, et aucun usage intravitréen ou ophtalmique n'est décrit.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66403621 | VECTIBIX 20 mg/ml (AMGEN EUROPE) | Solution à diluer pour perfusion | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (anticorps monoclonal anti-EGFR) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Magnésium et calcium sériques (risque d'hypomagnésémie et d'hypocalcémie lié à l'inhibition de l'EGFR) ; surveillance cutanée et oculaire |
| Protection de Manipulation | Veuillez consulter la notice |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune mise en garde, contre-indication ni interaction médicamenteuse n'est disponible dans les données reçues.

À titre d'orientation, l'analyse mécanistique signale des risques connus de la classe anti-EGFR, à confirmer avec la notice :
- **Troubles électrolytiques** : hypomagnésémie et hypocalcémie, particulièrement préoccupantes dans un contexte osseux.
- **Toxicités oculaires et cutanées** : pertinentes pour toute réflexion sur la rétinopathie diabétique.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Les deux indications prédites reposent uniquement sur le score du modèle (niveau L5), sans essai ni publication. Le sens de l'effet est incertain, et le risque d'hypocalcémie plaide même contre l'ostéoporose. Les données de sécurité de la notice ANSM manquent, ce qui bloque le passage à l'étape de dépistage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde et contre-indications)
- Obtenir les données détaillées sur le mécanisme d'action (MOA) via DrugBank
- Renseigner l'indication approuvée du produit
- Mener une recherche ciblée dans la littérature sur l'EGFR et le métabolisme osseux, ainsi que sur l'EGFR et la rétinopathie diabétique
- Évaluer la compatibilité de la voie d'administration (perfusion systémique) avec les indications prédites
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

