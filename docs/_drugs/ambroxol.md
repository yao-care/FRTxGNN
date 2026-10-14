---
layout: default
title: Ambroxol
parent: Prédiction du modèle uniquement (L5)
nav_order: 53
evidence_level: L5
indication_count: 5
---

# Ambroxol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Ambroxol : De la Pharyngite à la Maladie de la Cavité Nasale

## Résumé en Une Phrase

Ambroxol est un agent mucolytique et sécrétolytique, initialement associé au traitement de la pharyngite.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie de la cavité nasale**,
mais aucun essai clinique n'est enregistré et seule **1 publication** (une revue indirecte sur la toux aiguë) est disponible à ce jour.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Pharyngite (selon le graphe de connaissances TxGNN ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Maladie de la cavité nasale |
| Score de Prédiction TxGNN | 99,91 % |
| Niveau de Preuve | L4 (preuve indirecte et très limitée ; prédiction essentiellement computationnelle) |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, l'ambroxol est un agent mucolytique et sécrétolytique qui favorise la clairance du mucus des voies respiratoires. Il possède aussi des propriétés d'anesthésique local (blocage des canaux sodiques) et anti-inflammatoires.

Ces propriétés pourraient soulager des symptômes des voies aériennes supérieures tels que la congestion et l'hypersécrétion de mucus. La pharyngite et les maladies de la cavité nasale touchent toutes deux les voies aériennes supérieures, ce qui rend le lien anatomique et clinique plausible.

Cette justification repose sur des connaissances générales et non sur les données fournies. Le score très élevé de TxGNN (0,999) reste une prédiction computationnelle, et la seule publication associée est indirecte pour cette indication.

Par ailleurs, les données de pharmacologie indiquent que l'ambroxol cible la glucosylcéramidase bêta (GBA1) et est exploré pour des maladies neurodégénératives (maladie de Parkinson, sclérose latérale amyotrophique). Cela ne concerne pas l'indication prédite ici.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [26525480](https://pubmed.ncbi.nlm.nih.gov/26525480/) | 2015 | Revue | Vestnik otorinolaringologii | Article sur le traitement de la toux aiguë associée à la grippe et aux infections respiratoires virales aiguës ; preuve indirecte pour la maladie de la cavité nasale |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61641907 | MUXOL, solution buvable (LABORATOIRES FRILAB) | Solution buvable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : une interaction de nature pharmacologique est répertoriée avec la glucosylcéramidase bêta (GBA1). L'ambroxol agit comme chaperon de cette enzyme : inhibiteur à pH neutre dans un milieu acellulaire, mais il augmente l'activité enzymatique intracellulaire dans les lysosomes acides. Le niveau de gravité n'est pas précisé.

Veuillez consulter la notice pour les mises en garde et contre-indications.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé, mais aucun essai clinique n'existe et la seule publication est indirecte. L'AMM française est annulée et les données de sécurité de la notice sont absentes, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications)
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Réaliser une recherche bibliographique ciblée sur l'ambroxol dans les affections nasales et rhinosinusales
- Clarifier les raisons de l'annulation de l'AMM et le statut réglementaire actuel
- Évaluer la compatibilité des voies d'administration pour l'indication visée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

