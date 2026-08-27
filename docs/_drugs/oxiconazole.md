---
layout: default
title: Oxiconazole
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 1
---

# Oxiconazole
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

# Oxiconazole : Des Mycoses Cutanées Superficielles à la Candidose Cutanée

## Résumé en Une Phrase

Oxiconazole est un antifongique topique de la classe des imidazolés, historiquement utilisé pour traiter les mycoses cutanées superficielles (dermatophytoses, candidoses cutanées).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Candidose Cutanée**,
avec **0 essai clinique enregistré** et **5 publications** soutenant actuellement cette direction, dont un essai clinique comparatif historique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mycoses cutanées superficielles (usage topique antifongique) |
| Nouvelle Indication Prédite | Candidose Cutanée |
| Score de Prédiction TxGNN | 99.81% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action officiel (fiche DrugBank structurée) ne sont pas disponibles dans ce rapport. Sur la base des informations pharmacologiques connues, l'oxiconazole est un antifongique imidazolé à usage topique, dont l'efficacité contre les mycoses cutanées superficielles est bien établie en pratique clinique.

Mécanistiquement, l'oxiconazole inhibe l'enzyme fongique lanostérol 14α-déméthylase (CYP51), bloquant ainsi la biosynthèse de l'ergostérol et compromettant l'intégrité de la membrane cellulaire fongique. Cette action confère au médicament une activité fongicide/fongistatique directe contre *Candida albicans* et d'autres espèces du genre Candida.

Ce mécanisme n'est pas une extrapolation indirecte : il s'agit du mode d'action pharmacologique central du médicament, ce qui explique la forte pertinence mécanistique entre l'usage antifongique d'origine de l'oxiconazole et la candidose cutanée prédite par TxGNN. L'indication prédite s'inscrit ainsi dans le prolongement naturel du spectre d'activité déjà connu de la molécule plutôt que dans une nouvelle classe thérapeutique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [6382000](https://pubmed.ncbi.nlm.nih.gov/6382000/) | 1984 | Essai Clinique Comparatif | Mykosen | Comparaison de l'oxiconazole (Ro 13-8996) et de l'econazole dans le traitement des dermatomycoses |
| [24196340](https://pubmed.ncbi.nlm.nih.gov/24196340/) | 2013 | Revue | J Drugs Dermatol | Optimisation du traitement antifongique topique des infections fongiques cutanées superficielles, incluant les dermatophytoses |
| [10439936](https://pubmed.ncbi.nlm.nih.gov/10439936/) | 1999 | Revue | Drugs | Mise à jour sur l'usage des antifongiques allylamines/imidazolés dans les mycoses superficielles, efficacité fongistatique sur *Candida albicans* |
| [2670516](https://pubmed.ncbi.nlm.nih.gov/2670516/) | 1989 | Revue | Drugs | Activité antimicrobienne à large spectre des imidazolés topiques (dermatophytes, levures, champignons dimorphiques) dans les mycoses superficielles |
| [7501581](https://pubmed.ncbi.nlm.nih.gov/7501581/) | 1995 | Revue | Postgrad Med | Approche diagnostique et thérapeutique des infections fongiques cutanées et candidosiques, traitement par antifongiques topiques |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Le mécanisme d'action de l'oxiconazole (inhibition directe de la synthèse de l'ergostérol fongique) constitue une base mécanistique forte et directe pour l'indication de candidose cutanée, mais aucun essai clinique n'est actuellement enregistré pour cette indication précise, et des lacunes de données bloquantes (仿單/mises en garde TFDA, statut réglementaire en France) empêchent une évaluation de sécurité complète.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les mises en garde et contre-indications officielles (notice/RCP) — actuellement une lacune bloquante (DG001)
- Confirmer les indications d'origine et le MOA structuré via une source officielle (DrugBank complet) (DG002)
- Vérifier l'existence d'une voie d'accès au marché français (produit actuellement non commercialisé, 0 AMM)
- Envisager la conception d'un essai clinique dédié ou l'analyse rétrospective de données d'usage réel pour la candidose cutanée
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

