---
layout: default
title: Morphine
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
---

# Morphine
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

# Morphine : De la Douleur Sévère au Syndrome de Douleur Myofasciale

## Résumé en Une Phrase

La morphine est un analgésique opioïde de référence, historiquement utilisée pour le traitement de la douleur modérée à sévère (douleur cancéreuse, post-opératoire, douleur chronique réfractaire). Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **Syndrome de Douleur Myofasciale**, avec **33 essais cliniques** et **17 publications** identifiés en lien avec cette piste, bien que la majorité porte sur la gestion des opioïdes en contexte douloureux plutôt que sur la morphine ciblant spécifiquement les points gâchette myofasciaux.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Douleur modérée à sévère (analgésique opioïde de référence) — non documentée par une AMM dans ce dossier |
| Nouvelle Indication Prédite | Syndrome de Douleur Myofasciale |
| Score de Prédiction TxGNN | 99.75 % |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations connues, la morphine est un agoniste des récepteurs opioïdes μ (mu), agissant au niveau central et spinal pour produire une analgésie à large spectre. Son efficacité dans la douleur sévère est établie de longue date, et mécanistiquement cette action antalgique globale pourrait s'étendre au syndrome de douleur myofasciale (SDM).

La relation entre l'indication originale et le SDM reste toutefois indirecte : la morphine est un analgésique systémique non spécifique, alors que le SDM repose sur une physiopathologie localisée (points gâchette myofasciaux, sensibilisation centrale). L'usage des opioïdes dans ce contexte relève donc d'une extrapolation analgésique générale plutôt que d'un traitement ciblant le mécanisme pathologique propre au SDM — ce qui est cohérent avec le grade de preuve modéré (L3) et la présence de nombreux essais à pertinence indirecte (interventions non médicamenteuses, comparateurs autres que la morphine) dans le corpus identifié.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03161795](https://clinicaltrials.gov/study/NCT03161795) | Non applicable | Terminé | 258 | Étude coréenne multicentrique sur les risques de l'opiothérapie au long cours dans la douleur chronique non cancéreuse (population incluant des douleurs myofasciales chroniques) |
| [NCT04640896](https://clinicaltrials.gov/study/NCT04640896) | Phase 4 | En cours de recrutement | 60 | Comparaison des injections de points gâchette vs thérapies traditionnelles pour la douleur myofasciale cervicale post-chirurgie (ACDF) |
| [NCT06955923](https://clinicaltrials.gov/study/NCT06955923) | Phase 2 | Terminé | 11 | Injections de points gâchette après prothèse totale de genou pour réduire la douleur et la consommation d'opioïdes vs injection simulée |
| [NCT07413770](https://clinicaltrials.gov/study/NCT07413770) | Non applicable | En cours de recrutement | 60 | Effets du massage classique sur la douleur, la sensibilité musculaire et la qualité de vie dans le SDM |
| [NCT05478928](https://clinicaltrials.gov/study/NCT05478928) | Non applicable | Statut inconnu | 60 | Techniques invasives (micro-électrolyse percutanée, dry needling) sur les points gâchette myofasciaux, mesurées par algométrie |
| [NCT03944889](https://clinicaltrials.gov/study/NCT03944889) | Phase précoce 1 | Terminé | 20 | Sensibilisation musculaire par capsaïcine comme modèle expérimental du SDM et de la sensibilisation centrale |
| [NCT04684784](https://clinicaltrials.gov/study/NCT04684784) | Non applicable | Terminé | 46 | Effet du dry needling sur l'activité électromyographique des points gâchette latents du trapèze |
| [NCT03813485](https://clinicaltrials.gov/study/NCT03813485) | Non applicable | Statut inconnu | 24 | Différences électromyographiques du dry needling sur points gâchette latents (fibres toniques vs phasiques du trapèze) |
| [NCT00580294](https://clinicaltrials.gov/study/NCT00580294) | Non applicable | Terminé | 12 | Étude pilote de rotation rapide d'opioïdes (morphine/oxycodone vers oxymorphone) dans la douleur sévère |
| [NCT05050656](https://clinicaltrials.gov/study/NCT05050656) | Phase 4 | Terminé | 70 | Duloxétine en prémédication vs contrôle sur la douleur postopératoire après réparation du LCA (comparateur, non morphine) |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [41664327](https://pubmed.ncbi.nlm.nih.gov/41664327/) | 2026 | ECR | Asian Spine Journal | Comparaison dexmédétomidine+morphine vs ropivacaïne seule pour infiltration myofasciale lors de fusion spinale thoracolombaire |
| [35066974](https://pubmed.ncbi.nlm.nih.gov/35066974/) | 2022 | Cohorte | Pain Practice | Programme d'étirement structuré associé à la résolution de la douleur myofasciale et à la réduction de l'usage d'opioïdes chez les patients « legacy pain » |
| [20390305](https://pubmed.ncbi.nlm.nih.gov/20390305/) | 2010 | Cohorte | Schmerz | Modification des seuils de douleur pendant et après sevrage opioïde chez des patients lombalgiques chroniques |
| [21419546](https://pubmed.ncbi.nlm.nih.gov/21419546/) | 2011 | Revue | J Oral Maxillofac Surg | Usage à long terme des opioïdes dans le dysfonctionnement chronique de l'articulation temporo-mandibulaire |
| [16713811](https://pubmed.ncbi.nlm.nih.gov/16713811/) | 2006 | Non classé | J Oral Maxillofac Surg | Arthrocentèse de l'ATM suivie d'une perfusion intra-articulaire de morphine pour douleur réfractaire |
| [22648287](https://pubmed.ncbi.nlm.nih.gov/22648287/) | 2012 | Non classé | Journal of Anesthesia | Injections facettaires cervicales ajoutées à un traitement multimodal du syndrome myofascial cervical chronique |
| [17870625](https://pubmed.ncbi.nlm.nih.gov/17870625/) | 2008 | Non classé | European Journal of Pain | Comparaison analgésie péridurale vs cryoanalgésie intercostale (incluant morphine) pour douleur post-thoracotomie |
| [39793344](https://pubmed.ncbi.nlm.nih.gov/39793344/) | 2025 | Non classé | Eur J Obstet Gynecol Reprod Biol | Bloc du nerf honteux et douleur péri-opératoire après injection de toxine botulique pour douleur pelvienne myofasciale |
| [21691691](https://pubmed.ncbi.nlm.nih.gov/21691691/) | 2011 | Non classé | Rev Assoc Med Bras | Approche thérapeutique descriptive du syndrome de douleur post-chirurgie du dos (« failed back surgery ») chez 56 patients |
| [16967674](https://pubmed.ncbi.nlm.nih.gov/16967674/) | 2006 | Non classé | J Calif Dent Assoc | Usage de médications orales, perfusions et injections pour le diagnostic différentiel de la douleur orofaciale |

---

## Informations de Marché en France

Aucune AMM enregistrée dans ce dossier — statut de marché : **Non commercialisé** (0 licence recensée pour la molécule dans les données évaluées).

---

## Considérations de Sécurité

Les données de sécurité spécifiques (mises en garde, contre-indications, interactions médicamenteuses) ne sont pas disponibles dans ce dossier — veuillez consulter la notice officielle. Une lacune de données bloquante (DG001 : mises en garde/contre-indications TFDA) empêche actuellement toute évaluation de sécurité de niveau S1 pour cette molécule, un point critique compte tenu du profil de risque connu des opioïdes (dépression respiratoire, dépendance, sédation).

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Le niveau de preuve L3 (études observationnelles, séries de cas et un ECR récent sur l'infiltration myofasciale) et plusieurs essais ciblant directement le SDM (massage, dry needling, injections de points gâchette) soutiennent une piste plausible, mais le lien mécanistique reste une extrapolation analgésique générale plutôt qu'un ciblage spécifique de la physiopathologie myofasciale, et les données de sécurité réglementaires sont totalement absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données TFDA sur les mises en garde et contre-indications (DG001, bloquant)
- Données détaillées sur le mécanisme d'action via DrugBank (DG002)
- Évaluation spécifique du risque de dépendance/abus opioïde dans une indication non cancéreuse et potentiellement chronique comme le SDM
- Clarification du statut réglementaire en France (aucune AMM actuelle) avant toute démarche de repositionnement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

