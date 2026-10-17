---
layout: default
title: Metoprolol
parent: Prédiction du modèle uniquement (L5)
nav_order: 492
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Metoprolol : nouvelle indication prédite, Néphropathie hypertensive maligne (niveau de preuve L5). Indication d'origine : Non renseignée dans les textes d'AMM disponibles"
monitor_inn: "metoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "chronic pulmonary heart disease", "trichotillomania"]
---

# Metoprolol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Métoprolol : De l'hypertension et de l'infarctus du myocarde à la cardiopathie pulmonaire chronique

## Résumé en Une Phrase

Le métoprolol est un bêtabloquant cardiosélectif (bêta-1), initialement utilisé dans l'hypertension artérielle, le syndrome coronarien aigu et l'infarctus du myocarde.
Le modèle TxGNN prédit en premier rang des indications proches de l'hypertension (hypertension rénale maligne, hypertension rénovasculaire maligne), mais l'indication la mieux documentée est la **cardiopathie pulmonaire chronique**, avec **4 essais cliniques** et **20 publications** associés (preuves indirectes, centrées sur la BPCO).
Pour l'ensemble des prédictions, les preuves restent faibles : aucune étude ne démontre l'efficacité du métoprolol dans ces nouvelles indications.

---

## Aperçu Rapide

Les données compilées pour ce rapport portent sur dix indications prédites. Le tableau ci-dessous présente la prédiction classée n° 1 (conformément au format standard) ; l'indication la mieux étayée est indiquée à part.

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les textes d'AMM disponibles ; indications issues du graphe de connaissances : hypertension, syndrome coronarien aigu, infarctus du myocarde |
| Nouvelle Indication Prédite (rang 1) | Néphropathie hypertensive maligne |
| Score de Prédiction TxGNN | 99,91 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement) |
| Indication la mieux documentée | Cardiopathie pulmonaire chronique (score 99,40 %, niveau L3) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 14 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, le métoprolol est un bêtabloquant sélectif des récepteurs bêta-1 : il diminue la fréquence cardiaque, la contractilité et la consommation d'oxygène du myocarde, et réduit la sécrétion de rénine.

**Prédictions de rang 1 et 2 (néphropathie hypertensive maligne, hypertension rénovasculaire maligne).** Ces indications sont des extensions de l'hypertension déjà connue. La réduction de la pression artérielle et de la libération de rénine rend l'hypothèse plausible. Cependant, aucun essai ni publication pertinente n'étaye ces indications. Le seul article rattaché à l'hypertension rénovasculaire concerne la chromogranine A comme marqueur diagnostique du phéochromocytome et ne traite pas du métoprolol. Le score élevé reflète surtout la proximité avec l'indication connue.

**Infarctus du myocarde postéro-inférieur, postéro-latéral et septal.** Ce sont des sous-types d'une indication existante : l'apport en repositionnement est donc limité.

**Cardiopathie pulmonaire chronique.** La sélectivité bêta-1 limite le risque de bronchoconstriction, et des données observationnelles suggèrent que les bêtabloquants sont globalement tolérés en cas de BPCO associée à une cardiopathie. Mais les preuves portent sur la sécurité du métoprolol chez les patients atteints de BPCO, et non sur son efficacité dans la cardiopathie pulmonaire elle-même.

**Autres prédictions** (hypertension pulmonaire, syndrome de Braddock, trichotillomanie) : aucun lien mécanistique crédible n'est établi ; il s'agit vraisemblablement d'artefacts du graphe de connaissances. Dans l'hypertension pulmonaire, les bêtabloquants sont d'ordinaire utilisés avec prudence en raison du risque pour la fonction ventriculaire droite.

---

## Preuves d'Essais Cliniques

