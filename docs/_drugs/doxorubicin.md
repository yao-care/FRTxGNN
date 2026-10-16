---
layout: default
title: Doxorubicin
parent: Preuves élevées (L1-L2)
nav_order: 258
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Doxorubicin : nouvelle indication prédite, Sarcome d'Ewing (niveau de preuve L1). Indication d'origine : Leucémie lymphoblastique aiguë…"
---

# Doxorubicin
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

# Doxorubicine : Des Leucémies et Lymphomes au Sarcome d'Ewing

## Résumé en Une Phrase

La doxorubicine est une anthracycline cytotoxique, initialement utilisée dans le traitement de la leucémie lymphoblastique aiguë, des lymphomes (hodgkinien et non hodgkinien) et de l'histiocytose à cellules de Langerhans.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **Sarcome d'Ewing**,
avec **26 essais cliniques** et **20 publications** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie lymphoblastique aiguë, lymphomes hodgkiniens et non hodgkiniens (indications issues du graphe de connaissances ; le texte d'indication des AMM françaises n'est pas renseigné) |
| Nouvelle Indication Prédite | Sarcome d'Ewing |
| Score de Prédiction TxGNN | 99,90 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Autorisations annulées uniquement (aucune AMM valide) |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, la doxorubicine est une anthracycline qui inhibe la topoisomérase II et s'intercale dans l'ADN. Son efficacité a été établie dans les hémopathies lymphoïdes (leucémie lymphoblastique aiguë, lymphomes), et son action cytotoxique sur les cellules à prolifération rapide pourrait mécanistiquement s'appliquer au sarcome d'Ewing.

Dans les données compilées, la doxorubicine est un composant central des schémas de chimiothérapie multi-agents du sarcome d'Ewing (VDC/IE, VAC : vincristine, doxorubicine, cyclophosphamide, alternés avec ifosfamide et étoposide). Les tumeurs à petites cellules rondes, très prolifératives, y sont sensibles. Le lien avec l'indication originale tient donc à la chimiosensibilité de tumeurs à croissance rapide, plus qu'à une parenté histologique directe.

Il faut noter que la plupart des essais portent sur des associations : la contribution propre de la doxorubicine ne peut pas être isolée dans ces études. La toxicité cumulative cardiaque impose des limites de dose et une surveillance cardiaque.

## Preuves d'Essais Cliniques

