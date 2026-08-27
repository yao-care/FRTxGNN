---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab : Du Cancer du Sein HER2-Positif au Cancer du Sein RP-Positif

## Résumé en Une Phrase

Pertuzumab est un anticorps monoclonal anti-HER2 dont l'indication d'origine (cancer du sein HER2-positif) n'est pas documentée dans les champs structurés du dossier, mais ressort clairement des preuves cliniques rassemblées (essais CLEOPATRA/NeoSphere/APHINITY notamment).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Cancer du Sein RP-Positif (récepteur de la progestérone positif)**,
avec **10 essais cliniques** et **20 publications** actuellement associés — dont une part significative correspond en réalité à l'usage déjà approuvé de pertuzumab dans le cancer du sein HER2-positif plutôt qu'à une véritable nouvelle hypothèse de repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer du sein HER2-positif (reconstitué à partir des preuves cliniques du dossier ; non renseigné dans les champs structurés) |
| Nouvelle Indication Prédite | Cancer du Sein RP-Positif (récepteur de la progestérone positif) |
| Score de Prédiction TxGNN | 99.93% |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action structuré (champ `original_moa`) ne sont pas disponibles. Sur la base des informations issues du dossier de preuves, pertuzumab se lie au sous-domaine II du récepteur HER2 et bloque la dimérisation HER2-HER3, complétant ainsi l'action du trastuzumab dans le blocage de la voie de signalisation HER2.

Le statut « récepteur de la progestérone positif » constitue avant tout une variable de stratification au sein de la population HER2-positive, et non une cible pharmacologique distincte pour pertuzumab. D'après le raisonnement de repositionnement associé à cette prédiction, cette indication correspond en fait à une population déjà couverte par les indications approuvées historiques de pertuzumab (essais CLEOPATRA, NeoSphere, APHINITY), et non à une hypothèse de repositionnement véritablement nouvelle.

**Point de vigilance :** le score TxGNN élevé (99.93%) reflète ici la proximité du réseau avec une indication déjà connue du médicament plutôt qu'un signal de repositionnement inédit. Ce point est explicitement signalé dans le raisonnement mécanistique fourni avec la prédiction et doit être pris en compte dans l'interprétation de la recommandation « Proceed with Guardrails ».

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Terminé | 517 | Biosimilaire QL1209 vs pertuzumab de référence + trastuzumab + docetaxel en néoadjuvant, cancer du sein HER2+/ER-PR- précoce ou localement avancé |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Terminé | 417 | 4 bras néoadjuvants (type NeoSphere) comparant Herceptin ± pertuzumab ± docetaxel, taux de réponse pathologique complète |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Terminé | 454 | IMpassion050 : atezolizumab vs placebo en association avec chimiothérapie néoadjuvante + trastuzumab + pertuzumab, cancer du sein HER2+ précoce |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | En cours (non recrutant) | 398 | Comparaison biosimilaire BCD-178 vs Perjeta® en néoadjuvant, HER2+/ER-PR- |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | En cours (non recrutant) | 164 | Impact de l'hétérogénéité HER2 sur la réponse à T-DM1 + pertuzumab en préopératoire |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | En cours (non recrutant) | 128 | Lapatinib + trastuzumab ± hormonothérapie, 12 vs 24 semaines, cancer du sein HER2 surexprimé |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Terminé | 1151 | Étude rétrospective non interventionnelle sur la prévalence du HER2-low et les schémas de traitement |
| [NCT03058939](https://clinicaltrials.gov/study/NCT03058939) | Phase 2 | Retiré | 0 | Étude retirée, 0 participant, aucune donnée exploitable |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | Statut inconnu | 7 | Inhibiteur d'aromatase + pertuzumab/trastuzumab sans chimiothérapie, effectif insuffisant |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminé prématurément | 139 | DECRESCENDO : désescalade de chimiothérapie adjuvante après réponse pathologique complète, essai arrêté |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | ECR | JAMA Oncology | WSG-TP-II : hormonothérapie + trastuzumab/pertuzumab vs chimiothérapie désescaladée dans le cancer du sein RH+/ERBB2+ précoce |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | ECR (biosimilaire) | British Journal of Cancer | Équivalence du biosimilaire QL1209 vs pertuzumab de référence en néoadjuvant, HER2+/ER-PR- |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | ECR (suivi 5 ans) | The Lancet Oncology | NeoSphere : survie sans progression et sans maladie à 5 ans sous pertuzumab + trastuzumab néoadjuvant |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | ECR | Annals of Oncology | WSG-ADAPT HER2+/HR- : désescalade avec 12 semaines de double blocage trastuzumab/pertuzumab ± paclitaxel |
| [37609714](https://pubmed.ncbi.nlm.nih.gov/37609714/) | 2023 | ECR | Future Oncology | DECRESCENDO : désescalade de chimiothérapie dans le cancer du sein HER2+/RH- sans atteinte ganglionnaire |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Recommandation | Journal of Clinical Oncology | Mise à jour des recommandations ASCO pour le traitement systémique du cancer du sein HER2+ avancé |
| [28973704](https://pubmed.ncbi.nlm.nih.gov/28973704/) | 2017 | Revue | Southern Medical Journal | Revue des thérapies néoadjuvantes et adjuvantes du cancer du sein selon les sous-types moléculaires |
| [33902424](https://pubmed.ncbi.nlm.nih.gov/33902424/) | 2022 | Revue | Endocrine, Metabolic & Immune Disorders Drug Targets | Revue des options immunothérapeutiques dans le cancer du sein, incluant trastuzumab/pertuzumab |
| [40282499](https://pubmed.ncbi.nlm.nih.gov/40282499/) | 2025 | Cohorte | Cancers | Proposition de chimiothérapie métronomique adjuvante associée aux thérapies ciblées dans le cancer du sein HER2+/RH+ |
| [40739524](https://pubmed.ncbi.nlm.nih.gov/40739524/) | 2025 | Cohorte (real-world) | British Journal of Clinical Pharmacology | Schémas de traitement en vie réelle dans le cancer du sein métastatique RH-positif aux États-Unis |

---

## Informations de Marché en France

Pertuzumab n'est actuellement pas commercialisé en France (0 AMM enregistrée dans le dossier). Aucune information de produit (nom commercial, forme pharmaceutique, indication approuvée) n'est disponible à ce stade.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (anticorps monoclonal anti-HER2, bloque la dimérisation HER2-HER3) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Le niveau de preuve global est élevé (L1, plusieurs essais de Phase 3 complétés), mais une grande partie de cette preuve concerne en réalité l'indication déjà approuvée de pertuzumab (cancer du sein HER2-positif) plutôt qu'une hypothèse de repositionnement inédite vers le statut RP-positif spécifiquement. De plus, pertuzumab n'est pas commercialisé en France, et les données de sécurité et de mécanisme d'action structurées sont absentes du dossier (DG001, DG002).

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les mises en garde/contre-indications de la notice via le site de l'ANSM (bloquant pour l'évaluation de sécurité initiale — DG001)
- Confirmer le mécanisme d'action structuré via DrugBank (DG002)
- Clarifier si cette prédiction constitue réellement une nouvelle piste ou un chevauchement avec l'indication HER2-positive déjà établie
- Évaluer le statut réglementaire nécessaire pour une éventuelle mise sur le marché en France
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

