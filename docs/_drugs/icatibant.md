---
layout: default
title: Icatibant
parent: Prédiction du modèle uniquement (L5)
nav_order: 386
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "icatibant"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "pseudo-von Willebrand disease", "primary release disorder of platelets", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "Glanzmann thrombasthenia"]
description: "Icatibant : nouvelle indication prédite, Serpinopathy with toxic serpin polymerization (niveau de preuve L5). En France, AMM dans la BDPM : 7 (valides : 7)"
---

# Icatibant
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Icatibant: Serpinopathy with toxic serpin polymerization
{: .text-alpha }

## Résumé en Une Phrase

Icatibant est un antagoniste du récepteur B2 de la bradykinine, initialement utilisé pour traiter les crises d'angioedème héréditaire (y compris avec déficit en inhibiteur de la C1).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **déficit en inhibiteur de la C1** (notamment sa forme acquise), avec **11 essais cliniques** et **20 publications** soutenant actuellement cette direction.
Il convient de noter que cette prédiction recoupe en grande partie l'indication d'origine : il ne s'agit pas d'un repositionnement au sens strict.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Serpinopathy with toxic serpin polymerization |
| Score de Prédiction TxGNN | 0.9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 7 sur 7) |
| Nombre d'AMM | 7 (valides : 7) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Icatibant (traduction non officielle) : « L'icatibant est un antagoniste compétitif sélectif du récepteur B2 de la bradykinine, avec une affinité similaire à celle de la bradykinine. L'angio-œdème héréditaire est dû à une absence ou à un dysfonctionnement de l'inhibiteur de la C1-estérase, un régulateur clé de la cascade protéolytique facteur XII/kallicréine qui aboutit à la production de bradykinine. » Texte original en anglais : "Icatibant is a competitive antagonist selective for the bradykinin B2 receptor, with an affinity similar to bradykinin. Hereditary angioedema is caused by an absence or dysfunction of C1-esterase-inhibitor, a key regulator of the Factor XII/kallikrein proteolytic cascade that leads to bradykinin production." ([DailyMed: Firazyr (icatibant acetate) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ed6657ca-ab68-477a-9968-e12dc928b540), version du 2025-07-07 ; consulté le 2026-11-19). D'après les connaissances pharmacologiques générales, icatibant est un décapeptide antagoniste sélectif du récepteur B2 de la bradykinine. Les données de pharmacologie indiquent également une interaction avec le récepteur B1 (gène BDKRB1) et le récepteur B2 (gène BDKRB2).

Dans le déficit en inhibiteur de la C1, l'activité du système kallikréine-kinine n'est plus régulée, ce qui entraîne un excès de bradykinine, médiateur des crises d'angioedème. En bloquant le récepteur B2, icatibant neutralise directement cette voie. Le déficit en inhibiteur de la C1 correspond d'ailleurs à l'indication d'origine (angioedème héréditaire avec déficit en C1-Inh).

