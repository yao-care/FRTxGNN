---
layout: default
title: Flunarizine
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 1
---

# Flunarizine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Flunarizine : Du Vertige à la Prévention de la Migraine

## Résumé en Une Phrase

Flunarizine est un antagoniste non sélectif des canaux calciques, classiquement utilisé dans le traitement du vertige d'origine vestibulaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **prévention de la migraine (migraine disorder)**,
avec **19 essais cliniques** et **20 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Vertige vestibulaire |
| Nouvelle Indication Prédite | Migraine (prévention) |
| Score de Prédiction TxGNN | 99.12% |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Flunarizine est un bloqueur non sélectif des canaux calciques voltage-dépendants, avec une affinité particulière pour les canaux de type T. Son mécanisme central dans la migraine repose sur l'inhibition de la **dépression corticale envahissante** (CSD — Cortical Spreading Depression), considérée comme le substrat neurophysiologique de l'aura migraineuse. En stabilisant l'excitabilité neuronale corticale et en modulant la réactivité du système trigémino-vasculaire, flunarizine atténue la neuroinflammation neurogène à l'origine des crises.

Par ailleurs, flunarizine exerce une activité antagoniste au niveau des **récepteurs D2 dopaminergiques**, ce qui contribue à soulager les nausées liées aux crises migraineuses. Cette combinaison de mécanismes — blocage calcique T-type + antagonisme D2 — constitue un profil pharmacologique directement adapté à la prophylaxie migraineuse, parfaitement cohérent avec le score TxGNN de 0.991.

