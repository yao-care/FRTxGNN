---
layout: default
title: Itraconazole
parent: 僅模型預測 (L5)
nav_order: 158
evidence_level: L5
indication_count: 1
---

# Itraconazole
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

# Itraconazole : Des Mycoses Systémiques à la Pneumocystose

## Résumé en Une Phrase

L'itraconazole est un antifongique triazolé dont l'usage établi concerne le traitement des mycoses systémiques et superficielles. Le modèle TxGNN prédit une efficacité potentielle contre la **pneumocystose** (pneumonie à *Pneumocystis jirovecii*), avec un score de confiance de **99,34%**, mais cette direction n'est actuellement soutenue par **aucun essai clinique** et repose sur **20 publications** de nature majoritairement indirecte (revues sur les infections opportunistes, séries de cas), sans démonstration mécanistique ou clinique directe de l'efficacité de l'itraconazole contre ce pathogène.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mycoses systémiques (usage antifongique établi ; aucune donnée d'AMM française disponible dans le dossier) |
| Nouvelle Indication Prédite | Pneumocystose |
| Score de Prédiction TxGNN | 99,34% |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données structurées sur le mécanisme d'action (MOA) ne sont pas disponibles dans le dossier produit (Data Gap identifié en priorité *High*). Cependant, la littérature pharmacologique disponible permet de reconstituer le raisonnement mécanistique suivant : l'itraconazole est un antifongique triazolé qui agit en inhibant l'enzyme 14α-déméthylase, bloquant ainsi la synthèse de l'ergostérol fongique — un mécanisme efficace contre les champignons filamenteux et levures classiques (*Aspergillus*, *Candida*, *Histoplasma*, etc.).

Le lien entre l'indication originale (mycoses systémiques) et la nouvelle indication prédite (pneumocystose) tient au fait que *Pneumocystis jirovecii* est classé taxonomiquement parmi les champignons. Toutefois, cette similarité est superficielle : *P. jirovecii* dépend principalement de l'absorption du cholestérol de l'hôte comme source de stérols membranaires plutôt que de sa propre voie de synthèse de l'ergostérol. C'est précisément la raison pharmacologique pour laquelle les antifongiques azolés ont une efficacité limitée contre la pneumocystose, et pourquoi les recommandations cliniques actuelles ne préconisent pas leur usage en traitement ou en prophylaxie de la PCP.

Le traitement et la prophylaxie standard de la pneumocystose reposent aujourd'hui sur le TMP-SMX, la pentamidine, l'atovaquone et la dapsone — aucun n'étant un dérivé azolé. Le score TxGNN élevé (99,34%) provient vraisemblablement d'un **signal artefactuel de co-occurrence** dans le graphe de connaissances : itraconazole apparaît fréquemment associé aux mêmes contextes cliniques (patients immunodéprimés, VIH, greffés) que d'autres antifongiques réellement efficaces contre la pneumocystose, sans que cela reflète une efficacité propre du médicament sur ce pathogène.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement (ni sur ClinicalTrials.gov, ni sur ICTRP).

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | ECR | HIV Medicine | Essai randomisé en double aveugle contrôlé par placebo sur l'itraconazole en capsules pour la prévention des mycoses profondes chez des patients VIH+ ; ne cible pas spécifiquement la pneumocystose comme critère de jugement |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Revue | Drugs | Revue de la thérapie et prophylaxie des infections protozoaires systémiques incluant *Pneumocystis carinii* ; ne rapporte pas de données spécifiques sur l'itraconazole contre ce pathogène |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Rapport de cas | Frontiers in Immunology | Coïnfection rare *Talaromyces marneffei* / *Pneumocystis jirovecii* chez un enfant porteur d'une mutation STAT1 ; ne documente pas l'usage de l'itraconazole contre la pneumocystose elle-même |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Revue | BMJ Clinical Evidence | Revue des stratégies de prophylaxie primaire/secondaire des infections opportunistes chez les patients VIH ; l'itraconazole n'y figure pas comme option de référence contre *P. jirovecii* |
| [7877856](https://pubmed.ncbi.nlm.nih.gov/7877856/) | 1994 | Revue | Pathologie-biologie | Revue de l'aspergillose au cours du SIDA ; note qu'une pneumocystose antérieure est un facteur de risque associé, sans lien de traitement direct avec l'itraconazole |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Revue | Seminars in Respiratory Infections | Revue générale des infections après transplantation pulmonaire et des stratégies antimicrobiennes associées |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Revue | Current Clinical Topics in Infectious Diseases | Revue de la prophylaxie et du traitement des infections chez les receveurs de greffe de moelle osseuse |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohorte | Transplantation Proceedings | Expérience monocentrique sur les infections fongiques invasives après transplantation rénale |
| [17594870](https://pubmed.ncbi.nlm.nih.gov/17594870/) | 2007 | Cohorte/Revue | Allergologia et immunopathologia | 25 ans d'expérience sur la maladie granulomateuse chronique pédiatrique et ses complications fongiques |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Cohorte | Indian Journal of Medical Microbiology | Comparaison des pathogènes fongiques respiratoires selon le statut immunitaire et le taux de CD4+ |

**Note importante :** aucune des publications recensées ne démontre directement une efficacité de l'itraconazole dans le traitement ou la prévention de la pneumocystose. Il s'agit principalement de revues et d'études de cohorte sur les infections opportunistes en contexte d'immunodépression, où l'itraconazole est cité parmi d'autres antifongiques sans évaluation spécifique face à *P. jirovecii*.

---

## Informations de Marché en France

L'itraconazole n'est actuellement associé à **aucune AMM enregistrée en France** dans le dossier (0 licence, statut « non commercialisé »). Les données réglementaires ANSM détaillées (仿單/notice) constituent un point bloquant identifié (DG001) et devront être obtenues directement auprès de l'ANSM avant toute évaluation de sécurité.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

*(Les mises en garde, contre-indications et interactions médicamenteuses n'ont pas pu être documentées à partir des sources actuellement disponibles — requête DDI sans résultat, notice ANSM non exploitée.)*

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Aucun essai clinique ne soutient l'usage de l'itraconazole dans la pneumocystose, et la littérature disponible n'apporte que des preuves indirectes (revues générales sur les infections opportunistes). Le mécanisme d'action connu de l'itraconazole (inhibition de la synthèse de l'ergostérol fongique) est peu compatible avec la biologie de *Pneumocystis jirovecii*, qui dépend du cholestérol de l'hôte — ce qui explique pourquoi les guides cliniques actuels ne recommandent pas les azolés pour cette indication. Le score TxGNN élevé est probablement un artefact de co-occurrence dans le graphe de connaissances plutôt qu'un signal mécanistique réel.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice/仿單 ANSM complète (mises en garde, contre-indications) — point bloquant (DG001)
- Données de mécanisme d'action (MOA) structurées via DrugBank (DG002)
- Études précliniques ou in vitro évaluant spécifiquement l'activité de l'itraconazole contre *Pneumocystis jirovecii* (actuellement absentes)
- Comparaison formelle avec les traitements de référence (TMP-SMX, pentamidine, atovaquone, dapsone) si de nouvelles preuves mécanistiques émergent
- Sans nouvelle preuve mécanistique ou clinique directe, il n'est pas recommandé d'engager des ressources supplémentaires sur cette piste
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

