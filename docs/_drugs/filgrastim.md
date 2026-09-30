---
layout: default
title: Filgrastim
parent: Prédiction du modèle uniquement (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
---

# Filgrastim
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Filgrastim : Du Facteur de Croissance des Neutrophiles au Trouble Primaire de la Libération Plaquettaire

## Résumé en Une Phrase

Filgrastim est un facteur de stimulation des colonies de granulocytes (G-CSF). Il agit sur la lignée des neutrophiles et sur la mobilisation des cellules souches hématopoïétiques. Le texte de son indication originale n'est pas renseigné dans les données disponibles.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble primaire de la libération plaquettaire**, avec un score très élevé.
Cette prédiction repose sur **14 essais cliniques associés** et **1 publication**, mais aucun ne teste réellement le filgrastim dans cette maladie. La prédiction reste donc, en pratique, purement issue du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Trouble primaire de la libération plaquettaire |
| Score de Prédiction TxGNN | 99,998 % |
| Niveau de Preuve | L4 (indirect : aucune étude ne cible cette maladie) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 16 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le filgrastim est un G-CSF dont l'action établie porte sur la production de neutrophiles et la mobilisation des cellules souches.

**La prédiction est peu plausible sur le plan mécanistique.** Les troubles de la libération plaquettaire sont des défauts fonctionnels des plaquettes (sécrétion des granules). Aucune voie reliant la signalisation du G-CSF à la sécrétion plaquettaire n'est identifiable. Le score élevé (0,99998) est une prédiction issue du graphe de connaissances, qui ne remplace pas une preuve pharmacologique.

Les 14 essais associés sont surtout des protocoles de greffe de cellules souches hématopoïétiques. Le G-CSF y sert probablement d'agent de soutien ou de mobilisation. La correspondance vient vraisemblablement de termes communs liés à la greffe, et non d'un traitement de ce trouble.

Les autres indications prédites (pseudo-maladie de von Willebrand, thrombasthénie de Glanzmann, syndrome de Scott, etc.) présentent le même problème. Aucune n'a de lien mécanistique connu avec le G-CSF.

## Preuves d'Essais Cliniques

Les 10 essais les plus pertinents sont listés ci-dessous. Tous ont été jugés de faible pertinence ou non évalués pour cette indication.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Arrêté | 200 | Greffe de cellules souches de donneur non apparenté dans les hémopathies malignes. Le G-CSF n'est pas l'intervention testée. |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Terminé | 60 | Greffe allogénique/syngénique de cellules souches dans les sarcomes pédiatriques à haut risque |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Phase 2 | Arrêté | 16 | Greffe de sang de cordon pour leucémie myéloïde avec cellules NK |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Terminé | 19 | Greffe à conditionnement réduit chez des patients porteurs de mutations GATA2 |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Terminé | 64 | Autogreffe avec ou sans sélection CD34+ dans le lymphome du manteau et le lymphome B diffus à grandes cellules |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | En recrutement | 260 | Dose minimale efficace de cyclophosphamide post-greffe pour la prophylaxie de la GVHD |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Terminé | 9 | Lymphodéplétion intensifiée et autogreffe dans le lupus érythémateux systémique sévère |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | En recrutement | 358 | Protocole plateforme de prophylaxie de la GVHD à base de cyclophosphamide post-greffe |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | En recrutement | 156 | Autogreffe versus meilleur traitement disponible dans la sclérose en plaques résistante |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Terminé | 147 | Greffe non myéloablative (busulfan, fludarabine, irradiation corporelle totale) dans les hémopathies malignes |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Étude de mobilisation chez donneurs sains (type non précisé) | Frontiers in Immunology | La mobilisation des cellules souches par G-CSF chez des donneurs sains entraîne une mobilisation préférentielle de certains sous-ensembles de lymphocytes. Aucun lien avec les troubles plaquettaires. |

## Informations de Marché en France

Cinq AMM principales sur 16 sont listées. Le texte de l'indication approuvée n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 60670037 | ZARZIO 30 MU/0,5 mL, seringue préremplie | Solution injectable ou pour perfusion | SANDOZ (Autriche) |
| 66749096 | NEUPOGEN 48 MU/0,5 mL (0,96 mg/mL), seringue préremplie | Solution injectable | AMGEN EUROPE |
| 69287684 | NIVESTIM 30 MU/0,5 mL | Solution injectable ou pour perfusion | PFIZER EUROPE MA EEIG (Belgique) |
| 69225686 | NEUPOGEN 30 MU (0,3 mg/mL) | Solution injectable | AMGEN EUROPE |
| 65313021 | TEVAGRASTIM 48 MUI/0,8 mL | Solution injectable ou pour perfusion | TEVA (Allemagne) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai ni publication ne teste le filgrastim dans le trouble primaire de la libération plaquettaire, et aucun lien mécanistique plausible n'est identifiable. Le score TxGNN élevé n'est corroboré par aucune donnée clinique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM, indispensables au criblage de sécurité
- Les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Les textes d'indication approuvée des AMM françaises
- Une justification biologique reliant la voie du G-CSF à la sécrétion plaquettaire, ou des études précliniques dans cette maladie
- Une revue manuelle des essais restés sans évaluation de pertinence

*Ce rapport est fourni à titre de référence pour la recherche et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

