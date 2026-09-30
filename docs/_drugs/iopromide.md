---
layout: default
title: Iopromide
parent: Prédiction du modèle uniquement (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
---

# Iopromide
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

# Iopromide : D'un Produit de Contraste Iodé à la Susceptibilité à l'Arthrose

## Résumé en Une Phrase

L'iopromide est un produit de contraste radiologique iodé non ionique, commercialisé en France sous le nom d'Ultravist pour l'imagerie diagnostique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **susceptibilité à l'arthrose**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction.
Il s'agit d'une sortie de graphe de connaissances, sans base clinique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Susceptibilité à l'arthrose (osteoarthritis susceptibility) |
| Score de Prédiction TxGNN | 99,57 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 4 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. L'iopromide est un agent de contraste iodé non ionique, utilisé comme aide à l'imagerie. Il n'a pas d'action pharmacologique connue sur les tissus articulaires ni sur la susceptibilité génétique à l'arthrose.

Aucun lien mécanistique n'a été identifié entre l'indication d'origine (l'imagerie diagnostique) et la nouvelle indication. Le score élevé du modèle (99,57 %) reflète probablement des associations dans le graphe de connaissances, notamment la présence fréquente des produits de contraste dans la littérature d'imagerie ostéoarticulaire. Il ne traduit pas un effet thérapeutique. Cette prédiction doit donc être considérée comme peu plausible en l'état.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Fabricant |
|---------|------|------|------|
| 68373358 | ULTRAVIST 300 (300 mg d'iode/mL), solution injectable | Solution injectable | Bayer Healthcare |
| 62729413 | ULTRAVIST 370 (370 mg d'iode/mL), solution injectable | Solution injectable | Bayer Healthcare |
| 65027575 | ULTRAVIST 370 (370 mg d'iode/mL), solution injectable en seringue préremplie pour injecteur automatique | Solution injectable | Bayer Healthcare |
| 60385522 | ULTRAVIST 300 (300 mg d'iode/mL), solution injectable en seringue préremplie pour injecteur automatique | Solution injectable | Bayer Healthcare |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique, sans publication et sans mécanisme plausible.
- Parmi les autres prédictions du modèle, l'arthrose (2 publications) et la polyarthrite rhumatoïde (1 publication) sont documentées uniquement comme des usages diagnostiques en imagerie (blocs nerveux guidés par scanner, mesure du cartilage par IRM, TDM injecté), et non comme des traitements.
- Un cas publié d'événement vaso-occlusif cérébral après un contraste de faible osmolarité chez un patient drépanocytaire constitue un possible signal de sécurité. Il va à l'encontre d'un repositionnement dans les hémoglobinopathies.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour tout dépistage de sécurité).
- Compléter les données sur le mécanisme d'action (par exemple via l'API DrugBank).
- Identifier un rationnel biologique crédible avant tout investissement supplémentaire. En l'absence de lien mécanistique et de preuves cliniques, il est recommandé de ne pas poursuivre cette piste.

*Ce rapport est fourni à titre de référence pour la recherche et ne constitue pas un avis médical. Tout candidat au repositionnement nécessite une validation clinique avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

