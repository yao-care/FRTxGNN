---
layout: default
title: Alfacalcidol
parent: Prédiction du modèle uniquement (L5)
nav_order: 34
evidence_level: L5
indication_count: 3
monitor_inn: "ALFACALCIDOL"
predicted_indications: ["craniofacial conodysplasia", "acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis"]
last_modified_at: 2026-10-28
description: "Alfacalcidol : nouvelle indication prédite, Conodysplasie crânio-faciale (niveau de preuve L5). Indication d'origine : Hyperparathyroïdie, ostéite fibreuse, hypoparathyroïdie…"
---

# Alfacalcidol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Alfacalcidol : De l'hyperparathyroïdie à la conodysplasie crânio-faciale
{: .text-alpha }

## Résumé en Une Phrase

Alfacalcidol est un analogue actif de la vitamine D. Le graphe de connaissances utilisé par le modèle enregistre pour lui des relations avec l'hyperparathyroïdie, l'ostéite fibreuse, l'hypoparathyroïdie et l'ostéodystrophie rénale.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **conodysplasie crânio-faciale**, une dysplasie squelettique rare.
Actuellement, **aucun essai clinique** et **aucune publication** ne soutiennent cette direction : il s'agit d'une prédiction du modèle uniquement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hyperparathyroïdie, ostéite fibreuse, hypoparathyroïdie, ostéodystrophie rénale (relations enregistrées dans le graphe de connaissances ; les textes d'indication des AMM ne sont pas renseignés dans les données compilées) |
| Nouvelle Indication Prédite | Conodysplasie crânio-faciale |
| Score de Prédiction TxGNN | 0,9955 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 10 sur 10) |
| Nombre d'AMM | 10 (valides : 10) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Alfacalcidol est un analogue de la vitamine D hydroxylé en position 1-alpha, transformé dans le foie en calcitriol, la forme active de la vitamine D. Il intervient dans l'équilibre du calcium et du phosphate et dans la minéralisation osseuse.

Les relations enregistrées dans le graphe de connaissances (hyperparathyroïdie, ostéodystrophie rénale, etc.) concernent des troubles du métabolisme phosphocalcique et osseux. La conodysplasie crânio-faciale est une dysplasie squelettique. Le modèle a probablement établi le rapprochement à partir de phénotypes osseux communs.

Cette hypothèse reste très spéculative. Aucune voie biologique précise reliant l'alfacalcidol à cette maladie n'est établie, et l'absence de données sur le mécanisme d'action empêche de vérifier la cohérence de la prédiction. Le score élevé du modèle ne suffit pas à lui seul à justifier un développement.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 10 AMM compilées sont valides et concernent des spécialités à base d'alfacalcidol seul. Voici les 5 premières :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 65401076 | UN-ALFA 0,10 microgramme, solution buvable en gouttes | Solution buvable en gouttes |
| 68578562 | UN-ALFA 1 microgramme/0,5 ml, solution injectable IV en ampoule | Solution injectable |
| 64661847 | ALFACALCIDOL THERAMEX 0,25 microgramme, capsule molle | Capsule molle |
| 62092176 | UN ALFA 1 microgramme, capsule orale | Capsule |
| 62626139 | ALFACALCIDOL THERAMEX 1 microgramme, capsule molle | Capsule molle |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (L5), sans essai clinique ni publication portant sur la conodysplasie crânio-faciale, et sans lien mécanistique démontré.
- Les données de sécurité de la notice et le mécanisme d'action manquent également.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Récupération et analyse de la notice de l'ANSM (mises en garde et contre-indications)
- Revue de la littérature sur la physiopathologie de la conodysplasie crânio-faciale, afin de déterminer si une voie liée à la vitamine D est plausible
- Études précliniques ou de mécanisme si une piste biologique est identifiée

**Remarque sur une autre prédiction :** pour l'**acidose tubulaire rénale** (3e prédiction, score de 0,9927), les données compilées contiennent 5 rapports de cas. Ils décrivent l'ostéomalacie associée à cette acidose, dans certains cas traitée avec un dérivé actif de la vitamine D. Ils ne portent pas sur une efficacité démontrée dans l'acidose tubulaire elle-même. L'alfacalcidol y agirait plutôt comme traitement adjuvant des complications osseuses. Cette piste pourrait être explorée séparément comme question de recherche.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

