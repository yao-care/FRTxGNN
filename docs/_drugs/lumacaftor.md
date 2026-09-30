---
layout: default
title: Lumacaftor
parent: Prédiction du modèle uniquement (L5)
nav_order: 183
evidence_level: L5
indication_count: 1
---

# Lumacaftor
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Lumacaftor : De la Mucoviscidose à la Lèpre

## Résumé en Une Phrase

Lumacaftor est le composant de la spécialité ORKAMBI, connu de manière générale pour le traitement de la mucoviscidose. Cette indication d'origine ne figure pas dans le dossier fourni et vient de la connaissance pharmacologique générale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **lèpre**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans le dossier (texte d'indication des AMM vide) ; mucoviscidose selon la connaissance générale |
| Nouvelle Indication Prédite | Lèpre |
| Score de Prédiction TxGNN | 99,44 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 5 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances pharmacologiques générales (et non d'après ce dossier), le lumacaftor est un correcteur de la protéine CFTR : il améliore le repliement et l'adressage à la membrane de la protéine F508del-CFTR.

Aucun lien mécanistique direct avec la lèpre n'est étayé par les données fournies. On ne connaît pas d'action du lumacaftor sur *Mycobacterium leprae* ni sur les voies immunitaires de l'hôte impliquées dans la lèpre, comme les axes des réactions de type 1 et de type 2.

Le score TxGNN de 0,994 est une prédiction issue d'un graphe de connaissances uniquement. Il peut refléter une proximité dans le réseau (gènes ou protéines voisins partagés) plutôt qu'une justification biologique validée. Sans chemin traçable dans le graphe, aucun mécanisme ne peut être confirmé. Cette prédiction doit donc être considérée comme une hypothèse à explorer, pas comme un résultat établi.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 66352529 | ORKAMBI 200 mg/125 mg, comprimé pelliculé | Comprimé pelliculé |
| 66209488 | ORKAMBI 150 mg/188 mg, granulés en sachet | Granulés |
| 61962699 | ORKAMBI 100 mg/125 mg, comprimé pelliculé | Comprimé pelliculé |
| 65639871 | ORKAMBI 100 mg/125 mg, granulés en sachet | Granulés |
| 64733894 | ORKAMBI 75 mg/94 mg, granulés en sachet | Granulés |

Titulaire pour les cinq AMM : Vertex Pharmaceuticals (Ireland). Le texte de l'indication approuvée n'est pas renseigné dans les données reçues.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans la base interrogée.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau de preuve L5), sans essai clinique ni publication, et aucun lien mécanistique plausible avec la lèpre n'est démontré. Les données de sécurité issues de la notice de l'ANSM font également défaut, ce qui empêche toute évaluation de sécurité à ce stade.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications)
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via l'API DrugBank)
- Obtenir le chemin explicatif dans le graphe TxGNN pour vérifier si le score correspond à une base biologique réelle
- Rechercher activement des études précliniques ou observationnelles reliant le lumacaftor à la lèpre
- Confirmer l'indication d'origine à partir des textes d'AMM
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

