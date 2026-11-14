---
layout: default
title: Téléchargements
nav_order: 94
permalink: /downloads/
description: "Téléchargements de données ouvertes FRTxGNN : ressources FHIR, résultats de prédiction et index de recherche."
---

# Téléchargements

<div class="key-takeaway">
Les prédictions sont publiées au format FHIR R4, prêtes à être intégrées aux systèmes de dossiers médicaux.
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

## Ressources FHIR

Ce site publie les prédictions sous forme de ressources FHIR R4, directement exploitables par les applications SMART on FHIR :

| Ressource | Chemin | Description |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | Déclaration de capacités du serveur FHIR |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | Ressources médicaments |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | Indications prédites |
| Bundle | `/fhir/Bundle/all-predictions.json` | Ensemble de toutes les prédictions |

---

## Index de recherche

`/data/search-index.json` fournit un index de recherche des médicaments et des indications, permettant de construire votre propre
interface d'interrogation.

---

## Conditions d'utilisation

<ol class="actionable-steps">
<li>Les données de ce site sont <strong>fournies à titre de référence pour la recherche uniquement</strong> et ne doivent pas servir de base à des décisions médicales.</li>
<li>En cas de citation, créditez FRTxGNN (藥提醒科技有限公司) et citez l'article original sur TxGNN.</li>
<li>Les données dérivées restent soumises aux conditions de licence de chaque source originale (voir <a href="{{ '/sources/' | relative_url }}">Sources de données</a>).</li>
</ol>

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