Seule la cardiopathie pulmonaire chronique dispose d'essais enregistrés. Les autres indications prédites n'ont aucun essai associé.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT06825728](https://clinicaltrials.gov/study/NCT06825728) | Phase 4 | Pas encore en recrutement | 311 | Métoprolol dans l'insuffisance cardiaque à fraction d'éjection réduite avec BPCO ; critère principal : mortalité toute cause et réhospitalisations. Pas de résultats. |
| [NCT02587351](https://clinicaltrials.gov/study/NCT02587351) | Phase 3 | Arrêté | 532 | BLOCK-COPD : métoprolol versus placebo pour prévenir les exacerbations de BPCO. Arrêté prématurément ; pas de bénéfice démontré. |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Phase 4 | Retiré | 0 | Étude CAMERA : effets respiratoires du carvédilol et du métoprolol dans l'insuffisance cardiaque. Aucun patient inclus, donc aucune donnée. |
| [NCT05096884](https://clinicaltrials.gov/study/NCT05096884) | Phase 1 précoce | Arrêté | 14 | Dyspnée d'effort et tachycardie après COVID-19. Lien faible avec l'indication prédite. |

---

## Preuves de la Littérature

Publications les plus pertinentes pour la cardiopathie pulmonaire chronique (BPCO avec maladie cardiaque) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | ECR | JAMA | Essai BICS (bisoprolol) dans la BPCO à haut risque d'exacerbation ; rappelle que le métoprolol n'a pas réduit les exacerbations et a augmenté celles nécessitant une hospitalisation. |
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | ECR | N Engl J Med | Bêtabloquants après infarctus du myocarde avec fraction d'éjection préservée (indication cardiovasculaire, non pulmonaire). |
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | Cohorte | Am J Cardiol | Métoprolol versus carvédilol chez des patients âgés atteints d'insuffisance cardiaque, de BPCO, de diabète et d'insuffisance rénale. |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Cohorte | Medicine | Carvédilol, bisoprolol et métoprolol dans l'association insuffisance cardiaque et BPCO (base de données taïwanaise). |
| [29159953](https://pubmed.ncbi.nlm.nih.gov/29159953/) | 2018 | Cohorte | Eur J Heart Fail | Cohorte danoise : bêtabloquants, insuffisance cardiaque et BPCO. |
| [20413026](https://pubmed.ncbi.nlm.nih.gov/20413026/) | 2010 | Essai croisé randomisé | J Am Coll Cardiol | Différences entre bêtabloquants sélectifs et non sélectifs dans l'insuffisance cardiaque chronique avec BPCO. |
| [33784233](https://pubmed.ncbi.nlm.nih.gov/33784233/) | 2021 | Analyse secondaire d'ECR | Ann Am Thorac Soc | Indice chronotrope et exacerbations de BPCO dans BLOCK-COPD. |
| [14520486](https://pubmed.ncbi.nlm.nih.gov/14520486/) | 2003 | Étude clinique | Heart Vessels | Le métoprolol peut être utilisé en sécurité chez des patients coronariens atteints de BPCO. |
| [6851273](https://pubmed.ncbi.nlm.nih.gov/6851273/) | 1983 | Étude physiologique | Clin Cardiol | Effet du métoprolol sur la fonction cardiaque et pulmonaire dans la BPCO (6 patients). |
| [32250198](https://pubmed.ncbi.nlm.nih.gov/32250198/) | 2020 | Revue | Expert Rev Respir Med | Recommandations pratiques sur l'usage des bêtabloquants dans la BPCO. |

Pour les infarctus du myocarde septal et postéro-latéral, la littérature se limite à des études hémodynamiques anciennes (par ex. [6401230](https://pubmed.ncbi.nlm.nih.gov/6401230/), [6442004](https://pubmed.ncbi.nlm.nih.gov/6442004/)) et à un essai comparant métoprolol et xamotérol ([8737105](https://pubmed.ncbi.nlm.nih.gov/8737105/)). Pour l'hypertension pulmonaire due à une maladie pulmonaire ou à l'hypoxie, les publications retrouvées sont en grande partie hors sujet (études animales, rapports de cas).

---

## Informations de Marché en France

Les 14 AMM recensées sont annulées. Les textes d'indication approuvée ne sont pas disponibles. Principales AMM :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65340488 | SELOZOK LP 95 mg | Comprimé pelliculé à libération prolongée | Non renseignée |
| 68428420 | SELOZOK LP 190 mg | Comprimé pelliculé à libération prolongée | Non renseignée |
| 68679426 | SELOKEN L P 200 mg | Comprimé à libération prolongée | Non renseignée |
| 67211976 | LOPRESSOR 100 mg | Comprimé pelliculé sécable | Non renseignée |
| 64930518 | METOPROLOL SANDOZ 50 mg | Comprimé | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : phéochromocytome, myasthénie grave, diabète et acidocétose diabétique, maladie hépatique et encéphalopathie hépatique, hypotension, pancréatite, goutte, psoriasis, lupus érythémateux systémique, anurie, troubles anxieux et dysthymiques, entre autres.
- **Interactions médicamenteuses** : 338 interactions recensées. Parmi les exemples : interactions de niveau modéré avec l'épinéphrine, l'hydrocortisone, la dexaméthasone, le bupropion, la morphine, la cimétidine, la canagliflozine et la dapagliflozine ; niveau mineur avec l'acide acétylsalicylique et l'oxyde de magnésium.
- **Points d'attention spécifiques aux indications prédites** : dans l'essai BLOCK-COPD, le métoprolol a été associé à une augmentation des exacerbations de BPCO nécessitant une hospitalisation ; dans l'hypertension pulmonaire, le risque pour la fonction ventriculaire droite impose la prudence.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Neuf des dix prédictions sont au niveau L4-L5 : elles sont soit des extensions d'indications cardiovasculaires déjà connues, soit sans aucune base mécanistique ou clinique. Seule la cardiopathie pulmonaire chronique atteint le niveau L3, avec des preuves indirectes et mitigées (absence de bénéfice et signal de risque dans la BPCO), qui relèvent d'une question de recherche sur la sécurité plutôt que d'une recommandation. Toutes les AMM françaises étant annulées, aucune voie réglementaire immédiate n'existe.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice officielle de l'ANSM (mises en garde et contre-indications), lacune bloquante pour le dépistage de sécurité.
- Compléter les données sur le mécanisme d'action (via DrugBank).
- Clarifier le statut réglementaire actuel du métoprolol en France (AMM annulées).
- Pour la cardiopathie pulmonaire chronique : attendre ou examiner les résultats de l'essai NCT06825728 et mener une évaluation de sécurité spécifique chez les patients atteints de BPCO avec maladie cardiaque.
- Pour les prédictions de rang 1 et 2 : rechercher des données cliniques spécifiques, en distinguant clairement ce qui relève d'une simple extension de l'indication hypertension.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

