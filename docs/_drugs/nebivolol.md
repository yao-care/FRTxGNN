---
layout: default
title: Nebivolol
parent: Prédiction du modèle uniquement (L5)
nav_order: 528
evidence_level: L5
indication_count: 5
---

# Nebivolol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

# Nébivolol : De l'Hypertension Artérielle à l'Hypertension Rénale Maligne

## Résumé en Une Phrase

Le nébivolol est un bêta-bloquant cardiosélectif, initialement utilisé pour traiter l'hypertension artérielle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie rénale hypertensive maligne**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette indication précise : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (le texte d'indication de l'AMM n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Maladie rénale hypertensive maligne |
| Score de Prédiction TxGNN | 99,42 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisation annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, le nébivolol est un bêta-bloquant bêta-1 sélectif, dont l'effet vasodilatateur passe par la voie du monoxyde d'azote (NO). Son efficacité dans l'hypertension artérielle est établie.

La maladie rénale hypertensive maligne est une atteinte rénale secondaire à une hypertension sévère. Sur le plan théorique, une baisse de la pression artérielle pourrait limiter les lésions rénales. Toutefois, le score élevé du modèle (99,4 %) reflète très probablement la proximité dans le graphe de connaissances avec l'indication originale d'hypertension, et non une preuve indépendante.

Les autres indications prédites relèvent de la même logique : hypertension rénovasculaire maligne (score identique, absence de preuves ; le blocage bêta pourrait réduire la libération de rénine), hypertension pulmonaire (deux entités prédites) et syndrome de Braddock (aucun lien mécanistique clair).

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour la maladie rénale hypertensive maligne.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour la maladie rénale hypertensive maligne.

À titre informatif, une littérature indirecte existe pour l'hypertension pulmonaire (3ᵉ indication prédite), mais elle ne porte pas sur le traitement de cette maladie : il s'agit surtout d'études précliniques de protection d'organe (hépatique, rénale) et d'études cliniques sur les bêta-bloquants en contexte respiratoire ou d'hypoxie.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66673481 | TEMERIT 5 mg, comprimé quadrisécable (DIFARMED, Espagne) | Comprimé quadrisécable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, maladie hépatique, maladie de la vésicule biliaire, diabète, acidocétose diabétique, maladie vasculaire périphérique, claudication intermittente, artériopathie périphérique, hypoglycémie, bloc auriculo-ventriculaire, maladie bronchique, maladie du sinus et maladie familiale du sinus.
- **Interactions médicamenteuses** : 174 interactions recensées. Parmi les 20 premières, la plupart sont de niveau modéré (épinéphrine, corticoïdes tels que l'hydrocortisone, la dexaméthasone, la bétaméthasone, le budésonide et la triamcinolone, bupropion, morphine, atropine, hyoscyamine, glycopyrronium, dicyclomine, lorcasérine, canagliflozine, dapagliflozine, chlorpropamide, sels de calcium). L'acide acétylsalicylique et l'oxyde de magnésium sont de niveau mineur.
- **Points d'attention spécifiques** : les bêta-bloquants sont à utiliser avec prudence en cas d'hypertension pulmonaire ou de maladie pulmonaire hypoxique, et la fonction rénale doit être prise en compte dans l'indication rénale proposée.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui ne sont pas disponibles dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication pour la maladie rénale hypertensive maligne. De plus, les données de sécurité officielles sont absentes et l'AMM française est annulée.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice officielle (mises en garde et contre-indications) auprès de l'ANSM, lacune bloquante pour le dépistage de sécurité
- Compléter les données sur le mécanisme d'action (par exemple via DrugBank)
- Réaliser une revue de la littérature ciblée sur les bêta-bloquants et le nébivolol dans l'atteinte rénale hypertensive maligne
- Clarifier le statut réglementaire en France (AMM annulée, absence de produit valide)
- Évaluer la sécurité dans les populations à risque (insuffisance rénale, hépatique, maladie vasculaire périphérique, diabète)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

