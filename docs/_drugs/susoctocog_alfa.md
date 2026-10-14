---
layout: default
title: Susoctocog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 727
evidence_level: L5
indication_count: 10
---

# Susoctocog Alfa
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

# Susoctocog alfa : De l'hémophilie acquise à l'hémophilie (forme congénitale avec inhibiteurs)

## Résumé en Une Phrase

Susoctocog alfa est un facteur VIII recombinant porcin, délété du domaine B, initialement utilisé pour traiter les épisodes hémorragiques de l'hémophilie acquise.
Le modèle TxGNN prédit en première position un effet potentiel sur le **trouble de libération plaquettaire primaire**, une prédiction sans aucune preuve. L'indication la mieux documentée parmi les dix prédictions est l'**hémophilie** (1 étude d'observation et 20 publications), mais ces données portent surtout sur la forme acquise, c'est-à-dire l'indication d'origine.

> Remarque : la prédiction classée n°1 (trouble de libération plaquettaire primaire) ne repose sur aucune preuve (niveau L5). Cette analyse s'attarde donc sur l'hémophilie (rang 4), seule prédiction avec des éléments cliniques exploitables, et sur le déficit acquis en facteur de coagulation (rang 5).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémophilie acquise (l'indication approuvée n'est pas renseignée dans les données d'AMM) |
| Nouvelle Indication Predite (rang 1) | Trouble de libération plaquettaire primaire |
| Indication la mieux documentée | Hémophilie (rang 4) |
| Score de Prédiction TxGNN | 99,94 % (rang 1) ; 99,74 % (hémophilie) |
| Niveau de Preuve | L5 (rang 1) ; L3 (hémophilie) |
| Statut de Marché en France | Uniquement annulée |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold (rang 1) ; Proceed with Guardrails pour le déficit acquis en facteur de coagulation, qui correspond en pratique à l'indication d'origine |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, susoctocog alfa est un facteur VIII (FVIII) recombinant de séquence porcine, délété du domaine B. Son efficacité dans l'hémophilie acquise a été démontrée. Il apporte une activité FVIII tout en réagissant peu avec les auto-anticorps dirigés contre le FVIII humain.

**Prédiction n°1 (trouble de libération plaquettaire primaire)** : ce trouble est un défaut de la fonction plaquettaire, et non un déficit en FVIII. Le lien mécanistique est faible. Le score élevé semble refléter la proximité générale, dans le réseau de connaissances, entre les maladies hémorragiques. Il en va de même pour les autres prédictions plaquettaires ou hors coagulation : pseudo-maladie de von Willebrand, thrombasthénie de Glanzmann, syndrome de Scott, défaut du récepteur du collagène, thrombopénie constitutionnelle, déficit en facteur XIII et déficit en adénosine désaminase. Aucune ne dispose d'essai ni de publication.

**Hémophilie (rang 4)** : le lien mécanistique est direct, puisque le médicament apporte l'activité FVIII manquante. Toutefois, les publications soutiennent surtout la forme acquise, qui est l'indication d'origine. Pour l'hémophilie A congénitale avec inhibiteurs, les données se limitent à une étude de phase 3 à bras unique en chirurgie, à une étude in vitro de génération de thrombine et à des revues, des séries et des cas.

## Preuves d'Essais Cliniques

Pour la prédiction n°1, aucun essai clinique associé n'est enregistré actuellement. Pour l'hémophilie (rang 4) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT06461533](https://clinicaltrials.gov/study/NCT06461533) | N/A | En recrutement | 25 | Enquête japonaise de suivi de tous les cas traités par OBIZUR dans l'hémophilie acquise A. Elle évalue les effets indésirables et l'efficacité en conditions réelles. Il s'agit d'une étude observationnelle sur l'indication déjà approuvée. |

## Preuves de la Littérature

Pour la prédiction n°1, aucune littérature associée n'est disponible actuellement. Pour l'hémophilie (rang 4), voici une sélection des publications les plus pertinentes :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39158833](https://pubmed.ncbi.nlm.nih.gov/39158833/) | 2024 | Étude clinique prospective de phase II/III | Int J Hematol | Efficacité et sécurité du FVIII porcin recombinant chez des patients japonais atteints d'hémophilie acquise, avec une dose initiale de 200 U/kg. |
| [38317504](https://pubmed.ncbi.nlm.nih.gov/38317504/) | 2024 | Phase 3, bras unique | Haemophilia | FVIII porcin recombinant chez des patients atteints d'hémophilie A congénitale avec inhibiteurs, lors d'une chirurgie. |
| [27098420](https://pubmed.ncbi.nlm.nih.gov/27098420/) | 2016 | Revue | Drugs | Efficacité et bonne tolérance dans les saignements graves de l'hémophilie acquise (essai de phase II/III, n = 28 évaluables). |
| [35765670](https://pubmed.ncbi.nlm.nih.gov/35765670/) | 2022 | Étude in vitro | Res Pract Thromb Haemost | Le FVIII porcin recombinant corrige la génération de thrombine dans le plasma de patients atteints d'hémophilie A congénitale avec inhibiteurs. |
| [32698943](https://pubmed.ncbi.nlm.nih.gov/32698943/) | 2020 | Série de cas | Blood Transfus | Expérience italienne en conditions réelles chez 9 patients âgés atteints d'hémophilie acquise. |
| [37510704](https://pubmed.ncbi.nlm.nih.gov/37510704/) | 2023 | Série de cas et revue | J Clin Med | Chirurgie et prophylaxie par susoctocog alfa dans l'hémophilie acquise. |
| [40812597](https://pubmed.ncbi.nlm.nih.gov/40812597/) | 2025 | Étude pharmacocinétique | J Thromb Haemost | Stratégies pharmacocinétiques pour un contrôle précis du FVIII dans l'hémophilie acquise. |
| [31448877](https://pubmed.ncbi.nlm.nih.gov/31448877/) | 2020 | Étude de cohorte | J Thromb Haemost | Inhibiteurs à réactivité croisée contre le FVIII porcin recombinant dans l'hémophilie acquise. |
| [37584309](https://pubmed.ncbi.nlm.nih.gov/37584309/) | 2023 | Observationnelle en conditions réelles | Haemophilia | Étude post-autorisation de sécurité et d'efficacité dans l'hémophilie acquise (publication liée au déficit acquis en facteur de coagulation). |
| [41436689](https://pubmed.ncbi.nlm.nih.gov/41436689/) | 2025 | Cas clinique | CEN Case Rep | Initiation d'une hémodialyse chez un patient atteint d'hémophilie acquise, pris en charge par susoctocog alfa et emicizumab. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65982247 | OBIZUR 500 U, poudre et solvant pour solution injectable (BAXALTA INNOVATIONS, Autriche) | Poudre et solvant pour solution injectable | Non renseignée ; AMM annulée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les mises en garde, contre-indications et interactions médicamenteuses ne sont pas disponibles dans les données compilées pour ce rapport.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction n°1 (trouble de libération plaquettaire primaire), comme la plupart des autres prédictions, repose uniquement sur le modèle (L5) et n'a pas de plausibilité mécanistique : ces maladies sont des défauts plaquettaires ou d'autres voies, sans lien avec le FVIII.
- Le déficit acquis en facteur de coagulation (Proceed with Guardrails, L3) correspond en pratique à l'indication d'origine, et non à un véritable repositionnement. L'hémophilie (L3, Research Question) ne dispose que d'une étude de surveillance post-commercialisation et de publications surtout centrées sur la forme acquise.
- La seule AMM française est annulée, et les données de sécurité de la notice sont absentes, ce qui bloque le criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde, contre-indications) : lacune bloquante.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Confirmer la disponibilité du produit en France, l'AMM étant annulée.
- Pour toute piste dans l'hémophilie congénitale avec inhibiteurs, évaluer les données de phase 3 existantes. Garde-fous : suivi de l'activité FVIII, surveillance des événements thrombotiques et dosage des anticorps anti-porcins.
- Abandonner ou déprioriser les prédictions plaquettaires et non coagulantes, faute de justification mécanistique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

