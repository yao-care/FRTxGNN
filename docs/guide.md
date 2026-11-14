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

<p class="key-answer" data-question="Qu'est-ce que TxGNN ?">
TxGNN est le modèle de repositionnement de médicaments développé par le Zitnik Lab de Harvard Medical School et publié
dans <em>Nature Medicine</em>. FRTxGNN est le système de production que 藥提醒科技有限公司 a bâti sur ce modèle pour
la France : il génère les prédictions et les niveaux de preuve présentés dans chaque rapport de médicament.
</p>

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