Bien que non commercialisé en France, flunarizine est reconnu dans plusieurs référentiels internationaux de premier plan (EHF, AAN, Société Canadienne de Neurologie) comme traitement de première ou deuxième ligne de la prophylaxie migraineuse. Son utilisation est largement documentée en Asie, en Europe de l'Est et en Amérique latine, et fait l'objet d'une méta-analyse dédiée publiée par l'European Headache Federation en 2023.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | Non encore recruté | 460 | Étude pragmatique multicentrique (PREMI Study) comparant amitriptyline, flunarizine, topiramate et propranolol en première ligne de prévention en médecine générale |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | NA | Terminé | 120 | Trois bras en parallèle : GONB, topiramate et flunarizine pour la prévention de la migraine épisodique ; comparaison des scores VAS et des fréquences de crises post-traitement |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | NA | Inconnu | 84 | ECR tête-à-tête flunarizine vs amitriptyline pour la prophylaxie de la migraine ; évaluation de la fréquence des crises et du score EVA en centre tertiaire (Pakistan) |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | NA | En recrutement | 44 | Comparaison flunarizine vs propranolol dans la migraine pédiatrique (8–15 ans) à l'aide de l'échelle PedMIDAS ; en phase de recrutement |
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | Terminé | 62 | Efficacité de flunarizine 10 mg/j vs topiramate 50 mg/j dans la prophylaxie de la migraine chronique ; étude dédiée à l'efficacité comparative |
| [NCT04064814](https://clinicaltrials.gov/study/NCT04064814) | Phase 4 | Terminé | 60 | Flunarizine comme traitement de fond chez l'adolescent migraineux ; acide alpha-lipoïque en complément ; confirme la place clinique de flunarizine dans cette tranche d'âge |
| [NCT04766762](https://clinicaltrials.gov/study/NCT04766762) | NA | Inconnu | 96 | Acupuncture vs flunarizine hydrochloride dans la migraine sans aura ; flunarizine utilisé comme comparateur de référence standard |
| [NCT07203248](https://clinicaltrials.gov/study/NCT07203248) | N/A | Non encore recruté | 2000 | Vaste étude en vie réelle (n=2 000) sur les traitements CGRP dans la migraine vestibulaire en Chine ; flunarizine inclus comme traitement conventionnel de comparaison |
| [NCT06753825](https://clinicaltrials.gov/study/NCT06753825) | N/A | Actif, sans recrutement | 60 | Radiofréquence pulsée percutanée vs bloqueurs des canaux calciques (dont flunarizine) dans la migraine de l'enfant ; étude sur les effets à long terme |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | Terminé | 75 | Étude ouverte d'interaction pharmacocinétique flunarizine + topiramate en mono- et bithérapie ; évaluation de la sécurité sur toute la durée de l'étude |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37723437](https://pubmed.ncbi.nlm.nih.gov/37723437/) | 2023 | Revue systématique + méta-analyse | J Headache Pain | Réévaluation critique par l'EHF : flunarizine est un traitement de 1re ou 2e ligne de la prophylaxie migraineuse avec preuves d'efficacité établies ; méta-analyse dédiée |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Méta-analyse en réseau | JAMA Network Open | Comparaison des traitements préventifs de la migraine pédiatrique ; flunarizine évalué en termes d'efficacité et de sécurité chez l'enfant et l'adolescent |
| [31413170](https://pubmed.ncbi.nlm.nih.gov/31413170/) | 2019 | Recommandation clinique (AAN) | Neurology | Mise à jour des lignes directrices AAN sur la prévention pharmacologique de la migraine pédiatrique ; flunarizine inclus parmi les options recommandées |
| [22683887](https://pubmed.ncbi.nlm.nih.gov/22683887/) | 2012 | Recommandation clinique | Can J Neurol Sci | Lignes directrices de la Société Canadienne de Céphalées pour la prophylaxie de la migraine épisodique ; flunarizine cité comme traitement de première ligne |
| [30428122](https://pubmed.ncbi.nlm.nih.gov/30428122/) | 2019 | ECR | Acta Neurol Scand | La combinaison flunarizine + neurostimulation supraorbitaire transcutanée (tSNS) améliore la prophylaxie migraineuse par rapport aux monothérapies respectives |
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Revue systématique + analyse coût-efficacité | Health Technol Assess | Revue des traitements préventifs de la migraine chronique chez l'adulte avec modélisation économique ; mise en perspective flunarizine vs anticorps anti-CGRP |
| [40553594](https://pubmed.ncbi.nlm.nih.gov/40553594/) | 2025 | Revue systématique + méta-analyse | J Assoc Physicians India | Comparaison de l'amitriptyline avec propranolol et flunarizine en prophylaxie migraineuse ; évaluation de l'efficacité et de la sécurité comparatives |
| [40614441](https://pubmed.ncbi.nlm.nih.gov/40614441/) | 2025 | Étude comparative | Brain Dev | Topiramate vs flunarizine dans la migraine pédiatrique : efficacité analgésique et impact sur la scolarité et la vie sociale |
| [35791513](https://pubmed.ncbi.nlm.nih.gov/35791513/) | 2022 | Étude clinique prospective | Brain Behav | Efficacité de flunarizine + duloxétine dans la migraine chronique avec comorbidité dépressive et anxieuse ; bonne réponse clinique observée |
| [33722518](https://pubmed.ncbi.nlm.nih.gov/33722518/) | 2022 | Étude contrôlée non randomisée | Braz J Otorhinolaryngol | Comparaison de l'efficacité de propranolol, flunarizine, amitriptyline et toxine botulinique dans la migraine vestibulaire (cause la plus fréquente de vertige épisodique spontané) |

---

## Informations de Marché en France

Aucune AMM française n'est enregistrée pour la flunarizine à ce jour. Le médicament n'est pas commercialisé en France.

---

## Considérations de Sécurité

> Veuillez consulter la notice officielle (RCP/SmPC) pour les informations de sécurité complètes.

**Signaux de sécurité issus de la littérature clinique :**
À titre informatif, les données de la littérature identifient deux effets indésirables notables associés à un usage prolongé de flunarizine, qui devront être confirmés lors de la consultation du RCP officiel :

- **Syndrome extrapyramidal** (parkinsonisme iatrogène) : signalé notamment chez les personnes âgées et lors d'utilisations prolongées
- **Dépression** : rapportée dans les études post-commercialisation, en particulier chez les patients prédisposés

Ces éléments sont mentionnés dans l'étude post-commercialisation (PMID [9443168](https://pubmed.ncbi.nlm.nih.gov/9443168/)) et méritent une vigilance clinique particulière dans la population cible.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Les preuves cliniques sont robustes (niveau L1) : flunarizine figure dans plusieurs recommandations internationales de première ligne (AAN, EHF, Société Canadienne de Neurologie), fait l'objet d'une méta-analyse dédiée de l'EHF (2023), et est comparé directement à d'autres traitements prophylactiques de référence dans de multiples essais de Phase 4. Son mécanisme d'action (blocage des canaux calciques T-type, inhibition de la CSD, antagonisme D2) est directement pertinent pour la physiopathologie migraineuse, ce qui est parfaitement cohérent avec le score TxGNN de 99,12%.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser le RCP/SmPC officiel afin de documenter formellement les contre-indications et mises en garde (données actuellement absentes du dossier)
- Évaluer le profil de sécurité complet, notamment le risque extrapyramidal et dépressif pour les populations à risque (personnes âgées, grossesse/allaitement)
- Clarifier le statut réglementaire en France : procédure d'accès précoce (ATU/AAP) ou dépôt de dossier d'AMM si l'indication migraine est visée
- Compléter les données pharmacocinétiques et de mécanisme d'action via l'API DrugBank (DB04841)
- Définir un plan de surveillance clinique spécifique pour les sous-populations identifiées (pédiatrie, sujets âgés, femmes en âge de procréer)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

