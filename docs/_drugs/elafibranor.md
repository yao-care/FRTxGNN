---
layout: default
title: Elafibranor
parent: Prédiction du modèle uniquement (L5)
nav_order: 273
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Elafibranor : nouvelle indication prédite, Aménorrhée (niveau de preuve L5). Indication d'origine : Non renseignée dans l'AMM française (selon la littérature pharmacolog…"
monitor_inn: "elafibranor"
predicted_indications: ["amenorrhea (disease)"]
---

# Elafibranor
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Elafibranor : De l'indication d'origine non renseignée à l'aménorrhée

## Résumé en Une Phrase

Elafibranor (IQIRVO 80 mg, comprimé pelliculé) est un agoniste double des récepteurs PPARα et PPARδ. Il a été développé à l'origine pour la stéatohépatite non alcoolique (NASH), puis repositionné dans la cholangite biliaire primitive (CBP). Le texte d'indication de l'AMM française n'est pas renseigné dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**aménorrhée**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans l'AMM française (selon la littérature pharmacologique : CBP, après abandon de la NASH) |
| Nouvelle Indication Prédite | Aménorrhée |
| Score de Prédiction TxGNN | 99,86 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulée |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les informations pharmacologiques connues, elafibranor est un agoniste de PPARα et PPARδ (PPARβ/δ). Il est converti dans le foie en son métabolite actif principal, GFT-1007. Dans les études précliniques, il a réduit l'accumulation de graisse hépatique, l'inflammation et la fibrose.

Le lien avec l'aménorrhée reste spéculatif. Une hypothèse possible passerait par la modulation métabolique et inflammatoire des voies endocriniennes, par exemple dans l'aménorrhée liée au syndrome des ovaires polykystiques (SOPK) ou l'aménorrhée hypothalamique fonctionnelle. Aucun mécanisme spécifique à l'aménorrhée n'est établi, et aucune similarité démontrée avec l'indication d'origine n'a pu être évaluée. Le seul appui est le score élevé du modèle, qui est une prédiction computationnelle sans corroboration clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65387954 | IQIRVO 80 mg, comprimé pelliculé (IPSEN PHARMA) | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Considérations de Sécurité

Les données de la notice (mises en garde et contre-indications) ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité.

- **Interactions Médicamenteuses** : la requête est terminée, mais elle ne ressort que des interactions pharmacologiques avec les cibles (PPARα et PPARβ/δ). Aucune interaction médicamenteuse cliniquement classée n'est documentée.
- Aucune contre-indication issue du graphe de connaissances n'a été identifiée.

Remarque : les données de sécurité de l'ANSM manquent et constituent une lacune bloquante pour le criblage de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score TxGNN (niveau L5), sans essai clinique, sans publication et sans mécanisme spécifique établi. L'AMM française est annulée et les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde, contre-indications), lacune bloquante
- Obtenir les données détaillées sur le mécanisme d'action (MOA) via DrugBank
- Rechercher des études précliniques ou observationnelles reliant la modulation PPARα/δ à l'aménorrhée
- Clarifier le statut réglementaire en France (AMM annulée) et l'indication d'origine
- Évaluer la compatibilité de la voie d'administration et la similarité avec l'indication d'origine
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

