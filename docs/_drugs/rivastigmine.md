---
layout: default
title: Rivastigmine
parent: Preuves modérées (L3-L4)
nav_order: 676
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Rivastigmine : nouvelle indication prédite, Glaucome (niveau de preuve L4). Indication d'origine : Maladie d'Alzheimer"
monitor_inn: "RIVASTIGMINE"
predicted_indications: ["glaucoma"]
---

# Rivastigmine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **1** 
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

## Rivastigmine : De la maladie d'Alzheimer au glaucome
{: .text-alpha }

## Résumé en Une Phrase

La rivastigmine est un inhibiteur des cholinestérases, initialement utilisé pour le traitement de la maladie d'Alzheimer.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **glaucome**, mais il n'existe actuellement **aucun essai clinique** et seulement **3 publications** (dont une étude préclinique chez le lapin), ce qui place cette piste à un stade très précoce.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie d'Alzheimer (d'après les indications du graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Glaucome |
| Score de Prédiction TxGNN | 99,27 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Toutes les AMM sont annulées |
| Nombre d'AMM | 11 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances pharmacologiques générales, la rivastigmine est un inhibiteur de l'acétylcholinestérase et de la butyrylcholinestérase. Son efficacité dans la maladie d'Alzheimer repose sur l'augmentation de la transmission cholinergique.

Dans l'œil, une activité cholinergique accrue pourrait contribuer à abaisser la pression intraoculaire (PIO), en favorisant la contraction du muscle ciliaire et l'écoulement par le trabéculum. Ce mécanisme est comparable à celui des agents miotiques comme la pilocarpine et la physostigmine. Une étude chez le lapin normotendu a montré que la rivastigmine appliquée par voie topique réduisait la PIO, et une revue récente sur les agents cholinergiques et la PIO apporte un contexte mécanistique favorable.

Le score TxGNN très élevé (0,993) reste une prédiction informatique et ne constitue pas une preuve clinique. Aucune donnée humaine dans le glaucome n'a été identifiée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Préclinique (lapin) | J Ocul Pharmacol Ther | La rivastigmine topique, inhibiteur sélectif de l'acétylcholinestérase, abaisse la pression intraoculaire chez le lapin normotendu |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Revue / analyse de génétique des systèmes | Front Mol Biosci | Analyse du rôle du système cholinergique et des agents cholinergiques dans la réduction de la PIO ; les agonistes M3 existants sont limités par leurs effets cholinergiques systémiques |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Revue | Expert Opin Ther Pat | Revue des brevets sur les inhibiteurs et réactivateurs de l'acétylcholinestérase ; une inhibition modérée a un intérêt thérapeutique dans la maladie d'Alzheimer, la myasthénie et le glaucome |

---

## Informations de Marché en France

Toutes les AMM listées sont annulées ; aucune n'est actuellement valide. Le texte de l'indication approuvée n'est pas renseigné pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 61430397 | Rivastigmine EG Labo 9,5 mg/24 h | Patch transdermique | EG Labo |
| 66197477 | Rivastigmine Biogaran 9,5 mg/24 h | Dispositif transdermique | Biogaran |
| 64979294 | Rivastigmine Arrow 4,6 mg/24 h | Dispositif transdermique | Arrow Génériques |
| 61148412 | Rivastigmine Viatris 4,6 mg/24 h | Dispositif transdermique | Viatris Santé |
| 61322336 | Rivastigmine Biogaran 4,6 mg/24 h | Dispositif transdermique | Biogaran |

(5 AMM présentées sur 11, toutes annulées.)

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : épilepsie, maladies des ganglions de la base, dystonie focale de la main, blépharospasme, bronchopneumopathie chronique obstructive (dont forme sévère à début précoce), asthme (dont formes intrinsèque et allergique), maladies diarrhéiques, arrêt cardiaque soudain, maladies de la conduction cardiaque, anorexie mentale, ulcère peptique actif, obstruction des voies urinaires, maladie du sinus (dont forme familiale), syndromes parkinsoniens et maladie de Parkinson, bloc auriculo-ventriculaire.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les principales :
  - **Majeure** : bupropion.
  - **Modérées** : famotidine, ranitidine, cimétidine, hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, trospium, mépenzolate (anticholinergiques, avec risque d'antagonisme pharmacologique), lopéramide, métronidazole, clarithromycine, lévofloxacine, dolasétron, palonosétron, acide picosulfurique, polyéthylène glycol avec électrolytes, sulfate de sodium.

Les mises en garde et contre-indications issues de la notice française n'ont pas pu être consultées. Veuillez consulter la notice pour ces informations. Les effets systémiques cholinergiques (cardiaques, respiratoires, digestifs) sont particulièrement à considérer si une voie topique oculaire devait être explorée.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un score de modèle élevé et une seule étude animale (lapin), sans aucune donnée humaine dans le glaucome (niveau L4). De plus, le dépôt de sécurité issu de la notice est manquant, et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications, étape bloquante pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Confirmer l'effet sur la PIO dans des modèles animaux supplémentaires (notamment glaucome hypertensif) et évaluer la tolérance oculaire
- Évaluer la faisabilité d'une formulation oculaire topique, la formulation actuelle étant transdermique
- Comparer l'intérêt de la rivastigmine aux traitements du glaucome existants avant toute étude clinique de phase précoce
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

