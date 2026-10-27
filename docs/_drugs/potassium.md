---
layout: default
title: Potassium
parent: Prédiction du modèle uniquement (L5)
nav_order: 618
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Potassium : nouvelle indication prédite, Trouble hypertensif (hypertension artérielle) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "POTASSIUM"
predicted_indications: ["hypertensive disorder", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "malignant renovascular hypertension"]
---

# Potassium
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

## Potassium : D'un usage électrolytique sans indication renseignée à l'Hypertension artérielle
{: .text-alpha }

## Résumé en Une Phrase

Le potassium est un électrolyte essentiel utilisé en France sous de nombreuses formes (solutés de perfusion, sirops, comprimés), mais les données compilées pour ce rapport ne mentionnent aucune indication d'origine renseignée.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension artérielle (trouble hypertensif)**,
avec **23 essais cliniques** (dont seulement 2 testent directement le potassium comme agent actif en Phase 3) et **20 publications** associés, dont plusieurs méta-analyses d'essais randomisés.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Trouble hypertensif (hypertension artérielle) |
| Score de Prédiction TxGNN | 99,16 % |
| Niveau de Preuve | L1 (selon l'évaluation fournie ; voir réserve ci-dessous) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 19 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

> **Réserve sur le niveau de preuve :** le niveau L1 repose sur la présence d'essais de Phase 3 et de méta-analyses. Or, la plupart des essais de Phase 3 recensés concernent le losartan potassique, dans lequel le potassium n'est qu'un contre-ion. Seuls deux essais de Phase 3 (NCT00000509 et NCT03809884) testent réellement le potassium. L'un n'a pas d'effectif communiqué et l'autre ne comprend que 7 participants. Le niveau de preuve réel est donc plus proche de L3 (méta-analyses et revues) que d'un L1 strict.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances physiologiques établies, le potassium est le principal cation intracellulaire. Il est indispensable au potentiel de membrane des cellules et à la fonction cardiaque, musculaire et rénale.

Un apport accru en potassium favorise l'élimination urinaire de sodium (natriurèse). Il induit une vasodilatation par hyperpolarisation endothéliale, via les canaux potassiques et la stimulation de la pompe Na⁺/K⁺-ATPase. Il réduit aussi le tonus sympathique et la sensibilité au sel. Ces mécanismes expliquent un effet hypotenseur. Des méta-analyses d'essais randomisés (dose-réponse, patients hypertendus) vont dans ce sens.

Aucune indication d'origine n'étant renseignée, la relation avec une indication initiale ne peut pas être établie. La prédiction repose donc sur la physiologie et sur la littérature, non sur une proximité thérapeutique avec un usage antérieur. Il faudrait aussi préciser quelle forme de potassium (sel, complément alimentaire, aliments riches en potassium, sel enrichi en potassium) serait visée.

## Preuves d'Essais Cliniques

Parmi les essais recensés, seuls ceux dont l'intervention est le potassium lui-même sont directement pertinents. Les autres portent sur des sels potassiques d'antihypertenseurs (losartan potassique, par exemple) et ne sont pas listés comme preuves.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03809884](https://clinicaltrials.gov/study/NCT03809884) | Phase 3 | Terminé | 7 | Alimentation versus supplément pour augmenter l'apport en potassium ; effectif très faible |
| [NCT00000509](https://clinicaltrials.gov/study/NCT00000509) | Phase 3 | Terminé | Non communiqué | Réduction du sodium avec ou sans supplémentation en potassium chez des hommes hypertendus |
| [NCT02959931](https://clinicaltrials.gov/study/NCT02959931) | Non applicable | Terminé | 33 | Effets postprandiaux d'un repas riche en potassium sur la santé vasculaire de patients hypertendus |
| [NCT00949585](https://clinicaltrials.gov/study/NCT00949585) | Non applicable | Terminé | 29 | Deux niveaux d'apport en potassium dans l'insuffisance rénale chronique (bénéfices et sécurité) |
| [NCT02697708](https://clinicaltrials.gov/study/NCT02697708) | Phase 1/2 | Statut inconnu | 40 | Sources alimentaires de potassium (pommes de terre) : rétention, équilibre acido-basique, pression artérielle |
| [NCT00000501](https://clinicaltrials.gov/study/NCT00000501) | Phase 2 | Terminé | Non communiqué | Faisabilité de la prévention de l'hypertension (réduction du sodium avec ou sans apport accru en potassium) |
| [NCT01074918](https://clinicaltrials.gov/study/NCT01074918) | Phase 1/2 | Retiré | 0 | Citrate de potassium-magnésium versus chlorure de potassium ; aucun patient inclus |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [32500831](https://pubmed.ncbi.nlm.nih.gov/32500831/) | 2020 | Méta-analyse d'ECR | J Am Heart Assoc | Relation dose-réponse entre supplémentation en potassium et pression artérielle |
| [28024910](https://pubmed.ncbi.nlm.nih.gov/28024910/) | 2017 | Revue systématique et méta-analyse | Int J Cardiol | Effet de la supplémentation en potassium sur la pression artérielle des hypertendus |
| [23558164](https://pubmed.ncbi.nlm.nih.gov/23558164/) | 2013 | Revue systématique et méta-analyse | BMJ | Effet d'un apport accru en potassium sur les facteurs de risque et les maladies cardiovasculaires |
| [37772757](https://pubmed.ncbi.nlm.nih.gov/37772757/) | 2024 | Revue | Am J Hypertens | État des connaissances sur potassium et hypertension |
| [35045721](https://pubmed.ncbi.nlm.nih.gov/35045721/) | 2022 | Étude clinique | Hypertension | Natriurèse induite par le potassium chez des femmes ménopausées hypertendues, comparée à l'hydrochlorothiazide |
| [41263071](https://pubmed.ncbi.nlm.nih.gov/41263071/) | 2026 | Analyse d'essai | Hypertension | Cohérence de la réponse tensionnelle au sel enrichi en potassium (China Salt Substitute Study) |
| [26634368](https://pubmed.ncbi.nlm.nih.gov/26634368/) | 2016 | Revue | J Physiol Biochem | Rôle du potassium alimentaire dans l'hypertension et le diabète |
| [25398734](https://pubmed.ncbi.nlm.nih.gov/25398734/) | 2014 | Revue | Adv Nutr | Rapport sodium/potassium, pression artérielle et hypertension |
| [27455317](https://pubmed.ncbi.nlm.nih.gov/27455317/) | 2016 | Revue | Nutrients | Apport, biodisponibilité du potassium, hypertension et contrôle glycémique |
| [10979053](https://pubmed.ncbi.nlm.nih.gov/10979053/) | 2000 | Recommandations/revue | Arch Intern Med | Recommandations sur le remplacement du potassium en pratique clinique |

## Informations de Marché en France

Les 19 AMM recensées sont annulées. Aucune n'a de texte d'indication renseigné. Les cinq premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63010506 | NATI-K 500 mg | Comprimé gastro-résistant | Non renseignée (AMM annulée) |
| 61334096 | Chlorure de potassium Lavoisier 20 % | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 63382862 | Kaleorid LP 1000 mg | Comprimé pelliculé à libération prolongée | Non renseignée (AMM annulée) |
| 68081197 | Chlorure de potassium Lavoisier 7,46 % | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 68050732 | Potassium H2 Pharma 25 mg/mL | Sirop | Non renseignée (AMM annulée) |

## Considérations de Sécurité

Aucune donnée de sécurité issue de la notice n'est disponible (mises en garde, contre-indications), et aucune interaction médicamenteuse n'a été retrouvée dans les données compilées. Veuillez consulter la notice pour les informations de sécurité.

Les éléments suivants, issus de l'analyse des preuves, appellent une vigilance particulière :
- **Insuffisance rénale** : risque d'hyperkaliémie lors d'une supplémentation.
- **Associations avec des inhibiteurs du SRAA** (IEC, ARA II) ou des diurétiques épargneurs de potassium : risque accru d'hyperkaliémie.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Des méta-analyses d'essais randomisés soutiennent un effet hypotenseur d'un apport accru en potassium, avec un mécanisme physiologique plausible. En revanche, les essais directement centrés sur le potassium sont rares et de petite taille, et la plupart des essais d'hypertension recensés concernent des sels potassiques d'autres médicaments. Toutes les AMM françaises sont annulées.
- Les autres indications prédites (hypertension pulmonaire, maladie rénale hypertensive maligne, hypertension rénovasculaire maligne) ne reposent que sur le score du modèle ou sur une littérature indirecte. Elles relèvent d'un statut **Hold**. La prudence est particulièrement de mise en cas d'atteinte rénale sévère, du fait du risque d'hyperkaliémie.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications dans les notices de l'ANSM (donnée bloquante pour le criblage de sécurité).
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank.
- Définir la forme de potassium visée (médicament, supplément, sel enrichi), la dose et la voie d'administration.
- Confirmer l'efficacité par des essais contrôlés de plus grande taille centrés sur le potassium.
- Établir un plan de surveillance de la kaliémie et de la fonction rénale, avec exclusion ou encadrement des patients sous inhibiteurs du SRAA ou diurétiques épargneurs de potassium.
- Clarifier la situation réglementaire, puisque toutes les AMM sont annulées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

