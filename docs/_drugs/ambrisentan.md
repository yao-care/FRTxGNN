---
layout: default
title: Ambrisentan
parent: Preuves modérées (L3-L4)
nav_order: 31
evidence_level: L4
indication_count: 10
---

# Ambrisentan
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **10** 
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

# Ambrisentan : De l'Hypertension Artérielle Pulmonaire à la Malformation Artério-veineuse Pulmonaire

## Résumé en Une Phrase

L'ambrisentan est un antagoniste des récepteurs de l'endothéline, utilisé à l'origine pour traiter l'hypertension artérielle pulmonaire (HTAP).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **malformation artério-veineuse pulmonaire**,
mais cette prédiction ne repose actuellement sur **aucun essai clinique** et sur **1 seule publication** (un rapport de cas qui ne démontre pas d'effet du médicament sur cette maladie).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle pulmonaire (le texte d'indication des AMM n'est pas renseigné dans les données ANSM ; information issue de l'analyse du mécanisme) |
| Nouvelle Indication Prédite | Malformation artério-veineuse pulmonaire |
| Score de Prédiction TxGNN | 99,41 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 11 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base utilisée. D'après les informations connues, l'ambrisentan est un antagoniste des récepteurs de l'endothéline (ETRA), dont l'efficacité dans l'HTAP est établie.

Le lien avec la nouvelle indication est indirect. La seule publication associée décrit une HTAP chez une patiente atteinte de télangiectasie hémorragique héréditaire (maladie de Rendu-Osler). Il s'agit d'une atteinte vasculaire pulmonaire distincte de la malformation artério-veineuse elle-même. Rien ne montre qu'un traitement par ETRA agisse sur la malformation.

Le score élevé reflète très probablement la proximité, dans le graphe de connaissances, entre la maladie de Rendu-Osler, les maladies vasculaires et l'HTAP. Il ne constitue pas une preuve d'efficacité, et la plausibilité mécanistique reste faible.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Rapport de cas | World Journal of Clinical Cases | Cas d'HTAP chez un patient atteint de télangiectasie hémorragique héréditaire, avec analyse génétique de la famille. Ne montre pas d'effet de l'ambrisentan sur la malformation artério-veineuse. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62848645 | AMBRISENTAN VIATRIS 10 mg | Comprimé pelliculé | Non renseignée |
| 61398654 | AMBRISENTAN VIATRIS 5 mg | Comprimé pelliculé | Non renseignée |
| 68371574 | AMBRISENTAN TEVA 5 mg | Comprimé pelliculé | Non renseignée |
| 64673002 | AMBRISENTAN TEVA 10 mg | Comprimé pelliculé | Non renseignée |
| 68499606 | VOLIBRIS 5 mg | Comprimé pelliculé | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle et sur un rapport de cas non pertinent pour la malformation artério-veineuse. Aucun essai clinique n'est associé.
- Le mécanisme n'est pas étayé : l'HTAP de la maladie de Rendu-Osler est une maladie distincte de la malformation.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des données précons cliniques ou mécanistiques montrant un rôle de l'endothéline dans les malformations artério-veineuses pulmonaires
- Des études cliniques ciblant directement cette indication
- Les mises en garde et contre-indications de la notice ANSM, à récupérer et analyser. Elles sont indispensables avant tout dépistage de sécurité, notamment pour la toxicité embryo-fœtale des antagonistes de l'endothéline.
- Les données détaillées sur le mécanisme d'action (DrugBank)

**À noter :** dans ce même dossier, d'autres indications prédites disposent de preuves nettement plus solides, avec une recommandation « Proceed with Guardrails » (niveau L2). Il s'agit de l'HTAP associée aux cardiopathies congénitales, à l'infection par le VIH et aux connectives, cette dernière étant la mieux documentée. Ces pistes méritent une évaluation distincte.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Toute piste de repositionnement doit être validée cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

