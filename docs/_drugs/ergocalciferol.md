---
layout: default
title: Ergocalciferol
parent: Prédiction du modèle uniquement (L5)
nav_order: 294
evidence_level: L5
indication_count: 6
monitor_inn: "ergocalciferol"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis", "craniofacial conodysplasia", "hypophosphatemia (disease)", "renal osteodystrophy", "calcium-alkali syndrome"]
last_modified_at: 2026-10-23
description: "Ergocalciferol : nouvelle indication prédite, Dysplasie acromésomélique de type Campailla-Martinelli (acromesomelic dysplasia, Campailla Martinelli type) (niveau de preuve L5). Indication d'origine :…"
---

# Ergocalciferol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Ergocalciferol: Dysplasie acromésomélique de type Campailla-Martinelli (acromesomelic dysplasia, Campailla Martinelli type)
{: .text-alpha }

## Résumé en Une Phrase

L'ergocalciferol (vitamine D2) est utilisé dans les carences en vitamine D et les maladies osseuses associées (rachitisme, ostéomalacie, ostéoporose). Le modèle TxGNN prédit qu'il pourrait être efficace dans la **dysplasie acromésomélique de type Campailla-Martinelli**, une maladie osseuse génétique rare. **Aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Dysplasie acromésomélique de type Campailla-Martinelli (acromesomelic dysplasia, Campailla Martinelli type) |
| Score de Prédiction TxGNN | 0.9983 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 7 sur 7) |
| Nombre d'AMM | 7 (valides : 7) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, l'ergocalciferol est une forme de vitamine D. Il favorise l'absorption intestinale du calcium et du phosphate et intervient dans la minéralisation osseuse.

La dysplasie acromésomélique de type Campailla-Martinelli est une dysplasie squelettique génétique rare. Aucun lien mécanistique n'a été identifié avec l'ergocalciferol. Un défaut génétique de la signalisation de la croissance du squelette a peu de chances d'être corrigé par une supplémentation en vitamine D2. Le score élevé du modèle semble provenir de la proximité, dans le réseau de connaissances, avec d'autres maladies osseuses, plutôt que d'un mécanisme défini.

La prédiction doit donc être considérée comme une hypothèse purement computationnelle, sans fondement biologique ou clinique démontré à ce stade.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

L'ergocalciferol est commercialisé en France. Les textes d'indication approuvée ne sont pas disponibles dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69719090 | STEROGYL 15 "H" 600 000 UI/1,5 ml | Solution injectable (IM) | Texte non disponible |
| 62457493 | STEROGYL 2 000 000 UI/100 ml | Solution buvable en gouttes | Texte non disponible |
| 69443489 | STEROGYL 15 "A" 600 000 UI/1,5 ml | Solution buvable en ampoule | Texte non disponible |

Les quatre autres AMM concernent VITALIPIDE ADULTES, VITALIPIDE ENFANTS, UVESTEROL VITAMINE A.D.E.C. et HYDROSOL POLYVITAMINE. D'après leurs noms, ce sont des préparations polyvitaminiques. Elles ne sont pas détaillées ici et ne servent pas à décrire l'autorisation de l'ergocalciferol seul.

## Considérations de Sécurité

Les mises en garde et contre-indications issues des notices ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

- **Relations de contre-indication du graphe de connaissances** (elles ne proviennent pas du texte de la notice) : hypercalcémie, néphrocalcinose, hyperparathyroïdie, sarcoïdose, maladie rénale, maladie hépatique, maladie de la vésicule biliaire, hypertension, fibrillation auriculaire, diabète et acidocétose diabétique, hyperoxalurie primaire, hémochromatose et autres troubles du métabolisme du fer, maladie de Wilson, hyperlipidémie, cancer du sein et cancer de la prostate, notamment.
- **Interactions médicamenteuses** : 55 interactions sont répertoriées.
  - Interactions majeures : autres dérivés de la vitamine D (cholécalciférol, calcifédiol, calcitriol, doxercalciférol), avec un risque de cumul d'effets et d'hypercalcémie.
  - Interactions modérées, notamment : diurétiques thiazidiques (hydrochlorothiazide, chlorothiazide, chlortalidone), barbituriques (amobarbital, butalbital), carbamazépine, rifabutine, digoxine, résines chélatrices (cholestyramine, colestipol, colesevelam), sévélamer et oxyde de magnésium.
  - Interaction mineure : cimétidine.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique ni aucune publication n'étudie l'ergocalciferol dans la dysplasie acromésomélique de type Campailla-Martinelli, et aucun mécanisme plausible n'a été identifié. Le score TxGNN élevé (0,9983) ne suffit pas à justifier une avancée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action de l'ergocalciferol.
- Données de la notice (mises en garde, contre-indications) pour un criblage de sécurité.
- Hypothèse biologique reliant la vitamine D2 à la voie génétique de cette dysplasie, avec des données précliniques.

**Remarque :** parmi les autres prédictions du modèle, l'ostéodystrophie rénale est la mieux étayée. Elle s'appuie sur un essai de phase 4 (NCT01799317, statut inconnu) et sur des études comparatives, dont un essai randomisé ergocalciferol versus calcitriol dans la maladie rénale chronique. Cette piste mérite une évaluation distincte.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

