---
layout: default
title: Vitamin A
parent: Prédiction du modèle uniquement (L5)
nav_order: 818
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vitamin A : nouvelle indication prédite, Déficit congénital en prothrombine (niveau de preuve L5). Indication d'origine : Carence en vitamine A / carence vitaminique"
monitor_inn: "vitamin a"
predicted_indications: ["congenital prothrombin deficiency", "biotin metabolic disease", "non-syndromic esophageal malformation", "injury", "cell proliferation disorder", "perinatal disease", "florid cemento-osseous dysplasia", "segmental odontomaxillary dysplasia", "disease by subcellular system affected", "radiation or chemically induced disorder"]
---

# Vitamin A
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Vitamine A : De la carence en vitamine A au déficit congénital en prothrombine
{: .text-alpha }

## Résumé en Une Phrase

La vitamine A (SOLACY PÉDIATRIQUE, comprimé pour suspension buvable) est utilisée à l'origine pour traiter la carence en vitamine A et les carences vitaminiques.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **déficit congénital en prothrombine**, mais **aucun essai clinique ni aucune publication** ne soutient cette prédiction à ce jour.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carence en vitamine A / carence vitaminique (d'après le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Déficit congénital en prothrombine |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. La vitamine A est un nutriment essentiel, dont l'efficacité dans la correction des carences en vitamine A est établie.

Pour le déficit congénital en prothrombine, la prédiction paraît **peu plausible sur le plan mécanistique**. La synthèse de la prothrombine dépend de la gamma-carboxylation vitamine K-dépendante, et non de la vitamine A. Cette maladie est un défaut génétique du gène *F2*. Le score très élevé du modèle reflète probablement des associations « carence vitaminique » dans le graphe de connaissances, plutôt qu'un lien thérapeutique réel. Ce score doit donc être interprété avec une grande prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60238376 | SOLACY PEDIATRIQUE | Comprimé pour suspension buvable | Non renseignée |

Cette AMM (laboratoire GRIMBERG, spécialité à substance unique) est **annulée**. Aucune AMM valide n'existe actuellement pour ce médicament dans les données compilées.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : maladie rénale, maladie hépatique, maladie de la vésicule biliaire, ulcère gastroduodénal, sarcoïdose, hypercalcémie, néphrocalcinose, néphrolithiase, hyperphosphatémie, drépanocytose, hyperoxalurie primitive, hémochromatose héréditaire, hémosidérose, maladie de Wilson, néphropathie urique aiguë, rectocolite hémorragique, maladies inflammatoires chroniques de l'intestin, anémie hémolytique, hypervitaminose, artériopathie oblitérante, gastro-entérite, entre autres.
- **Interactions médicamenteuses** : 68 interactions recensées. Les interactions de niveau **majeur** les plus notables concernent :
  - les rétinoïdes (isotrétinoïne, acitrétine, trétinoïne) ;
  - les cyclines (doxycycline, tétracycline, minocycline, oxytétracycline, déméclocycline, oméga­cycline, éravacycline, sarécycline).

  Des interactions de niveau modéré existent avec la bexarotène, la colestyramine, le colesevelam, le colestipol, le sévélamer et le sélpercatinib. L'interaction avec l'orlistat est mineure.
- **Sécurité aux doses élevées** (littérature disponible pour d'autres indications) : risque de fractures osseuses, hépatotoxicité de l'hypervitaminose A, et effet tératogène en cas d'excès.

Veuillez consulter la notice pour les mises en garde officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication, et le mécanisme biologique invoqué est incompatible avec la physiopathologie du déficit en prothrombine.
- Le médicament ne dispose plus d'AMM valide en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Une justification mécanistique plausible, avec des données sur le mécanisme d'action de la vitamine A.
- Une revue de la notice de l'ANSM (mises en garde et contre-indications), actuellement manquante.
- Une réévaluation du statut réglementaire, puisque l'AMM est annulée.

**Remarque :** parmi les autres prédictions du modèle, la **maladie périnatale** (score de 99,63 %) est de loin la mieux étayée. Elle repose sur plusieurs méta-analyses Cochrane de la supplémentation en vitamine A chez les nourrissons de très faible poids de naissance, avec un bénéfice modeste sur la dysplasie bronchopulmonaire. Cette piste mériterait d'être évaluée en priorité, avec des garde-fous (voie d'administration, dosage, sécurité). L'indication « blessure » dispose également d'un essai randomisé de phase 1/2 (NCT01203488, 807 nourrissons), mais ses résultats portent sur la morbidité néonatale plutôt que sur les blessures en général.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

