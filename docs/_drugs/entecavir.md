---
layout: default
title: Entecavir
parent: Preuves modérées (L3-L4)
nav_order: 285
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-28
description: "Entecavir : nouvelle indication prédite, Infection chronique par le virus de l'hépatite C (niveau de preuve L4). Indication d'origine : Infection chronique par le virus de l'hépatite B"
monitor_inn: "entecavir"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "hepatitis C virus infection", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hepatitis, viral, animal", "hepatitis E virus infection", "hepatitis A virus infection"]
---

# Entecavir
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **9** 
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

## Entécavir : De l'hépatite B chronique à l'infection chronique par le virus de l'hépatite C
{: .text-alpha }

## Résumé en Une Phrase

L'entécavir est un analogue nucléosidique de la guanosine, initialement utilisé pour le traitement de l'infection chronique par le virus de l'hépatite B (VHB).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection chronique par le virus de l'hépatite C**, mais cette prédiction ne repose sur aucune preuve directe : **2 essais cliniques** associés testent d'autres agents ou une prophylaxie de la réactivation du VHB, et la littérature associée ne documente aucune activité anti-VHC de l'entécavir.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection chronique par le virus de l'hépatite B |
| Nouvelle Indication Prédite | Infection chronique par le virus de l'hépatite C |
| Score de Prédiction TxGNN | 0,9998 |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances établies, l'entécavir est un analogue nucléosidique de la guanosine qui inhibe la polymérase de l'ADN du VHB. Son efficacité dans l'hépatite B chronique est bien documentée.

Mécanistiquement, la prédiction est peu convaincante. Le VHC est un virus à ARN dont la réplication dépend de l'ARN polymérase ARN-dépendante NS5B ; il ne possède pas la cible (polymérase d'ADN) de l'entécavir. Le seul lien plausible est indirect : chez les patients co-infectés VHC/VHB, l'entécavir supprime la réplication du VHB et prévient sa réactivation lorsque le VHC est éliminé par les antiviraux à action directe (AAD). Le score élevé du modèle reflète probablement la proximité des deux maladies dans le réseau de connaissances (hépatites virales) plutôt qu'une véritable activité anti-VHC.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | Non applicable | Inconnu | 60 | Prophylaxie par analogues nucléos(t)idiques contre la réactivation du VHB chez des patients co-infectés VHC/VHB sous AAD ; ne concerne pas le traitement du VHC |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Terminé | 23 | AAD chez des patients co-infectés VHC/VHB, étude de la réactivation du VHB ; l'entécavir n'est pas l'agent testé |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34864158](https://pubmed.ncbi.nlm.nih.gov/34864158/) | 2022 | Essai randomisé | Clin Gastroenterol Hepatol | L'entécavir prévient la réactivation du VHB pendant un traitement par AAD en cas de double infection VHC/VHB |
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohorte | Viruses | Réactivation du VHC chez 66 patients anti-VHC positifs atteints d'hépatite B chronique sous analogues nucléos(t)idiques |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Revue | Expert Opin Pharmacother | Avancées dans la prise en charge de la co-infection VHB/VHC |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Revue | Minerva Gastroenterol Dietol | Antiviraux des hépatites B et C et leurs effets sur la fonction rénale |
| [35108715](https://pubmed.ncbi.nlm.nih.gov/35108715/) | 2022 | Observationnelle | Dig Dis | Incidence et évolution de la réactivation du VHB chez des patients traités par AAD pour le VHC |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Observationnelle | J Gastroenterol Hepatol | Risque de réactivation du VHB pendant un traitement du VHC par AAD |
| [32173307](https://pubmed.ncbi.nlm.nih.gov/32173307/) | 2020 | Revue | Clin Res Hepatol Gastroenterol | Prise en charge actuelle et future des hépatites B et C chez l'enfant |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Revue | Wien Med Wochenschr | Traitements actuels des hépatites B et C chroniques |

Ces publications portent sur la co-infection et la prévention de la réactivation du VHB, et non sur une activité anti-VHC de l'entécavir.

---

## Informations de Marché en France

Les 20 AMM recensées sont toutes au statut « annulée ». Le texte d'indication approuvée n'est pas renseigné dans les données compilées. Les 5 premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69469719 | BARACLUDE 0,5 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 62809635 | ENTECAVIR ZYDUS 0,5 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 62432383 | ENTECAVIR TEVA 0,5 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 65228610 | ENTECAVIR VIATRIS 1 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |
| 61115501 | ENTECAVIR EVOLUGEN 1 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée |

Une présentation en solution buvable (BARACLUDE 0,05 mg/ml) figure également parmi les AMM annulées.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance rénale, stéatose hépatique, stéatohépatite non alcoolique, acidose lactique.
- **Interactions médicamenteuses** : 44 interactions recensées, toutes de niveau modéré parmi celles listées. Principales : famotidine, ranitidine, cimétidine, metformine, amphotéricine B (et formes lipidiques/liposomales), amoxicilline, mésalazine, balsalazide, olsalazine, sulfasalazine, vancomycine, kanamycine, néomycine, lévofloxacine, orlistat, polymyxine B.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucune preuve ne soutient une activité anti-VHC de l'entécavir : le VHC est un virus à ARN dépourvu de la cible de l'entécavir, et les essais et publications retrouvés concernent la prévention de la réactivation du VHB, un usage déjà couvert par l'indication d'origine. Le score TxGNN élevé semble refléter un artefact de réseau. Les antiviraux à action directe restent le traitement de référence du VHC.

**Pour avancer, les éléments suivants seraient nécessaires :**
- Données détaillées sur le mécanisme d'action
- Texte des mises en garde et contre-indications de la notice (source ANSM)
- Données précliniques démontrant une éventuelle activité anti-VHC (aucune n'est actuellement disponible)
- Vérification de la disponibilité du produit en France, 20 AMM valides, médicament commercialisé

**Remarque sur les autres indications prédites :** l'hépatite B (rang 2) est l'indication d'origine (niveau L1, Proceed with Guardrails ; surveillance de l'acidose lactique, de la thrombocytopénie, des poussées post-traitement, adaptation de la dose en cas d'insuffisance rénale). L'infection par le VIH (rang 3, L3) relève d'une question de recherche, l'entécavir ne devant pas être utilisé comme traitement du VIH en raison du risque de sélection de la mutation M184V. Les autres prédictions (hépatites A et E, modèles animaux, trouble neurodéveloppemental rare) sont de niveau L4-L5 et restent en Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

