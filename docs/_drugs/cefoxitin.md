---
layout: default
title: Cefoxitin
parent: Prédiction du modèle uniquement (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Cefoxitin
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

# Céfoxitine : Des infections bactériennes à l'otite moyenne infectieuse

## Résumé en Une Phrase

La céfoxitine est une céphamycine injectable (proche des céphalosporines de 2e génération), initialement utilisée pour traiter des infections bactériennes (streptococciques, staphylococciques, à *Escherichia coli*, pneumonies bactériennes, péritonites, gonorrhée, etc.).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**otite moyenne infectieuse**,
mais **aucun essai clinique** et **une seule publication** (une revue sur le SARM, sans test clinique de la céfoxitine) soutiennent actuellement cette direction : la prédiction repose donc uniquement sur le modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infections bactériennes (streptococciques, staphylococciques, à *E. coli*, pneumonie bactérienne, péritonite, gonorrhée...) d'après le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné |
| Nouvelle Indication Predite | Otite moyenne infectieuse |
| Score de Prediction TxGNN | 99,30 % |
| Niveau de Preuve | L5 |
| Statut de Marche en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Decision Recommandee | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des informations connues, la céfoxitine est une céphamycine qui inhibe la synthèse de la paroi bactérienne et résiste à de nombreuses bêta-lactamases. Son spectre couvre notamment *S. aureus*, *E. coli* et des anaérobies, germes que l'on peut retrouver dans l'otite moyenne.

L'indication originale (infections bactériennes variées) et l'otite moyenne infectieuse partagent donc une logique antibactérienne. Mécanistiquement, l'application est plausible, mais cette plausibilité reste théorique.

Il faut rester prudent : la seule publication liée est une revue sur le SARM qui ne teste pas la céfoxitine en traitement. La céfoxitine y est surtout un marqueur de laboratoire pour détecter le SARM, et non un traitement. Le score élevé du modèle reste une simple prédiction.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33061472](https://pubmed.ncbi.nlm.nih.gov/33061472/) | 2020 | Revue | Infection and Drug Resistance | Revue « One Health » sur le SARM (épidémiologie, virulence, résistance, impact zoonotique) citant l'otite moyenne parmi les infections humaines ; aucun test clinique de la céfoxitine |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60329598 | CEFOXITINE SUBSTIPHARM 1 g | Poudre pour solution injectable | Non renseignée (AMM annulée) |
| 69084488 | CEFOXITINE PANPHARMA 1 g (IV) | Poudre pour solution injectable | Non renseignée (AMM annulée) |
| 60580134 | CEFOXITINE SUBSTIPHARM 2 g | Poudre pour solution injectable | Non renseignée (AMM annulée) |
| 67355243 | CEFOXITINE PANPHARMA 2 g (IV) | Poudre pour solution injectable | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (hors texte de notice) : maladie rénale, pyo-uretère, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, colite.
- **Interactions médicamenteuses** : 35 interactions recensées. Principales de niveau modéré : kanamycine, néomycine, streptomycine (aminosides), acide picosulfurique, dicoumarol. Héparine : niveau mineur. De nombreuses autres (morphine, oméprazole, vancomycine, métronidazole, clarithromycine, etc.) sont de niveau inconnu.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni donnée de traitement de l'otite moyenne. En outre, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank)
- Notice officielle de l'ANSM (mises en garde et contre-indications), actuellement manquante et bloquante pour le criblage de sécurité
- Études cliniques ou microbiologiques évaluant la céfoxitine comme traitement de l'otite moyenne
- Prise en compte de la résistance naturelle de *Pseudomonas* à la céfoxitine, pathogène fréquent des otites chroniques

**Note sur les autres indications prédites :** l'infection urinaire (L3, un essai de phase 4 terminé avec 6 patients, un modèle murin et des études anciennes) et l'urétrite gonococcique (L3, études de 1979-1983) relèvent déjà du périmètre des indications d'origine, sans grand intérêt moderne, la ceftriaxone étant privilégiée. Les prédictions ureaplasma et toxocarose sont mécanistiquement peu plausibles.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

