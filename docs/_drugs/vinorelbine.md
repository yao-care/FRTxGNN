---
layout: default
title: Vinorelbine
parent: Preuves élevées (L1-L2)
nav_order: 816
evidence_level: L2
indication_count: 8
last_modified_at: 2026-11-24
description: "Vinorelbine : nouvelle indication prédite, Sarcome d'Ewing (niveau de preuve L2). Indication d'origine : Cancer bronchique non à petites cellules"
monitor_inn: "vinorelbine"
predicted_indications: ["Ewing sarcoma", "fibromatosis, gingival", "fibroma of lung", "pulmonary sulcus neoplasm", "lung germ cell tumor", "hamartoma of lung", "lung benign neoplasm", "pulmonary blastoma"]
---

# Vinorelbine
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **8** 
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

## Vinorélbine : Du Cancer bronchique non à petites cellules au Sarcome d'Ewing
{: .text-alpha }

## Résumé en Une Phrase

La vinorélbine est un alcaloïde de la pervenche (vinca-alcaloïde), initialement utilisé dans le traitement du cancer bronchique non à petites cellules et du cancer du poumon.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **Sarcome d'Ewing**,
avec **3 essais cliniques** (dont un essai de phase 2 directement pertinent) et **6 publications** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer bronchique non à petites cellules ; cancer du poumon (les textes d'indication des AMM ne sont pas renseignés) |
| Nouvelle Indication Prédite | Sarcome d'Ewing |
| Score de Prédiction TxGNN | 1,0000 |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Commercialisé (autorisations valides : 14 sur 14) |
| Nombre d'AMM | 14 (valides : 14) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Vinorelbine (traduction non officielle) : « La vinorelbine est un alcaloïde de la pervenche qui interfère avec l'assemblage des microtubules. L'activité antitumorale de la vinorelbine serait principalement due à l'inhibition de la mitose en métaphase par son interaction avec la tubuline. La vinorelbine peut également interférer avec : 1) le métabolisme des acides aminés, de l'AMP cyclique et du glutathion, 2) l'activité de l'ATPase de transport du Ca++ dépendante de la calmoduline, 3) la respiration cellulaire, et 4) la biosynthèse des acides nucléiques et des lipides. » Texte original en anglais : "Vinorelbine is a vinca alkaloid that interferes with microtubule assembly. The antitumor activity of vinorelbine is thought to be due primarily to inhibition of mitosis at metaphase through its interaction with tubulin. Vinorelbine may also interfere with: 1) amino acid, cyclic AMP and glutathione metabolism, 2) calmodulin-dependent Ca++-transport ATPase activity, 3) cellular respiration, and 4) nucleic acid and lipid biosynthesis." ([DailyMed: vinorelbine prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10a70995-e04d-4044-b1dc-c9aa27460397), version du 2024-08-16 ; consulté le 2026-11-19). Sur la base des connaissances pharmacologiques établies, la vinorélbine fait partie de la classe des vinca-alcaloïdes : elle se lie à la tubuline et perturbe la dynamique des microtubules, ce qui provoque un arrêt mitotique puis l'apoptose des cellules à division rapide.

Le sarcome d'Ewing est une tumeur à petites cellules rondes très proliférative, qui répond à d'autres agents ciblant les microtubules, comme la vincristine. L'association de la vinorélbine à de faibles doses de cyclophosphamide en continu (schéma métronomique) a montré une activité dans les formes récidivantes ou réfractaires. Des travaux précliniques montrent par ailleurs une synergie entre les agents interférant avec les microtubules (dont la vinorélbine) et un inhibiteur de PLK1 dans des cellules de sarcome d'Ewing.

La relation avec l'indication d'origine est donc surtout mécanistique : le même effet antimitotique, démontré dans le cancer du poumon, pourrait s'appliquer à une tumeur osseuse à forte prolifération. Il s'agit d'un lien plausible, mais indirect.

