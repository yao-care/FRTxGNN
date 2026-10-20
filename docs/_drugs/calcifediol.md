---
layout: default
title: Calcifediol
parent: Prédiction du modèle uniquement (L5)
nav_order: 129
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Calcifediol : nouvelle indication prédite, Carence en vitamine D (terme obsolète) (niveau de preuve L5). Indication d'origine : Texte d'indication non renseigné dans les AMM. Selon le graphe de con…"
monitor_inn: "calcifediol"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "hereditary hypophosphatemic rickets", "vitamin D-dependent rickets"]
---

# Calcifediol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

# Calcifédiol : Des maladies osseuses et du métabolisme phosphocalcique à la carence en vitamine D (terme obsolète)

## Résumé en Une Phrase

Le calcifédiol (25-hydroxyvitamine D3) est un métabolite de la vitamine D, initialement utilisé dans des maladies du métabolisme phosphocalcique et osseux (rachitisme, ostéomalacie, hypophosphatémie, ostéodystrophie rénale).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **carence en vitamine D** (terme classé comme obsolète dans l'ontologie), avec un score de 99,99 %.
À ce jour, **aucun essai clinique** et **aucune publication** ne soutiennent directement cette prédiction : elle repose uniquement sur le modèle (niveau L5).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Texte d'indication non renseigné dans les AMM. Selon le graphe de connaissances : hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore, hypophosphatémie, rachitisme, ostéomalacie, ostéodystrophie rénale |
| Nouvelle Indication Prédite | Carence en vitamine D (terme obsolète) |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 4 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le calcifédiol est le précurseur circulant direct du calcitriol (forme active de la vitamine D) et le biomarqueur standard du statut en vitamine D. Son efficacité dans le rachitisme et l'ostéomalacie, deux maladies liées à un déficit en vitamine D, est connue.

La carence en vitamine D est biologiquement très proche de ces indications d'origine : un apport en 25-hydroxyvitamine D corrige directement le déficit. Le score élevé du modèle reflète probablement ce lien étroit.

Deux réserves s'imposent. Le terme de maladie utilisé est signalé comme obsolète et doit être rattaché au terme actuel de carence en vitamine D avant toute analyse. De plus, aucune étude n'est disponible dans les données compilées pour ce rapport.

### Autres indications prédites (pour information)

| Indication prédite | Score TxGNN | Niveau de preuve | Commentaire |
|------|------|------|------|
| Acidose tubulaire rénale | 99,86 % | L5 | Pas de mécanisme direct ; rôle possible de traitement de soutien des complications osseuses |
| Rachitisme hypophosphatémique héréditaire | 99,76 % | L4 | Le traitement de référence repose sur phosphate et vitamine D active ; rôle du calcifédiol au mieux complémentaire |
| Rachitisme vitamino-dépendant | 99,18 % | L4 | Mécanisme direct pour le type 1B (déficit en 25-hydroxylase, CYP2R1) : le calcifédiol contourne le blocage enzymatique. Question de recherche à approfondir |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'indication principale (carence en vitamine D). Pour les indications prédites secondaires, deux publications indirectes ont été identifiées :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Revue | Nutrients | Revue des types de rachitisme et de leur traitement par la vitamine D et ses analogues (rachitisme hypophosphatémique héréditaire) |
| [28548312](https://pubmed.ncbi.nlm.nih.gov/28548312/) | 2017 | Rapport de cas / Revue | J Bone Miner Res | Rachitisme vitamino-dépendant de type 1B (déficit en 25-hydroxylase) : sept patients de deux familles, affection rare ou sous-diagnostiquée |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67317463 | CALCIFEDIOL DESMA 15 mg/100 ml | Solution buvable en gouttes | Non renseignée (AMM annulée) |
| 68280975 | DEDROGYL 15 mg/100 ml | Solution buvable en gouttes | Non renseignée (AMM annulée) |
| 67563301 | LUZADEL 266 microgrammes | Capsule molle | Non renseignée (AMM annulée) |
| 60748767 | CALCIFEDIOL GERDA 15 mg/100 mL | Solution buvable en gouttes | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : maladie rénale, pyo-uretère, sarcoïdose, hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore, lithiase rénale (dont la forme liée à SLC26A1), néphropathie aiguë urique, hyperphosphatémie, hypervitaminose, artériosclérose oblitérante.
- **Interactions médicamenteuses** : 57 interactions recensées. Principales interactions de niveau majeur :
  - cholécalciférol, calcitriol (cumul d'effets vitaminiques D, risque d'hypercalcémie) ;
  - burosumab.
- Interactions de niveau modéré (extrait) : diurétiques thiazidiques (hydrochlorothiazide, bendrofluméthiazide, chlorothiazide, chlortalidone), anticonvulsivants et barbituriques (fosphénytoïne, carbamazépine, amobarbital, butalbital, butabarbital), hydroxyde d'aluminium, résines chélatrices (cholestyramine, colesevelam, colestipol), digitoxine, analogues topiques de la vitamine D (calcipotriol, calcitriol).

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La plausibilité biologique est forte, mais la prédiction n'est soutenue par aucun essai ni aucune publication directe (niveau L5). Les AMM françaises sont toutes annulées et les données de sécurité officielles manquent, ce qui bloque le passage à l'étape de criblage de sécurité.
- Parmi les pistes secondaires, le rachitisme vitamino-dépendant de type 1B (déficit en CYP2R1) est la plus cohérente mécanistiquement et mérite une question de recherche dédiée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde, contre-indications) auprès de l'ANSM.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Rattacher le terme obsolète au terme actuel de carence en vitamine D, puis réaliser une recherche bibliographique ciblée (essais, revues systématiques).
- Mener une revue ciblée de l'usage du calcifédiol dans le déficit en CYP2R1.
- Clarifier la disponibilité réelle du produit en France (AMM annulées) et les voies d'administration compatibles.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

