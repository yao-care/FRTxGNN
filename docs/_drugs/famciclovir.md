---
layout: default
title: Famciclovir
parent: Prédiction du modèle uniquement (L5)
nav_order: 315
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Famciclovir : nouvelle indication prédite, Névralgie post-infectieuse (niveau de preuve L5). Indication d'origine : Zona (herpès zoster)"
monitor_inn: "FAMCICLOVIR"
predicted_indications: ["post-infectious neuralgia", "sequela of COVID-19", "hepatitis C induced liver cirrhosis", "malignant pleural mesothelioma", "AIDS-related disorder", "malignant epithelioid mesothelioma", "chickenpox", "sarcomatoid mesothelioma", "malignant visceral pleura tumor"]
---

# Famciclovir
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

## Famciclovir : Du Zona à la Névralgie Post-Infectieuse
{: .text-alpha }

## Résumé en Une Phrase

Famciclovir est un antiviral, prodrogue du penciclovir, initialement utilisé pour le traitement du zona (herpès zoster).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **névralgie post-infectieuse** (névralgie post-zostérienne), mais **aucune publication** et **1 seul essai clinique** (sans lien direct avec le famciclovir) ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Zona (herpès zoster) |
| Nouvelle Indication Prédite | Névralgie post-infectieuse |
| Score de Prédiction TxGNN | 0,9975 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Famciclovir (traduction non officielle) : « Le famciclovir est une prodrogue administrée par voie orale de l'agent antiviral anti-alphaherpèsvirus penciclovir. » Texte original en anglais : "Famciclovir is an orally administered prodrug of the anti-alpha herpes viral agent penciclovir." ([DailyMed: famciclovir prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2c44b8d2-3b70-4e8b-af03-2e917178f761), version du 2026-11-13 ; consulté le 2026-11-19). Sur la base des informations connues, le famciclovir est une prodrogue du penciclovir : sous sa forme active (penciclovir triphosphate), il inhibe l'ADN polymérase du virus varicelle-zona (VZV).

Le zona est la maladie en amont de la névralgie post-zostérienne, qui en est la complication la plus fréquente. Réduire la réplication virale en phase aiguë pourrait limiter les lésions nerveuses et donc le risque de névralgie persistante. Ce lien est plausible sur le plan biologique, mais indirect.

Il faut souligner que le seul essai retrouvé teste l'oxycodone et non le famciclovir. Il n'apporte donc aucune preuve directe d'un bénéfice du famciclovir sur cette complication. Le score élevé du modèle reste, à ce stade, une prédiction.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | Non applicable | Inconnu | 140 | Effet de l'oxycodone précoce en phase aiguë du zona sur la prévention de la névralgie post-zostérienne. Le famciclovir n'est pas l'intervention étudiée. |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 69092403 | ORAVIR 125 mg, comprimé pelliculé | Comprimé pelliculé | PHOENIX LABS (IRLANDE) | Active |
| 62801318 | ORAVIR 500 mg, comprimé pelliculé | Comprimé pelliculé | PHOENIX LABS (IRLANDE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (hors notice)** : maladie rénale, pyourétère.
- **Interactions Médicamenteuses** : 84 interactions recensées, toutes de niveau « inconnu ». Parmi les médicaments concernés : calcitriol, doxycycline, clotrimazole, pantoprazole, glimépiride, morphine, metformine, oméprazole, vancomycine, prednisone, simvastatine.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être exploitées. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le lien mécanistique est plausible, mais aucune preuve directe n'existe : le seul essai associé n'évalue pas le famciclovir et aucune publication n'est disponible.

<!-- review:begin fr-lic-20261106-famciclovir-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Le lien mécanistique est plausible, mais aucune preuve directe n'existe : le seul essai associé n'évalue pas le famciclovir et aucune publication n'est disponible. De plus, les deux AMM françaises sont annulées, ce qui limite toute avancée pratique. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-famciclovir-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank)
- Mises en garde et contre-indications officielles de la notice (ANSM)
- Essais ou études évaluant spécifiquement le famciclovir sur la prévention ou le traitement de la névralgie post-zostérienne
- Évaluation de la faisabilité réglementaire, étant donné l'absence d'AMM valide en France

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « De plus, les deux AMM françaises sont annulées, ce qui limite toute avancée pratique » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: famciclovir prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2c44b8d2-3b70-4e8b-af03-2e917178f761) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

