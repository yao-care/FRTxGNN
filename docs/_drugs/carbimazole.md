---
layout: default
title: Carbimazole
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 3
---

# Carbimazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Carbimazole : De l'Hyperthyroïdie aux Affections Thyroïdiennes Spécialisées (Évaluation Multi-Indications)

## Résumé en Une Phrase

Carbimazole est un antithyroïdien de synthèse de la classe des thionamides, utilisé de longue date pour contrôler l'hyperthyroïdie en inhibant la synthèse des hormones thyroïdiennes. Le modèle TxGNN prédit qu'il pourrait être efficace pour **3 indications thyroïdiennes spécialisées** — résistance THRβ (99,71%), thyrotoxicose néonatale (99,41%) et hyperthyroxinémie (99,21%) — avec la **thyrotoxicose néonatale** comme indication prioritaire, soutenue par **19 publications** et un niveau de preuve L3 incluant des études observationnelles et des séries de cas cliniques.

---

## Aperçu Rapide

| Élément | Contenu |
|---------|---------|
| Indication Originale | Hyperthyroïdie (antithyroïdien thionamide — inhibiteur TPO) |
| Indication Prédite Rang 1 | Résistance aux hormones thyroïdiennes par mutation THRβ |
| Indication Prédite Rang 2 | Thyrotoxicose néonatale |
| Indication Prédite Rang 3 | Hyperthyroxinémie |
| Score TxGNN (Rang 1 / 2 / 3) | 99,71% / 99,41% / 99,21% |
| Niveau de Preuve (indication prioritaire) | L3 — Thyrotoxicose néonatale |
| Statut de Marché en France | Non commercialisé (0 AMM) |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** (RTHβ) · **Proceed with Guardrails** (Thyrotoxicose néonatale) · **Research Question** (Hyperthyroxinémie) |

---

## Pourquoi Ces Prédictions Sont-elles Raisonnables ?

Les données détaillées sur le mécanisme d'action de carbimazole ne sont pas disponibles dans ce dossier. Sur la base des informations connues, carbimazole fait partie de la classe des thionamides antithyroïdiens. Son efficacité dans le traitement de l'hyperthyroïdie a été prouvée, et il agit en inhibant la thyroperoxydase (TPO) — l'enzyme clé qui catalyse l'iodation de la thyroglobuline et la synthèse des hormones T3 et T4. C'est ce mécanisme central qui fonde l'évaluation de pertinence pour chacune des trois indications prédites.

**Thyrotoxicose néonatale (indication prioritaire)** : La thyrotoxicose néonatale survient principalement par transfert transplacentaire d'anticorps stimulants du récepteur TSH (TRAb) d'une mère atteinte de maladie de Basedow. Ces anticorps stimulent la thyroïde fœtale/néonatale de manière autonome. Carbimazole, en bloquant directement la synthèse de T4/T3 via l'inhibition de la TPO, agit sur la même cible pharmacologique que dans l'hyperthyroïdie adulte. Les TRAb maternels ayant une demi-vie de 3 à 12 semaines, un traitement antithyroïdien à court terme assure un pontage thérapeutique jusqu'à leur disparition naturelle — stratégie reconnue par les recommandations internationales.

**Résistance THRβ (rang 1, Hold)** : La mutation du récepteur THRβ empêche l'hypophyse d'être freinée par T4, maintenant une sécrétion excessive et continue de TSH. Dans ce contexte, réduire la T4 par carbimazole aggraverait le déficit hormonal dans les tissus à récepteur THR normal (cœur, foie, os) sans bénéficier aux tissus résistants. Le mécanisme d'action est directement opposé à l'objectif thérapeutique — l'utilisation est potentiellement délétère.

**Hyperthyroxinémie (rang 3)** : Cette entité est hétérogène. Carbimazole est efficace uniquement dans les formes de vraie hyperthyroïdie (Basedow, adénome thyréotrope sécrétant du TSH). Il est sans effet ou délétère dans les formes normothyroïdiennes (hyperthyroxinémie dysalbuminémique familiale FDH, RTHβ) où le T4 sérique est élevé mais le T4 libre est normal et la réponse tissulaire intacte. La stratification diagnostique précise est le prérequis indispensable.

---

## Indications Prédites — Vue d'Ensemble

| Rang | Indication | Score TxGNN | Niveau de Preuve | Recommandation |
|------|-----------|-------------|-----------------|----------------|
| 1 | Résistance THRβ aux hormones thyroïdiennes | 99,71% | L5 | Hold |
| 2 | Thyrotoxicose néonatale | 99,41% | L3 | Proceed with Guardrails |
| 3 | Hyperthyroxinémie | 99,21% | L4 | Research Question |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour les trois indications prédites.

