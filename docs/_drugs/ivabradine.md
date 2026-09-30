---
layout: default
title: Ivabradine
parent: Prédiction du modèle uniquement (L5)
nav_order: 162
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Ivabradine : Du Blocage des Canaux HCN Cardiaques à l'Hypertrichose

## Résumé en Une Phrase

L'ivabradine est un médicament commercialisé en France qui bloque les canaux HCN (courant cardiaque If).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertrichose**, avec un score élevé (99,79 %).
Cette prédiction n'est soutenue par **aucun essai clinique** et **aucune publication** : elle repose uniquement sur le modèle, et aucun lien mécanistique plausible n'a été identifié.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Hypertrichose |
| Score de Prédiction TxGNN | 99,79 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

Le texte de l'indication approuvée n'est pas renseigné dans les données ANSM fournies, l'indication originale n'est donc pas indiquée ici.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. On sait que l'ivabradine bloque les canaux HCN, responsables du courant cardiaque If, qui règle la fréquence du cœur.

Aucun lien connu n'a été trouvé entre ce mécanisme et la croissance des poils. La biologie de canaux ioniques voisins, comme les canaux K-ATP dans l'hypertrichose du syndrome de Cantú, ne fait pas intervenir les canaux HCN. Le score élevé est donc probablement un artefact du graphe de connaissances et non une preuve indépendante.

Les autres prédictions du modèle sont tout aussi peu étayées : hypertrichose congénitale d'Ambras (liée à la région TRPS1), anomalies génétiques de la tige pilaire, syndromes malformatifs dentaires ou parodontaux, syndromes avec malformation de Dandy-Walker et syndrome néphrogénique d'antidiurèse inappropriée (variants du récepteur V2 de la vasopressine). Aucune n'a de mécanisme plausible avec le blocage des canaux HCN. Plusieurs scores semblent refléter la proximité avec le nœud « hypertrichose » du graphe.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

Pour information, 20 publications ont été retrouvées pour une autre prédiction (malformations avec composante dentaire ou parodontale). Elles traitent de la parodontite en général et ne mentionnent ni l'ivabradine ni les canaux HCN. Elles ne constituent pas une preuve pour ce médicament.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 63501124 | PROCORALAN 7,5 mg | Comprimé pelliculé | Les Laboratoires Servier |
| 65486532 | IVABRADINE ALTER 7,5 mg | Comprimé | Laboratoires Alter |
| 61952527 | PROCORALAN 5 mg | Comprimé pelliculé | Les Laboratoires Servier |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est de niveau L5 : score du modèle uniquement, sans essai, sans publication pertinente et sans mécanisme plausible.
- Les données de sécurité de la notice ANSM manquent et bloquent le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications, indications approuvées).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Rechercher une éventuelle piste biologique spécifique reliant les canaux HCN à la croissance pilaire, avant tout investissement supplémentaire.
- Une fois ces éléments réunis, reprendre l'évaluation, sachant que le modèle seul ne justifie pas de progresser.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

