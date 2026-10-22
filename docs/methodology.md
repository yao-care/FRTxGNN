---
layout: default
title: Méthodologie
nav_order: 91
permalink: /methodology/
description: "Comment FRTxGNN produit et valide ses prédictions : prédiction par le modèle TxGNN (apprentissage profond), collecte de preuves, gradation L1-L5 et recommandations de décision."
---

# Méthodologie

<div class="key-takeaway">
De la prédiction par IA à la gradation des preuves — chaque candidat dispose d'une base traçable justifiant sa notation.
</div>

---

## Chaîne de traitement globale

<p class="key-answer" data-question="Comment FRTxGNN produit-il ses prédictions ?">
La plateforme utilise une chaîne de traitement en quatre étapes : le modèle TxGNN (apprentissage profond) prédit les associations
potentielles médicament&ndash;maladie, des preuves sont ensuite collectées automatiquement pour chaque paire prédite,
ces preuves sont graduées de L1 à L5, et enfin une recommandation de décision est émise.
</p>

<ol class="actionable-steps">
<li><strong>Prédiction TxGNN</strong> : relations médicament&ndash;maladie prédites par le modèle TxGNN (apprentissage profond : un réseau de neurones sur graphes entraîné sur un graphe de connaissances biomédical).</li>
<li><strong>Collecte des preuves</strong> : pour chaque paire prédite, les preuves sont rassemblées à partir de ClinicalTrials.gov, PubMed, DrugBank et l'ANSM.</li>
<li><strong>Gradation des preuves</strong> : graduées de L1 à L5, L1 étant le niveau le plus fort (plusieurs ECR de phase 3) et L5 la simple prédiction du modèle.</li>
<li><strong>Recommandation de décision</strong> : Go, Proceed, Consider, Explore ou Hold, selon le niveau de preuve.</li>
</ol>

---

## Critères de gradation des preuves

<table class="comparison-table">
<thead>
<tr><th>Niveau</th><th>Définition</th><th>Signification clinique</th></tr>
</thead>
<tbody>
<tr><td><strong>L1</strong></td><td>Plusieurs ECR de phase 3 / revues systématiques</td><td>Appui solide ; un usage clinique peut être envisagé</td></tr>
<tr><td><strong>L2</strong></td><td>Un seul ECR ou plusieurs essais de phase 2</td><td>Appui modéré ; des essais de validation peuvent être conçus</td></tr>
<tr><td><strong>L3</strong></td><td>Études observationnelles / grandes séries de cas</td><td>Appui préliminaire ; nécessite une validation complémentaire</td></tr>
<tr><td><strong>L4</strong></td><td>Études précliniques / mécanistiques</td><td>Appui théorique ; encore loin d'un usage clinique</td></tr>
<tr><td><strong>L5</strong></td><td>Prédiction du modèle uniquement</td><td>Stade d'hypothèse ; aucune preuve chez l'humain à ce jour</td></tr>
</tbody>
</table>

---

## Comment les prédictions sont produites

Le modèle d'apprentissage profond (DL) de TxGNN attribue un score à chaque couple médicament–maladie. Les indications et contre-indications déjà enregistrées pour le médicament dans le graphe de connaissances (KG) de TxGNN sont ensuite retirées : les pages médicament n'affichent donc que de nouvelles indications prédites avec un score d'au moins 0,99 (jusqu'à 10 par médicament).

| Étape | Rôle |
|-------|------|
| Apprentissage profond (DL) | Le réseau de neurones sur graphe de TxGNN attribue un score à chaque couple médicament–maladie |
| Vérification des usages connus (KG) | Retire les indications et contre-indications déjà enregistrées dans le graphe de connaissances ; elles ne comptent pas comme nouvelles prédictions |
| Collecte des preuves | Interroge ClinicalTrials.gov et PubMed pour chaque prédiction restante et attribue un niveau de preuve (L1–L5) |

---

## Intégration des données réglementaires

Les données d'autorisation des médicaments pour la France proviennent de l'ANSM. Les noms de substances sont mis en correspondance avec
le vocabulaire DrugBank ; les substances qui ne peuvent être appariées — extraits de plantes, vaccins, excipients
et autres éléments non répertoriés par DrugBank — sont exclues de la prédiction.

---

## Limites

<ol class="actionable-steps">
<li>Les prédictions sont des associations statistiques et <strong>n'impliquent ni causalité ni efficacité clinique</strong>.</li>
<li>Une notation L5 signifie une simple prédiction du modèle, sans preuve chez l'humain à l'appui.</li>
<li>La collecte des preuves dépend de bases de données publiques ; les études non publiées ou non indexées ne sont pas prises en compte.</li>
<li>La mise en correspondance des substances peut omettre des éléments en raison de différences de dénomination.</li>
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
modèle : intégration des données nationales d'enregistrement des médicaments, prédiction par apprentissage profond excluant les usages déjà enregistrés dans le graphe de connaissances, gradation des preuves PubMed / ClinicalTrials, et intégration
au dossier médical électronique via SMART on FHIR.

---

<div class="disclaimer">
<strong>Avertissement</strong><br>
Ce rapport est destiné uniquement à la recherche académique et <strong>ne constitue pas un avis médical</strong>. Suivez toujours les instructions de votre médecin ; ne modifiez jamais votre traitement de votre propre initiative. Toute décision de repositionnement de médicament nécessite une validation clinique complète et un examen réglementaire.
<br><br>
<small>Relu par : 藥提醒科技有限公司 (yao.care)</small>
</div>
