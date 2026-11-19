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

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## France : ce que contiennent les fichiers aujourd'hui

| Fichier | Contenu actuel |
|---|---|
| `/data/search-index.json` | {{ site.data.local_facts.files.search_index }} médicaments et leurs indications prédites |
| `/data/drugs.json` | {{ site.data.local_facts.files.drugs_json }} médicaments avec niveau de preuve et indication d'origine |
| `/fhir/MedicationKnowledge/` | {{ site.data.local_facts.fhir.medication_knowledge }} ressources MedicationKnowledge (une par médicament) |
| `/fhir/ClinicalUseDefinition/` | {{ site.data.local_facts.fhir.clinical_use_definition }} ressources ClinicalUseDefinition (une par indication prédite) |

Réutilisation du jeu de données local : [Base de données publique des médicaments (BDPM)](https://base-donnees-publique.medicaments.gouv.fr/), publié par ANSM (Base de données publique des médicaments) ; sa réutilisation relève des conditions de l'éditeur, et ce site n'accorde aucun droit supplémentaire.

{% if site.data.local_facts.top_licensed.size > 0 %}Médicaments ayant le plus d'AMM de la BDPM actives : {% for r in site.data.local_facts.top_licensed limit: 5 offset: 3 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Dernières corrections du journal de vérification : {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 16 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

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
