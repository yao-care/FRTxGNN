---
layout: default
title: Primidone
parent: Prédiction du modèle uniquement (L5)
nav_order: 250
evidence_level: L5
indication_count: 10
---

# Primidone
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

# Primidone : De l'épilepsie au neoplasme du nerf trijumeau

## Résumé en Une Phrase

Primidone est un antiépileptique de la famille des barbituriques, utilisé à l'origine dans la prise en charge de l'épilepsie. Le modèle TxGNN prédit qu'il pourrait être efficace pour le **neoplasme du nerf trijumeau**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans l'AMM fournie (antiépileptique par sa classe pharmacologique) |
| Nouvelle Indication Prédite | Neoplasme du nerf trijumeau |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, la primidone est une prodrogue antiépileptique métabolisée en phénobarbital et en PEMA. Son efficacité est établie dans les crises épileptiques, mais aucun mécanisme antitumoral plausible n'est identifié.

Le lien entre l'indication d'origine et la nouvelle indication est donc faible. Le score TxGNN très élevé reflète probablement une proximité dans le graphe de connaissances avec la **névralgie du trijumeau**, une pathologie douloureuse du même nerf traitée par des antiépileptiques. Il ne traduit vraisemblablement pas un véritable signal antitumoral.

En résumé, cette prédiction n'est étayée ni par la littérature ni par un raisonnement mécanistique. Elle doit être considérée comme un artefact probable du modèle, à ne pas exploiter en l'état.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 65201684 | MYSOLINE 250 mg, comprimé sécable (SERB) | Comprimé sécable |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai, sans publication et sans mécanisme antitumoral plausible.
- Les données de sécurité de la notice ANSM manquent, ce qui bloque l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications), point bloquant.
- Obtenir les données sur le mécanisme d'action, par exemple via DrugBank.
- Renseigner l'indication approuvée dans l'AMM.
- Réorienter l'évaluation vers la névralgie du trijumeau, une piste plus plausible parmi les prédictions du modèle. Son niveau de preuve est L4, avec des données indirectes uniquement. Un signal de sécurité lié aux barbituriques (nécrolyse épidermique toxique) est à garder à l'esprit.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

