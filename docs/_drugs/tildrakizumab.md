---
layout: default
title: Tildrakizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 762
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Tildrakizumab : nouvelle indication prédite, Rétinopathie diabétique non proliférante sévère (niveau de preuve L5). Indication d'origine : Non disponible dans les données compilées"
monitor_inn: "TILDRAKIZUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract", "drug-induced osteoporosis"]
---

# Tildrakizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

## Tildrakizumab : De l'indication d'origine non documentée à la rétinopathie diabétique non proliférante sévère
{: .text-alpha }

## Résumé en Une Phrase

Tildrakizumab est un anticorps monoclonal anti-IL-23 p19 (commercialisé sous le nom ILUMETRI). Les données compilées pour ce rapport ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **rétinopathie diabétique non proliférante sévère**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible dans les données compilées |
| Nouvelle Indication Prédite | Rétinopathie diabétique non proliférante sévère |
| Score de Prédiction TxGNN | 0,9963 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, tildrakizumab est un anticorps monoclonal dirigé contre la sous-unité p19 de l'IL-23, une cytokine de l'axe inflammatoire IL-23/IL-17.

Une inflammation chronique de bas grade, dont la signalisation de l'axe IL-23/IL-17, pourrait contribuer aux lésions vasculaires rétiniennes de la rétinopathie diabétique. Ce lien reste toutefois **hypothétique**. Le traitement de référence cible le VEGF et la vascularisation rétinienne, et non l'IL-23.

Le score élevé (0,9963) est une prédiction purement computationnelle. En l'absence d'essais, de publications et de données sur le mécanisme d'origine, il ne suffit pas à justifier la poursuite du projet.

### Autres indications prédites (pour information)

| Rang | Indication prédite | Score TxGNN | Niveau de preuve | Commentaire |
|---|---|---|---|---|
| 2 | Rétinopathie diabétique | 0,9953 | L5 | Même raisonnement que ci-dessus : rôle inflammatoire secondaire de l'axe IL-23/Th17, spéculatif. L'immunosuppression systémique chez des patients diabétiques exigerait une évaluation attentive du risque infectieux. |
| 3 | Cataracte diabétique | 0,9921 | L5 | Lien mécanistique faible (voie des polyols, stress osmotique et oxydatif). Un biomédicament serait peu plausible pour une affection traitée chirurgicalement. |
| 4 | Ostéoporose d'origine médicamenteuse | 0,9920 | L5 | L'axe IL-23/IL-17 influence l'ostéoclastogenèse, d'où un lien indirect plausible. Aucun effet protecteur osseux démontré. C'est la prédiction biologiquement la plus plausible, mais elle reste computationnelle. |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65992266 | ILUMETRI 200 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée (AMM active) |
| 69596271 | ILUMETRI 100 mg, solution injectable en seringue préremplie | Solution injectable | Non renseignée (AMM active) |
| 69150269 | ILUMETRI 100 mg, solution injectable en stylo prérempli | Solution injectable | Non renseignée (AMM active) |

Les trois AMM (titulaire : ALMIRALL, Espagne) sont valides ; le médicament est commercialisé.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité (mises en garde et contre-indications non disponibles dans les données compilées).

**Interactions médicamenteuses** : 78 interactions recensées. Parmi les principales :
- **Majeures** : adalimumab, baricitinib, certolizumab pegol, cladribine (risque d'immunosuppression cumulée)
- **Modérées** : roflumilast, tacrolimus, ciclosporine, azathioprine, alemtuzumab, anakinra, canakinumab, dénosumab, alefacept, ainsi que certains vaccins (anatoxine tétanique, vaccin charbonneux, vaccin cholérique vivant)
- **Mineures** : sels de zinc (sulfate, acétate, gluconate, chlorure)

Chez des patients diabétiques, une immunosuppression systémique nécessiterait une évaluation spécifique du risque infectieux.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Le lien mécanistique avec la rétinopathie diabétique est spéculatif, et les données de sécurité de la notice font défaut.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde, contre-indications, indications approuvées), élément bloquant pour le criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Mener une revue de la littérature préclinique sur le rôle de l'IL-23/IL-17 dans la rétinopathie diabétique
- Évaluer la compatibilité des voies d'administration (injectable systémique vs voies oculaires) et le profil de sécurité infectieuse chez les patients diabétiques
- Clarifier la situation réglementaire en France (AMM annulées)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

