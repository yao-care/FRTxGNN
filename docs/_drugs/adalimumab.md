---
layout: default
title: Adalimumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 25
evidence_level: L5
indication_count: 3
monitor_inn: "ADALIMUMAB"
predicted_indications: ["hypermobility of coccyx", "Kummell disease", "vertebral disease"]
last_modified_at: 2026-10-28
description: "Adalimumab : nouvelle indication prédite, Hypermobilité du coccyx (hypermobility of coccyx) (niveau de preuve L5). En France, AMM dans la BDPM : au moins 20"
---

# Adalimumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Adalimumab : anticorps monoclonal anti-TNF alpha → Hypermobilité du coccyx (hypermobility of coccyx)
{: .text-alpha }

## Résumé en Une Phrase

Adalimumab est un anticorps monoclonal dirigé contre le TNF alpha, une molécule centrale de l'inflammation.
Le modèle TxGNN prédit qu'il pourrait être utile dans l'**hypermobilité du coccyx (hypermobility of coccyx)**.
Aucun essai clinique ni aucune publication n'a été trouvé pour cette indication : il s'agit uniquement d'une prédiction informatique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hypermobilité du coccyx (hypermobility of coccyx) |
| Score de Prédiction TxGNN | 0.9977 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Adalimumab (traduction non officielle) : « Les produits à base d'adalimumab se lient spécifiquement au TNF-alpha et bloquent son interaction avec les récepteurs du TNF p55 et p75 de la surface cellulaire. Les produits à base d'adalimumab lysent également in vitro les cellules exprimant le TNF à leur surface en présence du complément. » Texte original en anglais : "Adalimumab products bind specifically to TNF-alpha and block its interaction with the p55 and p75 cell surface TNF receptors. Adalimumab products also lyse surface TNF expressing cells in vitro in the presence of complement." ([DailyMed: Simlandi (adalimumab-ryvk) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12f609c9-2088-bb05-e063-6394a90a9ecc), version du 2026-11-11 ; consulté le 2026-11-19). D'après les connaissances générales, l'adalimumab bloque le TNF alpha, ce qui réduit l'inflammation médiée par cette cytokine.

Le lien avec l'hypermobilité du coccyx reste faible. Cette affection est surtout mécanique ou traumatique, et on ne lui connaît pas de mécanisme inflammatoire clairement dépendant du TNF. Le score élevé de 0.9977 reflète probablement une proximité avec des pathologies inflammatoires axiales dans les données du modèle, et non une preuve biologique ou clinique.

Cette prédiction doit donc être considérée comme une hypothèse à vérifier, et non comme une piste thérapeutique étayée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

L'adalimumab est commercialisé en France sous forme de solution injectable (seringue préremplie ou stylo prérempli), sous plusieurs noms de marque. Cette liste est probablement partielle.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 68619482 | AMGEVITA 20 mg, seringue préremplie (0,2 mL) | Solution injectable |
| 62042376 | HULIO 40 mg, seringue préremplie | Solution injectable |
| 61192750 | IMRALDI 40 mg, seringue préremplie | Solution injectable |
| 65075488 | YUFLYMA 20 mg, seringue préremplie | Solution injectable |
| 69835440 | HUMIRA 80 mg, seringue préremplie | Solution injectable |

## Considérations de Sécurité

Les mises en garde et les contre-indications ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

**Interactions médicamenteuses** : 100 interactions sont recensées, dont voici les principales.

- **Majeures** :
  - Corticoïdes : bétaméthasone, budésonide, dexaméthasone, hydrocortisone, prednisolone, prednisone, triamcinolone (y compris ophtalmique).
  - Autres : déférisprone (déférasirox non concerné), ibritumomab tiuxétan, iobenguane (I-131), tositumomab et tositumomab (I-131).
- **Modérées** : métronidazole, tinidazole, rosuvastatine, simvastatine.
- **Mineures** : sels de zinc (acétate, gluconate, sulfate).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (0.9977), sans essai clinique ni publication. Le mécanisme proposé est peu plausible pour une affection essentiellement mécanique ou traumatique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action
- Revue de la littérature montrant une composante inflammatoire dépendante du TNF dans l'hypermobilité du coccyx
- Données de sécurité issues de la notice (mises en garde et contre-indications)
- Étude préclinique ou observationnelle préalable avant tout essai clinique

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Simlandi (adalimumab-ryvk) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12f609c9-2088-bb05-e063-6394a90a9ecc) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

