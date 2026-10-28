---
layout: default
title: Aprepitant
parent: Prédiction du modèle uniquement (L5)
nav_order: 69
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Aprepitant : nouvelle indication prédite, Syndrome néphrogénique d'antidiurèse inappropriée (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées"
monitor_inn: "aprepitant"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "hypertrichosis (disease)", "pulmonary hypertension", "leprosy", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "kyphoscoliotic heart disease", "syndrome with a Dandy-Walker malformation as major feature", "subarachnoid hemorrhage (disease)", "isolated genetic hair shaft abnormality"]
---

# Aprepitant
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

## Aprépitant : D'une indication d'origine non documentée à la Néphropathie : syndrome néphrogénique d'antidiurèse inappropriée
{: .text-alpha }

## Résumé en Une Phrase

L'aprépitant est un antagoniste des récepteurs NK1 de la substance P. Les données compilées pour ce rapport ne précisent pas son indication d'origine dans les AMM françaises.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome néphrogénique d'antidiurèse inappropriée**, mais **aucun essai clinique** et **aucune publication pertinente** ne soutiennent actuellement cette prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Syndrome néphrogénique d'antidiurèse inappropriée |
| Score de Prédiction TxGNN | 0,9997 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | 20 (dont 20 annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, l'aprépitant est un antagoniste des récepteurs NK1 (substance P/neurokinine 1).

Le signal substance P/NK1 a été relié, dans des modèles précliniques, à la régulation de la vasopressine et de l'équilibre hydrique. Cela fournit un argument de plausibilité, mais celui-ci reste spéculatif.

Le syndrome néphrogénique d'antidiurèse inappropriée est causé par des mutations gain de fonction du récepteur V2 (AVPR2), qui agit en aval de la libération de vasopressine. Un antagonisme NK1 ne devrait donc pas corriger ce défaut. Le score TxGNN élevé est une prédiction purement computationnelle, sans appui clinique ni bibliographique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour cette indication.

---

## Informations de Marché en France

Les 20 AMM recensées sont annulées. Aucun texte d'indication approuvée n'est disponible dans les données compilées. Principales AMM (5 sur 20) :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 65314130 | Aprepitant Evolugen 125 mg et 80 mg | Gélule | Active |
| 60574505 | Emend 125 mg | Gélule | Active |
| 66256064 | Emend 80 mg | Gélule | Active |
| 64986762 | Aprepitant Viatris 125 mg | Gélule | Active |
| 65652406 | Aprepitant Arrow 125 mg | Gélule | Active |

---

## Considérations de Sécurité

- **Contre-indication issue du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique.
- **Interactions médicamenteuses** : 469 interactions recensées. Parmi celles listées :
  - **Majeures** : fentanyl, alfentanil, acalabrutinib.
  - **Modérées** : paclitaxel, abémaciclib, nifédipine, ibuprofène, lévonorgestrel, hydrocortisone, albendazole, fluvoxamine, fosamprénavir, fosphénytoïne, gefitinib, rabéprazole, lidocaïne, dihydrocodéine, entre autres.
  - **Mineure** : dolutégravir.

Les mises en garde et contre-indications de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

---

## Autres Prédictions Examinées

Les neuf autres prédictions du classement (hypertrichose, hypertension pulmonaire, lèpre, hypertrichose généralisée congénitale de type Ambras, syndrome malformatif à composante dentaire/parodontale, cardiopathie cyphoscoliotique, syndrome de Dandy-Walker, hémorragie sous-arachnoïdienne, anomalie génétique isolée de la tige pilaire) sont toutes de niveau L5, avec la recommandation Hold. Aucune n'a d'essai clinique. La seule publication associée (PMID 28261651, essai de phase I pazopanib + cisplatine dans les tumeurs solides) concerne l'hypertension pulmonaire et semble être une association erronée : elle n'apporte aucune preuve. L'hémorragie sous-arachnoïdienne est la plus plausible biologiquement (neuro-inflammation, barrière hémato-encéphalique), mais reste au mieux préclinique.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et le mécanisme du syndrome (mutation du récepteur V2) est incompatible avec un effet attendu d'un antagoniste NK1.
- 20 AMM françaises sont valides, et les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice auprès de l'ANSM (point bloquant pour le criblage de sécurité).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Réaliser une revue de littérature préclinique ciblée sur NK1, vasopressine et AVPR2.
- Clarifier l'indication d'origine et la situation réglementaire (annulation des AMM).
- Réévaluer d'autres indications plus plausibles (par exemple l'hémorragie sous-arachnoïdienne) avant tout investissement.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

