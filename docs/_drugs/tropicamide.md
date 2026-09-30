---
layout: default
title: Tropicamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 327
evidence_level: L5
indication_count: 3
---

# Tropicamide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Tropicamide : D'un usage ophtalmique (mydriase) au syndrome de la queue de cheval

## Résumé en Une Phrase

La tropicamide est un anticholinergique (antimuscarinique) utilisé en ophtalmologie, sous forme de collyre, d'insert ophtalmique et de solution injectable commercialisés en France.
Le modèle TxGNN prédit qu'elle pourrait être utile pour le **syndrome de la queue de cheval**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données réglementaires (produits ophtalmiques : collyre, insert, solution injectable) |
| Nouvelle Indication Prédite | Syndrome de la queue de cheval |
| Score de Prédiction TxGNN | 99,53 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 4 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après la pharmacologie générale, la tropicamide est un antagoniste des récepteurs muscariniques, utilisé localement dans l'œil. Aucun mécanisme direct ne la relie au syndrome de la queue de cheval, une urgence neurologique compressive dont le traitement est chirurgical.

Le seul lien plausible est indirect : les antimuscariniques sont employés contre l'hyperactivité du détrusor, un trouble vésical qui peut suivre ce syndrome. Le score élevé du modèle (99,53 %) reflète une proximité dans le graphe de connaissances, et non une preuve d'efficacité. De plus, la forme ophtalmique n'entraîne qu'une exposition systémique minime.

Deux autres pistes ont été prédites, avec le même niveau de preuve (L5, aucune étude) :
- **Vessie neurogène** (score 99,13 %) : les antimuscariniques sont une classe établie dans cette situation, mais des médicaments approuvés (oxybutynine, solifénacine) couvrent déjà ce besoin. Le terme de la maladie est marqué « obsolète » dans l'ontologie et doit être remplacé par un terme actuel.
- **Syndrome de l'intestin irritable** (score 99,12 %) : des antispasmodiques antimuscariniques sont utilisés contre les crampes abdominales. La tropicamide n'a toutefois aucune forme orale ou systémique et son absorption par voie oculaire est négligeable.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62915154 | MYDRIATICUM 0,5 POUR CENT, collyre | Collyre | Non renseignée |
| 64029712 | MYDRIATICUM 2 mg/0,4 ml, collyre en récipient unidose | Collyre | Non renseignée |
| 67423452 | MYDRIASERT, insert ophtalmique | Insert | Non renseignée |
| 65082408 | MYDRANE 0,2 mg/ml + 3,1 mg/ml + 10 mg/ml, solution injectable | Solution injectable | Non renseignée |

Les quatre produits sont fabriqués par THEA.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5). Il n'existe ni essai ni publication, aucun mécanisme direct n'est établi, et les formes disponibles (ophtalmiques) ne permettent pas une exposition systémique pertinente.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour tout examen de sécurité)
- Compléter les données de mécanisme d'action (DrugBank) et les indications approuvées de chaque AMM
- Vérifier la faisabilité d'une voie d'administration adaptée (systémique ou intravésicale), aujourd'hui inexistante
- Pour la piste vessie neurogène : rattacher le terme obsolète à un terme d'ontologie actuel, puis comparer avec les antimuscariniques déjà approuvés
- Réaliser une revue de la littérature ciblée avant toute décision de poursuite

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

