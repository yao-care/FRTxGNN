---
layout: default
title: Trastuzumab
parent: 僅模型預測 (L5)
nav_order: 319
evidence_level: L5
indication_count: 10
---

# Trastuzumab
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

# Trastuzumab : D'une Indication Non Documentée au Cancer du Sein Récepteur de Progestérone Positif

## Résumé en Une Phrase

Le dossier de preuves ne documente aucune indication d'origine confirmée pour le trastuzumab (aucune AMM française enregistrée, mécanisme d'action officiel marqué en lacune de données — DG002). Le modèle TxGNN prédit néanmoins qu'il pourrait être efficace pour le **Cancer du Sein Récepteur de Progestérone Positif**, avec **36 essais cliniques identifiés** (8 retenus ci-dessous) et **20 publications** soutenant actuellement cette direction. À noter d'emblée : le raisonnement mécanistique disponible indique que le trastuzumab cible HER2(ERBB2), ce qui suggère que cette « nouvelle » indication recoupe potentiellement un usage déjà établi du médicament plutôt qu'un repositionnement inédit — ce point doit être vérifié avant toute décision.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible dans ce dossier (0 AMM en France, MOA en lacune de données — voir DG001/DG002) |
| Nouvelle Indication Prédite | Cancer du sein récepteur de progestérone positif (progesterone-receptor positive breast cancer) |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le champ officiel de mécanisme d'action (`original_moa`) est marqué en lacune de données (DG002, sévérité Élevée), et aucune indication d'origine n'est enregistrée dans le dossier réglementaire français fourni. Ces deux lacunes limitent l'analyse de plausibilité mécanistique et devraient être comblées en priorité avant toute décision finale.

Les notes d'évaluation associées à la prédiction indiquent cependant que le trastuzumab cible les tumeurs surexprimant HER2 (ERBB2). Environ 15 à 20 % des cancers du sein récepteur de progestérone (RP) positif présentent une co-surexpression de HER2 (sous-type RH+/HER2+). Le lien mécanistique proposé passe donc par cette co-expression HER2, et non par le récepteur de progestérone lui-même.

