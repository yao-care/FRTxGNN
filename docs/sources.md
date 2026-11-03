---
layout: default
title: Sources de données
nav_order: 93
permalink: /sources/
description: "Sources de données de FRTxGNN : Base de données publique des médicaments (BDPM, ANSM), TxGNN, ClinicalTrials.gov, PubMed et DrugBank."
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
<tr><td>Données d'enregistrement</td><td>Base de données publique des médicaments (BDPM, ANSM) : fichiers <a href="https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt">CIS_bdpm.txt</a> et <a href="https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_COMPO_bdpm.txt">CIS_COMPO_bdpm.txt</a></td><td>Médicaments autorisés en France (code CIS), leurs substances et le statut administratif de l'AMM</td></tr>
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

- **TxGNN** : usage académique ; citer Huang et al. (2024)
- **ClinicalTrials.gov / PubMed** : données publiques des NIH des États-Unis
- **DrugBank** : usage non commercial, soumis aux conditions de sa licence
- **BDPM (ANSM)** : fichiers publics téléchargeables sans inscription ; soumis aux conditions de réutilisation de la BDPM

---

## Fréquence de mise à jour

| Données | Fréquence |
|------|-----------|
| Statut administratif des AMM | Mis à jour automatiquement chaque semaine (le lundi) à partir de CIS_bdpm.txt |
| Preuves issues des essais / de la littérature | Recollectées périodiquement |
| Données d'interactions | Revues chaque trimestre |

---

## Citation académique

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## À propos du développeur

Cette plateforme est développée et exploitée par **藥提醒科技有限公司** (yao.care). Les informations sur
l'entreprise, le contexte du modèle TxGNN et la liste complète des sites de la gamme figurent sur la page
<a href="{{ '/about/' | relative_url }}">À propos</a>.

---

<div class="disclaimer">
<strong>Avertissement</strong><br>
Ce rapport est destiné uniquement à la recherche académique et <strong>ne constitue pas un avis médical</strong>. Suivez toujours les instructions de votre médecin ; ne modifiez jamais votre traitement de votre propre initiative. Toute décision de repositionnement de médicament nécessite une validation clinique complète et un examen réglementaire.
<br><br>
<small>Relu par : 藥提醒科技有限公司 (yao.care)</small>
</div>
