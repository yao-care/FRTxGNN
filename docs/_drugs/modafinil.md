---
layout: default
title: Modafinil
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 1
---

# Modafinil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Modafinil : De l'Hypersomnolence (Narcolepsie/SAOS) à l'Insomnie

## Résumé en Une Phrase

Modafinil est un agent favorisant l'éveil (eugeroïque), utilisé cliniquement contre l'hypersomnolence excessive (narcolepsie, apnée obstructive du sommeil, trouble du sommeil lié au travail posté) ; il n'est pas commercialisé en France selon les données disponibles. Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Insomnie**, avec **29 essais cliniques** et **19 publications** recensés — mais l'analyse mécanistique suggère que cette direction est pharmacologiquement contradictoire (un agent de l'éveil pour traiter un trouble nécessitant sédation), ce qui justifie une recommandation de prudence.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypersomnolence (narcolepsie, SAOS, trouble du sommeil lié au travail posté) — non documenté via AMM françaises, source : rationale mécanistique du pack |
| Nouvelle Indication Prédite | Insomnie |
| Score de Prédiction TxGNN | 99.85% |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Modafinil est un agent promoteur de l'éveil dont le mécanisme implique l'activation des voies histaminergiques et dopaminergiques de l'hypothalamus. Son usage clinique établi cible l'hypersomnolence (narcolepsie, apnée du sommeil, trouble du travail posté) — une direction pharmacologique **opposée** à celle requise pour traiter l'insomnie, qui nécessite typiquement un effet sédatif/hypnotique.

Le score TxGNN élevé (99.85%) reflète probablement une proximité topologique dans le graphe de connaissances entre modafinil et le cluster de maladies « troubles du sommeil », plutôt qu'une véritable relation thérapeutique. Sur 29 essais cliniques identifiés en lien avec le terme « insomnie », un seul (NCT01091974) mentionne explicitement l'insomnie dans son titre, et dans cet essai, l'armodafinil est utilisé comme adjuvant anti-fatigue tandis que l'insomnie elle-même est traitée par thérapie cognitivo-comportementale (CBT-I), et non par le médicament étudié.

En l'état, le mécanisme d'action ne soutient pas une application directe à l'insomnie ; la prédiction doit être interprétée comme un signal à investiguer plutôt qu'une hypothèse mécanistiquement validée.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01091974](https://clinicaltrials.gov/study/NCT01091974) | Phase 2 | Terminé | 138 | CBT-I ± armodafinil pour insomnie et fatigue post-chimiothérapie (cancer du sein) ; armodafinil = adjuvant anti-fatigue, l'insomnie étant traitée par CBT-I. **Pertinence B** (la plus élevée du pack, mais indirecte). |
| [NCT01080807](https://clinicaltrials.gov/study/NCT01080807) | Phase 4 | Terminé | 385 | Armodafinil vs placebo pour somnolence excessive liée au travail posté — cible l'hypersomnolence, direction opposée à l'insomnie. Pertinence C. |
| [NCT04299009](https://clinicaltrials.gov/study/NCT04299009) | N/A | Terminé | 15 | Luminothérapie (pas modafinil) pour symptômes diurnes résiduels de l'apnée du sommeil ; sans lien direct au médicament ni à l'insomnie. Pertinence C. |
| [NCT00481195](https://clinicaltrials.gov/study/NCT00481195) | Phase 2 | Terminé | 257 | Armodafinil en add-on pour dépression majeure associée au trouble bipolaire I ; vise probablement l'hypersomnolence associée. Pertinence C. |
| [NCT01305408](https://clinicaltrials.gov/study/NCT01305408) | Phase 3 | Terminé | 399 | Même design (armodafinil adjuvant) pour dépression bipolaire ; pas de lien direct à l'insomnie. Pertinence C. |
| [NCT00233090](https://clinicaltrials.gov/study/NCT00233090) | Phase 2 | Arrêté | 21 | Modafinil vs placebo pour fatigue post-traumatisme crânien ; essai terminé prématurément, fatigue ≠ insomnie. Pertinence C. |
| [NCT01965925](https://clinicaltrials.gov/study/NCT01965925) | Phase 4 | Terminé | 18 | Modafinil pour dysfonction circadienne et cognitive dans le trouble bipolaire stable ; petit échantillon, hors insomnie. Pertinence C. |
| [NCT03083132](https://clinicaltrials.gov/study/NCT03083132) | Phase 2 | Terminé | 21 | Modafinil pour le freezing of gait dans la maladie de Parkinson ; sans rapport avec l'insomnie. Pertinence C. |
| [NCT01072630](https://clinicaltrials.gov/study/NCT01072630) | Phase 3 | Terminé | 492 | Armodafinil adjuvant pour dépression bipolaire (réplique de design) ; vise l'hypersomnolence probable. Pertinence C. |
| [NCT01072929](https://clinicaltrials.gov/study/NCT01072929) | Phase 3 | Terminé | 433 | Idem — armodafinil adjuvant pour dépression bipolaire. Pertinence C. |

*Note : sur les 29 essais recensés, seuls ces 10 ont fait l'objet d'une évaluation de pertinence explicite dans le pack ; les 19 restants sont en attente de classification.*

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39535843](https://pubmed.ncbi.nlm.nih.gov/39535843/) | 2024 | Revue | Expert Opin Pharmacother | Prise en charge des troubles du sommeil dans la maladie de Parkinson (pharmacologique et non pharmacologique) — sujet large, non spécifique à l'insomnie ni au modafinil. |
| [18729534](https://pubmed.ncbi.nlm.nih.gov/18729534/) | 2008 | Revue | Drugs | Revue fondée sur les preuves des usages approuvés et expérimentaux du modafinil — couvre somnolence excessive, fatigue, cognition ; n'inclut pas l'insomnie. |
| [27010071](https://pubmed.ncbi.nlm.nih.gov/27010071/) | 2016 | Revue systématique/méta-analyse | Parkinsonism Relat Disord | Interventions pharmacologiques pour somnolence diurne et troubles du sommeil dans Parkinson — cible la somnolence, pas l'insomnie. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Revue | Drug Des Devel Ther | Profil du pitolisant (autre eugeroïque) dans la narcolepsie — sans rapport avec l'insomnie ni preuve directe pour modafinil. |
| [24312590](https://pubmed.ncbi.nlm.nih.gov/24312590/) | 2013 | Revue systématique/méta-analyse | PLoS One | Efficacité du modafinil sur la fatigue et la somnolence diurne excessive dans les troubles neurologiques — confirme l'usage pour l'EDS, direction opposée à l'insomnie. |
| [22021174](https://pubmed.ncbi.nlm.nih.gov/22021174/) | 2011 | Revue | Mov Disord | Revue MDS des traitements des symptômes non moteurs de Parkinson (incluant somnolence) ; ne cible pas l'insomnie. |
| [20166851](https://pubmed.ncbi.nlm.nih.gov/20166851/) | 2010 | Revue | Expert Opin Emerg Drugs | Traitements émergents de la narcolepsie — usage classique du modafinil (EDS), pas insomnie. |
| [18805301](https://pubmed.ncbi.nlm.nih.gov/18805301/) | 2008 | Revue | Rev Neurol | Narcolepsie avec cataplexie — mentionne l'insomnie de maintien comme symptôme associé, sans traiter du modafinil pour l'insomnie elle-même. |
| [17181377](https://pubmed.ncbi.nlm.nih.gov/17181377/) | 2006 | Revue | Drugs | Trouble du sommeil lié au travail posté (SWSD) — fardeau et prise en charge ; le modafinil/armodafinil y traite l'hypersomnolence, pas l'insomnie. |
| [17060310](https://pubmed.ncbi.nlm.nih.gov/17060310/) | 2006 | Rapport de cas | Am J Hosp Palliat Care | Le modafinil réduit la fatigue dans la maladie de Charcot-Marie-Tooth type 1A (série de cas) — fatigue, pas insomnie ; niveau de preuve faible. |

*Note : sur les 19 publications recensées, ces 10 ont une classification complète ; les autres restent en attente de classification.*

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La direction pharmacologique de modafinil (agent de l'éveil) est mécanistiquement opposée au traitement de l'insomnie, et le score TxGNN élevé provient vraisemblablement d'une proximité topologique dans le graphe de connaissances plutôt que d'une relation thérapeutique réelle. Sur 29 essais recensés, un seul apporte une évidence — indirecte — liée à l'insomnie (armodafinil en adjuvant anti-fatigue, insomnie traitée par CBT-I), et aucune publication ne documente d'effet direct sur l'insomnie primaire. De plus, l'absence de données sur les mises en garde/contre-indications TFDA (gap bloquant DG001) empêche toute évaluation de sécurité S1.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice/les mises en garde officielles (TFDA ou équivalent) pour compléter l'évaluation de sécurité S1 (DG001 — bloquant)
- Compléter les données détaillées de MOA via DrugBank pour renforcer l'analyse de pertinence mécanistique (DG002)
- Réévaluer la pertinence clinique de l'indication « insomnie » — les preuves actuelles concernent majoritairement l'hypersomnolence, pas l'insomnie primaire
- Rechercher des essais contrôlés randomisés ciblant directement l'insomnie primaire comme critère de jugement principal, plutôt que des essais où le médicament traite la somnolence/fatigue en comorbidité
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

