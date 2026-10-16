---
layout: default
title: Acetic Acid
parent: Prédiction du modèle uniquement (L5)
nav_order: 20
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Acetic Acid : nouvelle indication prédite, Trouble post-bactérien (niveau de preuve L5). Indication d'origine : Otite externe, maladie de l'oreille externe"
---

# Acetic Acid
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

# Acide acétique : De l'otite externe à la maladie post-bactérienne

## Résumé en Une Phrase

L'acide acétique est un antiseptique et acidifiant à usage local, initialement utilisé pour traiter l'otite externe et les affections du conduit auditif externe.
Le modèle TxGNN prédit qu'il pourrait être efficace pour les **troubles post-bactériens**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.
Il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Otite externe, maladie de l'oreille externe |
| Nouvelle Indication Prédite | Trouble post-bactérien |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisations annulées uniquement |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

*Remarque : les deux autorisations françaises ne comportent pas de texte d'indication ; l'indication originale provient du graphe de connaissances TxGNN.*

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'acide acétique est un antiseptique et acidifiant à usage local doté d'une activité antibactérienne. Son efficacité dans l'otite externe repose sur l'acidification du milieu et sur son effet antimicrobien direct.

Le lien avec les troubles post-bactériens (séquelles d'une infection bactérienne) n'est étayé par aucune donnée recueillie. Un effet antibactérien local ne permet pas, à lui seul, de justifier une action sur des séquelles ou des processus survenant après l'infection.

La prédiction reste donc une hypothèse issue du modèle, sans soutien mécanistique ni clinique à ce stade. Le score élevé (rang 564 du modèle) ne remplace pas des preuves réelles.

D'autres indications prédites avec des scores très proches (vascularite post-infectieuse, syndrome post-infectieux, cardiomyopathie de Chagas, sténose urétrale infectieuse, syndrome hémolytique et urémique lié à une infection) sont également sans preuve et sans lien mécanistique plausible.

Parmi les prédictions de rang inférieur, la **teigne du corps (tinea corporis)** est la seule à disposer d'indices indirects : l'acide acétique possède une activité antifongique plausible. Elle est classée niveau L4 (« question de recherche »), mais ces indices sont anciens et peu probants (voir ci-dessous).

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée à l'indication principale (trouble post-bactérien).

À titre d'information, une publication a été retrouvée pour la prédiction de rang 3 (syndrome post-infectieux) ; elle ne concerne pas l'acide acétique :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [20848144](https://pubmed.ncbi.nlm.nih.gov/20848144/) | 2011 | Revue systématique | J Gastroenterol | Modèles animaux du syndrome de l'intestin irritable post-infectieux ; n'évalue pas l'acide acétique comme traitement |

Pour la teigne du corps (rang 9, niveau L4), les éléments les plus pertinents sont :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [20996178](https://pubmed.ncbi.nlm.nih.gov/20996178/) | 1946 | Rapport clinique historique | JAMA | Teigne du cuir chevelu traitée par iode spécial et acide acétique dilué |
| [20983383](https://pubmed.ncbi.nlm.nih.gov/20983383/) | 1946 | Rapport clinique historique | Arch Dermatol Syphilol | Même approche (iode et acide acétique dilué) |
| [20256868](https://pubmed.ncbi.nlm.nih.gov/20256868/) | 1947 | Série de cas historique | Urol Cutaneous Rev | Résultats dans une série plus large de patients |
| [13616002](https://pubmed.ncbi.nlm.nih.gov/13616002/) | 1958 | Rapport clinique historique | Vestn Dermatol Venerol | Épidermophytie du pied traitée par concentrations croissantes d'acide acétique |
| [26857689](https://pubmed.ncbi.nlm.nih.gov/26857689/) | 2016 | Étude in vitro | Mycoses | Évaluation de produits antifongiques topiques dans un modèle d'onychomycose |
| [31049344](https://pubmed.ncbi.nlm.nih.gov/31049344/) | 2019 | Série de cas | Skin Appendage Disord | Peeling chimique comme alternative aux antifongiques oraux dans l'onychomycose |
| [37256034](https://pubmed.ncbi.nlm.nih.gov/37256034/) | 2023 | Série de cas (événements indésirables) | Arch Plast Surg | Brûlures causées par des remèdes populaires coréens ; signal de sécurité |

Plusieurs autres références retrouvées sont hors sujet (produits de fermentation par bactéries lactiques, méthode analytique chromatographique) et ne sont pas retenues.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68976484 | ACETICUM ACIDUM LEHNING, degré de dilution compris entre 2CH et 30CH ou entre 4DH et 60DH | Comprimé, solution(s), granules, poudre et pommade | Non renseignée (AMM annulée) |
| 69773711 | ACETICUM ACIDUM BOIRON, degré de dilution compris entre 2CH et 30CH ou entre 4DH et 60DH | Comprimé, solution(s), granules, poudre et pommade | Non renseignée (AMM annulée) |

Il s'agit de produits homéopathiques ; les deux autorisations sont annulées.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : porphyrie héréditaire, maladie du métabolisme des porphyrines, porphyrie, infection herpétique (herpès simplex), zona du ganglion géniculé.
- **Signal de sécurité de la littérature** : un rapport de cas décrit des brûlures liées à l'usage de remèdes populaires ; des concentrations élevées d'acide acétique peuvent causer des lésions cutanées.
- **Interactions médicamenteuses** : aucune interaction retrouvée dans les données consultées.

Veuillez consulter la notice pour les informations de sécurité complètes (mises en garde et contre-indications officielles).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction principale (trouble post-bactérien) repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible. Les autorisations françaises sont toutes annulées.
- Parmi les autres pistes, seule la teigne du corps présente des indices indirects (niveau L4), mais ils sont anciens, non contrôlés, souvent associés à d'autres agents, et constituent une hypothèse à tester plutôt qu'une base de recommandation.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (consultation de DrugBank)
- Mises en garde et contre-indications officielles de la notice ANSM (lacune bloquante pour le filtrage de sécurité)
- Revue ciblée de la littérature sur un lien entre acide acétique et séquelles post-bactériennes, ou réorientation de l'évaluation vers la teigne du corps
- Pour la teigne, études contrôlées modernes définissant la concentration, la formulation et le profil de tolérance cutanée
- Vérification de la compatibilité de la voie d'administration (actuellement en attente)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

