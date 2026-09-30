---
layout: default
title: Misoprostol
parent: Prédiction du modèle uniquement (L5)
nav_order: 199
evidence_level: L5
indication_count: 2
---

# Misoprostol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Misoprostol : D'une Indication d'Origine Non Renseignée à l'Aménorrhée

## Résumé en Une Phrase

Misoprostol est un analogue de la prostaglandine E1 à activité utérotonique et de maturation cervicale. Son indication d'origine n'est pas renseignée dans les données ANSM de ce dossier.
Le modèle TxGNN le prédit comme potentiellement efficace pour l'**aménorrhée**, mais **aucun essai clinique** et **7 publications** seulement sont disponibles, dont aucune ne porte sur le traitement de l'aménorrhée.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (texte d'indication vide pour les 3 AMM) |
| Nouvelle Indication Prédite | Aménorrhée |
| Score de Prédiction TxGNN | 99,64 % |
| Niveau de Preuve | L5 (prédiction du modèle uniquement, aucune étude directe) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Misoprostol est un analogue synthétique de la prostaglandine E1, avec une activité utérotonique et de maturation cervicale.

La littérature retrouvée concerne l'avortement médicamenteux (mifépristone + misoprostol), l'avortement manqué et les saignements utérins anormaux. Elle ne porte pas sur le traitement de l'aménorrhée. Le terme « aménorrhée » y apparaît surtout comme critère d'âge gestationnel (par exemple « aménorrhée ≤ 35 jours »). La grossesse est une cause fréquente d'aménorrhée. Le score élevé de TxGNN reflète donc probablement une association dans le graphe de connaissances entre le médicament et la sphère reproductive, plutôt qu'un effet thérapeutique.

Sur le plan pharmacologique, misoprostol tend à provoquer des saignements utérins, ce qui va à l'opposé de l'effet recherché dans un traitement de l'aménorrhée. La plausibilité mécanistique de cette prédiction est donc faible.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune de ces publications n'évalue misoprostol comme traitement de l'aménorrhée. Elles constituent des preuves indirectes.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | ECR | Reprod Sci | Mifépristone à faible dose + misoprostol auto-administré pour l'avortement médicamenteux ultra-précoce (744 femmes, aménorrhée ≤ 35 jours) : efficacité, sécurité et acceptabilité |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | ECR (recherche de dose) | Reprod Sci | Doses réduites de mifépristone (150 à 50 mg) suivies de misoprostol 200 µg pour l'interruption de grossesse ultra-précoce (2 500 femmes) |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Étude clinique | Hum Reprod | Prévention de grossesse non désirée par mifépristone à faible dose + misoprostol avant les règles attendues |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Étude clinique | J Obstet Gynaecol Res | Avortement médicamenteux précoce avec mifépristone à faible dose et misoprostol auto-administré |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Revue | J Obstet Gynaecol Can | Ablation endométriale dans la prise en charge des saignements utérins anormaux (misoprostol n'est pas le sujet) |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Revue / rapport clinique | BMJ | Prise en charge médicale de l'avortement manqué et de la grossesse anembryonnaire |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Rapport de cas | Cureus | Stéatose hépatique aiguë gravidique : difficulté diagnostique (l'aménorrhée est un symptôme de présentation, sans lien avec l'effet de misoprostol) |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 61240145 | MISOONE 400 microgrammes | Comprimé sécable | EXELGYN |
| 69981979 | GYMISO 200 microgrammes | Comprimé | LINEPHARMA |
| 60213914 | ANGUSTA 25 microgrammes | Comprimé | NORGINE (Pays-Bas) |

Les textes d'indication approuvée ne sont pas disponibles dans les données actuelles.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique n'existe et la littérature ne concerne pas le traitement de l'aménorrhée. Le score TxGNN élevé (99,64 %) est probablement un artefact d'association avec la grossesse et l'avortement, et l'effet pro-hémorragique de misoprostol est mécanistiquement contraire à l'objectif thérapeutique.
- La seconde indication prédite, la coarctation atypique de l'aorte (score 99,30 %), n'a ni essai ni publication. Le seul lien plausible est l'usage de l'alprostadil (PGE1) pour maintenir le canal artériel ouvert chez le nouveau-né. Misoprostol n'est pas utilisé dans ce but. Cette indication est également en Hold (L5).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les notices ANSM (mises en garde, contre-indications, indications approuvées). Cette lacune est bloquante pour le criblage de sécurité.
- Compléter les données sur le mécanisme d'action (DrugBank).
- Confirmer l'indication d'origine de chaque AMM.
- Rechercher de la littérature ciblée sur misoprostol dans le traitement de l'aménorrhée ou de ses causes, hors grossesse.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

