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
