---
layout: default
title: Volanesorsen
parent: Prédiction du modèle uniquement (L5)
nav_order: 819
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Volanesorsen : nouvelle indication prédite, Anémie mégaloblastique (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "volanesorsen"
predicted_indications: ["megaloblastic anemia (disease)", "sclerosing cholangitis", "sickle cell disease and related diseases", "sickle cell-hemoglobin E disease syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "sickle cell-hemoglobin c disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "meningococcal infection", "paroxysmal nocturnal hemoglobinuria"]
---

# Volanesorsen
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

## Volanesorsen : De l'indication d'origine non documentée à l'anémie mégaloblastique (prédiction non étayée)
{: .text-alpha }

## Résumé en Une Phrase

Volanesorsen (WAYLIVRA 285 mg, solution injectable en seringue préremplie) est un oligonucléotide antisens ciblant l'ARNm de l'APOC3 pour réduire les triglycérides ; le texte d'indication de son AMM française n'est pas renseigné dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**anémie mégaloblastique**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Anémie mégaloblastique |
| Score de Prédiction TxGNN | 1,0000 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les informations connues, volanesorsen est un oligonucléotide antisens dirigé contre l'ARNm de l'APOC3, dont l'effet attendu est la baisse des triglycérides. Son indication d'origine n'a pas pu être extraite de l'AMM française.

Aucun lien mécanistique plausible n'a été identifié avec l'anémie mégaloblastique, qui est un trouble lié à une carence en vitamine B12 ou en folates. Le score élevé de TxGNN (1,0000) est une prédiction du modèle seule : elle n'est étayée ni par des essais ni par de la littérature.

Les autres prédictions du classement (cholangite sclérosante, syndromes drépanocytaires, infection à méningocoque, hémoglobinurie paroxystique nocturne) souffrent des mêmes limites : absence de justification mécanistique et de preuves. Les syndromes drépanocytaires partagent des scores identiques (0.9999), ce qui suggère un signal commun issu du modèle TxGNN (deep learning), pouvant refléter des similarités apprises par le modèle entre maladies apparentées, et non des preuves biologiques indépendantes.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65766872 (annulée) | WAYLIVRA 285 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée |

Titulaire : AKCEA THERAPEUTICS IRELAND (Irlande).

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : thrombopénie.

Veuillez consulter la notice pour les autres informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication ni justification mécanistique. L'AMM française est de plus annulée, et les données de sécurité de la notice sont manquantes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), ce qui est bloquant pour tout examen de sécurité
- Obtenir les données sur le mécanisme d'action (via DrugBank) pour analyser un éventuel lien mécanistique
- Identifier l'indication d'origine de l'AMM
- Rechercher des études précliniques ou observationnelles en faveur d'un lien avec l'anémie mégaloblastique, ou réorienter l'évaluation vers des indications plus plausibles
- Évaluer la compatibilité des voies d'administration, la thrombopénie étant déjà signalée comme contre-indication dans le graphe de connaissances
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

