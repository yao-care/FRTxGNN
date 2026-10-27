---
layout: default
title: Terazosin
parent: Prédiction du modèle uniquement (L5)
nav_order: 742
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Terazosin : nouvelle indication prédite, Hypotrichose simple du cuir chevelu (niveau de preuve L5). Indication d'origine : Hypertension artérielle…"
monitor_inn: "terazosin"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine disorder", "migraine with brainstem aura", "Raynaud disease", "Ambras type hypertrichosis universalis congenita", "manic bipolar affective disorder", "kyphoscoliotic heart disease"]
---

# Terazosin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Terazosine : De l'Hypertension à l'Alopécie
{: .text-alpha }

## Resume en Une Phrase

La terazosine est un alpha-1 bloquant, initialement utilisé pour le traitement de l'hypertension artérielle et de l'hyperplasie bénigne de la prostate.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypotrichose simple du cuir chevelu** (rang 1), mais cette prédiction repose uniquement sur le modèle, sans aucun essai clinique ni publication.
Parmi les autres pistes prédites, la **maladie de Raynaud** est la mieux documentée, avec **1 publication** de 1997, et la **migraine** dispose de **2 publications** anciennes.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle, hyperplasie bénigne de la prostate (texte d'indication de l'AMM non disponible) |
| Nouvelle Indication Predite | Hypotrichose simple du cuir chevelu |
| Score de Prediction TxGNN | 99,97 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes annulées) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la terazosine est un alpha-1 bloquant adrénergique à activité vasodilatatrice. Son efficacité dans l'hypertension et l'hyperplasie bénigne de la prostate est établie.

Pour l'hypotrichose du cuir chevelu, le lien mécanistique reste très spéculatif : on pourrait imaginer un effet via la perfusion du follicule pileux, mais aucune donnée ne le soutient. Il s'agit d'une affection héréditaire, et le score élevé reflète probablement la proximité dans le graphe de connaissances avec d'autres termes liés aux cheveux.

Parmi les autres prédictions, deux pistes ont un fondement plus plausible. La maladie de Raynaud : le blocage alpha-1 réduit la vasoconstriction sympathique, ce qui est biologiquement cohérent. La migraine : une modulation du tonus vasculaire adrénergique a été évoquée. Pour l'alopécie au sens large, une seule revue sur les effets extracardiaques des médicaments cardiovasculaires est disponible. Elle est indirecte et centrée sur le minoxidil, non sur la terazosine.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

Aucune littérature associée disponible actuellement pour l'hypotrichose simple du cuir chevelu. Les publications ci-dessous concernent des indications prédites voisines ou alternatives :

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [9273472](https://pubmed.ncbi.nlm.nih.gov/9273472/) | 1997 | Étude clinique (conception à vérifier) | Minerva Cardioangiologica | Raynaud : diminution du nombre, de l'intensité et de la durée des crises vasospastiques, avec amélioration des examens télethermographiques et échographiques |
| [7911406](https://pubmed.ncbi.nlm.nih.gov/7911406/) | 1994 | Étude clinique ouverte (petite, conception peu claire) | La Clinica Terapeutica | Migraine sans aura : 46 patients, dont 10 sous terazosine, évalués pour une activité prophylactique |
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Revue / série de cas | Headache | Prophylaxie de la migraine : amélioration chez presque tous les 10 patients traités par terazosine ou doxazosine, mais 5 arrêts pour effets indésirables |
| [34779371](https://pubmed.ncbi.nlm.nih.gov/34779371/) | 2022 | Revue | Current Cardiology Reviews | Effets extracardiaques des médicaments cardiovasculaires, dont des effets capillaires ; lien indirect, surtout lié au minoxidil |

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 60376815 | HYTRINE 1 mg, comprimé (AMDIPHARM), annulée | Comprimé | Non disponible |
| 66297890 | HYTRINE 5 mg, comprimé (AMDIPHARM), annulée | Comprimé | Non disponible |

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, hypotension orthostatique, priapisme, syndrome de l'iris hypotonique peropératoire.
- **Interactions médicamenteuses** : 137 interactions recensées. Les principales, de niveau modéré, concernent les corticoïdes (hydrocortisone, prednisone, prednisolone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), les inhibiteurs du SGLT2 (canagliflozine, dapagliflozine, empagliflozine, ertugliflozine), les opioïdes (morphine, morphine liposomale, opium), le bupropion, ainsi que les cannabinoïdes (dronabinol, nabilone). Des interactions de niveau inconnu sont signalées avec le calcitriol, le pantoprazole et le glimépiride.
- Le profil connu de la classe (hypotension, vertiges) est pertinent pour toute évaluation de sécurité initiale, notamment dans la maladie de Raynaud.

Veuillez consulter la notice pour les mises en garde détaillées, qui ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- L'indication principale prédite (hypotrichose simple du cuir chevelu) repose uniquement sur le score du modèle (niveau L5), sans essai ni publication, et sans mécanisme plausible. Les produits français sont en outre tous annulés.
- Les pistes les plus intéressantes sont la maladie de Raynaud (niveau L3, « Research Question ») et la migraine (niveau L4, « Research Question »), mais les preuves sont anciennes et de faible qualité.

**Pour avancer, les elements suivants sont necessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le dépistage de sécurité)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Pour la maladie de Raynaud : vérifier la conception et l'effectif de l'étude de 1997 et rechercher des essais contrôlés plus récents
- Pour la migraine : des données contrôlées modernes avant toute considération au-delà de la génération d'hypothèses
- Une étude préclinique ou mécanistique sur les follicules pileux avant d'envisager une indication capillaire
- Une clarification du statut réglementaire, puisque toutes les AMM françaises sont annulées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

