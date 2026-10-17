---
layout: default
title: Imiquimod
parent: Prédiction du modèle uniquement (L5)
nav_order: 395
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Imiquimod : nouvelle indication prédite, Néoplasme prémalin (niveau de preuve L5). Indication d'origine : Verrue commune, infection anogénitale à HPV, kératose actinique…"
monitor_inn: "IMIQUIMOD"
predicted_indications: ["benign neoplasm of buccal mucosa", "cervical neuroblastoma", "odontogenic cyst", "benign neoplasm of tongue", "nasopharyngeal teratoma", "cystic neoplasm", "inner ear neoplasm", "neoplasm of major salivary gland", "schwannoma of jugular foramen"]
---

# Imiquimod
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

# Imiquimod : Des verrues cutanées et de la kératose actinique aux néoplasmes prémalins

## Résumé en Une Phrase

Imiquimod est un immunomodulateur topique (crème), initialement utilisé pour traiter les verrues, les infections anogénitales à papillomavirus humain (HPV), la kératose actinique et le carcinome basocellulaire superficiel.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **néoplasme prémalin**, avec **2 essais cliniques** et **9 publications** soutenant actuellement cette direction.
Cette prédiction recoupe en grande partie l'indication déjà connue de la kératose actinique : ce n'est donc pas un repositionnement entièrement nouveau.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Verrue commune, infection anogénitale à HPV, kératose actinique, carcinome basocellulaire superficiel multifocal (selon le graphe de connaissances ; le texte d'indication des AMM françaises n'est pas disponible) |
| Nouvelle Indication Prédite | Néoplasme prémalin |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L1 (selon le classement des données compilées ; voir la réserve dans la conclusion) |
| Statut de Marché en France | Uniquement annulées |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances pharmacologiques générales, imiquimod est un agoniste du récepteur Toll-like 7 (TLR7). Il stimule les réponses immunitaires innées et adaptatives locales (interféron alpha, TNF-alpha, IL-12), ce qui permet d'éliminer l'épithélium dysplasique et les cellules infectées par le HPV.

Les indications d'origine (kératose actinique, carcinome basocellulaire superficiel, lésions liées au HPV) sont des lésions épithéliales prémalignes ou malignes de faible grade. La catégorie « néoplasme prémalin » englobe ces situations, notamment la kératose actinique, lésion prémaligne typique. Des revues soutiennent aussi son usage dans les néoplasies intraépithéliales anales, vulvaires et cervicales.

Il faut toutefois être transparent : cette prédiction est en grande partie concordante avec l'indication existante, et non un signal de repositionnement réellement nouveau.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Terminé | 20 | Étude ouverte de la crème d'imiquimod 5 % (3 jours par semaine) dans les kératoses actiniques de la tête ; évaluation de la durée de l'effet. Petit effectif, sans groupe contrôle. |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Arrêté | 9 | Essai randomisé d'imiquimod topique dans la néoplasie intraépithéliale cervicale de haut grade (CIN 2-3), alternative à la résection. Arrêté avec 9 participants : sous-dimensionné, aucune conclusion d'efficacité possible. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Revue (Cochrane) | Cochrane Database Syst Rev | Interventions dans la néoplasie intraépithéliale du canal anal, état prémalin associé au HPV |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Revue (Cochrane) | Cochrane Database Syst Rev | Traitements médicaux de la néoplasie intraépithéliale vulvaire de haut grade |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Revue | Int J Mol Sci | Associations thérapeutiques avec la photothérapie dynamique dans le cancer cutané non mélanique |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Revue | Semin Cutan Med Surg | Traitements topiques (fluorouracile, diclofénac, imiquimod, PDT) des cancers cutanés non mélaniques et lésions précurseurs |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Revue | Skin Therapy Lett | Prise en charge actuelle des kératoses actiniques, lésions prémalignes pouvant évoluer en carcinome épidermoïde |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Cas clinique | Int J STD AIDS | Traitement réussi d'une néoplasie vulvaire de haut grade par imiquimod 5 % chez une transplantée rénale |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Cas clinique | Int J STD AIDS | Guérison d'une papulose bowénoïde du pénis par imiquimod 5 % |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Préclinique | Urol Oncol | Pharmacocinétique d'agonistes TLR7 chez le rat, étudiés pour une voie intravésicale |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Cas clinique/autre | Hautarzt | Imagerie par OCT d'une porokératose actinique ; lésions résistantes au traitement topique |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69349666 | ZYCLARA 3,75 %, crème (statut : annulée) | Crème | Texte d'indication non disponible |
| 66916232 | ALDARA 5 %, crème (statut : annulée) | Crème | Texte d'indication non disponible |

---

## Cytotoxicité

Imiquimod est un immunomodulateur topique, et non un cytotoxique conventionnel ; cette section est donc omise.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : réaction de photosensibilité, photosensibilité, maladie auto-immune, maladie du greffon contre l'hôte, coup de soleil.
- **Interactions médicamenteuses** : 59 interactions recensées, toutes de niveau de gravité « inconnu ». Parmi les principales : pantoprazole, morphine, oméprazole, lansoprazole, prednisone, prednisolone, simvastatine, warfarine, clopidogrel, hydroxychloroquine, acide acétylsalicylique, ibuprofène, budésonide, fluticasone.
- **Signaux de sécurité tirés de la littérature** : une transformation maligne d'une papillomatose orale florissante pendant un traitement par imiquimod, un lichen planopilaire et un érythème polymorphe après usage topique ont été rapportés (cas isolés). Une revue de 2024 s'interroge sur la sécurité de l'usage hors AMM dans les lésions orales.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, non disponibles dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Les données compilées classent le niveau de preuve en L1 pour le néoplasme prémalin, mais ce classement est fragile : seuls 2 essais de phase 3 existent (l'un terminé, ouvert, n = 20 ; l'autre arrêté, n = 9), et ils ne constituent pas deux essais randomisés complets et concluants. L'indication recoupe surtout la kératose actinique déjà connue. Il est donc raisonnable d'avancer avec prudence, sans conclure à un repositionnement nouveau.
- Les deux AMM françaises sont annulées : aucune spécialité n'est actuellement commercialisée en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mécanisme d'action détaillé (DrugBank) et texte officiel des mises en garde et contre-indications (notice ANSM)
- Définition précise du sous-type de lésion prémaligne visé (kératose actinique, néoplasies intraépithéliales anale, vulvaire ou cervicale) afin de distinguer l'indication connue de l'extension réelle
- Essais randomisés suffisamment dimensionnés dans les néoplasies intraépithéliales non cutanées
- Évaluation du statut réglementaire en France (spécialités annulées) et de la voie d'administration
- Plan de surveillance de sécurité (photosensibilité, maladies auto-immunes, réactions locales)

**Autres indications prédites (non retenues) :** les néoplasmes bénins de la muqueuse buccale (L4, question de recherche, aucun essai, signal de sécurité) et le kyste odontogène (L4, preuves indirectes via le syndrome de Gorlin-Goltz) relèvent de la recherche. Les autres prédictions classées (neuroblastome cervical, néoplasme bénin de la langue, tératome nasopharyngé, néoplasme kystique, néoplasme de l'oreille interne, néoplasme des glandes salivaires majeures, schwannome du foramen jugulaire) sont en niveau L5, sans preuve exploitable : Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

