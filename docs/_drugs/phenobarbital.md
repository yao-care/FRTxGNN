---
layout: default
title: Phenobarbital
parent: Prédiction du modèle uniquement (L5)
nav_order: 595
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "phenobarbital"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
description: "Phenobarbital : nouvelle indication prédite, Tumeur du nerf trijumeau (trigeminal nerve neoplasm) (niveau de preuve L5). En France, AMM dans la BDPM : 11 (valides : 11)"
---

# Phenobarbital
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

## Phenobarbital: Tumeur du nerf trijumeau (trigeminal nerve neoplasm)
{: .text-alpha }

## Résumé en Une Phrase

Le phénobarbital est un barbiturique anticonvulsivant, utilisé à l'origine pour traiter l'épilepsie (crises généralisées tonico-cloniques, épilepsie partielle, syndrome de Lennox-Gastaut) ainsi que certaines céphalées et migraines.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **tumeur du nerf trijumeau** (score très élevé), mais **aucun essai clinique** n'est enregistré et la seule publication retrouvée (une série de cas sur le syndrome de Sturge-Weber) ne concerne pas cette indication.
Les données compilées pour ce rapport ne soutiennent donc cette prédiction que par le modèle seul.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Tumeur du nerf trijumeau (trigeminal nerve neoplasm) |
| Score de Prédiction TxGNN | 0.9996 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 11 sur 11) |
| Nombre d'AMM | 11 (valides : 11) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Phenobarbital (traduction non officielle) : « Le mécanisme d'action précis du phénobarbital dans le traitement des convulsions néonatales n'est pas entièrement élucidé, mais on pense qu'il implique une potentialisation de l'inhibition synaptique par une action sur le récepteur GABA A. » Texte original en anglais : "The precise mechanism of action for phenobarbital for the treatment of neonatal seizures is not fully understood, but it is thought to involve potentiation of synaptic inhibition through an action on the GABA A receptor." ([DailyMed: Sezaby (phenobarbital sodium) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8c7d0402-4977-4c25-bc4b-11db91339e9a), version du 2026-10-23 ; consulté le 2026-11-19). D'après les connaissances pharmacologiques générales, le phénobarbital est un modulateur allostérique positif des récepteurs GABA-A qui supprime les crises, et il n'a pas d'activité antitumorale connue.

**La prédiction ne repose sur aucun lien mécanistique crédible.** Le score élevé provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises entre maladies voisines, et non une preuve biologique. La seule publication retrouvée porte sur la prise en charge des crises dans le syndrome de Sturge-Weber, et non sur une tumeur du trijumeau.

**Autres prédictions du modèle (classées par score) :**

| Rang | Indication prédite | Niveau | Commentaire |
|---|---|---|---|
| 2 | Crises induites par la miction | L4 | Preuves indirectes, extrapolées des indications générales de l'épilepsie |
| 3 | Crises induites par la pensée | L4 | Rien de spécifique ; données précliniques et néonatales |
| 4 | Crises induites par l'orgasme | L5 | Aucune donnée |
| 5 | Crises audiogéniques | L4 | Modèles animaux, rapports vétérinaires et un cas humain ; question de recherche |
| 6 | Crises induites par l'alimentation | L4 | Cas isolés |
| 7 | Épilepsie de sursaut | L4 | Cas cliniques sans preuve d'efficacité du phénobarbital |
| 8 | Crises induites par la lecture | L4 | Littérature non spécifique |
| 9 | Névralgie du trijumeau | L4 | Le phénobarbital n'est pas un traitement recommandé (carbamazépine en première ligne) ; question de recherche |
| 10 | Déficit en bêta-cétothiolase | L5 | Aucun lien mécanistique |

Les rangs 2 à 8 correspondent à des épilepsies réflexes, déjà largement couvertes par l'indication antiépileptique générale : ils ne constituent pas un véritable repositionnement.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Série de cas | Anales espanoles de pediatria | Revue de 14 cas de syndrome de Sturge-Weber suivis sur 25 ans (caractéristiques cliniques, évolution, réponse thérapeutique) ; ne concerne pas une tumeur du trijumeau |

## Informations de Marché en France

