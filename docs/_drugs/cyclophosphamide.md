---
layout: default
title: Cyclophosphamide
parent: Preuves élevées (L1-L2)
nav_order: 94
evidence_level: L2
indication_count: 5
---

# Cyclophosphamide
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **5** 
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

# Cyclophosphamide : Vers la Leucémie Myéloïde

## Résumé en Une Phrase

Le cyclophosphamide est un agent alkylant cytotoxique commercialisé en France sous le nom ENDOXAN. Les textes d'indication de ses AMM ne figurent pas dans les données reçues.
Le modèle TxGNN prédit qu'il pourrait être utile dans la **leucémie myéloïde**, avec **50 essais cliniques** et **20 publications** associés à cette direction.
Ces preuves concernent presque exclusivement le contexte de la greffe de cellules souches (conditionnement, prévention de la GVHD), et non un usage en monothérapie.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Leucémie myéloïde |
| Score de Prédiction TxGNN | 99,47 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après la pharmacologie générale, le cyclophosphamide est un agent alkylant activé dans le foie. Il est cytotoxique pour les cellules en prolifération et fortement lymphodéplétant. Ces propriétés justifient son usage dans de nombreux schémas de chimiothérapie.

Dans la leucémie myéloïde, les preuves montrent un rôle bien défini dans la greffe de cellules souches hématopoïétiques. Il entre dans le conditionnement myéloablatif (association busulfan-cyclophosphamide, BuCy). Il sert aussi en post-greffe (PTCy) pour prévenir la réaction du greffon contre l'hôte (GVHD). Il ne s'agit pas d'un traitement anti-leucémique autonome.

La prédiction est donc cohérente avec le mécanisme : la destruction des cellules leucémiques et l'immunosuppression contrôlée sont exactement ce que requiert la greffe. Elle doit toutefois être lue comme une indication « en contexte de greffe ».

---

## Preuves d'Essais Cliniques

