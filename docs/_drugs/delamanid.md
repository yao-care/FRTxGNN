---
layout: default
title: Delamanid
parent: Prédiction du modèle uniquement (L5)
nav_order: 223
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
monitor_inn: "delamanid"
predicted_indications: ["allergic urticaria"]
description: "Delamanid : nouvelle indication prédite, Allergic urticaria (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Delamanid
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Delamanid: Allergic urticaria
{: .text-alpha }

## Résumé en Une Phrase

Delamanid est un antituberculeux de la famille des nitroimidazoles, initialement utilisé pour le traitement de la tuberculose multirésistante.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **tuberculose bovine**, mais aucun essai clinique n'est enregistré pour cette indication et **1 seule publication** (une étude génomique indirecte) est disponible.
La prédiction repose donc essentiellement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Allergic urticaria |
| Score de Prédiction TxGNN | 0.9956 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
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
| 64639797 | DELTYBA 50 mg, comprimé pelliculé (active) | Comprimé pelliculé | Non renseignée |
| 62314890 | DELTYBA 25 mg, comprimés dispersibles (active) | Comprimé dispersible | Non renseignée |

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
| Urticaire allergique | 0,9956 | L5 | Hold | Aucun lien mécanistique plausible ; probable artefact du modèle |
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

