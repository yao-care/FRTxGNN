---
layout: default
title: Telmisartan
parent: Prédiction du modèle uniquement (L5)
nav_order: 734
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "TELMISARTAN"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "cerebral artery occlusion", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "intracerebral hemorrhage", "Braddock syndrome"]
description: "Telmisartan : nouvelle indication prédite, Prinzmetal angina (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Telmisartan
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

## Telmisartan: Prinzmetal angina
{: .text-alpha }

## Résumé en Une Phrase

Telmisartan est un antagoniste des récepteurs de l'angiotensine II (sartan), initialement utilisé pour traiter l'hypertension artérielle et réduire le risque d'accident vasculaire cérébral.
Le modèle TxGNN prédit en premier rang la **angine de Prinzmetal** (score le plus élevé), mais sans aucune preuve associée. Parmi les 10 indications prédites, la plus documentée sur le plan préclinique est l'**occlusion des artères cérébrales** (**3 essais cliniques**, **17 publications**, presque toutes précliniques) ; la plus solide sur le plan clinique est l'**hémorragie intracérébrale**, via l'essai de phase 3 TRIDENT (association de trois antihypertenseurs en une pilule).

> **Remarque :** Le classement TxGNN place l'angine de Prinzmetal en tête (0,9998), mais aucun essai ni publication n'a été retrouvé pour elle. Ce rapport présente donc l'ensemble des indications prédites, en détaillant celles qui disposent de preuves. L'occlusion des artères cérébrales a été retenue pour le titre car elle est la mieux documentée sur le plan préclinique, tout en restant une prédiction au niveau de preuve limité.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Prinzmetal angina |
| Score de Prédiction TxGNN | 0.9998 |
| Niveau de Preuve | L5 (preuves essentiellement précliniques, soutien clinique indirect) |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

### Vue d'ensemble des 10 indications prédites

| Rang | Indication prédite | Score TxGNN | Niveau de preuve | Recommandation |
|---|---|---|---|---|
| 1 | Angine de Prinzmetal | 0,9998 | L5 | Hold |
| 2 | Infarctus du tronc cérébral | 0,9998 | L5 | Hold |
| 3 | Amyloïdose ABri | 0,9997 | L5 | Hold |
| 4 | Occlusion des artères cérébrales | 0,9995 | L3 | Question de recherche |
| 5 | Hypertension pulmonaire d'origine multifactorielle peu claire | 0,9993 | L5 | Hold |
| 6 | Hypertension pulmonaire liée à une maladie pulmonaire et/ou à l'hypoxie | 0,9993 | L5 | Hold |
| 7 | Néphropathie hypertensive maligne | 0,9993 | L5 | Hold |
| 8 | Hypertension rénovasculaire maligne | 0,9993 | L5 | Hold |
| 9 | Hémorragie intracérébrale | 0,9993 | L5 | Question de recherche |
| 10 | Syndrome de Braddock | 0,9992 | L5 | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, telmisartan appartient à la classe des antagonistes des récepteurs AT1 de l'angiotensine II. Son efficacité dans l'hypertension et la prévention des accidents vasculaires cérébraux est établie, et il pourrait mécanistiquement s'appliquer à d'autres pathologies vasculaires.

Pour l'occlusion des artères cérébrales, les études précliniques évoquent deux axes : le blocage du récepteur AT1 et une activité agoniste partielle du récepteur PPARγ. Dans des modèles animaux d'occlusion de l'artère cérébrale moyenne, telmisartan réduit le stress oxydatif, l'inflammation et le volume de l'infarctus ; une synergie avec la nimodipine et une inhibition de Egr-1 médiée par PPARγ ont aussi été rapportées.

Cependant, aucune donnée humaine ne démontre un effet sur l'occlusion artérielle cérébrale aiguë. Le soutien clinique se limite à des essais de prévention par réduction de la pression artérielle. Pour l'hémorragie intracérébrale, le lien repose sur la baisse tensionnelle, mais l'effet propre de telmisartan ne peut être isolé de celui de la combinaison.

## Preuves d'Essais Cliniques

