---
layout: default
title: Susoctocog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
---

# Susoctocog Alfa
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

# Susoctocog alfa : De l'hémophilie A acquise au trouble de la libération plaquettaire primaire

## Résumé en Une Phrase

Susoctocog alfa (Obizur) est un facteur VIII recombinant de séquence porcine, dépourvu de domaine B. Il est commercialisé pour traiter les épisodes hémorragiques de l'hémophilie A acquise.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble de la libération plaquettaire primaire**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémophilie A acquise (usage commercialisé d'Obizur ; le texte d'indication de l'ANSM n'est pas renseigné dans les données) |
| Nouvelle Indication Prédite | Trouble de la libération plaquettaire primaire (*primary release disorder of platelets*) |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances établies, susoctocog alfa remplace le facteur VIII manquant ou neutralisé dans la cascade de la coagulation. Sa séquence porcine réagit peu avec les anticorps anti-FVIII humains, ce qui explique son efficacité dans l'hémophilie A acquise.

**Cette prédiction n'est pas plausible sur le plan mécanistique.** Le trouble de la libération plaquettaire est un défaut primaire de la fonction plaquettaire, à savoir la sécrétion des granules. Un apport de FVIII ne corrige pas ce défaut. Le score TxGNN très élevé s'explique probablement par un artefact de proximité dans le graphe : le modèle rapproche des maladies hémorragiques appartenant au même groupe, sans lien pharmacologique réel.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65982247 | OBIZUR 500 U, poudre et solvant pour solution injectable (BAXALTA INNOVATIONS, Autriche) | Poudre et solvant pour solution injectable | Non renseignée dans les données |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans la base interrogée.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Cette prédiction repose uniquement sur le modèle (L5). Elle n'a ni essai clinique, ni publication, ni justification mécanistique, car le FVIII n'agit pas sur un défaut plaquettaire.
- À titre d'information, dans le même dossier, deux prédictions sont soutenues par la littérature (niveau L3, « Proceed with Guardrails ») : l'hémophilie (rang 4) et le déficit acquis en facteur de coagulation (rang 5). Elles correspondent toutefois à l'hémophilie A acquise, c'est-à-dire à l'usage déjà commercialisé, et non à un véritable repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Le RCP/la notice de l'ANSM (mises en garde, contre-indications), dont l'absence bloque le criblage de sécurité
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Le texte d'indication approuvée de l'AMM 65982247
- Des données précliniques ou cliniques sur les troubles plaquettaires, qui ne sont pas attendues au vu du mécanisme

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

