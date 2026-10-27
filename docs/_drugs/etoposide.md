---
layout: default
title: Etoposide
parent: Preuves élevées (L1-L2)
nav_order: 308
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "etoposide"
predicted_indications: ["well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "Ewing sarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma"]
description: "Etoposide : nouvelle indication prédite, Sarcome d'Ewing (indication la mieux étayée (niveau de preuve L1). Indication d'origine : Cancer bronchique à petites cellules, tumeurs germinales du testicul"
---

# Etoposide
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

## Étoposide : Du Cancer Bronchique à Petites Cellules au Sarcome d'Ewing
{: .text-alpha }

## Résumé en Une Phrase

L'étoposide est un agent de chimiothérapie cytotoxique, initialement utilisé pour le traitement du cancer bronchique à petites cellules et des tumeurs germinales du testicule (séminome, tumeur du sac vitellin, tératome).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **sarcome d'Ewing**, l'indication la mieux étayée parmi les dix nouvelles indications prédites,
avec **33 essais cliniques** et **19 publications** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer bronchique à petites cellules, tumeurs germinales du testicule (le texte d'indication des AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Sarcome d'Ewing (indication la mieux étayée ; la première prédiction du classement, l'adénocarcinome fœtal bien différencié du poumon, ne repose que sur un cas clinique) |
| Score de Prédiction TxGNN | 99,85 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Uniquement annulé (aucune AMM valide) |
| Nombre d'AMM | 8 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, l'étoposide est un inhibiteur de la topoisomérase II : il provoque des cassures de l'ADN et bloque la division des cellules tumorales. Son efficacité est établie dans le cancer bronchique à petites cellules et dans les tumeurs germinales.

Le sarcome d'Ewing est une tumeur maligne de l'os et des tissus mous, très sensible aux agents génotoxiques. Les données compilées citent notamment une étude publiée dans *Nature* (2018) décrivant cette sensibilité à l'étoposide. L'association ifosfamide + étoposide fait partie des protocoles établis (alternance VDC/IE), ce qui rend la prédiction cohérente sur le plan pharmacologique.

Il faut cependant noter que, dans la plupart des essais, l'étoposide est utilisé au sein de polychimiothérapies : sa contribution propre est difficile à isoler.

## Preuves d'Essais Cliniques

Sélection parmi les 33 essais associés au sarcome d'Ewing (principaux essais de phase 3 et de phase 2 pertinents) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | Inconnu | Non renseigné | Étude coopérative européenne EICESS 92 : comparaison de polychimiothérapies contenant de l'étoposide, avec chirurgie et radiothérapie |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Terminé | 587 | Intensification de la chimiothérapie par compression des intervalles dans le sarcome d'Ewing |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Inconnu | 1200 | EURO-E.W.I.N.G.99 : chimiothérapie avec ou sans radiothérapie et/ou chirurgie |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Terminé | 642 | Ajout de vincristine-topotécan-cyclophosphamide au traitement standard à 5 médicaments (dont étoposide) dans la forme non métastatique |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Terminé | 278 | Intensification des doses dans le sarcome d'Ewing non métastatique |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Actif, non en recrutement | 312 | Ganitumab ajouté à la polychimiothérapie (dont étoposide) dans la forme métastatique |
| [NCT02727387](https://clinicaltrials.gov/study/NCT02727387) | Phase 2 | Terminé | 155 | Chimiothérapie à haute dose, radiothérapie et traitement d'entretien dans le sarcome d'Ewing métastatique |
| [NCT01864109](https://clinicaltrials.gov/study/NCT01864109) | Phase 2 | Actif, non en recrutement | 83 | Irinotécan et témozolomide ajoutés à une chimiothérapie à base d'alkylants dans le sarcome d'Ewing nouvellement diagnostiqué |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | Terminé | Non renseigné | Cyclophosphamide, doxorubicine, vincristine, étoposide et ifosfamide suivis de résection et de radiothérapie |
| [NCT00002643](https://clinicaltrials.gov/study/NCT00002643) | Phase 2 | Terminé | 130 | Traitement intensif avec facteurs de croissance dans le sarcome d'Ewing métastatique d'emblée |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | ECR | N Engl J Med | Ajout de l'ifosfamide et de l'étoposide au traitement standard du sarcome d'Ewing et de la tumeur neuroectodermique primitive de l'os |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | ECR de phase 3 | Lancet | EE2012 : comparaison de deux schémas de chimiothérapie dans le sarcome d'Ewing nouvellement diagnostiqué |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | ECR de phase 3 | J Clin Oncol | Ganitumab avec chimiothérapie à intervalles compressés dans le sarcome d'Ewing métastatique |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | ECR | J Clin Oncol | Chimiothérapie à intervalles compressés dans le sarcome d'Ewing localisé (alternance VDC/IE) |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | Protocole d'ECR | Trials | Protocole Euro Ewing 2012 |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Recommandations de consensus | Cancer | Recommandations de prise en charge du sarcome d'Ewing (National Ewing Sarcoma Tumor Board) |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Revue | J Clin Oncol | Prise en charge actuelle du sarcome d'Ewing et approches collaboratives |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Revue | Lancet Oncol | Revue générale sur le sarcome d'Ewing |
| [39713774](https://pubmed.ncbi.nlm.nih.gov/39713774/) | 2024 | Étude rétrospective | Sarcoma | Étoposide oral dans le sarcome d'Ewing en rechute ou réfractaire chez l'adolescent et l'adulte (33 patients) |
| [29513652](https://pubmed.ncbi.nlm.nih.gov/29513652/) | 2018 | Étude de mécanisme | Nature | EWS-FLI1 provoque des R-loops et bloque la réparation par BRCA1, expliquant la sensibilité à l'étoposide |

## Informations de Marché en France

Aucune AMM valide n'est enregistrée : les 8 AMM sont annulées et le texte d'indication approuvée n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 66338465 | ETOPOSIDE HIKMA 20 mg/mL | Solution à diluer pour perfusion | Annulée |
| 61683518 | ETOPOSIDE TEVA 100 mg/5 ml | Solution pour perfusion | Annulée |
| 61425560 | ETOPOSIDE TEVA 20 mg/ml | Solution à diluer pour perfusion | Annulée |
| 60155667 | ETOPOSIDE TEVA 200 mg/10 ml | Solution injectable pour perfusion | Annulée |
| 67802057 | CELLTOP 50 mg | Capsule molle (voie orale) | Annulée |

Trois autres AMM annulées existent (ETOPOSIDE ACCORD 20 mg/mL, ETOPOPHOS 100 mg, ETOPOSIDE VIATRIS 20 mg/ml).

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (inhibiteur de la topoisomérase II, épipodophyllotoxine) |
| Risque de Myélosuppression | Élevé : le graphe de connaissances associe l'étoposide à la thrombopénie, la neutropénie, l'agranulocytose, la leucopénie et l'anémie |
| Classification d'Émétogénicité | Faible à moyenne (selon la classe du médicament) |
| Éléments de Surveillance | NFS avec formule, fonction hépatique et rénale ; surveillance du risque de leucémie secondaire |
| Protection de Manipulation | Manipulation selon les règles applicables aux médicaments cytotoxiques |

Veuillez consulter les mises en garde et précautions de la notice pour les détails.

## Considérations de Sécurité

- **Contre-indications ou affections à risque (graphe de connaissances, hors texte de la notice)** : thrombopénie, neutropénie, agranulocytose, anémie (dont macrocytaire), leucopénie, pneumopathie interstitielle, fibrose pulmonaire (dont postinflammatoire), insuffisance rénale, acidose (dont métabolique), atteinte hépatique d'origine médicamenteuse.
- **Interactions médicamenteuses** : 495 interactions recensées. Exemples d'interactions de niveau modéré : aprépitant, métronidazole, éliglustat, rolapitant, rosuvastatine, simvastatine, tinidazole. Niveau mineur : lévofloxacine. De nombreuses autres sont de niveau non précisé (par exemple calcitriol, doxycycline, cimétidine, morphine).

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais randomisés de phase 3 (EICESS 92, EURO-E.W.I.N.G.99, essais COG) et un ECR publié dans le *New England Journal of Medicine* soutiennent l'usage de l'étoposide avec l'ifosfamide dans le sarcome d'Ewing, ce qui correspond au niveau de preuve L1. Cet usage fait déjà partie des protocoles établis ; il s'agit donc davantage d'une confirmation que d'un repositionnement inédit.
- Les garde-fous s'imposent : utilisation au sein de protocoles multi-agents dans des centres spécialisés, surveillance de la myélosuppression et du risque de leucémie secondaire, gestion du grand nombre d'interactions médicamenteuses.

**Autres prédictions du classement :**
- Rhabdomyosarcome : niveau L1, Proceed with Guardrails (un ECR de l'IRSG compare ifosfamide/étoposide à vincristine/melphalan). La contribution propre de l'étoposide reste difficile à isoler et certains résultats sont mitigés.
- Blastome pulmonaire et sous-types rares de rhabdomyosarcome : L4 à L5, uniquement des cas cliniques ou aucune donnée. Hold ou question de recherche.
- Lymphome pulmonaire primitif : L4, preuves indirectes (autres sous-types de lymphomes). Hold.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice officielle (mises en garde et contre-indications) auprès de l'ANSM : ces données manquent actuellement et bloquent l'évaluation de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank.
- Clarifier le statut réglementaire : les 8 AMM sont annulées, il faut vérifier la disponibilité réelle du produit en France (autres circuits, autorisations en vigueur).
- Préciser la contribution propre de l'étoposide au sein des polychimiothérapies.
- Établir un plan de surveillance de la sécurité (hématologique, hépatique, rénale, pulmonaire, interactions médicamenteuses) pour les populations pédiatriques et adultes concernées.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

