---
layout: default
title: Inotersen
parent: Prédiction du modèle uniquement (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Inotersen : nouvelle indication prédite, Porphyrie aiguë intermittente (niveau de preuve L4). Indication d'origine : Non renseignée dans l'AMM française"
monitor_inn: "inotersen"
predicted_indications: ["acute intermittent porphyria", "appendicitis", "IgG4-related pachymeningitis", "IgG4-related retroperitoneal fibrosis", "non-infectious meningitis", "peritonitis", "infectious meningitis", "IgG4-related mesenteritis", "IgG4-related mediastinitis", "eosinophilic angiocentric fibrosis"]
---

# Inotersen
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

## Inotersen : De l'amylose héréditaire à transthyrétine à la Porphyrie Aiguë Intermittente
{: .text-alpha }

## Résumé en Une Phrase

Inotersen est un oligonucléotide antisens ciblant l'ARN messager de la transthyrétine (TTR). Dans les données compilées pour ce report, aucune indication d'origine n'est renseignée dans l'AMM française, et la spécialité (TEGSEDI) n'y figure plus qu'à l'état d'AMM annulée.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Porphyrie Aiguë Intermittente**, mais **aucun essai clinique** n'est enregistré et **une seule publication** (une revue générale) y est associée : la prédiction repose essentiellement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans l'AMM française |
| Nouvelle Indication Prédite | Porphyrie aiguë intermittente |
| Score de Prédiction TxGNN | 0,9992 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales, inotersen est un oligonucléotide antisens qui cible l'ARNm de la TTR afin de réduire la production de la protéine, ce qui est la logique appliquée dans l'amylose héréditaire à transthyrétine (hATTR) avec polyneuropathie.

La porphyrie aiguë intermittente est un trouble hépatique de la biosynthèse de l'hème (déficit en HMBS) avec des manifestations neuropathiques. Le seul lien identifié est une revue générale sur les maladies neuromusculaires génétiques et les thérapies à base d'oligonucléotides, qui traite à la fois des neuropathies héréditaires et des traitements ciblant l'ARN.

Aucun lien mécanistique direct entre l'inhibition de la TTR et la physiopathologie de la porphyrie n'est établi. Le score élevé du modèle reflète probablement une proximité dans le réseau de connaissances via des phénotypes de neuropathie partagés, plutôt qu'un véritable mécanisme thérapeutique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [30847674](https://pubmed.ncbi.nlm.nih.gov/30847674/) | 2019 | Revue | Neurological Sciences | Revue des maladies neuromusculaires génétiques et des nouvelles thérapies des neuropathies périphériques, dont l'amylose hATTR ; aucune donnée directe sur la porphyrie aiguë intermittente |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60789511 | TEGSEDI 284 mg, solution injectable en seringue préremplie (AKCEA Therapeutics Ireland) | Solution injectable | Non renseignée (AMM active) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : thrombopénie, glomérulonéphrite. Ces deux risques sont à prendre au sérieux, notamment dans les pathologies pouvant atteindre le rein.
- **Interactions Médicamenteuses** : 132 interactions recensées. Principales interactions de niveau majeur :
  - Amphotéricine B (y compris formes lipidiques, liposomale et sulfate de cholestéryle)
  - Acide acétylsalicylique
  - Mésalazine, balsalazide, olsalazine, sulfasalazine
  - Aminosides : kanamycine, néomycine, streptomycine
  - Vancomycine, polymyxine B
  - Acide iothalamique
  - Interactions de niveau modéré : dexfenfluramine, fenfluramine, exénatide, naltrexone, sibutramine

Veuillez consulter la notice pour les mises en garde et contre-indications officielles ; ces informations n'ont pas pu être récupérées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle, sans essai clinique ni donnée directe, avec un lien mécanistique non établi. L'AMM française est annulée et les données de sécurité officielles manquent, ce qui bloque l'évaluation de sécurité.
- Les neuf autres indications prédites (appendicite, méningites, péritonite, atteintes liées aux IgG4, etc.) sont de niveau L5 et également en Hold.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde, contre-indications) auprès de l'ANSM
- Obtenir les données sur le mécanisme d'action via DrugBank
- Démontrer un lien biologique plausible entre la réduction de la TTR et la porphyrie (études précliniques)
- Évaluer le profil de risque (thrombopénie, glomérulonéphrite) au regard de l'indication visée
- Clarifier le statut réglementaire de l'AMM annulée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

