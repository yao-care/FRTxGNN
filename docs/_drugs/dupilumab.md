---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab : De la Dermatite Atopique à la Bronchite

## Résumé en Une Phrase

Dupilumab est un anticorps monoclonal ciblant la sous-unité alpha du récepteur à l'interleukine-4 (IL-4Rα), approuvé dans de nombreux pays pour la dermatite atopique modérée à sévère, l'asthme et d'autres pathologies de type Th2.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Bronchite**,
avec **1 essai clinique** et **6 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dermatite atopique modérée à sévère (approuvée mondialement ; non enregistrée dans la base de données réglementaire locale) |
| Nouvelle Indication Prédite | Bronchite |
| Score de Prédiction TxGNN | 99.92% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Non enregistré dans la base de données locale |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de données actuelle. Sur la base des informations connues, dupilumab est un anticorps monoclonal humain appartenant à la classe des inhibiteurs de l'IL-4Rα : en se fixant à la sous-unité alpha partagée des récepteurs à l'IL-4 et à l'IL-13, il bloque simultanément la signalisation de ces deux cytokines, piliers centraux de la réponse immunitaire de type 2 (Th2). Son efficacité clinique est bien établie dans la dermatite atopique, l'asthme non contrôlé et la rhinosinusite chronique avec polypes nasaux.

Dans la bronchite à profil Th2 — notamment la bronchite éosinophilique —, l'IL-4 favorise la commutation de classe des immunoglobulines vers l'IgE et l'IL-13 stimule l'hypersécrétion de mucus ainsi que l'hyperréactivité bronchique. Ce mécanisme présente une très forte similitude avec celui de l'asthme, indication déjà approuvée pour dupilumab, où la réduction des exacerbations et l'amélioration du VEMS ont été démontrées dans plusieurs essais de Phase 3. Le blocage de l'IL-4Rα offre donc une base mécanistique cohérente pour supprimer l'inflammation éosinophilique des voies aériennes dans ce contexte.

Cependant, la bronchite (chronique, aiguë ou éosinophilique) constitue une entité clinique distincte de l'asthme, et la voie clinique directe pour cette indication spécifique n'a pas encore été établie par des essais prospectifs dédiés. La prédiction TxGNN est plausible par analogie mécanistique, mais reste à confirmer par des données interventionnelles ciblées.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Terminé | 33 | Efficacité de dupilumab dans la rhinosinusite chronique sans polypes nasaux (CRSsNP) — preuve indirecte via le concept de « united airway disease » et la physiopathologie Th2 partagée entre voies respiratoires supérieures et inférieures |

> **Note** : Cet essai cible la CRSsNP et non la bronchite directement. La pertinence repose sur le chevauchement mécanistique Th2 (grade C) ; il ne constitue pas une preuve clinique directe.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Revue systématique / Méta-analyse | J Asthma | Méta-analyse d'ECR : dupilumab réduit significativement les exacerbations et améliore le VEMS dans l'asthme non contrôlé — base mécanistique la plus solide pour les voies aériennes |
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | Phase 3 OLE | Lancet Respir Med | Étude TRAVERSE : sécurité et efficacité de dupilumab maintenues à long terme dans l'asthme modéré à sévère au-delà d'un an de traitement |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Observationnel / Pilote | Chest | Dupilumab réduit les défauts de ventilation régionaux évalués par IRM dans l'asthme sévère avec éosinophilie sputale — implication directe pour les obstructions bronchiques Th2 |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Revue | Tuberc Respir Dis | Revue des interventions pharmacologiques pour prévenir les exacerbations de BPCO, incluant les nouveaux agents biologiques anti-Th2 comme agents émergents |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Revue / Série de cas | Pediatr Pulmonol | Thérapies émergentes pour la bronchite plastique éosinophilique pédiatrique — dupilumab évoqué comme option thérapeutique prometteuse dans ce sous-type bronchique Th2 |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Revue | Expert Opin Pharmacother | Défis de la prise en charge de l'asthme associé aux maladies respiratoires induites par le tabac, dont la bronchite chronique et l'ACO ; souligne l'exclusion systématique des fumeurs des essais de biologiques |

---

## Informations de Marché en France

Aucune autorisation de mise sur le marché (AMM) n'est enregistrée pour dupilumab dans la base de données réglementaire locale interrogée.

> **Remarque** : Dupilumab (Dupixent®) bénéficie d'approbations réglementaires en Europe (EMA) et aux États-Unis (FDA) pour plusieurs indications dont la dermatite atopique modérée à sévère (≥ 6 mois), l'asthme, la rhinosinusite chronique avec polypes nasaux, l'œsophagite à éosinophiles et la dermatite de contact chronique. Le statut affiché ci-dessus reflète uniquement l'état de la base de données locale au moment de la requête (2026-06-07) et ne reflète pas le statut réglementaire EMA.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction TxGNN repose sur un mécanisme Th2 cohérent avec l'indication asthme déjà approuvée, mais l'absence d'essai clinique prospectif spécifiquement dédié à la bronchite et la nature exclusivement indirecte des preuves disponibles (L3 — voies respiratoires adjacentes) ne permettent pas de justifier un repositionnement immédiat sans données cliniques ciblées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Clarification de la définition clinique cible : bronchite aiguë, bronchite chronique éosinophilique ou bronchite plastique (les mécanismes et populations diffèrent)
- Données complètes sur le mécanisme d'action de dupilumab (actuellement absentes de la base)
- Biomarquage préalable des patients : sélection de la population Th2-positive (FeNO élevé, éosinophilie sanguine ≥ 300/µL) pour maximiser le signal clinique
- Conception et initiation d'un essai clinique Phase 2 dédié à la bronchite éosinophilique Th2
- Évaluation du profil de sécurité dans des sous-populations à risque (BPCO, fumeurs actifs, sujets exclus des essais asthme)
- Confirmation du statut réglementaire AMM en France (EMA) pour orienter la stratégie de repositionnement et d'accès
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

