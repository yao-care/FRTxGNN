---
layout: default
title: Indacaterol
parent: Prédiction du modèle uniquement (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Indacaterol : nouvelle indication prédite, Maladie bronchique (bronchial disease) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données compilées"
monitor_inn: "indacaterol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "trigeminal autonomic cephalalgia", "paratenonitis", "calcific tendinitis", "hypertrichosis (disease)", "bronchial disease", "myositis", "anaphylaxis", "Ambras type hypertrichosis universalis congenita"]
---

# Indacaterol
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

# Indacaterol : Des Maladies Respiratoires Obstructives à la Maladie Bronchique

## Résumé en Une Phrase

L'indacaterol est un bêta-2-agoniste inhalé à action ultra-longue, utilisé dans les maladies respiratoires obstructives (les données d'indication originale ne sont pas renseignées dans les licences françaises compilées).
Le modèle TxGNN le prédit comme potentiellement efficace pour la **maladie bronchique**, avec **22 essais cliniques** et **20 publications** associés. Il s'agit toutefois en pratique du domaine respiratoire natif du médicament, et non d'un véritable repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données compilées |
| Nouvelle Indication Prédite | Maladie bronchique (bronchial disease) |
| Score de Prédiction TxGNN | 99,18 % |
| Niveau de Preuve | L1 (selon les règles du système ; à interpréter avec prudence, voir ci-dessous) |
| Statut de Marché en France | Uniquement annulé |
| Nombre d'AMM | 7 (toutes annulées) |
| Décision Recommandée | Hold |

Remarque : le classement a été fait sur l'indication prédite la mieux étayée (rang 7 dans la liste TxGNN). Les six premières prédictions (syndrome néphrogénique d'antidiurèse inappropriée, céphalées, céphalalgie trigémino-autonomique, paraténonite, tendinite calcifiante, hypertrichose) n'ont aucun essai ni publication (niveau L5) et aucune plausibilité mécanistique ; elles sont considérées comme des artefacts de calcul.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances pharmacologiques établies, l'indacaterol est un bêta-2-agoniste à action ultra-longue : il active les récepteurs bêta-2 adrénergiques, augmente l'AMPc et relâche le muscle lisse bronchique, ce qui permet une bronchodilatation sur 24 heures avec une prise quotidienne.

La maladie bronchique est directement liée à ce mécanisme. Cependant, l'indacaterol appartient déjà à ce domaine thérapeutique (asthme, BPCO) : la prédiction reflète donc très probablement une annotation incomplète des indications d'origine (le champ « indication originale » est vide) plutôt qu'une nouvelle piste thérapeutique. Il convient de réconcilier le statut réglementaire et l'historique de l'étiquetage avant toute recommandation.

---

## Preuves d'Essais Cliniques

