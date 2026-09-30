---
layout: default
title: Ofatumumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 220
evidence_level: L5
indication_count: 8
---

# Ofatumumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

# Ofatumumab : De l'indication d'origine (non renseignée) à la LLC/lymphome lymphocytique à petites cellules avec hypermutation somatique IGHV

## Résumé en Une Phrase

L'ofatumumab est un anticorps monoclonal anti-CD20 entièrement humain. Les données fournies ne précisent pas son indication d'origine en France.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **leucémie lymphoïde chronique/lymphome lymphocytique à petites cellules (LLC/LL) avec hypermutation somatique du gène IGHV**.
Pour cette prédiction précise, **aucun essai clinique et aucune publication** ne la soutiennent actuellement ; le niveau de preuve est donc L5.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | LLC/LL avec hypermutation somatique IGHV |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances générales, l'ofatumumab cible la molécule CD20 à la surface des lymphocytes B. Il détruit les cellules malignes par cytotoxicité dépendante du complément (CDC) et par cytotoxicité cellulaire dépendante des anticorps (ADCC).

La LLC/LL avec hypermutation IGHV est un sous-type moléculaire de la LLC/LL, une maladie des lymphocytes B exprimant CD20. Un rationnel mécanistique existe donc. Rien n'indique cependant que l'activité de l'ofatumumab dépende du statut IGHV.

Le score élevé reflète surtout la proximité du sous-type avec la LLC/LL dans le graphe de connaissances, et non une preuve indépendante. Les données de la LLC/LL ne constituent qu'un soutien indirect.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60690011 | KESIMPTA 20 mg, solution injectable en stylo prérempli | Solution injectable | Non renseignée dans les données |

Le titulaire est NOVARTIS EUROPHARM (Irlande). Le texte de l'indication est vide dans les données, alors que le rationnel du dossier suppose un usage autorisé dans la LLC. Les deux ne sont pas cohérents et doivent être vérifiés. Le seul produit listé est un stylo prérempli de 20 mg, une présentation qui ne correspond pas à la formulation utilisée en hématologie.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Cette prédiction repose uniquement sur le modèle, sans essai ni publication propre au sous-type IGHV muté (L5, stade S0).
- Les données de sécurité et l'indication d'origine sont manquantes, ce qui bloque le criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice de l'ANSM (mises en garde, contre-indications, indication autorisée de l'AMM 60690011).
- Compléter le mécanisme d'action via DrugBank (DB06650).
- Vérifier la cohérence entre l'AMM listée (stylo de 20 mg) et l'usage hématologique supposé.
- Rechercher des données propres au sous-type IGHV muté, par exemple des analyses en sous-groupes des essais sur la LLC/LL.
- Envisager de prioriser d'autres prédictions mieux documentées du même dossier :
  - la **LLC/LL sans sous-type** (rang 5), niveau L1 : plusieurs essais de phase 3 terminés, mais cette entrée relève surtout de la confirmation d'une indication existante ;
  - le **lymphome folliculaire** (rang 3), niveau L2 : 15 essais, dont des phases 2 randomisées, sans phase 3, avec l'anti-CD20 rituximab comme standard établi.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

