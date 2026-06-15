---
layout: default
title: Dipyridamole
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Dipyridamole
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

# Dipyridamole : De la Prévention Thromboembolique à la Prévention des Accidents Vasculaires Cérébraux

## Résumé en Une Phrase

Le Dipyridamole est un agent antiplaquettaire et vasodilatateur coronarien, reconnu pour son rôle dans l'imagerie de stress myocardique et la prévention des complications thromboemboliques.
Le modèle TxGNN prédit qu'il pourrait être efficace dans la prévention des **Accidents Vasculaires Cérébraux (AVC / Stroke disorder)**,
avec **plusieurs essais cliniques randomisés de Phase 3/4 complétés** (dont ESPS-2, ESPRIT, JASAP, PRoFESS — plus de 26 000 participants au total) et **18 publications**, incluant plusieurs méta-analyses Cochrane de niveau 1, soutenant actuellement cette direction.

> **⚠️ Note sur la prédiction de rang 1 :** L'angor de Prinzmetal figure au premier rang des prédictions TxGNN (score 99,99%, L5, Décision : Hold). Cette prédiction reflète une **contre-indication potentielle** et non une indication thérapeutique — le Dipyridamole peut induire un phénomène de « vol coronarien » aggravant les spasmes artériels coronariens. Le présent rapport se concentre sur l'indication de rang 2 (AVC), qui constitue le premier candidat viable au repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Non disponible (médicament non commercialisé en France) |
| Nouvelle Indication Prédite | Accident vasculaire cérébral (Stroke disorder) |
| Score de Prédiction TxGNN | 99,95% |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations connues, le Dipyridamole est un inhibiteur de la phosphodiestérase (PDE) et un bloqueur du recaptage de l'adénosine. Ce double mécanisme élève les concentrations intracellulaires d'AMPc et de GMPc dans les plaquettes, inhibant de façon réversible leur agrégation et leur adhésion à la paroi vasculaire. En parallèle, l'accumulation extracellulaire d'adénosine contribue à une vasodilatation artérielle et à des effets anti-inflammatoires documentés.

La relation entre la prévention thromboembolique (usage original) et la prévention des AVC ischémiques est directe : les deux pathologies partagent le même mécanisme physiopathologique central — la formation de thrombus plaquettaires dans le réseau artériel. Les AVC ischémiques d'origine athérothrombotique impliquent l'activation et l'agrégation plaquettaires comme étape clé. En inhibant cette cascade en amont de l'occlusion vasculaire, le Dipyridamole s'interpose logiquement dans la chaîne causale menant à l'infarctus cérébral.

