---
layout: default
title: Brinzolamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 115
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Brinzolamide : nouvelle indication prédite, Glaucome héréditaire primaire (niveau de preuve L5). Indication d'origine : Glaucome à angle ouvert, hypertension oculaire"
---

# Brinzolamide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Brinzolamide : Du Glaucome à Angle Ouvert au Glaucome Héréditaire Primaire
{: .text-alpha }

## Résumé en Une Phrase

Brinzolamide est un inhibiteur de l'anhydrase carbonique, initialement utilisé en collyre pour le traitement du glaucome à angle ouvert et de l'hypertension oculaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **glaucome héréditaire primaire**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Glaucome à angle ouvert, hypertension oculaire (le texte d'indication des AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Glaucome héréditaire primaire |
| Score de Prédiction TxGNN | 99,48 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 13 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, le brinzolamide est un inhibiteur de l'anhydrase carbonique II. Il réduit la sécrétion d'humeur aqueuse et fait ainsi baisser la pression intraoculaire (PIO). Ce mécanisme n'a pas pu être vérifié par des données de cibles validées.

Le glaucome héréditaire primaire (par exemple le glaucome congénital primaire, souvent lié à des variants de CYP1B1 ou MYOC) se caractérise lui aussi par une PIO élevée. La voie ciblée est donc la même que pour les indications approuvées, ce qui explique le score élevé du modèle.

Il faut toutefois nuancer : ces glaucomes résultent surtout d'une dysgénésie du trabéculum et des voies d'écoulement, et sont souvent traités chirurgicalement. Un suppresseur de l'humeur aqueuse comme le brinzolamide serait au mieux un traitement d'appoint ou temporaire. De plus, la nouvelle indication est très proche de l'indication d'origine : la nouveauté du repositionnement est limitée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 13 AMM recensées sont toutes annulées ; aucune n'est actuellement valide. Le texte d'indication approuvée n'est pas renseigné. Les 5 premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60868670 | AZOPT 10 mg/ml | Collyre en suspension | Non renseignée |
| 68305211 | BRINZOLAMIDE ARROW 10 mg/mL | Collyre en suspension | Non renseignée |
| 66126291 | BRINZOLAMIDE EG 10 mg/ml | Collyre en suspension | Non renseignée |
| 64907754 | BRINZOLAMIDE SANDOZ 10 mg/mL | Collyre en suspension | Non renseignée |
| 62196488 | BRINZOLAMIDE CRISTERS 10 mg/ml | Collyre en suspension | Non renseignée |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 32 interactions ont été identifiées, mais leur niveau de gravité n'est pas classé. Parmi les principales substances concernées : pantoprazole, oméprazole, lansoprazole, triamcinolone, prednisone, prednisolone, dexaméthasone, simvastatine, rosuvastatine, warfarine, clopidogrel, chlorure de potassium, pioglitazone, métoclopramide, ranitidine, famotidine, cétirizine, fexofénadine, salbutamol et lactulose.

Veuillez consulter la notice pour les mises en garde et contre-indications, qui ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. La nouveauté est limitée car l'indication est proche de l'indication d'origine, et les 13 AMM françaises sont toutes annulées. Les données de sécurité de la notice manquent, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice (ANSM) pour les mises en garde et contre-indications
- Obtenir les données sur le mécanisme d'action (par exemple via DrugBank)
- Rechercher des études cliniques ou observationnelles dans le glaucome héréditaire ou congénital
- Clarifier les raisons de l'annulation des AMM et la disponibilité réelle du produit en France
- Évaluer la place d'un traitement d'appoint par rapport à la chirurgie, et la pertinence en population pédiatrique
- Qualifier le niveau de gravité des interactions médicamenteuses
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

