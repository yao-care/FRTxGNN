---
layout: default
title: Iodixanol
parent: Prédiction du modèle uniquement (L5)
nav_order: 406
evidence_level: L5
indication_count: 2
monitor_inn: "IODIXANOL"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis"]
last_modified_at: 2026-10-28
description: "Iodixanol : nouvelle indication prédite, Arthrose (niveau de preuve L5). Indication d'origine : Non renseignée dans les textes d'AMM compilés"
---

# Iodixanol
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

## Iodixanol : D'un produit de contraste radiographique à l'arthrose (prédiction du modèle)
{: .text-alpha }

## Résumé en Une Phrase

L'iodixanol est un produit de contraste iodé, non ionique et iso-osmolaire, utilisé en imagerie radiographique (spécialité VISIPAQUE).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**arthrose**, mais **aucun essai clinique** ne soutient cette piste et les 5 publications retrouvées décrivent uniquement un usage en imagerie, sans effet thérapeutique démontré.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les textes d'AMM compilés |
| Nouvelle Indication Prédite | Arthrose |
| Score de Prédiction TxGNN | 0,9907 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. L'iodixanol est un produit de contraste iodé non ionique et iso-osmolaire, utilisé pour visualiser des structures en imagerie radiographique. Il n'a pas d'action connue modifiant l'évolution d'une maladie.

La littérature retrouvée le montre uniquement comme outil d'imagerie : scanner du cartilage avec agents de contraste, modélisation du transport de solutés à travers l'interface os-cartilage, et vérification in vitro de sa compatibilité avec le plasma riche en plaquettes. Aucune de ces études n'évalue un effet thérapeutique sur l'arthrose.

Le score élevé du modèle (0,9907) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique ni un effet pharmacologique sur la maladie articulaire. La prédiction est donc peu étayée sur le plan mécanistique.

Pour information, le modèle prédit aussi la **polyarthrite rhumatoïde** (score de 0,9900), sans lien mécanistique identifié et sans étude portant sur l'iodixanol : la seule publication retrouvée est un cas de désensibilisation à un autre produit de contraste (iohexol).

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

Aucune de ces publications n'évalue l'iodixanol comme traitement de l'arthrose : toutes concernent l'imagerie ou des modèles expérimentaux.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Méthode d'imagerie/diagnostic | Annals of Biomedical Engineering | Imagerie de la fonction du cartilage par diffusion de nanoparticules en scanner, associée à une modélisation par éléments finis |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Modèle computationnel | Journal of Biomechanics | Modélisation du transport de solutés neutres à travers l'interface os-cartilage (échantillons humains et équins) |
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Méthode d'imagerie/diagnostic | Annals of Biomedical Engineering | Agent de contraste double en scanner à comptage de photons pour évaluer la santé du cartilage articulaire |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Modèle computationnel | Journal of Biomechanics | Utilisation de l'iodixanol comme agent de contraste diffusant pour étudier la perméabilité de l'interface ostéochondrale |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | Étude in vitro | Journal of Experimental Orthopaedics | Les produits de contraste iodés n'altèrent pas la fonction du plasma riche en plaquettes à un stade précoce in vitro |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60960777 | VISIPAQUE 270 mg d'I/mL, solution injectable | Solution injectable | Non renseignée |
| 60567418 | VISIPAQUE 320 mg d'I/mL, solution injectable | Solution injectable | Non renseignée |

Les deux AMM (GE Healthcare) sont valides et concernent le médicament à substance unique.

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions sont recensées. Parmi les principales, de niveau majeur :
  - Metformine
  - Amphotéricine B (y compris les formes lipidique, liposomale et sulfate de cholestéryle)
  - Mésalazine, balsalazide, olsalazine et sulfasalazine
  - Vancomycine
  - Aminosides : kanamycine, néomycine, streptomycine
  - Polymyxine B

  L'interaction avec le mannitol est de niveau modéré. D'autres (famotidine, acide acétylsalicylique, morphine, oméprazole, prednisone) sont de niveau non précisé.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique ni étude ne teste l'iodixanol comme traitement de l'arthrose ; les publications ne concernent que l'imagerie. Le niveau de preuve est donc L5, et le score élevé du modèle semble dû à une association liée à l'imagerie plutôt qu'à un effet pharmacologique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des données sur le mécanisme d'action, afin d'établir un éventuel lien avec l'arthrose
- Des études précliniques démontrant un effet thérapeutique articulaire
- Les mises en garde et contre-indications de la notice, pour l'évaluation de sécurité
- Les indications approuvées figurant dans les AMM
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

