---
layout: default
title: Amlodipine
parent: Prédiction du modèle uniquement (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

# Amlodipine : De l'Hypertension et des Accidents Vasculaires Cérébraux à l'Hémorragie Intracérébrale

## Résumé en Une Phrase

Amlodipine est un inhibiteur calcique, initialement utilisé pour le traitement de l'hypertension artérielle, des maladies cérébrovasculaires (accident vasculaire cérébral, infarctus cérébral) et de l'angor de Prinzmetal.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Hémorragie intracérébrale** (indication retenue pour l'évaluation, car c'est celle qui dispose du plus grand nombre de preuves parmi les 10 prédictions), avec **4 essais cliniques** et **9 publications** actuellement associés, mais uniquement dans le cadre d'une association fixe de trois antihypertenseurs.

> Remarque : la première prédiction du modèle, l'infarctus du tronc cérébral (score 99,94 %), ne dispose d'aucun essai ni d'aucune publication. L'hémorragie intracérébrale (rang 10) est présentée ici car elle est la seule à disposer d'un essai de phase 3 achevé.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (les textes d'indication des AMM ne sont pas renseignés ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Hémorragie intracérébrale |
| Score de Prédiction TxGNN | 99,79 % |
| Niveau de Preuve | L1 (essai de phase 3 achevé, mais portant sur une association et non sur l'amlodipine seule : à interpréter avec prudence) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 6 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'amlodipine est un inhibiteur des canaux calciques de type L, qui provoque une relaxation du muscle lisse vasculaire et une baisse de la pression artérielle.

Le contrôle de la pression artérielle est le principal facteur de risque modifiable de récidive après une hémorragie intracérébrale. L'amlodipine fait partie de la « Triple Pill » de l'essai TRIDENT, une association fixe à faibles doses (avec telmisartan et indapamide). La prédiction s'appuie donc sur le mécanisme antihypertenseur déjà connu, et non sur un mécanisme nouveau.

Une limite importante : les preuves soutiennent la stratégie d'association, pas l'amlodipine seule. Son effet propre ne peut pas être isolé de celui de ses partenaires.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Terminé | 1671 | Triple pilule antihypertensive à faibles doses (incluant l'amlodipine) en plus des soins habituels, pour réduire la récidive d'AVC après hémorragie intracérébrale ; essai en double aveugle contre placebo |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | Non applicable | En recrutement | 140 | Triple traitement antihypertenseur après hémorragie intracérébrale avec le score TRICH ; résultats non disponibles |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | Non applicable | Arrêté | 4 | Sous-étude IRM de TRIDENT ; inscription trop faible pour être exploitable |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Arrêté | 1 | Sous-étude cognitive de TRIDENT ; un seul participant, non informative |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | ECR (résultats publiés) | N Engl J Med | Évaluation d'une pilule unique associant trois antihypertenseurs à faibles doses après hémorragie intracérébrale, pour réduire la pression artérielle et le risque de récidive d'AVC |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Protocole d'essai | Int J Stroke | Justification, conception et avancement de l'essai TRIDENT |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Rapport de cas | Ann Pharmacother | Angioedème probablement lié à l'amlodipine chez un patient ayant une hémorragie thalamique |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Revue | Cardiovasc Drugs Ther | Usage et efficacité comparée des antagonistes calciques dans l'hypertension (contexte général) |

Les autres références récupérées concernent d'autres médicaments (tizanidine, aténolol, bénidipine, candésartan) ou sont indirectes, et ne sont pas retenues.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63566442 | AMLODIPINE ZYDUS 5 mg | Gélule | Non renseignée (AMM annulée) |
| 62204255 | AMLODIPINE VIATRIS GENERIQUES 5 mg | Gélule | Non renseignée (AMM annulée) |
| 63811710 | AMLODIPINE EG 5 mg | Gélule | Non renseignée (AMM annulée) |
| 68500357 | AMLODIPINE ZYDUS 10 mg | Gélule | Non renseignée (AMM annulée) |
| 63436445 | AMLODIPINE VIATRIS GENERIQUES 10 mg | Gélule | Non renseignée (AMM annulée) |

Une sixième AMM, NATRIXAM 1,5 mg/5 mg (comprimé à libération modifiée, DIFARMED), est également annulée. Aucune AMM valide n'a été identifiée dans les données compilées.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, maladie rénale, pancréatite, hypothyroïdie, angioedème (dont héréditaire et induit par les bloqueurs du système rénine-angiotensine), lupus érythémateux systémique, myopathie, diabète et acidocétose diabétique, neutropénie et agranulocytose, hypotension, hyperparathyroïdie.
- **Interactions médicamenteuses** : 100 interactions recensées, au moins 20 de niveau modéré, notamment avec l'hydrocortisone, la bétaméthasone, la budésonide, la dexaméthasone, l'aprépitant, l'acide acétylsalicylique, le bupropion, la clarithromycine, le clotrimazole, la canagliflozine, la dapagliflozine et plusieurs sels de calcium.
- **Signaux issus de la littérature** : un cas d'angioedème (PMID 19299323) et un risque d'hypotension, à surveiller chez les patients après hémorragie cérébrale.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, non disponibles dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le seul essai de phase 3 achevé (n=1671) porte sur une association fixe de trois médicaments, et l'effet de l'amlodipine seule ne peut pas être isolé ; de plus, l'indication reste dans le rôle antihypertenseur existant. Il n'existe aucune AMM valide en France et les données de sécurité officielles sont absentes.
- Les neuf autres prédictions sont soit sans preuve (L5), soit soutenues par des données précliniques ou des cas isolés (L3-L4). L'occlusion de l'artère cérébrale (rang 6) n'est étayée que par des études animales.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications) et les données de mécanisme d'action depuis DrugBank
- Analyser les résultats détaillés de l'essai TRIDENT (publication NEJM 2026) pour estimer la contribution de chaque composant
- Clarifier la situation réglementaire (AMM annulées) et la disponibilité d'une formulation commercialisée
- Définir un plan de surveillance de la sécurité (hypotension, angioedème, interactions) chez les patients après hémorragie intracérébrale
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

