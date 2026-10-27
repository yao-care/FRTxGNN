---
layout: default
title: Imiglucerase
parent: Preuves modérées (L3-L4)
nav_order: 392
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Imiglucerase : nouvelle indication prédite, Syndrome de Hurler (niveau de preuve L4). Indication d'origine : Maladie de Gaucher"
monitor_inn: "imiglucerase"
predicted_indications: ["Hurler syndrome", "Scheie syndrome", "benign neoplasm of adrenal gland", "autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease"]
---

# Imiglucerase
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **5** 
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

## Imiglucérase : De la maladie de Gaucher au syndrome de Hurler
{: .text-alpha }

## Résumé en Une Phrase

L'imiglucérase est une enzyme recombinante (bêta-glucocérébrosidase), initialement utilisée pour le traitement de la maladie de Gaucher.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome de Hurler**, mais **aucun essai clinique** et **une seule publication** (une revue générale sur les thérapies enzymatiques substitutives) existent actuellement pour cette direction.
Il s'agit d'une prédiction purement computationnelle, sans soutien clinique réel.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Gaucher (source : graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Syndrome de Hurler |
| Score de Prédiction TxGNN | 99,52 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'imiglucérase est une bêta-glucocérébrosidase (GBA1) recombinante qui hydrolyse le glucosylcéramide ; son efficacité dans la maladie de Gaucher est établie.

Le syndrome de Hurler (MPS I) est causé par un déficit en alpha-L-iduronidase, entraînant l'accumulation de glycosaminoglycanes (sulfate de dermatane et d'héparane). Il s'agit d'une enzyme et de substrats différents : une substitution enzymatique directe n'est donc **pas plausible mécanistiquement**. Une accumulation secondaire de glycolipides (gangliosides GM2/GM3) existe dans les MPS, mais rien n'indique que l'apport de glucocérébrosidase la corrige.

Le score élevé (0,995) reflète vraisemblablement la proximité des deux maladies dans le réseau des maladies de surcharge lysosomale plutôt qu'un véritable lien fonctionnel. Le traitement spécifique approuvé est la laronidase.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Revue | La Revue de médecine interne | Revue générale des thérapies enzymatiques substitutives dans les maladies de surcharge lysosomale (Gaucher, Fabry, etc.) ; contexte indirect uniquement, sans données propres au syndrome de Hurler |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62616337 | CEREZYME 400 U, poudre pour solution à diluer pour perfusion (SANOFI, Pays-Bas) | Poudre pour solution à diluer pour perfusion | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : une interaction de niveau **modéré** est rapportée avec le **miglustat** (source : DDInter).

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (score élevé) sans essai clinique ni donnée spécifique ; l'imiglucérase et le syndrome de Hurler impliquent des enzymes et des substrats différents, et un traitement spécifique (laronidase) existe déjà. De plus, l'unique AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications de la notice ANSM (bloquant pour le criblage de sécurité)
- Données détaillées sur le mécanisme d'action (via DrugBank)
- Données précliniques démontrant un effet de l'imiglucérase sur l'accumulation de substrats dans la MPS I
- Éléments de compatibilité de voie d'administration et de similarité avec l'indication d'origine

---

*Note : les autres prédictions du modèle (syndrome de Scheie, néoplasme bénin de la surrénale, syndrome ichtyosique autosomique à évolution fatale, maladie de stockage des esters de cholestéryle) présentent un niveau de preuve L4 à L5, sans essai clinique, et sont également en statut Hold.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

