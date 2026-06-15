---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost : Du Glaucome à l'Alopécie

## Résumé en Une Phrase

Bimatoprost est un analogue prostamide F2α synthétique, approuvé à l'échelle internationale pour le traitement du glaucome et de l'hypertension oculaire, dont l'effet secondaire hypertrichosiant des cils a conduit à l'approbation FDA de Latisse pour l'hypotrichose des cils. Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Alopécie** (score 99,99%), avec **10 essais cliniques** et **20 publications** soutenant actuellement cette direction. Bien que TxGNN attribue ses scores les plus élevés à d'autres indications (syndromes malformatifs, rangs 1–7), l'analyse mécanistique identifie l'alopécie comme le seul candidat disposant à la fois d'une plausibilité biologique documentée et d'un corpus d'essais cliniques substantiel.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Glaucome / Hypertension oculaire (approbation internationale) ; hypotrichose des cils (Latisse, FDA) |
| Nouvelle Indication Prédite | Alopécie |
| Score de Prédiction TxGNN | 99,99% |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Bimatoprost active les récepteurs FP (récepteurs aux prostaglandines de type F2α) présents sur les cellules épithéliales des follicules pileux. Par ce mécanisme, il prolonge la phase anagène du cycle folliculaire (phase de croissance active) et stimule la prolifération des cellules de la gaine épithéliale interne. Ce lien a été découvert fortuitement chez des patients traités pour le glaucome par des analogues de prostaglandines, qui développaient une hypertrichose et un allongement marqué des cils comme effet secondaire.

Ce n'est pas une simple hypothèse théorique : la FDA a déjà approuvé bimatoprost 0,03% (Latisse) pour l'hypotrichose des cils, constituant une première validation clinique et réglementaire du concept de repositionnement vers les pathologies du follicule pileux. L'extension vers l'alopécie du cuir chevelu — qu'il s'agisse de l'alopécie androgénique (AGA) masculine ou féminine, ou de l'alopécie areata — repose sur le même mécanisme FP-récepteur, avec la nécessité d'une formulation topique adaptée assurant une pénétration cutanée suffisante au niveau du cuir chevelu.

