---
layout: default
title: Famciclovir
parent: Prédiction du modèle uniquement (L5)
nav_order: 315
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Famciclovir : nouvelle indication prédite, Névralgie post-infectieuse (niveau de preuve L4). Indication d'origine : Zona (herpès zoster)"
monitor_inn: "FAMCICLOVIR"
predicted_indications: ["post-infectious neuralgia", "sequela of COVID-19", "hepatitis C induced liver cirrhosis", "malignant pleural mesothelioma", "AIDS-related disorder", "malignant epithelioid mesothelioma", "chickenpox", "sarcomatoid mesothelioma", "malignant visceral pleura tumor"]
---

# Famciclovir
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Famciclovir : Du Zona à la Névralgie Post-Infectieuse
{: .text-alpha }

## Résumé en Une Phrase

Famciclovir est un antiviral, prodrogue du penciclovir, initialement utilisé pour le traitement du zona (herpès zoster).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **névralgie post-infectieuse** (névralgie post-zostérienne), mais **aucune publication** et **1 seul essai clinique** (sans lien direct avec le famciclovir) ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Zona (herpès zoster) |
| Nouvelle Indication Prédite | Névralgie post-infectieuse |
| Score de Prédiction TxGNN | 0,9975 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le famciclovir est une prodrogue du penciclovir : sous sa forme active (penciclovir triphosphate), il inhibe l'ADN polymérase du virus varicelle-zona (VZV).

Le zona est la maladie en amont de la névralgie post-zostérienne, qui en est la complication la plus fréquente. Réduire la réplication virale en phase aiguë pourrait limiter les lésions nerveuses et donc le risque de névralgie persistante. Ce lien est plausible sur le plan biologique, mais indirect.

Il faut souligner que le seul essai retrouvé teste l'oxycodone et non le famciclovir. Il n'apporte donc aucune preuve directe d'un bénéfice du famciclovir sur cette complication. Le score élevé du modèle reste, à ce stade, une prédiction.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | Non applicable | Inconnu | 140 | Effet de l'oxycodone précoce en phase aiguë du zona sur la prévention de la névralgie post-zostérienne. Le famciclovir n'est pas l'intervention étudiée. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69092403 | ORAVIR 125 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM active) |
| 62801318 | ORAVIR 500 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM active) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (hors notice)** : maladie rénale, pyourétère.
- **Interactions Médicamenteuses** : 84 interactions recensées, toutes de niveau « inconnu ». Parmi les médicaments concernés : calcitriol, doxycycline, clotrimazole, pantoprazole, glimépiride, morphine, metformine, oméprazole, vancomycine, prednisone, simvastatine.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être exploitées. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le lien mécanistique est plausible, mais aucune preuve directe n'existe : le seul essai associé n'évalue pas le famciclovir et aucune publication n'est disponible. De plus, les deux AMM françaises sont annulées, ce qui limite toute avancée pratique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank)
- Mises en garde et contre-indications officielles de la notice (ANSM)
- Essais ou études évaluant spécifiquement le famciclovir sur la prévention ou le traitement de la névralgie post-zostérienne
- Évaluation de la faisabilité réglementaire, étant donné l'absence d'AMM valide en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

