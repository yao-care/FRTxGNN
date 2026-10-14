---
layout: default
title: Benzocaine
parent: Prédiction du modèle uniquement (L5)
nav_order: 97
evidence_level: L5
indication_count: 1
---

# Benzocaine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Benzocaïne : Des Mycoses et Dermatites à la Conjonctivite Papillaire

## Résumé en Une Phrase

La benzocaïne est un anesthésique local de type ester, utilisé à l'origine pour soulager les symptômes de pathologies cutanées et pharyngées (dermatite, pharyngite, mycoses cutanées comme le pied d'athlète).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **conjonctivite papillaire**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM (le graphe de connaissances mentionne : pied d'athlète, dermatite, pharyngite, teigne du corps) |
| Nouvelle Indication Prédite | Conjonctivite papillaire |
| Score de Prédiction TxGNN | 99,38 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la benzocaïne est un anesthésique local topique de type ester qui bloque les canaux sodiques voltage-dépendants. Cela pourrait théoriquement soulager l'inconfort ou les démangeaisons de la surface oculaire.

La conjonctivite papillaire est le plus souvent due à une allergie ou à une irritation mécanique (port de lentilles de contact, prothèses oculaires, fils de suture exposés). C'est un processus à médiation immunitaire, que le blocage des canaux sodiques ne traite pas. La prédiction reflète probablement la proximité dans le réseau de connaissances avec des indications existantes (dermatite, pharyngite : soulagement symptomatique de l'irritation et de la douleur) plutôt qu'un véritable lien modificateur de la maladie.

Le score très élevé (0,994) ne doit donc pas être interprété comme une preuve d'efficacité : en l'absence de données sur le mécanisme d'action, aucune vérification mécanistique croisée n'est possible.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66400454 | SEDORRHOIDE CRISE HEMORROIDAIRE, crème rectale (annulée) | Crème | Non renseignée |
| 66426495 | SEDORRHOIDE CRISE HEMORROIDAIRE, suppositoire (annulée) | Suppositoire | Non renseignée |
| 64835493 | TRUE TEST 36, patch pour test épicutané (annulée) | Patch | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : insuffisance hépatique, maladie hépatique, encéphalopathie hépatique, coma hépatique, maladie rénale, épilepsie, troubles anxieux, porphyries, thrombopénie, neutropénie, agranulocytose, diabète et acidocétose diabétique, trouble de la coagulation, hyperparathyroïdie, hypercalcémie, néphrocalcinose, sarcoïdose, gastrite, maladie de la vésicule biliaire, herpès, abus/dépendance de substances, entre autres. Ces éléments sont indicatifs et doivent être vérifiés avec la notice officielle.
- **Risque spécifique à l'usage oculaire** : les anesthésiques topiques peuvent provoquer une toxicité cornéenne en cas d'utilisation répétée, et la benzocaïne n'est pas formulée pour un usage ophtalmique.
- **Interactions médicamenteuses** : aucune interaction retrouvée, ce qui peut refléter un manque de données plutôt qu'une absence réelle d'interactions.

Veuillez consulter la notice pour les informations de sécurité complètes (mises en garde et contre-indications officielles non disponibles).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Le lien mécanistique est faible pour une pathologie à composante immunitaire, l'usage oculaire pose un risque de toxicité cornéenne, et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications), actuellement bloquant pour le criblage de sécurité
- Obtenir les données sur le mécanisme d'action (via DrugBank)
- Rechercher des études précliniques ou cliniques sur l'usage oculaire de la benzocaïne dans la conjonctivite papillaire
- Évaluer la compatibilité de voie d'administration et de formulation (aucune forme ophtalmique disponible)
- Confirmer l'absence réelle d'interactions médicamenteuses
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

