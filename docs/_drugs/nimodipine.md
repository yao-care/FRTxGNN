---
layout: default
title: Nimodipine
parent: Prédiction du modèle uniquement (L5)
nav_order: 537
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "NIMODIPINE"
predicted_indications: ["homozygous familial hypercholesterolemia", "nephrogenic syndrome of inappropriate antidiuresis"]
description: "Nimodipine : nouvelle indication prédite, Hypercholestérolémie familiale homozygote (homozygous familial hypercholesterolemia) (niveau de preuve L5). Indication d'origine : Non renseignée dans les do…"
---

# Nimodipine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Nimodipine: Hypercholestérolémie familiale homozygote (homozygous familial hypercholesterolemia)
{: .text-alpha }

## Résumé en Une Phrase

Nimodipine est un inhibiteur calcique de type dihydropyridine, initialement utilisé pour la prise en charge de l'hémorragie sous-arachnoïdienne (notamment anévrismale).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypercholestérolémie familiale homozygote**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hypercholestérolémie familiale homozygote (homozygous familial hypercholesterolemia) |
| Score de Prédiction TxGNN | 0.9929 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Nimodipine (traduction non officielle) : « La nimodipine est un inhibiteur calcique de la famille des dihydropyridines. Les processus contractiles des cellules musculaires lisses dépendent des ions calcium, qui pénètrent dans ces cellules lors de la dépolarisation sous forme de courants ioniques transmembranaires lents. » Texte original en anglais : "Nimodipine is a dihydropyridine calcium channel blocker. The contractile processes of smooth muscle cells are dependent upon calcium ions, which enter these cells during depolarization as slow ionic transmembrane currents." ([DailyMed: Nymalize (nimodipine) prescribing information, Azurity Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e660fa26-b5c4-4d6d-8887-9e22b6666a10), version du 2024-08-30 ; consulté le 2026-11-19). Sur la base des informations connues, la nimodipine est un inhibiteur calcique de la classe des dihydropyridines, à activité préférentielle sur la circulation cérébrale. Son intérêt dans l'hémorragie sous-arachnoïdienne repose sur cette action vasculaire cérébrale.

La relation avec la nouvelle indication reste très fragile. L'hypercholestérolémie familiale homozygote résulte d'un défaut d'élimination du LDL-cholestérol (dysfonction du récepteur du LDL, d'APOB, de PCSK9 ou de LDLRAP1). Aucun lien mécanistique établi n'existe avec le blocage des canaux calciques de type L. Un éventuel effet vasculaire ou antiathérosclérotique des inhibiteurs calciques serait spéculatif et ne corrigerait pas le défaut sous-jacent du métabolisme lipidique.

Le score élevé de TxGNN (0,9929) est une prédiction informatique, non corroborée par des données cliniques ou bibliographiques. À noter que la seconde prédiction du modèle (syndrome néphrogénique d'antidiurèse inappropriée, score de 0,9905) n'est pas non plus étayée : elle relève d'un mécanisme (récepteur V2 de la vasopressine) sans lien démontré avec les canaux calciques.

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
| 65726536 | NIMOTOP 30 mg, comprimé pelliculé | Comprimé pelliculé | LABORATOIRE XO | Active |
| 61339638 | NIMOTOP 10 mg/50 ml, solution injectable pour perfusion | Solution injectable pour perfusion | LABORATOIRE XO | Active |
| 60193835 | NIMODIPINE ALTAN 10 mg/50 mL, solution injectable/pour perfusion | Solution injectable pour perfusion | ALTAN PHARMACEUTICALS (ESPAGNE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (ne provenant pas de la notice) : maladie hépatique, maladie de la vésicule biliaire, troubles hypotenseurs.
- **Interactions médicamenteuses** : 100 interactions recensées, dont les principales sont :
  - **Majeures** : clarithromycine, dolasétron.
  - **Modérées** (exemples) : bupropion, aprépitant, morphine, acide acétylsalicylique, cimétidine, miconazole, sulfate de magnésium, canagliflozine, dapagliflozine, empagliflozine, dronabinol, nabilone, kanamycine, néomycine, sels de calcium (carbonate, chlorure, acétate, phosphate).

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible avec la physiopathologie de l'hypercholestérolémie familiale homozygote.
- Les données de sécurité officielles sont manquantes, ce qui empêche à ce stade tout examen de sécurité.

<!-- review:begin fr-lic-20261106-nimodipine-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les AMM françaises sont toutes annulées et les données de sécurité officielles sont manquantes, ce qui empêche à ce stade tout examen de sécurité. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-nimodipine-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice auprès de l'ANSM (lacune bloquante).
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank).
- Mener une revue de la littérature et des données précliniques sur un éventuel effet de la nimodipine sur le métabolisme lipidique ou l'athérosclérose.
- Clarifier le statut réglementaire en France et la faisabilité de la voie d'administration.

<!-- review:begin fr-lic-20261106-nimodipine-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarifier le statut réglementaire en France (AMM annulées) et la faisabilité de la voie d'administration. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-nimodipine-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « es AMM françaises sont toutes annulées et l » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulées) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Nymalize (nimodipine) prescribing information, Azurity Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e660fa26-b5c4-4d6d-8887-9e22b6666a10) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

