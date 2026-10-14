---
layout: default
title: Secnidazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 695
evidence_level: L5
indication_count: 7
---

# Secnidazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

# Sécnidazole : De la vaginose bactérienne à la vaginite atrophique postménopausique

## Résumé en Une Phrase

Le sécnidazole est un antimicrobien de la famille des 5-nitroimidazoles, initialement utilisé contre les infections vaginales et parasitaires (vaginose bactérienne, trichomonase, giardiase).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **vaginite atrophique postménopausique**, avec un score très élevé.
Aucun essai clinique ni aucune publication ne soutient toutefois cette prédiction : **0 essai clinique** et **0 publication**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Vaginose bactérienne, trichomonase, giardiase, vaginite, vulvite, vulvovaginite (indications issues du graphe de connaissances, le texte d'indication de l'AMM n'étant pas renseigné) |
| Nouvelle Indication Prédite | Vaginite atrophique postménopausique |
| Score de Prédiction TxGNN | 99,70 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | AMM annulée uniquement (non commercialisé) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales sur la classe, le sécnidazole est un 5-nitroimidazole. Son groupement nitro est activé par réduction chez les micro-organismes anaérobies et les protozoaires, ce qui endommage leur ADN. Son efficacité est établie dans les infections vaginales d'origine microbienne ou parasitaire.

Le score élevé du modèle reflète vraisemblablement la proximité, dans le réseau de connaissances, avec les indications vaginales déjà reconnues (vaginite, vulvovaginite). Cette proximité anatomique ne constitue pas un argument pharmacologique. La vaginite atrophique est causée par la carence en œstrogènes après la ménopause, et non par une infection. L'activité antimicrobienne du sécnidazole n'a donc pas de lien mécanistique plausible avec la physiopathologie de cette maladie.

Cette prédiction doit être considérée comme un artefact probable du modèle et non comme une piste thérapeutique crédible en l'état.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63820798 | SECNOL 2 g, granulés en sachet-dose (SUBSTIPHARM), AMM annulée | Granulés | Non renseignée dans les données compilées |

La seule AMM connue est annulée. La disponibilité du produit en France devrait donc être vérifiée avant toute réflexion sur un usage ultérieur.

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 92 interactions ont été recensées, toutes les 20 premières étant de niveau modéré. Les principales concernent :
  - les autres nitroimidazoles (métronidazole, tinidazole), avec un risque de duplication thérapeutique ;
  - les statines (rosuvastatine, simvastatine, atorvastatine) ;
  - l'amiodarone ;
  - la lévodopa ;
  - des anticancéreux (paclitaxel, carboplatine, bortézomib, cabazitaxel, brentuximab védotin, trastuzumab emtansine, carfilzomib) ;
  - l'adalimumab, le certolizumab pégol et l'auranofine ;
  - le picosulfate et les iodures radioactifs (I-123, I-131).

Pour les mises en garde et les contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score de prédiction est très élevé (99,70 %), mais il n'existe aucun essai clinique ni publication, et le lien mécanistique avec une maladie hormonale non infectieuse est inexistant (niveau de preuve L5).
- L'AMM française est annulée et les données de sécurité issues de la notice ne sont pas disponibles.

À titre d'information, parmi les autres prédictions du modèle, le « pertes vaginales » est la mieux documentée (plusieurs essais de phase 3 et méta-analyses). Ces preuves reflètent surtout les indications déjà connues (vaginose bactérienne, trichomonase) et non une véritable nouvelle maladie. Elles ne soutiennent donc pas la prédiction retenue ici.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice officielle (mises en garde, contre-indications) auprès de l'ANSM ;
- Compléter les données sur le mécanisme d'action (par exemple via DrugBank) ;
- Rechercher d'éventuelles preuves précliniques ou cliniques spécifiques à la vaginite atrophique, en l'absence desquelles l'hypothèse ne devrait pas être poursuivie ;
- Vérifier la disponibilité réelle du produit en France, compte tenu de l'annulation de l'AMM.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

