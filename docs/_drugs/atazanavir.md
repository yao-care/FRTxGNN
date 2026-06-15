---
layout: default
title: Atazanavir
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 6
---

# Atazanavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Atazanavir : De l'Infection à VIH-1 au Complexe Lié au SIDA

## Résumé en Une Phrase

Atazanavir (Reyataz®) est un inhibiteur de protéase VIH-1 de la classe des azapeptides, initialement développé pour le traitement de l'infection à VIH-1 chez l'adulte et l'enfant en association avec d'autres antirétroviraux.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Complexe Lié au SIDA (AIDS Related Complex)**, avec **2 essais cliniques de Phase 3** (n=653 au total) et **3 publications** soutenant directement cette direction. Une seconde indication prioritaire — l'**Infection à VIH Congénitale** — est appuyée par **33 essais cliniques** et **7 publications**, représentant la base de données pédiatrique et PTME la plus dense de ce dossier.

> **Note sur le dossier multi-indications :** Ce rapport couvre un Evidence Pack à 6 indications prédites. Les rangs 1 à 4 (syndrome d'immunodéficience féline, infection à SIV, trouble neurodéveloppemental rare, hyperlipidémie familiale combinée obsolète) sont classés **Hold** (L4–L5) en raison d'un manque de données cliniques humaines, d'un champ vétérinaire non applicable ou d'un terme ontologique obsolète. Le rapport se concentre sur les deux indications humaines à niveau de preuve L1.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Infection à VIH-1 (inhibiteur de protéase antiretroviral) |
| Nouvelle Indication Prédite | Complexe Lié au SIDA (AIDS Related Complex) |
| Score de Prédiction TxGNN | 99,71 % |
| Niveau de Preuve | L1 |
| Statut de Marché (TFDA, Taiwan) | Non commercialisé à Taiwan |
| Nombre d'AMM (Taiwan) | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Atazanavir est un inhibiteur de protéase (IP) VIH-1 de deuxième génération appartenant à la classe des azapeptides. Il agit en se liant de manière compétitive au site actif de la protéase du VIH-1, enzyme essentielle au clivage post-traductionnel des polyprotéines précurseurs Gag et Gag-Pol en protéines structurelles fonctionnelles matures. Sans cette étape de maturation protéolytique, les virions produits restent sous forme immature et non infectieuse, bloquant efficacement la propagation intercellulaire du virus. Parmi les IP disponibles, atazanavir se distingue par son inhibition modérée de l'enzyme UGT1A1 (entraînant une hyperbilirubinémie non conjuguée bénigne fréquente) et par son profil lipidique favorable : à la différence de lopinavir, il n'inhibe pas le SREBP-1c, préservant ainsi mieux le profil triglycéridique des patients.

Le complexe lié au SIDA (ARC) désigne la phase intermédiaire de l'infection à VIH-1 caractérisée par une immunodépression progressive (CD4 entre 200 et 500 cellules/mm³) accompagnée de symptômes constitutionnels — fièvre, sueurs nocturnes, perte de poids, lymphadénopathie généralisée — sans infections opportunistes définissant le SIDA. Cette entité s'inscrit directement dans le continuum pathophysiologique ciblé par l'indication approuvée d'atazanavir. Le mécanisme d'inhibition de la protéase VIH est identique qu'il s'agisse d'une infection asymptomatique, d'un ARC ou d'un SIDA déclaré : la réplication virale non contrôlée est le moteur commun de la progression, et c'est précisément cette réplication que vise atazanavir.

La pertinence de la prédiction TxGNN (99,71 %) est ainsi solidement ancrée : deux essais de Phase 3 à haute pertinence directe (NCT00035932, n=571 chez patients expérimentés ; NCT01099579, n=82 pédiatriques) et un essai pivot comparatif majeur ATV/r versus LPV/r (NCT00272779, n=1 057) établissent l'efficacité antivirale d'atazanavir à des stades incluant les patients répondant à la définition de l'ARC. Le modèle capture ainsi une cohérence mécanistique réelle, et non une simple coïncidence ontologique.

---

## Preuves d'Essais Cliniques

### Indication Principale — Complexe Lié au SIDA (AIDS Related Complex)

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT00035932](https://clinicaltrials.gov/study/NCT00035932) | Phase 3 | Terminé | 571 | RCT ouvert : ATV+RTV ou ATV+SQV vs LPV/RTV + TDF + nucléoside chez patients VIH expérimentés en traitement ; essai de référence établissant l'efficacité d'ATV en multithérapie pour réduction de charge virale |
| [NCT01099579](https://clinicaltrials.gov/study/NCT01099579) | Phase 3 | Terminé | 82 | PRINCE I : sécurité, efficacité et PK d'ATV en poudre boosté au RTV chez enfants ≥3 mois à <6 ans infectés par le VIH ; résultats favorables sur tolérance et exposition pharmacologique adéquate |

### Indication Secondaire — Infection à VIH Congénitale

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT02269917](https://clinicaltrials.gov/study/NCT02269917) | Phase 3 | Terminé | 1 149 | Switch vers D/C/F/TAF vs maintien bPI (dont ATV) + FTC/TDF chez patients en suppression virologique ; plus grand essai du dossier, données de tolérance et d'efficacité comparatives |
| [NCT00272779](https://clinicaltrials.gov/study/NCT00272779) | Phase 3 | Terminé | 1 057 | ATV/r vs LPV/r + TDF/FTC sur 96 semaines chez patients naïfs ; essai pivot démontrant la non-infériorité d'ATV/r par rapport au standard LPV/r |
| [NCT02951052](https://clinicaltrials.gov/study/NCT02951052) | Phase 3 | Actif, non recruteur | 618 | ATLAS : cabotégravir + rilpivirine LA vs régime PI-basé (dont ATV) chez adultes en suppression virologique ; dernier RCT en cours, fournit des données de comparaison actuelles |
| [NCT01003990](https://clinicaltrials.gov/study/NCT01003990) | Phase 3 | Terminé | 710 | Étude d'accès élargi post-essais ATV : sécurité à long terme chez patients ayant complété les essais BMS ; suivi jusqu'à 14 ans |
| [NCT01691794](https://clinicaltrials.gov/study/NCT01691794) | Phase 4 | Terminé | 108 | Sécurité d'ATV capsule + RTV chez enfants VIH+ de 6 à <18 ans ; collecte de données de sécurité clinique pédiatrique |
| [NCT01335698](https://clinicaltrials.gov/study/NCT01335698) | Phase 3 | Terminé | 160 | PRINCE II : ATV poudre + RTV chez enfants de 3 mois à <11 ans ; sécurité, efficacité et PK en population pédiatrique étendue |
| [NCT01910402](https://clinicaltrials.gov/study/NCT01910402) | Phase 3 | Terminé | 499 | DTG/ABC/3TC vs ATV+RTV+TDF/FTC chez femmes naïves ARV ; données spécifiques à la population féminine, pertinent pour la prévention de la transmission mère-enfant (PTME) |
| [NCT04518228](https://clinicaltrials.gov/study/NCT04518228) | N/A | Terminé | 205 | PK des ARV et anti-tuberculeux pendant la grossesse et le post-partum ; évaluation PK en populations spéciales pour la PTME |
| [NCT00337467](https://clinicaltrials.gov/study/NCT00337467) | Phase 3 | Terminé | 61 | OREY : ATV/RTV en monothérapie IP pour maintien de la suppression virologique ; exploration du traitement simplifié |
| [NCT02397096](https://clinicaltrials.gov/study/NCT02397096) | Phase 3 | Terminé | 673 | Switch vers doravirine/3TC/TDF vs régime PI-basé (dont ATV) ; confirme l'efficacité du régime ATV comme bras de comparaison actif |

---

## Preuves de la Littérature

### Indication Principale — Complexe Lié au SIDA (AIDS Related Complex)

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohorte observationnelle | AIDS Reviews | Facteurs de risque d'événements indésirables gastro-intestinaux chez patients VIH traités et non traités ; l'ART améliore les symptômes GI associés à l'ARC chez de nombreux patients, avec différences entre agents |
| [28991888](https://pubmed.ncbi.nlm.nih.gov/28991888/) | 2018 | Cohorte | J Acquir Immune Defic Syndr | Comparaison des régimes cART sur l'incidence des pathologies neurologiques définissant le SIDA ; différences entre régimes PI et non-PI pour la prévention du neuroSIDA chez patients à stades avancés |
| [34978889](https://pubmed.ncbi.nlm.nih.gov/34978889/) | 2022 | In vitro | Antimicrob Agents Chemother | Nouveaux inhibiteurs de protéase VIH-1 avec modifications fluorées ciblant le SNC ; activité puissante contre souches multi-résistantes et pénétration améliorée de la barrière hémato-encéphalique par rapport aux IP classiques comme ATV |

### Indication Secondaire — Infection à VIH Congénitale

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Pharmacoépidémiologie cas/non-cas | Eur J Clin Pharmacol | Risque d'anomalies congénitales après exposition fœtale aux ARV, données de registre européen ; signal de risque quantifié pour ATV avec recommandation de surveillance renforcée |
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Cohorte prospective (PHACS SMARTT) | Frontiers in Immunology | Sécurité de l'exposition in utero aux ARV dans une cohorte de >3 500 nourrissons (22 sites US) ; évaluation multi-domaines : métabolique, cardiaque, neurologique, développemental, auditif |
| [25383770](https://pubmed.ncbi.nlm.nih.gov/25383770/) | 2015 | Cohorte rétrospective | JAMA Pediatrics | Anomalies congénitales et exposition ARV in utero chez nourrissons HEU ; la plupart des ARV n'augmentent pas significativement le risque, certains agents (dont ATV) nécessitent un suivi prolongé |
| [24992294](https://pubmed.ncbi.nlm.nih.gov/24992294/) | 2015 | Étude PK | Antiviral Therapy | Exposition adéquate d'ATV pendant la grossesse avec ou sans ténofovir ; recommandation d'ajustement de dose chez la femme enceinte en raison d'une AUC réduite par rapport aux non-enceintes |
| [29859254](https://pubmed.ncbi.nlm.nih.gov/29859254/) | 2018 | In vitro | Reprod Toxicol | ATV et RTV interagissent avec les transporteurs placentaires ABCB1/ABCG2/ABCC2 chez le rat ; facteurs déterminant le transfert placentaire d'ATV, avec implications pour la protection fœtale en contexte PTME |
| [28459118](https://pubmed.ncbi.nlm.nih.gov/28459118/) | 2016 | Observationnelle | J AIDS Immune Res | Dépistage auditif néonatal chez nourrissons HEU exposés in utero aux ARV ; proportion référée pour tests supplémentaires selon régime ARV maternel |
| [31595301](https://pubmed.ncbi.nlm.nih.gov/31595301/) | 2020 | Analyse pharmacovigilance | Clin Infect Dis | Sécurité du dolutégravir en grossesse ; ATV utilisé comme référence comparative dans l'analyse multi-bases de pharmacovigilance sur les malformations du tube neural |

---

## Considérations de Sécurité

> Veuillez consulter la notice officielle pour les informations de sécurité complètes (données TFDA non disponibles dans ce dossier).

Sur la base des données mécanistiques documentées dans ce dossier, les points de vigilance connus pour atazanavir sont :

- **Hyperbilirubinémie non conjuguée** : inhibition de l'UGT1A1 → ictère cutané ou oculaire fréquent (généralement bénin chez l'adulte, mais risque d'ictère nucléaire chez le nouveau-né dont la fonction UGT1A1 est immature — surveillance obligatoire en contexte PTME)
- **Néphro-lithiase** : risque accru, particulièrement en association avec ténofovir disoproxil fumarate (TDF) ; surveillance de la fonction rénale et de la créatinine recommandée
- **Interactions médicamenteuses majeures** : puissant inhibiteur du CYP3A4 et de la glycoprotéine-P — de nombreuses contre-indications d'association documentées (données DDI non disponibles dans ce dossier)
- **Modifications PK en grossesse** : AUC réduite (~25 % avec TDF), volume de distribution augmenté — ajustement de dose nécessaire (PMID 24992294)
- **Risque tératogène potentiel** : signal pharmacoépidémiologique identifié dans le registre européen des anomalies congénitales (PMID 40011239) — balance bénéfice/risque à évaluer individuellement en contexte PTME

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Atazanavir bénéficie d'un corpus d'essais cliniques de Phase 3 (dont plusieurs avec n > 500) confirmant une efficacité antivirale robuste pour l'infection à VIH-1, indication mécanistiquement identique au complexe lié au SIDA et à l'infection congénitale à VIH. Le niveau de preuve L1 est atteint pour ces deux indications humaines. Toutefois, l'absence de données réglementaires locales (TFDA), l'absence de commercialisation à Taiwan, et les lacunes sur les mises en garde complètes imposent des garde-fous avant toute démarche d'utilisation élargie.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir la notice officielle TFDA ou EMA/FDA pour les mises en garde complètes, contre-indications et liste des interactions médicamenteuses (DDI CYP3A4/P-gp)
- Confirmer le mécanisme d'action détaillé via DrugBank (DB01072) — donnée actuellement en Data Gap
- Évaluer la faisabilité d'une soumission réglementaire auprès de la TFDA pour les indications pédiatriques et PTME (indication non enregistrée à Taiwan)
- Définir un plan de surveillance spécifique pour les populations à risque : femmes enceintes (ajustement de dose, monitoring charge virale), nouveau-nés (bilirubine, audiologie), patients avec insuffisance rénale (co-prescription TDF)
- Réaliser une analyse DDI formelle avant intégration dans un programme cART complet, en particulier pour les associations avec antifongiques azolés, rifamycines et anticoagulants
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

