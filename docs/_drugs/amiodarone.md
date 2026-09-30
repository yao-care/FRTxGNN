---
layout: default
title: Amiodarone
parent: Prédiction du modèle uniquement (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
---

# Amiodarone
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Amiodarone : D'un antiarythmique commercialisé à la tachycardie ventriculaire polymorphe catécholergique

## Résumé en une phrase

L'amiodarone est un antiarythmique commercialisé en France (Cordarone®), mais l'indication d'origine n'est pas renseignée dans les données disponibles.
Le modèle TxGNN prédit qu'elle pourrait être utile dans la **tachycardie ventriculaire polymorphe catécholergique (TVPC)**.
Cette prédiction repose sur **0 essai clinique** et **10 publications** récupérées, dont aucune ne montre l'efficacité de l'amiodarone dans cette maladie.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Nouvelle indication prédite | Tachycardie ventriculaire polymorphe catécholergique (TVPC) |
| Score de prédiction TxGNN | 99,78 % (rang 2100) |
| Niveau de preuve | L4 (plausibilité mécanistique uniquement) |
| Statut de marché en France | ✓ Commercialisé |
| Nombre d'AMM | 4 |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier. On sait néanmoins que l'amiodarone bloque plusieurs canaux ioniques (potassium, sodium, calcium) et exerce un effet antagoniste bêta-adrénergique. Ces propriétés peuvent en théorie freiner les arythmies ventriculaires.

La TVPC est une maladie génétique rare, déclenchée par le stress adrénergique. Elle est due principalement à une fuite de calcium diastolique via le récepteur RYR2. Les traitements de référence sont les bêta-bloquants et la flécaïne. Le blocage bêta-adrénergique de l'amiodarone offre donc un lien plausible, mais théorique.

Le score élevé du modèle n'est **pas confirmé par les données cliniques**. Les publications retrouvées sont des cohortes, des revues et des cas cliniques sur la TVPC, sans aucune démonstration d'efficacité de l'amiodarone. Les rapports sur la flécaïne suggèrent même que l'amiodarone n'est pas l'agent de choix.

## Preuves d'essais cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la littérature

| PMID | Année | Type | Revue | Résultats principaux |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Revue systématique | Life (Basel) | Caractéristiques cliniques, bases génétiques et évolution rythmique des patients chinois atteints de TVPC. Aucune donnée sur l'amiodarone dans l'extrait disponible. |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohorte rétrospective | Rev Cardiovasc Med | Caractéristiques cliniques, génétique, recours aux soins et coûts de la TVPC dans une ville chinoise. |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Revue | Expert Opin Pharmacother | Avancées du traitement médicamenteux des arythmies ventriculaires (revue générale, non spécifique à la TVPC). |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Cas clinique | PACE | La flécaïne supprime l'orage rythmique induit par le défibrillateur chez un garçon de 14 ans atteint de TVPC (mutation CASQ2). |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Cas clinique | Front Cardiovasc Med | Résolution de la TVPC par dénervation sympathique cardiaque droite chez un adolescent, après une dénervation gauche. |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Cas clinique | Turk Pediatri Arsivi | Arrêt cardiaque soudain révélant une TVPC chez un enfant de 2 ans. |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Cas clinique | Medicine | Diagnostic retardé de 6 ans d'une TVPC avec mutation RYR2 (c.7580T>G) chez un enfant de 9 ans. |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Cas clinique | BMJ Case Rep | Survie d'un jeune enfant après arrêt cardiaque extrahospitalier, avec 40 chocs administrés pour TV/FV récidivantes. |
| [17125720](https://pubmed.ncbi.nlm.nih.gov/17125720/) | 2006 | Cas clinique | Rev Esp Cardiol | Orage rythmique induit par une décharge du défibrillateur chez un patient atteint de TVPC. |
| [22218697](https://pubmed.ncbi.nlm.nih.gov/22218697/) | 2012 | Cas clinique | Anesth Analg | Nouveau-né avec syndrome du QT long et arythmies réfractaires, traité par lidocaïne, esmolol et amiodarone. Il s'agit d'un QT long, pas d'une TVPC. |

## Informations de marché en France

| Numéro d'AMM | Nom du produit | Forme pharmaceutique | Fabricant |
|---------|------|------|-----------|
| 62305927 | CORDARONE 150 mg/3 ml | Solution injectable en ampoule (IV) | SANOFI WINTHROP INDUSTRIE |
| 64408662 | CORDARONE 200 mg | Comprimé sécable | SANOFI WINTHROP INDUSTRIE |
| 68973926 | CORDARONE 200 mg | Comprimé sécable | BB FARMA (Italie) |
| 60662396 | CORDARONE 200 mg | Comprimé sécable | DIFARMED (Espagne) |

## Considérations de sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la TVPC repose uniquement sur le modèle et sur une plausibilité mécanistique. Aucun essai ni publication ne montre l'efficacité de l'amiodarone, et les traitements établis (bêta-bloquants, flécaïne) sont préférés.
- Parmi les autres prédictions du même dossier, la **tachycardie ventriculaire** (niveau L1, décision « Proceed with Guardrails ») correspond à un usage déjà établi de l'amiodarone. Elle est appuyée par des essais randomisés (dont VANISH, NCT00905853), mais ce n'est pas un vrai repositionnement. La **tachycardie ventriculaire incessante du nourrisson** (niveau L3) reste une question de recherche.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité).
- Les données de mécanisme d'action (MOA) depuis DrugBank.
- Une recherche bibliographique ciblée « amiodarone et TVPC » pour vérifier l'existence de données directes.
- Une comparaison avec les traitements de référence (bêta-bloquants, flécaïne) avant tout passage à l'étape suivante.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

