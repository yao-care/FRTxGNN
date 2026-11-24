---
layout: default
title: Primidone
parent: Prédiction du modèle uniquement (L5)
nav_order: 631
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "PRIMIDONE"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
description: "Primidone : nouvelle indication prédite, Néoplasme du nerf trijumeau (trigeminal nerve neoplasm) (niveau de preuve L5). En France, AMM dans la BDPM : 1 (valides : 1)"
---

# Primidone
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

## Primidone: Néoplasme du nerf trijumeau (trigeminal nerve neoplasm)
{: .text-alpha }

## Résumé en Une Phrase

Primidone est un anticonvulsivant, initialement utilisé pour traiter plusieurs formes d'épilepsie (épilepsie généralisée tonico-clonique, épilepsie partielle, syndrome de Lennox-Gastaut).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **néoplasme du nerf trijumeau**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Néoplasme du nerf trijumeau (trigeminal nerve neoplasm) |
| Score de Prédiction TxGNN | 0.9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Primidone (traduction non officielle) : « MYSOLINE élève les seuils de crises convulsives induites par électrochoc ou par choc chimique, ou modifie les profils des crises chez l'animal de laboratoire. Le ou les mécanismes de l'action antiépileptique de la primidone ne sont pas connus. La primidone possède en soi une activité anticonvulsivante, de même que ses deux métabolites, le phénobarbital et le phényléthylmalonamide (PEMA). » Texte original en anglais : "MYSOLINE raises electro- or chemoshock seizure thresholds or alters seizure patterns in experimental animals. The mechanism(s) of primidone’s antiepileptic action is not known. Primidone per se has anticonvulsant activity as do its two metabolites, phenobarbital and phenylethylmalonamide (PEMA)." ([DailyMed: Mysoline (primidone) prescribing information, Bausch Health US, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=af593171-dabb-4ea3-b44c-89ed457b2c46), version du 2026-09-10 ; consulté le 2026-11-19). Sur la base des informations connues, primidone est un anticonvulsivant métabolisé en phénobarbital et en PEMA, qui agit sur l'excitabilité neuronale. Son efficacité dans l'épilepsie est établie.

En revanche, **aucune justification mécanistique n'apparaît pour un néoplasme du nerf trijumeau**. Primidone n'a pas d'activité antinéoplasique connue. Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées (par exemple la névralgie du trijumeau), et non une preuve biologique.

Cette prédiction doit donc être considérée avec une grande prudence.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Autres Prédictions Examinées

Les autres indications prédites sont présentées à titre de contexte. Elles concernent surtout des épilepsies réflexes, plus proches de l'indication d'origine, mais les preuves restent faibles.

| Indication Prédite | Score TxGNN | Niveau de Preuve | Preuves Disponibles |
|------|------|------|------|
| Crises déclenchées par l'alimentation | 0,9999 | L5 | Une étude vétérinaire de 1974 chez le chien |
| Crises induites par l'orgasme | 0,9999 | L5 | Aucune |
| Crises induites par la miction | 0,9999 | L5 | 15 références générales (revues sur les antiépileptiques, interactions), aucune spécifique à cette affection |
| Épilepsie de sursaut | 0,9999 | L5 | Un cas clinique de 1995, lien avec primidone non confirmé |
| Crises induites par la pensée | 0,9999 | L5 | Une étude générale sur le choix des antiépileptiques chez le sujet âgé |
| Crises audiogéniques | 0,9999 | L5 | Deux études animales (1964, 1976) |
| Crises de lecture | 0,9998 | L4 | Cas cliniques anciens d'autres épilepsies réflexes, revue sur le myoclonus |
| Névralgie du trijumeau | 0,9998 | L4 | Revues, surtout sur la carbamazépine ; une revue sur les antiépileptiques hors épilepsie (PMID 15246950) ; un modèle murin |
| Déficit en bêta-cétothiolase | 0,9996 | L5 | Aucune ; probable artefact du réseau |

Parmi elles, la **névralgie du trijumeau** est la piste la plus plausible (classée comme question de recherche). Les anticonvulsivants bloquant les canaux sodiques, comme la carbamazépine, y sont efficaces, mais aucun essai spécifique à primidone n'a été trouvé.

---

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 65201684 | MYSOLINE 250 mg, comprimé sécable | Comprimé sécable | SERB | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Considérations de Sécurité

Les données issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité.

**Contre-indications ou maladies à risque (graphe de connaissances, hors texte de notice) :**
- Troubles psychiatriques : trouble anxieux, trouble névrotique, trouble dysthymique, abus de substances/dépendance
- Porphyries : porphyrie héréditaire, maladies du métabolisme des porphyrines
- Atteintes organiques : maladie rénale, maladie hépatique, maladie de la vésicule biliaire
- Anomalies hématologiques : thrombopénie, neutropénie (y compris formes congénitales), agranulocytose, leucopénie, pancytopénie, anémie (y compris macrocytaire)
- Troubles respiratoires du sommeil : syndrome d'apnée du sommeil, syndrome d'hypoventilation centrale congénitale

**Interactions médicamenteuses** (100 interactions recensées ; extraits) :
- **Majeures** : morphine, éliglustat
- **Modérées** : doxycycline, hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, cholécalciférol, calcifédiol, calcitriol, pioglitazone, bupropion, aprépitant, métronidazole, canagliflozine, saxagliptine, difénoxine, diphénoxylate, dronabinol
- **Mineure** : cimétidine

Primidone est un inducteur enzymatique (via le phénobarbital), ce qui explique de nombreuses interactions, notamment avec les corticoïdes et les vitamines D.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour le néoplasme du nerf trijumeau, il n'existe ni essai, ni publication, ni logique mécanistique. Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.
- Les données de sécurité de la notice manquent, ce qui bloque le passage au criblage de sécurité.

<!-- review:begin fr-lic-20261106-primidone-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « L'AMM française est annulée et les données de sécurité de la notice manquent, ce qui bloque le passage au criblage de sécurité. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-primidone-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde, contre-indications) auprès de l'ANSM
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Si une piste doit être explorée, privilégier la névralgie du trijumeau ou les épilepsies réflexes, plus cohérentes avec le profil du médicament, en recherchant des données spécifiques à primidone
- Confirmer le statut réglementaire actuel du médicament en France et la faisabilité d'un accès

<!-- review:begin fr-lic-20261106-primidone-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Confirmer le statut réglementaire actuel du médicament en France (AMM annulée) et la faisabilité d'un accès » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-primidone-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « 'AMM française est annulée et l » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulée) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Mysoline (primidone) prescribing information, Bausch Health US, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=af593171-dabb-4ea3-b44c-89ed457b2c46) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

