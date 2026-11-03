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
