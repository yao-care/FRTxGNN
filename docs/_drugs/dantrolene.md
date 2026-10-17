---
layout: default
title: Dantrolene
parent: Preuves modérées (L3-L4)
nav_order: 213
evidence_level: L3
indication_count: 9
last_modified_at: 2026-10-14
description: "Dantrolene : nouvelle indication prédite, Susceptibilité à l'hyperthermie maligne (niveau de preuve L3). Indication d'origine : Hyperthermie maligne de l'anesthésie"
monitor_inn: "dantrolene"
predicted_indications: ["moderate multiminicore disease with hand involvement", "King-Denborough syndrome", "congenital multicore myopathy with external ophthalmoplegia", "central core myopathy", "hypokalemic periodic paralysis", "thyrotoxic periodic paralysis, susceptibility to", "thyrotoxic periodic paralysis", "myopathy, centronuclear"]
---

# Dantrolene
{: .fs-9 }

Niveau de preuve: **L3** | Indications prédites: **9** 
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

# Dantrolène : De l'hyperthermie maligne de l'anesthésie à la susceptibilité à l'hyperthermie maligne

## Résumé en Une Phrase

Le dantrolène est un myorelaxant injectable (et oral sous forme de gélules), initialement utilisé pour le traitement de l'hyperthermie maligne de l'anesthésie et de l'hyperthermie maligne d'effort.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **susceptibilité à l'hyperthermie maligne**, mais cette prédiction recoupe en grande partie l'indication d'origine : il ne s'agit pas d'un véritable repositionnement.
Aucun essai clinique n'est enregistré ; **18 publications** (revues, recommandations de bonne pratique et études mécanistiques) soutiennent cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hyperthermie maligne de l'anesthésie ; hyperthermie maligne d'effort (d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas disponible) |
| Nouvelle Indication Prédite | Susceptibilité à l'hyperthermie maligne |
| Score de Prédiction TxGNN | 99,93 % |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Uniquement annulé (aucune AMM en vigueur) |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. D'après les publications disponibles, le dantrolène agit sur le récepteur de la ryanodine de type 1 (RYR1), le canal qui libère le calcium du réticulum sarcoplasmique dans le muscle squelettique, et réduit cette libération. Une étude de 2017 (PMID 28373535) indique en outre que son action nécessite la présence de magnésium (Mg2+).

L'hyperthermie maligne est un trouble pharmacogénétique du muscle squelettique, dû principalement à des variants de RYR1 (plus rarement de CACNA1S) qui provoquent une libération incontrôlée de calcium en présence d'anesthésiques volatils ou de succinylcholine. Le lien mécanistique est donc direct. Il faut toutefois souligner que la « nouvelle » indication prédite correspond à l'indication d'origine : la prédiction est cohérente, mais elle n'apporte pas de nouvelle piste thérapeutique.

