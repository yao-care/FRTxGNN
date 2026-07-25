---
layout: default
title: Guide d'utilisation
nav_order: 92
permalink: /guide/
description: "Guide d'utilisation de FRTxGNN : comment rechercher un médicament, lire les niveaux de preuve et interpréter les recommandations."
---

# Guide d'utilisation

<div class="key-takeaway">
Vérifiez d'abord le niveau de preuve, puis la recommandation, puis lisez la littérature source.
</div>

---

## Rechercher un médicament

<ol class="actionable-steps">
<li>Utilisez le champ de recherche en haut de la page (les dénominations communes des substances donnent de meilleurs résultats que les noms de marque).</li>
<li>Ou parcourez la liste complète sur <a href="{{ '/drugs/' | relative_url }}">Tous les médicaments</a>.</li>
<li>Vous pouvez aussi parcourir par niveau de preuve : <a href="{{ '/evidence-high/' | relative_url }}">élevé</a>, <a href="{{ '/evidence-medium/' | relative_url }}">modéré</a>, <a href="{{ '/evidence-low/' | relative_url }}">prédiction du modèle uniquement</a>.</li>
</ol>

---

## Lire un rapport

<p class="key-answer" data-question="Que signifient les niveaux de preuve L1 à L5 ?">
Chaque rapport de médicament liste les nouvelles indications prédites, et chaque indication porte un niveau de preuve
L1&ndash;L5. <strong>L1 signifie que plusieurs essais contrôlés randomisés de phase 3 l'appuient déjà ; L5 signifie
une simple prédiction du modèle, sans preuve chez l'humain.</strong> Les critères complets figurent sur la page
<a href="{{ '/methodology/' | relative_url }}">Méthodologie</a>.
</p>

| Si vous voyez | Cela signifie | Action suggérée |
|-----------|----------|------------------|
| L1 / L2 | Des preuves issues d'essais cliniques existent | Consultez les enregistrements sources NCT et PMID |
| L3 / L4 | Preuves observationnelles ou précliniques | À considérer comme une piste de recherche |
| L5 | Prédiction du modèle uniquement | Génération d'hypothèses seulement ; pas de valeur de référence clinique |

---

## Citation et traçabilité

Chaque élément de preuve figurant dans un rapport porte un identifiant traçable :

- **Numéro NCT** : renvoie à l'enregistrement sur ClinicalTrials.gov
- **PMID** : renvoie à la notice PubMed
- **Identifiant DrugBank** : renvoie aux données sur le médicament et ses cibles

Veuillez lire la littérature source pour vérifier le contexte avant de citer une conclusion de cette plateforme.

---

## Questions fréquentes

<p class="key-answer" data-question="Les prédictions peuvent-elles être utilisées en clinique ?">
<strong>Non.</strong> Les prédictions de cette plateforme sont des pistes de recherche, et non des conseils cliniques. Toute
application clinique d'un repositionnement de médicament doit passer par une validation complète par essais cliniques et
un examen réglementaire.
</p>

<p class="key-answer" data-question="Pourquoi ne puis-je pas trouver un médicament particulier ?">
Une substance doit correspondre au vocabulaire DrugBank pour être incluse dans la prédiction. Les extraits de plantes,
les vaccins, les excipients et les autres éléments non répertoriés par DrugBank n'apparaissent pas sur cette plateforme.
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
