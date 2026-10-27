---
layout: default
title: Remimazolam
parent: Prédiction du modèle uniquement (L5)
nav_order: 660
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Remimazolam : nouvelle indication prédite, Insomnie (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées"
monitor_inn: "remimazolam"
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium"]
---

# Remimazolam
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Remimazolam : De la sédation procédurale à l'insomnie
{: .text-alpha }

## Résumé en Une Phrase

Remimazolam est une benzodiazépine d'action ultra-courte, administrée par voie intraveineuse pour la sédation procédurale et l'anesthésie.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**insomnie**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Insomnie |
| Score de Prédiction TxGNN | 99,91 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | AMM annulée uniquement |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de données consultée. Sur la base des connaissances pharmacologiques générales, le remimazolam est un modulateur allostérique positif du récepteur GABA-A, comme les benzodiazépines hypnotiques établies. Un lien mécanistique avec l'insomnie est donc plausible.

Cependant, plusieurs éléments limitent cette plausibilité. Son hydrolyse très rapide par les estérases tissulaires (principalement la carboxylestérase 1) donne une durée d'action trop courte pour maintenir le sommeil. De plus, il n'existe que sous forme intraveineuse, destinée à la sédation procédurale et à l'anesthésie. Le score très élevé de TxGNN (99,91 %) reflète probablement une similarité de classe avec les hypnotiques GABAergiques plutôt qu'une preuve propre à ce médicament.

Une seconde indication prédite, le **delirium de sevrage alcoolique** (score 99,30 %), est également plausible sur le plan biologique : les benzodiazépines sont le traitement de référence du sevrage alcoolique. L'apparition et la disparition rapides de l'effet pourraient permettre une titration fine en réanimation, mais cela reste théorique. Ce syndrome nécessite souvent de fortes doses cumulées sur plusieurs jours, et une demi-vie très courte pourrait provoquer des symptômes de rupture. La population est en outre à risque (dépression respiratoire, instabilité hémodynamique). Cette prédiction est aussi classée L5, avec une décision Hold.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68722379 | BYFAVO 20 mg, poudre pour solution injectable (PAION PHARMA, Allemagne) | Poudre pour solution injectable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 54 interactions ont été identifiées. Parmi celles présentées dans les données compilées :
  - **Majeures** : morphine, morphine liposomale, codéine, hydrocodone (risque d'addition des effets dépresseurs du système nerveux central et respiratoires).
  - **Modérées** : bupropion, dronabinol, nabilone, métoclopramide, opium, sibutramine, éthanol, diazoxide, phentolamine, prométhazine, disulfirame, lidocaïne, chlorphéniramine, cétirizine, azélastine (nasale), dextrométhorphane.

Les informations sur les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication. L'AMM française est annulée, et la durée d'action ultra-courte ainsi que la voie exclusivement intraveineuse rendent l'usage dans l'insomnie peu réaliste. Les données de sécurité de la notice sont absentes, ce qui bloque le criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice auprès de l'ANSM (lacune bloquante).
- Compléter les données sur le mécanisme d'action (DrugBank).
- Rechercher des études précliniques ou cliniques sur l'insomnie et le delirium de sevrage alcoolique.
- Évaluer la compatibilité de la voie d'administration (intraveineuse uniquement) et de la pharmacocinétique avec ces indications.
- Clarifier le statut réglementaire en France (AMM annulée) et l'indication d'origine.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