---

## Preuves de la Littérature

### Thyrotoxicose Néonatale (Rang 2 — Indication Prioritaire)

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-------|------|-------|---------------------|
| [41191399](https://pubmed.ncbi.nlm.nih.gov/41191399/) | 2025 | Rapport de cas | Endocrinology, Diabetes & Metabolism Case Reports | Hypercalcémie sévère secondaire à thyrotoxicose néonatale transitoire ; normalisation après traitement carbimazole |
| [24251220](https://pubmed.ncbi.nlm.nih.gov/24251220/) | 2013 | Revue clinique | Indian Journal of Endocrinology and Metabolism | Thyrotoxicose fœtale et néonatale : mortalité 12-20%, mécanisme TRAb transplacentaires, rôle des antithyroïdiens |
| [24622372](https://pubmed.ncbi.nlm.nih.gov/24622372/) | 2013 | Revue clinique | The Lancet Diabetes & Endocrinology | Hyperthyroïdie en grossesse : maladie de Basedow, risques maternels et néonataux, place des thionamides dont carbimazole |
| [7523202](https://pubmed.ncbi.nlm.nih.gov/7523202/) | 1994 | Cohorte rétrospective | Eur J Obstet Gynecol Reprod Biol | 32 grossesses compliquées par hyperthyroïdie ; carbimazole et PTU utilisés ; résultats maternels et périnataux documentés |
| [1971773](https://pubmed.ncbi.nlm.nih.gov/1971773/) | 1990 | Étude observationnelle | Clinical Endocrinology | 44 femmes Basedow / 46 grossesses / 48 nourrissons ; corrélation TBII, dose thionamide et fonction thyroïdienne néonatale |
| [11298090](https://pubmed.ncbi.nlm.nih.gov/11298090/) | 2001 | Série de cas | Clinical Endocrinology | Thyrotoxicose congénitale chez prématurés ; mortalité jusqu'à 25% ; index TBII maternel comme prédicteur |
| [25952662](https://pubmed.ncbi.nlm.nih.gov/25952662/) | 2015 | Rapport de cas | Indian Journal of Pediatrics | Traitement in utero par carbimazole chez deux fratries avec thyrotoxicose fœtale récurrente ; issue favorable |
| [29494342](https://pubmed.ncbi.nlm.nih.gov/29494342/) | 2018 | Rapport de cas | J Pediatric Endocrinology & Metabolism | Hyperthyroïdie néonatale sévère par TRAb chez enfant de mère hypothyroïdienne auto-immune atypique |
| [27747714](https://pubmed.ncbi.nlm.nih.gov/27747714/) | 2015 | Rapport de cas | Drug Safety - Case Reports | Prématuré 32 SA, thyrotoxicose traitée carbimazole 500 µg/8h + propranolol ; hypotension sévère sous amlodipine — signal DDI pédiatrique |
| [23320593](https://pubmed.ncbi.nlm.nih.gov/23320593/) | 2013 | Rapport de cas | J Paediatrics and Child Health | Thyrotoxicose maternelle et goitre fœtal ; traitement in utero puis néonatal par carbimazole ; monitoring échographique |

### Résistance THRβ (Rang 1)

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-------|------|-------|---------------------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Rapport de cas / Revue différentielle | BMJ Case Reports | Homme traité 10 ans par carbimazole pour hyperthyroïdie supposée ; T4L élevée persistante avec TSH non freinée → diagnostic RTHβ établi — **le carbimazole s'est révélé inadapté, voire délétère** |

### Hyperthyroxinémie (Rang 3)

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-------|------|-------|---------------------|
| [24847468](https://pubmed.ncbi.nlm.nih.gov/24847468/) | 2014 | Rapport de cas | European Thyroid Journal | Coexistence TSHome + Basedow ; valeurs TSH inappropriées ; complexité de l'hyperthyroxinémie par excès de TSH |
| [32854689](https://pubmed.ncbi.nlm.nih.gov/32854689/) | 2020 | Rapport de cas | BMC Endocrine Disorders | TSHome probable après Basedow initiale ; rechute de thyrotoxicose sous forme d'hyperthyroxinémie secondaire |
| [3923304](https://pubmed.ncbi.nlm.nih.gov/3923304/) | 1985 | Revue clinique | Medical Journal of Australia | Dilemme diagnostic hyperthyroxinémie sous amiodarone ; réponse médiocre aux antithyroïdiens ; mécanisme complexe |
| [8024995](https://pubmed.ncbi.nlm.nih.gov/8024995/) | 1994 | Série de cas | British Journal of Clinical Practice | Hyperthyroïdie + hyperemesis gravidarum : différenciation Basedow vs hyperthyroxinémie transitoire gestationnelle |

---

## Informations de Marché en France

Carbimazole ne dispose d'aucune Autorisation de Mise sur le Marché (AMM) référencée dans ce dossier.

> **Note** : Carbimazole est commercialisé dans d'autres pays européens (Royaume-Uni, Irlande) sous le nom Neo-Mercazole. Son statut auprès de l'ANSM doit être vérifié directement — le méthimazole (métabolite actif du carbimazole) est disponible en France sous Strumazol®. L'absence d'AMM carbimazole en France est à confirmer.

---

## Considérations de Sécurité

Les données de sécurité spécifiques (mises en garde, contre-indications, interactions médicamenteuses) ne sont pas disponibles dans ce dossier Evidence Pack.

Veuillez consulter la notice pour les informations de sécurité.

> **Signal de sécurité identifié dans la littérature** : La publication [PMID 12124735](https://pubmed.ncbi.nlm.nih.gov/12124735/) (2002, American Journal of Medical Genetics) rapporte un quatrième cas d'atrésie choanale chez un enfant dont la mère recevait la dose la plus élevée de carbimazole au moment critique du développement des choanes (jours 35-38 de gestation). Ce signal tératogène doit être documenté et intégré dans l'évaluation du profil de risque pour les indications liées à la grossesse.

---

## Conclusion et Prochaines Étapes

---

### Indication 1 : Résistance THRβ — **Hold**

**Justification :**
Malgré un score TxGNN de 99,71% (rang 1), le mécanisme d'action de carbimazole est directement opposé à l'objectif thérapeutique dans la RTHβ : réduire la T4 chez ces patients aggrave le déficit hormonal dans les tissus à récepteur THR normal sans corriger la résistance hypophysaire. Le cas PMID 24165508 illustre concrètement cette inadéquation.

**Pour avancer, les éléments suivants sont nécessaires :**
- Vérification par un expert en endocrinologie moléculaire de l'existence d'un mécanisme alternatif justifiant la prédiction TxGNN
- Exploration de la base de données du graphe de connaissances TxGNN pour identifier les arêtes à l'origine de cette prédiction surprenante

---

### Indication 2 : Thyrotoxicose Néonatale — **Proceed with Guardrails**

**Justification :**
L'usage empirique de carbimazole dans la thyrotoxicose néonatale est soutenu par 19 publications (études observationnelles, cohortes rétrospectives, séries de cas, revues cliniques — niveau L3) et une cohérence mécanistique forte. L'indication est reconnue en pratique clinique internationale même sans essai contrôlé randomisé dédié.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les données MOA complètes via DrugBank API (DB00389)
- Obtenir la notice/RCP complète pour les contre-indications et mises en garde pédiatriques (TFDA/ANSM)
- Confirmer le statut AMM en France auprès de l'ANSM (carbimazole vs méthimazole)
- Documenter le schéma posologique pédiatrique validé (500 µg/8h pour prématuré, d'après PMID 27747714)
- Évaluer et quantifier le risque tératogène lié à l'exposition maternelle en période embryonnaire (PMID 12124735)
- Établir un protocole de surveillance : TSH, T4L, T3L néonataux, NFS, bilan hépatique

---

### Indication 3 : Hyperthyroxinémie — **Research Question**

**Justification :**
L'hyperthyroxinémie est une entité nosologique hétérogène pour laquelle l'efficacité de carbimazole est strictement conditionnelle au sous-type étiologique. Le niveau de preuve est L4 (études mécanistiques et cas cliniques sans essai contrôlé), insuffisant pour progresser vers un développement sans stratification diagnostique préalable.

**Pour avancer, les éléments suivants sont nécessaires :**
- Définir précisément les sous-types cibles : hyperthyroïdie vraie (Basedow, TSHome) vs normothyroïdie avec T4 élevée (FDH, RTHβ) vs hyperthyroxinémie induite (amiodarone)
- Revue systématique de la littérature sur carbimazole dans l'hyperthyroxinémie amiodaronique
- Consultation d'expert en endocrinologie pour déterminer si un protocole de développement ciblé est envisageable
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

