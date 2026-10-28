---
layout: default
title: Misoprostol
parent: Prédiction du modèle uniquement (L5)
nav_order: 505
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Misoprostol : nouvelle indication prédite, Aménorrhée (niveau de preuve L4). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "MISOPROSTOL"
predicted_indications: ["amenorrhea (disease)", "atypical coarctation of aorta"]
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

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Misoprostol : D'une Indication Non Documentée à l'Aménorrhée
{: .text-alpha }

## Résumé en Une Phrase

Misoprostol est un analogue de la prostaglandine E1, commercialisé en France sous plusieurs noms (MISOONE, GYMISO, ANGUSTA), mais dont l'indication d'origine n'est pas renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**aménorrhée**, mais aucun essai clinique n'est enregistré et **7 publications** seulement, toutes indirectes (avortement médicamenteux, saignements utérins), sont disponibles.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Aménorrhée |
| Score de Prédiction TxGNN | 0,9964 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le misoprostol est un analogue de la prostaglandine E1 qui provoque des contractions utérines et la maturation du col de l'utérus.

Le lien avec l'aménorrhée n'est plausible que dans un sens restreint : régulation des menstruations, évacuation de produits de conception retenus ou interruption d'une grossesse très précoce. Il s'agirait alors d'une absence de règles d'origine gravidique, et non du traitement d'une aménorrhée primaire ou secondaire.

Le score élevé de TxGNN (0,9964) est une prédiction computationnelle, non étayée par des preuves cliniques directes dans l'aménorrhée. La littérature retrouvée porte sur l'avortement médicamenteux, l'avortement manqué et les saignements utérins : elle constitue au mieux une preuve indirecte.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | ECR | Reproductive Sciences | Mifépristone à faible dose et misoprostol auto-administré pour l'avortement médicamenteux ultra-précoce (744 femmes, aménorrhée ≤ 35 jours) |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | ECR (dose-réponse) | Reproductive Sciences | Doses réduites de mifépristone suivies de misoprostol 200 µg pour l'interruption de grossesse ultra-précoce (2 500 femmes) |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Étude clinique | Human Reproduction | Prévention de grossesse non désirée par mifépristone à faible dose et misoprostol avant les règles attendues |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Étude clinique | J Obstet Gynaecol Res | Sécurité et efficacité de l'avortement précoce avec misoprostol auto-administré |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Étude de cohorte | BMJ | Prise en charge médicale de l'avortement manqué et de la grossesse anembryonnaire |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Revue | J Obstet Gynaecol Can | Ablation endométriale dans la prise en charge des saignements utérins anormaux |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Cas clinique | Cureus | Stéatose hépatique aiguë gravidique ; l'aménorrhée n'y est qu'un élément de présentation, sans rapport avec le misoprostol |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61240145 | MISOONE 400 microgrammes (EXELGYN), active | Comprimé sécable | Non renseignée |
| 69981979 | GYMISO 200 microgrammes (LINEPHARMA), active | Comprimé | Non renseignée |
| 60213914 | ANGUSTA 25 microgrammes (NORGINE, Pays-Bas), active | Comprimé | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : hypertension, insuffisance hépatique et maladie du foie, atteinte hépatique d'origine médicamenteuse, maladie de la vésicule biliaire, insuffisance cardiaque congestive, maladie cardiovasculaire et cardiopathie, infarctus du myocarde et thrombose coronaire, accident vasculaire cérébral et infarctus cérébral, maladie inflammatoire de l'intestin, asthme (y compris allergique et intrinsèque), ulcère peptique actif, troubles de la coagulation, hémoglobinopathie, anémie, abus ou dépendance à des substances, méningite non infectieuse.
- **Interactions Médicamenteuses** (100 interactions recensées, principales) :
  - Majeure : dinoprostone (voie topique)
  - Modérée : antiacides à base de magnésium (oxyde, carbonate, hydroxyde), magaldrate, quinapril
  - Mineure : citrate de sodium, hydroxyde d'aluminium, carbonate de calcium, bicarbonate de sodium, naproxène
- **Grossesse** : l'exposition au misoprostol pendant la grossesse a été associée à des anomalies de disruption vasculaire fœtale ; la prudence s'impose.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé, mais il n'y a aucun essai clinique et la littérature, indirecte, concerne l'interruption de grossesse et non le traitement de l'aménorrhée. Les 3 AMM françaises sur 3 sont valides (médicament commercialisé), et les données de sécurité issues de la notice manquent (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Préciser l'indication d'origine du produit
- Définir le type d'aménorrhée visé et rechercher des preuves cliniques directes
- Évaluer la pertinence d'une relance de développement compte tenu du retrait des AMM et du risque tératogène

---

**Note complémentaire** : la 2ᵉ prédiction (coarctation atypique de l'aorte, score 0,9930, niveau L5) ne dispose d'aucune preuve ni d'aucun lien mécanistique clair ; elle est classée **Hold** et n'est pas développée ici.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

