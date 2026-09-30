---
layout: default
title: Guselkumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

# Guselkumab : De l'indication d'origine (non renseignée) à l'ostéoporose médicamenteuse

## Résumé en Une Phrase

Guselkumab est un anticorps monoclonal dirigé contre l'interleukine-23 (IL-23), commercialisé en France sous le nom TREMFYA. Les données fournies ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être utile dans l'**ostéoporose médicamenteuse**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle seule.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données d'AMM disponibles |
| Nouvelle Indication Prédite | Ostéoporose médicamenteuse (drug-induced osteoporosis) |
| Score de Prédiction TxGNN | 99,84 % (rang 1713) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, guselkumab fait partie de la classe des inhibiteurs de la sous-unité p19 de l'IL-23. Son efficacité est établie dans plusieurs maladies inflammatoires à médiation immunitaire, et mécanistiquement il pourrait être applicable à d'autres pathologies dans lesquelles l'IL-23 joue un rôle.

L'IL-23 a été évoquée dans le remodelage osseux, ce qui donne un point d'appui théorique à la prédiction. En revanche, les données fournies ne documentent **aucun lien direct** entre le blocage de l'IL-23 et l'ostéoporose d'origine médicamenteuse. Le score élevé du modèle (0,998) ne remplace pas une preuve clinique ou expérimentale.

La similarité entre l'indication d'origine et la nouvelle indication ne peut pas être évaluée, faute d'indication d'origine renseignée.

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
| 68372441 | TREMFYA 100 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée |
| 67296108 | TREMFYA 100 mg ONEPRESS, solution injectable en stylo prérempli | Solution injectable | Non renseignée |

Les deux AMM sont détenues par JANSSEN CILAG INTERNATIONAL NV.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données consultées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5). Il n'y a ni essai clinique, ni publication, ni mécanisme documenté reliant l'IL-23 à l'ostéoporose médicamenteuse.
- Les données de sécurité (mises en garde, contre-indications) sont absentes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) et les indications approuvées de chaque AMM.
- Compléter les données de mécanisme d'action via DrugBank.
- Mener une recherche bibliographique ciblée sur l'IL-23 et le métabolisme osseux, y compris les données précliniques.
- Confirmer la plausibilité biologique avant d'envisager toute étude clinique.

**À noter :** dans le même dossier, deux autres indications prédites disposent de preuves solides (niveau L1, « Proceed with Guardrails ») : le **psoriasis** et la **colite ulcéreuse**. Pour le psoriasis, il s'agit d'un usage déjà commercialisé, donc d'une confirmation plutôt que d'un vrai repositionnement. Pour la colite ulcéreuse, il faut vérifier le libellé réglementaire actuel en France.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

