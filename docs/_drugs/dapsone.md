---
layout: default
title: Dapsone
parent: Preuves élevées (L1-L2)
nav_order: 214
evidence_level: L1
indication_count: 1
last_modified_at: 2026-10-14
description: "Dapsone : nouvelle indication prédite, Pneumocystose (niveau de preuve L1). Indication d'origine : Dermatite herpétiforme, acné, lèpre"
monitor_inn: "DAPSONE"
predicted_indications: ["pneumocystosis"]
---

# Dapsone
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **1** 
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

## Dapsone : De la dermatite herpétiforme à la pneumocystose
{: .text-alpha }

## Résumé en Une Phrase

La dapsone est un médicament de la famille des sulfones, utilisé à l'origine pour traiter la dermatite herpétiforme, l'acné et la lèpre.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **pneumocystose**,
avec **10 essais cliniques** et **20 publications** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dermatite herpétiforme, acné, lèpre (selon le graphe de connaissances ; le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Pneumocystose |
| Score de Prédiction TxGNN | 99,73 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances pharmacologiques établies, la dapsone est une sulfone qui inhibe la dihydroptéroate synthase, une enzyme de la voie de biosynthèse des folates. C'est la même cible que celle des sulfamides comme le sulfaméthoxazole.

*Pneumocystis jirovecii* dépend de cette voie métabolique. Cela explique l'activité de la dapsone en prophylaxie et, en association avec le triméthoprime, dans le traitement des pneumocystoses légères à modérées. La dapsone possède par ailleurs des effets antimicrobiens et anti-inflammatoires, ce qui est cohérent avec ses usages historiques dans la lèpre et les dermatoses neutrophiliques.

Le score élevé de TxGNN (0,997) est donc compatible avec ce mécanisme connu. Ce lien est déduit de la pharmacologie générale et non du dossier fourni. La dapsone reste un traitement de seconde intention après l'association triméthoprime-sulfaméthoxazole, utilisée surtout chez les patients qui ne la tolèrent pas.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | Terminé | 700 | Dapsone quotidienne vs atovaquone quotidienne en prophylaxie de la pneumocystose chez des patients VIH intolérants au triméthoprime/sulfamides |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Terminé | 600 | Comparaison de trois agents anti-Pneumocystis associés à la zidovudine en prévention primaire chez des patients VIH avancés |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | Terminé | 400 | Pentamidine en aérosol mensuelle vs dapsone trois fois par semaine en prophylaxie, chez des patients intolérants au triméthoprime/sulfamides |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Terminé | 290 | Dapsone/triméthoprime et clindamycine/primaquine vs triméthoprime/sulfaméthoxazole dans la pneumocystose légère à modérée du SIDA |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Phase 1 | Terminé | 96 | Deux schémas posologiques de dapsone orale (quotidien vs hebdomadaire) en prophylaxie chez des enfants infectés par le VIH ; toxicité et pharmacocinétique |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | Terminé | 20 | Triméthrexate avec protection par leucovorine plus dapsone vs triméthoprime/sulfaméthoxazole ; sécurité et pharmacocinétique |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | Non applicable | Terminé | Non renseigné | Dapsone 100 mg vs 50 mg en prophylaxie primaire chez des patients présentant un ARC |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | Non applicable | Terminé | Non renseigné | Dapsone plus triméthoprime vs triméthoprime-sulfaméthoxazole dans le premier épisode de pneumocystose du SIDA |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Phase 4 | Inconnu | 3130 | Dépistage génétique HLA-B*1301 pour prévenir le syndrome d'hypersensibilité à la dapsone ; ne porte pas sur l'efficacité dans la pneumocystose |
| [NCT00636935](https://clinicaltrials.gov/study/NCT00636935) | Phase 4 | Retiré | 0 | Corticothérapie orale et fibrose interstitielle dans la pneumocystose ; essai retiré, sans données, non centré sur la dapsone |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Revue systématique / méta-analyse en réseau | Clin Microbiol Infect | Comparaison des schémas de prophylaxie de la pneumocystose chez les personnes vivant avec le VIH (TMP-SMX, schémas à base de dapsone, pentamidine, atovaquone) |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Revue systématique / méta-analyse en réseau | Clin Microbiol Infect | Comparaison des schémas thérapeutiques de la pneumocystose chez les personnes vivant avec le VIH ; le TMP-SMX reste le traitement de référence |
| [25835432](https://pubmed.ncbi.nlm.nih.gov/25835432/) | 2015 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Corticoïdes adjuvants dans la pneumocystose du patient VIH |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Recommandations | J Antimicrob Chemother | Recommandations ECIL : le TMP-SMX est le médicament de choix en prophylaxie primaire chez les patients d'hématologie et greffés |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Revue | Expert Opin Pharmacother | Synthèse sur la prévention et le traitement de la pneumocystose |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | Revue | Dermatol Clin | Dapsone et sulfapyridine : traitement de choix de la dermatite herpétiforme, utile en prophylaxie de la pneumocystose chez les patients VIH |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Revue | J Formos Med Assoc | Aperçu de la pneumocystose chez les patients immunodéprimés |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Rapport de cas | Ann Pharmacother | Méthémoglobinémie sous dapsone en prophylaxie de la pneumocystose |
| [32714715](https://pubmed.ncbi.nlm.nih.gov/32714715/) | 2020 | Rapport de cas | Cureus | Hypoxie due à une méthémoglobinémie sous dapsone |
| [31631707](https://pubmed.ncbi.nlm.nih.gov/31631707/) | 2021 | Revue de toxicité | Drug Chem Toxicol | Complications hépatiques induites par la dapsone, au-delà de la méthémoglobinémie |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67654911 | DISULONE 100 mg/200 mg (SANOFI WINTHROP INDUSTRIE) ; AMM annulée | Comprimé sécable | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : maladie hépatique, maladie de la vésicule biliaire, anémie (dont anémie macrocytaire), déficit en G6PD, maladie de surcharge en glycogène, cystinurie, galactosémie, déficit en pyruvate déshydrogénase E3, méthémoglobinémie par déficit en méthémoglobine réductase.
- **Interactions médicamenteuses** : 100 interactions recensées, dont 10 de niveau modéré parmi les 20 examinées. Les principales concernent l'aprépitant, le métronidazole, le tinidazole, la nateglinide, la nitisinone, la rosuvastatine, la simvastatine, la troglitazone, l'acide picosulfurique et le charbon activé. Plusieurs autres (calcitriol, pantoprazole, glimépiride, morphine, metformine, oméprazole, sucralfate, rosiglitazone, lansoprazole, vancomycine) sont de niveau inconnu.
- **Signaux de la littérature** : méthémoglobinémie et hypoxie (cas rapportés), atteintes hépatiques et pancréatite aiguë (cas rapportés).

Les mises en garde et contre-indications issues de la notice française n'ont pas pu être exploitées. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 3 terminés (prophylaxie et traitement de la pneumocystose) et des méta-analyses en réseau récentes soutiennent l'usage de la dapsone dans cette indication, ce qui correspond au niveau de preuve L1. Le profil de risque (hémolyse, méthémoglobinémie, déficit en G6PD) impose toutefois des garde-fous, et la dapsone reste un traitement de seconde intention après le TMP-SMX.
- Le statut réglementaire français est défavorable : la seule AMM identifiée est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde et contre-indications officielles), ce qui bloque actuellement le criblage de sécurité.
- Compléter les données sur le mécanisme d'action via DrugBank.
- Vérifier le statut réglementaire actuel de la dapsone en France et la disponibilité d'une spécialité commercialisée.
- Mettre en place un dépistage du déficit en G6PD avant traitement, ainsi qu'une surveillance de la méthémoglobinémie, de l'hémolyse (NFS) et de la fonction hépatique.
- Évaluer la pertinence d'un dépistage HLA-B*1301 selon les résultats de l'essai NCT02550080.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

