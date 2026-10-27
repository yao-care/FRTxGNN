---
layout: default
title: Dextromethorphan
parent: Prédiction du modèle uniquement (L5)
nav_order: 233
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Dextromethorphan : nouvelle indication prédite, Maladie de la cavité nasale (niveau de preuve L5). Indication d'origine : Rhinite allergique (source : base de connaissances TxGNN"
monitor_inn: "dextromethorphan"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "faucial diphtheria", "trigeminal autonomic cephalalgia", "cervical disc degenerative disorder", "allergic urticaria"]
---

# Dextromethorphan
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

## Dextrométhorphane : De la rhinite allergique à la maladie de la cavité nasale
{: .text-alpha }

## Résumé en Une Phrase

Le dextrométhorphane est un antitussif central, initialement associé dans la base de connaissances aux affections des voies respiratoires hautes (rhinite allergique, rhinite vasomotrice, pharyngite, rhume, rhinopharyngite) et aux céphalées.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie de la cavité nasale**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Rhinite allergique (source : base de connaissances TxGNN ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Maladie de la cavité nasale |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Toutes les AMM sont annulées |
| Nombre d'AMM | 7 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le dextrométhorphane agit principalement au niveau central, comme agoniste des récepteurs sigma-1 et antagoniste NMDA dans le centre de la toux. Aucun mécanisme direct sur le tissu de la cavité nasale n'est établi.

Les indications originales incluent déjà la rhinite allergique, la rhinite vasomotrice, la rhinite et la rhinopharyngite. Le score très élevé reflète donc probablement un chevauchement avec ces indications des voies respiratoires hautes, plutôt qu'une véritable nouvelle opportunité de repositionnement.

Il s'agit d'une prédiction issue d'un graphe de connaissances, sans preuve clinique à l'appui.

### Autres prédictions du modèle (à titre indicatif)

| Maladie prédite | Score TxGNN | Évaluation |
|------|------|------|
| Laryngopharyngite aiguë | 99,98 % | Probablement proche d'indications existantes (pharyngite, rhume) ; soulagement symptomatique de la toux seulement |
| Diphtérie faucale | 99,36 % | Aucune justification biologique (pas d'activité antibactérienne ni antitoxine) ; proximité avec la pharyngite dans le graphe |
| Céphalée autonome trigéminale | 99,32 % | Lien spéculatif via l'antagonisme NMDA et la sensibilisation centrale ; plausibilité indirecte |
| Dégénérescence discale cervicale | 99,30 % | Lien faible et indirect (douleur, pas la maladie elle-même) |
| Urticaire allergique | 99,25 % | Aucun mécanisme antiallergique ; bénéfice non attendu |

Toutes ces prédictions sont de niveau L5, sans essai clinique ni publication, avec une recommandation Hold.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 7 AMM sont annulées ; aucune n'est actuellement valide.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 66819541 | TUSSIDANE 1,5 mg/ml SANS SUCRE, solution buvable | Solution buvable | Annulée |
| 60940109 | TUSSIDANE 1,5 mg/ml, sirop | Sirop | Annulée |
| 65799705 | DEXTROMETHORPHANE BIOGARAN 1,5 mg/mL SANS SUCRE | Solution buvable | Annulée |
| 66078868 | PULMODEXANE 30 mg, comprimé pelliculé | Comprimé pelliculé | Annulée |
| 66367100 | PULMODEXANE 300 mg/100 ml SANS SUCRE | Solution buvable | Annulée |

Deux autres AMM annulées existent (NODEX ADULTES, sirop unidose ; TUSSIDANE 30 mg, comprimé pelliculé sécable). Le texte des indications approuvées n'est pas renseigné.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, syndrome du QT long (y compris familial), torsades de pointes, insuffisance hépatique, épilepsie, bronchopneumopathie chronique obstructive, bronchite, ulcère gastrique ou peptique, maladie rénale, pancréatite, maladie hépatique, maladie de la vésicule biliaire, thrombocytopénie, insuffisance surrénalienne (maladie d'Addison), hypothyroïdie, maladie inflammatoire de l'intestin, diabète et acidocétose diabétique, hyperplasie bénigne de la prostate, trouble hypotensif, entre autres.
- **Interactions médicamenteuses** : 306 interactions recensées. Interactions majeures : dexfenfluramine, dolasétron, fenfluramine, granisétron, lorcasérine, ondansétron, palonosétron, sibutramine. Interactions modérées : bupropion, morphine, cimétidine, dronabinol, éliglustat, métoclopramide, nabilone, opium, phentermine, entre autres. Les interactions sérotoninergiques et via le CYP2D6 appellent une attention particulière.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, non disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication. Elle recoupe probablement des indications déjà existantes. De plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank) pour évaluer le lien mécanistique
- Mises en garde et contre-indications officielles de la notice (ANSM), actuellement manquantes et bloquantes pour l'évaluation de sécurité
- Revue de la littérature et des registres d'essais pour la maladie de la cavité nasale
- Clarification de la nouveauté réelle de l'indication par rapport aux indications déjà couvertes
- Évaluation de la voie d'administration et du profil d'interactions avant toute étude
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