Il est important de noter que TxGNN attribue ses scores les plus élevés à des indications comme les syndromes malformatifs parodontaux (rang 1, score 99,999%) ou le syndrome de Dandy-Walker (rang 2), qui sont des **faux positifs confirmés** par l'analyse mécanistique — aucune connexion biologique connue ne relie bimatoprost à ces pathologies, et aucun essai clinique ne les soutient. L'alopécie (rang 8, score 99,99%) est le seul candidat disposant à la fois d'une rationale mécanistique établie et d'un large corpus de données cliniques.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | Terminé | 307 | Évaluation de 3 doses de bimatoprost vs véhicule et minoxidil 5% OTC chez les hommes atteints d'alopécie androgénique — essai de référence masculin, design en double aveugle |
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | Terminé | 306 | Évaluation de 3 doses de bimatoprost vs véhicule et minoxidil 2% OTC chez les femmes atteintes d'alopécie de type féminin — essai de référence féminin, design en double aveugle |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | Terminé | 244 | Sécurité et efficacité de bimatoprost chez les hommes atteints d'AGA — essai de validation indépendant des deux essais précédents |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | Terminé | 71 | Sécurité et efficacité de bimatoprost 0,03% vs véhicule pour la perte des cils ou l'hypotrichose chez l'enfant — extension pédiatrique de l'indication approuvée |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | Terminé | 30 | Laser CO2 fractionné combiné à bimatoprost 0,03% pour l'alopécie areata — évaluation d'une approche combinée novatrice pour contourner la composante immunitaire |
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Phase 2 | Terminé | 33 | Effet de la solution bimatoprost sur la croissance des cheveux des follicules dépendants des androgènes — étude de validation mécanistique AGA |
| [NCT01189279](https://clinicaltrials.gov/study/NCT01189279) | Phase 1 | Terminé | 42 | Sécurité et pharmacocinétique d'une nouvelle formulation topique de bimatoprost chez des patients atteints d'alopécie — établissement de la base de sécurité cutanée |
| [NCT02676310](https://clinicaltrials.gov/study/NCT02676310) | Phase 1 | Terminé prématurément | 53 | Escalade de dose, sécurité et pharmacocinétique de bimatoprost topique dans l'AGA masculine — ⚠️ arrêté prématurément après 12 mois ; raison non documentée publiquement |
| [NCT02848300](https://clinicaltrials.gov/study/NCT02848300) | Phase 1 | Terminé | 11 | Pharmacocinétique locale et tolérance de bimatoprost topique sur le cuir chevelu (AGA masculine) — étude PK exploratoire à effectif limité |
| [NCT00187577](https://clinicaltrials.gov/study/NCT00187577) | NA | Terminé | 14 | Efficacité et sécurité de latanoprost et bimatoprost pour promouvoir la croissance des cils dans l'alopécie areata — preuve de concept initiale, étude en chassé-croisé |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [40252129](https://pubmed.ncbi.nlm.nih.gov/40252129/) | 2025 | ECR | Archives of Dermatological Research | ECR démontrant l'efficacité supérieure de l'association laser CO2 fractionné + bimatoprost dans l'alopécie areata, avec amélioration significative de la repousse vs contrôle |
| [32250713](https://pubmed.ncbi.nlm.nih.gov/32250713/) | 2022 | Revue systématique | Journal of Dermatological Treatment | Méta-analyse en réseau des traitements non chirurgicaux de l'AGA chez l'homme et la femme ; évaluation comparative rigoureuse incluant bimatoprost comme candidat émergent |
| [28264599](https://pubmed.ncbi.nlm.nih.gov/28264599/) | 2017 | Revue | Expert Opinion on Investigational Drugs | Synthèse complète du potentiel de bimatoprost pour l'alopécie des cils, des sourcils et du cuir chevelu — revue de référence pour ce repositionnement |
| [35278027](https://pubmed.ncbi.nlm.nih.gov/35278027/) | 2022 | Cohorte prospective | Dermatologic Therapy | Étude prospective ouverte : bimatoprost topique pour la perte des cils dans l'alopécie totale/universelle — 16 répondeurs sur 20 patients traités |
| [37089845](https://pubmed.ncbi.nlm.nih.gov/37089845/) | 2023 | Essai clinique ouvert | Indian Dermatology Online Journal | Bimatoprost vs propionate de clobétasol dans l'alopécie areata du cuir chevelu — bimatoprost évalué comme alternative thérapeutique de première ligne |
| [29863806](https://pubmed.ncbi.nlm.nih.gov/29863806/) | 2018 | Recommandations cliniques | Journal of Dermatology | Lignes directrices japonaises 2017 pour le diagnostic et le traitement de l'AGA masculine et féminine — contexte de positionnement thérapeutique |
| [33631058](https://pubmed.ncbi.nlm.nih.gov/33631058/) | 2021 | Revue systématique | Dermatologic Therapy | Revue systématique et méta-analyse en réseau des traitements de l'alopécie areata — classement hiérarchique des options thérapeutiques disponibles |
| [29854658](https://pubmed.ncbi.nlm.nih.gov/29854658/) | 2018 | Revue | Indian Dermatology Online Journal | Bimatoprost en dermatologie : de la découverte de l'effet hypertrichosiant à de nouvelles applications incluant alopecia et vitiligo |
| [35040730](https://pubmed.ncbi.nlm.nih.gov/35040730/) | 2022 | Étude de formulation | Drug Delivery | Formulation topique de bimatoprost à flux cutané 4,6× supérieur et dépôt dermique +529% — démontre la faisabilité galénique pour le cuir chevelu |
| [38577618](https://pubmed.ncbi.nlm.nih.gov/38577618/) | 2024 | Étude de formulation | International Journal of Pharmaceutics: X | Nano-système spanlastique pour délivrance cutanée optimisée de bimatoprost : supériorité de dépôt et efficacité de repousse démontrées dans l'AGA |

---

## Informations de Marché en France

Bimatoprost ne dispose actuellement d'aucune Autorisation de Mise sur le Marché (AMM) en France.

> **Contexte réglementaire international :** Bimatoprost est commercialisé dans de nombreux pays sous les noms Lumigan® (glaucome, usage ophtalmique) et Latisse® (hypotrichose des cils, approbation FDA). L'absence d'AMM française implique qu'une procédure complète auprès de l'ANSM ou via une procédure centralisée EMA serait nécessaire pour tout développement clinique ou commercial sur le marché français.

---

## Considérations de Sécurité

Veuillez consulter la notice de référence internationale pour les informations de sécurité complètes (données formelles non disponibles pour la France — voir DG001).

> **Point d'attention prioritaire :** L'essai NCT02676310 (Phase 1, AGA masculine, n=53, Allergan) a été terminé prématurément en mars 2017 après seulement 12 mois de recrutement. La raison de cet arrêt n'est pas documentée publiquement. Ce signal doit faire l'objet d'une investigation prioritaire — contact direct du promoteur ou consultation des données de pharmacovigilance — avant toute avancée dans le développement pour l'alopécie du cuir chevelu.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Bimatoprost présente un mécanisme d'action biologiquement établi sur les follicules pileux (activation des récepteurs FP prolongeant l'anagène), une validation réglementaire préalable déjà obtenue (Latisse/FDA pour hypotrichose des cils), et un portefeuille d'essais de Phase 2 substantiel dans l'AGA masculine et féminine représentant plus de 600 patients dans les essais de grade A (NCT01325337, NCT01325350, NCT01904721). Les preuves sont suffisantes pour justifier une avancée, mais l'absence de données Phase 3 réussies, la terminaison prématurée d'un essai Phase 1, et l'absence d'AMM française imposent des conditions strictes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Investigation prioritaire de la cause de terminaison prématurée de NCT02676310 (signal de sécurité potentiel à exclure formellement)
- Obtention des données de sécurité de la notice de référence — actuellement manquantes (**DG001, sévérité Bloquante**)
- Données complètes sur le mécanisme d'action via DrugBank (**DG002, sévérité Haute**)
- Sélection et priorisation de la population cible : AGA (meilleur corpus de données) vs alopécie areata vs hypotrichose du cuir chevelu
- Évaluation d'une formulation topique optimisée pour le cuir chevelu (travaux de formulation déjà disponibles dans la littérature : NCE topique, spanlastics)
- Évaluation de la faisabilité réglementaire pour une demande d'AMM française ou européenne (procédure ANSM nationale vs EMA centralisée)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

