---
layout: default
title: Bezlotoxumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bezlotoxumab : nouvelle indication prédite, Péritonite pelvienne aiguë de la femme (niveau de preuve L5). Indication d'origine : Colite à Clostridium difficile"
monitor_inn: "BEZLOTOXUMAB"
predicted_indications: ["acute female pelvic peritonitis", "embryonic cyst of fallopian tube", "tubal pregnancy", "salpingitis isthmica nodosa", "disease of uterine broad ligament", "lumbar spinal stenosis", "abdominal ectopic pregnancy", "abdominal cystic lymphangioma", "celiac trunk compression syndrome", "pelvic varices"]
---

# Bezlotoxumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Bezlotoxumab : De la colite à Clostridium difficile à la péritonite pelvienne aiguë de la femme

## Résumé en Une Phrase

Bezlotoxumab est un anticorps monoclonal initialement utilisé pour traiter les infections à *Clostridium difficile* (colite à *C. difficile*).
Le modèle TxGNN le prédit comme potentiellement efficace pour la **péritonite pelvienne aiguë de la femme**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Colite à *Clostridium difficile* (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Péritonite pelvienne aiguë de la femme |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les informations connues, bezlotoxumab est un anticorps monoclonal qui neutralise la toxine B de *C. difficile*. Son efficacité a été établie dans la prévention des récidives d'infection à *C. difficile*.

Aucun lien mécanistique clair avec la péritonite pelvienne n'a été identifié. Cette affection est généralement polymicrobienne et n'est pas médiée par la toxine B. Le score élevé (99,89 %) reflète vraisemblablement une proximité dans le graphe de connaissances plutôt qu'un fondement biologique.

Les autres candidats prédits (kyste embryonnaire de la trompe, grossesse tubaire, sténose lombaire, varices pelviennes, etc.) présentent le même profil : scores très élevés, mais aucun mécanisme plausible et aucune preuve clinique. Cela suggère des artéfacts de voisinage dans le graphe, notamment parmi les maladies de l'appareil reproducteur féminin.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69894104 | ZINPLAVA 25 mg/mL, solution à diluer pour perfusion (MERCK SHARP & DOHME, Pays-Bas) — annulée | Solution à diluer pour perfusion | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées pour ce rapport.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai, sans publication ni mécanisme plausible, et l'unique AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Mises en garde et contre-indications issues de la notice ANSM, nécessaires au dépistage de sécurité
- Preuve biologique d'un rôle de la toxine B (ou d'une cible apparentée) dans la péritonite pelvienne
- Données précliniques ou cliniques préliminaires, absentes à ce jour
- Vérification de la voie d'administration : la forme disponible est une perfusion intraveineuse, dont la compatibilité avec l'indication n'a pas été évaluée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

