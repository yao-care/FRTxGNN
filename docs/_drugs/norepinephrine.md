---
layout: default
title: Norepinephrine
parent: Preuves modérées (L3-L4)
nav_order: 545
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Norepinephrine : nouvelle indication prédite, Maladie pulmonaire obstructive (niveau de preuve L4). Indication d'origine : Asthme"
monitor_inn: "norepinephrine"
predicted_indications: ["obstructive lung disease", "respiratory malformation", "Rienhoff syndrome"]
---

# Norepinephrine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **3** 
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

# Norépinéphrine : De l'asthme à la maladie pulmonaire obstructive

## Résumé en Une Phrase

La norépinéphrine (noradrénaline) est un agoniste adrénergique, dont les indications d'origine répertoriées dans la base de connaissances incluent l'asthme, la bronchite, l'emphysème pulmonaire, les bronchectasies et les troubles hypotensifs.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie pulmonaire obstructive**, mais **aucun essai clinique pertinent** ni **aucune publication démontrant un bénéfice clinique** ne soutient actuellement cette direction : la prédiction repose essentiellement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Asthme (texte d'indication des AMM non renseigné ; indications issues du graphe de connaissances : asthme, bronchite, emphysème, bronchectasies, troubles hypotensifs) |
| Nouvelle Indication Prédite | Maladie pulmonaire obstructive |
| Score de Prédiction TxGNN | 99,84 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Uniquement des AMM annulées |
| Nombre d'AMM | 7 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, la norépinéphrine agit sur les récepteurs adrénergiques (alpha et bêta). Le tonus du muscle lisse bronchique et l'inflammation des voies aériennes sont modulés par la signalisation adrénergique ; la bronchodilatation médiée par les récepteurs bêta-2 est la base biologique des traitements adrénergiques de l'asthme et de la BPCO.

Les indications d'origine (asthme, bronchite, emphysème, bronchectasies) relèvent déjà de la sphère des maladies respiratoires obstructives, ce qui explique la proximité de la nouvelle indication prédite dans le graphe de connaissances. Les publications retrouvées (signalisation adrénergique dans l'asthme allergique, innervation des voies aériennes dans l'asthme et la BPCO, circuits neuro-immuns respiratoires) rendent le mécanisme plausible, mais **ne montrent pas de bénéfice clinique de la norépinéphrine elle-même**.

Réserve importante : la norépinéphrine possède de forts effets alpha-1 et bêta-1 cardiaques et n'est pas un bronchodilatateur sélectif. Un usage systémique expose à l'hypertension, aux arythmies et à l'ischémie tissulaire.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | En recrutement | 420 | Fonction vasculaire, exercice et afférences musculaires dans la réadaptation de l'hypertension ; lien indirect avec la maladie pulmonaire obstructive, aucune preuve d'efficacité (pertinence faible) |

## Preuves de la Littérature

Aucune étude clinique contrôlée n'a été retrouvée. Les publications les plus pertinentes sont des revues mécanistiques ou physiologiques :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [29696025](https://pubmed.ncbi.nlm.nih.gov/29696025/) | 2018 | Revue | Front Immunol | Signalisation adrénergique à l'interface de l'asthme allergique et des infections virales |
| [41601146](https://pubmed.ncbi.nlm.nih.gov/41601146/) | 2026 | Revue | Ann Med | Circuits neuro-immuns dans la physiopathologie respiratoire et cibles thérapeutiques |
| [21271508](https://pubmed.ncbi.nlm.nih.gov/21271508/) | 2011 | Revue | Pneumologie | Innervation des voies aériennes dans l'asthme et la BPCO |
| [40870471](https://pubmed.ncbi.nlm.nih.gov/40870471/) | 2025 | Revue narrative | Medicina (Kaunas) | Anxiété et dépression comorbides de la BPCO |
| [35411324](https://pubmed.ncbi.nlm.nih.gov/35411324/) | 2022 | Revue (rapport d'atelier) | JACC Basic Transl Sci | Mécanismes neuraux autonomes de la régulation cardiopulmonaire |
| [3332227](https://pubmed.ncbi.nlm.nih.gov/3332227/) | 1987 | Revue | Crit Care Clin | Catécholamines en soins intensifs |
| [29030339](https://pubmed.ncbi.nlm.nih.gov/29030339/) | 2018 | Étude physiologique | Am J Physiol Heart Circ Physiol | Réactivité alpha-adrénergique musculaire à l'effort chez les patients atteints de BPCO |
| [11099681](https://pubmed.ncbi.nlm.nih.gov/11099681/) | 2000 | Étude clinique | Am J Med | Mécanismes de l'hypertension dans la BPCO avec insuffisance respiratoire aiguë (dont la norépinéphrine plasmatique) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65104648 | NORADRENALINE VIATRIS 2 mg/ml SANS SULFITES | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 64234749 | NORADRENALINE (TARTRATE) AGUETTANT 2 mg/ml (SANS SULFITES) | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |
| 60743407 | TANOREN 0,5 mg/mL | Solution à diluer pour injection ou pour perfusion | Non renseignée (AMM annulée) |
| 60385077 | CRONOMIR 10 microgrammes/mL | Solution injectable ou pour perfusion | Non renseignée (AMM annulée) |
| 64803855 | NORADRENALINE RENAUDIN 2 mg/mL SANS CONSERVATEUR | Solution à diluer pour perfusion | Non renseignée (AMM annulée) |

Au total, 7 AMM sont recensées, toutes annulées ; aucun produit n'est actuellement commercialisé sous ces AMM.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : trouble hypertensif, hypertension, maladie thrombotique.
- **Interactions médicamenteuses** : 70 interactions ont été recensées, toutes de niveau modéré parmi celles listées. Principales : antidiabétiques (metformine, pioglitazone, répaglinide, acarbose), inhibiteurs de la DPP-4 (sitagliptine, saxagliptine, linagliptine, alogliptine), inhibiteurs du SGLT2 (canagliflozine, dapagliflozine, empagliflozine), agonistes du GLP-1 (sémaglutide, dulaglutide, albiglutide), insulines (asparte, dégludec, détémir), ainsi que des anorexigènes/sympathomimétiques (phentermine, diéthylpropion).
- Les mises en garde et contre-indications issues de la notice de l'ANSM n'ont pas pu être exploitées. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé (99,84 %), mais il n'existe aucune preuve clinique : le seul essai retrouvé est indirect et les publications sont mécanistiques. Le profil hémodynamique de la molécule (effets alpha-1 et bêta-1 non sélectifs), l'absence de produit commercialisé en France et l'absence de données de sécurité issues de la notice rendent toute progression prématurée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Notice de l'ANSM (mises en garde et contre-indications) pour le dépistage de sécurité, point bloquant
- Études précliniques ou cliniques évaluant directement la norépinéphrine dans la maladie pulmonaire obstructive
- Analyse de la compatibilité des voies d'administration (seules des formes pour perfusion/injection existent) et du rapport bénéfice/risque cardiovasculaire
- Clarification du statut réglementaire (AMM annulées)

**Remarque sur les autres prédictions :** la « malformation respiratoire » (niveau L5) ne repose que sur un lien indirect avec le contrôle central de la respiration et ne relève pas d'une correction pharmacologique plausible ; le « syndrome de Rienhoff » (niveau L5) ne dispose d'aucun essai ni publication. Les deux sont en Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

