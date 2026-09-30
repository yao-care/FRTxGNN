---
layout: default
title: Cerliponase Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Cerliponase Alfa
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

# Cerliponase alfa : De la CLN2 (déficit en TPP1) au syndrome de Scheie

## Résumé en Une Phrase

Cerliponase alfa est une TPP1 recombinante (enzyme lysosomale) administrée par voie intraventriculaire. Le texte d'indication de l'AMM n'est pas renseigné dans les données, mais le mécanisme décrit dans le dossier renvoie à la maladie CLN2 (déficit en TPP1).
Le modèle TxGNN le prédit comme potentiellement efficace pour le **syndrome de Scheie**, avec **0 essai clinique** et **0 publication** à l'appui. La prédiction repose uniquement sur le modèle (niveau L5).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Syndrome de Scheie (MPS I atténuée) |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, cerliponase alfa est une enzyme de remplacement (TPP1 recombinante) qui dégrade des tripeptides dans le lysosome. Son efficacité dans son indication d'origine (CLN2) repose sur ce mécanisme, mais rien n'indique qu'il soit applicable au syndrome de Scheie.

Le syndrome de Scheie est une forme atténuée de MPS I, causée par un déficit en IDUA (alpha-L-iduronidase). Cette enzyme a un substrat différent de celui de la TPP1 : cerliponase alfa ne peut donc pas la remplacer. Le score TxGNN élevé reflète très probablement la proximité dans le graphe (voisinage « enzymothérapie substitutive lysosomale »), et non une justification au niveau du substrat.

Les neuf autres prédictions du top 10 sont également de niveau L5, sans essai clinique. Elles sont jugées sans fondement mécanistique plausible, soit parce qu'une enzymothérapie spécifique existe déjà (syndrome de Hurler, maladie de Gaucher, déficit en LIPA), soit parce que la maladie n'est pas un déficit enzymatique lysosomal (FENIB, ichtyose, myopathie). La seule publication liée à l'ensemble des prédictions est une revue de 2026 sur l'histoire naturelle des maladies lysosomales, qui utilise la maladie de Gaucher comme modèle (PMID [41527340](https://pubmed.ncbi.nlm.nih.gov/41527340/)). Elle ne fournit aucune donnée propre au médicament.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65808346 | BRINEURA 150 mg, solution pour perfusion (BIOMARIN INTERNATIONAL LIMITED, Irlande) | Solution pour perfusion | Non renseignée dans les données |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication. Le mécanisme est incompatible : la TPP1 ne peut pas remplacer l'IDUA déficiente.
- Les données de sécurité de l'ANSM sont absentes, ce qui bloque le passage à l'étape de criblage de sécurité S1.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde, contre-indications, indication approuvée)
- Compléter les données de mécanisme d'action via DrugBank
- Fournir des données précliniques démontrant une activité de la TPP1 sur les substrats du syndrome de Scheie
- Vérifier la compatibilité de la voie d'administration (intraventriculaire) avec une maladie principalement systémique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

