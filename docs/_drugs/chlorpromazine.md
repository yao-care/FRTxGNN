---
layout: default
title: Chlorpromazine
parent: Preuves modérées (L3-L4)
nav_order: 164
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Chlorpromazine : nouvelle indication prédite, Dystrophie rétinienne avec ou sans anomalies extraoculaires (niveau de preuve L4). Indication d'origine : Schizophrénie et troubles psychotiques"
monitor_inn: "CHLORPROMAZINE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "syndromic myopia", "hydranencephaly (disease)", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia 26, X-linked, female-limited", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "atypical glycine encephalopathy"]
---

# Chlorpromazine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
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

## Chlorpromazine : De la schizophrénie à la dystrophie rétinienne (avec ou sans anomalies extraoculaires)
{: .text-alpha }

## Résumé en une phrase

La chlorpromazine est un antipsychotique de la famille des phénothiazines, initialement utilisé pour traiter la schizophrénie et d'autres troubles psychotiques.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **dystrophie rétinienne avec ou sans anomalies extraoculaires**, mais **aucun essai clinique** n'est enregistré et **une seule publication** est disponible. Celle-ci décrit une toxicité (réactions phototoxiques) et non un bénéfice thérapeutique.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Schizophrénie et troubles psychotiques (le texte d'indication des AMM françaises n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Predite | Dystrophie rétinienne avec ou sans anomalies extraoculaires |
| Score de Prediction TxGNN | 99,95 % |
| Niveau de Preuve | L4 |
| Statut de Marche en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Decision Recommandee | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la chlorpromazine est un antagoniste des récepteurs dopaminergiques D2, dont l'efficacité dans la schizophrénie et les troubles psychotiques est établie.

Pour la dystrophie rétinienne, la prédiction semble peu soutenue sur le plan mécanistique. La seule publication disponible (JAMA, 1967) décrit des réactions phototoxiques induites par de fortes doses de chlorpromazine et de thioridazine, c'est-à-dire un effet indésirable. Le score élevé du modèle reflète probablement une association dans le graphe de connaissances avec la pathologie rétinienne, plus cohérente avec une toxicité médicamenteuse qu'avec un potentiel thérapeutique.

Aucun mécanisme thérapeutique plausible n'est actuellement étayé. Cette prédiction doit donc être considérée comme un signal du modèle, et non comme une piste de repositionnement crédible en l'état.

## Preuves d'essais cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la littérature

| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [5336672](https://pubmed.ncbi.nlm.nih.gov/5336672/) | 1967 | Rapport de cas / observationnel (toxicité) | JAMA | Réactions phototoxiques induites par de fortes doses de chlorpromazine et de thioridazine ; effet indésirable, pas de bénéfice thérapeutique (résumé non disponible) |

## Informations de marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62184888 | LARGACTIL 25 mg/5 ml, solution injectable en ampoule (annulée) | Solution injectable | Non renseignée |
| 68513504 | LARGACTIL 4 POUR CENT, solution buvable en gouttes (annulée) | Solution buvable en gouttes | Non renseignée |

## Considérations de sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypotension orthostatique, syndrome du QT long (y compris familial), torsades de pointes, arrêt cardiaque soudain, maladies de la conduction cardiaque, infarctus du myocarde, épilepsie, maladies des noyaux gris centraux, dystonie focale de la main, blépharospasme, maladie hépatique, maladie de la vésicule biliaire, thrombopénie, neutropénie, agranulocytose, leucopénie, anémie, hémoglobinopathie, hyperglycémie, hypertrophie bénigne de la prostate, obésité, carcinome mammaire féminin, abus/dépendance de substances, atrophie multisystématisée, syndrome de tachycardie orthostatique posturale.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les principales, deux sont de niveau **majeur** (bupropion, morphine). Les autres, de niveau modéré, concernent notamment des antidiabétiques (metformine, pioglitazone, alogliptine, canagliflozine, chlorpropamide, acarbose, albiglutide), des anticholinergiques (atropine, hyoscyamine, glycopyrronium), la loperamide, l'épinéphrine, l'hydrocortisone, l'amphotéricine B, la famotidine, la lorcaserine et le bisacodyl.

Les mises en garde de la notice ne sont pas disponibles dans les données compilées ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- Le score du modèle est très élevé, mais la seule publication décrit une toxicité (phototoxicité) et non un bénéfice. Aucun essai clinique n'existe et aucun mécanisme thérapeutique plausible n'est identifié.
- Le profil de sécurité (cardiaque, hématologique, neurologique) et l'annulation des deux AMM françaises s'ajoutent aux réserves.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles de la notice (ANSM), actuellement manquantes et bloquantes pour l'étape de sécurité
- Des données détaillées sur le mécanisme d'action (DrugBank)
- Des données précliniques ou mécanistiques démontrant un effet bénéfique, et non toxique, dans les dystrophies rétiniennes
- Une évaluation de la voie d'administration compatible avec une atteinte rétinienne

---

### Note complémentaire : autre indication prédite pertinente

Parmi les autres prédictions, la **schizophrénie à début précoce** (score 99,47 %, niveau L4, statut « question de recherche ») est la plus étayée : 6 publications observationnelles, d'association génétique ou d'imagerie, sans essai enregistré. Il s'agit essentiellement d'une extension pédiatrique de l'indication d'origine plutôt que d'un véritable repositionnement. Son usage chez l'enfant et l'adolescent exige une évaluation de sécurité approfondie (symptômes extrapyramidaux, sédation, effets métaboliques), et les antipsychotiques plus récents sont généralement préférés. Les sept autres prédictions (glycosylation, myopies, malformations cérébrales, Charcot-Marie-Tooth 1G, encéphalopathie glycinique atypique) reposent uniquement sur le modèle, sans preuve, et restent en **Hold**.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

