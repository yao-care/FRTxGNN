---
layout: default
title: Isoflurane
parent: Prédiction du modèle uniquement (L5)
nav_order: 414
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Isoflurane : nouvelle indication prédite, Angor de Prinzmetal (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées"
monitor_inn: "ISOFLURANE"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "manic bipolar affective disorder", "trichotillomania", "dysthymic disorder", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder"]
---

# Isoflurane
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Isoflurane : De l'anesthésie générale à l'angor de Prinzmetal

## Résumé en Une Phrase

L'isoflurane est un anesthésique général volatil administré par inhalation. Les données d'indication originale ne figurent pas dans les autorisations françaises compilées.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**angor de Prinzmetal**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Angor de Prinzmetal |
| Score de Prédiction TxGNN | 99,67 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations générales, l'isoflurane fait partie des anesthésiques volatils halogénés, utilisés pour l'induction et l'entretien de l'anesthésie générale.

Les anesthésiques volatils ont des effets vasodilatateurs et interagissent avec les canaux calciques, ce qui pourrait théoriquement avoir un lien avec le vasospasme coronarien à l'origine de l'angor de Prinzmetal. Cette hypothèse reste toutefois **spéculative** et n'est étayée par aucune donnée compilée pour ce rapport.

Il faut aussi noter que l'isoflurane a été discuté dans le contexte du « vol coronarien » (redistribution du flux sanguin au détriment de zones ischémiques), ce qui constitue une préoccupation de sécurité plutôt qu'un argument thérapeutique. De plus, une administration par inhalation d'anesthésique général se prête mal à une maladie chronique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'angor de Prinzmetal.

*À titre indicatif, pour d'autres indications prédites (non retenues comme indication principale) :*
- **Migraine** (score TxGNN 99,06 %, niveau L4, orientation « question de recherche ») : une étude préclinique de 1996 (PMID [8665587](https://pubmed.ncbi.nlm.nih.gov/8665587/)) rapporte que les anesthésiques inhalés inhibent la dépression corticale envahissante, corrélat de l'aura migraineuse. Deux publications de 2015 ([26323741](https://pubmed.ncbi.nlm.nih.gov/26323741/), [26363696](https://pubmed.ncbi.nlm.nih.gov/26363696/), doublon en langue non anglaise) décrivent un cas d'état de mal migraineux traité par anesthésie générale. Les preuves restent précliniques et au niveau de cas isolés.
- **Trouble bipolaire maniaque** (score 99,57 %, niveau L4, Hold) : une étude ouverte de 1993 (PMID [8462536](https://pubmed.ncbi.nlm.nih.gov/8462536/)) a comparé l'anesthésie à l'isoflurane en burst-suppression à l'électroconvulsivothérapie chez 12 patients atteints de dépression sévère. Les preuves sont trop limitées et anciennes.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée | Statut |
|---------|------|------|-----------|------|
| 61070419 | ISOFLURANE BELAMONT | Liquide pour inhalation par vapeur | Non renseignée | Annulée |
| 63498500 | AERRANE | Liquide pour inhalation par vapeur | Non renseignée | Annulée |
| 65849318 | CEDACONDA 100 % V/V | Liquide pour inhalation par vapeur | Non renseignée | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie, et non texte de notice) : maladie du foie, maladie de la vésicule biliaire, troubles hypotensifs, hyperthermie maligne de l'anesthésie, hyperthermie maligne d'effort, dystrophie musculaire de Duchenne, dystrophie musculaire de Becker et dystrophies musculaires en général.
- **Interactions médicamenteuses** : 38 interactions recensées. La plus importante est de niveau **majeur** avec l'**épinéphrine**. Deux interactions de niveau **modéré** concernent la **morphine** et l'**opium**. Les autres (atropine, hydrocortisone, mannitol, pantoprazole, oméprazole, vancomycine, etc.) sont de niveau non déterminé.
- **Point d'attention propre à l'indication prédite** : le risque de vol coronarien est préoccupant chez des patients présentant une maladie coronarienne.

Les mises en garde et contre-indications de la notice n'ont pas pu être obtenues : veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Le profil de sécurité soulève des signaux défavorables (vol coronarien, hypotension, interaction majeure avec l'épinéphrine), et l'usage d'un anesthésique général inhalé est peu réaliste pour un angor chronique. Les AMM françaises sont toutes annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice officielle (mises en garde et contre-indications) via le site de l'ANSM, qui constitue actuellement un point bloquant pour le criblage de sécurité
- Données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Études précliniques et mécanistiques sur le vasospasme coronarien
- Évaluation de la faisabilité de la voie d'administration et de la population cible
- Si une piste doit être poursuivie, la migraine réfractaire (niveau L4) constitue une question de recherche plus étayée que l'angor de Prinzmetal
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