Ce mécanisme a été validé cliniquement par plusieurs essais de grande envergure. La combinaison Dipyridamole à libération prolongée + Aspirine (Aggrenox® / Asasantin®) bénéficie d'approbations dans de nombreux pays européens pour la prévention secondaire des AVC, et figure dans les recommandations de l'AHA et de l'ESO. Des études récentes suggèrent en outre des effets neuroprotecteurs additionnels via des mécanismes anti-inflammatoires et antioxydants, indépendants de l'effet antiplaquettaire.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT00311402](https://clinicaltrials.gov/study/NCT00311402) | Phase 3 | Terminé | 1 295 | **JASAP** : Aggrenox (Dipyridamole LP 200 mg + ASA 25 mg) vs Aspirine 81 mg — prévention secondaire des infarctus cérébraux récidivants dans la population japonaise ; directement pertinent, Grade A |
| [NCT00562588](https://clinicaltrials.gov/study/NCT00562588) | Phase 4 | Terminé | 551 | **EARLY** : Aggrenox initié dans les 24h suivant l'AVC vs après 7 jours sous ASA seule — comparaison des stratégies de switch précoce en unité neurovasculaire ; Grade A |
| [NCT00153062](https://clinicaltrials.gov/study/NCT00153062) | Phase 4 | Terminé | 20 332 | **PRoFESS** : Aggrenox vs Clopidogrel (avec/sans Telmisartan) — prévention d'un second AVC en double aveugle ; plus grand essai de prévention secondaire avec Dipyridamole |
| [NCT00161070](https://clinicaltrials.gov/study/NCT00161070) | Phase 4 | Terminé | 4 500 | **ESPRIT** : Aspirine + Dipyridamole vs Aspirine seule ou anticoagulation légère après ischémie cérébrale d'origine artérielle — supériorité de la bithérapie confirmée |
| [NCT02966119](https://clinicaltrials.gov/study/NCT02966119) | Phase 3 | Arrêté (n=23) | 23 | **RESTART-FR** : Reprise ou éviction des antiplaquettaires (dont Dipyridamole) après hémorragie intracérébrale spontanée sous antithrombotiques — arrêt avant objectif d'inclusion, données limitées mais population pertinente |
| [NCT01661322](https://clinicaltrials.gov/study/NCT01661322) | Phase 3 | Arrêté | 3 096 | Antiplaquettaire intensif triple (ASA + Clopidogrel + Dipyridamole) vs Aspirine + Dipyridamole chez patients à haut risque post-AVC/AIT — arrêté pour raisons de sécurité, données partielles |
| [NCT02565693](https://clinicaltrials.gov/study/NCT02565693) | Phase 2 | Terminé | 101 | Apixaban vs antiplaquettaires vs absence de traitement après hémorragie intracérébrale avec FA — comparaison indirecte avec stratégie Dipyridamole, population partiellement pertinente |
| [NCT02630862](https://clinicaltrials.gov/study/NCT02630862) | N/A | Terminé | 240 | Profilage du stress oxydatif après revascularisation carotidienne sous Aspirine + Dipyridamole — démonstration de l'activité antioxydante in vivo du Dipyridamole |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [8981292](https://pubmed.ncbi.nlm.nih.gov/8981292/) | 1996 | ECR | J Neurol Sci | **ESPS-2** : ASA 50 mg + Dipyridamole LP 400 mg — réduction de 37 % des AVC récidivants vs placebo ; supériorité démontrée de la bithérapie sur chaque monothérapie |
| [11786451](https://pubmed.ncbi.nlm.nih.gov/11786451/) | 2002 | Méta-analyse | BMJ | Méta-analyse collaborative sur RCT d'antiplaquettothérapie : réduction significative des décès vasculaires, infarctus du myocarde et AVC dans les populations à haut risque |
| [15569877](https://pubmed.ncbi.nlm.nih.gov/15569877/) | 2005 | Méta-analyse | Stroke | Méta-analyse sur données individuelles de RCT : Dipyridamole (±ASA) réduit les AVC ischémiques récidivants et les événements vasculaires majeurs après AVC ou AIT |
| [17636684](https://pubmed.ncbi.nlm.nih.gov/17636684/) | 2007 | Revue Cochrane | Cochrane Database | Cochrane 2007 : Dipyridamole pour la prévention des événements vasculaires — la combinaison ASA + Dipyridamole est supérieure à ASA seule ; réduction de risque relatif de 22 % |
| [16625549](https://pubmed.ncbi.nlm.nih.gov/16625549/) | 2006 | Revue Cochrane | Cochrane Database | Mise à jour Cochrane 2006 : confirmation de la supériorité de l'association ASA + Dipyridamole vs ASA seule pour la prévention secondaire des AVC |
| [12535415](https://pubmed.ncbi.nlm.nih.gov/12535415/) | 2003 | Revue Cochrane | Cochrane Database | Cochrane 2003 : Dipyridamole dans la prévention des événements vasculaires chez patients avec AIT et AVC ischémique mineur — résumé des preuves disponibles |
| [23871093](https://pubmed.ncbi.nlm.nih.gov/23871093/) | 2013 | Méta-analyse | J Neurol Sci | Méta-analyse de RCT : efficacité et sécurité de l'association ASA + Dipyridamole vs ASA seule pour la prévention secondaire après AIT/AVC — résultats favorables à la bithérapie |
| [20955428](https://pubmed.ncbi.nlm.nih.gov/20955428/) | 2010 | Étude clinique | Ann NY Acad Sci | Effets du Dipyridamole lors d'AVC aigu : documentation des mécanismes neuroprotecteurs anti-inflammatoires indépendants de l'effet antiplaquettaire |
| [18174451](https://pubmed.ncbi.nlm.nih.gov/18174451/) | 2008 | Revue | Arterioscler Thromb Vasc Biol | Thérapeutiques translationnelles du Dipyridamole : inhibition des PDE, élévation des cAMP/cGMP plaquettaires, potentialisation de la protection vasculaire via le NO endothélial |
| [19300042](https://pubmed.ncbi.nlm.nih.gov/19300042/) | 2009 | Revue | Am J Ther | Ciblage de la réponse inflammatoire dans la prévention secondaire des AVC — rôle de l'association ASA + Dipyridamole LP selon les recommandations de l'American Heart Association |

---

## Informations de Marché en France

Aucune AMM enregistrée en France dans la base de données actuelle.

> **Note :** Le Dipyridamole est commercialisé dans plusieurs pays de l'Union Européenne (Allemagne, Italie, Pays-Bas, Royaume-Uni, Espagne) sous la dénomination **Aggrenox®** ou **Asasantin®** (association Dipyridamole LP 200 mg + Aspirine 25 mg) pour la prévention secondaire des AVC. Une vérification directe auprès de l'**ANSM** et via la base de données de l'**EMA** est nécessaire pour confirmer le statut réglementaire actuel en France.

---

## Considérations de Sécurité

Les données de sécurité spécifiques (contre-indications, mises en garde, interactions médicamenteuses) ne sont pas disponibles dans ce dossier.

> Veuillez consulter la notice officielle pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Plusieurs essais cliniques de Phase 3/4 — dont ESPS-2, ESPRIT, JASAP et PRoFESS (plus de 26 000 participants cumulés) — fournissent des preuves directes de niveau **L1** soutenant l'utilisation du Dipyridamole en association avec l'Aspirine pour la prévention secondaire des AVC ischémiques. La combinaison Aggrenox®/Asasantin® est intégrée aux recommandations internationales (AHA, ESO) et approuvée dans plusieurs pays européens. La décision "Proceed with Guardrails" reflète la robustesse des preuves cliniques, tempérée par l'absence d'AMM française confirmée et les lacunes documentaires sur la sécurité locale.

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmation du statut réglementaire en France auprès de l'ANSM et de l'EMA (vérifier si Aggrenox® / Asasantin® dispose d'une autorisation active en France)
- Documentation complète du mécanisme d'action (MOA) via DrugBank API — lacune de priorité **haute** (DG002)
- Données de sécurité complètes : mises en garde, contre-indications, interactions médicamenteuses selon la notice EMA — lacune de priorité **bloquante** (DG001)
- Analyse de l'accès au marché français : positionnement concurrentiel vs Clopidogrel, prix et conditions de remboursement
- Plan de surveillance spécifique pour les patients avec **angor de Prinzmetal** (signal de sécurité identifié par TxGNN au rang 1 — risque de spasme coronarien par phénomène de vol coronarien)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

