---
layout: default
title: Enzalutamide
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 7
---

# Enzalutamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Enzalutamide : Du Cancer de la Prostate Résistant à la Castration au Cancer des Organes Reproducteurs Masculins

## Résumé en Une Phrase

Enzalutamide est un antagoniste des récepteurs aux androgènes (AR) de deuxième génération, largement approuvé à l'échelle mondiale pour le traitement du cancer de la prostate résistant à la castration (CRPC) et hormono-sensible métastatique, bien qu'il ne soit pas encore enregistré en France.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Cancer des Organes Reproducteurs Masculins**,
avec **plus de 50 essais cliniques** et **20 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer de la prostate résistant à la castration (indication mondiale de référence, non enregistrée en France) |
| Nouvelle Indication Prédite | Cancer des organes reproducteurs masculins |
| Score de Prédiction TxGNN | 99.51% |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans cette base de données. Sur la base des informations connues, Enzalutamide appartient à la classe des antagonistes des récepteurs aux androgènes de deuxième génération (diarylamides). Contrairement aux anti-androgènes de première génération (ex. Bicalutamide), il inhibe la signalisation AR à travers trois mécanismes simultanés : (1) liaison compétitive au domaine de liaison du ligand de l'AR avec une affinité nettement supérieure, (2) inhibition de la translocation nucléaire de l'AR, et (3) inhibition de la liaison de l'AR à l'ADN — réduisant ainsi l'expression de gènes cibles comme le PSA.

Le cancer des organes reproducteurs masculins, notamment le cancer de la prostate, présente une forte dépendance aux androgènes via la voie AR. Cette dépendance persiste même dans les stades avancés résistants à la castration, où des mécanismes alternatifs (amplification, mutation, variants d'épissage de l'AR comme AR-V7) maintiennent l'activité de l'AR malgré la suppression androgénique classique. L'antagonisme multi-niveaux d'Enzalutamide sur l'AR le rend particulièrement adapté à cette indication, y compris dans les contextes de résistance.