Parmi les 22 essais recensés, les plus pertinents sont listés ci-dessous (10 maximum).

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01079130](https://clinicaltrials.gov/study/NCT01079130) | Phase 3 | Terminé | 511 | Efficacité bronchodilatatrice sur 14 jours de différentes doses d'indacaterol vs placebo et salmétérol dans l'asthme persistant |
| [NCT02554786](https://clinicaltrials.gov/study/NCT02554786) | Phase 3 | Terminé | 2216 | QMF149 (indacaterol/mométasone) vs mométasone seule sur 52 semaines dans l'asthme mal contrôlé |
| [NCT00529529](https://clinicaltrials.gov/study/NCT00529529) | Phase 3 | Terminé | 805 | Sécurité sur 26 semaines de l'indacaterol (300 et 600 µg) vs salmétérol dans l'asthme persistant modéré à sévère |
| [NCT04259164](https://clinicaltrials.gov/study/NCT04259164) | Phase 3 | Terminé | 28 | Effet anti-inflammatoire de l'ajout du glycopyrronium à indacaterol/mométasone sur la réponse asthmatique tardive induite par allergène |
| [NCT00403637](https://clinicaltrials.gov/study/NCT00403637) | Phase 2/3 | Terminé | 45 | Doses uniques d'indacaterol (150, 300, 600 µg) vs formotérol et placebo dans l'asthme persistant |
| [NCT00545272](https://clinicaltrials.gov/study/NCT00545272) | Phase 2 | Terminé | 392 | Étude dose-réponse de 14 jours de 4 doses d'indacaterol vs placebo et formotérol |
| [NCT01609478](https://clinicaltrials.gov/study/NCT01609478) | Phase 2 | Terminé | 335 | Efficacité, sécurité et pharmacocinétique de l'indacaterol acétate (75 et 150 µg) sur 12 semaines dans l'asthme persistant |
| [NCT01156844](https://clinicaltrials.gov/study/NCT01156844) | Phase 2 | Terminé | 191 | Efficacité bronchodilatatrice de trois schémas posologiques d'indacaterol dans l'asthme |
| [NCT02892019](https://clinicaltrials.gov/study/NCT02892019) | Phase 2 | Terminé | 79 | Effets de l'indacaterol acétate (75 et 150 µg) sur la fonction pulmonaire chez des enfants asthmatiques de 6 à 11 ans |
| [NCT04206761](https://clinicaltrials.gov/study/NCT04206761) | Phase 3 | Retiré | 0 | IRM au xénon sous trithérapie QVM149 ; étude retirée sans inclusion, donc sans valeur probante |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [32653074](https://pubmed.ncbi.nlm.nih.gov/32653074/) | 2020 | ECR (phase 3, IRIDIUM) | Lancet Respir Med | Trithérapie mométasone-indacaterol-glycopyrronium en une prise quotidienne vs ICS-LABA dans l'asthme insuffisamment contrôlé |
| [34783265](https://pubmed.ncbi.nlm.nih.gov/34783265/) | 2022 | ECR / revue | Expert Rev Respir Med | Association fixe indacaterol/glycopyrronium/mométasone dans l'asthme modéré à sévère |
| [33871819](https://pubmed.ncbi.nlm.nih.gov/33871819/) | 2021 | Revue | Drugs | Revue d'Enerzair Breezhaler dans l'asthme de l'adulte insuffisamment contrôlé |
| [31425937](https://pubmed.ncbi.nlm.nih.gov/31425937/) | 2019 | Revue | Respir Med | Ultra-LABA dans l'asthme, à utiliser uniquement avec un corticoïde inhalé |
| [23348973](https://pubmed.ncbi.nlm.nih.gov/23348973/) | 2013 | Revue | Am J Respir Crit Care Med | Rôle des bêta-2-agonistes dans les maladies pulmonaires |
| [22611179](https://pubmed.ncbi.nlm.nih.gov/22611179/) | 2012 | Revue | Pharmacol Rev | Pharmacologie et usage thérapeutique des bronchodilatateurs |
| [40887869](https://pubmed.ncbi.nlm.nih.gov/40887869/) | 2025 | Étude pharmacologique | Pharmacol Res Perspect | Comparaison moléculaire des bêta-2-agonistes courts, longs et ultra-longs |
| [19609496](https://pubmed.ncbi.nlm.nih.gov/19609496/) | 2009 | Revue | Adv Ther | Bronchodilatation rapide et soutenue de l'indacaterol dans la BPCO et l'asthme |
| [22499359](https://pubmed.ncbi.nlm.nih.gov/22499359/) | 2012 | Revue | Pharmacotherapy | Indacaterol, nouveau bêta-2-agoniste à action ultra-longue |
| [34329722](https://pubmed.ncbi.nlm.nih.gov/34329722/) | 2021 | Données de pontage de dose | Pulm Pharmacol Ther | Dose de mométasone dans les associations indacaterol/mométasone et indacaterol/glycopyrronium/mométasone |

---

## Informations de Marché en France

Les sept AMM recensées sont toutes annulées ; aucune indication approuvée n'est renseignée dans les données compilées. Les AMM sont listées ci-dessous (5 maximum).

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62036213 | ONBREZ BREEZHALER 300 µg | Poudre pour inhalation en gélule | Non renseignée (annulée) |
| 67084265 | ONBREZ BREEZHALER 150 µg | Poudre pour inhalation en gélule | Non renseignée (annulée) |
| 62553246 | ULTIBRO BREEZHALER 85 µg/43 µg | Poudre pour inhalation en gélule | Non renseignée (annulée) |
| 67100189 | ATECTURA BREEZHALER 125 µg/260 µg | Poudre pour inhalation en gélule | Non renseignée (annulée) |
| 64670426 | ATECTURA BREEZHALER 125 µg/127,5 µg | Poudre pour inhalation en gélule | Non renseignée (annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (pas du texte de la notice)** : hypertension, syndrome du QT long (y compris familial), épilepsie, hyperglycémie, diabète et acidocétose diabétique, carence en potassium, arrêt cardiaque soudain, maladie de la conduction cardiaque, thyrotoxicose/hyperthyroïdie/maladie de Basedow, maladie coronarienne.
- **Interactions médicamenteuses** : 441 interactions recensées. Parmi les principales :
  - Modérées : acarbose, isométheptène, famotidine, épinéphrine, albiglutide, alogliptine, metformine, pioglitazone, canagliflozine, chlorpropamide, clarithromycine, dapagliflozine, saxagliptine.
  - Mineures : hydrocortisone, aprépitant, triamcinolone, dexaméthasone, béclométasone, bétaméthasone, budésonide.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves cliniques pour la maladie bronchique sont abondantes, mais elles relèvent du domaine respiratoire natif de l'indacaterol et non d'un véritable repositionnement. De plus, toutes les AMM françaises sont annulées, et les données d'indication d'origine et de mécanisme sont incomplètes. Les neuf autres prédictions n'ont aucune preuve et aucune plausibilité mécanistique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice (mises en garde et contre-indications) sur le site de l'ANSM, afin de lever le blocage du criblage de sécurité.
- Obtenir les données de mécanisme d'action depuis DrugBank.
- Réconcilier le statut réglementaire (AMM annulées) et l'historique d'étiquetage, et confirmer les indications d'origine.
- Décider si l'évaluation d'une indication déjà couverte (asthme/BPCO) a un intérêt, ou si l'analyse doit être redirigée vers de véritables nouvelles indications.
- Plan de surveillance de sécurité pour les populations à risque cardiovasculaire, métabolique (diabète) et électrolytique (hypokaliémie).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

