---
layout: default
title: Rivastigmine
parent: Prédiction du modèle uniquement (L5)
nav_order: 676
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "RIVASTIGMINE"
predicted_indications: ["glaucoma"]
description: "Rivastigmine : nouvelle indication prédite, Glaucome (glaucoma) (niveau de preuve L5). En France, AMM dans la BDPM : 16 (valides : 16)"
---

# Rivastigmine
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

## Rivastigmine: Glaucome (glaucoma)
{: .text-alpha }

## Résumé en Une Phrase

La rivastigmine est un inhibiteur des cholinestérases, initialement utilisé pour le traitement de la maladie d'Alzheimer.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **glaucome**, mais il n'existe actuellement **aucun essai clinique** et seulement **3 publications** (dont une étude préclinique chez le lapin), ce qui place cette piste à un stade très précoce.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Glaucome (glaucoma) |
| Score de Prédiction TxGNN | 0.9927 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 16 sur 16) |
| Nombre d'AMM | 16 (valides : 16) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Rivastigmine (traduction non officielle) : « Bien que le mécanisme d'action précis de la rivastigmine soit inconnu, on pense qu'elle exerce son effet thérapeutique en renforçant la fonction cholinergique. Ceci est obtenu par l'augmentation de la concentration d'acétylcholine via l'inhibition réversible de son hydrolyse par la cholinestérase. » Texte original en anglais : "Although the precise mechanism of action of rivastigmine is unknown, it is thought to exert its therapeutic effect by enhancing cholinergic function. This is accomplished by increasing the concentration of acetylcholine through reversible inhibition of its hydrolysis by cholinesterase." ([DailyMed: rivastigmine tartrate prescribing information, American Health Packaging](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=52781229-ee82-43f9-a113-4419a611978d), version du 2025-11-11 ; consulté le 2026-11-19). Sur la base des connaissances pharmacologiques générales, la rivastigmine est un inhibiteur de l'acétylcholinestérase et de la butyrylcholinestérase. Son efficacité dans la maladie d'Alzheimer repose sur l'augmentation de la transmission cholinergique.

Dans l'œil, une activité cholinergique accrue pourrait contribuer à abaisser la pression intraoculaire (PIO), en favorisant la contraction du muscle ciliaire et l'écoulement par le trabéculum. Ce mécanisme est comparable à celui des agents miotiques comme la pilocarpine et la physostigmine. Une étude chez le lapin normotendu a montré que la rivastigmine appliquée par voie topique réduisait la PIO, et une revue récente sur les agents cholinergiques et la PIO apporte un contexte mécanistique favorable.

Le score TxGNN très élevé (0,9927) reste une prédiction informatique et ne constitue pas une preuve clinique. Aucune donnée humaine dans le glaucome n'a été identifiée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Préclinique (lapin) | J Ocul Pharmacol Ther | La rivastigmine topique, inhibiteur sélectif de l'acétylcholinestérase, abaisse la pression intraoculaire chez le lapin normotendu |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Revue / analyse de génétique des systèmes | Front Mol Biosci | Analyse du rôle du système cholinergique et des agents cholinergiques dans la réduction de la PIO ; les agonistes M3 existants sont limités par leurs effets cholinergiques systémiques |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Revue | Expert Opin Ther Pat | Revue des brevets sur les inhibiteurs et réactivateurs de l'acétylcholinestérase ; une inhibition modérée a un intérêt thérapeutique dans la maladie d'Alzheimer, la myasthénie et le glaucome |

---

## Informations de Marché en France

Les 16 AMM recensées sont valides ; le médicament est commercialisé. Le texte de l'indication approuvée n'est pas renseigné pour ces AMM.

<!-- review:begin fr-lic-20261106-rivastigmine-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « (5 AMM présentées sur 11, toutes annulées.) » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 11 AMM pour ce médicament, dont 11 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-rivastigmine-1 -->

