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
