---
layout: default
title: Eslicarbazepine
parent: Preuves élevées (L1-L2)
nav_order: 298
evidence_level: L2
indication_count: 6
---

# Eslicarbazepine
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **6** 
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

# Eslicarbazépine : De l'épilepsie à la migraine (prévention)

## Résumé en Une Phrase

L'eslicarbazépine est un antiépileptique (anticonvulsivant) dont les autorisations françaises sont aujourd'hui toutes annulées, et dont le texte d'indication d'origine n'est pas renseigné dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **migraine (traitement préventif)**,
avec **1 essai clinique** de phase 2 terminé et **aucune publication** portant directement sur l'eslicarbazépine dans la migraine.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM compilées (classe antiépileptique) |
| Nouvelle Indication Prédite | Migraine (migraine disorder) |
| Score de Prédiction TxGNN | 99,78 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'eslicarbazépine appartient à la classe des antiépileptiques bloqueurs des canaux sodiques voltage-dépendants : elle stabilise l'état inactivé du canal et réduit l'hyperexcitabilité neuronale. Ce lien est déduit de la classe pharmacologique et n'est pas documenté dans les données compilées.

Une hyperexcitabilité corticale et la dépression corticale envahissante sont impliquées dans la physiopathologie de la migraine. D'autres antiépileptiques (topiramate, valproate) sont des traitements préventifs établis, ce qui rend l'hypothèse plausible. Le score TxGNN très élevé (0,998) est cohérent avec ce raisonnement de classe.

Toutefois, il s'agit d'une inférence : l'eslicarbazépine n'est pas commercialisée dans la migraine, et l'absence de résultats publiés de l'essai de phase 2 pourrait suggérer un bénéfice insuffisant. Les résultats doivent être vérifiés avant toute recommandation.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01820559](https://clinicaltrials.gov/study/NCT01820559) | Phase 2 | Terminé | 452 | Essai multinational randomisé en double aveugle contre placebo : acétate d'eslicarbazépine 800 mg/j ou 1200 mg/j (une prise par jour) en prévention de la migraine avec ou sans aura (2009-2010). Aucun résultat n'est fourni dans les données compilées. |

## Preuves de la Littérature

Aucune publication ne porte directement sur l'eslicarbazépine dans la migraine. Les références liées sont des revues générales ou indirectes :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Revue | Expert Rev Neurother | Mise à jour sur la pharmacothérapie de la névralgie trigéminale ; mentionne les anticonvulsivants de troisième génération et les nouveaux inhibiteurs du CGRP dans la migraine comme options possibles |
| [32217376](https://pubmed.ncbi.nlm.nih.gov/32217376/) | 2020 | Revue | J Neurol Sci | Tolérance et sécurité de l'acétate d'eslicarbazépine dans les troubles neurologiques |
| [32025776](https://pubmed.ncbi.nlm.nih.gov/32025776/) | 2020 | Étude préclinique | Psychopharmacology | L'eslicarbazépine associée à des analgésiques standard ou alternatifs réduit la nociception trigéminale (interaction favorable) |
| [35363878](https://pubmed.ncbi.nlm.nih.gov/35363878/) | 2022 | Méta-analyse | Cochrane Database Syst Rev | Méta-analyse en réseau des monothérapies antiépileptiques dans l'épilepsie (indirect) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63927729 | ESLICARBAZEPINE ARROW 800 mg, comprimé sécable (ARROW GÉNÉRIQUES) | Comprimé sécable | Non renseignée (AMM annulée) |
| 68829121 | ZEBINIX 800 mg, comprimé (BIAL - PORTELA & CA) | Comprimé | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 125 interactions sont recensées. Parmi les interactions de niveau modéré figurent : aprépitant, morphine (y compris liposomale), opium, difénoxine, diphénoxylate, dronabinol, nabilone, éliglustat, naloxégol, mannitol, métoclopramide, nitisinone, rolapitant, rosuvastatine, simvastatine, sibutramine, éthanol, acide folique et cobicistat.

Les mises en garde et contre-indications de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Une seule étude directe existe (phase 2 terminée, 452 patients), sans résultats disponibles, et le médicament n'est pas commercialisé dans la migraine, ce qui laisse penser que le bénéfice n'a pas été démontré. Les autres indications prédites (sous-types de migraine, insomnie, affections dermatologiques rares) reposent sur le modèle seul ou sur des données indirectes. Pour l'insomnie, la seule publication suggère plutôt un effet indésirable sur le sommeil.
- Les AMM françaises sont toutes annulées et les données de sécurité de la notice font défaut.

**Pour avancer, les éléments suivants sont nécessaires :**
- Retrouver les résultats publiés ou enregistrés de l'essai NCT01820559 (efficacité et tolérance)
- Obtenir la notice (mises en garde, contre-indications) auprès de l'ANSM
- Compléter les données sur le mécanisme d'action
- Clarifier les raisons de l'annulation des AMM et le statut de marché actuel
- Regrouper les entrées de migraine apparentées (sous-types, terme de susceptibilité génétique) sous une seule indication
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

