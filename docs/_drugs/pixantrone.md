---
layout: default
title: Pixantrone
parent: Prédiction du modèle uniquement (L5)
nav_order: 241
evidence_level: L5
indication_count: 1
---

# Pixantrone
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

# Pixantrone : Du Lymphome Non Hodgkinien Agressif à la Cataracte Diabétique

## Résumé en Une Phrase

Pixantrone est un agent cytotoxique de la famille des aza-anthracènediones, commercialisé pour le traitement du lymphome non hodgkinien agressif en rechute ou réfractaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **cataracte diabétique**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Lymphome non hodgkinien agressif en rechute ou réfractaire (le texte d'indication de l'AMM n'est pas renseigné dans les données) |
| Nouvelle Indication Prédite | Cataracte diabétique |
| Score de Prédiction TxGNN | 99,01 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. D'après les connaissances générales, pixantrone est un intercalant de l'ADN et un inhibiteur de la topoisomérase II, de type anthracyclinique. Son efficacité est établie dans le lymphome non hodgkinien agressif, une maladie maligne.

**Aucun lien mécanistique crédible n'est étayé par les données disponibles.** La cataracte diabétique résulte surtout de l'hyperactivité de la voie des polyols (aldose réductase et sorbitol), du stress oxydatif et de la glycation avancée des protéines du cristallin. Aucun de ces processus n'est une cible connue de pixantrone. Le score élevé de TxGNN (0,99) provient d'un graphe de connaissances et n'est corroboré par aucune étude.

Le profil de risque est aussi peu adapté : myélosuppression et cardiotoxicité de classe anthracyclinique, pour une maladie chronique non létale qui dispose déjà d'un traitement chirurgical efficace. La question de la voie d'administration oculaire resterait par ailleurs entière.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69454261 | PIXUVRI 29 mg (Laboratoires Servier) | Poudre pour solution à diluer pour perfusion | Non renseignée dans les données |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (aza-anthracènedione, inhibiteur de la topoisomérase II) |
| Risque de Myélosuppression | Élevé (toxicité de classe anthracyclinique) |
| Classification d'Émétogénicité | Faible à modérée (estimation selon la classe, à confirmer dans le RCP) |
| Éléments de Surveillance | NFS avec formule, fonction cardiaque (fraction d'éjection ventriculaire gauche), fonction hépatique et rénale |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques (préparation en milieu protégé, gants, gestion des déchets) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai, sans publication et sans lien mécanistique plausible. Le rapport bénéfice/risque d'un cytotoxique cardiotoxique dans une maladie chronique non létale est défavorable.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice/RCP de l'ANSM (mises en garde et contre-indications), afin de pouvoir réaliser le criblage de sécurité
- Obtenir les données de mécanisme d'action (MOA) depuis DrugBank
- Trouver des données précliniques (modèle de cristallin diabétique) montrant un effet sur la voie des polyols, le stress oxydatif ou la glycation
- Évaluer la faisabilité d'une voie d'administration oculaire et sa tolérance locale
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

