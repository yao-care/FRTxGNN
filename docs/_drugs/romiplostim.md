---
layout: default
title: Romiplostim
parent: Prédiction du modèle uniquement (L5)
nav_order: 678
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "ROMIPLOSTIM"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "platelet-type bleeding disorder", "autosomal dominant macrothrombocytopenia", "Ehlers-Danlos syndrome, fibronectinemic type"]
description: "Romiplostim : nouvelle indication prédite, Trouble de libération plaquettaire primaire (primary release disorder of platelets) (niveau de preuve L5). Indication d'origine : Non renseignée dans les do…"
---

# Romiplostim
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

## Romiplostim: Trouble de libération plaquettaire primaire (primary release disorder of platelets)
{: .text-alpha }

## Résumé en Une Phrase

Romiplostim est un agoniste du récepteur de la thrombopoïétine (MPL), initialement utilisé pour le traitement du purpura thrombopénique auto-immun (PTI) et de l'anémie aplasique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble de libération plaquettaire primaire**, mais cette prédiction ne repose actuellement que sur **0 essai clinique** et **1 publication** de nature mécanistique indirecte.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Trouble de libération plaquettaire primaire (primary release disorder of platelets) |
| Score de Prédiction TxGNN | 1.0000 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. D'après les connaissances pharmacologiques, romiplostim est un agoniste du récepteur de la thrombopoïétine (MPL) : il stimule la prolifération des mégacaryocytes et augmente la production de plaquettes. Son efficacité dans le PTI chronique est établie.

Le score est issu du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. Cependant, le mécanisme est ici peu convaincant : un trouble de libération plaquettaire est un défaut **fonctionnel** (sécrétion des granules), et non un déficit numérique. Augmenter le nombre de plaquettes ne corrigerait vraisemblablement pas ce défaut.

La seule publication disponible (PMID 25682608) porte sur l'inhibition, par des auto-anticorps, de la formation des proplaquettes dans le PTI. Elle soutient le mécanisme du PTI, et non celui de la nouvelle indication prédite.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Étude fondamentale/mécanistique | Haematologica | Dans le PTI, les auto-anticorps antiplaquettaires inhibent in vitro la formation des proplaquettes par les mégacaryocytes et altèrent la production plaquettaire. Lien indirect avec l'indication prédite. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64313253 | NPLATE 250 microgrammes, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Non renseignée (AMM active) |
| 66384249 | NPLATE 125 microgrammes, poudre pour solution injectable | Poudre pour solution injectable | Non renseignée (AMM active) |
| 68638461 | NPLATE 500 microgrammes, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Non renseignée (AMM active) |

## Considérations de Sécurité

- **Interactions médicamenteuses** :
  - **Carfilzomib** : interaction de niveau **majeur** (source : DDInter).
  - Cible pharmacologique : récepteur de la thrombopoïétine (MPL), ce qui correspond à son mécanisme d'agoniste et non à une interaction cliniquement évaluée.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un score élevé du modèle TxGNN (apprentissage profond), mais le niveau de preuve est faible (L4) : aucun essai clinique, une seule étude mécanistique indirecte. Le défaut est fonctionnel, donc l'augmentation du nombre de plaquettes est peu susceptible d'être bénéfique. Par ailleurs, le médicament est commercialisé en France (3 AMM valides sur 3).

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action et sa pertinence pour un défaut fonctionnel plaquettaire.
- Notice de l'ANSM (mises en garde et contre-indications), indispensable avant toute évaluation de sécurité.
- Données précliniques ou cliniques spécifiques au trouble de libération plaquettaire.
- Clarification de la situation réglementaire (AMM annulées) et de la disponibilité du produit en France.

**Note complémentaire :** parmi les autres indications prédites, la thrombopénie alloimmune fœto-néonatale (niveau L4, « question de recherche »), les thrombopénies constitutionnelles et les macrothrombopénies autosomiques dominantes sont mécanistiquement plus plausibles, car il s'agit de déficits quantitatifs en plaquettes. Les preuves restent toutefois indirectes (principalement issues du PTI) ou inexistantes, et la sécurité pendant la grossesse reste à établir.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

