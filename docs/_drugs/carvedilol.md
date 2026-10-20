---
layout: default
title: Carvedilol
parent: Prédiction du modèle uniquement (L5)
nav_order: 144
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Carvedilol : nouvelle indication prédite, Hypertension rénovasculaire maligne (niveau de preuve L5). Indication d'origine : Hypertension artérielle"
monitor_inn: "carvedilol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Carvedilol
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

# Carvedilol : De l'Hypertension à l'Hypertension Rénovasculaire Maligne

## Résumé en Une Phrase

Le carvedilol est un bêta-bloquant non sélectif doté d'une activité alpha-1 bloquante, initialement utilisé pour traiter l'**hypertension artérielle**.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension rénovasculaire maligne**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction précise.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (selon le graphe de connaissances TxGNN ; aucun texte d'indication n'est disponible dans les AMM) |
| Nouvelle Indication Prédite | Hypertension rénovasculaire maligne |
| Score de Prédiction TxGNN | 99,55 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulé uniquement (aucune AMM valide) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, le carvedilol associe un blocage bêta-adrénergique et un blocage alpha-1, ce qui abaisse la pression artérielle. Son efficacité dans l'hypertension est établie.

Le lien avec l'hypertension rénovasculaire maligne reste uniquement théorique, au niveau de la classe pharmacologique. Le score élevé du modèle semble refléter la proximité de cette entité avec l'indication d'hypertension déjà connue dans le graphe de connaissances, et non une preuve indépendante. Cette pathologie est une urgence distincte, dominée par l'activation du système rénine-angiotensine, où les bêta-bloquants ne sont généralement pas un traitement de première intention. La prédiction s'apparente donc plutôt à une reformulation de l'indication d'origine qu'à un véritable signal de repositionnement.

Parmi les autres prédictions, deux concernent aussi des hypertensions malignes ou des formes pulmonaires : l'hypertension maligne avec atteinte rénale (99,55 %), l'hypertension pulmonaire de mécanisme multifactoriel incertain (99,54 %), l'hypertension pulmonaire liée à une maladie pulmonaire ou à l'hypoxie (99,54 %) et le syndrome de Braddock (99,37 %). Toutes sont de niveau L5, sauf l'hypertension pulmonaire liée à l'hypoxie (L4, préclinique indirect). Pour cette dernière, une étude chez le rat (PMID 26291659) montre que le carvedilol corrige l'hypertension induite par l'hypoxie intermittente chronique, mais il s'agit d'une hypertension systémique et non pulmonaire.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée à l'hypertension rénovasculaire maligne n'est disponible actuellement.

## Informations de Marché en France

Toutes les AMM recensées sont annulées. Le texte d'indication approuvée n'est pas renseigné. Les cinq premières sont listées ci-dessous (sur 20).

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 63608400 | CARVEDILOL ARROW 25 mg | Comprimé pelliculé sécable | Annulée |
| 63812043 | CARVEDILOL VIATRIS 12,5 mg | Comprimé pelliculé sécable | Annulée |
| 64203045 | CARVEDILOL EG 12,5 mg | Comprimé pelliculé sécable | Annulée |
| 64233832 | KREDEX 6,25 mg | Comprimé sécable | Annulée |
| 68474364 | CARVEDILOL TEVA 6,25 mg | Comprimé sécable | Annulée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, asthme (y compris intrinsèque et allergique), bronchite, emphysème pulmonaire et maladies bronchiques, diabète et acidocétose diabétique, hypotension, maladie vasculaire périphérique (claudication intermittente, artériopathie), bloc auriculo-ventriculaire, maladie du sinus (y compris familiale), angor de Prinzmetal, anaphylaxie, syndrome de l'iris hypotonique peropératoire.
- **Interactions médicamenteuses** : 329 interactions recensées. Une est majeure (**épinéphrine**). Plusieurs sont modérées : hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide, hyoscyamine, atropine, bupropion, morphine, lorcasérine, canagliflozine, acétohexamide, ainsi que des sels de calcium (phosphate, acétate, carbonate, citrate). Les interactions avec l'acide acétylsalicylique, l'hydroxyde d'aluminium et l'attapulgite sont mineures.
- **Points d'attention propres aux indications prédites** : le blocage bêta-adrénergique pourrait altérer la fonction ventriculaire droite et la réserve de débit cardiaque dans l'hypertension pulmonaire, ou aggraver la fonction respiratoire en cas de maladie pulmonaire.

Les mises en garde et contre-indications de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication spécifique. Elle reflète vraisemblablement la proximité avec l'indication d'hypertension d'origine. Il n'existe en outre aucune AMM valide en France, et les données de sécurité de la notice manquent (lacune bloquante).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications, afin de pouvoir réaliser le premier criblage de sécurité.
- Obtenir les données sur le mécanisme d'action (DrugBank).
- Rechercher des études cliniques ou observationnelles ciblées sur l'hypertension rénovasculaire maligne.
- Clarifier la raison de l'annulation des AMM et la disponibilité réelle du médicament en France.
- Si l'axe de l'hypertension pulmonaire est exploré, évaluer spécifiquement le risque cardiaque droit et respiratoire du blocage bêta-adrénergique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

