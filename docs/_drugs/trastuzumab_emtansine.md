---
layout: default
title: Trastuzumab Emtansine
parent: 僅模型預測 (L5)
nav_order: 320
evidence_level: L5
indication_count: 4
---

# Trastuzumab Emtansine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Trastuzumab Emtansine (T-DM1) : Du Cancer du Sein HER2-Positif au Cancer du Sein avec Récepteurs de Progestérone Positifs

## Résumé en Une Phrase

Trastuzumab emtansine (T-DM1) est un conjugué anticorps-médicament ciblant HER2, déjà utilisé en pratique clinique courante pour le cancer du sein métastatique HER2-positif (mention retrouvée dans plusieurs essais du dossier de preuves, ex. NCT03203616).
Le modèle TxGNN prédit qu'il pourrait être pertinent pour le **cancer du sein avec récepteurs de progestérone positifs (RP+)**,
avec un score de **99,82%**, mais seulement **4 essais cliniques** (dont un s'avère, après vérification, ne pas tester réellement le T-DM1) et **15 publications** de nature majoritairement indirecte (revues/guidelines) soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer du sein HER2-positif (métastatique/avancé) — établi à partir du contexte clinique des essais fournis dans le dossier ; texte réglementaire officiel non disponible (lacune de données, cf. DG001) |
| Nouvelle Indication Prédite | Cancer du sein avec récepteurs de progestérone positifs (RP+) |
| Score de Prédiction TxGNN | 99,82% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données formelles de mécanisme d'action (DrugBank) sont marquées comme lacune (DG002). Toutefois, les descriptions d'essais cliniques présentes dans le dossier de preuves précisent de façon cohérente que le T-DM1 est un conjugué anticorps-médicament : l'anticorps trastuzumab cible les cellules tumorales exprimant HER2, et sert de vecteur pour délivrer directement la charge cytotoxique DM1 (dérivé de maytansine, inhibiteur de la tubuline) à ces cellules (ex. NCT02038010 : « T-DM1 is a type of drug that contains an antibody (trastuzumab) linked to chemotherapy... targets a marker on breast cancer cells called HER2 »).

Le lien entre l'indication d'origine (cancer du sein HER2-positif) et la nouvelle indication prédite (cancer du sein RP+) repose sur une co-occurrence de populations plutôt que sur une cible pharmacologique directe : le statut RP n'est pas la cible du T-DM1, c'est le statut HER2 qui l'est. Cliniquement, les tumeurs HER2+/RP+ et HER2+/RP- coexistent dans la population déjà traitée par T-DM1, ce qui peut expliquer le score TxGNN élevé.

Cette hypothèse doit toutefois être nuancée : l'analyse du dossier de preuves a permis d'identifier qu'un essai initialement listé comme preuve de Phase 3 (NCT03726879) teste en réalité l'atézolizumab en association avec trastuzumab + pertuzumab, **sans T-DM1** — il ne peut donc pas être compté comme preuve directe. Après cette correction, l'indication RP+ ne dispose que de preuves indirectes de qualité modérée à faible (niveau L3), ce qui justifie une posture prudente malgré le score de prédiction élevé.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Actif, non recrutant | 164 | T-DM1 + pertuzumab en néoadjuvant, étude de l'hétérogénéité HER2 dans le cancer du sein HER2+ précoce ; preuve de contexte, non spécifique au statut RP |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Terminé | 1151 | Étude rétrospective non interventionnelle sur la prévalence du HER2-low et les schémas de traitement ; ne teste pas directement le T-DM1 |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Terminé | 454 | ⚠ Vérifié : l'intervention réelle est atézolizumab/placebo + trastuzumab + pertuzumab, **sans T-DM1** — ne constitue pas une preuve directe pour ce médicament malgré le titre |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Interrompu (TERMINATED) | 139 | Étude de désescalade de chimiothérapie adjuvante après double blocage HER2 ; interrompue prématurément, résultats incomplets |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline/Revue | J Clin Oncol | Mise à jour des recommandations ASCO sur le traitement systémique du cancer du sein HER2-positif avancé, incluant le T-DM1 |
| [29939838](https://pubmed.ncbi.nlm.nih.gov/29939838/) | 2018 | Guideline/Revue | J Clin Oncol | Mise à jour des recommandations ASCO pour le cancer du sein HER2-positif avancé, revue systématique de 622 articles |
| [24799465](https://pubmed.ncbi.nlm.nih.gov/24799465/) | 2014 | Guideline | J Clin Oncol | Recommandations de pratique clinique ASCO antérieures sur le traitement systémique du cancer du sein HER2-positif avancé |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Revue | Future Oncol | Tendances actuelles du traitement du cancer du sein HR+/HER2+, mentionnant explicitement le trastuzumab emtansine |
| [28259011](https://pubmed.ncbi.nlm.nih.gov/28259011/) | 2017 | Guideline | Eur J Cancer | Recommandations EGTM sur les biomarqueurs : le statut RP doit être mesuré sur tous les cancers du sein invasifs, HER2 conditionne l'usage du T-DM1 |
| [34215766](https://pubmed.ncbi.nlm.nih.gov/34215766/) | 2021 | Cohorte | Sci Rep | Essai ChangeHER : pertinence pronostique du gain de positivité HER2 chez des patientes traitées par pertuzumab et/ou T-DM1 |
| [25873876](https://pubmed.ncbi.nlm.nih.gov/25873876/) | 2015 | Rapport de Cas | Case Rep Oncol | T-DM1 à dose réduite, actif et sûr chez une patiente avec dysfonction hépatique aiguë |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Revue | Pharmacol Res | Revue des inhibiteurs ciblés et cytotoxiques en cancérologie mammaire ; le statut RP conditionne la prise en charge |
| [24892840](https://pubmed.ncbi.nlm.nih.gov/24892840/) | 2013 | pending | Clin Adv Hematol Oncol | Nouveaux développements dans le cancer du sein métastatique, classification par statut RE/RP/HER2 |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Rapport de Cas | Front Oncol | Cas de maladie leptoméningée HER2+ traité par pyrotinib/vinorelbine ; pertinence indirecte, ne teste pas le T-DM1 |

---

## Cytotoxicité

**Le trastuzumab emtansine est un agent antinéoplasique** (conjugué anticorps-médicament utilisé exclusivement en oncologie mammaire HER2-positive).

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Conjugué anticorps-médicament (ADC) — thérapie ciblée délivrant une charge cytotoxique (DM1, dérivé de maytansine, inhibiteur de la tubuline) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'indication RP+ ne dispose que d'un niveau de preuve L3 (études observationnelles/revues, pas d'ECR dédié), et l'essai de Phase 3 initialement le plus prometteur (NCT03726879) s'est avéré, après vérification, ne pas tester le T-DM1. Le lien mécanistique passe par une co-occurrence de population (HER2+/RP+) plutôt qu'une cible pharmacologique directe (RP), ce qui affaiblit la robustesse de la prédiction malgré le score TxGNN élevé.

**Pour avancer, les éléments suivants sont nécessaires :**
- Résolution de la lacune bloquante DG001 (mises en garde/contre-indications TFDA, notice officielle)
- Résolution de la lacune DG002 (mécanisme d'action formel via DrugBank)
- Essai(s) dédié(s) évaluant spécifiquement le T-DM1 dans une population stratifiée par statut RP
- Statut réglementaire et de commercialisation à clarifier (actuellement non commercialisé, 0 AMM)

*Note complémentaire : l'indication classée rang 3 dans ce dossier (cancer du sein RP-négatif, HER2+/RP-) présente un niveau de preuve nettement supérieur (L2, plusieurs essais directs sur le T-DM1 dont TDM4450g/NCT00679341), et pourrait justifier une évaluation séparée avec une recommandation plus favorable.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

