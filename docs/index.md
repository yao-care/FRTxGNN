---
layout: default
title: Prédictions de Repositionnement de Médicaments
nav_order: 1
description: "Prédictions de repositionnement de médicaments par IA pour la France. Analyse fondée sur les preuves des nouvelles indications thérapeutiques possibles des médicaments autorisés."
permalink: /
---

# Prédictions de Repositionnement de Médicaments — France

Ce projet utilise le modèle TxGNN (apprentissage profond) pour prédire de nouvelles utilisations thérapeutiques potentielles pour les médicaments approuvés en France.

**Avertissement** : Ce contenu est uniquement à des fins de recherche et ne constitue pas un avis médical. Toutes les prédictions de repositionnement de médicaments nécessitent une validation clinique avant application.

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## France : ce que couvre ce site

Ce site publie des rapports sur **{{ site.data.drug_stats.total_drugs }}** médicaments figurant dans les données d'enregistrement ([ANSM](https://ansm.sante.fr/), France).

Rapports par niveau de preuve : L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### Médicaments ayant le niveau de preuve le plus élevé sur ce site

| Médicament | Niveau de preuve |
|---|---|
| [Acetylcysteine](/drugs/acetylcysteine/) | L1 |
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Fluvoxamine](/drugs/fluvoxamine/) | L1 |
| [Lanadelumab](/drugs/lanadelumab/) | L1 |
| [Lormetazepam](/drugs/lormetazepam/) | L1 |
| [Rifabutin](/drugs/rifabutin/) | L1 |
| [Triptorelin](/drugs/triptorelin/) | L1 |
| [Conestat Alfa](/drugs/conestat-alfa/) | L1 |
| [Hydrocortisone](/drugs/hydrocortisone/) | L1 |

### Médicaments couverts uniquement par ce site parmi les 30 sites TxGNN

| Médicament | Niveau de preuve |
|---|---|
| [Almitrine](/drugs/almitrine/) | L3 |
| [Oxalic Acid](/drugs/oxalic-acid/) | L5 |
| [Tertatolol](/drugs/tertatolol/) | L5 |
| [Nordazepam](/drugs/nordazepam/) | L5 |
| [Clotiazepam](/drugs/clotiazepam/) | L5 |
| [Tixocortol](/drugs/tixocortol/) | L5 |
| [Fluindione](/drugs/fluindione/) | L5 |
| [Pipobroman](/drugs/pipobroman/) | L5 |
| [Prazepam](/drugs/prazepam/) | N/A |

<!-- local-home:end -->

## À propos du développeur

Cette plateforme est développée et exploitée par **藥提醒科技有限公司** (yao.care, numéro d'enregistrement
de société 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

FRTxGNN est le site France de la gamme de produits « TxGNN Drug Repurposing » de la société.
Le même système est déployé dans 30 pays et régions, chacun nommé `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, etc.) à l'adresse `{cc}txgnn.yao.care`.
Présentation du produit : <https://www.yao.care/medical/txgnn/>.

Le modèle TxGNN lui-même a été développé par le Zitnik Lab de Harvard Medical School et publié
dans *Nature Medicine*. Cette plateforme est le système de production que 藥提醒科技有限公司 a bâti sur ce
modèle : intégration des données nationales d'enregistrement des médicaments, prédiction par apprentissage profond excluant les usages déjà enregistrés dans le graphe de connaissances, gradation des preuves PubMed / ClinicalTrials, et intégration
au dossier médical électronique via SMART on FHIR.
