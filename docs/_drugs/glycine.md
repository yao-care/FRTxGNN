---
layout: default
title: Glycine
parent: Prédiction du modèle uniquement (L5)
nav_order: 141
evidence_level: L5
indication_count: 2
---

# Glycine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Glycine : Des Produits Commercialisés (Indication Non Renseignée) à la Maladie de la Cavité Nasale

## Résumé en Une Phrase

La glycine est un acide aminé présent dans plusieurs produits commercialisés en France, notamment des solutions d'acides aminés pour perfusion et un comprimé de magnésium glycocolle. Aucune indication d'origine n'est renseignée dans les données disponibles.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie de la cavité nasale**, mais cette prédiction repose **uniquement sur le modèle** : **1 essai clinique** et **2 publications** sont associés, et aucun ne teste réellement la glycine dans cette indication.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Maladie de la cavité nasale (nasal cavity disease) |
| Score de Prédiction TxGNN | 99,85 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la glycine entre dans la composition de solutions d'acides aminés pour perfusion et de sels de magnésium. Son indication d'origine n'est pas renseignée dans les données réglementaires fournies. Aucun lien mécanistique direct avec la maladie de la cavité nasale n'est démontré.

Un lien plausible mais **non vérifié** existe : la glycine aurait une activité cytoprotectrice et anti-inflammatoire, décrite comme passant par les canaux chlorure activés par la glycine sur les cellules immunitaires et épithéliales. Ce mécanisme pourrait théoriquement concerner une muqueuse nasale inflammatoire, mais rien dans le dossier ne le confirme.

Le score TxGNN très élevé (0,998) est une prédiction issue d'un graphe de connaissances. Il n'est soutenu ici par aucune preuve clinique.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Phase 1/2 | Terminé | 25 | Imagerie TEP/TDM ou TEP/IRM par 18F-FPPRGD2 (expression des intégrines αvβ3, biomarqueur d'angiogenèse) chez des patients atteints de glioblastome, de cancers gynécologiques et de cancer du rein sous traitement antiangiogénique |

**Pertinence :** cet essai est jugé peu pertinent (grade C). La glycine n'est pas l'intervention testée et la population ne concerne pas une maladie de la cavité nasale. Il ne peut donc pas soutenir l'indication prédite.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Étude fondamentale/histologique (tissu bovin) | Veterinary Pathology | Histochimie des lectines de la muqueuse nasale bovine normale ou infectée par l'herpèsvirus bovin 1 ; sans lien direct avec la glycine |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Étude préclinique de formulation | Chemical & Pharmaceutical Bulletin | Effet de la structure d'oligoarginines conjuguées à des polymères comme adjuvant muqueux pour l'induction d'anticorps dans les cavités nasales (souris) ; sans lien direct avec la glycine |

Ces deux publications ne testent pas la glycine dans une maladie nasale. Elles ne fournissent qu'un contexte général sur la muqueuse nasale.

## Informations de Marché en France

Sur 20 AMM au total, voici 5 AMM principales. Le texte d'indication approuvée n'est pas renseigné pour ces produits.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 60840614 | MAGNESIUM GLYCOCOLLE LAFARGE (SERP) | Comprimé pelliculé |
| 61960303 | AMINOVEN 10 POUR CENT (Fresenius Kabi France) | Solution pour perfusion |
| 69667989 | AMINOVEN 5 POUR CENT (Fresenius Kabi France) | Solution pour perfusion |
| 63183821 | AMINOPLASMAL 8 (B Braun Melsungen) | Solution pour perfusion |
| 61786735 | AMINOMIX 500 (Fresenius Kabi France) | Solution et solution pour perfusion |

Les formes commercialisées sont orales (comprimé) ou injectables (perfusion, émulsion, dialyse péritonéale). Aucune forme nasale n'est listée, ce qui pose la question de la compatibilité de voie d'administration.

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est de niveau L5 (modèle seul). Le seul essai clinique et les deux publications associés ne testent pas la glycine dans une maladie nasale.
- Le mécanisme d'action et les données de sécurité sont absents, et aucune voie d'administration compatible n'est identifiée.
- La seconde prédiction du modèle, la laryngopharyngite aiguë (99,84 %), est aussi de niveau L5 et Hold, sans preuve directe.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser les notices ANSM (mises en garde et contre-indications), point bloquant pour le criblage de sécurité
- Obtenir le mécanisme d'action détaillé via DrugBank
- Compléter les indications approuvées des AMM françaises pour identifier l'indication d'origine
- Mener une recherche ciblée d'études sur la glycine dans les pathologies nasales (essais cliniques, études précliniques)
- Évaluer la compatibilité des voies d'administration, aucune forme nasale n'étant disponible

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

