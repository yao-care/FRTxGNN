---
layout: default
title: Lipegfilgrastim
parent: Prédiction du modèle uniquement (L5)
nav_order: 454
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Lipegfilgrastim : nouvelle indication prédite, Trouble primaire de la libération plaquettaire (primary release disor… (niveau de preuve L5). Indication d'origine : Non disponible dans les données com…"
monitor_inn: "LIPEGFILGRASTIM"
predicted_indications: ["primary release disorder of platelets", "severe nonproliferative diabetic retinopathy", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "diabetic retinopathy"]
---

# Lipegfilgrastim
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

## Lipegfilgrastim : D'un facteur de croissance des neutrophiles à un défaut primaire de sécrétion plaquettaire (prédiction non étayée)
{: .text-alpha }

## Résumé en Une Phrase

Lipegfilgrastim est un analogue pégylé du G-CSF (facteur de stimulation des colonies de granulocytes), commercialisé en France sous le nom LONQUEX, qui stimule la production des neutrophiles.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble primaire de la libération plaquettaire**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible dans les données compilées (texte d'indication vide pour les deux AMM) |
| Nouvelle Indication Prédite | Trouble primaire de la libération plaquettaire (primary release disorder of platelets) |
| Score de Prédiction TxGNN | 0,9993 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, lipegfilgrastim est un analogue pégylé du G-CSF. Il agit sur le récepteur du G-CSF et stimule la prolifération et la différenciation de la lignée neutrophile.

La relation avec la nouvelle indication est **peu plausible sur le plan mécanistique**. Les troubles de la libération plaquettaire sont des défauts qualitatifs de la fonction plaquettaire (granules de sécrétion), et non un déficit en neutrophiles. Aucun lien connu n'existe entre la voie du G-CSF et ce type de défaut.

Le score élevé du modèle (0,9993) provient uniquement d'une prédiction du modèle TxGNN (apprentissage profond). Il ne doit pas être interprété comme une preuve d'efficacité, d'autant que l'absence de données sur le mécanisme d'action d'origine limite l'interprétation de cette prédiction.

### Autres indications prédites (pour information)

| Rang | Maladie prédite | Score TxGNN | Niveau de preuve | Commentaire |
|------|------|------|------|------|
| 2 | Rétinopathie diabétique non proliférative sévère | 0,9991 | L5 | Lien théorique via la mobilisation de progéniteurs endothéliaux ; risque théorique de néovascularisation pathologique, sens de l'effet incertain |
| 3 | Pseudo-maladie de von Willebrand | 0,9991 | L5 | Défaut de GPIbα plaquettaire ; aucun mécanisme plausible |
| 4 | Thrombasthénie de Glanzmann | 0,9991 | L5 | Déficit en intégrine αIIbβ3 ; non adressé par la voie du G-CSF |
| 5 | Rétinopathie diabétique | 0,9975 | L5 | Lien spéculatif ; préoccupation de sécurité en cas de maladie proliférative |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 66910592 | LONQUEX 6 mg/0,6 mL, solution injectable | Solution injectable | Non renseignée | Active |
| 64198267 | LONQUEX 6 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée | Active |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et le lien mécanistique avec les troubles plaquettaires n'est pas plausible.
- Les deux AMM françaises sont annulées et les données de sécurité de la notice sont absentes, ce qui bloque toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (téléchargement et analyse du document PDF)
- Compléter les données sur le mécanisme d'action (par exemple via DrugBank)
- Confirmer l'indication originale approuvée, absente des données actuelles
- Réaliser une revue de la littérature et des registres d'essais pour toute indication retenue ; une évaluation préclinique serait nécessaire avant toute avancée
- Pour les indications ophtalmologiques (rétinopathie diabétique), évaluer en priorité le risque pro-angiogénique avant toute étude
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

