---
layout: default
title: Tolcapone
parent: Prédiction du modèle uniquement (L5)
nav_order: 318
evidence_level: L5
indication_count: 10
---

# Tolcapone
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

# Tolcapone : De la maladie de Parkinson à l'encéphalite subaiguë de Rasmussen

## Résumé en Une Phrase

Tolcapone est un inhibiteur de la COMT (catéchol-O-méthyltransférase), connu comme traitement adjuvant de la lévodopa dans la maladie de Parkinson. Le texte d'indication de l'AMM française n'est pas renseigné dans les données reçues.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**encéphalite subaiguë de Rasmussen**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans l'AMM (maladie de Parkinson d'après la connaissance pharmacologique du médicament) |
| Nouvelle Indication Prédite | Encéphalite subaiguë de Rasmussen |
| Score de Prédiction TxGNN | 99,93 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. Sur la base des informations connues, tolcapone est un inhibiteur de la COMT : il prolonge l'exposition à la lévodopa et réduit les fluctuations motrices dans la maladie de Parkinson.

Le lien avec l'encéphalite de Rasmussen est en revanche **très faible**. Cette maladie est un processus inflammatoire à médiation immunitaire, piloté par les lymphocytes T. Or la inhibition de la COMT n'a aucune action immunomodulatrice connue. Le score TxGNN élevé résulte d'une prédiction fondée sur le graphe de connaissances, sans essai ni publication pour l'étayer.

Il faut donc lire ce résultat avec prudence : un score élevé ne signifie pas qu'un mécanisme plausible existe.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67077388 | TASMAR 100 mg, comprimé pelliculé (VIATRIS HEALTHCARE, Irlande) | Comprimé pelliculé | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

À titre indicatif, l'analyse de plausibilité du dossier évoque une **hépatotoxicité** de tolcapone, nécessitant une surveillance hépatique. Ce point n'est pas issu de la notice ANSM et doit être vérifié.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible avec une maladie inflammatoire à médiation immunitaire.
- Les données de sécurité de la notice ANSM sont absentes, ce qui empêche toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications) : point bloquant.
- Compléter les données sur le mécanisme d'action via DrugBank.
- Identifier un rationnel immunologique ou neuro-inflammatoire pour tolcapone dans l'encéphalite de Rasmussen, puis chercher des données précliniques ou cliniques.

**Autres candidats de la liste à examiner en priorité :** parmi les 10 prédictions, deux ont un niveau L4 et un statut « Research Question ». Ce sont la démence à corps de Lewy (2 publications précliniques, sans test de tolcapone) et la paralysie agitante juvénile de Hunt (parkinsonisme précoce, soutien indirect seulement). Leur proximité avec l'indication parkinsonienne existante les rend plus plausibles que l'encéphalite de Rasmussen, mais elles ne disposent d'aucun essai clinique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

