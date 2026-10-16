---
layout: default
title: Ravulizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 655
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ravulizumab : nouvelle indication prédite, Neutropénie congénitale sévère autosomique récessive par déficit en G… (niveau de preuve L5). Indication d'origine : Hémoglobinurie paroxystique nocturne"
---

# Ravulizumab
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

# Ravulizumab : De l'Hémoglobinurie Paroxystique Nocturne à la Neutropénie Congénitale Sévère par Déficit en G6PC3

## Résumé en Une Phrase

Ravulizumab est un inhibiteur du complément C5 à longue durée d'action, initialement utilisé pour le traitement de l'hémoglobinurie paroxystique nocturne.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **neutropénie congénitale sévère autosomique récessive par déficit en G6PC3**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction : elle repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémoglobinurie paroxystique nocturne (texte d'indication des AMM non disponible ; source : graphe de connaissances) |
| Nouvelle Indication Prédite | Neutropénie congénitale sévère autosomique récessive par déficit en G6PC3 |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (0 valide, 2 annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, ravulizumab est un inhibiteur du composant C5 du complément à longue durée d'action. Son efficacité dans l'hémoglobinurie paroxystique nocturne, une maladie d'hémolyse médiée par le complément, est établie.

Aucun lien mécanistique direct n'est établi avec la neutropénie par déficit en G6PC3. Cette maladie résulte d'un défaut de la sous-unité catalytique de la glucose-6-phosphatase, qui entraîne une apoptose des neutrophiles et un stress du réticulum endoplasmique. L'inhibition terminale du complément ne cible pas cette physiopathologie. Le score élevé du modèle est une inférence issue du graphe de connaissances, sans confirmation clinique ni bibliographique.

Les autres prédictions du modèle ne sont pas mieux étayées. Elles concernent d'autres neutropénies congénitales (dont les formes par déficit en CXCR2 et liées à l'X), l'hématopoïèse cyclique, l'hyperoxalurie primitive, la pseudo-maladie de von Willebrand, le déficit immunitaire par déficit en p14, un trouble de la libération plaquettaire et l'anémie mégaloblastique. Pour la plupart, aucun lien mécanistique avec l'inhibition de C5 n'est connu. Pour l'hyperoxalurie primitive, seul un lien indirect et spéculatif est évoqué.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64265627 | ULTOMIRIS 1100 mg/11 mL (ALEXION EUROPE), statut : annulée | Solution à diluer pour perfusion | Non renseignée |
| 61808523 | ULTOMIRIS 300 mg/3 mL (ALEXION EUROPE), statut : annulée | Solution à diluer pour perfusion | Non renseignée |

## Considérations de Sécurité

- **Contre-indication issue du graphe de connaissances** : infection à méningocoque (donnée issue des relations médicament-maladie du graphe, et non du texte de la notice).
- **Interactions médicamenteuses** : 4 interactions de niveau mineur, toutes avec des immunoglobulines G humaines (voie intraveineuse, sous-cutanée, intramusculaire, et intraveineuse et sous-cutanée).
- **Point de vigilance lié à la classe** : l'inhibition de C5 augmente le risque d'infections, notamment par des bactéries encapsulées. Ce risque est particulièrement préoccupant chez des patients déjà neutropéniques ou immunodéficients.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai ni publication ne la soutient, et aucun lien mécanistique plausible n'est établi.
- Le risque infectieux lié à l'inhibition de C5 est défavorable dans un contexte de neutropénie.
- Les AMM françaises sont toutes annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Une justification mécanistique ou des données précliniques reliant l'inhibition de C5 à la maladie ciblée
- Une revue de la littérature et des registres d'essais pour confirmer l'absence ou l'existence de preuves
- La clarification du statut réglementaire en France (AMM annulées) et de la compatibilité des voies d'administration
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