La robustesse de la prédiction TxGNN (99.51%) est soutenue par un corpus clinique exceptionnel : les essais de Phase 3 AFFIRM (2012), PREVAIL (2014), ARCHES (2019), ENZAMET (2019) et PROSPER (2018) ont tous démontré un bénéfice significatif en survie globale et/ou en survie sans progression dans le CRPC métastatique, le CRPC non métastatique, et le cancer de la prostate hormono-sensible métastatique. Ces données constituent le niveau de preuve le plus élevé (L1).

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01288911](https://clinicaltrials.gov/study/NCT01288911) | Phase 2 | Terminé | 375 | RCT randomisé en double aveugle comparant Enzalutamide (MDV3100) vs Bicalutamide chez des hommes castrés avec cancer de la prostate métastatique — étude fondatrice ayant directement soutenu le développement de l'essai AFFIRM Phase 3 |
| [NCT02312557](https://clinicaltrials.gov/study/NCT02312557) | Phase 2 | Actif non recrutant | 58 | Addition de Pembrolizumab après progression sous Enzalutamide dans le mCRPC ; Enzalutamide utilisé comme plateforme de traitement de base, évalue la séquence post-résistance |
| [NCT02319837](https://clinicaltrials.gov/study/NCT02319837) | Phase 3 | Actif non recrutant | 1 068 | Enzalutamide + Leuprolide vs Enzalutamide seul vs Placebo + Leuprolide dans le cancer de la prostate non métastatique à haut risque progressant après prostatectomie ou radiothérapie |
| [NCT01946165](https://clinicaltrials.gov/study/NCT01946165) | Phase 2 | Terminé | 69 | Étude préopératoire : Abiraterone + LHRH avec ou sans Enzalutamide pendant 6 mois dans le cancer de la prostate à haut risque de récidive ; évalue le bénéfice du blocage androgénique combiné |
| [NCT03103724](https://clinicaltrials.gov/study/NCT03103724) | Phase 2 | Terminé | 68 | Évaluation de l'efficacité d'Enzalutamide et du rôle biomarqueur d'AR-V7 dans le mCRPC avec atteinte viscérale ; taux de contrôle de la maladie à 3 mois comme critère principal |
| [NCT06992232](https://clinicaltrials.gov/study/NCT06992232) | Phase 2 | En recrutement | 144 | Radiothérapie ou prostatectomie radicale combinée avec ADT intensifiée (incluant Enzalutamide) pour le cancer de la prostate métastatique nouvellement diagnostiqué — essai multicentrique randomisé en Chine |
| [NCT01867333](https://clinicaltrials.gov/study/NCT01867333) | Phase 2 | Terminé | 57 | Vaccin thérapeutique PROSTVAC/TRICOM + Enzalutamide vs Enzalutamide seul dans le mCRPC ; évalue la synergie immunothérapie-thérapie hormonale |
| [NCT05873192](https://clinicaltrials.gov/study/NCT05873192) | Phase 2 | En recrutement | 30 | Talazoparib (inhibiteur PARP) + Enzalutamide en préchirurgical dans le cancer de la prostate métastatique aux ganglions lymphatiques de novo |
| [NCT02057939](https://clinicaltrials.gov/study/NCT02057939) | Phase 2 | Terminé | 38 | Enzalutamide + ADT standard + radiothérapie de rattrapage chez des hommes avec cancer de la prostate récidivant post-prostatectomie (essai STREAM) ; survie sans progression à 2 ans comme critère principal |
| [NCT04335682](https://clinicaltrials.gov/study/NCT04335682) | Phase 2 | Actif non recrutant | 111 | Étude randomisée comparant les effets cognitifs de Darolutamide vs Enzalutamide dans le CRPC et le cancer de la prostate hormono-sensible métastatique (essai ARACOG) |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [28655021](https://pubmed.ncbi.nlm.nih.gov/28655021/) | 2017 | Revue | JAMA | Revue de référence sur le diagnostic et le traitement du cancer de la prostate, incluant les données d'efficacité d'Enzalutamide dans le CRPC ; plus de 160 000 nouveaux cas/an aux États-Unis |
| [32534790](https://pubmed.ncbi.nlm.nih.gov/32534790/) | 2020 | Revue | Trends in Cancer | Synthèse des avancées thérapeutiques dans le cancer de la prostate avancé : Enzalutamide, Abiraterone, Apalutamide, Darolutamide, Docetaxel — guide de sélection des thérapies |
| [32592760](https://pubmed.ncbi.nlm.nih.gov/32592760/) | 2020 | Cohorte | Annals of Oncology | Hérédité homozygote HSD3B1(1245C) associée à de mauvais résultats dans le mCRPC traité par Abiraterone ou Enzalutamide ; implications pour la médecine de précision |
| [31614208](https://pubmed.ncbi.nlm.nih.gov/31614208/) | 2020 | Revue (mécanisme) | J Steroid Biochem Mol Biol | Intracrinologie revisitée : formation intratissulaire des androgènes dans le CRPC et le cancer du sein ; comprendre les mécanismes de résistance à Enzalutamide |
| [34752846](https://pubmed.ncbi.nlm.nih.gov/34752846/) | 2022 | Expérimentale | Cancer Letters | Résistance à Enzalutamide médiée par la dégradation de TGFBR2 via PTH1R dans les ostéoblastes lors de métastases osseuses du cancer de la prostate |
| [33542074](https://pubmed.ncbi.nlm.nih.gov/33542074/) | 2021 | Expérimentale | Clin Cancer Res | Émergence de la résistance à Enzalutamide associée aux dépendances BCL-2 et IKKB ; nouvelles pistes de thérapies combinées pour contourner la résistance |
| [34489465](https://pubmed.ncbi.nlm.nih.gov/34489465/) | 2021 | Séquençage single-cell | Nature Communications | scATAC et scRNA-seq identifient des sous-populations cellulaires pré-existantes et persistantes associées à la rechute du cancer de la prostate sous Enzalutamide |
| [30928160](https://pubmed.ncbi.nlm.nih.gov/30928160/) | 2019 | Cohorte génomique | European Urology | Caractérisation des altérations génomiques (PTEN, RB1, TP53) associées au mauvais pronostic et à la résistance à Enzalutamide dans le mCRPC |
| [29460922](https://pubmed.ncbi.nlm.nih.gov/29460922/) | 2018 | Revue | Nature Reviews Urology | Plasticité cellulaire et phénotype neuroendocrine : mécanisme de résistance AR-indépendant émergent sous Abiraterone et Enzalutamide, touchant environ un quart des tumeurs résistantes |
| [29734647](https://pubmed.ncbi.nlm.nih.gov/29734647/) | 2018 | Revue | Int J Mol Sci | Avancées récentes dans le traitement du cancer de la prostate : mécanismes moléculaires et données cliniques d'Enzalutamide, Abiraterone, Apalutamide dans le CRPC et le mHSPC |

---

## Informations de Marché en France

Enzalutamide ne possède actuellement aucune Autorisation de Mise sur le Marché (AMM) en France — aucune licence approuvée n'est répertoriée dans la base de données TFDA/ANSM consultée.

> **Note contextuelle** : À l'échelle internationale, Enzalutamide (Xtandi®, Astellas/Pfizer) bénéficie d'une approbation de la FDA (États-Unis) et de l'EMA (Europe) pour le CRPC métastatique, le CRPC non métastatique à haut risque, et le cancer de la prostate hormono-sensible métastatique. Une démarche de demande d'AMM spécifique auprès de l'ANSM ou via la procédure centralisée EMA serait nécessaire pour commercialisation en France.

---

## Cytotoxicité

Enzalutamide est un médicament antinéoplasique utilisé dans le traitement du cancer de la prostate. Il n'appartient pas à la classe des cytotoxiques conventionnels mais relève de la thérapie ciblée hormonale.

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée — Antagoniste des récepteurs aux androgènes (AR) de 2e génération (classe diarylamide) ; non cytotoxique conventionnel |
| Risque de Myélosuppression | Faible (médicament à action hormonale sans effet myélotoxique direct significatif ; ne nécessite pas de surveillance hématologique intensive comme les chimiothérapies) |
| Classification d'Émétogénicité | Faible à minimale (administration orale ; émétogénicité notablement inférieure aux chimiothérapies cytotoxiques de type taxane ou platine) |
| Éléments de Surveillance | Bilan hépatique (ASAT/ALAT), numération formule sanguine (NFS), tension artérielle, fonction rénale, évaluation neurologique périodique (risque de convulsions) |
| Protection de Manipulation | Précautions standards pour médicaments antinéoplasiques oraux recommandées : manipulation avec gants, éviter l'écrasement des capsules, élimination conforme aux réglementations DASRI |

---

## Considérations de Sécurité

Les données de sécurité détaillées (mises en garde officielles, contre-indications formelles) ne sont pas disponibles dans la base de données consultée.

> Veuillez consulter le Résumé des Caractéristiques du Produit (SmPC) pour les informations de sécurité complètes. Les points d'attention connus d'après les données internationales incluent : risque de convulsions (à surveiller chez les patients avec antécédents épileptiques), syndrome d'encéphalopathie postérieure réversible (PRES), interactions médicamenteuses significatives via les voies CYP3A4 et CYP2C8 (rifampicine, millepertuis, gemfibrozil), et risque cardiovasculaire accru dans les populations âgées.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Enzalutamide bénéficie d'un corpus de preuves cliniques de niveau L1, avec plusieurs essais de Phase 3 randomisés (AFFIRM, PREVAIL, ARCHES, ENZAMET, PROSPER) démontrant un bénéfice robuste en survie globale et en survie sans progression dans le cancer de la prostate à différents stades. Bien que non enregistré en France, les données internationales sont suffisamment solides pour justifier une démarche réglementaire ; la prédiction TxGNN (99.51%) valide la cohérence mécanistique du signal.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtention des données de mécanisme d'action (MOA) détaillées via DrugBank API — nécessaire pour l'analyse de cohérence mécanistique (DG002)
- Téléchargement et analyse du SmPC officiel (Xtandi®, version EMA) pour les mises en garde, contre-indications et profil de DDI complet (DG001)
- Dossier de demande d'AMM via la procédure centralisée EMA ou soumission directe ANSM, en s'appuyant sur les données Phase 3 disponibles
- Évaluation approfondie des interactions médicamenteuses (DDI), notamment avec les inducteurs puissants du CYP3A4 (rifampicine) et les inhibiteurs du CYP2C8 (gemfibrozil)
- Élaboration d'un Plan de Gestion des Risques (PGR) pour les populations à risque : patients âgés, antécédents épileptiques, risque cardiovasculaire élevé
- Stratégie de prix et d'accès au marché en lien avec la HAS (évaluation du Service Médical Rendu et de l'Amélioration du SMR)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

