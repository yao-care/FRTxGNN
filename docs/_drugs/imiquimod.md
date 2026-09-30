---
layout: default
title: Imiquimod
parent: Preuves élevées (L1-L2)
nav_order: 151
evidence_level: L2
indication_count: 10
---

# Imiquimod
{: .fs-9 }

Niveau de preuve: **L2** | Indications prédites: **10** 
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

# Imiquimod : D'un Immunomodulateur Topique à la Néoplasie Prémaligne

## Résumé en Une Phrase

Imiquimod est un immunomodulateur appliqué sur la peau sous forme de crème. Il est commercialisé en France sous les noms ZYCLARA 3,75 % et ALDARA 5 %. Le texte de l'indication approuvée n'est pas renseigné dans les données ANSM disponibles.
Le modèle TxGNN prédit qu'il pourrait être efficace pour les **néoplasmes prémalins** (par exemple kératose actinique, néoplasie intraépithéliale vulvaire, anale ou cervicale).
Actuellement, **19 essais cliniques** et **9 publications** soutiennent cette direction, mais aucun essai de phase 3 ne fournit de résultat interprétable sur cette indication.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Néoplasme prémalin (pre-malignant neoplasm) |
| Score de Prédiction TxGNN | 99,92 % (rang 1086) |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 2 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Imiquimod est un agoniste du récepteur TLR7. Appliqué localement, il déclenche la production d'interféron alpha, de TNF-alpha et d'IL-12, ce qui active l'immunité innée puis adaptative contre les cellules épithéliales dysplasiques.

Ce mécanisme est cohérent avec le traitement des lésions prémalignes : kératose actinique, néoplasie intraépithéliale vulvaire (VIN), anale (AIN) et papulose bowénoïde. Les revues Cochrane sur la VIN et l'AIN, ainsi que les revues sur les traitements topiques des kératoses actiniques, vont dans ce sens.

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans DrugBank pour ce dossier. Le raisonnement ci-dessus repose donc sur la littérature. Aucune indication d'origine n'est renseignée dans les données ANSM, ce qui empêche de comparer directement l'indication d'origine et la nouvelle.

## Preuves d'Essais Cliniques

Sur les 19 essais recensés, voici les 10 plus pertinents. Seule une partie d'entre eux a été évaluée pour sa pertinence, et plusieurs restent en attente de cette évaluation.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminé prématurément | 9 | Imiquimod topique dans la néoplasie intraépithéliale cervicale de haut grade. Trop peu de participants pour conclure sur l'efficacité |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | Terminé | 90 | Essai randomisé d'imiquimod topique dans les lésions intraépithéliales cervicales de haut grade |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | Terminé prématurément | 49 | Comparaison de l'imiquimod à 5 %, 0,05 % et 0,05 % nanoencapsulé dans la chéilite actinique. Informe sur la formulation et la dose plus que sur l'efficacité |
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | Terminé | 259 | Imiquimod néoadjuvant pour réduire la taille d'exérèse du lentigo malin du visage (mélanome intraépidermique) |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | Terminé | 5 | Mécanismes d'échappement immunitaire et effet de l'imiquimod dans la VIN 2/3 et les condylomes |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | Inconnu | 20 | Imiquimod 3,75 % après cryothérapie dans les kératoses actiniques hypertrophiques des mains et avant-bras |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Terminé | 20 | Étude ouverte d'imiquimod 5 % dans les kératoses actiniques de la tête, avec évaluation de la durée de l'effet |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | Inconnu | 145 | Exérèse chirurgicale versus curetage + imiquimod dans le carcinome basocellulaire nodulaire (cancer, non prémalin) |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Phase 1 précoce | Terminé | 16 | Imiquimod néoadjuvant dans le carcinome épidermoïde oral précoce. Soutient le mécanisme TLR7, mais concerne un cancer invasif |
| [NCT00142454](https://clinicaltrials.gov/study/NCT00142454) | Phase 1 | Terminé | 9 | Vaccin NY-ESO-1 avec imiquimod comme adjuvant dans le mélanome. Usage adjuvant, peu pertinent pour les lésions prémalignes |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Interventions pour la néoplasie intraépithéliale du canal anal, affection prémaligne liée au HPV |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Traitements médicaux de la VIN de haut grade, faute de consensus sur la prise en charge optimale |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Revue | Skin Therapy Lett | Prise en charge actuelle des kératoses actiniques, dont les traitements topiques de champ |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Revue | Semin Cutan Med Surg | Traitements topiques (fluorouracile, diclofénac, imiquimod, thérapie photodynamique) des cancers cutanés non mélaniques et des lésions précurseurs |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Revue | Int J Mol Sci | Associations de traitements avec la thérapie photodynamique pour les cancers cutanés non mélaniques |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Rapport de cas | Int J STD AIDS | Guérison d'une VIN de haut grade sous imiquimod 5 % chez une greffée rénale |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Rapport de cas | Int J STD AIDS | Guérison d'une papulose bowénoïde du pénis sous imiquimod 5 % |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Préclinique (animal) | Urol Oncol | Pharmacocinétique et pharmacodynamie d'agonistes TLR7 chez le rat, en cours d'étude pour le cancer de vessie |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 69349666 | ZYCLARA 3,75 %, crème | Crème | VIATRIS HEALTHCARE (Irlande) |
| 66916232 | ALDARA 5 %, crème | Crème | VIATRIS HEALTHCARE (Irlande) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les mises en garde, les contre-indications et les interactions ne sont pas disponibles dans les données ANSM de ce dossier.

La littérature de l'Evidence Pack signale toutefois des événements indésirables à connaître :
- Une conversion maligne d'une papillomatose orale et labiale florissante sous imiquimod topique (PMID 12719972).
- Un érythème polymorphe (PMID 29173871) et un lichen planopilaire (PMID 24575881) après application d'imiquimod chez des patients atteints du syndrome de Gorlin.
- Un carcinome mucineux apparu au cours d'un traitement d'une maladie de Paget extramammaire (PMID 21885944).

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le mécanisme TLR7 est cohérent avec les lésions prémalignes, et des revues Cochrane, des revues sur les kératoses actiniques, des essais de phase 2 à 4 et des cas cliniques soutiennent l'usage topique.
- L'unique essai de phase 3 sur la néoplasie cervicale (NCT02329171) a été arrêté à 9 participants, d'où le plafonnement au niveau L2.

**Pour avancer, les éléments suivants sont nécessaires :**
- **Bloquant :** récupérer et analyser la notice ANSM (mises en garde et contre-indications), sans quoi le dépistage de sécurité (S1) est impossible.
- Confirmer le type de lésion visé (kératose actinique, VIN, AIN ou NIC), avec un dosage et un suivi propres à chaque lésion.
- Obtenir le mécanisme d'action depuis DrugBank.
- Évaluer la pertinence des essais encore en attente, ainsi que les 9 essais non listés ici.

**Autres prédictions du modèle (rangs 2 à 10) :**
- Aucune ne justifie une avancée à ce stade.
- La muqueuse buccale est un sujet de recherche à traiter d'abord sous l'angle de la sécurité (niveau L4, signal de conversion maligne).
- Les autres signaux (neuroblastome cervical, kyste odontogène, tumeur bénigne de la langue, tératome nasopharyngé, néoplasme kystique, néoplasme de l'oreille interne, néoplasme des glandes salivaires majeures, schwannome du foramen jugulaire) sont en attente (Hold).
- Le signal « kyste odontogène » repose uniquement sur des données concernant le carcinome basocellulaire dans le syndrome de Gorlin.

*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical. Tout candidat de repositionnement nécessite une validation clinique avant utilisation.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

