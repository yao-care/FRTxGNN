---
layout: default
title: Politique de confidentialité
nav_order: 95
permalink: /privacy-policy/
description: "Politique de confidentialité de FRTxGNN : site statique sans compte ni formulaire ; il utilise des cookies de mesure d'audience de Google Analytics 4."
---

# Politique de confidentialité

<div class="key-takeaway">
Il s'agit d'un site statique — aucune inscription, aucun formulaire. Il utilise des cookies de mesure d'audience de Google Analytics 4 pour établir des statistiques d'utilisation.
</div>

---

## Ce que nous collectons

<p class="key-answer" data-question="FRTxGNN collecte-t-il des données personnelles ?">
<strong>Uniquement des statistiques d'utilisation, via Google Analytics 4.</strong> Ce site est hébergé sur GitHub Pages en tant que
site purement statique. Il n'existe aucun système de comptes ni aucun formulaire, et nous ne collectons ni noms, ni
adresses e-mail, ni dossiers médicaux. Le site utilise des cookies de mesure d'audience de Google Analytics 4 pour
établir des statistiques d'utilisation (pages consultées, site d'origine, profondeur de défilement et temps passé sur
la page). Les cookies sont déposés au chargement de la page ; les termes de recherche, le contenu des formulaires et
les paramètres de requête de l'URL ne sont pas transmis.
</p>

---

## Services tiers

Le site utilise les ressources tierces suivantes, qui peuvent enregistrer les accès conformément à leurs propres
politiques :

| Service | Finalité | Politique de confidentialité |
|---------|---------|----------------|
| GitHub Pages | Hébergement du site | [Déclaration de confidentialité de GitHub](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement) |
| Google Analytics 4 (www.googletagmanager.com, google-analytics.com) | Statistiques de visite (pages consultées, provenance) ; utilise des cookies de mesure d’audience. Les termes recherchés, le contenu des formulaires et les paramètres d’URL ne sont pas transmis. | [Règles de confidentialité de Google](https://policies.google.com/privacy) |
| cdn.jsdelivr.net | Bibliothèques de scripts : graphiques d3 sur toutes les pages ; Fuse.js pour la correspondance des noms et le client SMART on FHIR sur les pages SMART | [Politique de confidentialité de jsDelivr](https://www.jsdelivr.com/terms/privacy-policy-jsdelivr-net) |
| clinicaltrials.gov | Recherche d’essais cliniques sur les pages SMART : uniquement lorsque vous la demandez, les noms du médicament et de l’indication sont envoyés à l’API de ClinicalTrials.gov | [Politiques web de la NLM](https://www.nlm.nih.gov/web_policies.html) |
| rxnav.nlm.nih.gov | Application SMART : les codes RxNorm des médicaments lus dans votre dossier patient informatisé sont envoyés à l’API RxNav de la NLM pour retrouver le nom de la substance active (aucun identifiant de patient) | [Politiques web de la NLM](https://www.nlm.nih.gov/web_policies.html) |

Lorsque vous lancez volontairement l'application SMART on FHIR, celle-ci demande des données de traitement à votre système
de dossier médical électronique. L'identité du patient et les données du dossier <strong>ne sont pas envoyées aux serveurs
de ce site</strong> (il s'agit d'un site statique, sans serveur applicatif) et ne sont pas stockées par ce site. Pour faire
correspondre les noms de médicaments, l'application envoie leurs codes RxNorm au service RxNav de la National Library of
Medicine des États-Unis ; ces codes ne contiennent aucune information permettant d'identifier le patient. Lorsque vous
demandez les essais cliniques, le nom du médicament et l'indication sont envoyés à ClinicalTrials.gov.

---

## Droits des personnes concernées

Ce site n'a pas de comptes et ne conserve aucune donnée personnelle sur des serveurs propres (il n'en a pas). Les
statistiques d'utilisation sont collectées par Google Analytics 4 ; vous pouvez bloquer ou supprimer ses cookies dans les
paramètres de votre navigateur.
Pour toute question sur cette politique, contactez service@yao.care.

---

## Modifications de cette politique

Toute modification sera publiée directement sur cette page.

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
