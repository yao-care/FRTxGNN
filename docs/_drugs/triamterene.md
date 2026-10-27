---
layout: default
title: Triamterene
parent: Prédiction du modèle uniquement (L5)
nav_order: 787
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Triamterene : nouvelle indication prédite, Maladie rénale hypertensive maligne (niveau de preuve L5). Indication d'origine : Hypertension artérielle…"
monitor_inn: "triamterene"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
---

# Triamterene
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

## Triamtérène : De l'hypertension artérielle à la maladie rénale hypertensive maligne
{: .text-alpha }

## Résumé en Une Phrase

Le triamtérène est un diurétique épargneur de potassium, initialement utilisé pour traiter l'hypertension artérielle et l'insuffisance cardiaque congestive.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie rénale hypertensive maligne**,
mais **aucun essai clinique** ni **aucune publication** directement pertinente ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle, insuffisance cardiaque congestive (le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Maladie rénale hypertensive maligne |
| Score de Prédiction TxGNN | 99,89 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, le triamtérène est un diurétique épargneur de potassium qui bloque le canal sodique épithélial (ENaC) du néphron distal. Il réduit ainsi la pression artérielle par perte de sodium et de volume.

Ce mécanisme est proche de l'indication d'origine (hypertension), ce qui explique le score élevé du modèle pour la maladie rénale hypertensive. Le score reflète sans doute surtout la proximité dans le graphe de connaissances avec les termes liés à l'hypertension.

La plausibilité clinique est toutefois limitée. L'hypertension maligne exige un contrôle tensionnel rapide, le plus souvent par voie parentérale. Le risque d'hyperkaliémie et d'insuffisance rénale rend un diurétique épargneur de potassium peu adapté. La prédiction reste purement computationnelle.

### Autres prédictions du modèle (toutes classées Hold)

| Rang | Indication prédite | Score TxGNN | Niveau de preuve | Commentaire |
|---|---|---|---|---|
| 2 | Hypertension rénovasculaire maligne | 99,89 % | L5 | Urgence aiguë ; rétention de potassium et baisse de la perfusion rénale préoccupantes |
| 3 | Hypertension pulmonaire d'origine multifactorielle mal élucidée | 99,88 % | L5 | Lien faible ; aucun effet connu sur le remodelage vasculaire pulmonaire |
| 4 | Hypertension pulmonaire liée à une maladie pulmonaire et/ou à l'hypoxie | 99,88 % | L5 | Les deux articles retrouvés ne soutiennent pas l'indication |
| 5 | Syndrome de Braddock | 99,84 % | L5 | Prédiction purement computationnelle |
| 6 | Cœur pulmonaire chronique | 99,75 % | L4 | Preuves indirectes issues de l'insuffisance cardiaque en général |

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est actuellement enregistré.

## Preuves de la Littérature

Aucune littérature n'est disponible pour l'indication principale (maladie rénale hypertensive maligne). Pour les indications de rang inférieur, deux prédictions disposent de publications, qui restent indirectes ou peu pertinentes :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [1916562](https://pubmed.ncbi.nlm.nih.gov/1916562/) | 1991 | Étude clinique (hémodynamique, association) | Fortschritte der Medizin | Chez 12 patients en insuffisance cardiaque chronique (NYHA II-III), l'association vérapamil/triamtérène/hydrochlorothiazide pendant 4 semaines a réduit la pression artérielle (145/93 à 133/86 mmHg) et la fréquence cardiaque (indication : cœur pulmonaire chronique, preuve indirecte) |
| [2924690](https://pubmed.ncbi.nlm.nih.gov/2924690/) | 1989 | Revue | Deutsche medizinische Wochenschrift | Comparaison, chez 16 patients en insuffisance cardiaque, d'une association diurétique (hydrochlorothiazide + triamtérène) et d'un digitalique (indication : cœur pulmonaire chronique, preuve indirecte) |
| [2766837](https://pubmed.ncbi.nlm.nih.gov/2766837/) | 1989 | Rapport de cas | Chest | Œdème pulmonaire à basse pression après la prise d'un comprimé triamtérène-hydrochlorothiazide, attribué à l'hydrochlorothiazide : il s'agit d'un effet indésirable, non d'un bénéfice |
| [5639361](https://pubmed.ncbi.nlm.nih.gov/5639361/) | 1968 | Préclinique (physiologie animale) | The Journal of Physiology | Étude du potentiel électrique de la muqueuse colique chez le rat, sans pertinence clinique pour l'indication |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63870751 | PRESTOLE, gélule (ALMIRALL) | Gélule | Non renseignée (AMM annulée) |

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) :
  - Atteintes hépatiques : insuffisance hépatique, maladie du foie, coma hépatique, encéphalopathie hépatique, maladie de la vésicule biliaire, pancréatite
  - Atteintes rénales et urinaires : maladie rénale, anurie, néphrolithiase, néphrocalcinose, néphropathie urique aiguë, pyourètre
  - Troubles métaboliques : diabète de type 1 et de type 2, acidocétose diabétique, acidose, acidose lactique acquise, goutte, hyperuricémie, hypercalcémie, hyperparathyroïdie, ostéite fibreuse, troubles du métabolisme du phosphore
  - Autres : lupus érythémateux systémique (y compris pédiatrique), anémie par carence en acide folique, ictère néonatal
- **Interactions médicamenteuses** : 104 interactions recensées. Parmi celles listées :
  - **Majeure** : citrate de potassium (risque d'hyperkaliémie)
  - **Modérée** : hydrocortisone, métformine, bupropion, triamcinolone, morphine, dexaméthasone, bétaméthasone, bisacodyl, budésonide, canagliflozine, acide picosulfurique, polyéthylène glycol (3350 avec électrolytes), dapagliflozine, dronabinol
  - **Mineure** : famotidine, ranitidine, doxycycline, cimétidine, minocycline

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5 pour l'indication principale), sans essai ni publication. Le profil de risque est défavorable (hyperkaliémie, atteinte rénale) dans une urgence hypertensive. La seule AMM française est annulée, et les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle de l'ANSM (mises en garde, contre-indications), lacune bloquante pour le screening de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Rechercher des études cliniques ou observationnelles ciblant la maladie rénale hypertensive, en particulier en dehors de la forme maligne
- Évaluer le risque d'hyperkaliémie chez les patients à fonction rénale altérée, et clarifier le statut commercial actuel du triamtérène en France
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

