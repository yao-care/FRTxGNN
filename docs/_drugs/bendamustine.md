---
layout: default
title: Bendamustine
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Bendamustine
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

# Bendamustine : Du Lymphome Non Hodgkinien Indolent au Lymphome à Cellules du Manteau

## Résumé en Une Phrase

Bendamustine est un agent alkylant bifunctionnel à noyau benzimidazole, reconnu internationalement pour le traitement de la leucémie lymphoïde chronique et du lymphome non hodgkinien indolent réfractaire au rituximab.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Lymphome à Cellules du Manteau (Mantle Cell Lymphoma, MCL)**,
avec **plus de 10 essais cliniques de Phase 2/3** et **20 publications** — dont plusieurs ECR de Phase 3 complétés — soutenant solidement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie lymphoïde chronique / Lymphome non hodgkinien indolent réfractaire au rituximab (données de littérature internationales ; aucune AMM en France) |
| Nouvelle Indication Prédite | Lymphome à cellules du manteau (Mantle Cell Lymphoma) |
| Score de Prédiction TxGNN | 99.63% |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Bendamustine est un agent cytotoxique bifunctionnel atypique : il combine un groupement mustine alkylant (formation de pontages inter-brins de l'ADN) avec un noyau benzimidazole analogue aux purines, qui interfère avec la réparation de l'ADN et inhibe les points de contrôle mitotiques. Cette dualité mécanistique lui confère une résistance croisée partielle avec les agents alkylants classiques (cyclophosphamide, melphalan) et une activité cytotoxique dans les cellules tumorales à faible indice de prolifération — une caractéristique précieuse pour les lymphomes indolents.

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations disponibles dans la littérature incluse (notamment Balfour & Goa, 2001 ; Darwish et al., 2015), bendamustine appartient à la classe des alkylants et exerce une activité cytotoxique par activation de voies apoptotiques indépendantes des points de contrôle p53, ce qui lui permet d'agir dans des contextes où d'autres agents échouent.

Le MCL est une néoplasie lymphoïde B mature caractérisée par la translocation t(11;14) (surexpression de la cycline D1), une dépendance élevée à la signalisation BCR et NF-κB, et un comportement clinique souvent agressif. La combinaison Bendamustine + Rituximab (BR) cible simultanément la survie cellulaire B (via alkylation de l'ADN) et l'antigène de surface CD20 (via rituximab), induisant une apoptose synergique des cellules MCL. Cette complémentarité mécanistique est aujourd'hui reconnue dans les lignes directrices internationales (EHA-EU 2025, NCCN) qui positionnent BR comme standard de première ligne pour les patients MCL non éligibles à la transplantation.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00877006](https://clinicaltrials.gov/study/NCT00877006) | Phase 3 | Terminé | 447 | Essai BRIGHT : BR vs R-CHOP vs R-CVP en première ligne du MCL et NHL indolent — BR non-inférieur à R-CHOP avec profil de tolérance favorable, établissant BR comme référence de première ligne |
| [NCT01776840](https://clinicaltrials.gov/study/NCT01776840) | Phase 3 | Terminé | 523 | Ibrutinib + BR vs placebo + BR chez MCL nouvellement diagnostiqué ≥65 ans — BR utilisé comme bras contrôle actif, confirmant son statut de gold standard |
| [NCT04002297](https://clinicaltrials.gov/study/NCT04002297) | Phase 3 | Actif, non recrutant | 510 | Zanubrutinib + R vs BR chez MCL non éligible à la transplantation — BR retenu comme comparateur de référence Phase 3 |
| [NCT02972840](https://clinicaltrials.gov/study/NCT02972840) | Phase 3 | Actif, non recrutant | 635 | Acalabrutinib + BR vs placebo + BR en MCL non traité — nouvelle confirmation de BR comme épine dorsale standard |
| [NCT06363994](https://clinicaltrials.gov/study/NCT06363994) | Phase 3 | En recrutement | 476 | Orelabrutinib + BR vs BR en MCL naïf de traitement — évaluation de l'optimisation du schéma BR standard |
| [NCT03567876](https://clinicaltrials.gov/study/NCT03567876) | Phase 2 | Terminé | 141 | V-RBAC (Venetoclax + Rituximab + Bendamustine + Cytarabine) chez patients MCL âgés à haut risque — évaluation d'un schéma intensifié à base de bendamustine pour améliorer la survie sans progression |
| [NCT06854003](https://clinicaltrials.gov/study/NCT06854003) | Phase 2 | En recrutement | 60 | BRAZAN (Bendamustine + Rituximab + AraC + Zanubrutinib) puis maintenance en MCL naïf — application contemporaine de la plateforme bendamustine avec BTKi de nouvelle génération |
| [NCT01415752](https://clinicaltrials.gov/study/NCT01415752) | Phase 2 | Actif, non recrutant | 373 | Étude à 4 bras chez MCL ≥60 ans : RB ± Bortézomib suivi de R ou Lénalidomide+R — évaluation directe de bendamustine comme os du traitement avec différentes stratégies de maintenance |
| [NCT01662050](https://clinicaltrials.gov/study/NCT01662050) | Phase 2 | Terminé | 57 | R-BAC adapté à l'âge (Rituximab + Bendamustine + AraC) en induction chez MCL âgé — données d'efficacité et de toxicité en population gériatrique |
| [NCT01118845](https://clinicaltrials.gov/study/NCT01118845) | Phase 2 | Terminé | 63 | SyB L-0501 (bendamustine) + Rituximab en lymphome B diffus à grandes cellules R/R — données multinationales incluant des cohortes asiatiques, soutenant l'activité de bendamustine en B-NHL |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23433739](https://pubmed.ncbi.nlm.nih.gov/23433739/) | 2013 | ECR Phase 3 | Lancet | Étude BRIGHT : BR vs R-CHOP en première ligne MCL et lymphomes indolents — BR non-inférieur avec toxicité réduite (alopécie, neuropathie périphérique significativement moins fréquentes) |
| [35657079](https://pubmed.ncbi.nlm.nih.gov/35657079/) | 2022 | ECR Phase 3 | N Engl J Med | Ibrutinib + BR vs BR seul en MCL naïf ≥65 ans — BR démontre une activité élevée comme contrôle actif ; ibrutinib prolonge la PFS sans amélioration de la SG |
| [40311141](https://pubmed.ncbi.nlm.nih.gov/40311141/) | 2025 | ECR Phase 3 | J Clin Oncol | Acalabrutinib + BR vs placebo + BR en MCL naïf — BR maintient son efficacité comme bras de référence avec réponse globale élevée |
| [30811293](https://pubmed.ncbi.nlm.nih.gov/30811293/) | 2019 | ECR Phase 3 (suivi 5 ans) | J Clin Oncol | Résultats à 5 ans de l'étude BRIGHT — BR conserve une supériorité de survie sans progression sur R-CVP et maintient la non-infériorité sur R-CHOP pour MCL et NHL indolent |
| [41132246](https://pubmed.ncbi.nlm.nih.gov/41132246/) | 2025 | Recommandations cliniques | HemaSphere | Lignes directrices EHA-EU MCL 2025 — BR recommandé explicitement comme option standard de première ligne pour les patients MCL non éligibles à la transplantation intensive |
| [41052510](https://pubmed.ncbi.nlm.nih.gov/41052510/) | 2025 | ECR Phase 2/3 | Lancet | Essai ENRICH : Ibrutinib-Rituximab vs immunochimiothérapie standard (R-CHOP ou BR) en MCL ≥60 ans — BR positionné comme référence de soins standard dans le bras contrôle |
| [32985902](https://pubmed.ncbi.nlm.nih.gov/32985902/) | 2021 | ECR Phase 3 | Future Oncol | Protocole de l'essai Zanubrutinib + R vs BR — décrit BR comme gold standard du comparateur pour les patients MCL non éligibles à l'intensification |
| [32126141](https://pubmed.ncbi.nlm.nih.gov/32126141/) | 2020 | Cohorte prospective | Blood Advances | Analyse groupée : RB alterné avec RC (Rituximab/Cytarabine haute dose) avant autogreffe chez MCL éligible à la transplantation — taux de réponse complète élevé avec cette stratégie d'induction |
| [36456154](https://pubmed.ncbi.nlm.nih.gov/36456154/) | 2022 | Cohorte rétrospective multicentrique | Anticancer Res | BR en MCL en pratique clinique réelle en Corée — haute efficacité confirmée chez des patients naïfs et rechutés/réfractaires dans un contexte de routine |
| [26755518](https://pubmed.ncbi.nlm.nih.gov/26755518/) | 2016 | Revue | J Clin Oncol | Revue complète du MCL — BR établi comme traitement de référence chez les patients âgés ou non éligibles à l'autogreffe, après démonstration de l'importance de la cytarabine haute dose chez les patients jeunes |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel — agent alkylant bifunctionnel de classe unique (noyau mustine + benzimidazole analogue des purines) ; mécanisme double : alkylation de l'ADN et perturbation de la réparation de l'ADN |
| Risque de Myélosuppression | **Élevé** — neutropénie, thrombocytopénie et lymphopénie T fréquentes et potentiellement sévères ; la lymphopénie CD4+ peut persister plusieurs mois après la fin du traitement, augmentant le risque d'infections opportunistes |
| Classification d'Émétogénicité | Faible à modérée (administration intraveineuse) |
| Éléments de Surveillance | NFS avec différentielle avant chaque cycle ; bilan hépatique et rénal ; sérologies virales pré-traitement (HBV, CMV, VZV) ; surveillance active des infections opportunistes (pneumocystose, zona, réactivation CMV) compte tenu de la lymphopénie T prolongée |
| Protection de Manipulation | Manipulation selon les réglementations applicables aux médicaments cytotoxiques ; précautions d'extravasation requises (voie intraveineuse) ; équipement de protection individuelle obligatoire |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité (mises en garde, contre-indications et interactions médicamenteuses non disponibles dans ce dossier — voir points de données manquants DG001 et DG002).

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Plusieurs essais cliniques randomisés de Phase 3 complétés et les lignes directrices EHA-EU 2025 confirment que BR (Bendamustine + Rituximab) constitue un traitement de référence bien établi pour le MCL chez les patients non éligibles à la transplantation. Le niveau de preuve L1 est solide et le score TxGNN de 99,63 % reflète fidèlement cette réalité clinique. L'absence de commercialisation en France représente le principal obstacle réglementaire à lever.

**Pour avancer, les éléments suivants sont nécessaires :**
- Dépôt d'une demande d'AMM auprès de l'ANSM ou exploration d'un accès compassionnel / autorisation temporaire d'utilisation (ATU), bendamustine n'étant pas actuellement commercialisé en France
- Données complètes sur le mécanisme d'action (MOA) issues de DrugBank (DG002)
- Données de sécurité complètes : mises en garde spécifiques ANSM, contre-indications et interactions médicamenteuses (DG001)
- Plan de gestion du risque infectieux (surveillance CMV/VZV/PCP) compte tenu de la lymphopénie T prolongée induite par bendamustine
- Évaluation de l'accès au médicament pour les patients français dans le cadre d'essais cliniques en cours (notamment NCT04002297, NCT02972840)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

