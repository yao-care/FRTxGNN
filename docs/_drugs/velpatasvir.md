---
layout: default
title: Velpatasvir
parent: 僅模型預測 (L5)
nav_order: 329
evidence_level: L5
indication_count: 10
---

# Velpatasvir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

Utilisation directe des instructions du prompt — génération du rapport d'évaluation à partir de l'Evidence Pack fourni, sans code ni outil supplémentaire nécessaire.

# Velpatasvir : De l'Hépatite C Chronique à l'Infection par le Virus de l'Hépatite B

## Résumé en Une Phrase

Velpatasvir est un inhibiteur de la protéine NS5A du virus de l'hépatite C (VHC), commercialisé en association avec le sofosbuvir (Epclusa®) pour le traitement de l'hépatite C chronique. Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infection par le virus de l'hépatite B (VHB)**, avec un score de prédiction de **99.87%**, mais cette piste n'est actuellement soutenue par aucun essai clinique ciblant directement le VHB : les **26 essais cliniques** et **20 publications** recensés portent presque exclusivement sur le traitement du VHC, y compris chez des patients co-infectés VHB/VHC.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hépatite C chronique, en association avec le sofosbuvir (donnée déduite des essais cliniques associés — non renseignée formellement dans ce dossier) |
| Nouvelle Indication Prédite | Infection par le virus de l'hépatite B (VHB) |
| Score de Prédiction TxGNN | 99.87% (rang 1527) |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données structurées sur le mécanisme d'action ne sont pas disponibles dans ce dossier (écart de données signalé, sévérité élevée). Sur la base des informations extraites des essais cliniques et de la littérature associés, Velpatasvir appartient à la classe des inhibiteurs de la protéine NS5A du VHC et est utilisé en association fixe avec le sofosbuvir pour traiter l'hépatite C chronique de tous génotypes.

Le lien mécanistique avec le VHB est cependant faible : la protéine NS5A est spécifique au VHC (virus à ARN de la famille des Flaviviridae), tandis que le VHB est un virus à ADN à réplication par rétro-transcription, ne possédant pas de protéine homologue à NS5A. Il n'existe donc pas de cible moléculaire commune directe entre les deux virus.

La quasi-totalité des essais et publications associés à cette prédiction concernent en réalité le traitement du VHC — le VHB n'apparaît que dans le contexte de populations co-infectées VHB/VHC (prophylaxie de réactivation du VHB pendant le traitement du VHC) ou comme signal de sécurité (réactivation du VHB). Aucune preuve ne démontre une activité antivirale du Velpatasvir contre le VHB lui-même ; l'association avec le VHB dans le modèle TxGNN semble provenir de la proximité thématique « hépatite virale » plutôt que d'un mécanisme pharmacologique partagé.

## Preuves d'Essais Cliniques