<!-- review:begin fr-lic-20261106-vinorelbine-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Au total, 8 AMM sont recensées, toutes annulées : 6 capsules molles (voie orale) et 2 solutions à diluer pour perfusion (ARROW et ACCORD, 10 mg/mL). » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-vinorelbine-1 -->

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00180947](https://clinicaltrials.gov/study/NCT00180947) | Phase 2 | Inconnu | 210 | Vinorélbine + cyclophosphamide dans les tumeurs réfractaires ou en rechute (rhabdomyosarcomes, tumeurs d'Ewing, ostéosarcomes, etc.) ; résultats probablement non disponibles |
| [NCT00003234](https://clinicaltrials.gov/study/NCT00003234) | Phase 2 | Terminé | 50 | Vinorélbine chez des enfants atteints de tumeurs malignes récidivantes ou réfractaires ; preuve indirecte, non spécifique à Ewing |
| [NCT06451302](https://clinicaltrials.gov/study/NCT06451302) | Non applicable | Actif, ne recrute plus | 100 | Cohorte prospective multicentrique de traitement stratifié par risque dans le sarcome d'Ewing pédiatrique en Chine ; n'isole pas la contribution de la vinorélbine |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [42561548](https://pubmed.ncbi.nlm.nih.gov/42561548/) | 2026 | Revue systématique / cohorte | Cancer Treat Rev | Justification de la vinorélbine et du cyclophosphamide à faible dose en traitement d'entretien dans l'essai international INTER-EWING-1 |
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Essai de phase 2 | Eur J Cancer | Vinorélbine + cyclophosphamide continu chez l'enfant et le jeune adulte : bonne tolérance, efficacité notable dans le rhabdomyosarcome |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Essai de phase 2 | Cancer | Vinorélbine dans les sarcomes avancés de l'enfant déjà traités : activité dans le rhabdomyosarcome |
| [37637411](https://pubmed.ncbi.nlm.nih.gov/37637411/) | 2023 | Revue | Front Pharmacol | Revue des chimiothérapies des sarcomes des tissus mous |
| [26260582](https://pubmed.ncbi.nlm.nih.gov/26260582/) | 2016 | Préclinique | Int J Cancer | Synergie d'induction de l'apoptose entre un inhibiteur de PLK1 et des agents anti-microtubules, dont la vinorélbine, dans des cellules de sarcome d'Ewing |
| [36451163](https://pubmed.ncbi.nlm.nih.gov/36451163/) | 2022 | Cas clinique | BMC Urol | Sarcome d'Ewing extra-osseux du rein ; peu pertinent pour la vinorélbine |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 63337924 | VINORELBINE ACCORD 20 mg, capsule molle | Capsule molle | ACCORD HEALTHCARE FRANCE | Active |
| 66621926 | VINORELBINE MEDAC 30 mg, capsule molle | Capsule molle | MEDAC GESELLSCHAFT FUR KLINISCHE SPEZIALPRAPARATE (ALLEMAGN… | Active |
| 69968704 | VINORELBINE MEDAC 20 mg, capsule molle | Capsule molle | MEDAC GESELLSCHAFT FUR KLINISCHE SPEZIALPRAPARATE (ALLEMAGN… | Active |
| 63396029 | VINORELBINE ACCORD 30 mg, capsule molle | Capsule molle | ACCORD HEALTHCARE FRANCE | Active |
| 69684369 | VINORELBINE SANDOZ 20 mg, capsule molle | Capsule molle | SANDOZ | Active |
| 63313994 | VINORELBINE SANDOZ 30 mg, capsule molle | Capsule molle | SANDOZ | Active |
| 62924833 | VINORELBINE ARROW 10 mg/mL, solution à diluer pour perfusion | Solution à diluer pour perfusion | EUGIA PHARMA (MALTA) (MALTE) | Active |
| 63457489 | VINORELBINE ACCORD 10 mg/mL, solution à diluer pour perfusion | Solution à diluer pour perfusion | ACCORD HEALTHCARE FRANCE | Active |
| 60376637 | VINORELBINE PIERRE FABRE 20 mg, capsule molle | Capsule molle | PIERRE FABRE MEDICAMENT | Active |
| 61168991 | NAVELBINE 50 mg/5 ml, solution injectable en flacon | Solution injectable | PIERRE FABRE MEDICAMENT | Active |
| 63413635 | NAVELBINE 30 mg, capsule molle | Capsule molle | PIERRE FABRE MEDICAMENT | Active |
| 64503288 | NAVELBINE 20 mg, capsule molle | Capsule molle | PIERRE FABRE MEDICAMENT | Active |
| 64859633 | VINORELBINE PIERRE FABRE 30 mg, capsule molle | Capsule molle | PIERRE FABRE MEDICAMENT | Active |
| 68184425 | NAVELBINE 10 mg/1 ml, solution injectable en flacon | Solution injectable | PIERRE FABRE MEDICAMENT | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (vinca-alcaloïde, antimitotique) |
| Risque de Myélosuppression | Élevé : la neutropénie est la toxicité dose-limitante de la vinorélbine (selon la littérature fournie) |
| Classification d'Émétogénicité | Moyenne (classification générale de la classe ; à confirmer sur la notice) |
| Éléments de Surveillance | NFS avec formule (neutrophiles en particulier), fonction hépatique, signes de toxicité neurologique et digestive |
| Protection de Manipulation | Suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : insuffisance hépatique, maladie infectieuse, iléus, occlusion intestinale, pneumopathie interstitielle, maladie pulmonaire, leucopénie.
- **Interactions Médicamenteuses** : 465 interactions recensées. Parmi les principales : **clarithromycine (majeure)** ; modérées avec l'aprépitant, la dexaméthasone, le métronidazole, l'éliglustat, le miconazole, le rolapitant, la rosuvastatine, la simvastatine, le tinidazole et le phénylbutyrate de glycérol ; mineure avec la lévofloxacine.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de securité complètes.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Un essai de phase 2 de vinorélbine + cyclophosphamide inclut explicitement les tumeurs d'Ewing, et la littérature (essai de phase 2 pédiatrique, revue de 2026 sur l'essai INTER-EWING-1) soutient ce schéma. Les preuves restent toutefois indirectes (populations mixtes, résultats de l'essai principal non disponibles), d'où le niveau L2 et la nécessité de garde-fous.

<!-- review:begin fr-lic-20261106-vinorelbine-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les preuves restent toutefois indirectes (populations mixtes, résultats de l'essai principal non disponibles), d'où le niveau L2 et la nécessité de garde-fous. / Toutes les AMM françaises de vinorélbine sont annulées, ce qui complique l'accès local. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-vinorelbine-2 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications issues de la notice (ANSM) : lacune bloquante pour le dépistage de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Résultats publiés de l'essai NCT00180947 ou données spécifiques au sarcome d'Ewing
- Clarification du statut réglementaire en France et des voies d'administration disponibles
- Plan de surveillance hématologique et gestion des interactions (notamment inhibiteurs du CYP3A4 comme la clarithromycine)

<!-- review:begin fr-lic-20261106-vinorelbine-3 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarification du statut réglementaire en France (AMM annulées) et des voies d'administration disponibles » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-vinorelbine-3 -->

**Note sur les autres indications prédites :** le cancer bronchique à petites cellules (L1, Proceed with Guardrails) repose sur des essais portant surtout sur le cancer bronchique non à petites cellules, donc sur l'indication d'origine. Le néoplasme du sillon pulmonaire et la tumeur germinale du poumon relèvent de questions de recherche (L3). Les autres prédictions (fibromatose gingivale, fibrome, hamartome et néoplasme bénin du poumon, carcinome du hile, blastome pulmonaire) sont à mettre en attente (Hold), faute de preuves ou de justification thérapeutique.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Au total, 8 AMM sont recensées, toutes annulées : 6 capsules molles (voie orale) et 2 solutions à diluer pour perfusion (ARROW et ACCORD, 10 » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « Toutes les AMM françaises de vinorélbine sont annulées, ce qui complique l'accès local » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulées) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: vinorelbine prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10a70995-e04d-4044-b1dc-c9aa27460397) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

