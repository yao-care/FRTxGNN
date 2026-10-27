---
layout: default
title: Danaparoid
parent: Prédiction du modèle uniquement (L5)
nav_order: 211
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Danaparoid : nouvelle indication prédite, Thrombasthénie de Glanzmann (niveau de preuve L5). Indication d'origine : Non renseignée dans l'AMM disponible"
monitor_inn: "danaparoid"
predicted_indications: ["Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "Scott syndrome"]
---

# Danaparoid
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Danaparoïde : D'un anticoagulant à la thrombasthénie de Glanzmann
{: .text-alpha }

## Résumé en une phrase

Le danaparoïde est un héparinoïde anticoagulant (mélange d'héparane sulfate, de dermatane sulfate et de chondroïtine sulfate). Le texte de son indication d'origine n'est pas renseigné dans les données compilées pour ce rapport.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **thrombasthénie de Glanzmann**, mais **aucun essai clinique et aucune publication** ne soutiennent cette direction. Le mécanisme est même plutôt défavorable.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans l'AMM disponible |
| Nouvelle indication prédite | Thrombasthénie de Glanzmann |
| Score de prédiction TxGNN | 99,88 % |
| Niveau de preuve | L5 |
| Statut de marché en France | Autorisation annulée (aucune AMM valide) |
| Nombre d'AMM | 1 |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les sources compilées. D'après les connaissances générales, le danaparoïde agit surtout par une activité anti-Xa médiée par l'antithrombine. C'est un anticoagulant.

La thrombasthénie de Glanzmann est une maladie hémorragique due à un déficit ou un dysfonctionnement de l'intégrine plaquettaire αIIbβ3. Un anticoagulant devrait aggraver le risque hémorragique, et non l'améliorer. Il n'existe donc pas de lien mécanistique plausible entre l'usage d'origine et cette nouvelle indication.

Le score élevé (99,88 %) reflète vraisemblablement un artefact du graphe de connaissances, par exemple une association partagée avec des nœuds d'hémostase ou de coagulation. Il ne s'appuie sur aucun rationnel thérapeutique. Les cinq autres prédictions suivent la même logique, avec les mêmes réserves :

| Rang | Maladie prédite | Score TxGNN | Évaluation |
|------|------|------|------|
| 2 | Trouble primaire de la libération plaquettaire | 99,88 % | Défaut plaquettaire non corrigé par l'anticoagulation ; risque hémorragique accru |
| 3 | Pseudo-maladie de von Willebrand | 99,83 % | Aucun effet correcteur sur l'interaction GPIbα-VWF ; risque hémorragique accru |
| 4 | Diathèse hémorragique par défaut d'un récepteur du collagène | 99,30 % | Le médicament ne cible pas ces récepteurs ; aggravation attendue du saignement |
| 5 | Trouble hémorragique lié à une thrombopénie constitutionnelle | 99,30 % | L'usage dans la thrombopénie induite par l'héparine (affection acquise et prothrombotique) ne se transpose pas |
| 6 | Syndrome de Scott | 99,28 % | Aggrave le défaut d'activité procoagulante au lieu de le corriger |

## Preuves d'essais cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la littérature

Aucune littérature associée n'est disponible actuellement.

## Informations de marché en France

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Indication approuvée |
|---------|------|------|-----------|
| 69449143 | ORGARAN 750 U.I. anti Xa/0,6 ml, solution injectable en ampoule (VIATRIS SANTE) | Solution injectable | Non renseignée (AMM annulée) |

## Considérations de sécurité

**Interactions médicamenteuses** : 139 interactions ont été recensées. Parmi les exemples signalés, plusieurs sont de niveau **majeur**, avec un risque hémorragique additif attendu :
- Acide acétylsalicylique
- Ibuprofène
- Kétorolac
- Abciximab
- Alteplase
- Acalabrutinib
- Déférasirox
- Trastuzumab emtansine
- Ibritumomab tiuxétan
- Tositumomab (I-131)

Des interactions de niveau **modéré** sont également signalées, notamment avec la fenfluramine, la sibutramine, le célécoxib, l'amiloride, l'aliskirène, le sugammadex, le diclofénac topique et les iodures I-123 et I-131.

**Point d'attention** : la combinaison d'un anticoagulant et d'une maladie hémorragique constitue en soi une contre-indication logique. Elle est détaillée dans l'analyse mécanistique ci-dessus.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui ne sont pas disponibles dans les données compilées.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Le mécanisme anticoagulant est opposé au besoin thérapeutique (risque d'aggraver les saignements), et l'AMM française est annulée.
- Les lacunes de données sur les mises en garde de la notice (bloquantes) et sur le mécanisme d'action empêchent de passer au criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Disposer d'un rationnel biologique crédible expliquant comment un anticoagulant pourrait être bénéfique dans un trouble hémorragique plaquettaire. En l'absence d'un tel rationnel, il est recommandé de ne pas poursuivre cette piste.
- Clarifier l'indication d'origine de l'AMM annulée.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