D'autres maladies prédites partagent la voie RYR1/calcium, notamment le syndrome de King-Denborough, la myopathie à cores centraux et certaines myopathies centronucléaires. Pour ces entités, les données concernent surtout le risque d'hyperthermie maligne et non le traitement de la myopathie elle-même.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Sélection des publications les plus pertinentes pour l'indication prédite (recommandations de bonne pratique en priorité, puis revues) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33399225](https://pubmed.ncbi.nlm.nih.gov/33399225/) | 2021 | Recommandations | Anaesthesia | Recommandations 2020 de l'Association of Anaesthetists sur la prise en charge de l'hyperthermie maligne |
| [33131754](https://pubmed.ncbi.nlm.nih.gov/33131754/) | 2021 | Recommandations | Br J Anaesth | Consensus du groupe européen sur la prise en charge périopératoire des patients suspects ou susceptibles ; absence de données d'essais interventionnels |
| [26238698](https://pubmed.ncbi.nlm.nih.gov/26238698/) | 2015 | Revue | Orphanet J Rare Dis | Revue : incidence de 1/10 000 à 1/250 000 anesthésies ; trouble pharmacogénétique du muscle squelettique |
| [39171998](https://pubmed.ncbi.nlm.nih.gov/39171998/) | 2024 | Revue | Crit Care Med | Revue narrative d'experts sur l'épidémiologie et la prise en charge des patients en soins critiques |
| [32008650](https://pubmed.ncbi.nlm.nih.gov/32008650/) | 2020 | Revue | Anesthesiol Clin | Mise à jour : maladie rare et potentiellement létale touchant les canaux de libération du calcium ; mortalité en baisse |
| [28373535](https://pubmed.ncbi.nlm.nih.gov/28373535/) | 2017 | Étude mécanistique | PNAS | Le dantrolène nécessite Mg2+ pour arrêter l'hyperthermie maligne |
| [9538480](https://pubmed.ncbi.nlm.nih.gov/9538480/) | 1998 | Revue | Postgrad Med J | Le dantrolène sodique est le traitement de référence ; précautions chez les patients susceptibles |
| [23198031](https://pubmed.ncbi.nlm.nih.gov/23198031/) | 2012 | Revue | Korean J Anesthesiol | Transmission autosomique dominante à expression variable et pénétrance incomplète |
| [25989378](https://pubmed.ncbi.nlm.nih.gov/25989378/) | 2015 | Revue | Acta Anaesthesiol Scand | Mise à jour scandinave : lien avec les mutations du gène RYR1 |
| [17456235](https://pubmed.ncbi.nlm.nih.gov/17456235/) | 2007 | Revue | Orphanet J Rare Dis | Revue sur l'hyperthermie maligne et la prévalence des anomalies génétiques |

## Informations de Marché en France

Les trois AMM suivantes sont toutes annulées ; le texte d'indication approuvée n'est pas disponible.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65074386 | DANTRIUM INTRAVEINEUX | Lyophilisat pour préparation injectable | Non disponible |
| 60385682 | DANTRIUM 100 mg | Gélule | Non disponible |
| 67807645 | DANTRIUM 25 mg | Gélule | Non disponible |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de notice) : maladie du foie, maladie de la vésicule biliaire, myopathie, maladie musculaire, maladie du muscle squelettique, paralysie périodique familiale, maladie pulmonaire.
- **Interactions médicamenteuses** : 72 interactions recensées. Parmi celles listées :
  - Majeures : morphine (y compris liposomale).
  - Modérées : dronabinol, métoclopramide, nabilone, naltrexone, opium, sibutramine, éthanol, prométhazine.
  - Niveau inconnu : notamment pantoprazole, métformine, oméprazole, lansoprazole, simvastatine, ranitidine, famotidine, glipizide, clarithromycine, clopidogrel.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le lien mécanistique est direct et le dantrolène est le traitement de référence de l'hyperthermie maligne, soutenu par des recommandations et des revues. Le niveau L3 sous-estime probablement la certitude clinique, un essai randomisé étant impraticable. Cependant, la prédiction recoupe l'indication d'origine, aucune AMM n'est en vigueur en France et les données de sécurité officielles manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Vérifier la disponibilité réelle du produit en France (toutes les AMM sont annulées) et, le cas échéant, les alternatives ou importations autorisées.
- Obtenir les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le dépistage de sécurité).
- Compléter les données sur le mécanisme d'action depuis DrugBank.
- Évaluer les contre-indications liées au foie et aux muscles, en particulier pour un usage prolongé par voie orale.

**Autres indications prédites (à titre indicatif) :**
- Syndrome de King-Denborough, myopathie à cores centraux et myopathie centronucléaire (niveau L4, question de recherche) : soutien indirect, centré sur le risque d'hyperthermie maligne et non sur le traitement de la myopathie.
- Maladie multi-minicore avec atteinte des mains, myopathie multicore avec ophtalmoplégie externe, paralysies périodiques hypokaliémique et thyrotoxique (niveaux L4-L5, Hold) : prédictions purement computationnelles ou à données très limitées, sans bénéfice démontré.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

