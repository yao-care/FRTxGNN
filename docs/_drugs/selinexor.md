---
layout: default
title: Selinexor
parent: Prédiction du modèle uniquement (L5)
nav_order: 696
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Selinexor : nouvelle indication prédite, Ostéoporose médicamenteuse (niveau de preuve L5). Indication d'origine : Non disponible (texte d'indication absent de l'AMM)"
monitor_inn: "selinexor"
predicted_indications: ["drug-induced osteoporosis"]
---

# Selinexor
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

## Selinexor : D'une indication non documentée à l'ostéoporose médicamenteuse
{: .text-alpha }

## Résumé en Une Phrase

Selinexor est un inhibiteur sélectif de l'export nucléaire (XPO1), commercialisé en France sous le nom NEXPOVIO (comprimé pelliculé). Les données compilées pour ce rapport ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**ostéoporose médicamenteuse**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible (texte d'indication absent de l'AMM) |
| Nouvelle Indication Prédite | Ostéoporose médicamenteuse |
| Score de Prédiction TxGNN | 0,9922 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Selinexor (traduction non officielle) : « Dans des études non cliniques, le sélinexor inhibe de manière réversible l'export nucléaire des protéines suppresseurs de tumeurs (TSP), des régulateurs de croissance et des ARNm de protéines oncogènes en bloquant l'exportine 1 (XPO1). L'inhibition de XPO1 par le sélinexor entraîne une accumulation des TSP dans le noyau et une diminution de plusieurs oncoprotéines, telles que c-myc et la cycline D1, un arrêt du cycle cellulaire et l'apoptose des cellules cancéreuses. » Texte original en anglais : "In nonclinical studies, selinexor reversibly inhibits nuclear export of tumor suppressor proteins (TSPs), growth regulators, and mRNAs of oncogenic proteins by blocking exportin 1 (XPO1). XPO1 inhibition by selinexor leads to accumulation of TSPs in the nucleus and reductions in several oncoproteins, such as c-myc and cyclin D1, cell cycle arrest, and apoptosis of cancer cells." ([DailyMed: Xpovio (selinexor) prescribing information, Karyopharm Therapeutics Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6dd2682-75a6-4863-90a8-a3197f6f78a8), version du 2026-05-12 ; consulté le 2026-11-19). D'après les connaissances générales, selinexor est un inhibiteur sélectif de l'export nucléaire qui bloque XPO1 (exportine-1) et retient dans le noyau des protéines suppresseurs de tumeur. Cette description n'a pas été vérifiée à partir du dossier fourni.

Un lien avec la biologie osseuse est plausible mais non démontré : l'inhibition de XPO1 pourrait moduler les voies NF-κB et Wnt/β-caténine, ainsi que l'activité des ostéoclastes et des ostéoblastes. Des travaux précliniques dans l'atteinte osseuse du myélome multiple suggèrent un effet possible sur le remodelage osseux, mais ces éléments ne figurent pas dans les données compilées.

Il faut rester prudent : l'ostéoporose médicamenteuse est généralement un phénotype d'effet indésirable (glucocorticoïdes, inhibiteurs de l'aromatase, etc.). Le score élevé pourrait donc refléter une proximité dans le réseau avec des nœuds d'effets indésirables osseux plutôt qu'un véritable signal thérapeutique. Le sens de l'effet (protecteur ou délétère) reste non résolu.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 64317942 | NEXPOVIO 20 mg, comprimé pelliculé | Comprimé pelliculé | STEMLINE THERAPEUTICS (PAYS-BAS) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur sélectif de l'export nucléaire, XPO1), d'après les connaissances générales |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice (NFS, fonction hépatique et rénale à envisager) |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

**Interactions médicamenteuses** : 81 interactions ont été identifiées (source : DDInter). Parmi les principales :

- **Majeures** : deferiprone, samarium (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribine, clozapine
- **Modérées** : chlorure de strontium Sr-89, roflumilast, chloramphénicol (y compris ophtalmique), zidovudine, alefacept, alemtuzumab, anakinra, azathioprine, canakinumab, vaccin anthrax, anatoxine tétanique, vaccin vivant contre le choléra

Les mises en garde et contre-indications de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur un score de modèle (niveau L5), sans essai clinique ni publication. La direction de l'effet (protecteur ou délétère) est incertaine.

<!-- review:begin fr-lic-20261106-selinexor-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La direction de l'effet (protecteur ou délétère) est incertaine, et l'AMM française est annulée. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-selinexor-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice ANSM (mises en garde et contre-indications), car l'absence de ces données bloque le criblage de sécurité
- Données sur le mécanisme d'action issues de DrugBank
- Revue de la littérature préclinique et clinique sur XPO1 et le métabolisme osseux
- Clarification du sens de l'effet (bénéfique ou délétère) pour l'ostéoporose médicamenteuse
- Confirmation de l'indication d'origine et de la situation réglementaire
- Évaluation de la compatibilité des voies d'administration

<!-- review:begin fr-lic-20261106-selinexor-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Confirmation de l'indication d'origine et de la situation réglementaire (AMM annulée) » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-selinexor-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « et l'AMM française est annulée » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulée) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Xpovio (selinexor) prescribing information, Karyopharm Therapeutics Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6dd2682-75a6-4863-90a8-a3197f6f78a8) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

