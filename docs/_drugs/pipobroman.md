---
layout: default
title: Pipobroman
parent: Prédiction du modèle uniquement (L5)
nav_order: 608
evidence_level: L5
indication_count: 1
---

# Pipobroman
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

# Pipobroman : D'un usage antineoplasique à la Cataracte diabétique

## Résumé en Une Phrase

Pipobroman est un agent cytotoxique de type alkylant, historiquement utilisé dans les syndromes myéloprolifératifs (polyglobulie de Vaquez, thrombocytémie essentielle).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **cataracte diabétique**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées (usage historique : polyglobulie de Vaquez et thrombocytémie essentielle) |
| Nouvelle Indication Prédite | Cataracte diabétique |
| Score de Prédiction TxGNN | 99,01 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisation annulée uniquement (non commercialisé) |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le pipobroman est un dérivé de la pipérazine à activité cytotoxique de type alkylant, utilisé dans des affections myéloprolifératives. Son action repose sur l'alkylation de l'ADN et une myélosuppression.

Aucun lien mécanistique n'est établi avec la cataracte diabétique. Cette dernière résulte principalement de l'activation de la voie des polyols (aldose réductase), de l'accumulation de sorbitol et d'un stress osmotique et oxydatif dans le cristallin. L'activité alkylante et myélosuppressive du pipobroman n'a pas de connexion reconnue avec ces processus.

Le score élevé (0,990) est une sortie de modèle et peut refléter des artefacts de topologie du graphe de connaissances plutôt qu'une justification biologique. Tout lien proposé serait spéculatif et devrait être validé in vitro ou sur modèle animal avant toute autre considération.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60195398 | VERCYTE 25 mg, comprimé (LABORATOIRES DELBERT) – annulée | Comprimé | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et sans lien mécanistique plausible. De plus, le produit n'est plus autorisé en France et son profil cytotoxique rend un repositionnement dans une pathologie non cancéreuse peu favorable.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (interrogation de DrugBank)
- Mises en garde et contre-indications issues de la notice de l'ANSM (lacune bloquante pour tout dépistage de sécurité)
- Preuves précliniques (in vitro ou modèle animal de cataracte diabétique) justifiant un lien biologique
- Évaluation de la compatibilité de voie d'administration (une forme orale est a priori peu adaptée à une atteinte du cristallin)
- Analyse du rapport bénéfice/risque, compte tenu de la toxicité cytotoxique du médicament
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

