---
layout: default
title: Ammonium Chloride
parent: Prédiction du modèle uniquement (L5)
nav_order: 37
evidence_level: L5
indication_count: 2
---

# Ammonium Chloride
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Chlorure d'ammonium : D'une Indication Originale Non Renseignée à la Laryngopharyngite Aiguë

## Résumé en Une Phrase

Le chlorure d'ammonium est commercialisé en France dans des solutions pour perfusion (oligo-éléments et nutrition pédiatrique), mais les textes d'indication de ces AMM ne sont pas renseignés dans les données.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **laryngopharyngite aiguë**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Laryngopharyngite aiguë |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 4 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le chlorure d'ammonium est présent dans des solutions pour perfusion pédiatriques (gamme PEDIAVEN AP-HP et solution d'oligo-éléments Aguettant). Son efficacité dans une indication d'origine n'a pas pu être vérifiée à partir des données fournies, faute de texte d'indication.

Le chlorure d'ammonium est connu comme expectorant dans certaines préparations contre la toux sans ordonnance. Il pourrait irriter la muqueuse gastrique et augmenter par réflexe les sécrétions des voies respiratoires, ce qui fluidifierait le mucus dans une inflammation des voies aériennes supérieures. Il s'agit d'un raisonnement pharmacologique général et non d'une preuve issue des données. Son intérêt réel dans la laryngopharyngite aiguë n'est pas vérifié.

La deuxième prédiction, « maladie de la cavité nasale » (score 99,94 %), repose sur un terme très large et peu spécifique. Les propriétés expectorantes du médicament n'ont qu'un lien faible et indirect avec cette pathologie. Ce lien reste spéculatif et demande une définition plus précise de la maladie ainsi qu'un appui mécanistique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 63262521 | Solution injectable d'oligo-éléments Aguettant enfants et nourrissons | Solution injectable pour perfusion |
| 68575185 | Pediaven AP-HP G15 | Solution pour perfusion |
| 67678175 | Pediaven AP-HP G20 | Solution pour perfusion |
| 62083608 | Pediaven AP-HP G25 | Solution pour perfusion |

Les quatre AMM correspondent à des formes injectables pour perfusion. Aucune forme orale ou respiratoire n'est recensée, ce qui pose une question de compatibilité de voie d'administration avec la nouvelle indication prédite.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Le mécanisme d'action et les données de sécurité sont absents, et les formes commercialisées (perfusions) ne correspondent pas à une voie plausible pour une atteinte laryngopharyngée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications), point bloquant avant tout criblage de sécurité
- Obtenir le mécanisme d'action détaillé (DrugBank)
- Obtenir les textes d'indication des AMM françaises
- Rechercher des essais cliniques et de la littérature spécifiques à la laryngopharyngite aiguë
- Évaluer la compatibilité de voie d'administration (formes orales ou locales versus perfusion)
- Pour la « maladie de la cavité nasale », préciser d'abord la définition de la maladie

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