<!-- review:begin fr-lic-20261124-rivastigmine-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les 11 AMM listées sur 11 sont valides ; » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-rivastigmine-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 61430397 | RIVASTIGMINE EG LABO 9,5 mg/24 h, patch transdermique | Patch | EG LABO - LABORATOIRES EUROGENERICS | Active |
| 66197477 | RIVASTIGMINE BIOGARAN 9,5 mg/24 h, dispositif transdermique | Dispositif | BIOGARAN | Active |
| 64979294 | RIVASTIGMINE ARROW 4,6 mg/24 heures, dispositif transdermique | Dispositif | ARROW GENERIQUES | Active |
| 61148412 | RIVASTIGMINE VIATRIS 4,6 mg/24 heures, dispositif transdermique | Dispositif | VIATRIS SANTE | Active |
| 61322336 | RIVASTIGMINE BIOGARAN 4,6 mg/24 h, dispositif transdermique | Dispositif | BIOGARAN | Active |
| 61154803 | RIVASTIGMINE EG 9,5 mg/24 h, dispositif transdermique | Dispositif | EG LABO - LABORATOIRES EUROGENERICS | Active |
| 66442631 | RIVASTIGMINE VIATRIS 9,5 mg/24 heures, dispositif transdermique | Dispositif | VIATRIS SANTE | Active |
| 63140325 | RIVASTIGMINE EG LABO 4,6 mg/24 h, patch transdermique | Patch | EG LABO - LABORATOIRES EUROGENERICS | Active |
| 66177624 | RIVASTIGMINE ARROW 9,5 mg/24 heures, dispositif transdermique | Dispositif | ARROW GENERIQUES | Active |
| 64501892 | RIVASTIGMINE EG 4,6 mg/24 h, dispositif transdermique | Dispositif | EG LABO - LABORATOIRES EUROGENERICS | Active |
| 63927615 | RIVASTIGMINE SANDOZ 4,6 mg/24 h, dispositif transdermique | Dispositif | SANDOZ | Active |
| 63093669 | EXELON 9,5 mg/24 h, dispositif transdermique | Dispositif | NOVARTIS EUROPHARM (IRLANDE) | Active |
| 63290816 | RIVASTIGMINE ZENTIVA 4,6 mg/24 heures, dispositif transdermique | Dispositif | ZENTIVA FRANCE | Active |
| 67764293 | RIVASTIGMINE SANDOZ 9,5 mg/24 h, dispositif transdermique | Dispositif | SANDOZ | Active |
| 67885398 | EXELON 4,6 mg/24 h, dispositif transdermique | Dispositif | NOVARTIS EUROPHARM (IRLANDE) | Active |
| 69978449 | RIVASTIGMINE ZENTIVA 9,5 mg/24 heures, dispositif transdermique | Dispositif | ZENTIVA FRANCE | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : épilepsie, maladies des ganglions de la base, dystonie focale de la main, blépharospasme, bronchopneumopathie chronique obstructive (dont forme sévère à début précoce), asthme (dont formes intrinsèque et allergique), maladies diarrhéiques, arrêt cardiaque soudain, maladies de la conduction cardiaque, anorexie mentale, ulcère peptique actif, obstruction des voies urinaires, maladie du sinus (dont forme familiale), syndromes parkinsoniens et maladie de Parkinson, bloc auriculo-ventriculaire.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les principales :
  - **Majeure** : bupropion.
  - **Modérées** : famotidine, ranitidine, cimétidine, hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, trospium, mépenzolate (anticholinergiques, avec risque d'antagonisme pharmacologique), lopéramide, métronidazole, clarithromycine, lévofloxacine, dolasétron, palonosétron, acide picosulfurique, polyéthylène glycol avec électrolytes, sulfate de sodium.

Les mises en garde et contre-indications issues de la notice française n'ont pas pu être consultées. Veuillez consulter la notice pour ces informations. Les effets systémiques cholinergiques (cardiaques, respiratoires, digestifs) sont particulièrement à considérer si une voie topique oculaire devait être explorée.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un score élevé du modèle TxGNN (deep learning) et une seule étude animale (lapin), sans aucune donnée humaine dans le glaucome (niveau L4). De plus, le dépôt de sécurité issu de la notice est manquant ; les 16 AMM françaises sur 16 sont valides.

<!-- review:begin fr-lic-20261124-rivastigmine-2 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « les 11 AMM françaises sur 11 sont valides. » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-rivastigmine-2 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications, étape bloquante pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Confirmer l'effet sur la PIO dans des modèles animaux supplémentaires (notamment glaucome hypertensif) et évaluer la tolérance oculaire
- Évaluer la faisabilité d'une formulation oculaire topique, la formulation actuelle étant transdermique
- Comparer l'intérêt de la rivastigmine aux traitements du glaucome existants avant toute étude clinique de phase précoce

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « (5 AMM présentées sur 11, toutes annulées.) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: rivastigmine tartrate prescribing information, American Health Packaging](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=52781229-ee82-43f9-a113-4419a611978d) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

