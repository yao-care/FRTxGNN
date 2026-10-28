---
layout: default
title: Erdafitinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 292
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
description: "Erdafitinib : nouvelle indication prédite, Hypertension pulmonaire (niveau de preuve L5). Indication d'origine : Non renseignée dans les données compilées"
monitor_inn: "ERDAFITINIB"
predicted_indications: ["pulmonary hypertension", "kyphoscoliotic heart disease", "amenorrhea (disease)", "rheumatoid arthritis", "amyotrophic lateral sclerosis", "brachydactyly-syndactyly syndrome"]
---

# Erdafitinib
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Erdafitinib : De l'indication d'origine non documentée à l'Hypertension Pulmonaire
{: .text-alpha }

## Resume en Une Phrase

Erdafitinib est un inhibiteur de tyrosine kinase des récepteurs FGFR (FGFR1 à 4). Les données compilées pour ce rapport ne précisent pas son indication d'origine en France, les textes d'indication des AMM étant vides.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension pulmonaire**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données compilées |
| Nouvelle Indication Predite | Hypertension pulmonaire |
| Score de Prediction TxGNN | 0,9938 |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base compilée. D'après les connaissances générales, l'erdafitinib est un inhibiteur pan-FGFR (FGFR1-4). Son indication d'origine n'a pas pu être extraite des AMM françaises.

La voie de signalisation FGF/FGFR a été impliquée dans le remodelage vasculaire pulmonaire ainsi que dans la prolifération des cellules musculaires lisses et endothéliales. Un lien hypothétique existe donc avec l'hypertension pulmonaire. Des inhibiteurs de kinases à spectre plus large (par exemple l'imatinib) ont été explorés dans l'hypertension artérielle pulmonaire, mais cela ne constitue pas une preuve pour l'erdafitinib.

Ce lien repose uniquement sur le score de prédiction TxGNN. De plus, l'inhibition de FGFR s'accompagne de préoccupations de sécurité (hyperphosphatémie, toxicité oculaire, entre autres) qui devraient être évaluées dans cette population.

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 66039107 | BALVERSA 3 mg, comprimés pelliculés (active) | Comprimé pelliculé | Non renseignée |
| 65760218 | BALVERSA 4 mg, comprimés pelliculés (active) | Comprimé pelliculé | Non renseignée |
| 60039171 | BALVERSA 5 mg, comprimé pelliculé (active) | Comprimé pelliculé | Non renseignée |

## Cytotoxicite

| Element | Contenu |
|------|------|
| Classification de Cytotoxicite | Thérapie ciblée (inhibiteur de tyrosine kinase pan-FGFR) |
| Risque de Myelosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Emetogenicite | Veuillez consulter les mises en garde et précautions de la notice |
| Elements de Surveillance | Phosphatémie, examen ophtalmologique ; autres paramètres à consulter dans la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considerations de Securite

- **Interactions Médicamenteuses** : 100 interactions ont été recensées (échantillon de 20 affiché dans les données compilées).
  - **Majeures** : cholécalciférol, dexaméthasone, phosphate de calcium, calcifédiol, calcitriol, acétate de calcium, clarithromycine, oxyde de magnésium, sulfate de magnésium, chlorure de magnésium.
  - **Modérées** : metformine, lopéramide, saxagliptine, éliglustat, empagliflozine, linagliptine, naldémédine, naloxégol, prucalopride, rifaximine.
- **Point d'attention** : plusieurs interactions majeures concernent des suppléments de calcium, de vitamine D et de magnésium, ce qui est cohérent avec le risque d'hyperphosphatémie lié à la classe des inhibiteurs de FGFR.
- Les mises en garde principales et les contre-indications de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations de sécurité.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
La prédiction repose uniquement sur le score TxGNN (niveau de preuve L5), sans essai clinique ni publication spécifique. Les AMM françaises sont toutes annulées et les données de sécurité de la notice sont absentes, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les elements suivants sont necessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) depuis le site de l'ANSM
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Mener une revue de la littérature préclinique sur FGFR et l'hypertension pulmonaire
- Évaluer le profil de sécurité (hyperphosphatémie, toxicité oculaire) dans cette population
- Clarifier l'indication d'origine et le statut réglementaire actuel du produit

---

### Autres prédictions du modèle (à titre informatif)

Toutes ces prédictions sont de niveau L5 avec une décision **Hold**.

| Rang | Indication prédite | Score TxGNN | Remarque |
|------|------|------|------|
| 2 | Cardiopathie cyphoscoliotique | 0,9927 | Aucun lien mécanistique identifiable ; association probablement liée au réseau (via l'hypertension pulmonaire) |
| 3 | Aménorrhée | 0,9926 | Aucun lien mécanistique crédible ; l'hyperphosphatémie est un effet indésirable, non un rationnel thérapeutique |
| 4 | Polyarthrite rhumatoïde | 0,9925 | Hypothèse plausible mais non validée (activation des fibroblastes synoviaux, angiogenèse) ; la seule publication (PMID [31862477](https://pubmed.ncbi.nlm.nih.gov/31862477/), revue générale de 2020 sur les inhibiteurs de kinases approuvés par la FDA) est un contexte indirect |
| 5 | Sclérose latérale amyotrophique | 0,9906 | Sens de l'effet incertain, l'inhibition de FGFR pouvant être neutre ou délétère ; pénétration du SNC non caractérisée |
| 6 | Syndrome brachydactylie-syndactylie | 0,9903 | Lien conceptuel avec le développement des membres ; questions de sécurité importantes (effets squelettiques, développementaux, grossesse) |
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

