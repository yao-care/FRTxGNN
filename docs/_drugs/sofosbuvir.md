---
layout: default
title: Sofosbuvir
parent: 僅模型預測 (L5)
nav_order: 281
evidence_level: L5
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Sofosbuvir : De l'Hépatite C Chronique à l'Infection par le Virus de l'Hépatite B

## Résumé en Une Phrase

Sofosbuvir est un inhibiteur nucléotidique de la polymérase NS5B, utilisé depuis son approbation pour le traitement de l'hépatite C chronique (VHC). Le modèle TxGNN prédit qu'il pourrait être efficace contre l'**infection par le virus de l'hépatite B (VHB)**, avec **50 essais cliniques** et **19 publications** actuellement associés à cette piste — la plupart portant toutefois sur des populations co-infectées VHC/VHB plutôt que sur une efficacité directe contre le VHB seul.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hépatite C chronique (VHC) |
| Nouvelle Indication Prédite | Infection par le virus de l'hépatite B (VHB) |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L3 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Decision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action (MOA) issues de DrugBank ne sont pas disponibles pour cette évaluation. Sur la base des informations recueillies dans les preuves cliniques et littéraires, le sofosbuvir est connu comme un inhibiteur nucléotidique de l'ARN polymérase ARN-dépendante NS5B, une enzyme spécifique à la réplication du virus de l'hépatite C (VHC, virus à ARN simple brin positif). Son efficacité dans le traitement de l'hépatite C chronique a été largement démontrée et fait partie du standard de soin depuis plusieurs années.

Le lien mécanistique avec le VHB est cependant fragile : contrairement au VHC, le VHB se réplique principalement via une **transcriptase inverse (RT)**, une enzyme structurellement et fonctionnellement distincte de la NS5B. Il n'existe donc pas de base pharmacologique directe justifiant une activité anti-VHB du sofosbuvir. La quasi-totalité des essais cliniques recensés concernent des patients co-infectés VHC/VHB, où le traitement cible le VHC et où le VHB est surveillé pour un risque de réactivation — et non comme critère d'efficacité primaire.

Un signal clinique plus direct existe néanmoins : une étude pilote de phase 2 en ouvert a testé la combinaison ledipasvir/sofosbuvir chez des sujets mono-infectés par le VHB (sans VHC), avec une réduction modeste de l'antigène de surface HBsAg comme critère d'évaluation. Ce signal reste préliminaire et nécessite confirmation par des essais contrôlés dédiés au VHB.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Terminé | 21 | Étude pilote en ouvert de ledipasvir/sofosbuvir pendant 12 semaines chez des sujets **mono-infectés par le VHB** ; évaluation de la baisse de l'HBsAg et de l'ADN du VHB |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Terminé | 23 | Agents antiviraux directs chez des patients co-infectés VHC/VHB ; étude de l'incidence et des facteurs de réactivation du VHB pendant le traitement anti-VHC |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | Terminé | 111 | LDV/SOF pendant 12 semaines chez des sujets co-infectés VHC (génotype 1/2) et VHB à Taïwan ; efficacité et tolérance |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Statut inconnu | 120 | SOF/VEL 12 semaines + TAF prophylactique chez des patients co-infectés VHC/VHB, pour prévenir la réactivation du VHB |
| [NCT02605304](https://clinicaltrials.gov/study/NCT02605304) | Phase 2 | Arrêté prématurément | 7 | Stratégies de retraitement pour le VHC réfractaire aux DAA ; population à surveiller pour statut VHB, sans critère d'efficacité anti-VHB direct |

*Note : la grande majorité des 50 essais associés à cette prédiction (principalement des essais de phase 2/3 sur le VHC) ont été jugés non pertinents (grade C) ou en attente de classification — ils ciblent le VHC et non le VHB. Seuls les essais avec un lien direct ou une population co-infectée pertinente sont présentés ci-dessus.*

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Essai ouvert de Phase 2 | Journal of Medical Virology | LDV/SOF pendant 12 semaines chez des sujets mono-infectés VHB ; réduction modeste de l'HBsAg et de l'ADN du VHB observée |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Étude de cohorte | Trans R Soc Trop Med Hyg | Traitement SOF/daclatasvir chez des patients co-infectés VHC/VHB en Égypte |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Étude de cohorte | Journal of Clinical Gastroenterology | Risque de réactivation du VHB chez des patients traités par LDV/SOF pour le VHC |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Rapport de cas | Medicine | Réactivation du VHB après traitement réussi du VHC par SOF + ribavirine |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Étude de cohorte | Infection and Drug Resistance | Prise en charge de la réactivation du VHB post-DAA chez des patients co-infectés VHC/VHB |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Rapport de cas | Journal of Medical Case Reports | Réactivation du VHB par un variant d'échappement immunitaire pendant traitement SOF/velpatasvir du VHC |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Étude prospective observationnelle | Journal of Viral Hepatitis | Réactivation du VHB chez des patients cancéreux co-infectés VHC/VHB sous DAA |

*Note : la littérature disponible documente essentiellement le risque de réactivation du VHB pendant le traitement anti-VHC, plutôt qu'un effet antiviral direct du sofosbuvir sur le VHB — à l'exception de l'étude PMID 36045503, seule étude clinique testant directement le sofosbuvir chez des patients mono-infectés VHB.*

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les données de mises en garde, contre-indications et interactions médicamenteuses (TFDA) n'ont pas pu être récupérées à ce stade (écart de données bloquant — voir Prochaines Étapes).

---

## Conclusion et Prochaines Étapes

**Decision : Hold**

**Justification :**
Le niveau de preuve (L3) repose principalement sur des études observationnelles menées chez des populations co-infectées VHC/VHB où le VHB n'est pas le critère d'efficacité primaire, et sur une seule étude pilote de phase 2 en ouvert directement dédiée au VHB, dont le signal (baisse modeste de l'HBsAg) reste préliminaire. Le lien mécanistique est lui-même jugé faible : la NS5B ciblée par le sofosbuvir n'est pas l'enzyme de réplication principale du VHB (transcriptase inverse). De plus, un écart de données bloquant (absence des mises en garde/contre-indications TFDA) empêche actuellement toute évaluation de sécurité initiale (S1), et le médicament n'est pas commercialisé en France (0 AMM).

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtention des mises en garde et contre-indications officielles (notice TFDA) — écart bloquant (DG001)
- Données détaillées sur le mécanisme d'action via DrugBank (DG002)
- Confirmation par un essai contrôlé randomisé dédié spécifiquement à l'efficacité anti-VHB (hors contexte de co-infection VHC)
- Évaluation du profil d'interactions médicamenteuses, actuellement non trouvé dans les bases consultées
- Analyse de la voie réglementaire d'entrée sur le marché français, le médicament n'y étant pas actuellement commercialisé
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

