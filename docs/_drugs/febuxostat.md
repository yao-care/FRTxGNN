---
layout: default
title: Febuxostat
parent: Preuves modérées (L3-L4)
nav_order: 317
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Febuxostat : nouvelle indication prédite, Hypouricémie rénale (niveau de preuve L4). Indication d'origine : Hyperuricémie"
monitor_inn: "febuxostat"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "Lesch-Nyhan syndrome"]
---

# Febuxostat
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **3** 
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

# Fébuxostat : De l'hyperuricémie à l'hypouricémie rénale

## Resume en Une Phrase

Le fébuxostat est un inhibiteur sélectif non purique de la xanthine oxydase, initialement utilisé pour traiter l'hyperuricémie.
Le modèle TxGNN le prédit comme potentiellement efficace pour l'**hypouricémie rénale**, mais cette prédiction repose sur **1 essai clinique** (peu pertinent, grade C) et **2 publications** (revues/cas, sans données directes d'efficacité).
Cette prédiction est très probablement un artefact du graphe de connaissances et non un véritable lien thérapeutique.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Hyperuricémie (source : graphe de connaissances ; aucun texte d'indication n'est renseigné dans les AMM) |
| Nouvelle Indication Predite | Hypouricémie rénale |
| Score de Prediction TxGNN | 99,99 % |
| Niveau de Preuve | L4 |
| Statut de Marche en France | Toutes les AMM sont annulées |
| Nombre d'AMM | 20 (0 valide, 20 annulées) |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales, le fébuxostat est un inhibiteur non purique sélectif de la xanthine oxydase : il réduit la production d'acide urique et abaisse l'uricémie. Son efficacité dans l'hyperuricémie est établie.

L'hypouricémie rénale est cependant une situation inverse : l'uricémie est déjà basse en raison d'un défaut de réabsorption rénale de l'urate (perte de fonction de SLC22A12/URAT1 ou de SLC2A9). Abaisser davantage l'acide urique n'a pas de justification thérapeutique claire pour la maladie sous-jacente. Le score élevé du modèle reflète probablement l'association médicament–acide urique–maladie dans le graphe de connaissances plutôt qu'un lien thérapeutique réel.

Une publication japonaise (2023) évoque un usage possible d'inhibiteurs de la xanthine oxydoréductase pour prévenir l'insuffisance rénale aiguë d'effort, complication de l'hypouricémie rénale, chez un footballeur de 16 ans. Il s'agit d'une piste spéculative, indirecte et mécanistiquement différente. Un abaissement supplémentaire de l'urate pourrait en outre aggraver le phénotype.

Deux autres prédictions de rang inférieur sont à titre informatif : le déficit partiel en HPRT et le syndrome de Lesch-Nyhan, où l'inhibition de la xanthine oxydase pourrait contrôler l'hyperuricémie (composante métabolique uniquement, sans effet sur les signes neurologiques). Elles restent au stade de questions de recherche (L4).

---

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Inconnu | 100 | Étude prospective contrôlée sur l'effet du contrôle de l'acide urique sur la récidive de calculs et la fonction rénale chez des patients lithiasiques hyperuricémiques. Probablement sans rapport direct avec l'hypouricémie rénale (grade de pertinence C) |

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Cas clinique / revue | Internal Medicine | Footballeur de 16 ans avec hypouricémie rénale familiale (mutations URAT1) et épisodes récurrents d'insuffisance rénale aiguë d'effort ; l'hydratation seule n'a pas suffi et le fébuxostat est évoqué comme prophylaxie possible |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Revue narrative | Clinical Rheumatology | Mise à jour sur l'hypouricémie (urate sérique < 2 mg/dL) et ses étiologies, à l'usage du rhumatologue |

---

## Informations de Marche en France

Les 20 AMM sont annulées et aucun texte d'indication n'est renseigné. Les 5 premières sont listées ci-dessous.

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 61871331 | ADENURIC 80 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 64493890 | ADENURIC 120 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 67041972 | FEBUXOSTAT ALMUS 80 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 60685046 | FEBUXOSTAT TEVA SANTE 80 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 60661383 | FEBUXOSTAT TEVA SANTE 120 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |

---

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : accident vasculaire cérébral, maladie cérébrovasculaire, infarctus cérébral, infarctus du myocarde, thrombose coronaire, hémoglobinopathie.
- **Interactions médicamenteuses** : 22 interactions recensées.
  - **Majeures** : mercaptopurine, azathioprine, léflunomide, tériflunomide.
  - **Modérées** (exemples) : théophylline, aminophylline, méthotrexate, tioguanine, naltrexone, interférons bêta, asparaginase, pégaspargase, épirubicine, clofarabine, trabectédine, brentuximab védotine.
- **Risque spécifique à l'indication prédite** : un abaissement supplémentaire de l'urate pourrait aggraver le phénotype de l'hypouricémie rénale ou ses complications. Pour les autres pistes (HPRT, Lesch-Nyhan), une surveillance de l'accumulation de xanthine (néphropathie, calculs) serait nécessaire.

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles dans les données compilées ; veuillez consulter la notice.

---

## Conclusion et Prochaines Etapes

**Décision : Hold**

**Justification :**
- Les preuves se limitent à la prédiction du modèle (L4) : un seul essai peu pertinent et deux publications sans données directes d'efficacité. Le rationnel mécanistique est contradictoire, car le fébuxostat abaisse l'acide urique alors que la maladie ciblée est déjà une hypouricémie. Toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles de la notice (ANSM)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Une vérification de la fiche d'enregistrement de NCT04398251 (condition, intervention, critères)
- Des données cliniques directes sur l'usage du fébuxostat dans l'hypouricémie rénale, ou, plus plausiblement, une réorientation vers le déficit en HPRT / Lesch-Nyhan (alternative en cas d'intolérance à l'allopurinol, avec données de sécurité pédiatriques)
- Une évaluation du risque cardiovasculaire, compte tenu des contre-indications issues du graphe de connaissances
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

