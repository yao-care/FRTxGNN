---
layout: default
title: Lanreotide
parent: Prédiction du modèle uniquement (L5)
nav_order: 435
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Lanreotide : nouvelle indication prédite, Hypertrichose (niveau de preuve L5). Indication d'origine : Acromégalie"
monitor_inn: "lanreotide"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "Ambras type hypertrichosis universalis congenita"]
---

# Lanreotide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Lanréotide : De l'Acromégalie à l'Hypertrichose

## Résumé en Une Phrase

La lanréotide est un analogue de la somatostatine, initialement utilisé pour le traitement de l'acromégalie (ainsi que de l'hyperpituitarisme et du gigantisme hypophysaire).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypertrichose**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction, qui reste purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Acromégalie (texte d'indication des AMM non renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Hypertrichose |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Toutes les AMM sont annulées |
| Nombre d'AMM | 6 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la lanréotide fait partie des analogues de la somatostatine ; elle agit sur les récepteurs SSTR2 et SSTR5 pour freiner la sécrétion de l'hormone de croissance (GH) et de l'IGF-1, ce qui explique son efficacité dans l'acromégalie.

Un lien spéculatif pourrait exister : une baisse de la signalisation GH/IGF-1 pourrait influencer la croissance du follicule pileux. Toutefois, cette hypothèse n'est étayée par aucune donnée compilée pour ce rapport. Il faut aussi noter que l'hypertrichose est un effet indésirable connu de certains médicaments : l'association prédite reflète peut-être la topologie du graphe de connaissances plutôt qu'un bénéfice thérapeutique réel.

**Autres prédictions du modèle (toutes de niveau L5, sans aucune preuve clinique ni bibliographique) :**

| Rang | Maladie prédite | Score TxGNN |
|------|------|------|
| 2 | Syndrome malformatif avec atteinte dentaire et/ou parodontale | 99,96 % |
| 3 | Syndrome avec malformation de Dandy-Walker comme caractéristique majeure | 99,96 % |
| 4 | Anomalie génétique isolée de la tige pilaire | 99,96 % |
| 5 | Hypertrichose universelle congénitale de type Ambras | 99,96 % |

Pour ces prédictions, aucune voie mécanistique plausible n'a pu être établie à partir des données disponibles. Il s'agit probablement d'associations liées à des nœuds géniques ou phénotypiques partagés dans le graphe.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 6 AMM recensées sont toutes annulées ; aucune n'est actuellement valide. Le texte de l'indication approuvée n'est pas renseigné pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 61748503 | MYRELEZ L.P. 60 mg | Solution injectable à libération prolongée (seringue préremplie) | AMDIPHARM |
| 61670321 | MYRELEZ L.P. 120 mg | Solution injectable à libération prolongée (seringue préremplie) | AMDIPHARM |
| 63871159 | SOMATULINE L.P. 90 mg | Solution injectable à libération prolongée (seringue préremplie) | IPSEN PHARMA |
| 63787825 | SOMATULINE L.P. 120 mg | Solution injectable à libération prolongée (seringue préremplie) | IPSEN PHARMA |
| 68758076 | SOMATULINE L.P. 60 mg | Solution injectable à libération prolongée (seringue préremplie) | IPSEN PHARMA |

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

- **Affections associées à une contre-indication dans le graphe de connaissances** (et non issues du texte de la notice) : hypertension, maladie hépatique, maladie de la vésicule biliaire (dont lithiase biliaire, cholécystolithiase, choledocholithiase), hyperglycémie, hypoglycémie, hypothyroïdie (dont myxœdème et hypothyroïdie congénitale), insuffisance rénale.
- **Interactions médicamenteuses** : 136 interactions recensées. Les 20 premières, toutes de niveau modéré, concernent surtout les antidiabétiques : acarbose, albiglutide, alogliptine, metformine, pioglitazone, canagliflozine, chlorpropamide, dapagliflozine, dulaglutide, empagliflozine, linagliptine, glimépiride, sémaglutide, ainsi que plusieurs insulines (asparte, dégludec, détémir, glargine, glulisine, isophane, régulière). Cela impose une surveillance de la glycémie en cas d'association.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication, avec un mécanisme peu plausible. De plus, toutes les AMM françaises sont annulées et les données de sécurité de la notice font défaut, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice ANSM (mises en garde et contre-indications)
- Données détaillées sur le mécanisme d'action (via DrugBank)
- Recherche ciblée d'études précliniques ou de cas cliniques sur la lanréotide et l'hypertrichose
- Clarification du statut réglementaire en France (AMM annulées) et de la disponibilité du produit
- Évaluation de la compatibilité des voies d'administration pour la nouvelle indication
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

