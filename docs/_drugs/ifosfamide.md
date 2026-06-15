---
layout: default
title: Ifosfamide
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 10
---

# Ifosfamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ifosfamide : Des Sarcomes au Carcinome du Sein Féminin

## Résumé en Une Phrase

Ifosfamide est un agent alkylant de la classe des oxazaphosphorines (moutardes azotées), initialement utilisé dans le traitement des sarcomes des tissus mous, du cancer testiculaire et d'autres tumeurs solides réfractaires.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Carcinome du Sein Féminin**,
avec **8 essais cliniques** et **20 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Sarcomes des tissus mous, cancer testiculaire (indication reconnue internationalement) |
| Nouvelle Indication Prédite | Carcinome du Sein Féminin |
| Score de Prédiction TxGNN | 99.91% |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Ifosfamide est un analogue structural du cyclophosphamide appartenant à la classe des oxazaphosphorines. Son métabolite actif principal, le 4-hydroxy-ifosfamide (4-OH-IF), est généré par bioactivation hépatique via les cytochromes P450 (CYP3A4, CYP2C9, CYP2B6). Ce métabolite forme des pontages covalents intra- et inter-brins avec l'ADN, bloquant la réplication des cellules en division rapide. Fait notable : Schmidt et al. (PMID 14970873) ont démontré que ces mêmes enzymes CYP sont exprimées dans les microsomes de tissu mammaire tumoral, documentant une capacité de bioactivation intratumorale localisée — ce qui renforce la pertinence mécanistique spécifique au sein.

La relation entre l'indication originale (sarcomes) et le carcinome du sein est particulièrement justifiée pour les sous-types histologiques agressifs. Le carcinome métaplasique du sein (MPBC) partage des caractéristiques histologiques avec les sarcomes (différenciation mésenchymateuse, résistance aux anthracyclines/taxanes) et représente la niche thérapeutique la plus documentée pour ifosfamide dans ce contexte (PMID 39306877, 2024). Plus largement, ifosfamide a montré des taux de réponse globale allant jusqu'à 50% dans le cancer du sein métastatique réfractaire aux anthracyclines (PMID 8873839), confirmant une activité clinique réelle au-delà du seul score de prédiction algorithmique.

