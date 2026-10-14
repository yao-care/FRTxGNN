---
layout: default
title: Delamanid
parent: Preuves modérées (L3-L4)
nav_order: 223
evidence_level: L4
indication_count: 7
---

# Delamanid
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **7** 
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

# Delamanid : De la tuberculose multirésistante à la tuberculose bovine

## Résumé en Une Phrase

Delamanid est un antituberculeux de la famille des nitroimidazoles, initialement utilisé pour le traitement de la tuberculose multirésistante.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **tuberculose bovine**, mais aucun essai clinique n'est enregistré pour cette indication et **1 seule publication** (une étude génomique indirecte) est disponible.
La prédiction repose donc essentiellement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Tuberculose multirésistante (le texte d'indication des AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Tuberculose bovine |
| Score de Prédiction TxGNN | 99,91 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, delamanid est un promédicament nitroimidazolé qui inhibe la synthèse des acides mycoliques chez *Mycobacterium tuberculosis*. Son efficacité dans la tuberculose multirésistante est établie.

*Mycobacterium bovis*, agent de la tuberculose bovine et de la tuberculose zoonotique humaine, appartient au même complexe *M. tuberculosis*. Une activité est donc plausible sur le plan mécanistique. Toutefois, la sensibilité de *M. bovis* à delamanid n'a pas été établie dans les données disponibles.

Le score élevé du modèle reflète surtout la proximité avec l'indication tuberculeuse déjà approuvée. La seule publication disponible est une étude de diversité génétique et de résistance de *M. bovis* par séquençage du génome entier. Elle n'a pas testé delamanid et ne constitue qu'une preuve indirecte.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Cohorte | BMC Genomics | Séquençage du génome entier d'isolats de *M. bovis* issus de tuberculose zoonotique : diversité génétique et caractéristiques de résistance aux médicaments. Delamanid n'est pas évalué. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64639797 | DELTYBA 50 mg, comprimé pelliculé (annulée) | Comprimé pelliculé | Non renseignée |
| 62314890 | DELTYBA 25 mg, comprimés dispersibles (annulée) | Comprimé dispersible | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose sur le score du modèle et sur une seule étude génomique indirecte, sans essai clinique ni donnée de sensibilité à delamanid.
- Les deux AMM françaises sont annulées et les données de sécurité de la notice ne sont pas disponibles.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de sensibilité *in vitro* de *M. bovis* à delamanid (CMI)
- Données détaillées sur le mécanisme d'action
- Mises en garde et contre-indications issues de la notice ANSM
- Précisions sur la situation réglementaire actuelle de delamanid en France

---

## Annexe : Autres indications prédites (à titre informatif)

Le même modèle a prédit d'autres indications, toutes sans preuve solide.

| Indication prédite | Score TxGNN | Niveau de preuve | Décision | Commentaire |
|------|------|------|------|------|
| Tuberculome | 99,91 % | L4 | Hold | Pénétration dans le système nerveux central non établie ; seule une revue générale est disponible |
| Ascite tuberculeuse | 99,91 % | L5 | Hold | Prédiction informatique uniquement |
| Tuberculose inactive (latente) | 99,91 % | L3 | Question de recherche | L'essai de phase 2/3 CRUSH-TB (NCT05766267, 288 participants, actif non recrutant) porte sur la tuberculose pulmonaire active ; le rôle de delamanid dans ses schémas n'est pas confirmé ici ; littérature composée surtout de revues générales |
| Tuberculose aviaire | 99,91 % | L5 | Hold | *M. avium* n'appartient pas au complexe *M. tuberculosis* ; activité douteuse |
| Urticaire allergique | 99,56 % | L5 | Hold | Aucun lien mécanistique plausible ; probable artefact du modèle |
| Tuberculose cutanée | 99,10 % | L4 | Hold | La littérature porte sur la toxicité des antituberculeux de première ligne, non sur l'efficacité |
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

