---
layout: default
title: Iodixanol
parent: Prédiction du modèle uniquement (L5)
nav_order: 406
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Iodixanol : nouvelle indication prédite, Susceptibilité à l'arthrose (niveau de preuve L5). Indication d'origine : Non renseignée dans les données compilées (produit de contraste iodé)"
---

# Iodixanol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Iodixanol : D'un produit de contraste radiologique à la susceptibilité à l'arthrose

## Resume en Une Phrase

Iodixanol est un produit de contraste iodé utilisé en imagerie radiologique (spécialité VISIPAQUE).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **susceptibilité à l'arthrose**, mais aucun essai clinique n'est enregistré et aucune publication ne soutient un effet thérapeutique : la prédiction repose uniquement sur le modèle.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données compilées (produit de contraste iodé) |
| Nouvelle Indication Predite | Susceptibilité à l'arthrose |
| Score de Prediction TxGNN | 99,16 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Uniquement des AMM annulées |
| Nombre d'AMM | 2 |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Iodixanol est un produit de contraste radiographique iodé : son rôle est de rendre opaques aux rayons X les structures où il est administré, et non d'agir sur une voie biologique de la maladie.

La prédiction est donc peu plausible sur le plan mécanistique. La « susceptibilité » à l'arthrose est un concept de risque génétique et non un état pathologique traitable, et iodixanol n'a aucune action pharmacologique connue sur ces déterminants. Le score élevé (99,16 %) est probablement un artefact du graphe de connaissances, qui associe le produit et la maladie parce qu'ils apparaissent ensemble dans la recherche en imagerie.

Les deux autres prédictions les mieux classées sont l'**arthrose** (99,07 %) et la **polyarthrite rhumatoïde** (99,00 %). Elles ne sont pas non plus étayées par des preuves thérapeutiques (voir ci-dessous).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

Aucune publication n'est rattachée à la susceptibilité à l'arthrose. Les publications ci-dessous concernent la prédiction voisine « arthrose » et portent sur l'usage d'iodixanol comme agent d'imagerie, non comme traitement.

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Méthodologie d'imagerie | Annals of Biomedical Engineering | Imagerie de la fonction du cartilage par diffusion de nanoparticules en tomodensitométrie, avec modélisation par éléments finis |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Modélisation computationnelle | Journal of Biomechanics | Transport de solutés neutres à travers l'interface os-cartilage, modèle par éléments finis |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Méthodologie d'imagerie | Annals of Biomedical Engineering | Agent de contraste double en scanner à comptage de photons pour évaluer la santé du cartilage |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Étude expérimentale | Journal of Biomechanics | Perméabilité de l'interface ostéochondrale mesurée avec iodixanol comme agent de contraste au scanner |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | Étude in vitro | Journal of Experimental Orthopaedics | Les produits de contraste iodés n'altèrent pas la fonction du plasma riche en plaquettes à un stade précoce |

Pour la polyarthrite rhumatoïde, la seule publication retrouvée ([36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/), 2022, *Cureus*) est un rapport de cas de désensibilisation à un autre produit de contraste (iohexol) et ne concerne pas un traitement par iodixanol.

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 60960777 | VISIPAQUE 270 mg d'I/mL, solution injectable (GE Healthcare) | Solution injectable | Non renseignée (AMM annulée) |
| 60567418 | VISIPAQUE 320 mg d'I/mL, solution injectable (GE Healthcare) | Solution injectable | Non renseignée (AMM annulée) |

## Considerations de Securite

- **Interactions Medicamenteuses** : 100 interactions ont été recensées. Parmi les principales, de niveau **majeur** :
  - metformine ;
  - amphotéricine B (formes conventionnelle, complexe lipidique, sulfate de cholestéryle et liposomale) ;
  - mésalazine, balsalazide, olsalazine et sulfasalazine ;
  - vancomycine ;
  - aminosides (kanamycine, néomycine, streptomycine) ;
  - polymyxine B.

  Le mannitol est de niveau **modéré**. Plusieurs autres interactions (famotidine, acide acétylsalicylique, morphine, oméprazole, prednisone) sont de niveau inconnu.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- Aucun essai clinique n'est enregistré et la littérature ne montre aucun bénéfice thérapeutique. Elle décrit seulement l'usage d'iodixanol comme agent d'imagerie. La prédiction (niveau L5) est très probablement un artefact du graphe de connaissances, d'autant que la « susceptibilité » n'est pas une maladie traitable.
- Les deux AMM françaises sont annulées, et les données de sécurité de la notice ne sont pas disponibles.

**Pour avancer, les elements suivants sont necessaires :**
- Les mises en garde et contre-indications de la notice ANSM (étape de sécurité bloquante)
- Les données sur le mécanisme d'action, afin d'analyser un éventuel lien mécanistique
- Des études précliniques ou cliniques évaluant un effet thérapeutique réel d'iodixanol dans l'arthrose, qui n'existent pas à ce jour
- Une vérification de la compatibilité des voies d'administration (par exemple intra-articulaire), non évaluée à ce stade
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

