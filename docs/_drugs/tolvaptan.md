---
layout: default
title: Tolvaptan
parent: 僅模型預測 (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan : De la Polykystose Rénale Autosomique Dominante (ADPKD, PKD1/PKD2) à la Polykystose Rénale Type 3

## Résumé en Une Phrase

Le tolvaptan est un antagoniste du récepteur V2 de la vasopressine, déjà approuvé par la FDA/EMA pour ralentir la progression de la maladie rénale polykystique autosomique dominante liée aux gènes PKD1/PKD2. Le modèle TxGNN prédit qu'il pourrait aussi être efficace pour la **polycystic kidney disease 3 (avec ou sans maladie polykystique du foie)**, un sous-type génétique distinct, avec un score de prédiction de **99,99 %** et **20 publications** (dont 2 essais randomisés de phase 3 sur l'ADPKD en général) soutenant cette direction — mais aucun essai clinique n'est actuellement enregistré spécifiquement pour le sous-type PKD3.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie rénale polykystique autosomique dominante (ADPKD), principalement associée aux gènes PKD1/PKD2 |
| Nouvelle Indication Prédite | Polycystic kidney disease 3 avec ou sans maladie polykystique du foie |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données structurées de mécanisme d'action (champ MOA de DrugBank) ne sont pas disponibles pour ce rapport. Sur la base des informations mécanistiques rapportées dans la littérature associée, le tolvaptan est un antagoniste sélectif du récepteur V2 de la vasopressine (V2R) : il inhibe la production d'AMPc dans les cellules épithéliales des tubes collecteurs rénaux, ce qui ralentit la prolifération kystique et la croissance du volume rénal total. Ce mécanisme est déjà validé et approuvé par la FDA/EMA pour l'ADPKD associée aux loci PKD1 et PKD2.

La polycystic kidney disease 3 (PKD3) est un sous-type génétiquement distinct au sein du même spectre nosologique des maladies rénales polykystiques/ciliopathies. Elle partage avec l'ADPKD classique une physiopathologie de type kystogenèse dépendante de la voie AMPc, ce qui rend l'extrapolation mécanistique plausible.

Cependant, aucune des publications recensées ne porte spécifiquement sur le locus PKD3 : les essais pivots (TEMPO 3:4, REPRISE) et la majorité des revues concernent l'ADPKD au sens large (PKD1/PKD2). L'applicabilité au sous-type PKD3 repose donc sur une extrapolation de voie commune plutôt que sur une preuve directe.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour l'indication « polycystic kidney disease 3 with or without polycystic liver disease ».

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | ECR | N Engl J Med | Essai TEMPO 3:4 : le tolvaptan ralentit la croissance du volume rénal total et le déclin de la fonction rénale dans l'ADPKD |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | ECR | N Engl J Med | Essai REPRISE : efficacité et sécurité du tolvaptan dans l'ADPKD à un stade plus avancé |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | ECR | Pediatr Nephrol | Essai randomisé (NCT02964273) évaluant sécurité et pharmacodynamie du tolvaptan chez l'enfant (5-17 ans) atteint d'ADPKD |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Revue/Consensus | Nephrol Dial Transplant | Consensus ERA/ERKNet/PKD International sur l'utilisation du tolvaptan dans l'ADPKD, approches fondées sur les preuves pour l'initiation du traitement |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Revue systématique | Nefrologia | Méta-analyse : efficacité et sécurité du tolvaptan dans le traitement de l'ADPKD |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Revue des interventions pour prévenir la progression de l'ADPKD, incluant les agents ciblant la pathogenèse |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Revue | JAMA | Revue générale de l'ADPKD : épidémiologie, physiopathologie et prise en charge |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Revue | Clin Liver Dis | L'usage du tolvaptan dans l'ADPKD ralentit la détérioration de la fonction rénale et la croissance kystique ; revue de la maladie polykystique hépatique associée |
| [40726372](https://pubmed.ncbi.nlm.nih.gov/40726372/) | 2025 | Revue | Curr Opin Nephrol Hypertens | Le tolvaptan reste le seul traitement approuvé par la FDA ciblant la progression de l'ADPKD ; revue des thérapies émergentes |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Revue/Directive | J Hepatol | Recommandations EASL sur la prise en charge des maladies hépatiques kystiques, incluant la maladie polykystique du foie |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Deux essais randomisés de phase 3 (TEMPO 3:4, REPRISE) et un consensus international établissent solidement l'efficacité du tolvaptan dans l'ADPKD au sens large, mais aucune preuve directe (essai clinique ou publication dédiée) ne cible spécifiquement le sous-type PKD3. La recommandation avance donc sous garde-fous, avec extrapolation mécanistique plutôt que preuve directe.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir le texte complet de l'notice/RCP TFDA (mises en garde, contre-indications) — actuellement un gap bloquant (DG001)
- Compléter les données structurées de MOA via l'API DrugBank (DG002)
- Confirmer si les cohortes des essais ADPKD existants incluent des patients porteurs du locus PKD3, ou lancer une étude dédiée
- Suivre le statut réglementaire en France, le produit n'étant actuellement pas commercialisé (0 AMM)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

