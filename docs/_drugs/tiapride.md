---
layout: default
title: Tiapride
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 1
---

# Tiapride
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

# Tiapride : D'un Antagoniste Dopaminergique Benzamide vers la Migraine Chronique

## Résumé en Une Phrase

Tiapride est un antagoniste sélectif des récepteurs dopaminergiques D2/D3 de la famille des benzamides (apparenté au sulpiride) ; ses indications d'origine ne sont pas documentées dans ce jeu de données, le médicament n'étant pas commercialisé en France (0 AMM active).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Trouble Migraineux (migraine chronique)**,
avec **aucun essai clinique enregistré** mais **10 publications** (dont plusieurs essais contrôlés anciens) soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée (aucune AMM en France ; donnée manquante — voir DG002) |
| Nouvelle Indication Prédite | Migraine (Trouble Migraineux) |
| Score de Prédiction TxGNN | 99.18% |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action officiel (DrugBank) ne sont pas disponibles pour ce médicament. Sur la base des informations disponibles dans ce dossier de preuves, Tiapride est un antagoniste dopaminergique D2/D3 de la famille des benzamides (même famille que le sulpiride).

L'hypothèse mécanistique retenue est celle de « l'hypersensibilité dopaminergique » dans la physiopathologie de la migraine : les symptômes prodromiques (bâillements, nausées, changements d'humeur) seraient liés à une hyperactivité du système dopaminergique central. D'autres agents anti-dopaminergiques (metoclopramide, flunarizine) disposent déjà d'un usage clinique établi en traitement/prévention de la migraine, ce qui apporte un support indirect à la plausibilité de cette prédiction pour tiapride — mais aucune preuve moléculaire directe n'explique à ce jour son mécanisme d'action préventif dans la migraine.

L'indication d'origine du tiapride n'étant pas renseignée dans ce dossier (le produit n'est pas commercialisé en France et le champ MOA est marqué comme lacune de données — DG002, sévérité *High*), le lien mécanistique entre indication d'origine et nouvelle indication ne peut être établi de façon formelle à ce stade.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35548913](https://pubmed.ncbi.nlm.nih.gov/35548913/) | 2022 | ECR | Revista de neurología | Étude pilote randomisée en double aveugle comparant tiapride et topiramate en prophylaxie de la migraine chronique |
| [6256904](https://pubmed.ncbi.nlm.nih.gov/6256904/) | 1980 | ECR | La Semaine des Hôpitaux | Étude contrôlée versus placebo chez 40 patients migraineux ; effet du tiapride clairement démontré |
| [6266020](https://pubmed.ncbi.nlm.nih.gov/6266020/) | 1981 | ECR | La Semaine des Hôpitaux | Essai contrôlé chez 25 patients (migraine réfractaire / algie vasculaire de la face) : résultats excellents chez 10 patients |
| [7323625](https://pubmed.ncbi.nlm.nih.gov/7323625/) | 1981 | Cohorte (double aveugle) | Rivista di patologia nervosa e mentale | 300 mg/j pendant 30 jours chez 50 patients (dont 10 migraineux classiques) : bénéfice clinique chez 65% des patients |
| [6293072](https://pubmed.ncbi.nlm.nih.gov/6293072/) | 1982 | Cohorte | La Semaine des Hôpitaux | 180 patients dont 165 céphalalgiques : résultats bons à excellents chez 71% de ceux ayant terminé l'étude |
| [211624](https://pubmed.ncbi.nlm.nih.gov/211624/) | 1978 | Revue | La Semaine des Hôpitaux | Discussion du Tiapridal combinant effet antalgique, antiémétique et anticompulsif léger dans la céphalée/migraine |
| [6528587](https://pubmed.ncbi.nlm.nih.gov/6528587/) | 1984 | Revue | Wiadomości Lekarskie | Revue de l'usage des benzamides (sulpiride, tiapride) en traitement préventif de la migraine |
| [35831](https://pubmed.ncbi.nlm.nih.gov/35831/) | 1978 | Revue | La Semaine des Hôpitaux | Revue des approches thérapeutiques de la céphalée chronique, incluant les psychotropes |
| [39344](https://pubmed.ncbi.nlm.nih.gov/39344/) | 1979 | Série de cas | La Semaine des Hôpitaux | 4 patients traités ≥6 mois : résultats excellents à très bons, réduction de fréquence/intensité des crises |
| [229563](https://pubmed.ncbi.nlm.nih.gov/229563/) | 1979 | Série de cas | La Semaine des Hôpitaux | 47 patients gériatriques traités au tiapride pour indications variées (dyskinésie, agitation, alcoolisme) — non spécifique à la migraine |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

> Note : la notice/RCP TFDA n'a pas pu être récupérée pour ce médicament (lacune bloquante DG001), ce qui empêche toute évaluation de sécurité initiale (étape S1) à ce stade.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les données de sécurité réglementaire (notice/RCP, contre-indications, interactions) sont totalement manquantes et cette lacune est classée bloquante (DG001) — l'évaluation de sécurité S1 ne peut pas être complétée.
- Le médicament n'est pas commercialisé en France (0 AMM), et aucun essai clinique enregistré ne soutient l'indication migraine ; les preuves reposent uniquement sur une littérature ancienne (majoritairement 1978-1984), à effectifs réduits.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice/RCP officielle (TFDA ou équivalent) pour lever le blocage de sécurité (DG001)
- Compléter les données de mécanisme d'action via DrugBank (DG002)
- Identifier des essais cliniques enregistrés récents (ClinicalTrials.gov / ICTRP) sur tiapride et migraine
- Envisager une étude confirmative de Phase 2/3 avant toute réévaluation de la décision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

