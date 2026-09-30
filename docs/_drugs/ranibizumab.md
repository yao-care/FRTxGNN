---
layout: default
title: Ranibizumab
parent: Preuves élevées (L1-L2)
nav_order: 259
evidence_level: L1
indication_count: 10
---

# Ranibizumab
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Ranibizumab : De l'Indication Originale Non Renseignée à la Rétinopathie Diabétique Non Proliférante Sévère

## Résumé en Une Phrase

Le ranibizumab est un fragment d'anticorps anti-VEGF-A administré par voie intravitréenne. Les données fournies ne précisent pas son indication d'origine, mais il est commercialisé en France sous plusieurs noms (Lucentis et biosimilaires).
Le modèle TxGNN prédit qu'il pourrait être efficace dans la **rétinopathie diabétique non proliférante sévère**,
avec **6 essais cliniques** (dont 4 de phase 3) et **19 publications** soutenant actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données (les textes d'indication des AMM sont vides) |
| Nouvelle Indication Prédite | Rétinopathie diabétique non proliférante sévère |
| Score de Prédiction TxGNN | 99,99 % (rang 181) |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 6 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées de DrugBank sur le mécanisme d'action ne sont pas disponibles. Le ranibizumab est toutefois un fragment d'anticorps dirigé contre le VEGF-A. Dans la rétinopathie diabétique, un excès de VEGF favorise la fuite vasculaire et la néovascularisation. Le bloquer correspond donc directement au mécanisme de la maladie.

Les données fournies n'indiquent pas d'indication d'origine. Le dossier note cependant que le ranibizumab est commercialisé pour des maladies vasculaires rétiniennes. Il faudra confirmer le statut exact de chaque indication auprès de l'ANSM. Le lien mécanistique reste le même : le VEGF est la cible commune de ces maladies rétiniennes.

Les essais DRCR Protocol I et RIDE/RISE, menés dans l'œdème maculaire diabétique, ont aussi montré un effet du ranibizumab sur la sévérité de la rétinopathie. Cela renforce la plausibilité de la prédiction.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Phase 3 | Terminé | 174 | Étude Pavilion : système d'administration continue de ranibizumab (Port Delivery System) contre comparateur dans la rétinopathie diabétique sans œdème maculaire central. Pertinence A : population cible. |
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Phase 3 | Terminé | 691 | DRCR Protocol I : ranibizumab ou triamcinolone + laser dans l'œdème maculaire diabétique. Population œdème maculaire, mais des effets sur la sévérité de la rétinopathie sont observés. |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Phase 3 | Terminé | 399 | Traitement anti-VEGF pour prévenir les complications menaçant la vue dans la rétinopathie non proliférante à haut risque. Il s'agit probablement du DRCR Protocol W, qui aurait utilisé l'aflibercept : soutien au niveau de la classe. |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Phase 3 | Inconnu | 118 | Ranibizumab intravitréen contre injections simulées pour prévenir la rétinopathie diabétique à haut risque. Le statut est inconnu. |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Phase 4 | Terminé | 25 | Étude pilote monocentrique : ranibizumab dans l'œdème maculaire avec rétinopathie non proliférante, effets sur les microanévrismes et la zone non perfusée. Petit échantillon. |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | Inconnu | 1000 | Étude observationnelle en vie réelle des anti-VEGF (DMLA exsudative, rétinopathie diabétique proliférante, œdème maculaire, néovascularisation choroïdienne). Pertinence faible. |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | ECR | JAMA Ophthalmol | Essai Pavilion : ranibizumab par Port Delivery System contre surveillance dans la rétinopathie non proliférante sans œdème maculaire |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Revue systématique et méta-analyse | Health Technol Assess | Anti-VEGF comparés à la photocoagulation laser dans la rétinopathie diabétique |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Revue systématique et analyse économique | Health Technol Assess | Anti-VEGF contre laser, avec analyse économique |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | Analyse secondaire d'ECR | Retina | DRCR Protocol I à 5 ans : évolution de la sévérité de la rétinopathie sous ranibizumab |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | Analyse secondaire d'ECR | JAMA Ophthalmol | Évolution de la rétinopathie à 2 ans : aflibercept, bevacizumab et ranibizumab comparés |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Analyse post hoc d'ECR | Clin Ophthalmol | Facteurs prédictifs de régression précoce de la rétinopathie sous ranibizumab (RIDE/RISE) |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Méta-analyse post hoc d'ECR | Ophthalmol Retina | Sévérité initiale de la rétinopathie et délai de résolution de l'œdème maculaire sous ranibizumab |
| [35417296](https://pubmed.ncbi.nlm.nih.gov/35417296/) | 2022 | Analyse post hoc d'ECR | Ophthalmic Surg Lasers Imaging Retina | Évolution de la rétinopathie dans les yeux controlatéraux non traités (RIDE/RISE) |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | Analyse post hoc d'ECR | BMJ Open Ophthalmol | Effet d'un traitement moins fréquent sur les scores de sévérité DRSS (extension RIDE/RISE) |
| [37278412](https://pubmed.ncbi.nlm.nih.gov/37278412/) | 2023 | Modélisation | BMJ Open Ophthalmol | Simulation de l'impact à long terme d'un traitement anti-VEGF proactif dans la rétinopathie non proliférante sévère |

## Informations de Marché en France

Le dossier indique 6 AMM au total, mais seules 5 sont détaillées. Le texte d'indication approuvée est vide pour toutes.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68654266 | BYOOVIZ 10 mg/mL (Samsung Bioepis) | Solution injectable | Non renseignée |
| 64339586 | LUCENTIS 10 mg/ml, seringue préremplie (Novartis Europharm) | Solution injectable | Non renseignée |
| 68594506 | RANIVISIO 10 mg/mL, seringue préremplie (Midas Pharma) | Solution injectable | Non renseignée |
| 64389258 | RANIVISIO 10 mg/mL (Midas Pharma) | Solution injectable | Non renseignée |
| 67026689 | XIMLUCI 10 mg/mL (Stada Arzneimittel) | Solution injectable | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Les données de sécurité de l'ANSM n'ont pas pu être récupérées. Aucune interaction médicamenteuse n'a été trouvée dans la base interrogée. Un signal de sécurité oculaire est signalé dans la littérature : une opacification du cristallin et un cas de syndrome de blocage capsulaire ont été rapportés après injection intravitréenne de ranibizumab (PMID 38476863).

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Plusieurs essais de phase 3 terminés soutiennent la prédiction, dont l'essai Pavilion, mené directement chez des patients atteints de rétinopathie non proliférante et publié en 2025. Le mécanisme anti-VEGF est cohérent avec la maladie. Toutefois, les notices de l'ANSM (contre-indications, mises en garde) manquent, ce qui bloque le criblage de sécurité. Une partie des preuves concerne l'œdème maculaire ou d'autres anti-VEGF, ou le système d'administration continue (Port Delivery System) plutôt que l'injection standard.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser les notices de l'ANSM (mises en garde, contre-indications)
- Confirmer les indications autorisées de chaque AMM en France
- Compléter les données de mécanisme d'action (DrugBank)
- Vérifier quel anti-VEGF a été utilisé dans NCT02634333 et NCT03452657, et le statut de ce dernier essai
- Évaluer séparément l'injection standard et le Port Delivery System pour la rétinopathie non proliférante

**Autres prédictions du modèle :** les prédictions suivantes n'ont pas de mécanisme plausible ni de preuve clinique de bénéfice. Elles sont classées **Hold** :
- cataractes (immature, mature, tétanique, craniosténose, associée au diabète de type 2, nucléaire sénile, corticale, sénile) ;
- maladie hémorragique du nouveau-né.

Pour la cataracte, les données disponibles évoquent plutôt un signal de sécurité qu'un bénéfice. Le score élevé semble refléter une proximité dans le graphe de connaissances.

*Ce rapport est fourni à titre de référence pour la recherche et ne constitue pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

