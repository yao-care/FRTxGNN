---
layout: default
title: Ginseng
parent: Prédiction du modèle uniquement (L5)
nav_order: 361
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ginseng : nouvelle indication prédite, Ostéoporose médicamenteuse (drug-induced osteoporosis) (niveau de preuve L5). Indication d'origine : Non renseignée dans l'AMM"
monitor_inn: "ginseng"
predicted_indications: ["drug-induced osteoporosis", "acne (disease)", "severe nonproliferative diabetic retinopathy", "hemorrhagic disease of newborn", "cortical cataract", "nuclear senile cataract", "diabetic retinopathy", "amenorrhea (disease)", "immature cataract", "craniostenosis cataract"]
---

# Ginseng
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

## Ginseng : D'une indication d'origine non renseignée à l'ostéoporose médicamenteuse
{: .text-alpha }

## Résumé en Une Phrase

Ginseng (DrugBank DB01404) est présent en France sous forme de préparation homéopathique (GINSENG BOIRON, dilutions 2CH à 30CH ou 4DH à 60DH). Aucune indication approuvée n'est renseignée dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**ostéoporose médicamenteuse**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette prédiction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans l'AMM |
| Nouvelle Indication Prédite | Ostéoporose médicamenteuse (drug-induced osteoporosis) |
| Score de Prédiction TxGNN | 99,95 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Le ginseng est une plante médicinale dont les principaux constituants actifs sont les ginsénosides. Aucune indication d'origine n'est documentée dans l'AMM française, ce qui empêche d'établir un lien direct entre l'usage initial et la nouvelle indication.

Des travaux précliniques évoquent une influence des ginsénosides sur le métabolisme osseux. Cette piste reste une hypothèse : les données compilées pour ce rapport ne contiennent aucune étude qui la confirme pour l'ostéoporose médicamenteuse. La prédiction repose donc uniquement sur la proximité du médicament et de la maladie dans le graphe de connaissances du modèle.

Le produit commercialisé en France est une préparation homéopathique fortement diluée. La transposition de données obtenues avec des extraits de ginseng ou des ginsénosides à cette préparation est donc très incertaine.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62760800 | GINSENG BOIRON, degré de dilution compris entre 2CH et 30CH ou entre 4DH et 60DH (BOIRON) | Comprimé, solution(s), granules, poudre et pommade | Non renseignée |

Cette AMM est annulée. Il n'existe aucune AMM en vigueur pour ce médicament en France.

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 83 interactions sont recensées. Parmi celles analysées, toutes sont de niveau **modéré**. Elles concernent surtout les médicaments antidiabétiques, avec un risque probable d'effet hypoglycémiant additif :
  - Antidiabétiques oraux : metformine, pioglitazone, acarbose, glimépiride, chlorpropamide.
  - Inhibiteurs de la DPP-4 : alogliptine, linagliptine.
  - Inhibiteurs du SGLT2 : canagliflozine, dapagliflozine, empagliflozine.
  - Agonistes du GLP-1 : albiglutide, dulaglutide, sémaglutide, lixisénatide.
  - Insulines : asparte, dégludec, détémir, glargine, glulisine.
  - Acide acétylsalicylique.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour l'ostéoporose médicamenteuse repose uniquement sur le score du modèle (niveau L5), sans essai ni publication. Le produit n'a plus d'AMM en vigueur et son indication d'origine n'est pas documentée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les informations de sécurité de la notice ANSM (mises en garde, contre-indications), actuellement manquantes et bloquantes pour l'étape de screening de sécurité.
- Les données sur le mécanisme d'action, par exemple via DrugBank, pour analyser le lien mécanistique avec le métabolisme osseux.
- Des études précliniques ou cliniques portant spécifiquement sur le ginseng ou les ginsénosides dans l'ostéoporose médicamenteuse.
- Une clarification de la pertinence des données du ginseng (extraits) pour une préparation homéopathique diluée.

**Remarque :** parmi les autres prédictions, la **rétinopathie diabétique** dispose de la base de preuves la plus riche (20 publications, niveau L4). Elle comprend surtout des études précliniques et des revues, ainsi qu'une étude prospective randomisée en double aveugle de 2026 sur le ginseng rouge coréen. Elle mérite une évaluation distincte, sous réserve de la confirmation des résultats cliniques.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

