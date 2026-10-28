---
layout: default
title: Articaine
parent: Prédiction du modèle uniquement (L5)
nav_order: 73
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Articaine : nouvelle indication prédite, Goutte (niveau de preuve L5). Indication d'origine : Non précisée dans les données compilées (anesthésie dentaire d'après…"
monitor_inn: "articaine"
predicted_indications: ["gout", "exostosis", "allergic asthma", "intrinsic asthma"]
---

# Articaine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

## Articaïne : De l'anesthésie locale dentaire à la goutte
{: .text-alpha }

## Résumé en Une Phrase

L'articaïne est un anesthésique local de type amide, utilisé à l'origine pour l'anesthésie dentaire par infiltration.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **goutte**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction issue uniquement du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données compilées (anesthésie dentaire d'après la forme pharmaceutique « solution injectable à usage dentaire ») |
| Nouvelle Indication Prédite | Goutte |
| Score de Prédiction TxGNN | 0,9958 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales, l'articaïne est un anesthésique local de type amide qui bloque les canaux sodiques et est utilisé pour l'anesthésie dentaire et par infiltration.

Aucun lien mécanistique établi n'existe avec la goutte. L'articaïne n'a pas d'effet connu sur le métabolisme de l'acide urique, sur la xanthine oxydase ni sur l'inflammation liée aux cristaux d'urate (voie NLRP3). Le score élevé (0,9958) reflète une prédiction du modèle TxGNN (apprentissage profond), sans support clinique ni bibliographique. Au mieux, un rationnel se limiterait à l'analgésie locale lors de crises aiguës, ce qui serait purement symptomatique et non modificateur de la maladie.

Les autres indications prédites présentent le même profil : exostose (rang 2, score 0,9942), asthme allergique (rang 3, 0,9938) et asthme intrinsèque (rang 4, 0,9934). Toutes sont de niveau L5, sans lien mécanistique identifié.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la goutte.

À titre d'information, deux publications ont été retrouvées pour l'indication de rang 3 (asthme allergique). Elles portent sur l'allergie *aux* anesthésiques locaux et non sur un traitement de l'asthme par l'articaïne ; elles ne constituent pas une preuve d'efficacité.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38404118](https://pubmed.ncbi.nlm.nih.gov/38404118/) | 2024 | Cohorte | Pediatric Allergy and Immunology | Évaluation des tests diagnostiques de l'allergie aux anesthésiques locaux chez l'enfant, en conditions réelles |
| [21507228](https://pubmed.ncbi.nlm.nih.gov/21507228/) | 2011 | Étude expérimentale (allergie) | Allergy, Asthma, and Clinical Immunology | Allergie retardée à la prilocaïne ; pas de réactivité croisée observée avec la lidocaïne, l'articaïne et la mépivacaïne |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69602201 | ALPHACAINE SP, solution injectable à usage dentaire | Solution injectable pour usage dentaire | Non renseignée (AMM active) |
| 66862795 | ALPHACAINE N, solution injectable à usage dentaire | Solution injectable pour usage dentaire | Non renseignée (AMM active) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie du graphe, et non texte de la notice) : hypertension, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, diabète et acidocétose diabétique, maladie coronarienne et infarctus du myocarde, mort cardiaque subite, maladie de la conduction cardiaque, cardiopathies et cardiomyopathie dilatée, hémoglobinopathie, glaucome à angle fermé, myasthénie et maladies de la jonction neuromusculaire, déficit en butyrylcholinestérase, hyperthyroïdie (maladie de Basedow, thyrotoxicose), maladie de Parkinson et syndromes parkinsoniens.
- **Interactions médicamenteuses** (10 recensées) :
  - Majeure : acide nitreux
  - Modérées : morphine liposomale, benzocaïne (topique), lidocaïne (ophtalmique et topique), oxybuprocaïne (ophtalmique), cinchocaïne (topique), tétracaïne (ophtalmique et topique)
  - Mineure : hyaluronidase
- **Point d'attention pour l'asthme** : certaines préparations associées à l'épinéphrine peuvent contenir des sulfites, ce qui peut être préoccupant chez les patients asthmatiques. Les publications retrouvées signalent aussi une vigilance quant à l'hypersensibilité chez les patients atopiques.

Les mises en garde et contre-indications de la notice ANSM n'ont pas pu être obtenues ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5) : aucun essai, aucune publication pertinente et aucun lien mécanistique plausible avec la goutte. De plus, le médicament est commercialisé en France, avec 2 AMM valides sur 2.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mécanisme d'action détaillé (interrogation de DrugBank)
- Mises en garde et contre-indications de la notice ANSM (blocage de l'étape de sécurité S1 tant que ce point n'est pas résolu)
- Hypothèse mécanistique crédible et données précliniques reliant l'articaïne à la goutte
- Indication originale précise et vérification de la compatibilité de voie d'administration (actuellement injectable dentaire uniquement)
- Revue de littérature ciblée, puis éventuellement des études exploratoires avant toute réévaluation
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

