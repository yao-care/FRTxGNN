---
layout: default
title: Zonisamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 832
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Zonisamide : nouvelle indication prédite, Syndrome de Gilles de la Tourette (rang 1) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM disponibles (les textes d'indi…"
monitor_inn: "ZONISAMIDE"
predicted_indications: ["Tourette syndrome", "trichotillomania", "methemoglobinemia, alpha type", "methemoglobinemia", "Prinzmetal angina", "methemoglobin reductase deficiency", "manic bipolar affective disorder", "fibromyalgia", "conjunctivitis"]
---

# Zonisamide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Zonisamide : De l'épilepsie au syndrome de Gilles de la Tourette (prédiction principale du modèle)
{: .text-alpha }

## Résumé en une phrase

Zonisamide est un antiépileptique de la famille des sulfonamides. Le modèle TxGNN le prédit comme potentiellement efficace dans le **syndrome de Gilles de la Tourette** (score de 0,9985), mais aucun essai clinique ni aucune publication ne soutient cette prédiction. Parmi les dix indications prédites, la mieux étayée est l'**épilepsie-absence** (niveau L3), avec 20 publications issues des données compilées pour ce rapport, principalement des séries de cas et des revues.

---

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans les données d'AMM disponibles (les textes d'indication sont vides) |
| Nouvelle indication prédite | Syndrome de Gilles de la Tourette (rang 1) |
| Score de prédiction TxGNN | 0,9985 |
| Niveau de preuve | L5 (prédiction du modèle uniquement) |
| Statut de Marché en France | Commercialisé (autorisations valides : 17 sur 20) |
| Nombre d'AMM | 20 (valides : 17) |
| Décision recommandée | Hold |

---

## Pourquoi cette prédiction est-elle raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Zonisamide (traduction non officielle) : « Le ou les mécanismes précis par lesquels le zonisamide exerce son effet antiépileptique sont inconnus. Le zonisamide a démontré une activité anticonvulsivante dans plusieurs modèles expérimentaux. Chez l'animal, le zonisamide a été efficace contre les crises d'extension tonique induites par électrochoc maximal, mais inefficace contre les crises cloniques induites par le pentétrazol administré par voie sous-cutanée. » Texte original en anglais : "The precise mechanism(s) by which zonisamide exerts its antiseizure effect is unknown. Zonisamide demonstrated anticonvulsant activity in several experimental models. In animals, zonisamide was effective against tonic extension seizures induced by maximal electroshock but ineffective against clonic seizures induced by subcutaneous pentylenetetrazol." ([DailyMed: Zonegran (zonisamide) prescribing information, Advanz Pharma (US) Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d12de43e-3ac3-4335-bc85-70d7366a91eb), version du 2026-09-23 ; consulté le 2026-11-19). D'après les connaissances générales, zonisamide agit en bloquant les canaux sodiques voltage-dépendants et les canaux calciques de type T, avec aussi des effets sur les systèmes dopaminergique et sérotoninergique. Il s'agit d'une hypothèse mécanistique plausible, mais spéculative pour le syndrome de Gilles de la Tourette.

Aucune donnée clinique ne confirme cette piste. Une revue (PMID 36005856) décrit au contraire des troubles obsessionnels compulsifs et des tics **induits** par les médicaments antiépileptiques. Elle constitue donc un signal de sécurité potentiel plutôt qu'un argument d'efficacité.

Les autres prédictions à score élevé (méthémoglobinémie, déficit en méthémoglobine réductase, conjonctivite, trichotillomanie) n'ont ni données ni mécanisme plausible. Leurs scores proviennent du modèle TxGNN (apprentissage profond) et peuvent refléter des similarités apprises par le modèle entre maladies proches, non des preuves biologiques. Les indications dotées de données exploitables sont le trouble bipolaire maniaque et la fibromyalgie, détaillées ci-dessous.

---

## Preuves d'essais cliniques

Aucun essai clinique associé n'est enregistré pour le syndrome de Gilles de la Tourette.

À titre d'information, un seul essai a été retrouvé parmi les indications prédites, pour la fibromyalgie :

