---
layout: default
title: Amiloride
parent: Prédiction du modèle uniquement (L5)
nav_order: 56
evidence_level: L5
indication_count: 6
---

# Amiloride
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

# Amiloride : De l'hypertension à l'hypertension maligne d'origine rénale

## Résumé en Une Phrase

L'amiloride est un diurétique épargneur de potassium, initialement utilisé pour traiter l'hypertension artérielle et l'insuffisance cardiaque congestive.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie rénale hypertensive maligne**, mais aucun essai clinique ni aucune publication ne soutient directement cette prédiction (**0 essai clinique**, **0 publication** pour cette indication).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle, insuffisance cardiaque congestive (l'indication figurant dans les AMM françaises n'est pas renseignée) |
| Nouvelle Indication Prédite | Maladie rénale hypertensive maligne |
| Score de Prédiction TxGNN | 99,82 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compiléesées pour ce rapport. D'après les connaissances pharmacologiques établies, l'amiloride bloque le canal sodique épithélial (ENaC) du néphron distal. Il réduit ainsi la réabsorption du sodium et contribue au contrôle de la pression artérielle tout en épargnant le potassium.

L'indication originale (hypertension) et la nouvelle indication prédite (maladie rénale hypertensive maligne) sont étroitement liées sur le plan physiopathologique : il s'agit d'une atteinte rénale dans un contexte d'hypertension sévère. Le score élevé du modèle (0,998) reflète vraisemblablement cette proximité avec l'indication déjà connue, et non une preuve spécifique.

Il faut rester prudent : aucun essai ni aucune publication n'étudie la forme maligne et rénale. La prédiction reste donc une hypothèse issue du modèle. Le même constat vaut pour les autres pistes prédites (hypertension rénovasculaire maligne, hypertension pulmonaire, syndrome de Braddock), dont les preuves sont absentes ou indirectes. La seule piste un peu mieux documentée est le cœur pulmonaire chronique (niveau L3), par extrapolation depuis l'insuffisance cardiaque.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour l'indication principale (maladie rénale hypertensive maligne).

Pour information, une publication concerne une indication voisine prédite en rang 2 (hypertension rénovasculaire maligne) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Revue | J Hypertens Suppl | Investigation de l'hypertension minéralocorticoïde (aldostéronisme primaire, hypokaliémie). Référence diagnostique et physiopathologique, sans démonstration d'efficacité de l'amiloride. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63371015 | MODAMIDE 5 mg, comprimé (annulée) | Comprimé | Non renseignée |
| 63824615 | LOGIRENE, comprimé sécable (annulée) | Comprimé sécable | Non renseignée |
| 64343809 | MODUCREN, comprimé (annulée) | Comprimé | Non renseignée |

## Considérations de Sécurité

- **Contre-indications (issues du graphe de connaissances, non du texte de la notice)** : insuffisance rénale, anurie, néphropathie diabétique, maladie hépatique, encéphalopathie et coma hépatiques, pancréatite, maladie de la vésicule biliaire, diabète et acidocétose diabétique, déficit en potassium, goutte et hyperuricémie, acidose (dont acidose lactique acquise), hyperparathyroïdie, lupus érythémateux systémique, ictère néonatal, pyourétère.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi celles listées : de niveau modéré avec les corticoïdes (hydrocortisone, bétaméthasone, dexaméthasone, budésonide), la metformine, les inhibiteurs de SGLT2 (canagliflozine, dapagliflozine, empagliflozine, ertugliflozine), l'exénatide, le bupropion, le dronabinol et certains laxatifs (bisacodyl, huile de ricin, glycérine, lactitol, lactulose). Niveau mineur avec la doxycycline, l'amoxicilline et la cimétidine.
- **Signal de sécurité** : un cas rapporté d'hyperkaliémie sévère chez une patiente âgée sous triméthoprime-sulfaméthoxazole souligne la nécessité de surveiller le potassium et la fonction rénale.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être obtenues. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication directe, et le médicament n'a plus d'AMM active en France.
- Les contre-indications du graphe de connaissances incluent des atteintes rénales, ce qui est préoccupant pour une indication rénale.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Des études cliniques ou précliniques ciblant l'atteinte rénale hypertensive maligne
- Une évaluation du risque d'hyperkaliémie en cas d'insuffisance rénale
- Une clarification du statut réglementaire (AMM annulées) et des indications approuvées
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

