---
layout: default
title: Siltuximab
parent: Prédiction du modèle uniquement (L5)
nav_order: 704
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Siltuximab : nouvelle indication prédite, Mastocytome extracutané (niveau de preuve L5). Indication d'origine : Maladie de Castleman (source : base de connaissances TxGNN…"
monitor_inn: "SILTUXIMAB"
predicted_indications: ["extracutaneous mastocytoma", "hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "Kaposi's sarcoma (disease)", "autosomal recessive familial Mediterranean fever", "aggressive systemic mastocytosis", "autosomal dominant familial periodic fever"]
---

# Siltuximab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

# Siltuximab : De la maladie de Castleman au mastocytome extracutané

## Résumé en Une Phrase

Siltuximab est un anticorps monoclonal chimérique anti-IL-6, initialement utilisé pour le traitement de la maladie de Castleman (et de la maladie de Kimura selon la base de connaissances du modèle).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **mastocytome extracutané**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement informatique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Castleman (source : base de connaissances TxGNN, le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Mastocytome extracutané |
| Score de Prédiction TxGNN | 99,64 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 2 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, siltuximab est un anticorps monoclonal dirigé contre l'interleukine-6 (IL-6). Son efficacité dans la maladie de Castleman, caractérisée par une forte production d'IL-6, est le fondement de son usage d'origine.

Pour le mastocytome extracutané, aucun lien direct avec la biologie des mastocytes n'est établi dans les données compilées. L'IL-6 pourrait contribuer à la prolifération mastocytaire ou à la signalisation inflammatoire, mais cette hypothèse reste spéculative. Le score élevé de TxGNN est une prédiction issue du graphe de connaissances, sans corroboration clinique.

**Autres indications prédites (toutes sans essai clinique) :**

| Rang | Maladie | Score TxGNN | Niveau | Commentaire |
|------|------|------|------|------|
| 2 | Infarctus hépatique | 99,44 % | L5 | Aucune justification pour une nécrose ischémique d'origine vasculaire |
| 3 | Maladie veino-occlusive hépatique | 99,40 % | L5 | Lien hypothétique via l'inflammation endothéliale médiée par l'IL-6 |
| 4 | Péliose hépatique | 99,29 % | L5 | Lien indirect plausible via la maladie de Castleman |
| 5 | Sarcome de Kaposi | 99,28 % | L4 | Lien plausible via KSHV/HHV-8 et l'IL-6 (virale et humaine) ; une revue générale seulement |
| 6 | Fièvre méditerranéenne familiale (récessive) | 99,22 % | L5 | Plausible via l'IL-6, mais les inhibiteurs de l'IL-1 sont l'alternative établie |
| 7 | Mastocytose systémique agressive | 99,16 % | L5 | Maladie dominée par les mutations KIT ; rôle de l'IL-6 non établi |
| 8 | Fièvre périodique familiale (dominante) | 99,05 % | L5 | Plausible (ex. TRAPS), sans donnée propre au siltuximab |

Parmi elles, le sarcome de Kaposi est la piste la plus étayée sur le plan biologique (niveau L4, « question de recherche »).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune publication ne concerne directement le mastocytome extracutané. La seule publication identifiée dans l'ensemble des prédictions concerne le sarcome de Kaposi (rang 5) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39970477](https://pubmed.ncbi.nlm.nih.gov/39970477/) | 2024 | Revue | AIDS Reviews | Revue générale des étiologies de la maladie de Castleman (formes associées à des infections virales, dont KSHV) ; ne constitue pas une preuve directe chez les patients atteints de sarcome de Kaposi |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60622302 | SYLVANT 100 mg (annulée) | Poudre pour solution à diluer pour perfusion | Non renseignée |
| 63846800 | SYLVANT 400 mg (annulée) | Poudre à diluer pour solution pour perfusion | Non renseignée |

Les deux AMM, détenues par Recordati Netherlands, sont annulées ; il n'existe donc actuellement aucune AMM valide en France.

## Considérations de Sécurité

- **Interactions médicamenteuses** : 100 interactions répertoriées au total ; les principales parmi celles affichées :
  - **Majeure** : déférasirox non, mais **défériprone** (niveau Majeur).
  - **Modérée** : anticoagulants (warfarine, apixaban, rivaroxaban, dicoumarol), simvastatine, tacrolimus, fentanyl, hydrocodone, lidocaïne, nifédipine, théophylline et dérivés (aminophylline, oxtriphylline), roflumilast, anatoxine tétanique.
  - **Mineure** : sels de zinc (sulfate, acétate, gluconate, chlorure).

  Une partie de ces interactions modérées concerne des médicaments à marge thérapeutique étroite métabolisés par le CYP450 (warfarine, théophylline, tacrolimus), cohérent avec la normalisation de l'activité des enzymes hépatiques lors du blocage de l'IL-6.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour le mastocytome extracutané repose uniquement sur le modèle (niveau L5), sans essai ni publication, et le lien mécanistique avec l'IL-6 est spéculatif. De plus, les AMM françaises sont toutes annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice ANSM (mises en garde et contre-indications), actuellement bloquante pour le criblage de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Revue de la littérature sur le rôle de l'IL-6 dans les néoplasmes mastocytaires
- Exploration prioritaire de la piste du sarcome de Kaposi / syndrome inflammatoire à cytokines associé à KSHV, biologiquement plus plausible
- Clarification du statut réglementaire (annulation des AMM) et de la disponibilité du produit
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

