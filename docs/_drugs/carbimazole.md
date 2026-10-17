---
layout: default
title: Carbimazole
parent: Preuves modérées (L3-L4)
nav_order: 140
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Carbimazole : nouvelle indication prédite, Thyrotoxicose néonatale (niveau de preuve L4). Indication d'origine : Hyperthyroïdie, maladie de Basedow…"
monitor_inn: "CARBIMAZOLE"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia"]
---

# Carbimazole
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **3** 
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

# Carbimazole : De l'Hyperthyroïdie à la Thyrotoxicose Néonatale

## Résumé en Une Phrase

Le carbimazole est un antithyroïdien de synthèse (précurseur du méthimazole), initialement utilisé pour traiter l'hyperthyroïdie, la maladie de Basedow et la thyrotoxicose.
Le modèle TxGNN prédit qu'il pourrait être utile dans la **thyrotoxicose néonatale** (la première prédiction, la résistance aux hormones thyroïdiennes, étant mécanistiquement peu plausible).
Les données compilées pour ce rapport contiennent **aucun essai clinique** et **13 publications** (revues, cohortes, séries et rapports de cas) sur la thyrotoxicose néonatale.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hyperthyroïdie, maladie de Basedow, thyrotoxicose (le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Thyrotoxicose néonatale |
| Score de Prédiction TxGNN | 99,41 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

**Remarque sur le choix de l'indication :** la prédiction de rang 1 (résistance aux hormones thyroïdiennes par mutation du récepteur bêta) a le score le plus élevé (99,71 %), mais elle n'est pas retenue comme indication principale. Les antithyroïdiens ne sont généralement pas recommandés dans cette pathologie (voir ci-dessous). La thyrotoxicose néonatale, de rang 2, est la prédiction la plus plausible. La prédiction de rang 3 (hyperthyroxinémie) recoupe en grande partie l'indication déjà approuvée.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances pharmacologiques établies, le carbimazole est une prodrogue du méthimazole : il inhibe la thyroperoxydase et réduit ainsi la synthèse des hormones thyroïdiennes. Son efficacité dans l'hyperthyroïdie et la maladie de Basedow est établie.

La thyrotoxicose néonatale résulte le plus souvent du passage transplacentaire des anticorps maternels stimulant le récepteur de la TSH au cours de la maladie de Basedow. Le mécanisme (excès de synthèse hormonale) est donc le même que dans l'indication d'origine, et le blocage de la synthèse hormonale est directement pertinent. La littérature rapporte des nouveau-nés traités par carbimazole, ainsi qu'un traitement intra-utérin chez deux fratries.

Il faut toutefois rester prudent : une grande partie des données sont indirectes (traitement de la mère, effets sur le fœtus et le nouveau-né), et en pratique néonatale, le méthimazole est l'agent habituel. Quant à la prédiction de rang 1, le blocage de la synthèse hormonale élèverait la TSH par perte du rétrocontrôle, ce qui risquerait d'aggraver le goitre ; son score élevé reflète probablement une proximité dans le réseau de connaissances plutôt qu'un vrai lien thérapeutique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24251220](https://pubmed.ncbi.nlm.nih.gov/24251220/) | 2013 | Revue | Indian J Endocrinol Metab | La thyrotoxicose fœtale/néonatale est rare ; mortalité de 12 à 20 %, due surtout à l'insuffisance cardiaque ; transfert placentaire d'anticorps stimulants |
| [24622372](https://pubmed.ncbi.nlm.nih.gov/24622372/) | 2013 | Revue | Lancet Diabetes Endocrinol | Hyperthyroïdie pendant la grossesse : distinction avec les modifications physiologiques, risques pour la mère et l'enfant |
| [7523202](https://pubmed.ncbi.nlm.nih.gov/7523202/) | 1994 | Cohorte rétrospective | Eur J Obstet Gynecol Reprod Biol | 32 grossesses avec hyperthyroïdie traitées par carbimazole ou propylthiouracile ; issues maternelles et périnatales |
| [1971773](https://pubmed.ncbi.nlm.nih.gov/1971773/) | 1990 | Cohorte | Clin Endocrinol | 44 femmes avec maladie de Basedow traitées par PTU ou carbimazole ; liens entre anticorps, dose et fonction thyroïdienne néonatale |
| [11298090](https://pubmed.ncbi.nlm.nih.gov/11298090/) | 2001 | Série de cas / revue | Clin Endocrinol | Thyrotoxicose congénitale chez les prématurés ; mortalité rapportée jusqu'à 25 % |
| [41191399](https://pubmed.ncbi.nlm.nih.gov/41191399/) | 2025 | Rapport de cas | Endocrinol Diabetes Metab Case Rep | Hypercalcémie néonatale sévère secondaire à une thyrotoxicose, qui a répondu au carbimazole |
| [25952662](https://pubmed.ncbi.nlm.nih.gov/25952662/) | 2015 | Rapport de cas | Indian J Pediatr | Traitement intra-utérin par carbimazole chez deux fratries après plusieurs mort-nés |
| [12124735](https://pubmed.ncbi.nlm.nih.gov/12124735/) | 2002 | Rapport de cas (signal de sécurité) | Am J Med Genet | Quatrième cas publié d'atrésie des choanes après traitement maternel par carbimazole |
| [27747714](https://pubmed.ncbi.nlm.nih.gov/27747714/) | 2015 | Rapport de cas | Drug Saf Case Rep | Hypotension sévère après amlodipine chez un nouveau-né sous carbimazole et propranolol |
| [2315685](https://pubmed.ncbi.nlm.nih.gov/2315685/) | 1990 | Rapport de cas | Scott Med J | Rechute post-opératoire avec anticorps anti-récepteur de la TSH ; nouveau-né thyrotoxique répondant au carbimazole |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61451683 | NEO-MERCAZOLE 20 mg, comprimé (AMDIPHARM), annulée | Comprimé | Non renseignée |
| 63839179 | NEO-MERCAZOLE 5 mg, comprimé (AMDIPHARM), annulée | Comprimé | Non renseignée |

## Considérations de Sécurité

- **Signaux rapportés dans la littérature :** atrésie des choanes après exposition maternelle au carbimazole en période critique du développement (jours 35 à 38) ; hypothyroïdie ou goitre néonatal en cas de surtraitement ; hypotension sévère lors de l'association de l'amlodipine à un traitement par carbimazole et propranolol chez un nouveau-né.
- **Prédiction de rang 1 :** les antithyroïdiens ne sont généralement pas recommandés dans la résistance aux hormones thyroïdiennes (risque d'élévation de la TSH, d'aggravation du goitre et d'hypothyroïdie tissulaire).

Pour les mises en garde, contre-indications et interactions médicamenteuses officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves se limitent à des revues, des petites séries et des rapports de cas, sans aucun essai clinique ni donnée comparative prospective (niveau L4).
- Aucune AMM n'est en vigueur en France (statut « annulée » uniquement), les données de sécurité officielles sont absentes, et le méthimazole reste l'agent usuel en pratique néonatale.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), une lacune bloquante pour l'étape de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Évaluer les données sur le traitement direct du nouveau-né (et non seulement de la mère), avec comparaison au méthimazole
- Clarifier le statut réglementaire et la disponibilité d'une formulation adaptée à l'usage néonatal
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

