---
layout: default
title: Flucytosine
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 1
---

# Flucytosine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Flucytosine : Des Infections Fongiques à la Maladie de Paget Osseuse

## Résumé en Une Phrase

Flucytosine (5-fluorocytosine) est un antifongique classique utilisé depuis les années 1970, notamment contre les infections à *Cryptococcus* et *Candida*, en association avec l'amphotéricine B.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Maladie de Paget Osseuse**,
cependant **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction — il s'agit d'une prédiction de modèle sans base de preuves cliniques.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infections fongiques systémiques (cryptococcose, candidose) — aucune AMM en France dans cette base |
| Nouvelle Indication Prédite | Maladie de Paget Osseuse |
| Score de Prédiction TxGNN | 99.04% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans cette base. Sur la base des informations connues, Flucytosine est un antimétabolite antifongique : après pénétration dans la cellule fongique, il est converti par la cytosine désaminase fongique en 5-fluorouracile (5-FU), lequel est ensuite métabolisé en 5-FUTP et 5-FdUMP — interférant respectivement avec la synthèse de l'ARN et inhibant la thymidylate synthase, bloquant ainsi la réplication de l'ADN fongique. Cette sélectivité pour les cellules fongiques (qui possèdent la cytosine désaminase, contrairement aux cellules mammifères) constitue la base de sa sécurité relative chez l'humain.

La Maladie de Paget Osseuse est une pathologie caractérisée par un dysfonctionnement des ostéoclastes avec hyperactivation locale, aboutissant à une résorption et une néoformation osseuses anarchiques. Les voies impliquées sont l'axe RANKL/OPG et la signalisation NF-κB. Le traitement standard repose sur les bisphosphonates.

**Il n'existe aucune intersection mécanistique directe connue** entre le mécanisme de Flucytosine et les voies de la maladie de Paget : Flucytosine n'agit pas sur la différenciation ostéoclastique et ne possède aucune cible documentée dans le métabolisme osseux. Le score TxGNN élevé (0.9904) est très probablement attribuable à une proximité d'embedding dans le graphe de connaissances plutôt qu'à un support biologique — ce cas constitue un exemple typique de faux positif à risque élevé pour les réseaux de neurones sur graphes.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Considerations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction TxGNN atteint un score de 99.04%, mais repose exclusivement sur une similarité d'embedding dans le graphe de connaissances, sans aucun mécanisme biologique plausible, aucun essai clinique, et aucune publication reliant Flucytosine à la Maladie de Paget Osseuse. Le niveau de preuve L5 (prédiction de modèle seule) et l'absence totale de données de sécurité disponibles pour cette base ne permettent pas d'avancer vers une évaluation clinique.

**Pour avancer, les éléments suivants seraient nécessaires :**
- Identification d'un mécanisme d'action biologique plausible reliant Flucytosine ou ses métabolites (5-FU, 5-FUTP, 5-FdUMP) à la voie RANKL/OPG ou NF-κB dans les ostéoclastes
- Données précliniques (études in vitro ou in vivo sur modèles osseux) démontrant un effet sur le remodelage osseux
- Données de sécurité complètes (contre-indications, interactions médicamenteuses, mises en garde) issues de la notice officielle
- Réévaluation de la pertinence clinique après exploration mécanistique — si aucun lien n'est identifié, abandonner cette piste au profit d'indications mieux fondées biologiquement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

