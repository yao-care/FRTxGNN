---
layout: default
title: Sofosbuvir
parent: Preuves modérées (L3-L4)
nav_order: 708
evidence_level: L3
indication_count: 8
last_modified_at: 2026-10-14
description: "Sofosbuvir : nouvelle indication prédite, Infection par le virus de l'hépatite B (niveau de preuve L3). Indication d'origine : Infection chronique par le virus de l'hépatite C"
monitor_inn: "SOFOSBUVIR"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection", "Omsk hemorrhagic fever", "chronic hepatitis B virus infection", "Kyasanur forest disease", "HIV infectious disease"]
---

# Sofosbuvir
{: .fs-9 }

Niveau de preuve: **L3** | Indications prédites: **8** 
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

# Sofosbuvir : De l'hépatite C chronique à l'infection par le virus de l'hépatite B

## Résumé en Une Phrase

Le sofosbuvir est un antiviral à action directe, initialement utilisé pour le traitement de l'infection chronique par le virus de l'hépatite C.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection par le virus de l'hépatite B**, mais les preuves restent indirectes : **10 essais cliniques** et **20 publications** sont associés à cette prédiction, presque tous portant sur la co-infection VHC/VHB, et un seul essai de phase 2 (21 patients) évalue directement le VHB.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection chronique par le virus de l'hépatite C |
| Nouvelle Indication Prédite | Infection par le virus de l'hépatite B |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Autorisations uniquement annulées |
| Nombre d'AMM | 7 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. D'après les connaissances établies, le sofosbuvir est un analogue nucléotidique qui inhibe l'ARN polymérase ARN-dépendante NS5B du virus de l'hépatite C. Son efficacité dans l'hépatite C est démontrée.

Pour l'hépatite B, la plausibilité mécanistique est **faible**. Le VHB se réplique par une transcriptase inverse à partir d'une matrice d'ADN, et non par une ARN polymérase ARN-dépendante. Un effet antiviral direct est donc peu vraisemblable. Le score élevé du modèle reflète surtout les associations de co-infection VHC/VHB dans le graphe de connaissances.

Une observation rétrospective a toutefois montré une réduction modeste de l'HBsAg chez des patients co-infectés traités par lédipasvir/sofosbuvir. Cela a conduit à un essai pilote chez des patients mono-infectés par le VHB, dont les résultats restent à confirmer.

---

## Preuves d'Essais Cliniques

