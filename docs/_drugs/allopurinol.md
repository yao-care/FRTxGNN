---
layout: default
title: Allopurinol
parent: Prédiction du modèle uniquement (L5)
nav_order: 42
evidence_level: L5
indication_count: 10
monitor_inn: "ALLOPURINOL"
predicted_indications: ["hepatic porphyria", "primitive portal vein thrombosis", "idiopathic copper-associated cirrhosis", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "inflammatory myopathy with abundant macrophages"]
last_modified_at: 2026-10-28
description: "Allopurinol : nouvelle indication prédite, Porphyrie hépatique (hepatic porphyria) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Allopurinol
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

## Allopurinol : inhibiteur de la xanthine oxydase → Porphyrie hépatique (hepatic porphyria)
{: .text-alpha }

## Résumé en Une Phrase

L'allopurinol est un inhibiteur de la xanthine oxydase, utilisé de longue date en France sous forme de comprimés.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **porphyrie hépatique (hepatic porphyria)**,
mais seules **2 publications** indirectes (une hypothèse théorique et une étude chez le rat portant sur un autre médicament) sont associées, et **aucun essai clinique** n'a été enregistré.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Porphyrie hépatique (hepatic porphyria) |
| Score de Prédiction TxGNN | 0,9995 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'allopurinol est un inhibiteur de la xanthine oxydase, enzyme impliquée dans la production d'acide urique.

Le lien avec la porphyrie hépatique reste indirect et spéculatif. Une hypothèse publiée en 2019 propose de cibler l'enzyme 5-aminolévulinate synthase (ALAS1), enzyme limitante de la biosynthèse de l'hème, dans les porphyries aiguës. Cependant, rien n'établit que l'allopurinol agisse sur cette voie. Des données anciennes évoquent même un effet de l'allopurinol sur le renouvellement hépatique de l'hème et du cytochrome P450, ce qui pourrait constituer un risque théorique plutôt qu'un bénéfice chez les patients atteints de porphyrie.

Le score élevé du modèle reflète donc une proximité statistique dans les données d'apprentissage, et non une démonstration mécanistique ou clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune de ces publications n'étudie l'allopurinol chez des patients atteints de porphyrie.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothèse/Revue | Medical Hypotheses | Propose de cibler l'ALAS1 hépatique via le tryptophane ou l'inhibition de la tryptophane 2,3-dioxygénase comme piste thérapeutique des porphyries hépatiques aiguës |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Préclinique (animal) | Biochemical Pharmacology | Chez le rat, la carbamazépine à très faible dose perturbe le métabolisme de l'hème et aggrave les porphyries ; l'allopurinol n'est pas étudié |

## Informations de Marché en France

La liste ci-dessous peut être partielle. Le texte d'indication n'est pas renseigné dans les données locales.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63215258 | ALLOPURINOL SUN 300 mg, comprimé | comprimé | Non renseignée |
| 61060033 | ALLOPURINOL ZENTIVA 100 mg, comprimé | comprimé | Non renseignée |
| 66363543 | ALLOPURINOL SANDOZ 100 mg, comprimé | comprimé | Non renseignée |
| 64661021 | ALLOPURINOL ARROW LAB 100 mg, comprimé | comprimé | Non renseignée |
| 60470499 | ZYLORIC 300 mg, comprimé | comprimé | Non renseignée |

## Considérations de Sécurité

Les données issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité.

- **Interactions médicamenteuses** (100 interactions recensées ; principales) :
  - Modérées : hydroxyde d'aluminium, attapulgite, kaolin, magaldrate, sucralfate
  - Mineures : amoxicilline, chlorpropamide
  - Niveau non précisé : calcitriol, vitamine A, pantoprazole, glimépiride, mésalazine, doxycycline, métformine, oméprazole, morphine, entre autres
- **Points d'attention théoriques** : l'allopurinol pourrait interférer avec le métabolisme hépatique de l'hème, ce qui est préoccupant en cas de porphyrie. Il peut aussi être associé à des réactions d'hypersensibilité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle, sans essai clinique ni étude directe de l'allopurinol dans la porphyrie hépatique. Le mécanisme n'est pas établi et un risque théorique existe pour ces patients.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action et sur son lien éventuel avec la voie de l'hème
- Études précliniques évaluant l'effet de l'allopurinol sur l'ALAS1 et sur le métabolisme hépatique de l'hème
- Examen approfondi de la sécurité dans la porphyrie (notice ANSM, risque de crise porphyrique)
- Données cliniques ou observationnelles chez des patients atteints de porphyrie
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

