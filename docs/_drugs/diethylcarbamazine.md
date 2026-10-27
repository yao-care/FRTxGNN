---
layout: default
title: Diethylcarbamazine
parent: Prédiction du modèle uniquement (L5)
nav_order: 239
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Diethylcarbamazine : nouvelle indication prédite, Lymphœdème syndromique (niveau de preuve L5). Indication d'origine : Filariose lymphatique, éléphantiasis, loase…"
monitor_inn: "diethylcarbamazine"
predicted_indications: ["syndromic lymphedema", "primary lymphedema"]
---

# Diethylcarbamazine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Diéthylcarbamazine : De la filariose lymphatique au lymphœdème syndromique
{: .text-alpha }

## Résumé en Une Phrase

La diéthylcarbamazine est un antifilarien, initialement utilisé pour traiter les filarioses (filariose lymphatique, loase, onchocercose) et leurs complications telles que l'éléphantiasis et la pneumonie à éosinophiles.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **lymphœdème syndromique**, mais **aucun essai clinique** ne soutient cette direction et la littérature recueillie concerne la filariose, pas le lymphœdème syndromique.
Il s'agit d'une prédiction du modèle seule, sans validation réelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Filariose lymphatique, éléphantiasis, loase, onchocercose (texte d'indication de l'AMM non renseigné) |
| Nouvelle Indication Prédite | Lymphœdème syndromique |
| Score de Prédiction TxGNN | 99,59 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement pour l'indication ciblée ; le système source indiquait L4) |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, la diéthylcarbamazine est un microfilaricide : elle agit sur le système neuromusculaire des parasites et favorise la cytotoxicité à médiation immunitaire de l'hôte (voie de l'acide arachidonique notamment).

Le score élevé reflète très probablement la proximité, dans le graphe de connaissances, entre le lymphœdème syndromique et les lymphœdèmes filariens, qui font déjà partie des indications d'origine. Il ne traduit pas un effet validé sur les lymphœdèmes d'origine génétique.

Le lymphœdème syndromique résulte de défauts de développement ou génétiques du système lymphatique (voies VEGFR3, FOXC2, GJC2, par exemple), alors que le médicament cible le parasite. Aucun lien mécanistique plausible avec la pathologie sous-jacente n'a été établi. Tout bénéfice serait indirect et spéculatif.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Deux publications ont été rattachées à l'indication prédite. Elles portent sur des atteintes filariennes, non sur le lymphœdème syndromique.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [1580599](https://pubmed.ncbi.nlm.nih.gov/1580599/) | 1992 | Revue | Annual Review of Medicine | Éosinophilie pulmonaire tropicale : hyperréactivité immunitaire aux filaires (*W. bancrofti*, *B. malayi*), avec toux nocturne, dyspnée et éosinophilie sanguine |
| [24772754](https://pubmed.ncbi.nlm.nih.gov/24772754/) | 2013 | Rapport de cas | J Assoc Physicians India | Chylurie et protéinurie néphrotique secondaires à une filariose, traitées par sclérothérapie et diéthylcarbamazine ; patiente asymptomatique à 19 mois |

Pour le lymphœdème primaire (2e prédiction, score 99,25 %), 19 publications ont été recueillies. Elles portent presque exclusivement sur la filariose lymphatique, l'onchocercose ou l'éosinophilie pulmonaire tropicale (épidémiologie, programmes d'élimination, revues sur les antifilariens, une méta-analyse en réseau de 2025 et un essai randomisé sur des associations à base de moxidectine en 2025). Elles soutiennent l'usage dans la maladie filarienne, pas dans le lymphœdème primaire.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63411794 | NOTEZINE 100 mg, comprimé sécable (SANOFI WINTHROP INDUSTRIE) | Comprimé sécable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées. La littérature rappelle néanmoins que la diéthylcarbamazine peut provoquer des événements oculaires graves chez les personnes atteintes d'onchocercose, ce qui limite son usage dans certaines zones (Afrique subsaharienne).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score élevé du modèle semble refléter la proximité avec les lymphœdèmes filariens déjà connus, sans effet démontré sur les lymphœdèmes syndromiques ou primaires d'origine génétique. Aucun essai clinique n'existe, aucun lien mécanistique n'est établi, et l'AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank) et analyse d'un éventuel lien avec les voies lymphatiques génétiques
- Mises en garde et contre-indications de la notice ANSM (bloquant pour l'évaluation de sécurité)
- Données précliniques ou études observationnelles sur le lymphœdème non filarien
- Clarification du statut réglementaire, l'AMM étant annulée et sans indication renseignée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

