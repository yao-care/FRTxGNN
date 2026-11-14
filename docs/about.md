---
layout: default
title: À propos
nav_order: 90
permalink: /about/
description: "FRTxGNN est une plateforme de prédiction du repositionnement de médicaments développée par 藥提醒科技有限公司 (yao.care), fondée sur le modèle TxGNN de Harvard et couvrant les médicaments autorisés par l'ANSM en France."
---

# À propos

<div class="key-takeaway">
Accélérer la validation des preuves du repositionnement de médicaments grâce à l'IA — de la prédiction à la preuve, en un coup d'œil.
</div>

---

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## France : données de ce site

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

<!-- site-data:end -->

## Contexte

<p class="key-answer" data-question="Qu'est-ce que FRTxGNN ?">
<strong>FRTxGNN</strong> est une plateforme d'aide à la recherche sur le repositionnement de médicaments, fondée sur le modèle TxGNN
publié dans <em>Nature Medicine</em> par le Zitnik Lab de l'université Harvard. Elle prédit
l'extension des indications des médicaments autorisés par l'ANSM en France. Au-delà des scores de prédiction de l'IA,
la plateforme intègre des preuves cliniques issues de ClinicalTrials.gov et de PubMed, afin que les chercheurs puissent
évaluer rapidement la crédibilité de chaque prédiction.
</p>

---

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

---

## Qu'est-ce que le repositionnement de médicaments ?

<p class="key-answer" data-question="Qu'est-ce que le repositionnement de médicaments ?">
Le <strong>repositionnement de médicaments</strong> consiste à trouver de nouvelles utilisations thérapeutiques pour des médicaments existants.
Comparé au développement d'un nouveau médicament à partir de zéro — 10 à 15 ans et 1 à 2 milliards de dollars US —
le repositionnement demande 3 à 5 ans et 100 à 300 millions de dollars US, et des données de sécurité chez l'humain existent déjà,
si bien que le risque d'échec est plus faible.
</p>

<table class="comparison-table">
<thead>
<tr><th>Aspect</th><th>Développement d'un nouveau médicament</th><th>Repositionnement de médicaments</th></tr>
</thead>
<tbody>
<tr><td>Durée</td><td>10&ndash;15 ans</td><td>3&ndash;5 ans</td></tr>
<tr><td>Coût</td><td>1&ndash;2 milliards USD</td><td>100&ndash;300 millions USD</td></tr>
<tr><td>Données de sécurité</td><td>À établir</td><td>Données humaines déjà disponibles</td></tr>
<tr><td>Risque d'échec</td><td>Très élevé (&gt;90 %)</td><td>Plus faible</td></tr>
</tbody>
</table>

---

## Qu'est-ce que TxGNN ?

<p class="key-answer" data-question="Qu'est-ce que TxGNN ?">
<a href="https://www.nature.com/articles/s41591-024-03233-x">TxGNN</a> est un modèle d'apprentissage profond
développé par le Zitnik Lab de Harvard Medical School et publié dans <em>Nature Medicine</em>.
Il prédit de nouvelles associations médicament&ndash;maladie et constitue le premier modèle de fondation pour le
repositionnement de médicaments conçu spécifiquement pour les cliniciens.
</p>

<blockquote class="expert-quote">
« TxGNN intègre un graphe de connaissances couvrant 17 080 maladies et utilise des réseaux de neurones sur graphes
pour apprendre les relations complexes entre les nœuds, prédisant l'efficacité potentielle de médicaments contre
les maladies rares. »
<cite>&mdash; Huang et al., Nature Medicine (2024)</cite>
</blockquote>

---

## Sources de données

Les sources des prédictions, des preuves et des données sur les médicaments, avec leurs licences et
leur fréquence de mise à jour, sont réunies sur la page <a href="{{ '/sources/' | relative_url }}">Sources de données</a>.

---

## Base académique

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## Échelle

| Élément | Valeur |
|------|-------|
| Rapports de médicaments | {{ site.data.drug_stats.total_drugs }} |
| Autorité réglementaire | ANSM |
| Sites déployés | 30 pays / régions |

---

## Contact

- **GitHub Issues** : <https://github.com/yao-care/FRTxGNN/issues>
- **Développeur** : 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **Présentation du produit** : <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>Avertissement</strong><br>
Ce rapport est destiné uniquement à la recherche académique et <strong>ne constitue pas un avis médical</strong>. Suivez toujours les instructions de votre médecin ; ne modifiez jamais votre traitement de votre propre initiative. Toute décision de repositionnement de médicament nécessite une validation clinique complète et un examen réglementaire.
<br><br>
<small>Relu par : 藥提醒科技有限公司 (yao.care)</small>
</div>
