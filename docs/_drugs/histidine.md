---
layout: default
title: Histidine
parent: Prédiction du modèle uniquement (L5)
nav_order: 380
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Histidine : nouvelle indication prédite, Gastroparésie (niveau de preuve L5). Indication d'origine : Non précisée dans les données compilées (les textes d'indication des…"
monitor_inn: "HISTIDINE"
predicted_indications: ["gastroparesis (disease)", "sclerosing cholangitis"]
---

# Histidine
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

## Histidine : Des Usages Nutritionnels et de Conservation d'Organes à la Gastroparésie
{: .text-alpha }

## Résumé en Une Phrase

L'histidine est un acide aminé présent dans de nombreuses solutions de nutrition parentérale et de conservation d'organes, dont les autorisations françaises sont aujourd'hui toutes annulées.
Le modèle TxGNN la prédit comme potentiellement efficace pour la **gastroparésie**, mais **aucun essai clinique** et **une seule publication** (sans lien direct avec l'histidine) soutiennent cette piste.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données compilées (les textes d'indication des AMM sont vides) |
| Nouvelle Indication Prédite | Gastroparésie |
| Score de Prédiction TxGNN | 0,9955 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 19) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'histidine fait partie des acides aminés entrant dans des solutions de nutrition parentérale, de dialyse péritonéale et de conservation d'organes. Aucune indication originale n'est documentée dans les données compilées.

La prédiction repose presque exclusivement sur le score du modèle TxGNN (0,9955). La seule publication retrouvée (PMID 42668409, 2026) porte sur la pathologie amyloïde gastrique et la dénervation de la muqueuse dans l'amylose ATTRv. Elle ne teste pas l'histidine et ne décrit aucun mécanisme lié à l'histidine pour la gastroparésie.

Aucun mécanisme plausible par lequel l'histidine améliorerait la motricité gastrique n'est étayé par les données disponibles. La prédiction doit donc être considérée comme une hypothèse purement computationnelle.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [42668409](https://pubmed.ncbi.nlm.nih.gov/42668409/) | 2026 | Étude mécanistique/pathologique (patients et modèles murins) | Amyloid | Pathologie amyloïde gastrique et dénervation muqueuse dans l'amylose ATTRv avec polyneuropathie ; l'histidine n'est pas étudiée |

---

## Informations de Marché en France

Le médicament est commercialisé en France, avec 19 AMM valides. Les textes d'indication approuvée ne sont pas renseignés dans les données compilées. Cinq AMM sur 20 sont listées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68491709 | PERISOC, solution de cardioplégie/solution pour conservation d'organe | Solution cardioplégique | Non renseignée |
| 65635346 | CELSIOR, solution pour conservation d'organes | Solution | Non renseignée |
| 66534581 | KETOSTERIL, comprimé enrobé | Comprimé enrobé | Non renseignée |
| 61960303 | AMINOVEN 10 POUR CENT, solution pour perfusion | Solution pour perfusion | Non renseignée |
| 69667989 | AMINOVEN 5 POUR CENT, solution pour perfusion | Solution pour perfusion | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues d'une notice)** : maladie rénale (dont insuffisance rénale chronique et terminale), maladies cardiaques et cardiovasculaires, hypercalcémie (dont hypercalcémie humorale des tumeurs malignes), sarcoïdose, néphrocalcinose, lithiase rénale, néphropathie uratique aiguë, troubles du métabolisme du phosphore, intoxication digitalique, fibrillation ventriculaire, phénylcétonurie et troubles du métabolisme de la phénylalanine.

Aucune donnée d'interaction médicamenteuse n'a été trouvée. Pour les mises en garde officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni mécanisme plausible. Les données de sécurité officielles manquent, et le médicament est commercialisé en France avec 19 AMM valides.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Identifier un lien mécanistique entre l'histidine et la motricité gastrique
- Clarifier les indications originales des AMM annulées

---

## Piste Secondaire : Cholangite Sclérosante (Question de Recherche)

La deuxième indication prédite, la **cholangite sclérosante** (score 0,9927, niveau L4), est étayée par des études précliniques indirectes. L'histidine est le substrat de l'histidine décarboxylase, qui produit l'histamine. Or l'histamine dérivée des mastocytes favorise la prolifération biliaire et la fibrose dans les modèles murins (PMID 27351144, 35799467). La suppression de l'histidine décarboxylase (PMID 32054995) ou le blocage des récepteurs H1/H2 (PMID 29601088) réduit les lésions.

L'effet attendu d'un apport en histidine est donc **incertain, voire défavorable** : les données soutiennent l'inhibition de la voie de l'histamine, non l'administration d'histidine. Aucun essai clinique n'existe. Cette piste reste une question de recherche et non une recommandation de développement.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

