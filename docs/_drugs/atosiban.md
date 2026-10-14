---
layout: default
title: Atosiban
parent: Prédiction du modèle uniquement (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Atosiban
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

# Atosiban : Du Traitement de la Menace d'Accouchement Prématuré au Glaucome Primitif Héréditaire

## Résumé en Une Phrase

Atosiban est un antagoniste peptidique des récepteurs de l'ocytocine et de la vasopressine, utilisé comme tocolytique pour retarder l'accouchement prématuré chez la femme adulte enceinte de 24 à 33 semaines.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **glaucome primitif héréditaire**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM compilées (usage tocolytique d'après les données pharmacologiques) |
| Nouvelle Indication Prédite | Glaucome primitif héréditaire |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les informations pharmacologiques, atosiban se lie aux récepteurs V1A, V1B, V2 de la vasopressine et au récepteur de l'ocytocine, et est utilisé comme tocolytique.

Aucun lien mécanistique n'est établi entre ce profil et le glaucome primitif héréditaire. Le score élevé du modèle TxGNN repose sur une prédiction issue d'un graphe de connaissances, sans essai ni publication à l'appui. Pour le glaucome à angle ouvert (deuxième prédiction), seule une hypothèse spéculative a été formulée : un rôle de la signalisation ocytocine/vasopressine dans l'hémodynamique oculaire ou la dynamique de l'humeur aqueuse. Aucune donnée ne la soutient.

Cette prédiction doit donc être considérée comme une piste exploratoire et non comme une indication plausible validée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour le glaucome primitif héréditaire.

À titre contextuel, la prédiction classée en sixième position (maladie vasculaire) est accompagnée de publications, presque toutes précliniques et portant sur l'ocytocine ou d'autres agonistes, et non sur l'atosiban. La seule étude de cohorte (PMID 30646165) décrit une association entre l'exposition aux tocolytiques et l'hémorragie intraventriculaire chez le prématuré, ce qui constitue un signal de sécurité et non une preuve de bénéfice.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62476853 | TRACTOCILE 6,75 mg/0,9 ml (annulée) | Solution injectable | Non renseignée |
| 61710552 | TRACTOCILE 37,5 mg/5 ml (annulée) | Solution à diluer pour perfusion | Non renseignée |

## Considérations de Sécurité

- **Interactions et cibles pharmacologiques** : atosiban agit sur les récepteurs V1A, V1B, V2 et de l'ocytocine. Aucune interaction médicamenteuse classique n'est documentée avec un niveau de gravité.
- **Signal de sécurité observationnel** : une étude de cohorte chez le prématuré associe l'exposition aux tocolytiques à l'hémorragie intraventriculaire et au décès.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication ciblée et sans lien mécanistique démontré. Les AMM françaises sont toutes annulées, et la voie d'administration (injectable) n'a pas été évaluée pour une indication oculaire.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action
- Texte de la notice (mises en garde et contre-indications) depuis le site de l'ANSM
- Revue de la littérature sur la signalisation ocytocine/vasopressine dans la pression intraoculaire et la dynamique de l'humeur aqueuse
- Études précliniques de l'atosiban dans des modèles de glaucome
- Évaluation de la compatibilité des voies d'administration (injectable versus voie oculaire)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

