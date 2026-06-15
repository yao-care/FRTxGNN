---
layout: default
title: Estazolam
parent: 僅模型預測 (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
---

# Estazolam
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

# Estazolam : Du Statut Non Enregistré à Taïwan vers la Prise en Charge de l'Insomnie

## Résumé en Une Phrase

Estazolam est une triazolo-benzodiazépine à propriétés hypnotiques, largement utilisée à l'échelle mondiale pour le traitement de l'insomnie, mais actuellement sans aucune autorisation de mise sur le marché à Taïwan.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Insomnie**, confirmant computationnellement son profil pharmacologique établi à l'international,
avec **12 essais cliniques** et **18 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Aucune AMM enregistrée à Taïwan |
| Nouvelle Indication Prédite | Insomnie |
| Score de Prédiction TxGNN | 99.48% |
| Niveau de Preuve | L1 |
| Statut de Marché à Taïwan | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Estazolam exerce son effet hypnotique par un mécanisme direct sur le récepteur GABA-A : en renforçant l'ouverture des canaux chlorure associés, il provoque une hyperpolarisation neuronale qui se traduit cliniquement par une réduction de la latence d'endormissement et une prolongation du sommeil NREM. Ce mécanisme est parfaitement aligné avec les cibles physiopathologiques de l'insomnie, et les paramètres cliniques habituellement mesurés (ISI, PSG) reflètent directement cette action pharmacologique.

La prédiction TxGNN ne constitue pas ici un repositionnement vers une nouvelle pathologie, mais plutôt une **validation computationnelle** d'une indication historiquement établie qui reste en attente d'enregistrement à Taïwan. L'utilisation d'Estazolam comme médicament de référence (bras actif comparateur) dans au moins quatre essais de Phase 3 ou 4 conduits principalement en Asie — dont un essai réalisé à Taïwan même (NCT02648776, n = 1 400) — reflète son statut de standard de soins de facto dans la région.

L'absence d'AMM taïwanaise contraste donc avec un niveau de preuve international L1 et une approbation FDA américaine en vigueur (Schedule IV). La démarche appropriée est une régularisation réglementaire ciblée, non un repositionnement exploratoire.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00956319](https://clinicaltrials.gov/study/NCT00956319) | Phase 4 | Terminé | 42 | Essai contrôlé actif en groupes parallèles : évaluation directe de l'efficacité et de la sécurité d'Estazolam (Eurodin) vs Zolpidem LP dans l'insomnie primaire |
| [NCT00347295](https://clinicaltrials.gov/study/NCT00347295) | Phase 3 | Terminé | 253 | RCT double-aveugle double-placebo multicentriques : Brotizolam vs Estazolam dans l'insomnie ambulatoire — preuve directe d'efficacité et de sécurité d'Estazolam |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | Observationnelle | Inconnu | 1 400 | Grande cohorte prospective taïwanaise évaluant les hypnotiques (dont Estazolam) chez les personnes âgées : patterns d'usage, efficacité, sécurité et caractéristiques pharmacocinétiques en vie réelle |
| [NCT06859190](https://clinicaltrials.gov/study/NCT06859190) | Phase 3 | En recrutement | 60 | Essai évaluant Estazolam en association avec auriculothérapie et électropuncture dans l'insomnie induite par le cancer — résultats attendus décembre 2026 |
| [NCT07306494](https://clinicaltrials.gov/study/NCT07306494) | Phase 4 | Non encore ouvert | 1 200 | Grand essai multicentriques double-aveugle double-placebo : Compound Ciwujia Granules vs Estazolam (bras actif de référence) dans l'insomnie chronique sur 4 semaines |
| [NCT03997058](https://clinicaltrials.gov/study/NCT03997058) | Phase 4 | Inconnu | 120 | Comparaison pression auriculaire vs Estazolam oral dans l'insomnie des patients sous hémodialyse chronique (MHD) à Guangzhou |
| [NCT06212934](https://clinicaltrials.gov/study/NCT06212934) | N/A | Inconnu | 96 | Essai multicentriques de non-infériorité : acupuncture « Tiaoshen » vs Estazolam dans l'insomnie de courte durée |
| [NCT06258226](https://clinicaltrials.gov/study/NCT06258226) | N/A | Inconnu | 108 | ECR évaluant la pression auriculaire pour faciliter la réduction progressive d'Estazolam chez des patients présentant une dépendance — données indirectes sur le profil de tolérance |
| [NCT04932395](https://clinicaltrials.gov/study/NCT04932395) | Phase 4 | Inconnu | 400 | RCT multicentriques à enrichissement adaptatif, double-aveugle vs placebo : pilule Anshen Buxin Liuwei dans la névrose cardiaque avec composante insomnie |
| [NCT05452577](https://clinicaltrials.gov/study/NCT05452577) | N/A | Terminé | 187 | Évaluation normative de la médecine chinoise selon la théorie Yin-Yang dans l'insomnie chronique et sa corrélation avec le rythme circadien |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [1968721](https://pubmed.ncbi.nlm.nih.gov/1968721/) | 1990 | Synthèse clinique | Am J Medicine | Synthèse de l'expérience clinique américaine : Estazolam 1–2 mg améliore significativement la latence d'endormissement, la durée totale du sommeil, les éveils nocturnes et la qualité subjective sur 6 semaines sans perte d'efficacité |
| [30625122](https://pubmed.ncbi.nlm.nih.gov/30625122/) | 2018 | Revue systématique | Medical Letter | Revue comparative des hypnotiques oraux dans l'insomnie chronique, incluant le positionnement d'Estazolam dans la classe des benzodiazépines |
| [36571227](https://pubmed.ncbi.nlm.nih.gov/36571227/) | 2022 | ECR | Acupuncture Research | ECR : Thérapie à l'aiguille superficielle combinée à Estazolam dans l'insomnie par stagnation hépatique ; mesure d'ACTH et cortisol comme marqueurs biologiques du mécanisme d'action combiné |
| [37697875](https://pubmed.ncbi.nlm.nih.gov/37697875/) | 2023 | ECR | Chinese Acupuncture | ECR comparatif : acupuncture syndrome-différenciée vs Estazolam dans l'insomnie chronique, avec évaluation comparative de l'impact sur la fonction cognitive |
| [30625124](https://pubmed.ncbi.nlm.nih.gov/30625124/) | 2018 | Référence | Medical Letter | Tableau étendu des hypnotiques oraux : posologie, profil de tolérance et positionnement comparatif d'Estazolam parmi les agents disponibles |
| [33798303](https://pubmed.ncbi.nlm.nih.gov/33798303/) | 2021 | Observation clinique | Chinese Acupuncture | Comparaison Baduanjin + pression auriculaire vs Estazolam oral dans l'insomnie liée à la COVID-19 sur fond de traitement conventionnel |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Transversale | Medicine | Étude transversale multicentrique sur l'insomnie chez 8 questions de survivants COVID-19 (déc. 2022–fév. 2023) : facteurs influençant la sévérité mesurée par l'ISI |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Pharmacoépidémiologie | China J Chinese Med | Analyse en vie réelle de 1 067 patients hospitalisés avec insomnie : Estazolam figure parmi les traitements les plus fréquemment prescrits, en association avec hypertension et insuffisance cérébrale |
| [40827342](https://pubmed.ncbi.nlm.nih.gov/40827342/) | 2025 | Transversale | Psychiatry Clin Psychopharm | Évaluation rétrospective transversale des pratiques de prescription dans un hôpital de médecine chinoise à Shenzhen : rationalité de l'usage d'Estazolam pour l'insomnie |
| [40896345](https://pubmed.ncbi.nlm.nih.gov/40896345/) | 2025 | Revue de portée | Integrative Med Research | Revue de portée sur l'insomnie comorbide à la douleur chronique (>20 % des adultes) : contexte thérapeutique incluant les benzodiazépines dont Estazolam |

---

## Informations de Marché à Taïwan

Aucune autorisation de mise sur le marché n'est actuellement enregistrée pour Estazolam à Taïwan selon les données TFDA disponibles au 7 juin 2026. Le médicament est classé **non commercialisé** (未上市).

Cette absence d'enregistrement contraste avec la situation internationale : Estazolam est approuvé par la FDA américaine depuis 1990 (Schedule IV, indication insomnie) et utilisé comme médicament de référence dans des essais cliniques conduits en Chine, au Japon et à Taïwan même.

---

## Considérations de Sécurité

Veuillez consulter la notice officielle (仿單) pour les informations de sécurité complètes. Les données de mise en garde, contre-indications et interactions médicamenteuses spécifiques à Taïwan n'ont pas été accessibles dans le cadre de cette évaluation et constituent un point bloquant à résoudre avant toute démarche réglementaire.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Deux essais de Phase 3/4 complétés avec Estazolam comme agent actif ou comparateur direct, complétés par une synthèse clinique de Tier 1 (PMID 1968721) établissant l'efficacité sur paramètres polysomnographiques, confèrent un niveau de preuve L1 — le plus élevé de la classification. L'absence d'AMM taïwanaise ne reflète pas un déficit de données scientifiques mais un déficit d'enregistrement réglementaire qui constitue l'obstacle principal à lever.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice officielle TFDA (仿單) pour documenter les mises en garde et contre-indications — actuellement bloquant (DG001)
- Vérifier et compléter les données de mécanisme d'action via DrugBank (DB01215) — actuellement en Data Gap (DG002)
- Constituer un dossier d'interactions médicamenteuses (DDI), notamment avec les inhibiteurs du CYP3A4 qui métabolisent les benzodiazépines
- Évaluer la faisabilité réglementaire d'un dépôt de dossier auprès de la TFDA, en s'appuyant sur les données FDA américaines et les essais Phase 3/4 asiatiques disponibles
- Intégrer un plan de gestion du risque de dépendance et de sevrage, en particulier pour les populations âgées (cohorte NCT02648776 taïwanaise)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

