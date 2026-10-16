---
layout: default
title: Cabergoline
parent: Prédiction du modèle uniquement (L5)
nav_order: 127
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Cabergoline : nouvelle indication prédite, Cancer de l'hypophyse (niveau de preuve L5). Indication d'origine : Hyperprolactinémie (y compris formes familiale et acquise) et tumeur…"
---

# Cabergoline
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Cabergoline : De l'hyperprolactinémie au cancer de l'hypophyse

## Résumé en Une Phrase

Cabergoline est un agoniste dopaminergique D2, initialement utilisé pour traiter l'hyperprolactinémie et les tumeurs hypophysaires sécrétant de la prolactine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **cancer de l'hypophyse**, avec **12 essais cliniques** et **20 publications** associés à cette direction. Ces preuves portent toutefois surtout sur les adénomes hypophysaires, majoritairement bénins, et non sur le carcinome hypophysaire proprement dit.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hyperprolactinémie (y compris formes familiale et acquise) et tumeur hypophysaire sécrétant de la prolactine (source : graphe de connaissances, aucun texte d'indication n'est renseigné dans les AMM) |
| Nouvelle Indication Prédite | Cancer de l'hypophyse |
| Score de Prédiction TxGNN | 99,04 % |
| Niveau de Preuve | L1 (selon l'application stricte des règles : ≥ 2 ECR de phase 3 terminés ; voir réserve ci-dessous) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 6 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

> **Réserve sur le niveau de preuve :** les essais de phase 3 terminés concernent les adénomes corticotropes et les adénomes non fonctionnels, non le carcinome hypophysaire. Le niveau L1 doit donc être interprété avec prudence pour l'indication exacte prédite.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la cabergoline est un agoniste des récepteurs dopaminergiques D2. Elle freine la sécrétion hormonale des cellules hypophysaires et peut réduire le volume des tumeurs exprimant ces récepteurs.

Son efficacité est bien établie dans les prolactinomes. Les données émergentes concernent les adénomes corticotropes et les adénomes hypophysaires non fonctionnels (NFPA). Elles s'appuient sur l'expression des récepteurs D2 et sur des travaux montrant que le ciblage de HTR2B sensibilise les tumeurs à la cabergoline.

Point important : l'étiquette « cancer de l'hypophyse » semble être un rattachement large. Les preuves disponibles concernent des adénomes, pas le carcinome métastatique, et ne doivent pas être extrapolées à celui-ci. Le score TxGNN élevé est une prédiction informatique, pas une preuve clinique. Le signal de repositionnement se situe surtout dans les NFPA et les tumeurs corticotropes ; le prolactinome relève de l'indication d'origine.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03271918](https://clinicaltrials.gov/study/NCT03271918) | Phase 3 | Terminé | 140 | Cabergoline dans l'adénome non fonctionnel résiduel après chirurgie transsphénoïdale (essai randomisé ouvert) |
| [NCT00889525](https://clinicaltrials.gov/study/NCT00889525) | Phase 3 | Terminé | Non renseignée | Cabergoline dans la maladie de Cushing par adénome corticotrope ; résultats non rapportés |
| [NCT02288962](https://clinicaltrials.gov/study/NCT02288962) | Phase 3 | Actif, non en recrutement | 60 | Traitement par agoniste dopaminergique des adénomes non fonctionnels (essai randomisé contrôlé) |
| [NCT01620138](https://clinicaltrials.gov/study/NCT01620138) | Phase 2/3 | Terminé | 21 | Expression des récepteurs de la somatostatine et de la dopamine dans les NFPA et prolactinomes résistants |
| [NCT07034859](https://clinicaltrials.gov/study/NCT07034859) | Phase 4 | Inscription sur invitation | 30 | Cabergoline en traitement primaire de l'adénome non fonctionnel, sur 48 semaines |
| [NCT00376064](https://clinicaltrials.gov/study/NCT00376064) | Phase 4 | Terminé | 20 | Octréotide + cabergoline dans l'acromégalie partiellement répondeuse |
| [NCT01915303](https://clinicaltrials.gov/study/NCT01915303) | Phase 2 | Arrêté | 68 | Pasiréotide seul ou avec cabergoline dans la maladie de Cushing |
| [NCT00460616](https://clinicaltrials.gov/study/NCT00460616) | Non applicable | Terminé | 50 | Étude observationnelle des anomalies cardiaques et valvulaires sous cabergoline au long cours dans les prolactinomes |

Les essais portant sur les prolactinomes (indication d'origine) ne sont pas listés ici, car ils ne relèvent pas du repositionnement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37097352](https://pubmed.ncbi.nlm.nih.gov/37097352/) | 2023 | Revue | JAMA | Diagnostic et prise en charge des adénomes hypophysaires |
| [31597135](https://pubmed.ncbi.nlm.nih.gov/31597135/) | 2020 | Revue | Neuroendocrinology | Nouveaux mécanismes antitumoraux de la cabergoline et applications potentielles élargies |
| [38989697](https://pubmed.ncbi.nlm.nih.gov/38989697/) | 2024 | Préclinique | Neuro-oncology | Le ciblage de HTR2B freine la croissance des NFPA et sensibilise à la cabergoline |
| [28025719](https://pubmed.ncbi.nlm.nih.gov/28025719/) | 2017 | Revue | Pituitary | Place de la cabergoline dans l'acromégalie |
| [25732645](https://pubmed.ncbi.nlm.nih.gov/25732645/) | 2015 | Revue | Endocrinol Metab Clin North Am | Cabergoline et valvulopathies : dans la plupart des études, pas de sur-risque significatif |
| [36013562](https://pubmed.ncbi.nlm.nih.gov/36013562/) | 2022 | Revue | Medicina (Kaunas) | Prise en charge des prolactinomes, dont les formes agressives |
| [20497940](https://pubmed.ncbi.nlm.nih.gov/20497940/) | 2010 | Rapport de cas | Endocr Pract | Octréotide ou cabergoline au long cours dans une sécrétion ectopique de corticotropine |

Aucune de ces publications ne démontre directement un bénéfice de la cabergoline dans le carcinome hypophysaire.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69671845 | DOSTINEX 0,5 mg, comprimé (annulée) | Comprimé | Non renseignée |
| 63313930 | DOSTINEX 0,5 mg, comprimé (annulée) | Comprimé | Non renseignée |
| 66386969 | CABERGOLINE BIOGARAN 0,5 mg (annulée) | Comprimé sécable | Non renseignée |
| 69823057 | CABERGOLINE ARROW 0,5 mg (annulée) | Comprimé sécable | Non renseignée |
| 65266671 | CABERGOLINE ZENTIVA 0,5 mg (annulée) | Comprimé sécable | Non renseignée |

Une sixième AMM (CABERGOLINE TEVA 0,5 mg, n° 64986919, annulée) complète la liste. Aucune AMM n'est actuellement valide.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie hépatique, maladie de la vésicule biliaire, valvulopathie cardiaque, fibrose pulmonaire (y compris post-inflammatoire), fibrose rétropéritonéale liée aux IgG4, pré-éclampsie (y compris sévère).
- **Interactions médicamenteuses** : 60 interactions recensées. Les principales sont de niveau majeur avec la lorcasérine et la clarithromycine, et de niveau modéré avec le métoclopramide. Les autres interactions listées (pantoprazole, oméprazole, metformine, simvastatine, prednisone, etc.) sont de niveau non précisé.
- **Signal de sécurité oculaire** : un cas de glaucome bilatéral à angle fermé a été rapporté chez une jeune femme sous cabergoline (PMID 21347189).
- **Valvulopathies** : le risque est débattu ; la plupart des études ne montrent pas de sur-risque significatif, mais les antécédents valvulaires restent à prendre en compte.

Les mises en garde et contre-indications de la notice n'ont pas pu être obtenues. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 3 testent la cabergoline dans les adénomes corticotropes et non fonctionnels, ce qui soutient une exploration plus poussée. Toutefois, ces données concernent les adénomes et non le carcinome hypophysaire, et le statut actuel des AMM (toutes annulées) limite l'accès en France.
- Les autres indications prédites ne sont pas soutenues : le syndrome de progéria-petite taille-nævus pigmentés et la paralysie cérébrale spastique quadriplégique n'ont ni essai ni publication (niveau L5). Pour le glaucome, la seule donnée clinique est un signal de sécurité. Ces trois pistes sont en attente (Hold).

**Pour avancer, les éléments suivants sont nécessaires :**
- Publication des résultats des essais de phase 3 (NCT03271918, NCT00889525, NCT02288962)
- Données spécifiques au carcinome hypophysaire, distinctes des adénomes
- Données détaillées sur le mécanisme d'action
- Mises en garde et contre-indications issues de la notice de l'ANSM
- Clarification du statut réglementaire en France (AMM annulées) et de la voie d'administration
- Plan de surveillance cardiaque (valvulopathies), hépatique et ophtalmologique
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

