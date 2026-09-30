---
layout: default
title: Atazanavir
parent: Prédiction du modèle uniquement (L5)
nav_order: 46
evidence_level: L5
indication_count: 6
---

# Atazanavir
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

# Atazanavir : Du VIH-1 (usage établi) au Syndrome d'Immunodéficience Acquise Féline

## Résumé en Une Phrase

Atazanavir est un inhibiteur de protéase du VIH-1, utilisé dans le traitement de l'infection par le VIH.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Syndrome d'Immunodéficience Acquise Féline (FIV)**, une indication vétérinaire.
Actuellement, **0 essai clinique** et **0 publication** soutiennent cette direction : il s'agit d'une prédiction du modèle uniquement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les AMM françaises ; inhibiteur de protéase du VIH-1 (usage établi) |
| Nouvelle Indication Prédite | Syndrome d'immunodéficience acquise féline |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Atazanavir inhibe la protéase du VIH-1. Cette enzyme coupe le précurseur polyprotéique Gag-Pol, une étape indispensable à la maturation des virions infectieux. Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier fourni. Ce qui suit repose donc sur la classe pharmacologique connue du médicament.

Le virus de l'immunodéficience féline (FIV) est un lentivirus, comme le VIH-1. Les protéases des lentivirus partagent certaines caractéristiques structurales, d'où un lien plausible au niveau de la classe de médicaments.

Ce lien reste toutefois **non vérifié**. La spécificité de substrat de la protéase du FIV diffère de celle du VIH-1, et l'activité d'atazanavir sur cette cible n'est pas démontrée. Le score TxGNN est très élevé, mais il repose uniquement sur le graphe de connaissances. Par ailleurs, cette indication est vétérinaire et sort du cadre de ce dossier, centré sur l'humain.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69443966 | REYATAZ 150 mg, gélule | Gélule | Non précisée |
| 68301348 | REYATAZ 200 mg, gélule | Gélule | Non précisée |
| 66745660 | REYATAZ 300 mg, gélule | Gélule | Non précisée |

Titulaire pour les trois AMM : Bristol-Myers Squibb Pharma (Irlande).

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction est de niveau L5 : score élevé du modèle, mais aucun essai ni publication. L'indication est vétérinaire, hors du périmètre humain de ce dossier, et la spécificité de la protéase du FIV rend l'activité incertaine.

À titre de contexte, les autres indications prédites pour ce médicament se répartissent ainsi :
- **Complexe apparenté au SIDA** et **VIH congénital** : elles correspondent à l'usage établi d'atazanavir dans l'infection par le VIH. Ce sont des indications déjà couvertes, non de vrais repositionnements. Elles atteignent le niveau L1 avec la décision « Proceed with Guardrails ». Pour le VIH congénital, la population cible n'est que partiellement couverte par les essais, et il faut surveiller l'hyperbilirubinémie, notamment chez le nouveau-né.
- **Infection par le virus de l'immunodéficience simienne** : preuve limitée à une étude animale (niveau L4).
- **Trouble neurodéveloppemental rare** et **hyperlipidémie familiale combinée (terme obsolète)** : probablement des artefacts du graphe de connaissances, à ne pas poursuivre sans hypothèse moléculaire précise.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action (DrugBank) et mises en garde/contre-indications de la notice ANSM, qui manquent actuellement.
- Données précliniques ou de biochimie comparant l'activité d'atazanavir sur la protéase du FIV et sur celle du VIH-1.
- Décision sur la pertinence d'une indication vétérinaire dans ce cadre d'évaluation.
- Remappage du terme obsolète (hyperlipidémie familiale combinée) vers un concept de maladie actuel avant toute revue.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

