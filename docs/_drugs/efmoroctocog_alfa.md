---
layout: default
title: Efmoroctocog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
---

# Efmoroctocog Alfa
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

# Efmoroctocog alfa : De l'Hémophilie A à la Pseudo-maladie de von Willebrand

## Résumé en Une Phrase

Efmoroctocog alfa est un facteur VIII de coagulation recombinant fusionné à un fragment Fc, commercialisé en France sous le nom ELOCTA. Il est utilisé dans l'hémophilie A, une indication qui ne figure pas dans les données fournies.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pseudo-maladie de von Willebrand** (de type plaquettaire), mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Pseudo-maladie de von Willebrand |
| Score de Prédiction TxGNN | 99,997 % (rang 113) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 8 |
| Décision Recommandée | Hold |

L'indication originale n'est pas renseignée dans les textes d'AMM fournis (champs vides). L'hémophilie A dans le titre repose sur la connaissance générale du produit et doit être confirmée par la notice ANSM.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les informations connues, efmoroctocog alfa est un facteur VIII recombinant à demi-vie prolongée (fusion Fc), qui apporte le facteur VIII manquant chez les patients hémophiles.

La pseudo-maladie de von Willebrand est un défaut de gain de fonction du récepteur plaquettaire GPIb, qui augmente la fixation du facteur de von Willebrand (VWF). Un apport de facteur VIII ne corrige pas ce défaut plaquettaire. Le taux de facteur VIII peut être secondairement bas à cause de la perte de VWF, mais aucune donnée ne l'étaye ici. Le lien mécanistique est donc faible : le score élevé du graphe reflète probablement la proximité générale des « maladies hémorragiques » plutôt qu'un lien biologique spécifique.

Les autres prédictions du modèle (9 au total) sont toutes au niveau L5, sans essai ni publication. Trois d'entre elles se distinguent :
- **Déficit acquis en facteur de coagulation** (rang 5) : le plus cohérent sur le plan mécanistique, car un déficit acquis en facteur VIII pourrait en théorie relever d'un apport de facteur VIII. En pratique, les inhibiteurs auto-anticorps neutralisent le facteur perfusé et les agents de contournement sont l'approche standard.
- **Hémophilie A avec anomalie vasculaire** (rang 9) : le plus proche biologiquement, mais la relation de cette entité avec l'hémophilie A classique est floue.
- **Purpura thrombotique thrombocytopénique** (rang 10) : le facteur VIII est souvent déjà élevé dans cette maladie, et un apport supplémentaire pourrait aggraver l'état prothrombotique. Il s'agit d'un signal de sécurité, pas d'un argument thérapeutique.

## Informations de Marché en France

8 AMM au total ; les 5 principales sont listées ci-dessous. Les textes d'indication approuvée sont vides dans les données.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 69349794 | ELOCTA 1500 UI | Poudre et solvant pour solution injectable | Swedish Orphan Biovitrum International (Suède) |
| 60602449 | ELOCTA 750 UI | Poudre et solvant pour solution injectable | Swedish Orphan Biovitrum International (Suède) |
| 68853909 | ELOCTA 2000 UI | Poudre et solvant pour solution injectable | Swedish Orphan Biovitrum International (Suède) |
| 69009069 | ELOCTA 1000 UI | Poudre et solvant pour solution injectable | Swedish Orphan Biovitrum International (Suède) |
| 64440763 | ELOCTA 250 UI | Poudre et solvant pour solution injectable | Swedish Orphan Biovitrum International (Suède) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication, et le mécanisme est peu plausible : le défaut se situe au niveau du récepteur plaquettaire GPIb, pas du facteur VIII.
- Les données de sécurité et de mécanisme d'action sont absentes, ce qui bloque le passage à l'étape de sécurité (S1).

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice ANSM (mises en garde, contre-indications, indications approuvées)
- Obtenir le mécanisme d'action via l'API DrugBank
- Rechercher activement des essais cliniques et de la littérature pour la pseudo-maladie de von Willebrand
- Clarifier l'entité « hémophilie A avec anomalie vasculaire » (rang 9) et le déficit acquis en facteur de coagulation (rang 5), les deux pistes les plus cohérentes biologiquement
- Écarter le purpura thrombotique thrombocytopénique (rang 10) en raison du risque prothrombotique

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

