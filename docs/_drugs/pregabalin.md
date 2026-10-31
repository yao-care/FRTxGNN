---
layout: default
title: Pregabalin
parent: Prédiction du modèle uniquement (L5)
nav_order: 627
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
monitor_inn: "pregabalin"
predicted_indications: ["tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "inclusion body myositis", "migraine disorder", "migraine with brainstem aura"]
description: "Pregabalin : nouvelle indication prédite, Tendinitis (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Pregabalin
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

## Pregabalin: Tendinitis
{: .text-alpha }

## Résumé en Une Phrase

Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **tendinite**, mais **aucun essai clinique** et **aucune publication directement pertinente** ne soutiennent actuellement cette direction.
La prédiction repose donc uniquement sur le modèle (les articles retrouvés concernent surtout l'analgésie après chirurgie de l'épaule, des cas de compression nerveuse et un effet indésirable d'un antibiotique).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Tendinitis |
| Score de Prédiction TxGNN | 0.9971 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances pharmacologiques générales, la prégabaline se fixe sur la sous-unité alpha-2-delta des canaux calciques voltage-dépendants et réduit la libération de neurotransmetteurs excitateurs. Cela peut atténuer les composantes neuropathiques et la sensibilisation centrale des douleurs musculo-squelettiques chroniques.

Ses indications d'origine (fibromyalgie, syndrome myofascial, névralgie post-zostérienne) sont des douleurs chroniques où cette modulation joue un rôle. La tendinite est une douleur musculo-squelettique ; un bénéfice symptomatique est donc concevable.

Le lien reste toutefois **indirect** : la littérature retrouvée ne traite ni l'inflammation tendineuse ni le traitement des tendinopathies. Le score très élevé du modèle est une prédiction et n'est pas étayé par des preuves cliniques directes.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour la tendinite.

---

## Preuves de la Littérature

Aucune de ces publications ne porte sur le traitement de la tendinite par la prégabaline. Les plus proches :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | ECR | Arthroscopy | Après réparation arthroscopique de la coiffe des rotateurs, la prégabaline orale a donné des scores de douleur postopératoire équivalents à ceux d'un bloc interscalénique (analgésie périopératoire, pas tendinite) |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Cohorte rétrospective | J Orthop Sci | Évaluation de l'effet analgésique et d'épargne des opioïdes de la prégabaline après chirurgie de la coiffe des rotateurs |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Cas / revue | Praxis | Handicap associé aux fluoroquinolones après ciprofloxacine (atteintes tendineuses parmi les effets indésirables) |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Cas clinique | Pain Pract | Atteinte du nerf cutané fémoral postérieur après un marathon, liée à une tendinite des ischio-jambiers |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Éditorial | Arthroscopy | Syndrome du piriforme et traitement par neurolyse du nerf sciatique |

Une étude préclinique chez le rat sur un extrait végétal (PMID 39703364) a aussi été retrouvée ; elle n'est pas pertinente.

---

## Informations de Marché en France

Les 20 AMM sont annulées. Le texte d'indication approuvée n'est pas renseigné. Cinq exemples :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66368704 | PREGABALINE EVOLUGEN PHARMA 50 mg | Gélule | Non renseignée (AMM active) |
| 63595091 | PREGABALINE HCS 100 mg | Gélule | Non renseignée (AMM active) |
| 67326252 | PREGABALINE SANDOZ 50 mg | Gélule | Non renseignée (AMM active) |
| 63096099 | LYRICA 75 mg | Gélule | Non renseignée (AMM active) |
| 62285549 | PREGABALINE BIOGARAN 75 mg | Gélule | Non renseignée (AMM active) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : trouble anxieux, trouble névrotique, trouble dysthymique, thrombocytopénie, angio-œdème (acquis, héréditaire, induit par les bloqueurs du système rénine-angiotensine, non histaminique), myopathie, maladie musculaire, maladie du muscle squelettique, paralysie périodique familiale, rhabdomyolyse, fasciite nodulaire, insuffisance rénale, bloc auriculo-ventriculaire.
  - À noter : le trouble anxieux figure à la fois comme indication d'origine et comme contre-indication dans le graphe, une incohérence à vérifier.
  - La présence de maladies musculaires et de la rhabdomyolyse est à considérer pour des indications musculo-squelettiques.
- **Interactions médicamenteuses** : 183 interactions recensées. Parmi les principales :
  - **Majeures** : morphine, morphine liposomale
  - **Modérées** : pioglitazone, rosiglitazone, troglitazone, difénoxine, diphénoxylate, dronabinol, nabilone, métoclopramide, opium, sibutramine

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique ni publication directe ne soutient l'usage dans la tendinite (niveau L4). Le score de 0,9971 est une prédiction seule.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice officielle (mises en garde, contre-indications) auprès de l'ANSM
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Confirmer le statut réglementaire actuel de la prégabaline en France
- Mener des études précliniques ou cliniques spécifiques à la tendinopathie
- Évaluer le risque lié aux atteintes musculaires et aux interactions avec les opioïdes

**Autres indications prédites (pour information) :**

| Indication | Score TxGNN | Niveau de preuve | Recommandation | Remarque |
|------|------|------|------|------|
| Migraine | 0,9947 | L2 | Question de recherche | Petits ECR pédiatriques (prégabaline vs propranolol et valproate) ; l'essai de phase 3 chez l'adulte (NCT00447369) a été retiré sans données |
| Migraine avec aura du tronc cérébral | 0,9943 | L5 | Hold | Données précliniques sur la dépression corticale envahissante |
| Myosite par fibrose | 0,9971 | L5 | Hold | Prédiction seule |
| Myosite granulomateuse idiopathique | 0,9971 | L5 | Hold | Prédiction seule |
| Myosite à inclusions | 0,9952 | L5 | Hold | Prédiction seule |

La migraine est l'indication prédite la mieux étayée (L2). Elle mérite une évaluation distincte.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