Les essais ci-dessous sont les plus pertinents pour le VHB parmi ceux compilés (10 essais au total pour cette indication).

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Terminé | 21 | Lédipasvir/sofosbuvir 12 semaines chez des sujets infectés par le VHB ; étude ouverte à un seul bras, la plus directe pour le VHB |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Terminé | 23 | Antiviraux directs dans la co-infection VHC/VHB ; réactivation du VHB pendant le traitement anti-VHC |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Inconnu | 120 | SOF/VEL avec TAF prophylactique dans la co-infection VHC/VHB ; prévention de la réactivation du VHB |
| [NCT03186313](https://clinicaltrials.gov/study/NCT03186313) | Phase 3 | Terminé | 72 | Sofosbuvir/daclatasvir (± ribavirine) dans l'hépatite C de génotype 4 ; critère principal portant sur le VHC |
| [NCT03261349](https://clinicaltrials.gov/study/NCT03261349) | Phase 2 | Inconnu | 21 | Lédipasvir/sofosbuvir dans les lymphomes B indolents associés au VHC ; pertinence VHB limitée |
| [NCT02483156](https://clinicaltrials.gov/study/NCT02483156) | Phase 2/3 | Terminé | 80 | Sofosbuvir + ribavirine dans l'hépatite C de génotype 4 ; critère portant sur le VHC |

Les autres essais compilés (programmes de dépistage et de traitement du VHC, populations d'usagers de drogues, prisons) ne concernent pas l'efficacité contre le VHB.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Essai ouvert de phase 2 | J Med Virol | Lédipasvir/sofosbuvir chez des patients mono-infectés par le VHB ; critère principal : baisse de l'HBsAg à la semaine 12 |
| [42558970](https://pubmed.ncbi.nlm.nih.gov/42558970/) | 2026 | Étude clinique multicentrique | J Clin Transl Hepatol | Sécurité et efficacité de SOF/VEL avec prétraitement par TAF dans la co-infection VHB/VHC |
| [35268497](https://pubmed.ncbi.nlm.nih.gov/35268497/) | 2022 | Cohorte | J Clin Med | Cinétique de l'ADN du VHB et de l'HBsAg chez des patients co-infectés sous antiviraux directs |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Étude observationnelle prospective | J Viral Hepat | Réactivation du VHB chez des patients cancéreux traités par antiviraux directs pour le VHC |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Rapport de cas | J Med Case Rep | Réactivation du VHB avec mutant d'échappement de l'HBsAg sous sofosbuvir/velpatasvir |
| [27621502](https://pubmed.ncbi.nlm.nih.gov/27621502/) | 2015 | Rapport d'effets indésirables | Hosp Pharm | Réactivation de l'hépatite B sous siméprévir et sofosbuvir |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Revue | Minerva Gastroenterol Dietol | Antiviraux des hépatites B et C et effets sur la fonction rénale |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Revue | World J Gastroenterol | Prise en charge des hépatites virales pédiatriques, dont les antiviraux directs pour le VHC |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61206641 | SOVALDI 400 mg, comprimé pelliculé | Comprimé pelliculé | Non précisée (annulée) |
| 60348342 | EPCLUSA 200 mg/50 mg, comprimé pelliculé | Comprimé pelliculé | Non précisée (annulée) |
| 60704272 | EPCLUSA 150 mg/37,5 mg, granulés enrobés en sachet | Granulés enrobés | Non précisée (annulée) |
| 68425495 | EPCLUSA 200 mg/50 mg, granulés enrobés en sachet | Granulés enrobés | Non précisée (annulée) |
| 64426906 | HARVONI 90 mg/400 mg, comprimé pelliculé | Comprimé pelliculé | Non précisée (annulée) |

Au total, 7 AMM sont enregistrées, toutes annulées. Les deux autres sont EPCLUSA 400 mg/100 mg (63434686) et VOSEVI 400 mg/100 mg/100 mg (61932485).

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** (8 interactions identifiées) :
  - **Majeures** : apalutamide, enzalutamide, lorlatinib
  - **Modérées** : fostamatinib, warfarine, dicoumarol, encorafenib
  - **Mineure** : ciclosporine
- **Réactivation du VHB** : la littérature compilée rapporte des cas de réactivation de l'hépatite B pendant un traitement antiviral direct du VHC chez des patients co-infectés. C'est un point de vigilance majeur pour toute utilisation chez des patients porteurs du VHB.

Veuillez consulter la notice pour les mises en garde et contre-indications détaillées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le mécanisme d'action du sofosbuvir (ARN polymérase) est peu compatible avec la réplication du VHB (ADN/transcriptase inverse). Les données cliniques portent presque entièrement sur la co-infection VHC/VHB, où le sofosbuvir traite le VHC, et la réactivation du VHB est un risque de sécurité connu. Le seul essai direct est petit (n = 21) et à un seul bras.
- Toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action et sur la plausibilité d'un effet anti-VHB
- Résultats confirmatoires contrôlés chez des patients mono-infectés par le VHB, avec un critère d'efficacité clair (HBsAg, ADN du VHB)
- Mises en garde et contre-indications issues de la notice de l'ANSM, actuellement manquantes
- Clarification de la situation réglementaire en France (AMM annulées)

**Note sur les autres indications prédites :** parmi les autres pistes, l'**hépatite E** présente les preuves les plus directes (essai pilote de phase 2 NCT03282474, 10 patients, avec baisse initiale de la charge virale mais sans réponse virologique soutenue, et émergence de variants associés à la résistance). Elle mériterait une évaluation distincte. Les autres pistes (hépatite A, fièvre hémorragique d'Omsk, maladie de la forêt de Kyasanur, VIH) reposent sur des données précliniques, une simple prédiction ou des études de co-infection, et sont à mettre en attente.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

