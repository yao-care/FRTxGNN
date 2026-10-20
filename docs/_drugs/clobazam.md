---
layout: default
title: Clobazam
parent: Prédiction du modèle uniquement (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Clobazam : nouvelle indication prédite, Syndrome d'épilepsie lié à une infection fébrile (FIRES) (niveau de preuve L5). Indication d'origine : Syndrome de Lennox-Gastaut"
monitor_inn: "CLOBAZAM"
predicted_indications: ["febrile infection-related epilepsy syndrome", "perioral myoclonia with absences", "photosensitive occipital lobe epilepsy", "atypical childhood epilepsy with centrotemporal spikes", "cryptogenic late-onset epileptic spasms", "childhood onset epileptic encephalopathy", "benign occipital epilepsy", "early-onset epileptic encephalopathy and intellectual disability due to GRIN2A mutation", "restless legs syndrome", "polymicrogyria with optic nerve hypoplasia"]
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

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

# Clobazam : Du Syndrome de Lennox-Gastaut au Syndrome d'épilepsie lié à une infection fébrile (FIRES)

## Résumé en Une Phrase

Le clobazam est une benzodiazépine (1,5-benzodiazépine) initialement utilisée dans le traitement du syndrome de Lennox-Gastaut.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome d'épilepsie lié à une infection fébrile (FIRES)**,
mais cette prédiction ne repose que sur **2 publications** (séries et rapports de cas) portant sur d'autres médicaments, **sans aucun essai clinique** : il s'agit à ce stade d'une hypothèse de recherche.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Syndrome de Lennox-Gastaut (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Syndrome d'épilepsie lié à une infection fébrile (FIRES) |
| Score de Prédiction TxGNN | 99,82 % |
| Niveau de Preuve | L5 selon la grille de ce rapport (aucun essai clinique ; seulement 2 cas/séries de cas n'évaluant pas le clobazam) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le clobazam est un modulateur allostérique positif du récepteur GABA-A (benzodiazépine). Son efficacité dans le syndrome de Lennox-Gastaut, une encéphalopathie épileptique sévère, est reconnue.

Le FIRES est une forme d'état de mal épileptique réfractaire d'apparition récente (NORSE) survenant chez des enfants auparavant en bonne santé. Les crises y sont souvent résistantes aux antiépileptiques usuels et nécessitent des anesthésiques à haute dose. Le raisonnement est donc de classe : les agents GABAergiques sont couramment employés dans ces situations.

Il faut toutefois rester prudent : les deux publications retrouvées portent sur le sevrage par lorazépam entéral après midazolam et sur le pérampanel pour réduire la dépendance aux barbituriques. Aucune n'évalue directement le clobazam.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | Série de cas | Epileptic Disorders | Le lorazépam entéral comme stratégie de sevrage chez des patients FIRES dépendants du midazolam (ne concerne pas le clobazam) |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | Rapport de cas | Cureus | Rôle potentiel du pérampanel pour réduire la dépendance aux barbituriques chez un garçon de 13 ans atteint de FIRES (ne concerne pas le clobazam) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 62905911 | URBANYL 10 mg, comprimé sécable | Comprimé sécable | Non renseignée | Annulée |
| 65899602 | LIKOZAM 1 mg/ml, suspension buvable | Suspension buvable | Non renseignée | Annulée |
| 64630403 | URBANYL 5 mg, gélule | Gélule | Non renseignée | Annulée |
| 63470312 | URBANYL 20 mg, comprimé | Comprimé | Non renseignée | Annulée |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions sont recensées au total. Parmi celles affichées :
  - **Majeures** : morphine (y compris liposomale), éliglustat
  - **Modérées** : bupropion, aprépitant, oméprazole, ésoméprazole, lansoprazole, cimétidine, clarithromycine, dexfenfluramine, fenfluramine, dronabinol, métoclopramide
  - **Mineures** : antiacides (oxyde de magnésium, hydroxyde d'aluminium, carbonate de calcium, magaldrate, carbonate de magnésium, hydroxyde de magnésium)

Veuillez consulter la notice pour les mises en garde et contre-indications, qui n'ont pas pu être obtenues pour ce rapport.

## Autres Indications Prédites (pour information)

| Rang | Maladie | Score TxGNN | Niveau de preuve | Recommandation |
|---|---|---|---|---|
| 2 | Myoclonies périorales avec absences | 99,79 % | L5 | Hold |
| 3 | Épilepsie photosensible du lobe occipital | 99,77 % | L4 | Hold |
| 4 | Épilepsie atypique de l'enfant à pointes centrotemporales | 99,77 % | L4 | Question de recherche |
| 5 | Spasmes épileptiques tardifs cryptogéniques | 99,77 % | L4 | Hold |
| 6 | Encéphalopathie épileptique de l'enfant | 99,59 % | L3 | Question de recherche |
| 7 | Épilepsie occipitale bénigne | 99,58 % | L4 | Question de recherche |
| 8 | Encéphalopathie épileptique précoce liée à GRIN2A | 99,40 % | L5 | Hold |
| 9 | Syndrome des jambes sans repos | 99,30 % | L5 | Hold |
| 10 | Polymicrogyrie avec hypoplasie du nerf optique | 99,09 % | L5 | Hold |

Ces niveaux sont ceux attribués dans les données compilées. L'encéphalopathie épileptique de l'enfant (rang 6) est la piste la plus proche de l'usage connu (guides et revues sur le syndrome de Lennox-Gastaut), mais elle repose sur des revues et recommandations, sans essai dédié.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour le FIRES, la prédiction repose uniquement sur le score du modèle et sur un raisonnement de classe GABAergique. Les deux publications ne concernent pas le clobazam, et il n'existe aucun essai clinique.
- Toutes les AMM françaises du clobazam sont annulées, et les données de sécurité issues de la notice sont absentes, ce qui bloque le passage au criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice auprès de l'ANSM
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Rechercher des données spécifiques au clobazam dans le FIRES/NORSE (séries de cas, registres)
- Vérifier le statut réglementaire actuel du clobazam en France (AMM annulées) et la disponibilité d'autres présentations
- Examiner en priorité la piste « encéphalopathie épileptique de l'enfant », la plus proche de l'indication d'origine
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