### Occlusion des artères cérébrales

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01075698](https://clinicaltrials.gov/study/NCT01075698) | Phase 4 | Terminé | 1228 | Telmisartan vs traitement habituel chez des hypertendus à haut risque ; effets sur les biomarqueurs et les événements cardiovasculaires (prévention, cible non spécifique) |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | Non applicable | Arrêté | 4 | Sous-étude IRM de TRIDENT ; effectif trop faible pour être exploitable |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Arrêté | 1 | Sous-étude cognitive de TRIDENT ; aucune donnée interprétable |

### Hémorragie intracérébrale

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Terminé | 1671 | TRIDENT : pilule combinée de trois antihypertenseurs à faible dose contre placebo après hémorragie intracérébrale ; critère principal : récidive d'AVC |

Les deux autres essais (NCT03783754 et NCT03785067) sont des sous-études arrêtées prématurément, non informatives.

## Preuves de la Littérature

### Occlusion des artères cérébrales (sélection)

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24780412](https://pubmed.ncbi.nlm.nih.gov/24780412/) | 2014 | Préclinique (animal) | J Stroke Cerebrovasc Dis | Réduction du stress oxydatif et de l'accumulation d'α-synucléine phosphorylée chez le rat après occlusion transitoire |
| [25307428](https://pubmed.ncbi.nlm.nih.gov/25307428/) | 2014 | Préclinique (animal) | J Stroke Cerebrovasc Dis | Amélioration de molécules liées au syndrome métabolique (PPAR-γ, AT1R) à long terme |
| [21901125](https://pubmed.ncbi.nlm.nih.gov/21901125/) | 2011 | Préclinique (animal) | PLoS One | Comparaison telmisartan/ramipril et association dans plusieurs modèles d'AVC chez le rat |
| [19604102](https://pubmed.ncbi.nlm.nih.gov/19604102/) | 2009 | Préclinique (animal) | J Neurotrauma | Réduction du volume de l'infarctus cérébral et de la cPLA2 péri-infarctus |
| [24650592](https://pubmed.ncbi.nlm.nih.gov/24650592/) | 2014 | Préclinique (animal) | Pharmacol Biochem Behav | Effet neuroprotecteur synergique avec la nimodipine à dose non hypotensive |
| [32992165](https://pubmed.ncbi.nlm.nih.gov/32992165/) | 2020 | Préclinique (animal) | J Stroke Cerebrovasc Dis | Activation de PPARγ et inhibition d'Egr-1, bénéfique contre les lésions cérébrales ischémiques |
| [20498620](https://pubmed.ncbi.nlm.nih.gov/20498620/) | 2010 | Préclinique (animal) | J Hypertens | Une faible dose prévient les lésions ischémiques cérébrales via PPARγ chez la souris diabétique |
| [41341617](https://pubmed.ncbi.nlm.nih.gov/41341617/) | 2025 | Préclinique (animal) | Toxicol Rep | Atténuation de la neurotoxicité d'ischémie-reperfusion via la voie Nrf2/HO-1 |

### Hémorragie intracérébrale (sélection)

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | ECR | N Engl J Med | Trois antihypertenseurs à faible dose en une pilule après hémorragie intracérébrale (TRIDENT) ; effet attribuable à la combinaison |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Protocole d'essai | Int J Stroke | Justification et conception de TRIDENT |
| [24636673](https://pubmed.ncbi.nlm.nih.gov/24636673/) | 2014 | Analyse post-hoc d'ECR | Int J Stroke | Différences de récidive ischémique et hémorragique selon l'origine ethnique dans PRoFESS |
| [17538008](https://pubmed.ncbi.nlm.nih.gov/17538008/) | 2007 | Préclinique (animal) | J Pharmacol Exp Ther | Le blocage d'AT1 réduit apoptose, inflammation et stress oxydatif dans l'hémorragie intracérébrale chez le rat |
| [27078703](https://pubmed.ncbi.nlm.nih.gov/27078703/) | 2016 | Préclinique (animal) | Neurol Res | Atténuation du stress oxydatif et du vasospasme après hémorragie sous-arachnoïdienne |

### Hypertension pulmonaire liée à l'hypoxie

Les publications retrouvées sont surtout précliniques (modèles murins d'hypoxie intermittente chronique, par exemple [29969996](https://pubmed.ncbi.nlm.nih.gov/29969996/) et [22447170](https://pubmed.ncbi.nlm.nih.gov/22447170/)) ; plusieurs sont seulement indirectement liées. Elles ne portent pas sur l'hypertension pulmonaire elle-même.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67169534 | TELMISARTAN TEVA SANTE 40 mg | comprimé | Non renseignée (AMM active) |
| 69536527 | TELMISARTAN EG 80 mg | comprimé pelliculé | Non renseignée (AMM active) |
| 62260706 | TELMISARTAN VIATRIS 80 mg | comprimé | Non renseignée (AMM active) |
| 65179106 | TELMISARTAN BIOGARAN 40 mg | comprimé | Non renseignée (AMM active) |
| 68369993 | PRITOR 20 mg | comprimé | Non renseignée (AMM active) |


## Considérations de Sécurité

- **Contre-indications (issues du graphe de connaissances, non du texte de la notice)** : insuffisance hépatique, maladie rénale, anurie, cholestase (dont formes intrahépatiques familiales), pancréatite, maladie de la vésicule biliaire, encéphalopathie hépatique, diabète et acidocétose diabétique, goutte, hypotension, lupus érythémateux systémique, hypercalcémie, hyperparathyroïdie, déficit en potassium, obstruction de l'artère rénale, entre autres.
- **Interactions médicamenteuses** (100 interactions recensées) :
  - Majeures : citrate de potassium, bicarbonate de potassium (risque d'hyperkaliémie).
  - Modérées (exemples) : corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), acide acétylsalicylique, morphine, bupropion, inhibiteurs du SGLT2 (canagliflozine, dapagliflozine, empagliflozine), insulines, exénatide.
- **Point d'attention propre aux indications rénovasculaires** : les sartans comportent un risque en cas de sténose bilatérale des artères rénales ; une revue de sécurité serait nécessaire.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Pour l'occlusion des artères cérébrales, les preuves sont presque exclusivement précliniques, sans essai humain spécifique ; pour l'hémorragie intracérébrale, l'essai TRIDENT est encourageant mais ne permet pas d'isoler l'effet de telmisartan. Les autres indications prédites n'ont aucune preuve (L5).

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications issues de la notice de l'ANSM (lacune bloquante pour le dépistage de sécurité)
- Données détaillées sur le mécanisme d'action
- Examen des résultats détaillés de TRIDENT pour évaluer la contribution propre de telmisartan
- Essais cliniques humains ciblant directement l'indication retenue
- Clarification du statut réglementaire (AMM annulées) et de la disponibilité commerciale du médicament en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

