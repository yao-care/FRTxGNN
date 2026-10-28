---
layout: default
title: Milrinone
parent: Prédiction du modèle uniquement (L5)
nav_order: 501
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Milrinone : nouvelle indication prédite, Alopécie (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM (les textes d'indication sont v…"
monitor_inn: "MILRINONE"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "headache disorder", "migraine disorder", "migraine with brainstem aura", "trigeminal autonomic cephalalgia", "acute pulmonary heart disease"]
---

# Milrinone
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Milrinone : De l'insuffisance cardiaque à l'alopécie (prédiction principale du modèle)
{: .text-alpha }

## Résumé en une phrase

Milrinone est un inhibiteur de la phosphodiestérase de type 3 (PDE3), utilisé en perfusion intraveineuse dans l'insuffisance cardiaque congestive.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**alopécie** (score de 0,9991), mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.
Parmi les autres prédictions, seules l'**insuffisance cardiaque congestive** et la **cardiopathie pulmonaire aiguë** disposent de preuves cliniques réelles, mais elles relèvent de l'usage cardiovasculaire déjà connu du médicament et non d'un véritable repositionnement.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans les données d'AMM (les textes d'indication sont vides) ; usage clinique connu : insuffisance cardiaque congestive |
| Nouvelle indication prédite | Alopécie |
| Score de prédiction TxGNN | 0,9991 |
| Niveau de preuve | L5 (prédiction du modèle uniquement) |
| Statut de marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le jeu de données. D'après les informations pharmacologiques connues, milrinone inhibe la PDE3 (cibles PDE3A et PDE3B), ce qui élève l'AMPc intracellulaire. Il en résulte un effet inotrope positif et une vasodilatation (effet « inodilatateur »), d'où son usage dans l'insuffisance cardiaque décompensée.

Pour l'alopécie, le lien mécanistique est **faible et spéculatif**. On pourrait invoquer une amélioration de la perfusion du cuir chevelu par vasodilatation, mais aucune donnée ne l'appuie. Le score élevé provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. Les autres prédictions capillaires (hypotrichose simple du cuir chevelu, hypotrichose congénitale avec milia, alopécie areata diffuse) sont dans la même situation : pathologies génétiques ou auto-immunes (voie JAK/IFN-γ pour l'alopécie areata) sans lien PDE3 établi.

Les prédictions les mieux étayées sont cardiovasculaires. Pour la **céphalée**, la littérature porte sur le syndrome de vasoconstriction cérébrale réversible (SVCR), où la milrinone, par voie intra-artérielle ou intraveineuse, a levé le vasospasme dans des cas isolés. L'extrapolation aux céphalées primaires reste indirecte. Pour la **migraine**, les vasodilatateurs sont plutôt des facteurs déclenchants.

## Preuves d'essais cliniques

Aucun essai clinique associé n'est enregistré pour l'alopécie. Les essais ci-dessous concernent l'**insuffisance cardiaque congestive** (prédiction n° 6) et la **cardiopathie pulmonaire aiguë** (prédiction n° 10) ; ils illustrent l'usage cardiovasculaire de la milrinone, pas l'indication capillaire.

| Numéro d'essai | Phase | Statut | Inscription | Résultats principaux |
|---------|------|------|------|---------|
| [NCT01849094](https://clinicaltrials.gov/study/NCT01849094) | Phase 1/2 | Terminé | 9 | Formulation orale à libération prolongée : profil pharmacocinétique et effet hémodynamique dans l'insuffisance cardiaque |
| [NCT01956006](https://clinicaltrials.gov/study/NCT01956006) | Phase 1/2 | Terminé | 26 | Étude pilote de milrinone orale à libération prolongée dans l'insuffisance cardiaque avancée |
| [NCT07186062](https://clinicaltrials.gov/study/NCT07186062) | Phase 4 | Terminé | 60 | Lévosimendan vs dobutamine vs milrinone dans l'insuffisance cardiaque aiguë décompensée avec atteinte rénale |
| [NCT03207165](https://clinicaltrials.gov/study/NCT03207165) | Phase 4 | Terminé | 192 | Milrinone vs dobutamine chez des patients critiques en unité de soins coronariens |
| [NCT04718350](https://clinicaltrials.gov/study/NCT04718350) | Non applicable | Terminé | 40 | Milrinone inhalée vs lévosimendan IV en chirurgie cardiaque avec hypertension pulmonaire |
| [NCT05450328](https://clinicaltrials.gov/study/NCT05450328) | Phase 2 | En recrutement | 141 | Milrinone inhalée et époprosténol pour prévenir le sevrage difficile de la circulation extracorporelle |
| [NCT02077010](https://clinicaltrials.gov/study/NCT02077010) | Phase 1 | Terminé | 10 | Milrinone nébulisée dans l'insuffisance cardiaque avancée hospitalisée (exploratoire) |
| [NCT02408003](https://clinicaltrials.gov/study/NCT02408003) | Non applicable | Terminé | 30 | Déformation cardiaque et hémodynamique sous lévosimendan ou milrinone |
| [NCT00338455](https://clinicaltrials.gov/study/NCT00338455) | Phase 2 | Arrêté | 16 | Nésiritide chez des candidats à la greffe sous dobutamine ou milrinone ; pertinence limitée pour la milrinone |
| [NCT02644057](https://clinicaltrials.gov/study/NCT02644057) | Phase 2 | Retiré | 0 | Dobutamine vs milrinone dans le syndrome cardio-rénal ; aucune donnée |

## Preuves de la littérature

Aucune publication n'est disponible pour l'alopécie. Les références ci-dessous concernent les indications cardiovasculaires et le SVCR (céphalée).

| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [25625413](https://pubmed.ncbi.nlm.nih.gov/25625413/) | 2015 | Revue systématique / méta-analyse | Basic Clin Pharmacol Toxicol | Sécurité et efficacité de la milrinone dans l'insuffisance cardiaque aiguë après infarctus du myocarde |
| [37999764](https://pubmed.ncbi.nlm.nih.gov/37999764/) | 2024 | Revue systématique / méta-analyse | Eur J Pediatr | Rôle de la milrinone dans l'insuffisance cardiaque et l'hypertension pulmonaire du nouveau-né et de l'enfant |
| [3591689](https://pubmed.ncbi.nlm.nih.gov/3591689/) | 1987 | Essai randomisé (79 patients) | Am J Cardiol | Milrinone IV vs dobutamine dans l'insuffisance cardiaque congestive d'origine ischémique ou dilatée |
| [2035427](https://pubmed.ncbi.nlm.nih.gov/2035427/) | 1991 | Essai de phase III multicentrique | Am Heart J | Bénéfices hémodynamiques et cliniques de la perfusion de milrinone dans l'insuffisance cardiaque chronique sévère (189 patients) |
| [4019930](https://pubmed.ncbi.nlm.nih.gov/4019930/) | 1985 | Étude clinique | J Am Coll Cardiol | Amélioration hémodynamique aiguë et chronique sous milrinone orale chez 37 patients |
| [31865433](https://pubmed.ncbi.nlm.nih.gov/31865433/) | 2020 | Étude clinique comparative | Heart Vessels | Milrinone vs olprinone chez 288 patients hospitalisés pour insuffisance cardiaque |
| [37322827](https://pubmed.ncbi.nlm.nih.gov/37322827/) | 2023 | Étude comparative | ESC Heart Fail | Mortalité et hémodynamique sous milrinone dans le choc cardiogénique par insuffisance cardiaque décompensée |
| [26879807](https://pubmed.ncbi.nlm.nih.gov/26879807/) | 2016 | Revue | Clin Res Cardiol | Les inotropes IV au long cours sont associés à une surmortalité dans l'insuffisance cardiaque avancée |
| [18647181](https://pubmed.ncbi.nlm.nih.gov/18647181/) | 2009 | Cas clinique | Headache | Milrinone intra-artérielle dans un SVCR avec déficit neurologique focal |
| [34784343](https://pubmed.ncbi.nlm.nih.gov/34784343/) | 2021 | Cas clinique | Am J Case Rep | SVCR sur fond d'éclampsie répondant à la perfusion de milrinone |

## Informations de marché en France

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Indication approuvée |
|---------|------|------|-----------|
| 61448776 | COROTROPE 10 mg/10 ml, solution injectable IV (SANOFI WINTHROP INDUSTRIE) | Solution injectable | Non renseignée (AMM active) |
| 61412965 | MILRINONE TILLOMED 1 mg/mL (TILLOMED PHARMA) | Solution injectable ou pour perfusion | Non renseignée (AMM active) |
| 65725263 | MILRINONE CARINOPHARM 1 mg/ml (CARINOPHARM) | Solution injectable ou pour perfusion | Non renseignée (AMM active) |
| 64507226 | MILRINONE STRAGEN 1 mg/ml (STRAGEN-FRANCE) | Solution injectable | Non renseignée (AMM active) |

## Considérations de sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie, et non texte de la notice) : maladie rénale, hypotension, infarctus du myocarde et thrombose coronaire, arrêt cardiaque soudain, maladies de la conduction cardiaque, sténose valvulaire pulmonaire, cardiomyopathie hypertrophique (y compris familiale), hémoglobinopathie, pyo-uretère.
- **Interactions médicamenteuses** (niveau modéré) : amifostine, diatrizoate, anagrélide, ozanimod, procarbazine. Les cibles pharmacologiques identifiées sont PDE2A, PDE3A, PDE3B et PDE5A.
- **Point d'attention** : l'usage oral au long cours a été associé à une surmortalité (essai PROMISE), et les inotropes IV prolongés sont liés à une surmortalité dans l'insuffisance cardiaque avancée. Une surveillance de l'hypotension et des arythmies, ainsi qu'un ajustement de la dose selon la fonction rénale, sont nécessaires.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui ne sont pas disponibles dans les données compilées pour ce rapport.

## Conclusion et prochaines étapes

**Décision : Hold** (pour l'alopécie)

**Justification :**
- La prédiction pour l'alopécie repose uniquement sur le score du modèle, sans essai, sans publication et sans mécanisme plausible. Les autres indications capillaires prédites sont dans la même situation.
- Seules l'insuffisance cardiaque congestive et la cardiopathie pulmonaire aiguë (niveau L2, « Proceed with Guardrails ») disposent de preuves réelles, mais elles correspondent à l'usage cardiovasculaire connu et non à un repositionnement. La céphalée (niveau L4, simple question de recherche) ne repose que sur des cas cliniques de SVCR.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications officielles de la notice (ANSM), actuellement manquantes et bloquantes pour le criblage de sécurité
- Obtenir les données de mécanisme d'action (DrugBank) pour évaluer tout lien avec les pathologies capillaires
- Des données précliniques (perfusion du cuir chevelu, follicule pileux) avant toute étude clinique dans l'alopécie
- Clarifier l'indication originale réelle et le statut des AMM, toutes annulées en France
- Pour les indications cardiovasculaires : un essai randomisé de phase 3 pour atteindre le niveau L1, et un plan de surveillance de l'hypotension, des arythmies et de la fonction rénale
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