Le médicament est commercialisé : 11 AMM valides sur 11 identifiées. Le texte d'indication approuvée n'est pas renseigné.

<!-- review:begin fr-lic-20261106-phenobarbital-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Six autres AMM annulées (Gardenal 200 mg/4 ml, Gardenal 50 mg, Alepsal 15, 50, 100 et 150 mg) ne sont pas détaillées ici. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-phenobarbital-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 63019074 | PHENOBARBITALUM BOIRON, degré de dilution compris entre 4CH et 30CH ou entre 8DH et 60DH | Comprimé et solution(s) et granules et poudre et pommade | BOIRON | Active |
| 63707416 | GARDENAL 10 mg, comprimé | Comprimé | ATNAHS PHARMA FRANCE | Active |
| 64933585 | GARDENAL 40 mg/2 ml, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | ATNAHS PHARMA FRANCE | Active |
| 60323481 | PHENOBARBITAL RICHARD 100 mg, comprimé sécable | Comprimé sécable | RICHARD | Active |
| 61475588 | GARDENAL 100 mg, comprimé | Comprimé | ATNAHS PHARMA FRANCE | Active |
| 68473458 | GARDENAL 200 mg/4 ml, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | ATNAHS PHARMA FRANCE | Active |
| 65391080 | GARDENAL 50 mg, comprimé | Comprimé | ATNAHS PHARMA FRANCE | Active |
| 60622868 | ALEPSAL 50 mg, comprimé | Comprimé | TEOFARMA | Active |
| 66086808 | ALEPSAL 100 mg, comprimé | Comprimé | TEOFARMA | Active |
| 63131269 | ALEPSAL 15 mg, comprimé | Comprimé | TEOFARMA | Active |
| 66014762 | ALEPSAL 150 mg, comprimé | Comprimé | TEOFARMA | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, insuffisance et maladies hépatiques, porphyries, maladies rénales, BPCO, insomnie, troubles anxieux et névrotiques, troubles psychotiques et mentaux, ulcère gastrique et gastrite, maladies de la vésicule biliaire, thrombocytopénie, hyperglycémie, hypothyroïdie et myxœdème, lupus érythémateux systémique.
- **Interactions médicamenteuses** : 273 interactions recensées. Les interactions **majeures** incluent la morphine (y compris liposomale), l'éliglustat, la naldémédine, le naloxégol et le rolapitant. Les interactions **modérées** incluent notamment la doxycycline, les corticoïdes (hydrocortisone, dexaméthasone, prednisone, prednisolone, bétaméthasone, triamcinolone), le métronidazole, le bupropion, l'aprépitant, la pioglitazone, le dronabinol, la vitamine D et la pyridoxine. Le phénobarbital est un inducteur enzymatique puissant, ce qui explique en partie ce grand nombre d'interactions.
- La littérature retrouvée signale aussi des effets cognitifs et un risque d'apoptose neuronale en exposition néonatale (données précliniques), ainsi que le syndrome d'hypersensibilité aux anticonvulsivants.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être récupérées : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction principale (tumeur du nerf trijumeau) n'a ni essai clinique, ni littérature pertinente, ni lien mécanistique plausible ; son score provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises entre maladies voisines, non une preuve biologique. Le médicament est par ailleurs commercialisé (11 AMM valides sur 11).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications officielles), ce qui bloque actuellement le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Démontrer un rationnel biologique pour une activité antitumorale, avant toute étude
- Pour les épilepsies réflexes (rangs 2 à 8) et la névralgie du trijumeau, réaliser une revue ciblée de la littérature, qui relèvent davantage de questions de recherche que de véritables repositionnements
- Clarifier le statut réglementaire avant toute perspective de développement

<!-- review:begin fr-lic-20261106-phenobarbital-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarifier le statut réglementaire (AMM annulées) avant toute perspective de développement » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-phenobarbital-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Six autres AMM annulées (Gardenal 200 mg/4 ml, Gardenal 50 mg, Alepsal 15, 50, 100 et 150 mg) ne sont pas détaillées ici » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulées) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Sezaby (phenobarbital sodium) prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8c7d0402-4977-4c25-bc4b-11db91339e9a) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

