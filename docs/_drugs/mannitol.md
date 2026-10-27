---
layout: default
title: Mannitol
parent: Prédiction du modèle uniquement (L5)
nav_order: 472
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Mannitol : nouvelle indication prédite, Syndrome néphrogénique d'antidiurèse inappropriée (niveau de preuve L5). Indication d'origine : Œdème cérébral, hypertension intracrânienne, hypertension ocula…"
monitor_inn: "MANNITOL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "malignant hyperthermia, susceptibility to", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "nephrogenic diabetes insipidus", "central core myopathy"]
---

# Mannitol
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

## Mannitol : Du Œdème Cérébral au Syndrome Néphrogénique d'Antidiurèse Inappropriée
{: .text-alpha }

## Résumé en Une Phrase

Le mannitol est un agent osmotique, initialement utilisé pour le traitement de l'œdème cérébral, de l'hypertension intracrânienne et de l'hypertension oculaire.
Le modèle TxGNN le prédit comme potentiellement efficace pour le **syndrome néphrogénique d'antidiurèse inappropriée**, mais **aucun essai clinique** n'est enregistré et seule **1 publication** (une revue générale sur l'hyponatrémie, sans donnée propre au mannitol) est associée à cette prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Œdème cérébral, hypertension intracrânienne, hypertension oculaire (données du graphe de connaissances ; aucun texte d'indication d'AMM disponible) |
| Nouvelle Indication Prédite | Syndrome néphrogénique d'antidiurèse inappropriée |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 9 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le mannitol est un agent osmotique qui favorise la diurèse hydrique et pourrait, en théorie, faire augmenter la natrémie.

Cependant, le syndrome néphrogénique d'antidiurèse inappropriée est causé par des mutations avec gain de fonction du récepteur V2 de la vasopressine (AVPR2). Le mannitol n'agit pas sur cette voie. La seule publication associée est une revue générale sur les pièges de l'évaluation de l'hyponatrémie, qui ne contient aucune donnée spécifique au mannitol.

Le score TxGNN élevé reflète donc une prédiction du modèle, et non un signal thérapeutique étayé. Le lien mécanistique est faible.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Revue | European Journal of Internal Medicine | Dix pièges courants dans l'évaluation de l'hyponatrémie ; aucune donnée spécifique au mannitol |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62126714 | MANNITOL 10 % AGUETTANT | Solution pour perfusion | Non renseignée (AMM annulée) |
| 68274328 | MANNITOL B. BRAUN 10 POUR CENT | Solution pour perfusion | Non renseignée (AMM annulée) |
| 66972245 | MANNITOL LAVOISIER 20 POUR CENT | Solution pour perfusion | Non renseignée (AMM annulée) |
| 62093602 | MANNITOL 20 POUR CENT B. BRAUN | Solution injectable hypertonique pour perfusion | Non renseignée (AMM annulée) |
| 69361469 | MANNITOL BIOSEDRA 10 POUR CENT | Solution pour perfusion | Non renseignée (AMM annulée) |

Au total, 9 AMM sont recensées, toutes annulées ; seules les 5 premières sont présentées ici.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : insuffisance hépatique, maladie hépatique, encéphalopathie et coma hépatiques, anurie, altération de la fonction rénale, œdème pulmonaire, hémorragie intracrânienne, porphyries, thrombopénie, neutropénie, agranulocytose, anémies, syndromes d'apnée du sommeil, maladies de la vésicule biliaire, troubles liés à l'usage de substances et troubles anxieux ou névrotiques.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les principales :
  - Majeure : amikacine.
  - Modérées : lamivudine, formotérol, salbutamol, arformotérol, amifostine, bénazépril, captopril, canagliflozine, dapagliflozine, carbamazépine, cisatracurium, citalopram, desvenlafaxine, bisacodyl, acide picosulfurique, polyéthylène glycol, acide iothalamique, diatrizoate.
  - Mineure : doxycycline.
- **Point d'attention propre à la prédiction** : en raison de son effet diurétique osmotique, le mannitol pourrait aggraver la polyurie et la perte d'eau libre dans certaines pathologies, et provoquer une surcharge volémique ou un œdème pulmonaire.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucun essai clinique, une seule revue générale sans lien direct avec le mannitol, et un mécanisme d'action incompatible avec la physiopathologie (mutations activatrices d'AVPR2).
- Toutes les AMM françaises sont annulées, et les données de sécurité officielles sont manquantes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA) du mannitol
- Mises en garde et contre-indications issues de la notice de l'ANSM
- Preuves précliniques ou cliniques directes de l'effet du mannitol sur cette pathologie
- Évaluation de l'intérêt de poursuivre, au vu de l'absence de lien mécanistique plausible

**Remarque sur les autres prédictions :** les neuf autres indications prédites (cœur pulmonaire aigu, hyperthermie maligne, paralysies périodiques, myopathies à cores, diabète insipide néphrogénique) sont également en Hold. Plusieurs associations semblent provenir du rôle du mannitol comme excipient (par exemple dans les formulations de dantrolène) plutôt que d'un effet thérapeutique. Pour le diabète insipide néphrogénique, le mannitol est même mécanistiquement contre-indiqué.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

