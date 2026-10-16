---
layout: default
title: Iopromide
parent: Prédiction du modèle uniquement (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Iopromide : nouvelle indication prédite, Susceptibilité à l'arthrose (osteoarthritis susceptibility) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données compilées (les texte…"
monitor_inn: "IOPROMIDE"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "alopecia", "myosclerosis", "hemoglobinopathy", "pseudoachondroplasia"]
---

# Iopromide
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

# Iopromide : D'un produit de contraste iodé à l'arthrose (prédiction non étayée)

## Résumé en Une Phrase

Iopromide est un produit de contraste iodé non ionique, utilisé en imagerie diagnostique (commercialisé en France sous le nom ULTRAVIST).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **susceptibilité à l'arthrose**, mais cette prédiction repose uniquement sur un calcul de graphe.
Aucun essai clinique ni aucune publication ne la soutient actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données compilées (les textes d'indication des AMM sont vides) |
| Nouvelle Indication Prédite | Susceptibilité à l'arthrose (osteoarthritis susceptibility) |
| Score de Prédiction TxGNN | 99,57 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Iopromide est un produit de contraste radiographique iodé non ionique, destiné à l'imagerie diagnostique (y compris l'arthrographie). Il n'a pas d'activité pharmacologique connue sur le cartilage ou les voies articulaires.

La relation avec la nouvelle indication est donc très faible. La « susceptibilité à l'arthrose » est un trait de prédisposition génétique et non une maladie à traiter, ce qui réduit encore la plausibilité. Le score élevé (0,996) reflète vraisemblablement une proximité dans le graphe de connaissances, et non un effet thérapeutique.

Les autres prédictions du modèle vont dans le même sens : arthrose (99,53 %), polyarthrite rhumatoïde (99,37 %), brachyolmie, dysplasie acromésomélique de type Hunter-Thompson, syndrome brachyolmie-amélogenèse imparfaite, alopécie, myosclérose, hémoglobinopathie et pseudoachondroplasie. Aucune n'a de lien mécanistique identifié ni de preuve clinique. Pour les hémoglobinopathies, l'usage de produits de contraste iodés demande même de la prudence dans certaines situations (par exemple la drépanocytose).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68373358 | ULTRAVIST 300 (300 mg d'iode/mL), solution injectable | Solution injectable | Non renseignée (AMM annulée) |
| 62729413 | ULTRAVIST 370 (370 mg d'iode/mL), solution injectable | Solution injectable | Non renseignée (AMM annulée) |
| 65027575 | ULTRAVIST 370 (370 mg d'iode/mL), solution injectable en seringue préremplie pour injecteur automatique | Solution injectable | Non renseignée (AMM annulée) |
| 60385522 | ULTRAVIST 300 (300 mg d'iode/mL), solution injectable en seringue préremplie pour injecteur automatique | Solution injectable | Non renseignée (AMM annulée) |

Les quatre AMM, détenues par BAYER HEALTHCARE, sont annulées : aucune AMM valide n'est recensée.

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions ont été recensées. Parmi les principales, de niveau **majeur** : metformine, amphotéricine B (y compris formes lipidique, sulfate de cholestéryle et liposomale), mésalazine, balsalazide, olsalazine, sulfasalazine, vancomycine, kanamycine, néomycine, streptomycine et polymyxine B. Le mannitol est de niveau **modéré**. Plusieurs autres (clotrimazole, acide acétylsalicylique, bupropion, dexaméthasone, pantoprazole) sont de niveau inconnu.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est purement computationnelle (niveau L5), sans essai clinique, sans publication et sans mécanisme plausible. Les AMM françaises sont toutes annulées, et la notice n'a pas pu être exploitée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice (ANSM), actuellement manquantes et bloquantes pour le criblage de sécurité
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Justifier d'abord, sur le plan biologique, un lien entre un produit de contraste diagnostique et une action thérapeutique articulaire
- Réévaluer la pertinence d'une « susceptibilité » génétique comme indication traitable, ou privilégier une indication plus plausible (arthrose) avant tout travail supplémentaire
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

