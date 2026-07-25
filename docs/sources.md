---
layout: default
title: Sources de données
nav_order: 93
permalink: /sources/
description: "Sources de données de FRTxGNN : données d'enregistrement de l'ANSM, TxGNN, ClinicalTrials.gov, PubMed et DrugBank."
---

# Sources de données

<div class="key-takeaway">
Chaque conclusion remonte à une source de données publique — rien n'est une boîte noire.
</div>

---

## Vue d'ensemble des sources

<table class="comparison-table">
<thead>
<tr><th>Type</th><th>Source</th><th>Utilisée pour</th></tr>
</thead>
<tbody>
<tr><td>Données d'enregistrement</td><td><a href="https://ansm.sante.fr/">ANSM</a></td><td>Liste des médicaments autorisés et de leurs substances pour la France</td></tr>
<tr><td>Modèle de prédiction</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Prédiction des associations médicament&ndash;maladie</td></tr>
<tr><td>Essais cliniques</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Gradation des preuves (NCT)</td></tr>
<tr><td>Littérature</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Gradation des preuves (PMID)</td></tr>
<tr><td>Informations sur les médicaments</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Mise en correspondance des substances et données sur les cibles</td></tr>
<tr><td>Interactions</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Données sur les interactions médicamenteuses</td></tr>
</tbody>
</table>

---

## Licences

Chaque source dispose de sa propre licence — veuillez la consulter avant toute citation :

- **TxGNN** : usage académique ; citer Huang et al. (2023)
- **ClinicalTrials.gov / PubMed** : données publiques des NIH des États-Unis
- **DrugBank** : usage non commercial, soumis aux conditions de sa licence
- **ANSM** : soumis aux conditions d'ouverture des données du régulateur français

---

## Fréquence de mise à jour

| Données | Fréquence |
|------|-----------|
| Données d'enregistrement | Selon la publication du régulateur |
| Preuves issues des essais / de la littérature | Recollectées périodiquement |
| Données d'interactions | Revues chaque trimestre |

---

## Citation académique

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

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
modèle : intégration des données nationales d'enregistrement des médicaments, double prédiction par graphe de
connaissances et apprentissage profond, gradation des preuves PubMed / ClinicalTrials, et intégration
au dossier médical électronique via SMART on FHIR.

---

<div class="disclaimer">
<strong>Avertissement</strong><br>
Ce rapport est destiné uniquement à la recherche académique et <strong>ne constitue pas un avis médical</strong>. Suivez toujours les instructions de votre médecin ; ne modifiez jamais votre traitement de votre propre initiative. Toute décision de repositionnement de médicament nécessite une validation clinique complète et un examen réglementaire.
<br><br>
<small>Relu par : 藥提醒科技有限公司 (yao.care)</small>
</div>
