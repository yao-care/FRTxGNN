---
layout: default
title: Silodosin
parent: Prédiction du modèle uniquement (L5)
nav_order: 703
evidence_level: L5
indication_count: 6
---

# Silodosin
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

# Silodosine : De l'Hyperplasie Bénigne de la Prostate à l'Hypertrichose Universelle Congénitale de type Ambras

## Résumé en Une Phrase

La silodosine est un antagoniste sélectif des récepteurs alpha-1A adrénergiques, initialement utilisé pour le traitement de l'hyperplasie bénigne de la prostate.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypertrichose universelle congénitale de type Ambras**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction.
Il s'agit d'une prédiction issue uniquement d'un graphe de connaissances, sans fondement mécanistique établi.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hyperplasie bénigne de la prostate (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Hypertrichose universelle congénitale de type Ambras |
| Score de Prédiction TxGNN | 99,99 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les informations connues, la silodosine est un antagoniste sélectif des récepteurs alpha-1A adrénergiques, agissant principalement sur le bas appareil urinaire et la prostate. Son efficacité dans l'hyperplasie bénigne de la prostate repose sur ce mécanisme.

La relation avec la nouvelle indication est très ténue. Le syndrome d'Ambras est d'origine génétique : il implique des remaniements chromosomiques en 8q22 qui affectent la régulation du gène TRPS1. Aucun lien plausible n'existe entre le blocage des récepteurs alpha-1A et cette cause. Le score élevé reflète probablement une proximité dans le réseau du graphe avec des phénotypes liés aux poils, et non une véritable relation thérapeutique.

Les autres prédictions du modèle (hypertrichose, malformations avec composante dentaire ou parodontale, syndromes avec malformation de Dandy-Walker, anomalies génétiques isolées de la tige pilaire, trichomégalie familiale isolée) présentent le même profil : scores élevés (de 99,2 % à 99,99 %), aucune preuve clinique ou bibliographique, et aucun mécanisme crédible. Pour l'hypertrichose, le sens de l'effet recherché (réduire la pilosité) reste de plus incertain.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Les 20 AMM recensées sont toutes annulées, aucune n'est actuellement valide. Le texte de l'indication approuvée n'est pas renseigné dans les données compilées. Voici les 5 premières :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60054312 | SILODOSINE SANDOZ 4 mg, gélule | Gélule | Non renseignée |
| 62493774 | SILODOSINE BIOGARAN 8 mg, gélule | Gélule | Non renseignée |
| 61605245 | SILODYX 4 mg, gélule | Gélule | Non renseignée |
| 63206729 | SILODOSINE EG 8 mg, gélule | Gélule | Non renseignée |
| 63168424 | SILODOSINE VIATRIS 4 mg, gélule | Gélule | Non renseignée |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : atrophie multisystématisée, syndrome de tachycardie orthostatique posturale, hypotension orthostatique, insuffisance hépatique, maladie rénale, pyo-uretère, syndrome de l'iris hypotonique peropératoire (IFIS).
- **Interactions médicamenteuses** : 99 interactions recensées. Parmi celles listées, la **clarithromycine** est classée comme **majeure**. Les interactions de niveau **modéré** incluent notamment le bupropion, l'aprépitant, la morphine, la dexaméthasone, la cimétidine, le miconazole, le clotrimazole, le rolapitant, le dronabinol, la nabilone, l'éliglustat, la métréleptine, ainsi que plusieurs inhibiteurs du SGLT2 (canagliflozine, dapagliflozine, empagliflozine, ertugliflozine).

Les mises en garde et contre-indications issues de la notice ANSM ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et sans mécanisme plausible reliant le blocage alpha-1A à une maladie génétique de la pilosité. De plus, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA) de la silodosine
- Mises en garde et contre-indications issues de la notice ANSM (blocage pour tout examen de sécurité)
- Éléments biologiques ou précliniques démontrant un lien entre la voie alpha-1A et la pilosité ou la voie TRPS1
- Clarification du sens de l'effet thérapeutique recherché dans l'hypertrichose
- Évaluation de la compatibilité de voie d'administration et de la similarité avec l'indication d'origine
- Réexamen d'autres indications prédites ou de pistes plus plausibles avant tout investissement
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

