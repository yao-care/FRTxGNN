---
layout: default
title: Sulpiride
parent: Preuves modérées (L3-L4)
nav_order: 723
evidence_level: L4
indication_count: 9
---

# Sulpiride
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **9** 
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

# Sulpiride : De la Schizophrénie à la Dystrophie Rétinienne

## Résumé en Une Phrase

Le sulpiride est un antagoniste sélectif des récepteurs dopaminergiques D2/D3, initialement utilisé pour le traitement de la schizophrénie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dystrophie rétinienne avec ou sans anomalies extraoculaires**,
mais **aucun essai clinique** n'est enregistré et seules **2 publications précliniques** (modèle de rat) soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Schizophrénie (d'après le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Dystrophie rétinienne avec ou sans anomalies extraoculaires |
| Score de Prédiction TxGNN | 99,95 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Uniquement des AMM annulées |
| Nombre d'AMM | 6 (toutes annulées) |
| Décision Recommandée | Hold (question de recherche) |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le sulpiride est un antagoniste sélectif des récepteurs dopaminergiques D2 et D3, avec une faible affinité pour le récepteur D4. Les données compilées indiquent également une interaction avec plusieurs anhydrases carboniques (CA1, CA7, CA12), dont la portée clinique n'est pas précisée. Les données détaillées sur le mécanisme d'action issues de DrugBank ne sont pas disponibles ; cette description repose sur les données pharmacologiques compilées.

La dopamine module les réponses lumineuses des cellules ganglionnaires de la rétine. Dans le modèle de rat P23H de rétinite pigmentaire, les antagonistes D2 (dont le sulpiride) semblent améliorer les réponses visuelles de ces cellules, en augmentant leur sensibilité à la lumière et en transformant des cellules ON anormales à latence longue en cellules OFF. Le lien avec l'indication d'origine est donc pharmacologique (blocage D2) et non une similarité de maladie : la schizophrénie et la dystrophie rétinienne n'ont pas de parenté clinique.

Cette preuve reste préclinique et indirecte. Elle montre que le blocage D2 modifie la signalisation rétinienne, mais pas qu'il ralentit la dégénérescence ni qu'il améliore la vision chez le patient. Le score TxGNN très élevé est une prédiction computationnelle uniquement.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [27788033](https://pubmed.ncbi.nlm.nih.gov/27788033/) | 2016 | Préclinique (électrophysiologie animale) | J Ocul Pharmacol Ther | Étude des effets de l'halopéridol et de la clozapine sur les réponses visuelles des cellules ganglionnaires dans le modèle de rat P23H ; le résumé rappelle que le sulpiride et l'éticlopride semblent les améliorer |
| [26717015](https://pubmed.ncbi.nlm.nih.gov/26717015/) | 2015 | Préclinique (électrophysiologie animale) | PLoS One | Effets des antagonistes D2 sur les réponses lumineuses des cellules ganglionnaires dans les rétines de rats sauvages et P23H |

## Informations de Marché en France

Les six AMM sont annulées ; le texte d'indication approuvée n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 61055303 | SULPIRIDE TEVA 50 mg | Gélule | Annulée |
| 64285722 | DOGMATIL 0,5 g/100 ml sans sucre | Solution buvable | Annulée |
| 67208161 | DOGMATIL 200 mg | Comprimé sécable | Annulée |
| 62344129 | DOGMATIL 50 mg | Gélule | Annulée |
| 66241856 | SULPIRIDE TEVA 200 mg | Comprimé sécable | Annulée |

## Considérations de Sécurité

- **Interactions et cibles pharmacologiques** : le sulpiride cible les récepteurs D2 et D3 (effet recherché) et interagit avec les anhydrases carboniques 1, 7 et 12. Aucune interaction médicamenteuse avec niveau de gravité n'est disponible.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold (question de recherche)**

**Justification :**
- Seules deux études précliniques sur le rat, indirectes, soutiennent l'hypothèse ; aucune donnée clinique n'existe et l'effet sur la dégénérescence ou la vision est inconnu. Toutes les AMM françaises sont annulées.
- Les autres prédictions (hydranencéphalie, polymicrogyrie, Charcot-Marie-Tooth 1G, formes de myopie, anomalies de glycosylation, encéphalopathie à glycine atypique) n'ont aucune preuve ; pour les myopies, l'antagonisme D2 pourrait même être défavorable.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications issues de la notice ANSM (bloquant pour le criblage de sécurité)
- Données détaillées sur le mécanisme d'action (DrugBank)
- Études précliniques supplémentaires (autres modèles, effet sur la survie des photorécepteurs et la fonction visuelle)
- Évaluation de la voie d'administration et de la sécurité oculaire/systémique avant toute étude clinique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

