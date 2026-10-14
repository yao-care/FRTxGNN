---
layout: default
title: Ipilimumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 410
evidence_level: L5
indication_count: 2
---

# Ipilimumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Ipilimumab : Du Mélanome Métastatique à la Choroïdérémie

## Résumé en Une Phrase

L'ipilimumab est un anticorps monoclonal anti-CTLA-4, initialement utilisé dans le traitement du mélanome métastatique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **choroïdérémie**, une dégénérescence rétinienne héréditaire rare.
Actuellement, **aucun essai clinique** et **aucune publication** ne soutiennent cette prédiction, qui repose uniquement sur le modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mélanome métastatique (issue de la base de connaissances du modèle ; le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Choroïdérémie |
| Score de Prédiction TxGNN | 99,06 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. L'ipilimumab est un anticorps anti-CTLA-4 qui lève un frein de l'activation des lymphocytes T et amplifie la réponse immunitaire antitumorale. Son efficacité est établie dans le mélanome.

**En pratique, cette prédiction n'est pas étayée sur le plan mécanistique.** La choroïdérémie est une maladie monogénique liée à l'X, causée par la perte de fonction du gène *CHM* (REP1). Elle se caractérise par la dégénérescence progressive de l'épithélium pigmentaire rétinien, des photorécepteurs et de la choroïde. Aucun mécanisme dépendant des points de contrôle immunitaires n'est établi dans cette maladie.

Le score élevé du modèle (99,06 %) est une prédiction issue d'un graphe de connaissances. Il n'est confirmé par aucune donnée clinique ou bibliographique. L'activation immunitaire systémique expose en outre à des événements indésirables d'origine immunitaire, notamment des inflammations oculaires comme l'uvéite, ce qui serait défavorable dans une rétine déjà en dégénérescence.

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
| 66532840 (annulée) | YERVOY 5 mg/mL, solution à diluer pour perfusion (BRISTOL-MYERS SQUIBB / PFIZER EEIG, Irlande) | Solution à diluer pour perfusion | Texte d'indication non renseigné |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Immunothérapie (anticorps anti-CTLA-4) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Surveillance des événements indésirables d'origine immunitaire, notamment oculaires (uvéite) ; pour le reste, consulter la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

- **Événements indésirables d'origine immunitaire** : l'activation immunitaire systémique peut provoquer des inflammations oculaires, dont l'uvéite. Ce risque est particulièrement préoccupant dans une rétine dégénérative.
- **Interactions médicamenteuses** : 100 interactions sont répertoriées. Les principales sont :
  - **Majeures** : anticoagulants (apixaban, bétrixaban, édoxaban, bivalirudine, dalteparine, désirudine, argatroban, danaparoïde).
  - **Modérées** : corticoïdes (hydrocortisone, prednisone, prednisolone, dexaméthasone, bétaméthasone, triamcinolone, budésonide), statines (rosuvastatine, simvastatine), métronidazole, tinidazole et naltrexone.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Aucun lien mécanistique crédible n'existe avec la choroïdérémie, et le risque d'inflammation oculaire immuno-induite est défavorable.
- Le seul produit français est de plus annulé. À titre de comparaison, d'autres indications prédites par le modèle, comme le mélanome non cutané, disposent de bien plus de données.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des données précliniques ou mécanistiques justifiant l'implication de la voie CTLA-4 dans la choroïdérémie.
- Les données détaillées sur le mécanisme d'action et les informations de sécurité issues de la notice (mises en garde et contre-indications).
- Une évaluation du risque d'uvéite et d'effets oculaires immuno-induits dans un contexte de dégénérescence rétinienne.
- La confirmation du statut réglementaire en France, l'AMM étant annulée.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