**Point d'attention important :** la totalité des indications les mieux soutenues par des preuves dans ce dossier (RP+, RP-, sous-types luminal A/B, sous-type « normal-like ») appartiennent à la famille du cancer du sein. Sans confirmation de l'indication d'origine du trastuzumab, il n'est pas possible d'établir si cette prédiction constitue un véritable repositionnement ou un simple raffinement de sous-population au sein d'un usage oncologique déjà connu du médicament. Une vérification de l'indication d'origine (via TFDA/ANSM ou DrugBank) est nécessaire pour trancher.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Terminé | 3270 | Chimiothérapie adjuvante ± trastuzumab, femmes ganglions positifs ou HER2-low à haut risque ; essai fondateur du traitement adjuvant HER2+ |
| [NCT00005970](https://clinicaltrials.gov/study/NCT00005970) | Phase 3 | Terminé | 3436 | AC puis paclitaxel hebdomadaire ± trastuzumab en adjuvant, cancer du sein HER2+ ganglions positifs ou haut risque |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Terminé | 517 | Trastuzumab + QL1209 + docétaxel vs trastuzumab + pertuzumab + docétaxel, cancer du sein HER2+/RE-RP- précoce ou localement avancé |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Terminé | 652 | Chimiothérapie à base de taxane + lapatinib vs + trastuzumab en première ligne, cancer du sein métastatique HER2+ |
| [NCT01785420](https://clinicaltrials.gov/study/NCT01785420) | Phase 3 | Recrutant | 1100 | Trastuzumab préopératoire de courte durée vs placebo, cancer du sein HER2+ opérable |
| [NCT00003992](https://clinicaltrials.gov/study/NCT00003992) | Phase 2 | Terminé | 200 | Essai pilote paclitaxel-trastuzumab en adjuvant, cancer du sein stade II/IIIA surexprimant HER2 |
| [NCT01750073](https://clinicaltrials.gov/study/NCT01750073) | Phase 2 | Actif, non recrutant | 92 | Chimiothérapie néoadjuvante ± trastuzumab, cancer du sein non traité auparavant |
| [NCT02774681](https://clinicaltrials.gov/study/NCT02774681) | Phase 2 | Terminé prématurément | 12 | Palbociclib chez patientes HER2+ avec métastases cérébrales (essai arrêté, échantillon faible, preuve limitée) |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | ECR (analyse à 5 ans) | Lancet Oncol | NeoSphere : pertuzumab + trastuzumab néoadjuvant améliore la survie sans progression à 5 ans, cancer du sein HER2+ localement avancé/inflammatoire |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | Méta-analyse | Lancet | Effets de la chimiothérapie/hormonothérapie sur récidive et survie à 15 ans dans le cancer du sein précoce |
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | ECR phase 2 | Lancet Oncol | monarcHER : abémaciclib + trastuzumab ± fulvestrant vs chimiothérapie standard + trastuzumab, cancer du sein avancé RH+/HER2+ |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | ECR phase 3 | Lancet Oncol | ExteNET : nératinib après trastuzumab adjuvant réduit le risque de récidive, cancer du sein HER2+ précoce |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | ECR phase 2 | Ann Oncol | WSG-ADAPT : blocage double néoadjuvant trastuzumab + pertuzumab ± paclitaxel, HER2+/RH- |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | ECR | JAMA Oncol | WSG-TP-II : hormonothérapie + trastuzumab + pertuzumab vs chimiothérapie désescaladée, cancer du sein précoce RH+/HER2+ |
| [29117498](https://pubmed.ncbi.nlm.nih.gov/29117498/) | 2017 | Cohorte (suivi long terme) | NEJM | Risque de récidive à 20 ans après arrêt de l'hormonothérapie à 5 ans, cancer du sein RE+ |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Cohorte / étude moléculaire | Theranostics | Portraits moléculaires et réponse au trastuzumab des cancers du sein triple-positifs (RE+/RP+/HER2+) |
| [26253814](https://pubmed.ncbi.nlm.nih.gov/26253814/) | 2015 | Revue | Breast (Edinburgh) | Implications cliniques des sous-types moléculaires intrinsèques du cancer du sein |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Recommandation (guideline ASCO) | J Clin Oncol | Mise à jour des recommandations ASCO sur le traitement systémique du cancer du sein avancé HER2+ |

---

## Cytotoxicité

Le trastuzumab cible des indications strictement oncologiques (cancer du sein) et le raisonnement mécanistique disponible dans ce dossier le décrit comme un agent ciblant HER2(ERBB2) — cette section est donc pertinente. Ces informations proviennent des notes d'évaluation du dossier de preuves et non d'un champ officiel de MOA (marqué en lacune de données, DG002) ; elles doivent être confirmées.

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (anticorps monoclonal anti-HER2/ERBB2, selon les notes d'évaluation du dossier — à confirmer via DG002) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune donnée de mise en garde, contre-indication ou interaction médicamenteuse n'est actuellement disponible dans ce dossier (DG001, sévérité Bloquante — recherche du RCP/notice TFDA-ANSM requise avant toute évaluation de sécurité S1).

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Le niveau de preuve L1 (≥2 essais de phase 3 complétés : NCT01275677 et NCT04629846) soutient la plausibilité clinique de cette prédiction pour le sous-groupe RH+/HER2+. Toutefois, deux lacunes bloquantes empêchent une validation complète : l'absence de données d'indication d'origine et de sécurité (DG001) et l'absence de MOA confirmé (DG002).

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmation de l'indication d'origine et du statut réglementaire réel du trastuzumab (recherche TFDA/ANSM, car le statut « non commercialisé / 0 AMM » de ce dossier semble incohérent avec un médicament aussi établi que le trastuzumab — à vérifier comme anomalie possible des données)
- Téléchargement et analyse du RCP/notice pour lever le DG001 (mises en garde, contre-indications)
- Confirmation du MOA officiel via DrugBank pour lever le DG002
- Stratification obligatoire par statut HER2 (IHC/FISH) avant toute application clinique, le lien mécanistique passant par HER2 et non par le récepteur de progestérone
- Clarification si cette « nouvelle indication » recoupe un usage déjà autorisé du trastuzumab, ce qui changerait la nature du dossier (extension de sous-population vs repositionnement réel)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

