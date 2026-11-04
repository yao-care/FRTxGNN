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

Jeu de données : [Base de données publique des médicaments (BDPM)](https://base-donnees-publique.medicaments.gouv.fr/) ; il est téléchargé et comparé automatiquement chaque semaine (le lundi). Détails : [Sources de données]({{ '/sources/' | relative_url }}).

Rapports par niveau de preuve :

| Niveau de preuve | Rapports | Part |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

31 paires médicament–maladie prédites sur ce site n'apparaissent sur aucun autre des 30 sites TxGNN.

### Médicaments ayant le niveau de preuve le plus élevé sur ce site

| Médicament | Niveau de preuve |
|---|---|
| [Acetylcysteine](/drugs/acetylcysteine/) | L1 |
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Clomipramine](/drugs/clomipramine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Potassium](/drugs/potassium/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |
| [Dapsone](/drugs/dapsone/) | L1 |
| [Ketamine](/drugs/ketamine/) | L1 |

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

Cette plateforme est développée et exploitée par **藥提醒科技有限公司** (yao.care). Les informations sur
l'entreprise, le contexte du modèle TxGNN et la liste complète des sites de la gamme figurent sur la page
<a href="{{ '/about/' | relative_url }}">À propos</a>.