Dix essais parmi les plus pertinents (sur 26 enregistrés) sont présentés.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Terminé | 587 | Essai randomisé comparant des schémas de chimiothérapie par compression d'intervalles dans le sarcome d'Ewing et tumeurs apparentées |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Terminé | 642 | Ajout de vincristine-topotécan-cyclophosphamide au traitement standard à 5 médicaments (dont doxorubicine) dans le sarcome d'Ewing non métastatique |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Terminé | 278 | Intensification de dose dans le sarcome d'Ewing non métastatique (traitement standard vs intensif) |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Inconnu | 1200 | EURO-E.W.I.N.G.99 : chimiothérapie avec ou sans radiothérapie/chirurgie/greffe de cellules souches |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Actif, ne recrute plus | 312 | Ajout du ganitumab (anti-IGF-1R) à la chimiothérapie multi-agents dans le sarcome d'Ewing métastatique |
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | Inconnu | Non renseigné | EICESS 92 : comparaison de schémas de chimiothérapie associés à chirurgie et radiothérapie |
| [NCT00038142](https://clinicaltrials.gov/study/NCT00038142) | Phase 2 | Arrêté | 46 | VAC avec dexrazoxane, avec ou sans ImmTher, dans le sarcome d'Ewing à haut risque ; arrêté avec effectif limité |
| [NCT00003667](https://clinicaltrials.gov/study/NCT00003667) | Phase 2 | Terminé | Non renseigné | Essai randomisé VAC + dexrazoxane avec ou sans ImmTher |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | Terminé | Non renseigné | Cyclophosphamide, doxorubicine, vincristine, étoposide et ifosfamide suivis de résection et radiothérapie |
| [NCT01946529](https://clinicaltrials.gov/study/NCT01946529) | Phase 2 | Terminé | 24 | Traitement stratifié des tumeurs de la famille du sarcome d'Ewing et des tumeurs desmoplastiques à petites cellules rondes |

## Preuves de la Littérature

Dix publications parmi les plus pertinentes (sur 20) sont présentées, avec priorité aux essais randomisés.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | ECR | N Engl J Med | Ajout d'ifosfamide et d'étoposide à la chimiothérapie standard dans le sarcome d'Ewing nouvellement diagnostiqué |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | ECR | J Clin Oncol | Chimiothérapie à intervalles compressés dans le sarcome d'Ewing localisé (Children's Oncology Group) |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | ECR (phase 3) | Lancet | EE2012 : comparaison de deux schémas de chimiothérapie dans le sarcome d'Ewing nouvellement diagnostiqué |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | ECR (phase 3) | J Clin Oncol | Ganitumab associé à la chimiothérapie à intervalles compressés dans le sarcome d'Ewing métastatique |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | Protocole d'ECR | Trials | Protocole de l'essai international EURO EWING 2012 |
| [39838616](https://pubmed.ncbi.nlm.nih.gov/39838616/) | 2025 | Cohorte | Pediatr Blood Cancer | Essai GALOP-2011 : chimiothérapie multi-agents à intervalles compressés (VDC/IE) dans le sarcome d'Ewing localisé |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Revue | Cancer | Recommandations consensuelles du National Ewing Sarcoma Tumor Board |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Revue | J Clin Oncol | Prise en charge actuelle du sarcome d'Ewing et perspectives de collaboration |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Revue | Lancet Oncol | Survie passée d'environ 10 % à environ 75 % pour les formes localisées grâce à la chimiothérapie |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | Analyse de dose-intensité | J Natl Cancer Inst | Influence de l'intensité de dose de doxorubicine sur la réponse et l'évolution dans l'ostéosarcome et le sarcome d'Ewing |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64367525 (annulée) | ADRIBLASTINE 50 mg | Poudre pour solution injectable | Non renseignée |
| 65771499 (annulée) | ADRIBLASTINE 10 mg | Poudre pour solution injectable | Non renseignée |

Les deux autorisations, détenues par PFIZER HOLDING FRANCE, sont annulées. Aucune AMM valide n'est donc recensée dans les données compilées.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (anthracycline, inhibiteur de la topoisomérase II) |
| Risque de Myélosuppression | Élevé (les contre-indications du graphe de connaissances incluent neutropénie, leucopénie, thrombopénie, agranulocytose et anémie) |
| Classification d'Émétogénicité | Moyenne à élevée (selon la classe ; non précisée dans les données compilées) |
| Éléments de Surveillance | NFS avec formule, fonction hépatique (bilirubine) et rénale, fonction cardiaque (échocardiographie/FEVG) avec suivi de la dose cumulée |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

Les données de mises en garde et de contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance et maladie hépatiques, insuffisance cardiaque congestive, cardiomyopathies, maladies cardiovasculaires, arrêt cardiaque soudain, maladies de la conduction cardiaque, thrombopénie, neutropénie, agranulocytose, leucopénie, anémie, hyperbilirubinémie (dont syndrome de Gilbert), maladies infectieuses et fongiques, déficit en G6PD.
- **Interactions médicamenteuses** : 665 interactions recensées. Parmi les principales, **majeures** : dolasétron, cisapride, papavérine ; **modérées** : ondansétron, granisétron, palonosétron, aprépitant, rolapitant, dexaméthasone, clarithromycine, lévofloxacine, famotidine, lopéramide, eliglustat, métréleptine, troglitazone.
- **Point de vigilance** : la toxicité cardiaque cumulative impose des limites de dose et une surveillance cardiaque ; elle est particulièrement préoccupante chez l'enfant. Les essais utilisent parfois le dexrazoxane comme cardioprotecteur.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Plusieurs essais randomisés de phase 3 et de grandes publications incluent la doxorubicine dans le traitement standard du sarcome d'Ewing, ce qui soutient fortement la prédiction (niveau L1). Toutefois, la doxorubicine y est administrée en association, son rôle propre n'est pas isolé, les AMM françaises sont toutes annulées et les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice (mises en garde, contre-indications) auprès de l'ANSM, lacune bloquante pour le dépistage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Clarifier le statut réglementaire en France (AMM annulées) et identifier une présentation disponible, par exemple une autre spécialité de doxorubicine
- Confirmer la contribution propre de la doxorubicine dans les schémas VDC/IE à partir des résultats des essais de phase 3
- Établir un plan de surveillance cardiaque (limite de dose cumulée, évaluation de la FEVG, cardioprotection) et de la myélosuppression, notamment en pédiatrie

**Remarque sur les autres indications prédites :** le rhabdomyosarcome (niveau L1, Proceed with Guardrails) est également soutenu par des essais de phase 3 sur les sarcomes des tissus mous, mais ceux-ci ne sont pas spécifiques du rhabdomyosarcome. Les autres prédictions (adénocarcinome fœtal du poumon, lymphome pulmonaire primitif, blastome pulmonaire, leucémie myéloïde chronique BCR-ABL1, leucémie monocytaire, rhabdomyosarcome embryonnaire vaginal ou paraméningé, ganglioneuroblastome) reposent sur des preuves limitées ou indirectes (Hold ou question de recherche).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

