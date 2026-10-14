---
layout: default
title: Ketamine
parent: Prédiction du modèle uniquement (L5)
nav_order: 422
evidence_level: L5
indication_count: 1
---

# Ketamine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Kétamine : D'une indication d'origine non renseignée à la céphalée (headache disorder)

## Résumé en Une Phrase

La kétamine est un anesthésique/analgésique injectable (spécialités KETAMINE PANPHARMA 10 mg/mL et 50 mg/mL, voie I.V.-I.M.), dont l'indication d'origine n'est pas renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour les **céphalées (headache disorder)**,
avec **8 essais cliniques** et **20 publications** associés, dont une partie seulement est directement pertinente.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les AMM disponibles |
| Nouvelle Indication Prédite | Céphalée (headache disorder) |
| Score de Prédiction TxGNN | 99,33 % |
| Niveau de Preuve | L1 (selon les règles du modèle : un seul essai de Phase 3 terminé, THINK, et un essai de Phase 3 encore en recrutement ; niveau à interpréter avec prudence) |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la fiche du médicament. D'après les connaissances pharmacologiques générales, la kétamine est un antagoniste des récepteurs NMDA du glutamate.

La signalisation glutamatergique médiée par les récepteurs NMDA contribue à la sensibilisation centrale, à la nociception trigémino-vasculaire et à la dépression corticale envahissante, mécanismes impliqués dans la migraine, l'algie vasculaire de la face et d'autres céphalées chroniques. Bloquer ces récepteurs pourrait réduire l'amplification de la douleur (phénomène de « wind-up »).

Le score élevé de TxGNN est cohérent avec cette plausibilité biologique, mais le lien mécanistique repose sur la pharmacologie générale et non sur les données de la fiche médicament. Les preuves sont plus solides pour le traitement aigu aux urgences que pour les céphalées chroniques ou réfractaires, et l'hétérogénéité des sous-types (migraine, céphalée de tension, algie vasculaire, céphalée quotidienne chronique) limite la généralisation.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Terminé | 80 | Essai THINK : kétamine intranasale à dose sub-dissociative vs traitement standard pour les céphalées primaires aux urgences |
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Phase 3 | En recrutement | 56 | Kétamine IV à forte dose vs placebo dans les céphalées quotidiennes chroniques (KetHead) ; pas encore de résultats |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Phase 4 | Terminé | 54 | Kétamine à faible dose vs prochlorpérazine pour les céphalées aux urgences |
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Phase 4 | Terminé | 93 | Perfusion unique de kétamine + sulfate de magnésium dans l'algie vasculaire de la face chronique réfractaire |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Inconnu | 60 | Kétamine vs kétorolac dans la céphalée de tension aiguë |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | Non applicable | Terminé | 34 | Kétamine sub-dissociative vs placebo dans la céphalée de type migraine aux urgences |
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Phase 1/2 | Terminé | 23 | Preuve de concept : spray nasal de kétamine dans l'algie vasculaire de la face chronique |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Phase 4 | Terminé | 5 | Kétamine orale + aspirine vs rimégépant aux urgences ; échantillon trop petit pour être interprétable |

Remarque : l'essai NCT02403687 (étude PACE, AINS topiques) n'a pas de lien direct avec la kétamine dans les céphalées et n'est pas retenu.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [34703891](https://pubmed.ncbi.nlm.nih.gov/34703891/) | 2021 | Revue systématique | J Dent Anesth Pain Med | Efficacité de la kétamine dans la migraine et les autres céphalées primaires comparée au placebo et à d'autres traitements |
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | Étude de cohorte rétrospective | Front Neurol | Perfusions de lidocaïne et de kétamine dans les céphalées : efficacité, durée et sécurité |
| [36310189](https://pubmed.ncbi.nlm.nih.gov/36310189/) | 2023 | Revue systématique et méta-analyse | J Neurol | Traitement préventif de l'algie vasculaire de la face chronique réfractaire |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Recommandations | Headache | Mise à jour 2025 des recommandations de l'AHS sur le traitement aigu de la migraine aux urgences (thérapies parentérales) |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Revue | Drugs | Traitement médicamenteux de l'algie vasculaire de la face |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Revue | Expert Rev Neurother | Kétamine et cannabinoïdes comme options adjuvantes possibles dans la névralgie du trijumeau |

Les autres publications retrouvées concernent surtout la dépression, l'abus d'alcool ou d'autres douleurs, et ne sont pas directement liées aux céphalées.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62768665 | KETAMINE PANPHARMA 10 mg/mL, solution injectable (I.V.-I.M.) | Solution injectable | Non renseignée (AMM annulée) |
| 69278297 | KETAMINE PANPHARMA 50 mg/mL, solution injectable (I.V.-I.M.) | Solution injectable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (à confirmer avec la notice)** : hypertension artérielle, hypertension intracrânienne et pseudotumeur cérébrale, hypertension oculaire, accident vasculaire cérébral et maladies cérébrovasculaires, infarctus du myocarde et ischémie myocardique, maladie coronarienne, insuffisance respiratoire, hyperthyroïdie (dont maladie de Basedow), délire, abus ou dépendance aux substances, hémoglobinopathies.
- **Interactions médicamenteuses** : 111 interactions recensées. Parmi les principales, de niveau modéré : morphine, diphénoxylate, dronabinol, métoclopramide, nabilone, opium, sibutramine, phentermine, éphédrine, fenfluramine, isométheptène, épinéphrine (topique). Des interactions de niveau inconnu concernent notamment l'atropine, l'amphotéricine B, la famotidine, l'oméprazole, le chlorure de potassium, l'ondansétron et l'acide ursodésoxycholique.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les essais dans les céphalées sont nombreux mais de petite taille, hétérogènes (sous-types, voies d'administration, comparateurs) et l'essai de Phase 3 en cours n'a pas encore de résultats. De plus, les AMM françaises sont toutes annulées et les données de sécurité issues de la notice manquent (lacune bloquante), ce qui empêche de passer à l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications) sur le site de l'ANSM
- Compléter les données sur le mécanisme d'action via DrugBank
- Obtenir les résultats de l'essai KetHead (NCT05306899) et ceux publiés de l'essai THINK (NCT03081416)
- Préciser le sous-type de céphalée visé (aiguë aux urgences ou chronique réfractaire) et la voie d'administration
- Clarifier la situation réglementaire (AMM annulées) et la faisabilité d'une voie d'administration adaptée
- Évaluer le profil de risque cardiovasculaire, cérébrovasculaire et d'abus potentiel dans la population cible
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

