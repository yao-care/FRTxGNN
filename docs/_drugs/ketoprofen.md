---
layout: default
title: Ketoprofen
parent: Prédiction du modèle uniquement (L5)
nav_order: 424
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ketoprofen : nouvelle indication prédite, Dysplasie acromésomélique de type Hunter-Thompson (1re du classement… (niveau de preuve L5). Indication d'origine : Polyarthrite rhumatoïde, arthrose, arthro…"
---

# Ketoprofen
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

# Kétoprofène : De l'Arthrose et de la Polyarthrite Rhumatoïde à la Spondylarthropathie

## Résumé en Une Phrase

Le kétoprofène est un anti-inflammatoire non stéroïdien (AINS), initialement utilisé pour traiter la polyarthrite rhumatoïde, l'arthrose et les arthropathies.
Le modèle TxGNN prédit des scores très élevés pour plusieurs maladies rares. Parmi elles, la **spondylarthropathie (susceptibilité)** est la piste biologiquement la plus plausible.
Aucun essai clinique ni aucune publication ne soutient actuellement cette direction : il s'agit d'une **prédiction de modèle uniquement**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde, arthrose, arthropathie (le texte d'indication des AMM n'est pas renseigné ; ces indications proviennent du graphe de connaissances) |
| Nouvelle Indication Prédite | Dysplasie acromésomélique de type Hunter-Thompson (1re du classement TxGNN) ; spondylarthropathie retenue comme piste la plus plausible (8e) |
| Score de Prédiction TxGNN | 99,98 % (dysplasie acromésomélique de type Hunter-Thompson) ; 99,86 % (spondylarthropathie) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold (la spondylarthropathie est à considérer comme question de recherche) |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, le kétoprofène est un inhibiteur non sélectif des cyclooxygénases (COX), à l'origine d'une action anti-inflammatoire et antalgique. Son efficacité symptomatique dans les affections articulaires inflammatoires et dégénératives est établie.

**Prédiction classée première (dysplasie acromésomélique de type Hunter-Thompson)** : cette maladie est un trouble du développement squelettique dû à une perte de fonction de CDMP1/GDF5. Aucun lien plausible entre l'inhibition des COX et la correction de ce défaut génétique n'est identifiable. Au mieux, un AINS pourrait soulager la douleur, sans modifier l'évolution de la maladie. Il en va de même pour la plupart des autres prédictions de tête (brachyolmie, syndrome brachyolmie-amélogenèse imparfaite, myosclérose, syndrome colobomateux microphtalmie-dysplasie rhizomélique, syndrome brachydactylie-syndactylie), pour lesquelles le score reflète probablement une proximité dans le graphe avec les nœuds « dysplasie squelettique » et « arthropathie » plutôt qu'une logique biologique. Le syndrome WHIM (mutation gain de fonction de CXCR4) relève d'une voie que l'inhibition des COX n'adresse pas.

**Pistes les plus plausibles** :
- **Spondylarthropathie (susceptibilité)** : les AINS sont un traitement de première intention de la spondylarthrite axiale et de la spondylarthrite ankylosante. Cette piste est cohérente avec les indications inflammatoires d'origine du kétoprofène, mais reste une hypothèse fondée sur la connaissance de classe (AINS).
- **Arthrite juvénile par déficit en LACC1** : forme monogénique d'arthrite juvénile. Les AINS sont utilisés en traitement symptomatique de première ligne, mais ces formes nécessitent en général un traitement de fond ou une biothérapie ; l'AINS serait au mieux adjuvant.
- **Pseudoachondroplasie** : lien faible et indirect, via l'arthropathie précoce symptomatique (douleurs articulaires). Aucune modification de la maladie n'est attendue.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées. Le texte d'indication approuvée n'est pas renseigné pour ces AMM. Les 5 premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 64552068 | KETOPROFENE CRISTERS LP 100 mg | Comprimé sécable à libération prolongée | Annulée |
| 67899241 | PROFEMIGR 150 mg | Comprimé sécable | Annulée |
| 62473063 | KETOPROFENE SANDOZ LP 100 mg | Comprimé sécable à libération prolongée | Annulée |
| 69159834 | KETUM 100 mg | Comprimé pelliculé | Annulée |
| 66771790 | PROFENID 100 mg | Comprimé pelliculé | Annulée |

Le kétoprofène existe aussi sous forme injectable, suppositoire, gélule, solution pour perfusion et gel topique (AMM annulées).

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension et troubles hypertensifs, insuffisance hépatique, maladie rénale, ulcère gastroduodénal (y compris actif), troubles de la coagulation, infarctus du myocarde, thrombose coronaire, maladie cardiovasculaire et cardiopathie, hémoglobinopathie, pyouretère.
- **Interactions médicamenteuses** : 226 interactions recensées. Parmi les exemples relevés :
  - Niveau modéré : acide acétylsalicylique, corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide), metformine, glimépiride, chlorpropamide, mésalazine, balsalazide, naltrexone, citrate et bicarbonate de potassium, acide picosulfurique, polyéthylène glycol.
  - Niveau mineur : famotidine, ranitidine, cimétidine, linaclotide.

Les mises en garde et contre-indications issues de la notice n'ont pas pu être récupérées : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Toutes les prédictions reposent uniquement sur le modèle (niveau L5), sans essai ni publication. Pour la plupart d'entre elles, aucun mécanisme plausible n'est identifié.
- Les AMM françaises sont toutes annulées, ce qui limite la pertinence pratique. La spondylarthropathie et l'arthrite juvénile liée à LACC1 sont à traiter comme des questions de recherche.

**Pour avancer, les éléments suivants sont nécessaires :**
- Recherche ciblée d'essais et de publications sur le kétoprofène dans la spondylarthrite (et l'arthrite juvénile) pouvant faire évoluer le niveau de preuve
- Données détaillées sur le mécanisme d'action
- Mises en garde et contre-indications issues de la notice (étape bloquante pour le criblage de sécurité)
- Clarification du statut réglementaire, toutes les AMM étant annulées, et de la voie d'administration requise
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

