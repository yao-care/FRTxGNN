---
layout: default
title: Topiramate
parent: Prédiction du modèle uniquement (L5)
nav_order: 320
evidence_level: L5
indication_count: 9
---

# Topiramate
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Topiramate : De l'Épilepsie à la Tumeur du Nerf Trijumeau

## Résumé en Une Phrase

Le topiramate est un médicament antiépileptique (les données ANSM disponibles ne précisent toutefois pas le texte de l'indication approuvée).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **tumeur du nerf trijumeau**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction issue du modèle seul.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Épilepsie (usage connu du topiramate ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Tumeur du nerf trijumeau |
| Score de Prédiction TxGNN | 99,70 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 17 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances pharmacologiques générales, le topiramate agit sur les canaux sodiques, les récepteurs GABA-A, les récepteurs AMPA/kaïnate et l'anhydrase carbonique. Ce profil convient au contrôle des crises épileptiques.

Ces mécanismes ne relèvent pas de la biologie tumorale. Aucune donnée ne permet de relier l'épilepsie, indication d'origine, à une tumeur du nerf trijumeau. Le score élevé de TxGNN (0,997) reflète uniquement une proximité dans le graphe de connaissances.

En conséquence, la plausibilité mécanistique de cette prédiction n'est pas démontrée. Elle doit être considérée comme une piste à vérifier, et non comme une hypothèse étayée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Cinq des 17 AMM sont présentées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68906660 | TOPIRAMATE VIATRIS 200 mg (VIATRIS SANTE) | Comprimé pelliculé | Non précisée dans les données disponibles |
| 64696702 | TOPIRAMATE ARROW LAB 100 mg (ARROW GENERIQUES) | Comprimé pelliculé | Non précisée dans les données disponibles |
| 61913385 | EPITOMAX 100 mg (JANSSEN CILAG) | Comprimé pelliculé | Non précisée dans les données disponibles |
| 64137353 | TOPIRAMATE VIATRIS 50 mg (VIATRIS SANTE) | Comprimé pelliculé | Non précisée dans les données disponibles |
| 68987922 | EPITOMAX 25 mg (JANSSEN CILAG) | Gélule | Non précisée dans les données disponibles |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données disponibles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication et sans justification mécanistique.
- Les informations de sécurité de la notice ANSM manquent, ce qui bloque toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), donnée bloquante.
- Compléter les données sur le mécanisme d'action via DrugBank.
- Rechercher toute donnée préclinique ou clinique reliant le topiramate aux tumeurs du nerf trijumeau. À défaut, la piste est à abandonner.

**Pour information :** d'autres indications prédites pour ce médicament sont mieux étayées. C'est le cas de l'épilepsie visuelle (niveau L4, étape S1, « Question de recherche »), qui reste une extension d'un sous-type d'épilepsie déjà couverte par le topiramate. Elles pourraient être examinées en priorité.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

