---
layout: default
title: Prednisolone
parent: 僅模型預測 (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
---

# Prednisolone
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

# Prednisolone : De la Corticothérapie Systémique à la Pelade (Alopecia Areata)

## Résumé en Une Phrase

Prednisolone est un glucocorticoïde de synthèse largement utilisé pour ses propriétés anti-inflammatoires et immunosuppressives dans de nombreuses pathologies inflammatoires et auto-immunes. Le modèle TxGNN prédit qu'il pourrait être efficace pour la **pelade (alopecia areata)**, avec **18 essais cliniques** et **20 publications** actuellement associés à cette indication dans la littérature.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée dans les données disponibles (aucune AMM française répertoriée) — usage général reconnu comme corticothérapie anti-inflammatoire/immunosuppressive systémique |
| Nouvelle Indication Prédite | Pelade (Alopecia Areata) |
| Score de Prédiction TxGNN | 99.99 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le pack de preuves. Sur la base des informations connues, la prednisolone fait partie de la classe des glucocorticoïdes de synthèse (corticostéroïdes), dont l'efficacité anti-inflammatoire et immunosuppressive est largement établie dans de nombreuses pathologies inflammatoires et auto-immunes, et mécanistiquement pourrait être applicable à la pelade.

La pelade résulte d'une agression auto-immune à médiation lymphocytaire T contre le privilège immunitaire (immune privilege) du follicule pileux. L'action immunosuppressive et anti-inflammatoire de la prednisolone peut directement inhiber l'infiltration des lymphocytes T CD8+ autour du follicule pileux, ce qui constitue une concordance mécanistique forte avec la physiopathologie de la maladie.

La corticothérapie orale en bolus (pulse) est déjà une option de pratique clinique établie pour les formes modérées à sévères de pelade, ce qui renforce la plausibilité de cette prédiction. Toutefois, les effets secondaires d'un usage prolongé (densité osseuse, métabolisme, suppression surrénalienne) doivent impérativement être intégrés à l'évaluation de sécurité avant toute utilisation clinique élargie.

---

## Preuves d'Essais Cliniques

*Note : la requête TxGNN a retourné 18 essais associés à cette indication, mais la majorité concerne en réalité le lupus érythémateux systémique ou d'autres pathologies sans lien direct (probable erreur d'appariement dans la base de données, signalée comme non pertinente dans l'évaluation de pertinence). Seuls les essais directement pertinents pour la pelade sont présentés ci-dessous.*

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Terminé | 42 | Essai évaluant un protocole de méthylprednisolone orale en bolus à haute dose et fréquence accrue chez des patients atteints de pelade sévère résistante aux traitements conventionnels (formes étendue, totale, universelle, ophiasique) |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | Observationnelle (N/A) | Terminé | 296 | Évaluation de la sécurité et de l'efficacité du tofacitinib (Rhofanib®) chez des patients atteints de pelade, avec ou sans prednisolone en traitement adjuvant |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Inconnu | 20 | Comparaison de deux techniques d'injection intralésionnelle de corticostéroïde (DERMOJET sans aiguille vs seringue conventionnelle) chez des patients atteints de pelade |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | ECR | J Am Acad Dermatol | Premier essai randomisé contrôlé par placebo évaluant la prednisolone orale en bolus dans la pelade ; aucune étude antérieure n'avait été randomisée ou contrôlée par placebo |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Revue (méta-analyse en réseau) | Cochrane Database Syst Rev | Méta-analyse en réseau Cochrane comparant les traitements de la pelade (immunosuppresseurs, stimulants de pousse, immunothérapie de contact), incluant les corticostéroïdes systémiques |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | Revue systématique | Australas J Dermatol | Revue systématique des traitements systémiques de la pelade (formes étendue, totale, universelle) couvrant la littérature de 1946 à 2018, incluant les essais randomisés sur corticostéroïdes |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Revue | Dermatol Pract Concept | Revue sur l'efficacité et les effets indésirables de la corticothérapie en bolus dans la pelade, incluant taux de rechute et facteurs pronostiques de réponse |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | Étude clinique | Dermatoendocrinol | Prednisolone en bolus à dose moyenne dans la pelade ; efficace en phase précoce mais effets secondaires significatifs pouvant entraîner l'arrêt du traitement |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Cohorte rétrospective | Dermatol Ther | Comparaison méthylprednisolone seule vs méthylprednisolone + méthotrexate dans la pelade étendue (26 patients) |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | Cohorte | J Dtsch Dermatol Ges | Protocole séquentiel haute dose puis faible dose de corticostéroïdes systémiques chez l'enfant atteint de pelade sévère ; bonne réponse initiale mais rechute fréquente à l'arrêt |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Revue | Pediatr Dermatol | Revue des protocoles de dose et d'administration de la corticothérapie en bolus pédiatrique dans la pelade, incluant les effets secondaires associés |
| [30294905](https://pubmed.ncbi.nlm.nih.gov/30294905/) | 2019 | Étude mécanistique | J Cosmet Dermatol | Modification des taux sériques et tissulaires de TNF-α, éclairant le mécanisme d'action de la corticothérapie orale en bolus dans la pelade |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Revue | J Dermatolog Treat | Corticothérapie orale en mini-bolus par dexaméthasone comme alternative durable chez les patients inéligibles aux inhibiteurs de JAK, pour pelade sévère |

---

## Informations de Marché en France

Prednisolone (DrugBank DB00860) n'est associé à aucune AMM dans les données disponibles (0 licence répertoriée, statut : non commercialisé). Aucune information de marché n'est donc disponible pour ce candidat.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Un essai randomisé contrôlé par placebo (PMID 15692475) et un essai Phase 4 (NCT01167946) soutiennent directement l'usage de la prednisolone en bolus dans la pelade sévère, complétés par plusieurs revues systématiques et études de cohorte convergentes — d'où un niveau de preuve L2. Le mécanisme d'action (immunosuppression T-lymphocytaire) est mécanistiquement cohérent avec la physiopathologie de la maladie. Cependant, l'absence de données réglementaires françaises (仿單/TFDA) constitue un obstacle bloquant à l'évaluation de sécurité formelle (S1), ce qui justifie une progression prudente sous garde-fous plutôt qu'une décision "Go" complète.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les données de mises en garde/contre-indications officielles (仿單 TFDA) — actuellement bloquantes pour l'évaluation de sécurité initiale
- Compléter les données de mécanisme d'action (MOA) via l'API DrugBank
- Réaliser une requête complète des interactions médicamenteuses (DDI), actuellement introuvables
- Évaluer les modalités d'accès en France en l'absence d'AMM existante (voie ATU/RTU ou équivalent)
- Établir un plan de surveillance des effets indésirables liés à un usage prolongé (densité osseuse, métabolisme, axe surrénalien) en contexte de traitement en bolus pour la pelade
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

