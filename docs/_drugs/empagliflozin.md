---
layout: default
title: Empagliflozin
parent: Prédiction du modèle uniquement (L5)
nav_order: 280
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "empagliflozin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia"]
description: "Empagliflozin : nouvelle indication prédite, Syndrome de la personne raide classique (classic stiff person syndrome) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données loca…"
---

# Empagliflozin
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

## Empagliflozin: Syndrome de la personne raide classique (classic stiff person syndrome)
{: .text-alpha }

## Résumé en Une Phrase

L'empagliflozine est un inhibiteur du SGLT2, initialement utilisé pour le traitement du diabète de type 2.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome de la personne raide classique**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Syndrome de la personne raide classique (classic stiff person syndrome) |
| Score de Prédiction TxGNN | 0.9906 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Empagliflozin (traduction non officielle) : « L'empagliflozine est un inhibiteur du SGLT2, le principal transporteur responsable de la réabsorption du glucose du filtrat glomérulaire vers la circulation. En inhibant le SGLT2, l'empagliflozine réduit la réabsorption rénale du glucose filtré et abaisse le seuil rénal du glucose, augmentant ainsi l'excrétion urinaire de glucose. » Texte original en anglais : "Empagliflozin is an inhibitor of SGLT2, the predominant transporter responsible for reabsorption of glucose from the glomerular filtrate back into the circulation. By inhibiting SGLT2, empagliflozin reduces renal reabsorption of filtered glucose and lowers the renal threshold for glucose, and thereby increases urinary glucose excretion." ([DailyMed: Jardiance (empagliflozin) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=faf3dd6a-9cd0-39c2-0d2e-232cb3f67565), version du 2026-11-10 ; consulté le 2026-11-19). D'après les informations connues, l'empagliflozine est un inhibiteur du SGLT2 qui abaisse la glycémie en bloquant la réabsorption rénale du glucose, indépendamment de l'insuline. Son efficacité dans le diabète de type 2 est établie.

Aucun lien mécanistique solide n'a été identifié avec le syndrome de la personne raide, une maladie neurologique auto-immune généralement associée aux anticorps anti-GAD65, avec une altération de l'inhibition GABAergique. Une piste spéculative est la co-occurrence fréquente de ce syndrome avec le diabète auto-immun (type 1), ce qui pourrait expliquer le rapprochement fait par le modèle. Il s'agit d'une association de comorbidité et non d'un argument thérapeutique : l'inhibition du SGLT2 n'a aucun effet connu sur la signalisation GABA ni sur la pathologie auto-immune.

Aucune ne repose sur une justification pharmacologique établie.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 69963066 | JARDIANCE 25 mg, comprimé pelliculé | Comprimé pelliculé | BOEHRINGER INGELHEIM INTERNATIONAL | Active |
| 67947145 | JARDIANCE 10 mg, comprimé pelliculé | Comprimé pelliculé | BOEHRINGER INGELHEIM INTERNATIONAL | Active |
| 64866745 | SYNJARDY 12,5 mg/1000 mg, comprimé pelliculé | Comprimé pelliculé | BOEHRINGER INGELHEIM INTERNATIONAL | Active |
| 60901946 | SYNJARDY 5 mg/1000 mg, comprimé pelliculé | Comprimé pelliculé | BOEHRINGER INGELHEIM INTERNATIONAL | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 369 interactions sont recensées. Parmi les premières listées, la plupart sont de niveau **modéré** : phényléphrine, acébutolol, acétazolamide, formotérol, pseudoéphédrine, nifédipine, épinéphrine, éthinylestradiol, hydrocortisone, salbutamol, éthanol, fosamprénavir, fosinopril, fosphénytoïne, fostamatinib, fostémsavir, furosémide, géméfloxacine. Deux sont de niveau **mineur** : hydrocortisone (topique) et alclométasone (topique). Cette liste est partielle et ne reflète pas l'ensemble des 369 interactions.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai clinique ni publication, et sans lien mécanistique plausible.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (donnée bloquante)
- Obtenir les données sur le mécanisme d'action (par exemple via DrugBank)
- Rechercher des études précliniques ou des cas rapportés reliant l'inhibition du SGLT2 au syndrome de la personne raide
- Vérifier le statut réglementaire actuel de l'empagliflozine en France
- Confirmer la prédiction de manière indépendante avant toute évaluation clinique

<!-- review:begin fr-lic-20261106-empagliflozin-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Vérifier le statut réglementaire actuel de l'empagliflozine en France (les AMM compilées sont toutes annulées) » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-empagliflozin-1 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « (les AMM compilées sont toutes annulées) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Jardiance (empagliflozin) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=faf3dd6a-9cd0-39c2-0d2e-232cb3f67565) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

