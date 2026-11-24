---
layout: default
title: Vismodegib
parent: Prédiction du modèle uniquement (L5)
nav_order: 817
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Vismodegib : nouvelle indication prédite, Médulloblastome avec nodularité extensive (niveau de preuve L5). Indication d'origine : Carcinome basocellulaire (et autres cancers cutanés ou annexiels)"
monitor_inn: "vismodegib"
predicted_indications: ["medulloblastoma with extensive nodularity", "xeroderma pigmentosum", "annular epidermolytic ichthyosis", "epidermolysis bullosa simplex with mottled pigmentation", "Brenner tumor", "cutaneous adenocystic carcinoma", "prostate leiomyoma", "benign neoplasm of sweat gland"]
---

# Vismodegib
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Vismodégib : Du carcinome basocellulaire au médulloblastome avec nodularité extensive
{: .text-alpha }

## Résumé en Une Phrase

Le vismodégib (ERIVEDGE 150 mg, gélule) est un inhibiteur de la voie Hedgehog, initialement utilisé pour traiter le carcinome basocellulaire et d'autres cancers cutanés.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **médulloblastome avec nodularité extensive**.
Pour cette indication précise, **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome basocellulaire (et autres cancers cutanés ou annexiels) |
| Nouvelle Indication Prédite | Médulloblastome avec nodularité extensive |
| Score de Prédiction TxGNN | 0,9993 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Vismodegib (traduction non officielle) : « Le vismodégib est un inhibiteur de la voie Hedgehog. Le vismodégib se lie à Smoothened, une protéine transmembranaire impliquée dans la transduction du signal Hedgehog, et l'inhibe. » Texte original en anglais : "Vismodegib is an inhibitor of the Hedgehog pathway. Vismodegib binds to and inhibits Smoothened, a transmembrane protein involved in Hedgehog signal transduction." ([DailyMed: Erivedge (vismodegib) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eb368bb6-80e3-4df9-8a85-91df0a2ada6a), version du 2024-12-02 ; consulté le 2026-11-19). D'après les informations connues, le vismodégib inhibe la protéine Smoothened (SMO) de la voie de signalisation Hedgehog. Cette voie est anormalement activée dans le carcinome basocellulaire, ce qui explique l'efficacité du médicament dans cette indication.

Le médulloblastome du sous-groupe SHH est lui aussi porté par une activation de la voie Hedgehog. Le lien biologique est donc plausible : le même point d'action (SMO) pourrait être pertinent dans les deux maladies.

Cette plausibilité reste théorique. Les données compilées ne contiennent ni essai ni publication portant sur ce sous-type de médulloblastome. Le soutien se limite à la prédiction du modèle, sans confirmation clinique.

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
| 67507605 | ERIVEDGE 150 mg, gélule | Gélule | ROCHE REGISTRATION (ALLEMAGNE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de la voie Hedgehog / SMO), et non cytotoxique conventionnel |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter la notice ; appliquer les règles de manipulation des médicaments anticancéreux oraux |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 56 interactions sont référencées. Parmi celles listées dans les données compilées :
  - **Modérée** : clarithromycine.
  - **Mineures** : antiacides et protecteurs gastriques, dont les inhibiteurs de la pompe à protons (oméprazole, ésoméprazole, lansoprazole, pantoprazole, rabéprazole, dexlansoprazole), les anti-H2 (famotidine, ranitidine, cimétidine, nizatidine), l'hydroxyde d'aluminium, le carbonate de calcium, les sels de magnésium, le bicarbonate de sodium et le citrate de sodium.
- **Contexte pour d'autres indications** : la littérature associée à d'autres indications prédites signale des effets indésirables connus (alopécie, spasmes musculaires, dysgueusie, perte de poids) et une tératogénicité. La sécurité chez l'enfant demande une attention particulière, ce qui est pertinent pour le médulloblastome, fréquent dans cette population.

Pour les mises en garde et contre-indications détaillées, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le lien mécanistique (inhibition de SMO dans un médulloblastome dépendant de Hedgehog) est plausible. Mais l'indication repose uniquement sur le score du modèle, sans essai ni publication.

<!-- review:begin fr-lic-20261106-vismodegib-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Mais l'indication repose uniquement sur le score du modèle, sans essai ni publication, et l'unique AMM française est annulée. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-vismodegib-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Une recherche ciblée de données précliniques et cliniques sur le médulloblastome du sous-groupe SHH traité par inhibiteurs de SMO.
- Les données détaillées sur le mécanisme d'action.
- Les mises en garde et contre-indications officielles de la notice.
- Une évaluation de la sécurité pédiatrique (tératogénicité, effets sur la croissance).
- Une clarification du statut réglementaire en France.

<!-- review:begin fr-lic-20261106-vismodegib-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Une clarification du statut réglementaire en France, l'AMM étant annulée. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-vismodegib-2 -->

À titre d'orientation complémentaire, parmi les autres indications prédites, le **xeroderma pigmentosum** est la mieux documentée (trois publications, dont deux cas cliniques de traitement par vismodégib de carcinomes basocellulaires associés). L'effet est cependant indirect : il traite la complication tumorale et non le défaut de réparation de l'ADN.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « et l'unique AMM française est annulée » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « l'AMM étant annulée » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Erivedge (vismodegib) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eb368bb6-80e3-4df9-8a85-91df0a2ada6a) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

