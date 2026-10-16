---
layout: default
title: Allopurinol
parent: Preuves modérées (L3-L4)
nav_order: 42
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Allopurinol : nouvelle indication prédite, Porphyrie hépatique (niveau de preuve L4). Indication d'origine : Goutte"
---

# Allopurinol
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

# Allopurinol : De la goutte à la porphyrie hépatique

## Résumé en Une Phrase

Allopurinol est un inhibiteur de la xanthine oxydase, initialement utilisé pour traiter la goutte, l'hyperuricémie et la néphropathie aiguë à l'urate.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **porphyrie hépatique**, mais cette prédiction ne repose que sur **2 publications** indirectes (une hypothèse théorique et une étude animale portant sur un autre médicament) et **aucun essai clinique**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Goutte (le texte d'indication des AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Porphyrie hépatique |
| Score de Prédiction TxGNN | 99,95 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'allopurinol est un inhibiteur de la xanthine oxydase, dont l'efficacité dans la goutte et l'hyperuricémie est établie par l'usage clinique.

Le lien mécanistique avec la porphyrie hépatique est **indirect et spéculatif**. Un article d'hypothèse de 2019 propose de cibler l'enzyme 5-aminolévulinate synthase (ALAS1) en modulant l'utilisation de l'hème, mais il ne porte pas sur l'allopurinol. L'étude de 1992 chez le rat concerne la carbamazépine, qui aggrave les porphyries. Aucun mécanisme établi ne relie l'inhibition de la xanthine oxydase au contrôle de la biosynthèse de l'hème.

De plus, des données anciennes décrivent un effet de l'allopurinol sur le renouvellement de l'hème hépatique et du cytochrome P450. Cela pourrait constituer une préoccupation de sécurité dans la porphyrie plutôt qu'un bénéfice. Le score élevé du modèle doit donc être interprété avec une grande prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothèse/Revue | Medical Hypotheses | Propose de cibler l'ALAS1 hépatique via le tryptophane ou l'inhibition de la tryptophane 2,3-dioxygénase comme piste thérapeutique dans les porphyries hépatiques aiguës ; n'étudie pas l'allopurinol |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Préclinique (animal) | Biochemical Pharmacology | Effets de la carbamazépine sur le métabolisme de l'hème dans le foie de rat, en lien avec l'aggravation des porphyries ; ne concerne pas l'allopurinol |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63215258 | ALLOPURINOL SUN 300 mg, comprimé | Comprimé | Non renseignée (AMM annulée) |
| 61060033 | ALLOPURINOL ZENTIVA 100 mg, comprimé | Comprimé | Non renseignée (AMM annulée) |
| 66363543 | ALLOPURINOL SANDOZ 100 mg, comprimé | Comprimé | Non renseignée (AMM annulée) |
| 64661021 | ALLOPURINOL ARROW LAB 100 mg, comprimé | Comprimé | Non renseignée (AMM annulée) |
| 60470499 | ZYLORIC 300 mg, comprimé | Comprimé | Non renseignée (AMM annulée) |

Les 20 AMM recensées sont annulées ; aucune AMM valide n'a été identifiée dans les données compilées pour ce rapport.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie hépatique, maladie de la vésicule biliaire, insuffisance rénale, vascularite d'hypersensibilité, angéite leucocytoclasique cutanée, vascularite cutanée allergique, maladie des anticorps anti-membrane basale glomérulaire.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi celles de niveau modéré : hydroxyde d'aluminium, attapulgite, kaolin, magaldrate, sucralfate. De niveau mineur : amoxicilline, chlorpropamide. Plusieurs autres (pantoprazole, metformine, oméprazole, doxycycline, morphine, etc.) sont de niveau non précisé.
- **Point d'attention propre à l'indication** : la maladie hépatique figure parmi les contre-indications du graphe, et un effet de l'allopurinol sur le métabolisme de l'hème hépatique a été décrit ; une évaluation de sécurité spécifique à la porphyrie serait indispensable.

Veuillez consulter la notice pour les mises en garde officielles, qui n'ont pas pu être intégrées aux données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur un score de modèle élevé, mais les seules publications disponibles ne concernent pas l'allopurinol dans la porphyrie, et aucun essai clinique n'existe. Le lien mécanistique est spéculatif et un risque théorique de sécurité existe.
- Les 20 AMM françaises sont toutes annulées, ce qui complique tout développement local.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action de l'allopurinol (non disponibles)
- Mises en garde et contre-indications de la notice ANSM (non récupérées)
- Études précliniques directes de l'allopurinol sur le métabolisme de l'hème et l'ALAS1
- Évaluation du risque de déclenchement de crises de porphyrie
- Clarification du statut réglementaire actuel du produit en France

**Note sur les autres prédictions :** les neuf autres indications prédites (thrombose portale primitive, cirrhose associée au cuivre, sclérose hépatoportale, hypertension portale familiale non cirrhotique, syndrome hépatopulmonaire, trouble du métabolisme de la phénylalanine, myopathie nécrosante à médiation immunitaire, syndrome des antisynthétases, myopathie inflammatoire à macrophages abondants) sont de niveau L5, sans preuve clinique ni mécanisme étayé, et sont également en Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

