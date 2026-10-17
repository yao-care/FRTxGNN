---
layout: default
title: Relebactam
parent: Prédiction du modèle uniquement (L5)
nav_order: 658
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Relebactam : nouvelle indication prédite, Hyperamylasémie (niveau de preuve L5). Indication d'origine : Infection urinaire, pyélonéphrite"
monitor_inn: "relebactam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia"]
---

# Relebactam
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Relebactam : Des Infections Urinaires à l'Hyperamylasémie

## Résumé en Une Phrase

Le relebactam est un inhibiteur de bêta-lactamases, utilisé uniquement en association avec l'imipénème/cilastatine, initialement indiqué dans les infections urinaires et la pyélonéphrite.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hyperamylasémie**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection urinaire, pyélonéphrite (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Hyperamylasémie |
| Score de Prédiction TxGNN | 99,22 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Annulée uniquement (AMM annulée) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le relebactam est un inhibiteur de bêta-lactamases de type diazabicyclooctane, sans activité antibactérienne propre. Il protège l'imipénème contre les bêta-lactamases de classes A et C, ce qui explique son utilité dans les infections urinaires compliquées et la pyélonéphrite.

**En réalité, cette prédiction n'est pas étayée mécanistiquement.** L'hyperamylasémie est une anomalie biologique, souvent liée à une atteinte pancréatique ou des glandes salivaires. Aucune voie plausible ne relie l'inhibition des bêta-lactamases bactériennes à son traitement.

Le score élevé (0,992) provient du graphe de connaissances et ne s'appuie sur aucune preuve clinique ou bibliographique. Deux autres prédictions (syndrome d'hyperviscosité polyclonale, score identique de 99,22 %, et analbuminémie congénitale, 99,08 %) présentent le même profil. Le score identique des deux premières suggère un artefact de structure du graphe plutôt qu'un signal biologique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65172663 | RECARBRIO 500 mg/500 mg/250 mg, poudre pour solution pour perfusion (MERCK SHARP & DOHME, Pays-Bas) | Poudre pour solution pour perfusion | Non renseignée (AMM annulée) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées pour ce rapport.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible. De plus, la seule AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (MOA) du relebactam
- Mises en garde et contre-indications issues de la notice de l'ANSM (données bloquantes pour le criblage de sécurité)
- Hypothèse biologique crédible reliant l'inhibition des bêta-lactamases à l'hyperamylasémie
- Études précliniques ou observationnelles, si l'hypothèse est confirmée
- Vérification de la compatibilité des voies d'administration et de la similarité avec l'indication d'origine (en attente)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