| Numéro d'essai | Phase | Statut | Inscription | Résultats principaux |
|---------|------|------|------|---------|
| [NCT00259636](https://clinicaltrials.gov/study/NCT00259636) | Phase 4 | Retiré | 0 | Zonisamide versus placebo dans la fibromyalgie et la migraine. Essai retiré sans aucun participant : il ne fournit aucune donnée d'efficacité ni de sécurité. |

---

## Preuves de la littérature

Aucune littérature associée n'est disponible pour le syndrome de Gilles de la Tourette. Les publications les plus pertinentes retrouvées pour les autres indications prédites sont :

| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [15847848](https://pubmed.ncbi.nlm.nih.gov/15847848/) | 2005 | Série de cas (absences) | Epilepsy Res | Sur 45 patients de moins de 18 ans, 23 (51,1 %) n'ont plus eu d'absences sous zonisamide |
| [24907183](https://pubmed.ncbi.nlm.nih.gov/24907183/) | 2014 | Série de cas | Epilepsy Res | Zonisamide dans l'épilepsie-absence juvénile pharmaco-résistante |
| [15634623](https://pubmed.ncbi.nlm.nih.gov/15634623/) | 2004 | Étude rétrospective | Epileptic Disord | Efficacité et tolérance dans l'épilepsie myoclonique juvénile (15 patients) |
| [35363878](https://pubmed.ncbi.nlm.nih.gov/35363878/) | 2022 | Méta-analyse en réseau | Cochrane Database Syst Rev | Monothérapie antiépileptique, données générales sur l'épilepsie |
| [17163811](https://pubmed.ncbi.nlm.nih.gov/17163811/) | 2007 | Étude ouverte pilote | Expert Opin Pharmacother | Zonisamide dans la dépression bipolaire, sans bascule maniaque observée |
| [2109869](https://pubmed.ncbi.nlm.nih.gov/2109869/) | 1990 | Rapport de cas | Psychosomatics | Épisode de manie induit par zonisamide (signal de sécurité) |
| [36005856](https://pubmed.ncbi.nlm.nih.gov/36005856/) | 2022 | Revue | Expert Rev Neurother | TOC et tics induits par les antiépileptiques |
| [22575611](https://pubmed.ncbi.nlm.nih.gov/22575611/) | 2013 | Revue systématique | Int J Neuropsychopharmacol | Anticonvulsivants dans la dépression bipolaire aiguë |

---

## Informations de marché en France

Aucun texte d'indication approuvée n'est disponible. Les cinq premières sont :

<!-- review:begin fr-lic-20261106-zonisamide-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les 20 AMM recensées sont annulées. Aucun texte d'indication approuvée n'est disponible. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 20 AMM pour ce médicament, dont 17 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-zonisamide-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 64122807 | ZONEGRAN 100 mg, gélule | Gélule | AMDIPHARM | Active |
| 63127527 | ZONISAMIDE SANDOZ 25 mg, gélule | Gélule | SANDOZ | Active |
| 61247321 | ZONISAMIDE ARROW 50 mg, gélule | Gélule | ARROW GENERIQUES | Active |
| 69552780 | ZONISAMIDE NEURAXPHARM 200 mg, comprimé sécable | Comprimé sécable | NEURAXPHARM FRANCE | Active |
| 65968728 | ZONISAMIDE NEURAXPHARM 50 mg, comprimé sécable | Comprimé | NEURAXPHARM FRANCE | Active |
| 61088036 | ZONEGRAN 25 mg, gélule | Gélule | AMDIPHARM | Active |
| 69287499 | ZONEGRAN 50 mg, gélule | Gélule | AMDIPHARM | Active |
| 61436457 | ZONISAMIDE VIATRIS 100 mg, gélule | Gélule | VIATRIS (IRLANDE) | Active |
| 68467163 | ZONISAMIDE NEURAXPHARM 100 mg, comprimésécable | Comprimé sécable | NEURAXPHARM FRANCE | Active |
| 64467657 | ZONISAMIDE SANDOZ 50 mg, gélule | Gélule | SANDOZ | Active |
| 64784675 | ZONISAMIDE VIATRIS 50 mg, gélule | Gélule | VIATRIS (IRLANDE) | Active |
| 64827518 | ZONISAMIDE ARROW 25 mg, gélule | Gélule | ARROW GENERIQUES | Active |
| 62741554 | ZONISAMIDE SANDOZ 100 mg, gélule | Gélule | SANDOZ | Active |
| 65362239 | ZONISAMIDE ARROW 100 mg, gélule | Gélule | ARROW GENERIQUES | Active |
| 61207572 | ZONISAMIDE NEURAXPHARM 300 mg, comprimé sécable | Comprimé sécable | NEURAXPHARM FRANCE | Active |
| 65732820 | ZONISAMIDE NEURAXPHARM 25 mg, comprimé sécable | Comprimé sécable | NEURAXPHARM FRANCE | Active |
| 64892042 | ZONISAMIDE VIATRIS 25 mg, gélule | Gélule | VIATRIS (IRLANDE) | Active |
| 62540779 | ZONISAMIDE TEVA 25 mg, gélule | Gélule | TEVA SANTE | Abrogée |
| 62096228 | ZONISAMIDE TEVA 100 mg, gélule | Gélule | TEVA SANTE | Abrogée |
| 65110708 | ZONISAMIDE TEVA 50 mg, gélule | Gélule | TEVA SANTE | Abrogée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Considérations de sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie du graphe, et non texte de notice) : troubles anxieux et névrotiques, troubles psychotiques et schizo-affectifs, maladie rénale, lithiase rénale, maladie hépatique, maladie de la vésicule biliaire, acidose métabolique, agranulocytose et diverses neutropénies, maladies diarrhéiques.
- **Interactions médicamenteuses** : 100 interactions recensées. Les interactions **majeures** concernent surtout des anticholinergiques (atropine, scopolamine, hyoscyamine, glycopyrronium, dicyclomine, clidinium, trospium, méthscopolamine, mépenzolate, propanthéline) et la metformine. Les interactions **modérées** concernent notamment l'aprépitant, la morphine, la dexaméthasone, la cimétidine, la clarithromycine, le dronabinol, la nabilone, le métoclopramide et le miconazole.
- **Signaux psychiatriques** : cas de manie induite (PMID 2109869) et tics ou TOC induits par les antiépileptiques (PMID 36005856), ce qui pèse directement contre un usage dans le syndrome de Gilles de la Tourette ou le trouble bipolaire maniaque.

Veuillez consulter la notice pour les mises en garde officielles, qui ne sont pas disponibles dans les données compilées.

---

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- La prédiction principale (syndrome de Gilles de la Tourette) repose uniquement sur le modèle (L5), sans essai ni publication, et la littérature disponible évoque plutôt un risque de tics induits. Aucune donnée de sécurité issue de la notice n'est disponible.
- L'épilepsie-absence (L3) reste une question de recherche, car des traitements de première intention (éthosuximide, valproate) sont mieux documentés.

<!-- review:begin fr-lic-20261106-zonisamide-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La prédiction principale (syndrome de Gilles de la Tourette) repose uniquement sur le modèle (L5), sans essai ni publication, et la littérature disponible évoque plutôt un risque de tics induits. Le médicament est commercialisé en France, avec 20 AMM valides sur 20. » Supprimé : le nombre ou le statut des AMM indiqué ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 20 AMM pour ce médicament, dont 17 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-zonisamide-2 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications officielles de la notice ANSM (lacune bloquante pour le dépistage de sécurité).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Clarifier les raisons de l'annulation des AMM et le statut réglementaire actuel du produit.
- Pour toute indication retenue, rechercher des essais contrôlés randomisés ou des études observationnelles de qualité, avec évaluation du risque de tics, de manie et de symptômes obsessionnels.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Les 20 AMM recensées sont annulées » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « Le médicament est commercialisé en France, avec 20 AMM valides sur 20 » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-13 | Supprimé : « les raisons de l'annulation des AMM » | Vérification retirée (2026-11-24 : d'après la BDPM (données du 2026-11-23 ; fiche produit consultée le 2026-11-24), 3 des 20 AMM de zonisamide sont abrogées (62540779, 62096228, 65110708) ; le texte d'origine est donc exact et la correction est retirée ; auparavant : Corrigé) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Zonegran (zonisamide) prescribing information, Advanz Pharma (US) Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d12de43e-3ac3-4335-bc85-70d7366a91eb) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

