---
layout: default
title: Ziconotide
parent: Preuves modérées (L3-L4)
nav_order: 338
evidence_level: L4
indication_count: 10
---

# Ziconotide
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
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

# Ziconotide : De la douleur chronique sévère à la migraine

## Résumé en Une Phrase

Le ziconotide est un analgésique administré par voie intrathécale, utilisé à l'origine dans la douleur chronique sévère.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **migraine (« migraine disorder »)**.
Cette prédiction ne repose aujourd'hui que sur **1 rapport de cas** publié, sans **aucun essai clinique** enregistré.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Douleur chronique sévère (le texte d'indication de l'AMM n'est pas renseigné dans les données ; cette indication est déduite du dossier de preuves) |
| Nouvelle Indication Prédite | Migraine (migraine disorder) |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de référence. D'après les informations connues, le ziconotide est un bloqueur des canaux calciques de type N (Cav2.2). Il réduit la libération de neurotransmetteurs impliqués dans la nociception (substance P, CGRP) au niveau de la corne dorsale de la moelle épinière.

La signalisation trigémino-vasculaire de la migraine pourrait emprunter des voies proches. Cela explique que le graphe de connaissances rapproche la douleur chronique sévère de la migraine.

Cette hypothèse reste théorique. La seule preuve clinique est un cas isolé, et plusieurs freins limitent la faisabilité :
- la voie intrathécale est invasive ;
- l'avertissement encadré (boxed warning) signale des effets indésirables psychiatriques et neurologiques ;
- il existe des traitements de la migraine moins invasifs.

Cette piste ne mérite d'être formulée comme question de recherche que pour des cas réfractaires.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26392785](https://pubmed.ncbi.nlm.nih.gov/26392785/) | 2015 | Rapport de cas | Journal of Pain Research | Résolution de céphalées migraineuses chroniques après traitement par ziconotide intrathécal chez un patient |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66495139 | PRIALT 100 microgrammes/ml, solution pour perfusion (ESTEVE PHARMACEUTICALS, Allemagne) | Solution pour perfusion | Non renseignée dans les données |

## Considérations de Sécurité

- **Mises en Garde Principales** : le dossier de preuves signale un avertissement encadré (boxed warning) pour des effets indésirables psychiatriques et neurologiques. Il mentionne aussi un risque d'hypotension, qui pose problème pour tout usage systémique.

Le texte détaillé des mises en garde, des contre-indications et des interactions de la notice ANSM n'est pas disponible. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La preuve se limite à un rapport de cas (niveau L4), sans essai clinique. Le profil de sécurité de la voie intrathécale et l'absence de la notice ANSM bloquent le passage à l'étape de criblage de sécurité.
- Les autres prédictions (migraine avec aura du tronc cérébral, syndrome de la queue de cheval, obésité, accident ischémique transitoire, glaucomes, prééclampsie, etc.) reposent sur des données encore plus faibles. Elles sont classées L4 ou L5 et restent en Hold.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), qui constitue une lacune bloquante.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Évaluer la compatibilité de la voie d'administration, en particulier l'acceptabilité de la voie intrathécale pour la migraine.
- Rechercher d'autres cas ou études observationnelles dans la migraine réfractaire, avant d'envisager un essai exploratoire.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

