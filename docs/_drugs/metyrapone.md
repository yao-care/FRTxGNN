---
layout: default
title: Metyrapone
parent: Prédiction du modèle uniquement (L5)
nav_order: 495
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Metyrapone : nouvelle indication prédite, Hyperthermie maligne d'effort (niveau de preuve L5). Indication d'origine : Non renseignée dans les AMM disponibles (usage connu : test diagnosti…"
monitor_inn: "metyrapone"
predicted_indications: ["exercise-induced malignant hyperthermia", "malignant hyperthermia, susceptibility to", "King-Denborough syndrome", "central core myopathy", "moderate multiminicore disease with hand involvement", "congenital multicore myopathy with external ophthalmoplegia", "myopathy, centronuclear", "familial periodic paralysis", "renal tubular acidosis", "malignant hyperthermia of anesthesia"]
---

# Metyrapone
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

# Métyrapone : De l'usage diagnostique et endocrinien à l'hyperthermie maligne d'effort

## Résumé en Une Phrase

Le métyrapone est un inhibiteur de la synthèse du cortisol, utilisé comme outil diagnostique de la fonction hypothalamo-hypophysaire et, occasionnellement, dans le traitement du syndrome de Cushing.
Le modèle TxGNN le prédit comme potentiellement efficace pour l'**hyperthermie maligne d'effort**, mais **aucun essai clinique** et **aucune publication** ne soutiennent cette prédiction.
La seule publication identifiée pour l'ensemble des indications prédites concerne la paralysie périodique familiale (rang 8) et date de 1971.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM disponibles (usage connu : test diagnostique de la fonction hypothalamo-hypophysaire, syndrome de Cushing) |
| Nouvelle Indication Prédite | Hyperthermie maligne d'effort |
| Score de Prédiction TxGNN | 99,95 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisation annulée uniquement |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Selon les informations pharmacologiques connues, le métyrapone inhibe la 11-bêta-hydroxylase (CYP11B1) et, dans une moindre mesure, CYP11B2, ce qui réduit la synthèse du cortisol.

**Cette prédiction est mécanistiquement peu plausible.** L'hyperthermie maligne est principalement liée à des variants de RYR1 ou CACNA1S, qui provoquent une libération incontrôlée de calcium par le réticulum sarcoplasmique. L'inhibition de la stéroïdogenèse surrénalienne ne cible pas cette voie. Le score élevé reflète très probablement la proximité dans le graphe de connaissances avec des nœuds de myopathies et d'hyperthermie, et non une justification pharmacologique.

Les autres indications prédites (hyperthermie maligne de susceptibilité, syndrome de King-Denborough, myopathies à cores, myopathie centronucléaire, acidose tubulaire rénale) relèvent du même constat : pas de lien mécanistique établi et aucune donnée clinique fournie.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature n'est disponible pour l'indication principale. La seule publication identifiée parmi les indications prédites concerne une autre indication (paralysie périodique familiale) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [4322666](https://pubmed.ncbi.nlm.nih.gov/4322666/) | 1971 | Étude physiologique/clinique de petite taille (type incertain) | J Clin Invest | Chez un patient de 19 ans atteint de paralysie périodique hyperkaliémique, la paralysie a été induite par le chlorure de potassium, la corticotropine et divers glucocorticoïdes, mais pas par les minéralocorticoïdes ni par l'ACTH associée au métyrapone |

Cette publication est ancienne, porte sur un seul patient et n'étudie pas le métyrapone comme traitement. Elle ne soutient pas l'indication principale.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68806037 | METYRAPONE ESTEVE 250 mg, capsule molle (ESTEVE PHARMACEUTICALS, Espagne) | Capsule molle | Non renseignée (AMM annulée) |

## Cytotoxicité

Le métyrapone n'est pas un médicament antineoplasique cytotoxique conventionnel. Cette section est donc omise.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : maladie d'Addison, insuffisance surrénalienne (primaire chronique et autres formes), insuffisance surrénalienne cortico-déficiente familiale, hypoplasie surrénalienne congénitale liée à l'X, hypoplasie surrénalienne familiale avec absence de LH hypophysaire, déficit partiel en CYP11A1, hyperplasie congénitale des surrenales, insuffisance corticosurrénalienne.
- **Interactions médicamenteuses** (12 relevées, niveau modéré) :
  - Œstrogènes : éthinylestradiol, estradiol (y compris topique), œstrogènes conjugués (y compris topiques), mestranol, œstrogènes estérifiés, sulfate d'estrone (y compris topique).
  - Cyproheptadine.
  - Cibles pharmacologiques : CYP11B1 et CYP11B2.

Les mises en garde et contre-indications issues de la notice ANSM ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible avec la physiopathologie de l'hyperthermie maligne (RYR1).
- Le produit n'a plus d'AMM valide en France, et les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice ANSM (mises en garde, contre-indications), un manque bloquant pour toute étape de sécurité.
- Compléter les données sur le mécanisme d'action via DrugBank.
- Démontrer un lien biologique entre l'inhibition de CYP11B1 et la voie RYR1/calcium, par exemple par des études précliniques.
- Réexaminer les autres indications prédites ; la paralysie périodique familiale (L4) est la seule disposant d'un signal bibliographique, mais indirect et ancien.
- Clarifier le statut réglementaire (AMM annulée) et la disponibilité d'autres spécialités à base de métyrapone.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

