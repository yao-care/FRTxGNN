---
layout: default
title: Altretamine
parent: Prédiction du modèle uniquement (L5)
nav_order: 49
evidence_level: L5
indication_count: 6
monitor_inn: "altretamine"
predicted_indications: ["female breast carcinoma", "rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "extrahepatic bile duct mucinous adenocarcinoma"]
last_modified_at: 2026-10-28
description: "Altretamine : nouvelle indication prédite, Carcinome du sein chez la femme (female breast carcinoma) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Altretamine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Altrétamine : agent antinéoplasique de la famille des s-triazines → Carcinome du sein chez la femme (female breast carcinoma)
{: .text-alpha }

## Résumé en Une Phrase

L'altrétamine (hexaméthylmélamine) est un médicament anticancéreux de la famille des s-triazines, de type alkylant, qui nécessite une activation métabolique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome du sein chez la femme (female breast carcinoma)**,
mais aucun essai clinique n'est enregistré et seules **3 publications** (précliniques ou indirectes) sont disponibles.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Carcinome du sein chez la femme (female breast carcinoma) |
| Score de Prédiction TxGNN | 0,9991 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'altrétamine est un antinéoplasique de type alkylant de la famille des s-triazines. Elle doit être activée par le métabolisme (N-déméthylation en intermédiaires méthylol réactifs) pour exercer son effet cytotoxique.

Une étude préclinique de 1995 (PMID 7559101) a montré une activité in vivo de l'hexaméthylmélamine sur des xénogreffes de carcinome mammaire humain chez la souris. Une revue systématique de 2023 (PMID 37298753) soutient une activité antitumorale au niveau de la classe des s-triazines, mais ne porte pas directement sur l'altrétamine dans le cancer du sein. Ces éléments rendent la prédiction biologiquement plausible, sans la démontrer chez l'humain.

Aucune étude citée n'évalue directement l'altrétamine chez des patientes atteintes d'un cancer du sein : les données sont précliniques ou de classe. Le niveau de preuve est donc plafonné à L5.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37298753](https://pubmed.ncbi.nlm.nih.gov/37298753/) | 2023 | Revue systématique (classe) | Molecules | Les dérivés s-triazines, dont l'altrétamine, ont une activité antitumorale ; la classe est utilisée dans le cancer de l'ovaire, du sein métastatique et la leucémie |
| [7559101](https://pubmed.ncbi.nlm.nih.gov/7559101/) | 1995 | Préclinique (xénogreffes) | Jpn J Cancer Res | Activité antitumorale in vivo de l'hexaméthylmélamine sur des xénogreffes de carcinome mammaire, gastrique et colique humains chez la souris nude |
| [8411257](https://pubmed.ncbi.nlm.nih.gov/8411257/) | 1993 | Analyse d'intensité de dose (indirecte) | J Natl Cancer Inst | Méta-analyse dans le carcinome ovarien avancé ; seule la dose de cisplatine est associée de façon significative à la réponse |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69985098 | HEXASTAT, gélule | Gélule | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (agent de type alkylant, famille des s-triazines) |
| Risque de Myélosuppression | Données détaillées non disponibles ; leucopénie, thrombopénie et anémie figurent parmi les affections à surveiller |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Numération formule sanguine, fonction hépatique et rénale, examen neurologique (neuropathie périphérique) |
| Protection de Manipulation | À manipuler selon les réglementations applicables aux médicaments cytotoxiques |

## Considérations de Sécurité

- **Affections à risque signalées pour ce médicament** : thrombopénie, maladie du système nerveux périphérique, neuropathie périphérique, anémie (dont anémie macrocytaire), vertige d'origine centrale, leucopénie.
- **Interactions médicamenteuses** : 120 interactions recensées. Parmi elles, des interactions **majeures** avec la déférIprone, le samarium (153Sm) lexidronam et l'adalimumab ; des interactions modérées notamment avec la cimétidine, la pyridoxine, la zidovudine, le chloramphénicol, le ganciclovir, l'alemtuzumab et la doxépine ; des interactions mineures avec la lévofloxacine et la gémifloxacine.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction est portée par un score TxGNN élevé, mais aucun essai clinique n'existe et les données disponibles sont précliniques ou de classe. Les informations de sécurité issues de la notice manquent également.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA)
- Mises en garde et contre-indications issues de la notice de l'ANSM
- Études cliniques ou données observationnelles directement dans le cancer du sein
- Évaluation du rapport bénéfice/risque, compte tenu des toxicités hématologiques et neurologiques
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