*Sur les 26 essais recensés, un seul mentionne explicitement le VHB (NCT04997564, dans un contexte de co-infection) ; les autres concernent le traitement du VHC et sont inclus ici pour leur pertinence pharmacologique générale sur le Velpatasvir.*

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Statut inconnu | 120 | SOF/VEL + prophylaxie TAF chez patients co-infectés VHC/VHB en Chine, pour prévenir la réactivation du VHB pendant le traitement du VHC — seul essai en lien direct avec le VHB |
| [NCT02996682](https://clinicaltrials.gov/study/NCT02996682) | Phase 3 | Terminé | 102 | Efficacité/sécurité de SOF/VEL ± ribavirine chez des patients VHC avec cirrhose décompensée (essai pivot) |
| [NCT02201901](https://clinicaltrials.gov/study/NCT02201901) | Phase 3 | Terminé | 268 | SOF/VEL ± ribavirine chez des patients VHC avec cirrhose Child-Pugh B (essai ASTRAL-4) |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Phase 2 | Terminé | 379 | SOF/VEL chez patients naïfs de traitement, VHC génotypes 1 à 6 (étude princeps de développement) |
| [NCT02533427](https://clinicaltrials.gov/study/NCT02533427) | Phase 1 | Terminé | 15 | Étude d'interaction pharmacocinétique entre SOF/VEL/VOX et un contraceptif hormonal (grade de pertinence C) |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Terminé | 87 | Risque cardiovasculaire après éradication du VHC chez des patients co-infectés VIH/VHC (grade de pertinence C) |
| [NCT04695769](https://clinicaltrials.gov/study/NCT04695769) | Phase 4 | Terminé | 281 | Ribavirine associée à SOF/VEL/VOX chez des patients en échec thérapeutique du VHC chronique |
| [NCT03250910](https://clinicaltrials.gov/study/NCT03250910) | Phase 4 | Terminé | 228 | SOF/VEL générique ± ribavirine chez des patients co-infectés VIH/VHC |
| [NCT01826981](https://clinicaltrials.gov/study/NCT01826981) | Phase 2 | Terminé | 359 | Efficacité/sécurité de schémas à base de sofosbuvir pour le VHC chronique |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | En cours | 200 | Cohorte prospective évaluant Vosevi (SOF/VEL/VOX) chez des patients en échec de traitement antiviral direct du VHC |

## Preuves de la Littérature

*Seule la publication PMID 31542053 concerne directement le VHB — et il s'agit d'un signal de sécurité (réactivation), pas d'une preuve d'efficacité.*

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Rapport de cas | J Med Case Rep | Réactivation du VHB (mutant d'échappement de l'AgHBs) chez un patient anti-HBc positif traité par sofosbuvir/velpatasvir pour le VHC — signal de sécurité, non une preuve d'efficacité anti-VHB |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Étude rétrospective | Klin Mikrobiol Infekc Lek | Évaluation rétrospective du traitement antiviral de l'hépatite virale B et C chronique chez l'enfant (Ostrava) |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Étude transversale | Ann Hepatol | Comparaison internationale des prix des traitements de l'hépatite B et de l'hépatite C |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Revue | World J Gastroenterol | Avancées et défis de la prise en charge de l'hépatite virale pédiatrique (VHB et VHC) |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Revue | Eur J Gen Pract | Diagnostic et traitement de l'hépatite C chronique en médecine générale |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | Étude en vie réelle | J Virus Erad | Efficacité/sécurité de SOF/VEL chez des patients chinois VHC, incluant des co-infectés VHB |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | Étude de cohorte | J Viral Hepat | Résultats et coûts du traitement du VHC au Myanmar, incluant des patients co-infectés VIH/VHB traités simultanément par ténofovir |
| [33217040](https://pubmed.ncbi.nlm.nih.gov/33217040/) | 2021 | Étude en vie réelle | J Gastroenterol Hepatol | Efficacité/sécurité de SOF/VEL chez une cohorte VHC de génotype 3 |
| [38910758](https://pubmed.ncbi.nlm.nih.gov/38910758/) | 2024 | Étude descriptive | Cureus | Efficacité de SOF/VEL chez des patients VHC avec insuffisance rénale chronique |
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | Essai à bras unique | Lancet Gastroenterol Hepatol | Sécurité/efficacité de SOF/VEL chez des patients naïfs de traitement au Rwanda (VHC génotype 4) |

## Informations de Marché en France

Velpatasvir n'est pas commercialisé en France de manière autonome (statut : non commercialisé, 0 AMM enregistrée dans ce dossier). Il est connu par ailleurs comme composant de spécialités combinées (sofosbuvir/velpatasvir), mais aucune donnée d'AMM n'est disponible dans cet Evidence Pack.

## Considérations de Sécurité

Aucune donnée structurée de sécurité (mises en garde, contre-indications, interactions médicamenteuses) n'est disponible dans ce dossier — la fiche TFDA correspondante n'a pas encore été récupérée (écart de données bloquant).

À noter cependant, à partir de la littérature associée à cette indication : un cas de **réactivation du VHB** a été rapporté chez un patient anti-HBc positif traité par sofosbuvir/velpatasvir pour le VHC (PMID 31542053). Ce signal renforce la nécessité d'une évaluation prudente avant toute exploration de Velpatasvir dans une indication liée au VHB, et devra être approfondi dès que les données de sécurité officielles seront disponibles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le mécanisme d'action (inhibition de NS5A, protéine spécifique au VHC) n'a pas d'équivalent chez le VHB, et aucun essai ni publication ne démontre une efficacité du Velpatasvir contre le VHB — les preuves disponibles concernent uniquement le traitement du VHC, parfois chez des patients co-infectés VHB, avec un signal de sécurité défavorable (réactivation du VHB).

**Pour avancer, les éléments suivants sont nécessaires :**
- Fiche TFDA (mises en garde/contre-indications) — écart bloquant à résoudre en priorité
- Données MOA structurées via DrugBank
- Données précliniques ou in vitro testant spécifiquement l'activité du Velpatasvir contre le VHB
- Évaluation approfondie du risque de réactivation du VHB avant toute exploration clinique
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

