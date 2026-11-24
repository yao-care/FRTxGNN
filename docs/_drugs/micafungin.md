---
layout: default
title: Micafungin
parent: Preuves modérées (L3-L4)
nav_order: 497
evidence_level: L3
indication_count: 1
last_modified_at: 2026-11-24
description: "Micafungin : nouvelle indication prédite, Infection des voies urinaires (urinary tract infection) (niveau de preuve L3). Indication d'origine : Candidose œsophagienne, candidémie…"
monitor_inn: "micafungin"
predicted_indications: ["urinary tract infection (disease)"]
---

# Micafungin
{: .fs-9 }

Niveau de preuve: **L3** | Indications prédites: **1** 
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

## Micafungine : Des Candidoses Systémiques à l'Infection des voies urinaires
{: .text-alpha }

## Résumé en Une Phrase

La micafungine est un antifongique de la classe des échinocandines, initialement utilisé pour traiter la candidose œsophagienne, la candidémie et la candidose disséminée.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**infection des voies urinaires** (notamment à Candida), avec **13 publications** disponibles à ce jour, mais **aucun essai clinique** enregistré. Ces publications sont surtout des cohortes, des séries et des rapports de cas.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Candidose œsophagienne, candidémie, candidose disséminée (les textes d'indication des AMM ne sont pas renseignés) |
| Nouvelle Indication Prédite | Infection des voies urinaires (urinary tract infection) |
| Score de Prédiction TxGNN | 0,9903 |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Commercialisé (autorisations valides : 8 sur 10) |
| Nombre d'AMM | 10 (valides : 8) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon les rubriques « Mechanism of Action » et « Microbiology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Micafungin (traduction non officielle) : « La micafungine appartient à la classe des échinocandines, agents antifongiques. […] La micafungine inhibe la synthèse du 1,3-bêta-D-glucane, un composant essentiel de la paroi cellulaire fongique, absent des cellules de mammifères. Activité dans les modèles animaux de candidose L'activité de la micafungine a été démontrée dans des modèles murins et lapins de candidose muqueuse et disséminée. » Texte original en anglais : "Micafungin is a member of the echinocandin class of antifungal agents. […] Micafungin inhibits the synthesis of 1,3-beta-D-glucan, an essential component of fungal cell walls, which is not present in mammalian cells. Activity in Animal Models of Candidiasis Activity of micafungin has been demonstrated in both mucosal and disseminated murine and rabbit models of candidiasis." ([DailyMed: Micafungin (micafungin sodium) prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=33e579c1-b315-44cb-a690-e2dd2cdf44ee), version du 2025-11-08 ; consulté le 2026-11-19). Sur la base des connaissances sur la classe, la micafungine est une échinocandine : elle inhibe la 1,3-bêta-D-glucane synthase et perturbe la synthèse de la paroi cellulaire fongique. Cette analyse repose donc sur le mécanisme connu de la classe et non sur les données fournies.

L'indication originale (candidoses œsophagienne, sanguine et disséminée) et la nouvelle indication visent le même genre de pathogène, Candida. La candidurie ou l'infection urinaire à Candida est donc biologiquement plausible, car le mécanisme antifongique est le même.

Une réserve pharmacocinétique existe : les échinocandines sont traditionnellement considérées comme ayant une faible excrétion urinaire de la forme active. Une étude de 2016 (PMID 27424599) a toutefois rapporté des concentrations urinaires de micafungine suffisantes pour traiter des infections urinaires à Candida, ce qui atténue en partie cette préoccupation. Le score TxGNN élevé est cohérent avec cette logique, mais il reste une prédiction et ne constitue pas une preuve clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35146837](https://pubmed.ncbi.nlm.nih.gov/35146837/) | 2022 | Cohorte | Pediatr Int | Résultats de la micafungine chez des enfants en réanimation pédiatrique avec infection urinaire nosocomiale à Candida ; analyse des taux de succès selon l'espèce |
| [27587066](https://pubmed.ncbi.nlm.nih.gov/27587066/) | 2016 | Cohorte | Int Urol Nephrol | Taux d'éradication de la candidurie chez des patients hospitalisés traités par micafungine |
| [27424599](https://pubmed.ncbi.nlm.nih.gov/27424599/) | 2016 | Étude pharmacocinétique | Int J Antimicrob Agents | Six cas d'infection urinaire traités avec succès ; niveaux urinaires de micafungine jugés suffisants |
| [26937340](https://pubmed.ncbi.nlm.nih.gov/26937340/) | 2016 | Série de cas | Med Mycol Case Rep | Cinq cas de candidurie traités par micafungine (≥ 6 jours) ; résolution de la fongurie en 30 jours après la fin du traitement |
| [31111613](https://pubmed.ncbi.nlm.nih.gov/31111613/) | 2019 | Rapport de cas | Transpl Infect Dis | Éradication d'une infection urinaire chronique à *C. krusei* sous micafungine à dose augmentée chez un greffé hépatique et rénal |
| [38827222](https://pubmed.ncbi.nlm.nih.gov/38827222/) | 2024 | Rapport de cas | Front Pediatr | Infection urinaire à *C. glabrata* chez un prématuré traitée par micafungine |
| [38681664](https://pubmed.ncbi.nlm.nih.gov/38681664/) | 2024 | Rapport de cas | Med Mycol Case Rep | Bézoard fongique rénal à *C. glabrata* sensible à la micafungine, traité par antifongique et extraction endoscopique |
| [40765059](https://pubmed.ncbi.nlm.nih.gov/40765059/) | 2025 | Rapport de cas | J Pharm Health Care Sci | Pyélonéphrite et bactériémie à *C. glabrata* sous inhibiteur du SGLT2, traitées avec succès par micafungine |
| [29109159](https://pubmed.ncbi.nlm.nih.gov/29109159/) | 2018 | Cohorte rétrospective | Antimicrob Agents Chemother | Surtraitement fréquent de la candidurie asymptomatique ; les recommandations déconseillent l'antifongique dans ce cas |

## Informations de Marché en France

Le statut des AMM recensées figure dans l'Aperçu rapide et dans le tableau ci-dessous ; les textes d'indication ne sont pas renseignés.

<!-- review:begin fr-lic-20261124-micafungin-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les 8 AMM ci-dessous sont toutes valides ; » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans l'Aperçu rapide. Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés : le nombre et le statut à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché, générés à partir des données BDPM. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-micafungin-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 62470487 | MICAFUNGINE HIKMA 100 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | HIKMA FARMACEUTICA (PORTUGAL) | Active |
| 62450342 | MYCAMINE 100 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | SANDOZ PHARMACEUTICALS (SLOVENIE) | Active |
| 60754631 | MICAFUNGINE VIATRIS 50 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | VIATRIS SANTE | Active |
| 63197760 | MYCAMINE 50 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | SANDOZ PHARMACEUTICALS (SLOVENIE) | Active |
| 69105377 | MICAFUNGINE REIG JOFRE 50 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | LABORATORIO REIG JOFRE (ESPAGNE) | Active |
| 62635145 | MICAFUNGINE VIATRIS 100 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | VIATRIS SANTE | Active |
| 62262657 | MICAFUNGINE REIG JOFRE 100 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | LABORATORIO REIG JOFRE (ESPAGNE) | Active |
| 63461174 | MICAFUNGINE HIKMA 50 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | HIKMA FARMACEUTICA (PORTUGAL) | Active |
| 61841758 | MICAFUNGINE STRAGEN 50 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | STRAGEN-FRANCE | Abrogée |
| 64022529 | MICAFUNGINE STRAGEN 100 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | STRAGEN-FRANCE | Abrogée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie rénale, pyo-uretère. Ces éléments sont à interpréter avec prudence, d'autant que la population cible (infection urinaire) peut présenter une atteinte rénale ou des voies urinaires.
- **Interactions médicamenteuses** (5 interactions de niveau modéré) : amphotéricine B, nitisinone, évérolimus, ribociclib, sirolimus.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves sont de niveau L3 (cohortes, séries et rapports de cas, sans essai clinique). Les recommandations déconseillent par ailleurs l'antifongique en cas de candidurie asymptomatique, et la faible excrétion urinaire de la forme active reste une réserve. De plus, la micafungine est commercialisée en France (8 AMM valides sur 10), mais les données de sécurité de la notice manquent, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice (ANSM)
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Disposer d'essais comparatifs ou d'études pharmacocinétiques urinaires plus robustes
- Clarifier la situation réglementaire en France
- Évaluer le risque chez les patients ayant une atteinte rénale ou des voies urinaires

<!-- review:begin fr-lic-20261106-micafungin-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarifier la situation réglementaire en France (AMM annulées, indications non renseignées) » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-micafungin-1 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « (AMM annulées, indications non renseignées) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Micafungin (micafungin sodium) prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=33e579c1-b315-44cb-a690-e2dd2cdf44ee) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