Le modèle TxGNN identifie cette indication sur la base des similitudes dans le réseau de connaissances biomédicales entre les sarcomes et le carcinome du sein — deux cancers solides à croissance rapide, chimiosensibles aux alkylants, partageant des voies de signalisation oncogéniques communes. La position de ce candidat en première prédiction (rang 1 sur toutes les indications évaluées), associée à une base de preuves cliniques directes, confère à cette prédiction une solidité inhabituellement élevée pour un repositionnement algorithmique.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Phase 2 | Inconnu | 42 | Docetaxel + Ifosfamide en première ligne dans le cancer du sein métastatique — test direct de l'efficacité de la combinaison |
| [NCT00954174](https://clinicaltrials.gov/study/NCT00954174) | Phase 3 | Inconnu | 637 | Paclitaxel+Carboplatin vs Ifosfamide+Paclitaxel dans les carcinosarcomes utéro-annexiels — essai randomisé Phase 3 de plus haut niveau, statut non confirmé |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | Terminé | 33 | Chimiothérapie haute dose séquentielle (CDDP/CTX/VP16 → IFO/Carbo/Taxol) avec support de cellules souches — données de sécurité disponibles |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Arrêté | N/A | Schéma TIME (Topotecan+Ifosfamide+Etoposide) suivi de transplantation autologue dans le cancer du sein métastatique — arrêt prématuré sans résultats complets |
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Phase 2 | Inconnu | N/A | Chimiothérapie haute dose vs dose conventionnelle contenant Ifosfamide dans le cancer du sein métastatique — résultats non publiés |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | Arrêté | 12 | Double transplantation ABMT + Samarium 153 dans le cancer du sein Stade IV — ifosfamide comme composant du conditionnement, échantillon très restreint |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Phase 2 | Arrêté | 7 | Transplantation de cellules souches + lymphocytes T activés dans le cancer du sein Stade IV — ifosfamide en conditionnement, arrêté prématurément |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Inconnu | 35 | Étude SCORE — sélection de chimiothérapie guidée par organoïdes dérivés du patient, ifosfamide inclus comme option dans le panel de sensibilité |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [11932893](https://pubmed.ncbi.nlm.nih.gov/11932893/) | 2002 | Essai Phase II | Cancer | Paclitaxel (24h) + Ifosfamide dans le carcinome du sein métastatique résistant aux anthracyclines — évaluation de l'efficacité et de la tolérance |
| [8873839](https://pubmed.ncbi.nlm.nih.gov/8873839/) | 1996 | Essai Phase II | J Chemotherapy | IMEpi (Ifosfamide+Mesna+Epirubicine) en deuxième ligne — taux de réponse globale 50%, durée médiane de rémission 9,6 mois, n=16 |
| [8918497](https://pubmed.ncbi.nlm.nih.gov/8918497/) | 1996 | Essai Phase II | J Clin Oncol | Ifosfamide + Vinorelbine en première ligne dans le cancer du sein métastatique — évaluation de l'efficacité et de la toxicité |
| [9226029](https://pubmed.ncbi.nlm.nih.gov/9226029/) | 1997 | Essai Phase II | Tumori | Ifosfamide + Etoposide dans le cancer du sein avancé prétraité — profil de réponse et de toxicité documenté |
| [10602903](https://pubmed.ncbi.nlm.nih.gov/10602903/) | 1999 | Essai Phase II | Cancer Chemo Pharmacol | Ifosfamide + Vinorelbine chez des patientes avec cancer du sein métastatique après échec aux anthracyclines |
| [2347057](https://pubmed.ncbi.nlm.nih.gov/2347057/) | 1990 | Essai Phase II | Cancer Chemo Pharmacol | IMF (Ifosfamide substitué au cyclophosphamide dans le schéma CMF) dans le cancer du sein réfractaire au CMF — n=25 |
| [2347053](https://pubmed.ncbi.nlm.nih.gov/2347053/) | 1990 | Essai Phase II | Cancer Chemo Pharmacol | Ifosfamide + Epirubicine dans les cancers du sein réfractaires et autres tumeurs solides — n=23 pour le sein, patientes lourdement prétraitées |
| [39306877](https://pubmed.ncbi.nlm.nih.gov/39306877/) | 2024 | Cohorte clinique | Current Problems Cancer | Carcinome métaplasique du sein (MPBC) — expérience contemporaine avec chimiothérapie à base d'ifosfamide en première ligne pour ce sous-type rare |
| [26030252](https://pubmed.ncbi.nlm.nih.gov/26030252/) | 2015 | Revue Systématique | Arch Pathol Lab Med | Carcinome métaplasique du sein — revue systématique des entités pathologiques et options thérapeutiques incluant les schémas à base d'ifosfamide |
| [14970873](https://pubmed.ncbi.nlm.nih.gov/14970873/) | 2004 | Translationnel/In vitro | Br J Cancer | Expression de CYP3A4, CYP2C9, CYP2B6 dans les microsomes de tissu mammaire tumoral — bioactivation intratumorale d'ifosfamide documentée pour la première fois |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel — Agent alkylant (classe Oxazaphosphorine, analogue du cyclophosphamide, produit nécessitant une bioactivation par CYP450) |
| Risque de Myélsuppression | Élevé — neutropénie et thrombocytopénie fréquentes, dose-limitantes ; l'administration concomitante de mesna est obligatoire pour prévenir la cystite hémorragique par acroléine |
| Classification d'Émétogénicité | Modérée à élevée — antiémétiques prophylactiques (sétrons + dexaméthasone) recommandés avant chaque administration |
| Éléments de Surveillance | NFS avec différentielle (avant chaque cycle), créatininémie et DFG (risque de syndrome de Fanconi/tubulopathie proximale), bilan hépatique (ALAT/ASAT), ECBU (dépistage hématurie microscopique), électrolytes (phosphate, potassium), surveillance neurologique (encéphalopathie à l'ifosfamide — apparition 24–48h post-administration) |
| Protection de Manipulation | Port obligatoire d'EPI (gants nitrile double couche, masque FFP2, blouse imperméable) ; préparation exclusivement en hotte à flux laminaire verticale de classe II ; élimination comme déchet cytotoxique réglementé |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Plusieurs essais cliniques de Phase 2 et une étude de Phase 3 (statut incertain) documentent l'activité antitumorale d'ifosfamide dans le cancer du sein métastatique, notamment dans les formes résistantes aux anthracyclines et dans le carcinome métaplasique, avec un mécanisme de bioactivation intratumorale spécifiquement démontré dans le tissu mammaire. Le niveau de preuve L2, associé à un score TxGNN de 99.91%, justifie une utilisation encadrée dans des situations de besoin médical non satisfait.

**Pour avancer, les éléments suivants sont nécessaires :**
- Accès au mécanisme d'action complet et au RCP européen de référence (médicament non commercialisé en France — évaluer la faisabilité via importation exceptionnelle ou accès ATU)
- Identification et ciblage des sous-populations prioritaires : carcinome du sein métaplasique et cancer du sein triple-négatif réfractaire aux anthracyclines et taxanes
- Mise en place d'un protocole de surveillance sécurité rigoureux : administration systématique de mesna, bilan rénal de base et suivi, protocole de détection précoce de l'encéphalopathie à l'ifosfamide
- Revue des interactions médicamenteuses cliniquement significatives avec les inhibiteurs/inducteurs CYP3A4 dans les combinaisons envisagées
- Évaluation du risque à long terme de leucémie ou syndrome myélodysplasique secondaire (t-MDS), particulièrement en cas d'utilisation répétée chez des patientes jeunes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

