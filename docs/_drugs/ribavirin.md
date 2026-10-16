---
layout: default
title: Ribavirin
parent: Preuves élevées (L1-L2)
nav_order: 663
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Ribavirin : nouvelle indication prédite, Infection chronique par le virus de l'hépatite B (niveau de preuve L2). Indication d'origine : Infection chronique par le virus de l'hépatite C"
monitor_inn: "ribavirin"
predicted_indications: ["chronic hepatitis B virus infection", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "idiopathic copper-associated cirrhosis", "hepatopulmonary syndrome", "primitive portal vein thrombosis", "hepatic porphyria", "IgG4-related pachymeningitis", "IgG4-related aortitis", "IgG4-related mediastinitis"]
---

# Ribavirin
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

# Ribavirine : De l'hépatite C chronique à l'infection chronique par le virus de l'hépatite B

## Résumé en Une Phrase

La ribavirine est un analogue nucléosidique de la guanosine à large spectre antiviral, initialement utilisé pour traiter l'infection chronique par le virus de l'hépatite C et l'infection à virus respiratoire syncytial.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**infection chronique par le virus de l'hépatite B**, avec **15 essais cliniques** enregistrés (dont seulement quelques-uns portent réellement sur l'hépatite B) et **20 publications**, essentiellement des revues générales sur les hépatites B et C.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infection chronique par le virus de l'hépatite C ; infection par le virus de l'hépatite C ; infection à virus respiratoire syncytial (source : graphe de connaissances, aucun texte d'AMM disponible) |
| Nouvelle Indication Prédite | Infection chronique par le virus de l'hépatite B |
| Score de Prédiction TxGNN | 99,86 % |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. D'après les connaissances générales, la ribavirine est un analogue nucléosidique de la guanosine à large activité contre les virus à ARN (inhibition de l'IMPDH, déplétion du pool de GTP, effet immunomodulateur). Son efficacité dans l'hépatite C, en association avec l'interféron pégylé, est établie.

Le virus de l'hépatite B est toutefois un virus à ADN : l'activité antivirale directe de la ribavirine y est faible. Un éventuel bénéfice proviendrait surtout de l'effet immunomodulateur, en association avec l'interféron, et non d'une inhibition directe du VHB.

Le score TxGNN élevé reflète probablement la proximité dans le réseau de connaissances avec l'hépatite C et les voies communes des hépatites, plutôt qu'un mécanisme validé pour l'hépatite B. La prédiction doit donc être considérée comme une question de recherche, non comme une conclusion.

## Preuves d'Essais Cliniques

Parmi les 15 essais compilés, seuls ceux qui testent la ribavirine dans un contexte lié à l'hépatite B sont détaillés ci-dessous. La plupart des autres essais portent sur l'hépatite C, avec la ribavirine en traitement de fond ou comparateur, et n'apportent qu'une pertinence indirecte (par ex. NCT01425970, NCT01447420, NCT02219477, NCT01195181, NCT01795911, NCT01309932, NCT00911963, NCT03186313, NCT02483156, NCT01001754, NCT01830127).

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | Terminé | 138 | Peginterféron alfa-2a + ribavirine versus peginterféron seul dans l'hépatite B chronique AgHBe-négatif ; résultats non fournis, et la contribution propre de la ribavirine est difficile à isoler |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | Terminé | 120 | Étude pilote interféron alfa-2b + ribavirine dans l'hépatite B chronique ; résultats non fournis |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Phase 3 | Inconnu | 24 | Utilisation des propriétés immunomodulatrices de la ribavirine pour renforcer l'activité des analogues nucléos(t)idiques contre le VHB (essai pilote) |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | Inconnu | 320 | Peginterféron alfa-2a + ribavirine dans la co-infection VHC/VHB ; rôle de la ribavirine et résultats peu clairs |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Phase 4 | Inconnu | 20 | Peginterféron alfa-2b + ribavirine dans la double infection hépatite B et delta |

## Preuves de la Littérature

