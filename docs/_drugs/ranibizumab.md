---
layout: default
title: Ranibizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 651
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "RANIBIZUMAB"
predicted_indications: ["immature cataract", "mature cataract", "tetanic cataract", "craniostenosis cataract", "diabetes mellitus type 2 associated cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "hemorrhagic disease of newborn"]
description: "Ranibizumab : nouvelle indication prédite, Immature cataract (niveau de preuve L5). En France, AMM dans la BDPM : 7 (valides : 7)"
---

# Ranibizumab
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

## Ranibizumab: Immature cataract
{: .text-alpha }

## Résumé en Une Phrase

Le ranibizumab est un fragment d'anticorps anti-VEGF, initialement utilisé pour traiter des maladies vasculaires de la rétine (rétinopathie diabétique, œdème maculaire diabétique, dégénérescence maculaire).
avec **19 publications** soutenant actuellement cette direction, mais **aucun essai clinique enregistré** dans les données compilées pour cette indication.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Immature cataract |
| Score de Prédiction TxGNN | 0.9999 |
| Niveau de Preuve | L5 (à confirmer, voir ci-dessous) |
| Statut de Marché en France | Commercialisé (autorisations valides : 7 sur 7) |
| Nombre d'AMM | 7 (valides : 7) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Ranibizumab (traduction non officielle) : « Les produits à base de ranibizumab se lient au site de liaison au récepteur des formes actives du VEGF-A, y compris la forme clivée biologiquement active de cette molécule, le VEGF110. Il a été démontré que le VEGF-A provoque une néovascularisation et des fuites dans des modèles d'angiogenèse oculaire et d'occlusion vasculaire, et on pense qu'il contribue à la physiopathologie de la DMLA néovasculaire, de la NVC myopique, de la RD, de l'OMD et de l'œdème maculaire consécutif à une OVR. » Texte original en anglais : "Ranibizumab products bind to the receptor binding site of active forms of VEGF-A, including the biologically active, cleaved form of this molecule, VEGF110. VEGF-A has been shown to cause neovascularization and leakage in models of ocular angiogenesis and vascular occlusion and is thought to contribute to pathophysiology of neovascular AMD, mCNV, DR, DME and macular edema following RVO." ([DailyMed: Nufymco (ranibizumab-leyk) prescribing information, Zydus Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=05ed75bc-ae21-480b-9be4-cbc51689dd8a), version du 2026-11-05 ; consulté le 2026-11-19). Sur la base des informations connues, le ranibizumab fait partie de la classe des anti-VEGF (fragment d'anticorps dirigé contre le VEGF-A). Son efficacité dans la rétinopathie diabétique et l'œdème maculaire diabétique est documentée, et mécanistiquement il est applicable à la rétinopathie non proliférante sévère.

Le VEGF favorise la perméabilité vasculaire rétinienne et la néovascularisation dans la rétinopathie diabétique. Des taux élevés de VEGF sériques et vitréens sont décrits dans cette maladie. La forme non proliférante sévère est un stade de la même maladie que l'indication d'origine : le lien est donc direct.

La littérature comprend des analyses post hoc des essais de phase 3 RIDE/RISE montrant une régression de la sévérité de la rétinopathie sous ranibizumab, ainsi qu'un essai randomisé du système de délivrance par port (PAVILION) dans la rétinopathie diabétique non proliférante. **Réserve :** aucun essai enregistré n'accompagne cette indication, et le niveau L1 repose sur les titres de publications, dont la conception et la phase n'ont pas été vérifiées à partir des résumés.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour cette indication.

<!-- review:begin fr-lic-20261106-ranibizumab-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Une sixième AMM annulée existe (RIMMYRAH 10 mg/ml, solution injectable, n° 61190863). » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 6 AMM pour ce médicament, dont 6 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-ranibizumab-1 -->

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | ECR | JAMA Ophthalmol | Système de délivrance par port de ranibizumab vs surveillance dans la RD non proliférante sans œdème maculaire (essai PAVILION) |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Méta-analyse (post hoc d'ECR) | Ophthalmol Retina | Lien entre la sévérité initiale de la RD et le délai de résolution de l'œdème maculaire sous ranibizumab |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Analyse post hoc d'ECR | Clin Ophthalmol | Prédicteurs de régression précoce de la RD dans RIDE/RISE |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | Extension ouverte d'ECR | BMJ Open Ophthalmol | Évolution du score de sévérité de la RD avec un traitement moins fréquent après induction |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | Analyse secondaire d'ECR | JAMA Ophthalmol | Évolution de la RD à 2 ans : aflibercept, bévacizumab et ranibizumab |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | Analyse d'ECR (DRCR.net Protocole I) | Retina | Changements de sévérité de la RD à 5 ans sous ranibizumab |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2025 | Revue systématique et méta-analyse | Health Technol Assess | Anti-VEGF vs photocoagulation laser dans la RD |
| [42219053](https://pubmed.ncbi.nlm.nih.gov/42219053/) | 2026 | Revue systématique et méta-analyse | Eur J Pharmacol | Système de délivrance par port de ranibizumab dans la RD et l'œdème maculaire diabétique |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Revue | Expert Opin Biol Ther | Ranibizumab dans le traitement de la rétinopathie diabétique |
| [40969370](https://pubmed.ncbi.nlm.nih.gov/40969370/) | 2025 | Cohorte rétrospective | Front Endocrinol | Nomogramme prédictif de réponse à l'anti-VEGF + laser dans la RD non proliférante sévère |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 68654266 | BYOOVIZ 10 mg/mL, solution injectable | Solution injectable | SAMSUNG BIOEPIS NL (PAYS-BAS) | Active |
| 64339586 | LUCENTIS 10 mg/ml, solution injectable en seringue préremplie | Solution injectable | NOVARTIS EUROPHARM (IRLANDE) | Active |
| 68594506 | RANIVISIO 10 mg/mL, solution injectable en seringue préremplie | Solution injectable | MIDAS PHARMA (ALLEMAGNE) | Active |
| 64389258 | RANIVISIO 10 mg/mL, solution injectable | Solution injectable | MIDAS PHARMA (ALLEMAGNE) | Active |
| 67026689 | XIMLUCI 10 mg/mL, solution injectable | Solution injectable | STADA ARZNEIMITTEL AG | Active |
| 61190863 | RIMMYRAH 10 mg/ml, solution injectable | Solution injectable | QILU PHARMA SPAIN (ESPAGNE) | Active |
| 66082489 | BYOOVIZ 10 mg/mL, solution injectable en seringue préremplie | Solution injectable | SAMSUNG BIOEPIS NL (PAYS-BAS) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : infection oculaire, conjonctivite.

Pour le reste, veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le lien mécanistique est direct (anti-VEGF dans une rétinopathie VEGF-dépendante) et la littérature inclut des analyses d'essais de phase 3 (RIDE/RISE) et un ECR dans la RD non proliférante.

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmer directement la conception, la phase et les résultats des essais (RIDE/RISE, PAVILION)
- Vérifier la disponibilité et le statut réglementaire actuels en France
- Obtenir la notice (mises en garde, contre-indications) auprès de l'ANSM
- Obtenir les données sur le mécanisme d'action

<!-- review:begin fr-lic-20261106-ranibizumab-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Vérifier la disponibilité et le statut réglementaire actuels en France (AMM annulées ; autres procédures éventuelles) » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 6 AMM pour ce médicament, dont 6 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-ranibizumab-2 -->

## Autres indications prédites (non retenues)

Décision : **Hold**. À noter, un cas de syndrome de blocage capsulaire après injection de ranibizumab a été rapporté (effet indésirable, pas un bénéfice thérapeutique).

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Une sixième AMM annulée existe (RIMMYRAH 10 mg/ml, solution injectable, n° 61190863) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulées ; autres procédures éventuelles) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Nufymco (ranibizumab-leyk) prescribing information, Zydus Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=05ed75bc-ae21-480b-9be4-cbc51689dd8a) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

