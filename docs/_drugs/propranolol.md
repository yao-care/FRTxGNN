---
layout: default
title: Propranolol
parent: 僅模型預測 (L5)
nav_order: 249
evidence_level: L5
indication_count: 6
---

# Propranolol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Propranolol : D'un Bêta-Bloquant Cardiovasculaire vers la Myopathie Distale de Type Tateyama (Candidat Principal Parmi Six Pistes)

## Résumé en Une Phrase

Propranolol est un bêta-bloquant non sélectif dont l'usage cardiovasculaire est bien établi dans la pratique clinique, mais dont l'indication d'origine précise et le mécanisme d'action détaillé ne sont pas documentés dans cet Evidence Pack (marché France : non commercialisé, 0 AMM).
Le modèle TxGNN a produit **6 prédictions de repositionnement** pour ce médicament ; la mieux notée est la **Myopathie Distale de Type Tateyama** (score 99.40 %), mais **aucun essai clinique ni publication ne la soutient**, et le raisonnement mécanistique suggère un possible artefact du graphe de connaissances plutôt qu'un lien pharmacologique réel.
En revanche, trois candidats de rang inférieur — **cardiomyopathie hypertrophique liée à l'entraînement sportif intensif**, **cardiomyopathie cirrhotique** et **cardiomyopathie** (générale) — bénéficient d'un ancrage mécanistique et/ou de preuves réelles (jusqu'à **3 essais cliniques** et **20 publications** pour la cardiomyopathie générale), ce qui en fait des pistes bien plus solides que le candidat en tête de score.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée dans l'Evidence Pack (usage cardiovasculaire établi de longue date — hypertension, arythmies, angor, etc., selon les connaissances pharmacologiques générales) |
| Nouvelle Indication Prédite (rang 1) | Distal Myopathy, Tateyama Type |
| Score de Prédiction TxGNN (rang 1) | 99.40 % |
| Niveau de Preuve (rang 1) | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée (rang 1) | Hold |

### Comparatif des 6 Indications Prédites

| Rang | Indication Prédite | Score TxGNN | Niveau de Preuve | Étape de Décision | Recommandation |
|---|---|---|---|---|---|
| 1 | Distal myopathy, Tateyama type | 99.40 % | L5 | S0 | Hold |
| 2 | Congenital myopathy with excess of thin filaments | 99.30 % | L5 | S0 | Hold |
| 3 | Cardiomyopathie hypertrophique liée à l'entraînement sportif intensif | 99.17 % | L4 | S1 | Proceed with Guardrails (Research Question) |
| 4 | Chondroma | 99.14 % | L5 | S0 | Hold |
| 5 | Cardiomyopathie cirrhotique | 99.12 % | L3 | S2 | Proceed with Guardrails (Research Question) |
| 6 | Cardiomyopathie (générale) | 99.12 % | L3 | S2 | Proceed with Guardrails (Research Question) |

---

## Pourquoi Ces Prédictions sont-elles Raisonnables ?

Actuellement, les données détaillées sur le mécanisme d'action (MOA) de Propranolol ne sont pas disponibles dans cet Evidence Pack (écart de données DG002, sévérité *High*), et aucune indication d'origine n'a pu être extraite des données réglementaires françaises puisque le médicament n'y est pas commercialisé. Sur la base des connaissances pharmacologiques générales, Propranolol appartient à la classe des bêta-bloquants non sélectifs, dont l'action repose sur le blocage des récepteurs β-adrénergiques et dont les usages cardiovasculaires (hypertension, arythmies, angor, cardiomyopathie hypertrophique obstructive) sont bien établis. C'est ce profil pharmacologique qui explique la présence de plusieurs candidats dans la famille des cardiomyopathies parmi les prédictions TxGNN.

### Rang 1 — Distal myopathy, Tateyama type (Hold)
La myopathie distale de type Tateyama (myotilinopathie) est une maladie structurelle du muscle squelettique liée au gène *MYOT*, sans lien mécanistique connu avec le blocage β-adrénergique de propranolol. Le score élevé du modèle pourrait refléter une similarité topologique entre nœuds « myopathie » dans le graphe de connaissances plutôt qu'une véritable connexion pharmacologique.

### Rang 2 — Congenital myopathy with excess of thin filaments (Hold)
Maladie structurelle/génétique caractérisée par une accumulation excessive de protéines des filaments fins (actine, nébuline). Aucune voie moléculaire intermédiaire ne relie ce mécanisme à l'action cardiovasculaire/sympathique de propranolol.

### Rang 3 — Cardiomyopathie hypertrophique liée à l'entraînement sportif intensif (Proceed with Guardrails)
Propranolol est un traitement historique de référence de la cardiomyopathie hypertrophique obstructive (CMHO) classique : son effet inotrope et chronotrope négatif réduit le gradient de pression dans la chambre de chasse et atténue l'hyperactivation sympathique liée à l'effort. Le sous-type « lié à l'entraînement sportif intensif » partage ce mécanisme, mais constitue une entité étiologique distincte, à différencier du remodelage cardiaque physiologique de l'athlète (« cœur d'athlète »), pour laquelle un traitement pourrait être inapproprié. Aucune étude prospective dédiée à ce sous-type précis n'existe.

### Rang 4 — Chondroma (Hold)
Tumeur bénigne du cartilage, mécanisme de prolifération chondrocytaire sans rapport connu avec l'action antiangiogénique de propranolol observée dans l'hémangiome infantile. Cette prédiction est probablement un faux positif lié à une proximité d'embedding entre « tumeurs bénignes » et « angiomes » dans le graphe de connaissances.

### Rang 5 — Cardiomyopathie cirrhotique (Proceed with Guardrails)
La cardiomyopathie cirrhotique se caractérise par une dysautonomie cardiaque, un allongement du QTc et une réponse émoussée aux catécholamines. Propranolol est déjà largement utilisé chez les patients cirrhotiques en prévention de l'hémorragie variqueuse ; certaines publications suggèrent un effet correcteur sur le QTc, mais d'autres montrent qu'un bêta-bloquant non sélectif peut aggraver l'hémodynamique globale et la fonction rénale, en particulier au stade décompensé. Le bénéfice/risque dépend donc fortement de la sévérité de la maladie hépatique.

### Rang 6 — Cardiomyopathie (générale) (Proceed with Guardrails)
Catégorie hétérogène. Pour la cardiomyopathie hypertrophique obstructive, l'usage de propranolol est ancien et documenté par plusieurs études de physiologie/hémodynamique. Pour la cardiomyopathie dilatée, les données sont mixtes : certains patients montrent un bénéfice hémodynamique, mais des cas de surdosage ont provoqué une cardiomyopathie dilatée aiguë et une toxicité du système nerveux central. Une stratification par sous-type est nécessaire avant toute recommandation globale.

---

## Preuves d'Essais Cliniques

### Rang 1 — Distal myopathy, Tateyama type
Aucun essai clinique associé enregistré actuellement.

### Rang 2 — Congenital myopathy with excess of thin filaments
Aucun essai clinique associé enregistré actuellement.

### Rang 3 — Cardiomyopathie hypertrophique liée à l'entraînement sportif intensif
Aucun essai clinique associé enregistré actuellement.

### Rang 4 — Chondroma
Aucun essai clinique associé enregistré actuellement.

### Rang 5 — Cardiomyopathie cirrhotique
Aucun essai clinique associé enregistré actuellement.

### Rang 6 — Cardiomyopathie (générale)

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04767061](https://clinicaltrials.gov/study/NCT04767061) | Phase 4 | Terminé | 9 | Essais N-of-1 sur l'arrêt (déprescription) des bêta-bloquants chez des patients âgés atteints d'insuffisance cardiaque à FEVG préservée (HFpEF) — n'évalue pas l'efficacité de propranolol mais son retrait ; pertinence indirecte seulement (grade C) |
| [NCT05427474](https://clinicaltrials.gov/study/NCT05427474) | Phase 3 | Statut inconnu | 90 | Propranolol + gabapentine dans l'hyperactivité sympathique paroxystique après traumatisme crânien ; lien avec la cardiomyopathie uniquement via l'atteinte myocardique secondaire aux catécholamines (grade C) |
| [NCT05019027](https://clinicaltrials.gov/study/NCT05019027) | Phase 4 | Recrutement sur invitation | 20 | Essais N-of-1 évaluant l'arrêt du bêta-bloquant chez des patients atteints d'amylose cardiaque à transthyrétine ; suggère une mauvaise tolérance de ce sous-groupe à propranolol plutôt qu'un bénéfice (grade B, signal négatif) |

---

## Preuves de la Littérature

### Rang 1 — Distal myopathy, Tateyama type
Aucune littérature associée disponible actuellement.

### Rang 2 — Congenital myopathy with excess of thin filaments
Aucune littérature associée disponible actuellement.

### Rang 3 — Cardiomyopathie hypertrophique liée à l'entraînement sportif intensif
Aucune littérature associée disponible actuellement.

### Rang 4 — Chondroma
Aucune littérature associée disponible actuellement.

### Rang 5 — Cardiomyopathie cirrhotique

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [25250684](https://pubmed.ncbi.nlm.nih.gov/25250684/) | 2015 | Cohorte | J Pediatr Gastroenterol Nutr | Incidence et facteurs de risque de cardiomyopathie cirrhotique chez l'enfant atteint d'hypertension portale |
| [32446716](https://pubmed.ncbi.nlm.nih.gov/32446716/) | 2020 | Cohorte | J Hepatol | Les bêta-bloquants non sélectifs altèrent l'homéostasie circulatoire globale et la fonction rénale chez les cirrhotiques avec ascite réfractaire |
| [38738176](https://pubmed.ncbi.nlm.nih.gov/38738176/) | 2024 | Cohorte | Front Pharmacol | Propranolol peut corriger l'allongement du QT chez les patients cirrhotiques |
| [35763518](https://pubmed.ncbi.nlm.nih.gov/35763518/) | 2022 | Cohorte | PLoS One | Effets cardiovasculaires atténués des bêta-bloquants chez les cirrhotiques, en lien avec la sévérité de la maladie |
| [15387011](https://pubmed.ncbi.nlm.nih.gov/15387011/) | 2004 | Cohorte | Ugeskr Laeger | Cardiomyopathie cirrhotique : allongement du QTc et dyssynchronie électromécanique |

### Rang 6 — Cardiomyopathie (générale)

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [7200796](https://pubmed.ncbi.nlm.nih.gov/7200796/) | 1982 | ECR | Br Heart J | Effets hémodynamiques de nifédipine et propranolol chez 12 patients atteints de cardiomyopathie hypertrophique obstructive ; association supérieure à nifédipine seule |
| [8989641](https://pubmed.ncbi.nlm.nih.gov/8989641/) | 1996 | Cohorte | J Card Fail | Prédicteurs hémodynamiques d'intolérance précoce à propranolol dans la cardiomyopathie dilatée |
| [4586631](https://pubmed.ncbi.nlm.nih.gov/4586631/) | 1973 | Non classé (probable étude comparative) | Br Heart J | Essai en double aveugle de propranolol vs practolol dans la cardiomyopathie hypertrophique |
| [3189143](https://pubmed.ncbi.nlm.nih.gov/3189143/) | 1988 | Non classé (probable étude comparative) | Am Heart J | Effets hémodynamiques aigus du pindolol et de propranolol dans la cardiomyopathie dilatée |
| [6686544](https://pubmed.ncbi.nlm.nih.gov/6686544/) | 1983 | Non classé | Eur Heart J | Effets de propranolol et vérapamil sur la rigidité diastolique dans la cardiomyopathie hypertrophique |
| [7192151](https://pubmed.ncbi.nlm.nih.gov/7192151/) | 1980 | Non classé | Br Heart J | Effets de propranolol sur la consommation myocardique d'oxygène et l'hémodynamique dans la CMHO |
| [1611637](https://pubmed.ncbi.nlm.nih.gov/1611637/) | 1992 | Non classé | Cardiology | Effet de propranolol et disopyramide sur la fonction ventriculaire gauche au repos et à l'effort dans la CMH |
| [2920304](https://pubmed.ncbi.nlm.nih.gov/2920304/) | 1989 | Non classé | Can J Cardiol | Association disopyramide et propranolol dans la cardiomyopathie hypertrophique |
| [3433863](https://pubmed.ncbi.nlm.nih.gov/3433863/) | 1987 | Non classé | Z Kardiol | Traitement combiné nifédipine-propranolol dans la cardiomyopathie hypertrophique |
| [10460081](https://pubmed.ncbi.nlm.nih.gov/10460081/) | 1999 | Rapport de cas | Pediatr Emerg Care | Cardiomyopathie dilatée aiguë et toxicité du SNC après intoxication au propranolol (signal de sécurité) |

*10 publications les plus pertinentes affichées sur 20 disponibles pour ce candidat.*

---

## Informations de Marché en France

Propranolol n'est actuellement **pas commercialisé en France** selon les données réglementaires disponibles (0 AMM enregistrée, statut « 未上市 »/non commercialisé). Aucune information de spécialité (numéro d'AMM, nom de produit, forme pharmaceutique) n'est donc disponible.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

À noter : les mises en garde, contre-indications et interactions médicamenteuses de Propranolol ne sont pas encore renseignées dans cet Evidence Pack. Il s'agit d'un écart de données classé **sévérité Blocking** (DG001 —仿單警語/禁忌 TFDA), qui empêche actuellement toute évaluation de sécurité initiale (étape S1) pour l'ensemble des candidats, y compris ceux disposant d'un signal d'efficacité (rangs 3, 5, 6).

---

## Conclusion et Prochaines Étapes

**Décision Globale : Hold** (en attente de la levée de l'écart de données de sécurité DG001)

**Par candidat :**
- **Rangs 1, 2, 4** (myopathie de Tateyama, myopathie congénitale à filaments fins, chondrome) : **Hold** — absence totale de preuve clinique/littérature et lien mécanistique non plausible ; probables artefacts du modèle.
- **Rangs 3, 5, 6** (cardiomyopathie hypertrophique liée au sport, cardiomyopathie cirrhotique, cardiomyopathie générale) : **Proceed with Guardrails** — mécanisme pharmacologique plausible et, pour les rangs 5 et 6, appuyé par des données cliniques réelles (essais et/ou publications), mais nécessitant une stratification par sous-type et la résolution de l'écart de sécurité avant toute avancée.

**Justification :**
Le score TxGNN le plus élevé (rang 1) n'est soutenu par aucune preuve réelle et repose sur un lien mécanistique jugé peu plausible, tandis que des candidats de rang inférieur dans la famille des cardiomyopathies bénéficient d'un ancrage physiopathologique solide et, pour deux d'entre eux, de données cliniques concrètes. Toutefois, l'absence de données de sécurité TFDA (écart Blocking) empêche toute progression vers une évaluation de sécurité initiale, quel que soit le niveau de preuve d'efficacité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir le texte complet des mises en garde/contre-indications TFDA (résolution de DG001, priorité bloquante)
- Compléter les données de mécanisme d'action (MOA) via DrugBank (DG002)
- Confirmer l'indication d'origine et l'historique réglementaire de Propranolol (actuellement non extrait de l'Evidence Pack)
- Pour le rang 3 : lancer une étude ciblée distinguant la cardiomyopathie hypertrophique liée au sport du remodelage physiologique de l'athlète
- Pour le rang 5 : stratifier le bénéfice/risque de propranolol selon la sévérité de la cirrhose (ascite réfractaire vs compensée)
- Pour le rang 6 : analyser séparément les sous-types de cardiomyopathie (hypertrophique vs dilatée) avant toute recommandation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

