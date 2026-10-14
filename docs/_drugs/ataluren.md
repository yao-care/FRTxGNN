---
layout: default
title: Ataluren
parent: Prédiction du modèle uniquement (L5)
nav_order: 75
evidence_level: L5
indication_count: 6
---

# Ataluren
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Ataluren : De la dystrophie musculaire de Duchenne à la cholestase intrahépatique récurrente bénigne

## Résumé en Une Phrase

Ataluren est un médicament initialement utilisé pour traiter la dystrophie musculaire de Duchenne (et les dystrophies musculaires apparentées, dont celle de Becker).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **cholestase intrahépatique récurrente bénigne**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dystrophie musculaire de Duchenne (le texte d'indication des AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Cholestase intrahépatique récurrente bénigne |
| Score de Prédiction TxGNN | 99,42 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées (non commercialisé) |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'ataluren favorise la translecture ribosomale des codons stop prématurés (mutations non-sens). Son intérêt dans la dystrophie de Duchenne concerne donc les patients dont la maladie est due à une mutation non-sens.

La cholestase intrahépatique récurrente bénigne (BRIC) est causée par des mutations d'*ATP8B1* (BRIC1) ou d'*ABCB11* (BRIC2). Un sous-groupe de patients pourrait porter des variants non-sens, pour lesquels une translecture serait théoriquement plausible. Le lien avec l'indication d'origine n'est donc pas la maladie elle-même, mais le type de mutation en cause.

Cette hypothèse reste à confirmer : le score élevé (0,994) est une prédiction computationnelle, aucun essai ni publication n'a été retrouvé, et le lien n'a pas pu être vérifié par rapport à des données mécanistiques validées. Toute exploration ultérieure nécessiterait une stratification génotypique ciblant les porteurs de variants non-sens.

## Autres Indications Prédites

| Rang | Maladie | Score TxGNN | Commentaire |
|------|------|------|------|
| 2 | Trouble inné du métabolisme de la bilirubine | 99,40 % | Catégorie hétérogène (ex. Crigler-Najjar, Dubin-Johnson) ; la translecture ne s'appliquerait qu'aux porteurs de codons stop prématurés. Aucune preuve. |
| 3 | Cirrhose infantile héréditaire des Indiens d'Amérique du Nord | 99,33 % | Due à une mutation faux-sens de *UTP4* ; la translecture ne s'applique pas de façon évidente. Probable artefact de proximité dans le réseau. |
| 4 | Cholestase intrahépatique familiale | 99,26 % | Les formes progressives (*ATP8B1*, *ABCB11*, *ABCB4*) comptent des porteurs de variants non-sens ; hypothèse non étayée. |
| 5 | Rétinopathie diabétique non proliférative sévère | 99,24 % | Aucun lien mécanistique identifié ; association probablement fallacieuse. |
| 6 | Maladie du métabolisme de la bilirubine | 99,11 % | Catégorie parente trop peu spécifique pour formuler une hypothèse concrète. |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68469328 | TRANSLARNA 1000 mg | Granulés pour suspension buvable | Non renseignée (AMM annulée) |
| 65945882 | TRANSLARNA 250 mg | Granulés pour suspension buvable | Non renseignée (AMM annulée) |
| 67503464 | TRANSLARNA 125 mg | Granulés pour suspension buvable | Non renseignée (AMM annulée) |

Les trois AMM sont détenues par PTC Therapeutics International (Irlande) et sont toutes annulées ; aucune n'est actuellement valide.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les mises en garde et contre-indications issues de la notice ANSM n'ont pas pu être récupérées, et aucune interaction médicamenteuse n'a été retrouvée dans les données compilées pour ce rapport.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Le seul lien plausible (translecture de variants non-sens) ne concerne qu'un sous-groupe de patients, et les AMM françaises sont toutes annulées.
- Les données de sécurité de la notice sont absentes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice ANSM (mises en garde, contre-indications) pour le criblage de sécurité
- Données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Identification de la proportion de patients BRIC / cholestase familiale porteurs de variants non-sens (génotypage)
- Recherche de données précliniques (modèles cellulaires ou animaux de translecture sur *ATP8B1* / *ABCB11*) et de rapports de cas
- Évaluation de la compatibilité de la voie d'administration (granulés pour suspension buvable) avec la nouvelle indication
- Clarification du statut réglementaire, les trois AMM françaises étant annulées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

