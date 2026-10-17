---
layout: default
title: Aflibercept
parent: Prédiction du modèle uniquement (L5)
nav_order: 29
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Aflibercept : nouvelle indication prédite, Ésotropie (niveau de preuve L5). Indication d'origine : Métastases d'une tumeur maligne du côlon"
monitor_inn: "AFLIBERCEPT"
predicted_indications: ["esotropia"]
---

# Aflibercept
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Aflibercept : Du Néoplasme du Côlon Métastatique et des Maladies Rétiniennes à l'Ésotropie

## Résumé en Une Phrase

Aflibercept est une protéine de fusion qui piège le VEGF, initialement utilisée pour le traitement du cancer colorectal métastatique et de maladies rétiniennes néovasculaires (dégénérescence maculaire, œdème maculaire diabétique, occlusion de l'artère rétinienne).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**ésotropie**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Métastases d'une tumeur maligne du côlon ; dégénérescence maculaire ; occlusion de l'artère rétinienne ; œdème maculaire diabétique (selon le graphe de connaissances, le texte des indications des AMM françaises n'étant pas renseigné) |
| Nouvelle Indication Prédite | Ésotropie |
| Score de Prédiction TxGNN | 99,38 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Toutes les AMM sont annulées |
| Nombre d'AMM | 8 (0 valide, 8 annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les informations connues, l'aflibercept est un piège à VEGF-A, VEGF-B et PlGF. Son efficacité dans les maladies vasculaires rétiniennes et dans le cancer colorectal métastatique repose sur l'inhibition de l'angiogenèse et de la perméabilité vasculaire.

Aucune voie mécanistique directe ne relie l'inhibition du VEGF à l'ésotropie. L'ésotropie est avant tout un trouble de l'alignement oculaire, lié aux muscles extraoculaires, au contrôle neural ou à des facteurs réfractifs/accommodatifs. Un lien indirect est possible : les anti-VEGF sont utilisés dans des maladies rétiniennes comme la rétinopathie du prématuré, dans laquelle le strabisme est une séquelle fréquente. Le score élevé du modèle pourrait donc refléter une simple co-occurrence de maladies dans le graphe et non un véritable effet thérapeutique.

Cette hypothèse n'est pas vérifiée. De plus, des injections intravitréennes d'anti-VEGF ont été associées à la survenue de strabisme dans certains contextes pédiatriques, ce qui va à l'encontre d'un rôle thérapeutique. La similarité avec les indications d'origine reste à évaluer.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 8 AMM sont annulées ; le texte des indications approuvées n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 60089217 | ZALTRAP 25 mg/ml | Solution à diluer pour perfusion | Annulée |
| 67140625 | EYLEA 114,3 mg/mL (seringue préremplie) | Solution injectable | Annulée |
| 69166985 | EYLEA 114,3 mg/mL | Solution injectable | Annulée |
| 61858889 | PAVBLU 40 mg/mL (seringue préremplie) | Solution injectable | Annulée |
| 69613703 | EYLEA 40 mg/mL (seringue préremplie) | Solution injectable | Annulée |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 78 interactions recensées. Parmi les principales :
  - **Majeures** : défériprone, samarium (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribine, clozapine.
  - **Modérées** : chlorure de strontium Sr-89, roflumilast, chloramphénicol (y compris ophtalmique), zidovudine, alefacept, alemtuzumab, anakinra, azathioprine, canakinumab, ainsi que certains vaccins (tétanos, charbon, choléra vivant).

Veuillez consulter la notice pour les mises en garde et contre-indications.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Aucun lien mécanistique direct n'est identifié, et un signal de strabisme après anti-VEGF chez l'enfant plaide plutôt contre un effet thérapeutique. Toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Obtenir les données sur le mécanisme d'action via DrugBank
- Réaliser une revue systématique de la littérature sur anti-VEGF et strabisme/ésotropie, y compris les signaux de sécurité pédiatriques
- Évaluer la compatibilité des voies d'administration et la similarité avec les indications d'origine
- Clarifier le statut réglementaire actuel (AMM annulées) et la disponibilité réelle du produit en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

