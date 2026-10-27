---
layout: default
title: Buprenorphine
parent: Preuves modérées (L3-L4)
nav_order: 124
evidence_level: L4
indication_count: 6
last_modified_at: 2026-10-14
description: "Buprenorphine : nouvelle indication prédite, Porphyrie aiguë intermittente (niveau de preuve L4). Indication d'origine : Dépendance aux opiacés"
monitor_inn: "buprenorphine"
predicted_indications: ["acute intermittent porphyria", "lingual-facial-buccal dyskinesia", "chronic tic disorder", "continuous spikes and waves during sleep", "benign shuddering attacks", "extrapyramidal and movement disease"]
---

# Buprenorphine
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **6** 
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

## Buprénorphine : De la dépendance aux opiacés à la porphyrie aiguë intermittente
{: .text-alpha }

## Résumé en Une Phrase

La buprénorphine est un agoniste partiel des récepteurs opioïdes, initialement utilisé dans le traitement de la dépendance aux opiacés (et, sous forme de Temgesic, comme antalgique).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **porphyrie aiguë intermittente**, mais **aucun essai clinique** et **une seule publication** (un rapport de cas de prise en charge anesthésique, sans lien thérapeutique) soutiennent cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dépendance aux opiacés (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas disponible) |
| Nouvelle Indication Prédite | Porphyrie aiguë intermittente |
| Score de Prédiction TxGNN | 99,41 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 10 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, la buprénorphine est un agoniste partiel des récepteurs opioïdes mu et un antagoniste kappa. Son efficacité dans la dépendance aux opiacés est établie.

La porphyrie aiguë intermittente est un trouble neuroviscéral causé par un défaut de la biosynthèse de l'hème. Aucun lien mécanistique thérapeutique n'est établi : l'activité sur les récepteurs mu n'a pas de rôle connu dans la correction de cette voie métabolique. Au mieux, la buprénorphine pourrait servir d'antalgique lors des crises, ce qui reste symptomatique et ne modifie pas la maladie.

Le score élevé (0,994) est donc une prédiction du modèle, non étayée par des données cliniques. La seule publication retrouvée (PMID 8301837, 1993) concerne la sécurité des médicaments en période périopératoire, et non le traitement de la maladie.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Rapport de cas | Masui (Jpn J Anesthesiol) | Prise en charge anesthésique d'une patiente suspectée de porphyrie aiguë intermittente lors d'une hystérectomie pour tumeur ovarienne maligne ; concerne la sécurité périopératoire, pas un traitement de la maladie |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62157859 | BUVIDAL 64 mg | Solution injectable à libération prolongée | Non disponible |
| 65489051 | BUVIDAL 96 mg | Solution injectable à libération prolongée | Non disponible |
| 61617482 | BUVIDAL 24 mg | Solution injectable à libération prolongée | Non disponible |
| 65870700 | BUVIDAL 128 mg | Solution injectable à libération prolongée | Non disponible |
| 62299972 | TEMGESIC 0,3 mg/ml | Solution injectable | Non disponible |

Les 10 AMM recensées (dont 8 BUVIDAL et 2 TEMGESIC) sont toutes annulées ; aucune n'est actuellement valide.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : syndrome du QT long (y compris familial) et torsades de pointes ; hypotension orthostatique, atrophie multisystématisée et syndrome de tachycardie posturale ; bronchopneumopathie chronique obstructive et insuffisance respiratoire ; maladie hépatique et hépatites virales B/C chroniques ; occlusion intestinale et iléus paralytique ; hypothyroïdie et myxœdème ; insuffisance surrénalienne (maladie d'Addison) ; hypertension intracrânienne ; hyperplasie bénigne de la prostate et sténose urétrale ; maladie de la vésicule biliaire.
- **Interactions médicamenteuses** : 264 interactions recensées. Parmi les principales de niveau majeur : morphine, bupropion, alvimopan, cisapride, dolasétron. De nombreuses interactions de niveau modéré existent également (famotidine, cimétidine, clarithromycine, atropine, dexaméthasone, lopéramide, etc.).

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique n'existe, la seule publication ne porte pas sur un effet thérapeutique, et aucun mécanisme plausible n'est établi. Le score TxGNN seul ne suffit pas. Par ailleurs, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications, indispensables au criblage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Démontrer un lien mécanistique ou des données précliniques/cliniques spécifiques à la porphyrie aiguë intermittente
- Évaluer la sécurité dans la porphyrie, notamment les interactions et la tolérance des opioïdes
- Clarifier le statut réglementaire, toutes les AMM étant annulées

Les autres indications prédites (dyskinésie linguo-faciale-buccale, trouble tic chronique, pointes-ondes continues du sommeil, secousses bénignes du nourrisson, maladies extrapyramidales) reposent également uniquement sur la prédiction du modèle ou sur de la littérature indirecte (niveaux L4 à L5) et sont toutes en statut Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

