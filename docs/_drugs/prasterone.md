---
layout: default
title: Prasterone
parent: Prédiction du modèle uniquement (L5)
nav_order: 621
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Prasterone : nouvelle indication prédite, Déficience en cofacteur II de l'héparine (niveau de preuve L5). Indication d'origine : Non précisée dans les données d'AMM"
monitor_inn: "prasterone"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "severe nonproliferative diabetic retinopathy", "thrombophilia due to protein S deficiency, autosomal recessive", "scleroderma (disease)", "complement component 4a deficiency", "pseudo-von Willebrand disease", "primary release disorder of platelets"]
---

# Prasterone
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Prastérone : De la dyspareunie psychologique à la déficience en cofacteur II de l'héparine
{: .text-alpha }

## Résumé en Une Phrase

La prastérone (DHEA) est utilisée à l'origine pour traiter la dyspareunie (douleur lors des rapports sexuels) liée à l'atrophie vulvo-vaginale. Dans la base de connaissances du modèle, elle est aussi associée au lupus érythémateux systémique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **déficience en cofacteur II de l'héparine**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données d'AMM ; la base de connaissances indique : lupus érythémateux systémique, lupus érythémateux systémique pédiatrique, dyspareunie psychologique |
| Nouvelle Indication Prédite | Déficience en cofacteur II de l'héparine |
| Score de Prédiction TxGNN | 0,9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Prasterone (traduction non officielle) : « La prastérone est un stéroïde endogène inactif qui est converti en androgènes et/ou en œstrogènes actifs. Le mécanisme d'action d'INTRAROSA chez les femmes ménopausées présentant une atrophie vulvaire et vaginale n'est pas entièrement établi. » Texte original en anglais : "Prasterone is an inactive endogenous steroid and is converted into active androgens and/or estrogens. The mechanism of action of INTRAROSA in postmenopausal women with vulvar and vaginal atrophy is not fully established." ([DailyMed: Intrarosa (prasterone) prescribing information, Millicent US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ada639d4-bac0-2ad0-e053-2a95a90afce7), version du 2026-07-17 ; consulté le 2026-11-19). Sur la base des informations connues, la prastérone est la forme pharmaceutique de la déhydroépiandrostérone (DHEA), un précurseur stéroïdien converti localement en androgènes et en œstrogènes. Elle a été utilisée dans la dyspareunie liée à l'atrophie vulvo-vaginale. Les données de pharmacologie compilées mentionnent aussi une interaction avec le récepteur de la glycine (tous sous-types).

Aucun lien mécanistique établi ne relie la DHEA à la déficience en cofacteur II de l'héparine (SERPIND1), un défaut d'un inhibiteur de la coagulation de la famille des serpines. Tout lien serait spéculatif (par exemple, des effets indirects des androgènes et œstrogènes sur l'hémostase). Le score élevé provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, non une preuve biologique ; il n'est corroboré par aucune donnée clinique.

Les autres prédictions les mieux classées (déficit en facteur V, déficit en antithrombine de type 2, thrombophilie, déficit en protéine S) relèvent également de troubles de la coagulation, sans mécanisme plausible identifié. Un lien indirect est évoqué pour la sclérodermie, en raison de l'activité immunomodulatrice de la DHEA dans les maladies auto-immunes, mais il reste une hypothèse, également de niveau L5.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 60073960 | INTRAROSA 6,5 mg, ovule | Ovule | ENDOCEUTICS (BELGIQUE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Interactions et pharmacologie** : une seule entrée a été relevée, concernant le récepteur de la glycine (tous sous-types), sans niveau de gravité précisé.
- **Point de vigilance** : la prastérone étant convertie en androgènes et en œstrogènes, ses effets sur l'hémostase sont incertains et pourraient être prothrombotiques. Ce point est particulièrement préoccupant dans les pathologies thrombotiques ou thrombophiliques ciblées par les prédictions.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, sans mécanisme plausible, et avec un risque thrombotique potentiel.

<!-- review:begin fr-lic-20261106-prasterone-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, sans mécanisme plausible, et avec un risque thrombotique potentiel. Le produit n'a plus d'AMM en vigueur en France. » Supprimé : l'affirmation contredisait les données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-prasterone-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank), pour analyser un éventuel lien avec la voie de la coagulation
- Mises en garde et contre-indications de la notice ANSM, indispensables à l'évaluation de sécurité
- Revue systématique de la littérature sur la DHEA et l'hémostase/la thrombose
- Évaluation de la compatibilité de la voie d'administration (ovule vaginal) avec les indications visées
- Réévaluation éventuelle de pistes plus plausibles sur le plan mécanistique, comme la sclérodermie, après revue de la littérature

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Le produit n'a plus d'AMM en vigueur en France » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Intrarosa (prasterone) prescribing information, Millicent US, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ada639d4-bac0-2ad0-e053-2a95a90afce7) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