L'extension à la forme acquise du déficit est cohérente sur le plan mécanistique, car elle repose sur la même voie médiée par la bradykinine. Une série observationnelle en conditions réelles chez 8 patients (48 crises traitées) va dans ce sens. Les données disponibles restent toutefois limitées pour cette forme acquise.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00097695](https://clinicaltrials.gov/study/NCT00097695) | Phase 3 | Terminé | 84 | Étude randomisée en double aveugle contre placebo : efficacité et sécurité d'icatibant sous-cutané dans les crises cutanées et/ou abdominales d'AAH |
| [NCT00500656](https://clinicaltrials.gov/study/NCT00500656) | Phase 3 | Terminé | 85 | Icatibant contre acide tranexamique oral, randomisé en double aveugle ; critère principal : délai d'apparition du soulagement |
| [NCT00912093](https://clinicaltrials.gov/study/NCT00912093) | Phase 3 | Terminé | 98 | Étude randomisée en double aveugle contre placebo dans les crises aiguës d'angioedème héréditaire |
| [NCT00997204](https://clinicaltrials.gov/study/NCT00997204) | Phase 3 | Terminé | 151 | Étude ouverte sur l'auto-administration : sécurité, tolérance locale et efficacité |
| [NCT01386658](https://clinicaltrials.gov/study/NCT01386658) | Phase 3 | Terminé | 32 | Pharmacocinétique, tolérance et sécurité d'une dose unique chez l'enfant et l'adolescent |
| [NCT03888755](https://clinicaltrials.gov/study/NCT03888755) | Phase 3 | Terminé | 8 | Étude ouverte chez des patients japonais (AAH de type I ou II) |
| [NCT01457430](https://clinicaltrials.gov/study/NCT01457430) | Phase 4 | Terminé | 19 | Auto-administration : sécurité, tolérance locale, commodité et efficacité |
| [NCT04057131](https://clinicaltrials.gov/study/NCT04057131) | N/A | Terminé | 179 | Enquête japonaise de suivi post-commercialisation (sécurité et efficacité) |
| [NCT05509569](https://clinicaltrials.gov/study/NCT05509569) | N/A | Terminé | 32 | Surveillance pédiatrique japonaise après commercialisation |
| [NCT04654351](https://clinicaltrials.gov/study/NCT04654351) | Phase 3 | Terminé | 2 | Étude ouverte chez des enfants et adolescents japonais ; effectif trop faible pour conclure |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [29757016](https://pubmed.ncbi.nlm.nih.gov/29757016/) | 2018 | Cohorte / revue | Expert Rev Clin Immunol | Sécurité et efficacité d'icatibant chez l'adolescent et l'enfant de plus de 2 ans (études randomisées, ouvertes et observationnelles) |
| [22686628](https://pubmed.ncbi.nlm.nih.gov/22686628/) | 2012 | Étude observationnelle | Allergy | Icatibant dans le déficit acquis en C1-Inh : 8 patients, 48 crises modérées à sévères traitées |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Revue systématique | Pneumonol Alergol Pol | Comparaison de l'efficacité de conestat alfa, de l'inhibiteur de la C1 humain et d'icatibant |
| [20030426](https://pubmed.ncbi.nlm.nih.gov/20030426/) | 2010 | Revue | Drugs | Essai FAST-1 : critère principal non significatif, mais efficacité sur plusieurs autres critères |
| [32753245](https://pubmed.ncbi.nlm.nih.gov/32753245/) | 2020 | Recommandations | Rev Med Interne | Recommandations CREAK pour le diagnostic et le traitement de l'angioedème acquis par déficit en C1-Inh |
| [37716525](https://pubmed.ncbi.nlm.nih.gov/37716525/) | 2023 | Étude rétrospective | J Allergy Clin Immunol Pract | Étude bicentrique de l'angioedème acquis : diagnostic, évolution, traitement ; aucun traitement homologué |
| [28687105](https://pubmed.ncbi.nlm.nih.gov/28687105/) | 2017 | Revue | Immunol Allergy Clin North Am | Déficit acquis en inhibiteur de la C1 : association avec l'auto-immunité et les hémopathies lymphoïdes B |
| [20667117](https://pubmed.ncbi.nlm.nih.gov/20667117/) | 2010 | Revue | Allergy Asthma Clin Immunol | Angioedème acquis médié par la bradykinine |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Revue | J Investig Allergol Clin Immunol | Prise en charge actuelle de l'angioedème héréditaire |
| [21284353](https://pubmed.ncbi.nlm.nih.gov/21284353/) | 2010 | Évaluation | Prescrire Int | Pour les crises, l'inhibiteur de la C1 estérase reste le traitement de première intention |

---

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 66169887 | ICATIBANT ACCORD 30 mg, solution injectable en seringue préremplie | Solution injectable | ACCORD HEALTHCARE (ESPAGNE) | Active |
| 61680479 | FIRAZYR 30 mg, solution injectable en seringue pré-remplie | Solution injectable | TAKEDA PHARMACEUTICALS INTERNATIONAL (IRLANDE) | Active |
| 68903664 | ICATIBANT PIRAMAL 30 mg, solution injectable en seringue pré-remplie | Solution injectable | PIRAMAL CRITICAL CARE (PAYS-BAS) | Active |
| 69800927 | ICATIBANT FRESENIUS 30 mg, solution injectable en seringue préremplie | Solution injectable | FRESENIUS KABI FRANCE | Active |
| 63030672 | ICATIBANT VIATRIS 30 mg, solution injectable en seringue préremplie | Solution injectable | VIATRIS SANTE | Active |
| 62044509 | ICATIBANT ZENTIVA 30 mg, solution injectable en seringue préremplie | Solution injectable | ZENTIVA FRANCE | Active |
| 64043021 | ICATIBANT HIKMA 30 mg, solution injectable en seringue préremplie | Solution injectable | HIKMA FARMACEUTICA (PORTUGAL) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

Les AMM recensées figurent dans le tableau ci-dessus.

<!-- review:begin fr-lic-20261106-icatibant-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Au total, 7 AMM sont recensées, toutes annulées. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-icatibant-1 -->

---

## Considérations de Sécurité

- **Interactions médicamenteuses** : 10 interactions de niveau modéré sont recensées avec les inhibiteurs de l'enzyme de conversion (IEC) : bénazépril, captopril, énalapril, périndopril, trandolapril, moexipril, lisinopril, quinapril, ramipril et fosinopril.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 3, dont trois randomisés, soutiennent l'efficacité d'icatibant dans l'angioedème héréditaire avec déficit en C1-Inh, ce qui correspond à l'indication d'origine.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications issues de la notice de l'ANSM (lacune bloquante pour le dépistage de sécurité)
- Données détaillées sur le mécanisme d'action (DrugBank)
- Études prospectives ou contrôlées dans le déficit acquis en inhibiteur de la C1
- Clarification du statut réglementaire français et du texte d'indication
- Plan de gestion des interactions avec les IEC

<!-- review:begin fr-lic-20261106-icatibant-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarification du statut réglementaire français (AMM toutes annulées) et du texte d'indication » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-icatibant-2 -->

**Autres prédictions (niveau L5, décision : Hold) :** les six autres indications prédites (serpinopathie avec polymérisation toxique, pseudo-maladie de von Willebrand, trouble de la sécrétion plaquettaire, myopathie nécrosante à médiation immune, syndrome des antisynthétases, thrombasthénie de Glanzmann) ne reposent sur aucun essai ni publication.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « toutes annulées » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM toutes annulées) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Firazyr (icatibant acetate) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ed6657ca-ab68-477a-9968-e12dc928b540) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

