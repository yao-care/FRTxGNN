---
layout: default
title: Palbociclib
parent: Prédiction du modèle uniquement (L5)
nav_order: 228
evidence_level: L5
indication_count: 4
---

# Palbociclib
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

# Palbociclib : Du Cancer du Sein à l'Hyperthyroïdie

## Résumé en Une Phrase

Palbociclib est un inhibiteur de CDK4/6 utilisé dans le cancer du sein métastatique HR+/HER2-, d'après la littérature du dossier. Le texte des indications des AMM françaises n'est pas renseigné.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hyperthyroïdie**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer du sein HR+/HER2- (déduit de la littérature ; texte d'indication des AMM non renseigné) |
| Nouvelle Indication Prédite | Hyperthyroïdie |
| Score de Prédiction TxGNN | 99,44 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, palbociclib fait partie des inhibiteurs de CDK4/6 (contrôle du cycle cellulaire), son efficacité dans le cancer du sein a été établie, mais rien ne démontre qu'il soit applicable à l'hyperthyroïdie.

Aucun lien mécanistique entre l'inhibition de CDK4/6 et l'excès d'hormones thyroïdiennes n'est étayé par les données fournies. Le score élevé de TxGNN (0,994) reste une sortie de modèle, sans essai ni publication associés. Toute hypothèse de lien serait à ce stade spéculative.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68016146 | IBRANCE 100 mg, gélule | Gélule | Non renseignée dans les données |
| 67316379 | IBRANCE 75 mg, gélule | Gélule | Non renseignée dans les données |
| 60321676 | IBRANCE 125 mg, gélule | Gélule | Non renseignée dans les données |

Titulaire des trois AMM : PFIZER EUROPE MA EEIG (Belgique).

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de CDK4/6) |
| Risque de Myélosuppression | Moyen à élevé : la littérature du dossier cite la suppression médullaire parmi les effets indésirables fréquents des inhibiteurs de CDK4/6 (niveau exact non quantifié) |
| Classification d'Émétogénicité | Faible (estimation selon la classe, à confirmer avec la notice) |
| Éléments de Surveillance | NFS avec formule (neutrophiles), fonction hépatique ; vigilance sur les événements thromboemboliques et pulmonaires (pneumopathie interstitielle) signalés dans la littérature |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

À titre indicatif, la littérature du dossier (études de pharmacovigilance FAERS, cohortes, revues) décrit pour la classe des inhibiteurs de CDK4/6 des signaux d'événements thromboemboliques, de pneumopathie interstitielle et de myélosuppression. Ces données proviennent de populations oncologiques.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'hyperthyroïdie n'est soutenue que par un score de modèle (L5), sans essai, sans publication ni mécanisme plausible. La sécurité en dehors de l'oncologie n'est pas caractérisée.
- Parmi les autres prédictions du dossier, la **polyarthrite rhumatoïde** (rang 2, niveau L4) est nettement mieux documentée : 4 publications (un cas clinique, une cohorte, deux études précliniques) suggèrent un rôle de CDK6 dans l'hyperplasie synoviale. C'est une question de recherche plus pertinente que l'hyperthyroïdie. Le rapport porte toutefois sur le rang 1, comme demandé. La maladie thrombotique (rang 3) est contredite par les signaux de sécurité, et la résistance aux hormones thyroïdiennes (rang 4) n'a aucune preuve.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (requête DrugBank)
- Mises en garde et contre-indications de la notice ANSM (bloquant pour le criblage de sécurité)
- Indications approuvées des trois AMM
- Preuve précliniques ou observationnelles reliant CDK4/6 à la physiopathologie thyroïdienne
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

