---
layout: default
title: Dupilumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 113
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab : De l'Indication Originale Non Renseignée à la Bronchite

## Résumé en Une Phrase

Dupilumab est un anticorps monoclonal qui bloque le récepteur IL-4Rα (signalisation de l'IL-4 et de l'IL-13). Les données réglementaires françaises fournies ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **bronchite**, mais les preuves sont uniquement indirectes : **1 essai clinique** (dans la rhinosinusite chronique, pas la bronchite) et **6 publications** (surtout sur l'asthme et la BPCO).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM disponibles |
| Nouvelle Indication Prédite | Bronchite |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L4 (preuves indirectes uniquement) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 4 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. On sait néanmoins que dupilumab bloque la sous-unité IL-4Rα, commune aux récepteurs de l'IL-4 et de l'IL-13. Ces deux cytokines pilotent l'inflammation dite de « type 2 ». Ce médicament est déjà utilisé dans des maladies respiratoires de type 2, comme l'asthme et certains phénotypes éosinophiliques.

Le lien avec la bronchite est donc indirect. Il repose sur les données de l'asthme et de la BPCO, ainsi que sur une revue consacrée à la bronchite plastique éosinophilique de l'enfant. Aucun essai n'a évalué dupilumab dans la bronchite elle-même, et le seul essai associé porte sur la rhinosinusite chronique sans polypes nasaux.

Un bénéfice éventuel serait probablement limité aux bronchites avec un profil de type 2 ou éosinophilique. Il ne faut pas l'extrapoler aux bronchites infectieuses ou non éosinophiliques.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Terminé | 33 | Essai randomisé en double aveugle contre placebo dans la rhinosinusite chronique sans polypes nasaux (CRSsNP). Il ne concerne pas la bronchite et apporte seulement un indice d'activité de type 2 dans les voies aériennes supérieures. Résultats non détaillés dans le dossier. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | Extension d'ECR (asthme) | Lancet Respir Med | Étude ouverte (TRAVERSE) évaluant la sécurité et l'efficacité à long terme (au-delà d'un an) dans l'asthme modéré à sévère. |
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Méta-analyse d'ECR (asthme) | J Asthma | Méta-analyse d'ECR contre placebo évaluant l'efficacité et la sécurité dans l'asthme non contrôlé. |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Étude prospective d'imagerie (asthme) | Chest | Effet des biothérapies anti-type 2 sur la ventilation pulmonaire évaluée par IRM chez des adultes asthmatiques dépendants de la prednisone. |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Revue | Tuberc Respir Dis | Revue des traitements pharmacologiques pour prévenir les exacerbations de BPCO, incluant les agents récents. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Revue | Expert Opin Pharmacother | Difficultés de prise en charge de l'asthme associé aux maladies des voies aériennes liées au tabac (dont la bronchite chronique). |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Revue | Pediatr Pulmonol | Revue sur les thérapies récentes de la bronchite plastique éosinophilique pédiatrique (résumé non disponible). |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 64039311 | DUPIXENT 300 mg, solution injectable en stylo prérempli | Solution injectable |
| 64423080 | DUPIXENT 200 mg, solution injectable en seringue préremplie | Solution injectable |
| 64627916 | DUPIXENT 300 mg, solution injectable en seringue préremplie | Solution injectable |
| 66004227 | DUPIXENT 200 mg, solution injectable en stylo prérempli | Solution injectable |

Le titulaire est SANOFI WINTHROP INDUSTRIE pour les quatre AMM. Le texte des indications approuvées n'est pas renseigné dans les données reçues.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction TxGNN est très élevée (99,92 %), mais aucune donnée clinique directe ne l'appuie : le seul essai lié concerne une autre maladie et la littérature porte sur l'asthme, la BPCO et une revue de bronchite éosinophilique.
- Les informations de sécurité et les indications approuvées en France manquent, ce qui empêche une évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (indications approuvées, mises en garde, contre-indications).
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank.
- Préciser la forme de bronchite visée (éosinophilique ou de type 2 versus infectieuse) et rechercher des essais ou séries de cas spécifiques.
- Une piste à explorer en parallèle : la dermatite (niveau de preuve L1) est mieux soutenue, mais il s'agit probablement d'une indication déjà approuvée, donc d'une confirmation d'étiquette plutôt que d'un vrai repositionnement.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

