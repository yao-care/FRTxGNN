---
layout: default
title: Metformin
parent: Prédiction du modèle uniquement (L5)
nav_order: 483
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Metformin : nouvelle indication prédite, Syndrome du membre raide focal (niveau de preuve L5). Indication d'origine : Diabète de type 2"
monitor_inn: "metformin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
---

# Metformin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Metformine : Du Diabète de Type 2 au Syndrome du Membre Raide Focal

## Résumé en Une Phrase

La metformine est un antidiabétique oral, initialement utilisé pour le traitement du diabète de type 2.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **syndrome du membre raide focal**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Diabète de type 2 (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas disponible) |
| Nouvelle Indication Prédite | Syndrome du membre raide focal |
| Score de Prédiction TxGNN | 99,45 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 9 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la metformine appartient à la classe des biguanides. Elle est reconnue pour activer l'AMPK, réduire la production hépatique de glucose et exercer de légers effets anti-inflammatoires. Son efficacité dans le diabète de type 2 est établie.

Le syndrome du membre raide focal appartient au spectre du syndrome de la personne raide, un trouble neurologique d'origine auto-immune, souvent associé à des anticorps anti-GAD. Aucun lien mécanistique direct n'est établi entre les actions connues de la metformine et cette pathologie. La prédiction reflète vraisemblablement des voisins communs dans le graphe de connaissances, notamment la comorbidité fréquente avec le diabète auto-immun associé aux anti-GAD, plutôt qu'un véritable mécanisme thérapeutique.

Le même constat s'applique au syndrome de la personne raide classique, qui obtient exactement le même score (99,45 %), ce qui suggère une représentation commune dans le graphe. Par prudence, la plausibilité mécanistique de cette prédiction doit être considérée comme faible.

## Autres Indications Prédites

| Rang | Maladie | Score TxGNN | Niveau de Preuve | Remarque |
|------|------|------|------|------|
| 2 | Syndrome de la personne raide classique | 99,45 % | L5 | Même logique de comorbidité avec le diabète ; aucun mécanisme direct |
| 3 | Opsismodysplasie | 99,40 % | L5 | Lien spéculatif via la voie PI3K/AKT (INPPL1/SHIP2) et l'AMPK/mTOR |
| 4 | Syndrome de dysfonction répondant à la thiamine | 99,40 % | L5 | Lien indirect (phénotype diabétique, transporteurs) ; le traitement reste la thiamine |
| 5 | Lipodystrophie localisée d'origine médicamenteuse | 99,06 % | L5 | La plus plausible sur le plan biologique (sensibilité à l'insuline), mais sans données pour cette forme |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 9 AMM recensées sont toutes annulées ; aucune AMM valide n'est actuellement répertoriée. Le texte de l'indication approuvée n'est pas renseigné pour ces AMM.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 68196071 | METFORMINE VIATRIS 500 mg | Comprimé pelliculé | Annulée |
| 61232102 | STAGID 700 mg | Comprimé sécable | Annulée |
| 61048305 | METFORMINE EG LABO 500 mg | Comprimé pelliculé | Annulée |
| 60915020 | METFORMINE VIATRIS 1000 mg | Comprimé pelliculé sécable | Annulée |
| 67231181 | METFORMINE EG LABO 850 mg | Comprimé pelliculé | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, maladie rénale, pancréatite, maladie de la vésicule biliaire, insuffisance cardiaque congestive, insuffisance corticosurrénale, ainsi que plusieurs déficits hypophysaires et hypogonadismes hypogonadotropes (dont le syndrome de Kallmann et le syndrome de Sheehan).
- **Interactions médicamenteuses** : 642 interactions recensées. Parmi les exemples relevés :
  - *Majeures* : acétazolamide, éthanol
  - *Modérées* : dolutégravir, abémaciclib, phényléphrine, ranitidine, formotérol, pseudoéphédrine, kétorolac, nifédipine, épinéphrine, ibuprofène, éthinylestradiol, hydrocortisone, salbutamol, hydrochlorothiazide, acétohexamide
  - *Mineures* : acarbose, corticoïdes topiques (hydrocortisone, alclométasone)

Les mises en garde et contre-indications issues de la notice ANSM ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et aucun mécanisme plausible n'est identifié pour le syndrome du membre raide focal. De plus, aucune AMM n'est actuellement valide en France pour les produits recensés.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de la notice ANSM (mises en garde et contre-indications), actuellement bloquantes pour le criblage de sécurité
- Données détaillées sur le mécanisme d'action (via DrugBank)
- Revue de la littérature et des registres d'essais ciblée sur la metformine et le spectre du syndrome de la personne raide
- Vérification du statut réglementaire actuel de la metformine en France, car toutes les AMM recensées sont annulées
- Si une piste est à poursuivre, envisager en priorité la lipodystrophie localisée d'origine médicamenteuse (rang 5), mécanistiquement la plus plausible, après une recherche de preuves dédiée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

