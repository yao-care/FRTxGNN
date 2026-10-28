---
layout: default
title: Durvalumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 265
evidence_level: L5
indication_count: 6
monitor_inn: "DURVALUMAB"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-23
description: "Durvalumab : nouvelle indication prédite, Adénocarcinome du ligament utérin (prédiction de rang 1) (niveau de preuve L5). Indication d'origine : Carcinome à cellules transitionnelles"
---

# Durvalumab
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

## Durvalumab : Du Carcinome à Cellules Transitionnelles à l'Adénocarcinome du ligament utérin
{: .text-alpha }

## Resume en Une Phrase

Le durvalumab est un anticorps monoclonal dont l'usage d'origine, tel qu'enregistré dans le graphe de connaissances utilisé par le modèle, est le carcinome à cellules transitionnelles (cancer urothélial).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **carcinome endocervical**, mais les preuves restent très limitées : **1 essai clinique** de phase 1 (combinaison) et **2 publications** non directement centrées sur cette maladie.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Carcinome à cellules transitionnelles (relation enregistrée dans le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné dans les données compilées) |
| Nouvelle Indication Predite | Adénocarcinome du ligament utérin (prédiction de rang 1) ; carcinome endocervical (prédiction de rang 2, la seule avec des données de soutien) |
| Score de Prediction TxGNN | 0,9992 (rang 1) ; 0,9991 (carcinome endocervical) |
| Niveau de Preuve | L5 (aucune étude citée ne porte directement sur le carcinome endocervical lui-même ; l'unique essai concerne un cancer du col, du vagin ou de la vulve en association) |
| Statut de Marche en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Decision Recommandee | Hold |

Remarque : la prédiction classée en premier (adénocarcinome du ligament utérin) ne dispose d'aucun essai ni publication. Les sections suivantes détaillent le carcinome endocervical, seule prédiction accompagnée de données, tout en restant prudent sur leur portée.

## Pourquoi Cette Prediction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. D'après les connaissances générales, le durvalumab est un anticorps dirigé contre PD-L1 : il bloque l'inhibition des lymphocytes T et rétablit ainsi leur activité antitumorale.

Les carcinomes du col utérin sont souvent liés au papillomavirus humain (HPV) et expriment fréquemment PD-L1, ce qui offre une justification biologique plausible pour une inhibition des points de contrôle immunitaires. Le lien avec l'indication d'origine (tumeur urothéliale) repose sur ce mécanisme commun d'échappement immunitaire, et non sur une parenté histologique.

Cette justification reste une hypothèse : l'efficacité dans le carcinome endocervical n'a pas été démontrée. Le seul essai disponible associe le durvalumab au trémélimumab et à une radiothérapie, de sorte que l'apport du durvalumab seul ne peut pas être isolé.

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | Terminé | 20 | Radiothérapie hypofractionnée associée au durvalumab et au trémélimumab chez des patientes atteintes d'un cancer du col, du vagin ou de la vulve récidivant ou métastatique ; données de faisabilité et de sécurité précoces, sans démonstration d'efficacité propre au carcinome endocervical |

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Revue | Biomedical Journal | Carcinome neuroendocrine à petites cellules du col : base moléculaire et avancées thérapeutiques ; données limitées à des séries et rapports de cas |
| [42518016](https://pubmed.ncbi.nlm.nih.gov/42518016/) | 2026 | Essai non randomisé | Oncology and Therapy | Céralasertib plus durvalumab chez des patients chinois atteints de tumeurs solides avancées (phase 1, sécurité, pharmacocinétique, activité antitumorale) ; non spécifique au col utérin |

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 63690956 | IMFINZI 50 mg/ml, solution à diluer pour perfusion | Solution à diluer pour perfusion | Texte d'indication non renseigné dans les données compilées |

Le durvalumab est commercialisé en France (1 AMM valide, titulaire : AstraZeneca AB).

## Cytotoxicite

| Element | Contenu |
|------|------|
| Classification de Cytotoxicite | Immunothérapie (anticorps anti-PD-L1) |
| Risque de Myelosuppression | Faible (pas de cytotoxicité conventionnelle) |
| Classification d'Emetogenicite | Faible |
| Elements de Surveillance | NFS, fonction hépatique, rénale, thyroïdienne et surrénalienne (effets indésirables immuno-médiés) |
| Protection de Manipulation | Veuillez consulter la notice pour les précautions de manipulation |

## Considerations de Securite

**Interactions Médicamenteuses** : 81 interactions ont été recensées. Les principales :
- **Majeure** : adalimumab
- **Modérée** : corticoïdes (hydrocortisone, triamcinolone, dexaméthasone, bétaméthasone, budésonide, prednisolone, prednisone, méthylprednisolone, déflazacort), roflumilast, alefacept, alemtuzumab, anakinra, vaccin antitétanique, vaccin anticharbonneux
- **Mineure** : sels de zinc (acétate, gluconate, sulfate, chlorure)

Veuillez consulter la notice pour les mises en garde et contre-indications.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- Le score TxGNN est très élevé (> 0,9990), mais il provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique. Aucune étude citée ne porte directement sur le carcinome endocervical, ce qui limite le niveau de preuve à L5. Cinq des six prédictions n'ont aucune donnée de soutien et concernent des tumeurs très rares.

**Pour avancer, les elements suivants sont necessaires :**
- Données sur le mécanisme d'action (MOA) et analyse du lien mécanistique
- Mises en garde et contre-indications issues de la notice de l'ANSM
- Texte de l'indication de l'AMM pour confirmer l'usage approuvé
- Données d'efficacité sur le carcinome endocervical (expression de PD-L1, essais de phase 2 ciblés)
- Évaluation de la faisabilité d'essais pour ces tumeurs rares
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