Parmi les 50 essais recensés, voici les 10 plus pertinents. Dans la plupart, le cyclophosphamide fait partie d'un schéma de conditionnement ou de prophylaxie de la GVHD, et non de la variable testée.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01191957](https://clinicaltrials.gov/study/NCT01191957) | Phase 3 | Terminé | 252 | Essai randomisé : busulfan-fludarabine vs busulfan-cyclophosphamide (BuCy2) avant allogreffe chez les LAM de 40 à 65 ans en rémission complète |
| [NCT00002945](https://clinicaltrials.gov/study/NCT00002945) | Phase 3 | Terminé | 61 | Cytarabine/idarubicine, puis étoposide/cyclophosphamide à haute dose, autogreffe et interleukine-2 dans la leucémie myéloïde de l'adulte |
| [NCT00852709](https://clinicaltrials.gov/study/NCT00852709) | Phase 1 | Arrêté | 35 | Escalade de dose de clofarabine suivie de cyclophosphamide fractionné chez l'enfant en leucémie aiguë en rechute ou réfractaire |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | Terminé | 213 | Greffe de sang de cordon avec conditionnement myéloablatif cyclophosphamide/fludarabine/irradiation corporelle totale |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Phase 2 | Arrêté | 16 | Sang de cordon et cellules NK avec cyclophosphamide/fludarabine/irradiation dans la leucémie myéloïde non en rémission |
| [NCT00003868](https://clinicaltrials.gov/study/NCT00003868) | Phase 2 | Terminé | 40 | Anticorps anti-CD45 radiomarqué avec cyclophosphamide et irradiation avant greffe dans la LAM avancée |
| [NCT02446964](https://clinicaltrials.gov/study/NCT02446964) | Phase 1 | Terminé | 31 | Irradiation médullaire totale à doses croissantes avec cyclophosphamide post-greffe (haplo-identique) |
| [NCT03246906](https://clinicaltrials.gov/study/NCT03246906) | Phase 2 | Arrêté | 150 | Essai randomisé : cyclophosphamide post-greffe vs ciclosporine/sirolimus/MMF pour prévenir la GVHD |
| [NCT00290641](https://clinicaltrials.gov/study/NCT00290641) | N/A | Terminé | 68 | Conditionnement cyclophosphamide/fludarabine/irradiation avant greffe de sang de cordon |
| [NCT04835519](https://clinicaltrials.gov/study/NCT04835519) | Phase 1/2 | Terminé | 5 | Lymphocytes T CAR-CD33 dans la LAM en rechute ou réfractaire ; le cyclophosphamide sert à la lymphodéplétion |

---

## Preuves de la Littérature

Aucun essai randomisé n'apparaît dans la littérature retenue. Elle se compose d'une méta-analyse en réseau et d'études de cohorte, surtout rétrospectives.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Revue systématique / méta-analyse en réseau | Bone Marrow Transplant | Comparaison des conditionnements myéloablatifs chez les adultes atteints de LAM en rémission complète (dont Bu/Cy) |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Cohorte | Future Oncol | BuCy, conditionnement standard, comparé à fludarabine-busulfan (efficacité jugée similaire, toxicité moindre) |
| [31628924](https://pubmed.ncbi.nlm.nih.gov/31628924/) | 2020 | Étude comparative | Hematol Oncol Stem Cell Ther | Efficacité comparée de Bu/Cy et Bu/Flu, avec un accent sur la qualité de vie |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | Rétrospective (1823 patients) | Bone Marrow Transplant | Intensité du conditionnement selon le risque cytogénétique/moléculaire de la LAM, avec cyclophosphamide post-greffe |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | Cohorte | Eur J Haematol | Impact de l'intensité du conditionnement sur la survie avec SAL et cyclophosphamide post-greffe |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Cohorte (217 patients) | Haematologica | Classification du risque génétique après conditionnement myéloablatif et cyclophosphamide post-greffe ; survie globale à 2 ans de 77 % |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Cohorte | Transpl Immunol | Cladribine avec busulfan et cyclophosphamide comme conditionnement intensif dans la LAM en rechute ou réfractaire |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Cohorte | Int J Mol Sci | Cyclophosphamide post-greffe après greffe apparentée ou non apparentée chez l'enfant atteint de LAM |
| [33325761](https://pubmed.ncbi.nlm.nih.gov/33325761/) | 2021 | Série de cas (27 patients) | Leuk Lymphoma | Cyclophosphamide à haute dose (60 mg/kg) pour réduire la masse tumorale en cas d'hyperleucocytose ou de leucostase |
| [29039989](https://pubmed.ncbi.nlm.nih.gov/29039989/) | 2017 | Série de cas (17 patients) | Pediatr Hematol Oncol | Clofarabine, cyclophosphamide et étoposide dans la LAM pédiatrique en rechute ou réfractaire : 7 réponses (41 %) |

---

## Informations de Marché en France

Les textes d'indication approuvée ne sont pas renseignés dans les données pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 62554177 | ENDOXAN 50 mg, comprimé enrobé | Comprimé enrobé | BAXTER |
| 64635418 | ENDOXAN 500 mg, poudre pour solution injectable | Poudre et solvant pour solution injectable | BAXTER |
| 69586327 | ENDOXAN 1000 mg, poudre pour solution injectable | Poudre pour solution injectable | BAXTER |

---

## Cytotoxicité

Le cyclophosphamide appartient à une classe connue de chimiothérapie cytotoxique (agents alkylants). Le pack ne contient pas de données de toxicité, donc les éléments ci-dessous reposent sur la pharmacologie générale.

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (agent alkylant, oxazaphosphorine) |
| Risque de Myélosuppression | Élevé (neutropénie principalement, dépendante de la dose) |
| Classification d'Émétogénicité | Moyenne à élevée selon la dose |
| Éléments de Surveillance | NFS avec formule, fonction rénale et hépatique, examen urinaire (risque de cystite hémorragique), fonction cardiaque en cas de haute dose |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Un essai randomisé de phase 3 terminé (NCT01191957) et plusieurs essais de phase 2 terminés, ainsi qu'une méta-analyse en réseau, soutiennent l'usage du cyclophosphamide dans la greffe pour leucémie myéloïde, d'où le niveau L2.
- Ces preuves restent limitées au contexte de la greffe, où le cyclophosphamide est un composant et non la variable testée, et les données de sécurité ne sont pas disponibles.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), une lacune bloquante pour le dépistage de sécurité
- Obtenir les textes d'indication des trois AMM ENDOXAN
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Préciser le périmètre visé (conditionnement, cyclophosphamide post-greffe ou traitement de réduction tumorale), puis confirmer la faisabilité par voie (comprimé ou injectable)

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

