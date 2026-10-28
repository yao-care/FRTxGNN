---
layout: default
title: Tamoxifen
parent: Prédiction du modèle uniquement (L5)
nav_order: 731
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "tamoxifen"
predicted_indications: ["mammary Paget disease", "Ehrlich tumor carcinoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
description: "Tamoxifen : nouvelle indication prédite, Mammary Paget disease (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Tamoxifen
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Tamoxifen: Mammary Paget disease
{: .text-alpha }

## Résumé en Une Phrase

Le tamoxifène est un modulateur sélectif des récepteurs aux estrogènes, initialement utilisé pour le traitement du carcinome mammaire féminin (dont le carcinome canalaire invasif).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome mammaire in situ**, avec **33 essais cliniques** et **19 publications** soutenant actuellement cette direction.
Il s'agit toutefois d'une indication très proche de l'indication d'origine, et non d'un repositionnement au sens strict.

> Note de lecture : la première prédiction du modèle (rang 1) est la maladie de Paget mammaire. Elle ne repose que sur des cas cliniques et des séries rétrospectives (niveau L4, décision « Hold »). Le carcinome mammaire in situ (rang 4) est présenté ici comme indication principale car il dispose des preuves les plus solides parmi les prédictions. Le tableau ci-dessous reprend les données de ce candidat.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Mammary Paget disease |
| Score de Prédiction TxGNN | 0.9969 |
| Niveau de Preuve | L5 (rang 1 : L4) |
| Statut de Marché en France | Commercialisé (autorisations valides : 14 sur 14) |
| Nombre d'AMM | 14 (valides : 14) |
| Décision Recommandée | Proceed with Guardrails (rang 1 : Hold) |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le tamoxifène appartient à la classe des modulateurs sélectifs des récepteurs aux estrogènes (SERM). Il antagonise de façon compétitive le récepteur aux estrogènes (RE) dans le tissu mammaire. Son efficacité dans le cancer du sein RE-positif est établie.

Le carcinome canalaire in situ (CCIS) RE-positif est un stade précoce de la même maladie. Le blocage de la signalisation du RE réduit les récidives ipsilatérales et controlatérales. Ce bénéfice est soutenu par l'essai NSABP B-24 et par l'essai randomisé contre placebo TAM-01 (tamoxifène à faible dose, 5 mg/jour pendant 3 ans). Le suivi à 10 ans de TAM-01 est publié, avec une analyse poolée de trois études (NCT06982313).

Pour les autres prédictions, la plausibilité mécanistique varie. Elle est forte pour le carcinome tubulaire invasif et le cancer du sein RE-positif (indication déjà existante).

## Preuves d'Essais Cliniques

Essais les plus pertinents pour le carcinome mammaire in situ :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT06982313](https://clinicaltrials.gov/study/NCT06982313) | Non applicable | Terminé | 1545 | Suivi à long terme de TAM-01 et analyse poolée de trois études : réduction de 42 % des événements mammaires sur 10 ans avec le tamoxifène à faible dose dans le CCIS et les lésions à haut risque |
| [NCT01357772](https://clinicaltrials.gov/study/NCT01357772) | Phase 3 | Actif, non en recrutement | 500 | Tamoxifène 5 mg/j contre placebo dans la néoplasie intraépithéliale mammaire (suivi à long terme) |
| [NCT00072462](https://clinicaltrials.gov/study/NCT00072462) | Phase 3 | Terminé | 2980 | IBIS-II DCIS : tamoxifène contre anastrozole après chirurgie du CCIS |
| [NCT00053898](https://clinicaltrials.gov/study/NCT00053898) | Phase 3 | Terminé | 3104 | Anastrozole contre tamoxifène dans le CCIS après tumorectomie et radiothérapie |
| [NCT00003857](https://clinicaltrials.gov/study/NCT00003857) | Phase 3 | Terminé | 636 | Tamoxifène seul contre tamoxifène plus radiothérapie dans le CCIS de bon pronostic |
| [NCT04046159](https://clinicaltrials.gov/study/NCT04046159) | Phase 3 | Inconnu | 810 | Radiothérapie contre tamoxifène à faible dose après chirurgie conservatrice dans le CCIS RE-positif de faible risque |
| [NCT00952731](https://clinicaltrials.gov/study/NCT00952731) | Phase 2 | Terminé | 27 | 4-hydroxytamoxifène transdermique contre tamoxifène oral avant chirurgie dans le CCIS |
| [NCT02993159](https://clinicaltrials.gov/study/NCT02993159) | Phase 2 | Terminé | 100 | Tamoxifène oral contre 4-hydroxytamoxifène transdermique avant chirurgie dans le CCIS |
| [NCT00290745](https://clinicaltrials.gov/study/NCT00290745) | Phase 1/2 | Terminé | 79 | Hormonothérapie primaire (tamoxifène ou létrozole) dans le CCIS |
| [NCT00096369](https://clinicaltrials.gov/study/NCT00096369) | Phase 2 | Terminé (arrêt anticipé) | 130 | Biomarqueurs de substitution modulés par le tamoxifène contre placebo chez des femmes à risque accru |

Pour la maladie de Paget mammaire (rang 1), le seul essai associé (NCT00002920, phase 3, 313 patientes) porte sur la prévention de l'atteinte de l'endomètre sous tamoxifène. Il n'apporte aucune preuve directe d'efficacité.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [36917758](https://pubmed.ncbi.nlm.nih.gov/36917758/) | 2023 | ECR | J Clin Oncol | Résultats à 10 ans de TAM-01 : tamoxifène à faible dose contre placebo dans la néoplasie intraépithéliale mammaire |
| [30973790](https://pubmed.ncbi.nlm.nih.gov/30973790/) | 2019 | ECR | J Clin Oncol | Tamoxifène à faible dose et prévention des récidives locales et controlatérales dans la néoplasie intraépithéliale |
| [9747868](https://pubmed.ncbi.nlm.nih.gov/9747868/) | 1998 | ECR | J Natl Cancer Inst | Essai NSABP P-1 : tamoxifène dans la prévention du cancer du sein |
| [25605856](https://pubmed.ncbi.nlm.nih.gov/25605856/) | 2015 | ECR | J Clin Oncol | RTOG 9804 : radiothérapie contre observation dans le CCIS de bon pronostic |
| [34406870](https://pubmed.ncbi.nlm.nih.gov/34406870/) | 2021 | ECR | J Clin Oncol | Rapport à long terme de NRG/RTOG 9804 sur la radiothérapie après exérèse du CCIS |
| [25023044](https://pubmed.ncbi.nlm.nih.gov/25023044/) | 2014 | Revue systématique | Breast | Revue Cochrane et méta-analyse du tamoxifène postopératoire dans le CCIS |
| [23076938](https://pubmed.ncbi.nlm.nih.gov/23076938/) | 2012 | Revue systématique | Cochrane Database Syst Rev | Tamoxifène postopératoire dans le CCIS |
| [20071685](https://pubmed.ncbi.nlm.nih.gov/20071685/) | 2010 | Revue systématique | J Natl Cancer Inst | Incidence, traitement et devenir du CCIS |
| [21398619](https://pubmed.ncbi.nlm.nih.gov/21398619/) | 2011 | Cohorte | J Natl Cancer Inst | Récidives invasives ipsilatérales après tumorectomie dans NSABP B-17 et B-24 |
| [17145343](https://pubmed.ncbi.nlm.nih.gov/17145343/) | 2006 | Revue | Semin Oncol | Le tamoxifène dans le carcinome canalaire in situ |

## Informations de Marché en France

Les 14 AMM recensées sont annulées. Le texte de l'indication approuvée n'est pas renseigné dans les données compilées. Cinq AMM sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61003801 | TAMOXIFENE SANDOZ 20 mg | Comprimé pelliculé | Non renseignée (AMM active) |
| 69203907 | TAMOXIFENE BIOGARAN 10 mg | Comprimé | Non renseignée (AMM active) |
| 61961476 | NOLVADEX 10 mg | Comprimé pelliculé | Non renseignée (AMM active) |
| 60328432 | NOLVADEX 20 mg | Comprimé enrobé | Non renseignée (AMM active) |
| 69424909 | TAMOXIFENE SANDOZ 10 mg | Comprimé pelliculé | Non renseignée (AMM active) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Hormonothérapie antinéoplasique (modulateur sélectif des récepteurs aux estrogènes), non cytotoxique conventionnel |
| Risque de Myélosuppression | Faible. Aucune donnée de toxicité détaillée n'est disponible dans les données compilées, mais le graphe de connaissances associe la leucopénie et la thrombopénie aux contre-indications. |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | NFS (leucocytes, plaquettes), fonction hépatique, calcémie, surveillance gynécologique (endomètre) |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : thrombopénie, hypercalcémie, néphrocalcinose, trouble du métabolisme du phosphore, accident vasculaire cérébral, trouble cérébrovasculaire, infarctus cérébral, embolie pulmonaire, leucopénie, troubles de la vision, cécité.
- **Interactions médicamenteuses** : 546 interactions recensées. Parmi les interactions majeures figurent le bupropion, la lorcasérine, la cimétidine, le dolasétron, l'éliglustat, le cisapride, la dexfenfluramine et la fenfluramine. Des interactions modérées concernent notamment la famotidine, le lopéramide, l'aprépitant, la dexaméthasone, la clarithromycine, le granisétron et la lévofloxacine.
- Les risques thromboemboliques et endométriaux sont à prendre en compte. Le métabolisme par le CYP2D6 est également à considérer.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, car elles ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails** (carcinome mammaire in situ ; Hold pour la maladie de Paget mammaire et les autres prédictions)

**Justification :**
- Le tamoxifène dispose de plusieurs essais de phase 3 et d'un essai randomisé contre placebo (TAM-01, suivi à 10 ans) dans le CCIS RE-positif. Il s'agit toutefois d'un usage oncologique établi, proche de l'indication d'origine.
- Les autres prédictions sont soit sans données (carcinome cribriforme intracanalaire, carcinome mammaire sébacé), soit fondées sur des cas isolés (Paget), soit contraires à la biologie (basal-like, rhabdomyosarcome), soit précliniques (Ehrlich).
- Les 14 AMM françaises sont toutes annulées, ce qui constitue un frein réglementaire important.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice ANSM (mises en garde, contre-indications, indications approuvées) : lacune bloquante pour le criblage de sécurité.
- Compléter les données sur le mécanisme d'action (via DrugBank).
- Clarifier la situation réglementaire en France (raisons de l'annulation des AMM, éventuelles autres présentations disponibles).
- Limiter l'usage aux maladies RE-positives et définir un plan de surveillance des risques thromboemboliques et endométriens, avec prise en compte du statut CYP2D6 et de la charge d'interactions.
- Pour la maladie de Paget mammaire, disposer d'études spécifiques avant toute décision.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

