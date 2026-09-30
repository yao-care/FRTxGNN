---
layout: default
title: Siltuximab
parent: Prédiction du modèle uniquement (L5)
nav_order: 282
evidence_level: L5
indication_count: 8
---

# Siltuximab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

# Siltuximab : De la Maladie de Castleman Multicentrique au Mastocytome Extracutané

## Résumé en Une Phrase

Siltuximab est un anticorps monoclonal chimérique dirigé contre l'interleukine-6 (IL-6). Il est établi dans la maladie de Castleman multicentrique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **mastocytome extracutané**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction, qui reste purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Castleman multicentrique (d'après le rationnel mécanistique du dossier ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Mastocytome extracutané |
| Score de Prédiction TxGNN | 99,64 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, siltuximab neutralise l'IL-6, une cytokine pro-inflammatoire. Son efficacité dans la maladie de Castleman multicentrique est reconnue, et mécanistiquement il pourrait être applicable à des maladies où l'IL-6 est élevée.

Dans les troubles mastocytaires, l'IL-6 est effectivement élevée. Toutefois, rien ne démontre que l'IL-6 soit le moteur de la croissance d'un mastocytome. Le lien reste donc spéculatif : il repose sur la seule prédiction du modèle, sans donnée directe. L'indication originale (trouble lymphoprolifératif) et la nouvelle indication (prolifération mastocytaire) n'ont pas, à ce stade, de similarité évaluée.

À titre de contexte, parmi les autres prédictions du modèle, le sarcome de Kaposi (rang 5) est la seule pour laquelle un lien mécanistique indirect plausible est décrit (IL-6 viral codée par le HHV-8/KSHV, biologie proche de la maladie de Castleman associée au KSHV). Il n'existe pas non plus de donnée directe d'efficacité pour cette indication.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60622302 | SYLVANT 100 mg | Poudre pour solution à diluer pour perfusion | Non précisée dans les données fournies |
| 63846800 | SYLVANT 400 mg | Poudre à diluer pour solution pour perfusion | Non précisée dans les données fournies |

Les deux AMM sont détenues par Recordati Netherlands.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5). Aucun essai, aucune publication et aucune donnée mécanistique directe ne la soutient, et le rôle de l'IL-6 dans la croissance du mastocytome n'est pas démontré.
- Les données de sécurité issues de la notice ANSM manquent et bloquent le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications), point bloquant.
- Compléter les données sur le mécanisme d'action (MOA) via DrugBank.
- Obtenir le texte des indications approuvées des deux AMM.
- Rechercher des données précliniques ou cliniques sur l'IL-6 dans le mastocytome extracutané.
- Étudier en priorité le sarcome de Kaposi, qui présente le lien mécanistique le plus plausible parmi les prédictions.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

