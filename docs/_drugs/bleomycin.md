---
layout: default
title: Bleomycin
parent: Prédiction du modèle uniquement (L5)
nav_order: 111
evidence_level: L5
indication_count: 6
---

# Bleomycin
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

# Bléomycine : Du lymphome de Hodgkin au néoplasme de la queue de cheval

## Résumé en Une Phrase

La bléomycine est un antibiotique cytotoxique utilisé en oncologie, notamment dans le traitement des lymphomes (Hodgkin et non-Hodgkin) et des cancers de la tête et du cou.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **néoplasme de la queue de cheval**.
Cette prédiction repose pour l'instant sur **aucun essai clinique** et sur **une seule publication**, indirecte.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Lymphome de Hodgkin (indications issues du graphe de connaissances, le texte d'indication des AMM françaises n'étant pas renseigné) |
| Nouvelle Indication Prédite | Néoplasme de la queue de cheval |
| Score de Prédiction TxGNN | 99,30 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Aucune AMM en vigueur (AMM annulées uniquement) |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, la bléomycine est un antibiotique cytotoxique qui provoque des cassures des brins d'ADN. Elle est utilisée dans les lymphomes, les cancers de la tête et du cou et les tumeurs germinales.

Le néoplasme de la queue de cheval est une tumeur du système nerveux central, éloignée des lymphomes. Le seul lien documenté est indirect : une étude sur la radiothérapie des germinomes du SNC en rechute après une chimiothérapie incluant la bléomycine (schéma PEB). Il n'existe aucune donnée propre à la bléomycine dans cette tumeur.

Le score élevé du modèle (99,30 %) est une prédiction purement computationnelle. Il ne remplace pas une preuve clinique ou mécanistique. Par ailleurs, la barrière hémato-encéphalique pourrait limiter la distribution du médicament au niveau du SNC.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [9440744](https://pubmed.ncbi.nlm.nih.gov/9440744/) | 1998 | Cohorte (rétrospective) | Journal of Clinical Oncology | Évaluation de la radiothérapie de rattrapage chez des patients atteints de germinome du SNC en rechute après une chimiothérapie primaire (carboplatine, étoposide, bléomycine). Association indirecte, sans donnée sur la queue de cheval. |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60033389 | BLEOMYCINE ACCORD 15000 UI | Poudre pour solution injectable ou pour perfusion | Non renseignée |
| 62789360 | BLEOMYCINE BELLON 15 mg | Poudre pour solution injectable | Non renseignée |

Les deux AMM sont au statut « annulée ». Aucune AMM n'est actuellement en vigueur pour ce médicament en France.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (antibiotique antitumoral, cassures de l'ADN) |
| Risque de Myélosuppression | Faible (la bléomycine est réputée épargner la moelle osseuse) |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | Fonction pulmonaire (dont DLCO), fonction rénale, NFS, tolérance cutanée |
| Protection de Manipulation | Manipulation selon les réglementations applicables aux médicaments cytotoxiques |

Veuillez consulter les mises en garde et précautions de la notice pour confirmer ces éléments.

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 205 interactions sont recensées. Parmi celles listées, une est de niveau mineur (lévofloxacine). Les autres sont de niveau non précisé : pantoprazole, palonosétron, lactulose, aprépitant, morphine, oméprazole, lansoprazole, vancomycine, prednisone, hydrocortisone, mannitol, chlorure de potassium, prednisolone, ranitidine, granisétron, ondansétron, famotidine, clarithromycine et métoclopramide.

Veuillez consulter la notice pour les mises en garde et contre-indications détaillées. Elles ne sont pas disponibles dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle, sans essai clinique et avec une seule publication indirecte (niveau L5).
- Le médicament n'a plus d'AMM en vigueur en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action
- Mises en garde et contre-indications issues de la notice (ANSM)
- Données précliniques ou cliniques de la bléomycine dans les tumeurs de la queue de cheval ou du SNC
- Évaluation de la faisabilité d'une administration locale ou intrathécale, compte tenu de la barrière hémato-encéphalique
- Évaluation du risque de toxicité pulmonaire et plan de surveillance associé
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

