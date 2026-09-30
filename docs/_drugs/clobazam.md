---
layout: default
title: Clobazam
parent: Prédiction du modèle uniquement (L5)
nav_order: 81
evidence_level: L5
indication_count: 10
---

# Clobazam
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

# Clobazam : Nouvelle indication prédite, le syndrome d'épilepsie liée à une infection fébrile (FIRES)

## Résumé en Une Phrase

Le clobazam est une benzodiazépine 1,5 utilisée comme antiépileptique et commercialisée en France (4 AMM). Le texte des indications autorisées n'est pas renseigné dans les données disponibles.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome d'épilepsie liée à une infection fébrile (FIRES)**. Aucun essai clinique n'est enregistré et seulement **2 publications** existent (une série de cas et un cas clinique). Aucune d'elles ne porte sur le clobazam, donc le soutien est indirect.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Syndrome d'épilepsie liée à une infection fébrile (FIRES) |
| Score de Prédiction TxGNN | 99,82 % |
| Niveau de Preuve | L4 (preuves indirectes uniquement, aucune donnée spécifique au clobazam) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 4 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances générales, le clobazam est une benzodiazépine 1,5 qui agit comme modulateur allostérique positif des récepteurs GABA-A. Il renforce ainsi l'inhibition neuronale, ce qui explique son usage dans les épilepsies.

Le FIRES est une forme d'état de mal épileptique réfractaire d'apparition récente (NORSE) qui touche des enfants auparavant en bonne santé. Les antiépileptiques conventionnels échouent souvent, et les patients nécessitent des cycles répétés de coma pharmacologique (midazolam, barbituriques). Une modulation GABA-A est donc mécanistiquement plausible.

Cette plausibilité reste toutefois théorique. Les deux articles retrouvés traitent du lorazépam entéral (sevrage du midazolam) et du pérampanel (réduction de la dépendance aux barbituriques), pas du clobazam. Le score élevé du modèle repose donc surtout sur des effets de classe.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Série de cas (cohorte) | Epileptic Disord | Le lorazépam entéral est une stratégie de sevrage prometteuse chez les patients FIRES dépendants du midazolam. Cette étude ne concerne pas le clobazam. |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Cas clinique | Cureus | Chez un garçon de 13 ans, le pérampanel aurait pu réduire la dépendance aux barbituriques dans le FIRES. Cette étude ne concerne pas le clobazam. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 62905911 | URBANYL 10 mg, comprimé sécable | Comprimé sécable | ATNAHS PHARMA FRANCE |
| 65899602 | LIKOZAM 1 mg/ml, suspension buvable | Suspension buvable | TAW PHARMA (Irlande) |
| 64630403 | URBANYL 5 mg, gélule | Gélule | ATNAHS PHARMA FRANCE |
| 63470312 | URBANYL 20 mg, comprimé | Comprimé | ATNAHS PHARMA FRANCE |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Il n'existe aucun essai clinique et aucune publication spécifique au clobazam dans le FIRES. La prédiction repose sur le score du modèle et sur un effet de classe des benzodiazépines.
- Les données de sécurité issues de la notice de l'ANSM manquent, ce qui bloque le passage à l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde, contre-indications), une lacune bloquante.
- Compléter les données de mécanisme d'action via DrugBank.
- Rechercher de la littérature spécifique au clobazam dans le FIRES et le NORSE (séries de cas, données d'usage en pratique réelle).
- Renseigner les indications autorisées de chaque AMM afin de documenter l'indication d'origine.
- Vérifier la compatibilité des voies d'administration : les formes disponibles sont orales (dont la suspension buvable), et les patients en réanimation reçoivent souvent des traitements par sonde.
- Autre piste : la prédiction « encéphalopathie épileptique de l'enfant » (rang 6) s'appuie sur une littérature bien plus fournie (revues et recommandations sur le syndrome de Lennox-Gastaut, le syndrome de Dravet et les crises du nourrisson). Elle mérite d'être examinée en priorité, après vérification indépendante des essais pivots.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

