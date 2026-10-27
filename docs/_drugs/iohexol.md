---
layout: default
title: Iohexol
parent: Prédiction du modèle uniquement (L5)
nav_order: 407
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Iohexol : nouvelle indication prédite, Insomnie (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM (produit de contraste radiologi…"
monitor_inn: "IOHEXOL"
predicted_indications: ["insomnia (disease)", "anxiety"]
---

# Iohexol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Iohexol : D'un produit de contraste iodé à l'insomnie (prédiction non étayée)
{: .text-alpha }

## Résumé en Une Phrase

Iohexol est un produit de contraste radiologique iodé non ionique, utilisé en imagerie médicale (indication originale non renseignée dans les données d'AMM compilées).
Le modèle TxGNN le prédit comme potentiellement efficace pour l'**insomnie**, mais **aucun essai clinique** et **aucune publication** ne soutiennent cette direction.
Une seconde prédiction, l'**anxiété**, est également signalée, avec 4 publications sans lien thérapeutique réel.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM (produit de contraste radiologique iodé) |
| Nouvelle Indication Prédite | Insomnie |
| Score de Prédiction TxGNN | 99,87 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, iohexol est un produit de contraste iodé non ionique, pharmacologiquement inerte et non métabolisé. Son rôle est d'opacifier les structures lors d'examens d'imagerie, et non d'agir sur une cible thérapeutique.

**Il n'existe pas de lien mécanistique identifié** avec l'insomnie. Iohexol n'a pas d'activité connue sur les cibles de régulation du sommeil (récepteurs GABA, orexine, histamine, mélatonine). Le score TxGNN très élevé (99,87 %) est une prédiction issue d'un graphe de connaissances. Il reflète probablement des artefacts de réseau, comme le grand nombre de liens d'interactions médicamenteuses (100), plutôt qu'une plausibilité biologique.

Pour l'anxiété (score de 99,25 %), la conclusion est la même : aucun effet anxiolytique pharmacologique n'est connu, et les publications retrouvées ne mentionnent l'anxiété que de façon incidentale.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée à l'insomnie disponible actuellement.

À titre informatif, quatre publications ont été retrouvées pour la seconde prédiction (anxiété). Aucune ne teste iohexol comme traitement de l'anxiété :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8883531](https://pubmed.ncbi.nlm.nih.gov/8883531/) | 1996 | ECR | Academic Radiology | Comparaison en double aveugle de l'iodixanol et de l'iohexol en phlébographie des membres ; évalue l'efficacité, la sécurité et l'inconfort à l'injection, pas l'anxiété |
| [2352635](https://pubmed.ncbi.nlm.nih.gov/2352635/) | 1990 | Cohorte observationnelle | Neuroradiology | Effets indésirables après myélographie lombaire à l'iohexol (200 patients) ; l'anxiété figure parmi les symptômes mentaux mineurs rapportés |
| [2125805](https://pubmed.ncbi.nlm.nih.gov/2125805/) | 1990 | Étude physiologique clinique | Acta Neurochirurgica | Suivi hémodynamique par Doppler transcrânien pendant l'angiographie cérébrale |
| [39861464](https://pubmed.ncbi.nlm.nih.gov/39861464/) | 2025 | Revue | Nutrients | Nutrition et activité physique en onco-néphrologie ; sans rapport avec l'efficacité d'iohexol |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65106581 | OMNIPAQUE 300 mg d'I/mL, solution injectable | Solution injectable | Non renseignée (AMM annulée) |
| 63688752 | OMNIPAQUE 180 mg d'I/mL, solution injectable | Solution injectable | Non renseignée (AMM annulée) |
| 66892062 | OMNIPAQUE 240 mg d'I/mL, solution injectable | Solution injectable | Non renseignée (AMM annulée) |
| 67846776 | OMNIPAQUE 350 mg d'I/mL, solution injectable | Solution injectable | Non renseignée (AMM annulée) |

Les quatre AMM sont détenues par GE Healthcare et sont toutes annulées.

---

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Interactions Médicamenteuses** : 100 interactions sont recensées. Parmi les principales de niveau **majeur** :
  - Corticoïdes : hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone
  - Metformine
  - Amphotéricine B (y compris le complexe lipidique)
  - Antibiotiques : vancomycine, kanamycine, néomycine, lévofloxacine
  - Mésalazine et balsalazide
  - Bupropion, morphine, métoclopramide
  - Diéthylpropion, phentermine, dronabinol

  Une interaction de niveau **modéré** est notée avec le mannitol.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Iohexol est un produit de contraste inerte, sans mécanisme plausible dans l'insomnie ni l'anxiété. Le score TxGNN élevé ne s'appuie sur aucun essai clinique ni aucune publication pertinente (niveau L5).
- Les quatre AMM sont annulées, et les données de sécurité de la notice manquent, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice de l'ANSM (mises en garde et contre-indications)
- Données détaillées sur le mécanisme d'action (DrugBank)
- Justification biologique de tout lien avec le sommeil ou l'anxiété, avant d'envisager des études précliniques
- Vérification que le score ne résulte pas d'un artefact du graphe (nombre élevé d'interactions médicamenteuses)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