Les 20 publications compilées sont majoritairement des revues générales sur les hépatites B et C ou la co-infection. Aucun essai randomisé ni revue systématique spécifique n'y figure. Les principales :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Revue | Viruses | Co-infection VHC/VHB : traitement agressif recommandé ; association peginterféron + ribavirine auparavant proposée si ARN du VHC positif |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Revue | World J Gastroenterol | Mise à jour sur le traitement et l'évolution de la double infection VHC/VHB |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | Revue | World J Gastroenterol | Les traitements de référence reposaient sur l'IFN-α avec ou sans ribavirine, puis sur les antiviraux à action directe |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Revue | World J Gastroenterol | Polymorphisme IL28B et évolution de l'infection par le VHB |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Revue | Curr Opin Virol | Effet du génotype IL28B sur les infections par le VHB et le VHC |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Revue | Annu Rev Med | Stratégies thérapeutiques actuelles des hépatites B et C chroniques |

## Informations de Marché en France

Aucune AMM n'est enregistrée en France pour ce médicament dans les données compilées (statut : non commercialisé).

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Non classée comme antinéoplasique ; analogue nucléosidique antiviral |

Cette section est donnée à titre indicatif : la ribavirine n'est pas un antinéoplasique. Veuillez consulter les mises en garde et précautions de la notice.

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Les informations suivantes proviennent du graphe de connaissances (et non d'un texte de notice) :

- **Contre-indications issues du graphe de connaissances** (principales) :
  - Maladies respiratoires : bronchopneumopathie chronique obstructive, asthme, sarcoïdose, pneumopathie interstitielle
  - Maladies hématologiques : drépanocytose, hémoglobinopathies, anémie (dont hémolytique), pancytopénie, anémie aplasique héréditaire
  - Maladies cardiovasculaires : infarctus du myocarde, maladie coronarienne, ischémie myocardique, athérosclérose
  - Maladies hépatiques et autres : cirrhose du foie, hépatite auto-immune, insuffisance rénale, pancréatite, parodontite
- **Interactions médicamenteuses** : 105 interactions recensées, toutes de niveau de gravité non précisé. Exemples : calcitriol, pantoprazole, glimépiride, mésalazine, doxycycline, métformine, oméprazole, prednisone, amphotéricine B, morphine.
- **Signal d'alerte** : plusieurs publications rapportent l'apparition de porphyrie cutanée tardive pendant un traitement peginterféron/ribavirine, ce qui suggère un risque plutôt qu'un bénéfice dans ce contexte.

Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le niveau de preuve est limité (L2 selon la règle appliquée, mais reposant sur peu d'essais réellement centrés sur l'hépatite B, dont les résultats ne sont pas fournis). Le mécanisme est peu plausible pour un virus à ADN, et le score élevé reflète vraisemblablement une proximité de réseau avec l'hépatite C. Le médicament n'est pas commercialisé en France, et les données de sécurité de la notice sont absentes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (donnée bloquante)
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Obtenir les résultats publiés des essais NCT00114361, NCT00275938 et NCT03759782, en isolant la contribution de la ribavirine par rapport à l'interféron
- Évaluer le bénéfice/risque au regard des contre-indications du graphe de connaissances (anémie hémolytique, maladie cardiovasculaire, etc.) et des alternatives anti-VHB établies
- Clarifier la situation réglementaire en France (absence d'AMM)

**Autres indications prédites (rang 2 à 10) :** sclérose hépatoportale, hypertension portale non cirrhotique familiale précoce, cirrhose idiopathique associée au cuivre, syndrome hépatopulmonaire, thrombose portale primitive, porphyrie hépatique, pachyméningite, aortite et médiastinite associées aux IgG4. Toutes sont au niveau L4-L5 (prédiction du modèle ou cas rapportés uniquement) et en décision **Hold**. Les seules publications liées (syndrome hépatopulmonaire, porphyrie) décrivent des effets indésirables du traitement et non un bénéfice.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

