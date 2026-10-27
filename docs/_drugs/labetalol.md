---
layout: default
title: Labetalol
parent: Preuves modérées (L3-L4)
nav_order: 428
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-14
description: "Labetalol : nouvelle indication prédite, Hypertension rénovasculaire maligne (niveau de preuve L4). Indication d'origine : Hypertension artérielle / troubles hypertensifs"
monitor_inn: "labetalol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Labetalol
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **4** 
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

## Labetalol : De l'Hypertension à l'Hypertension Rénovasculaire Maligne
{: .text-alpha }

## Résumé en Une Phrase

Labétalol est un bêta-bloquant doté d'une activité alpha-1 bloquante, initialement utilisé pour le traitement de l'hypertension artérielle et des troubles hypertensifs.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension rénovasculaire maligne**,
mais **aucun essai clinique** et **une seule publication** (un cas clinique) soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle / troubles hypertensifs (d'après le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Hypertension rénovasculaire maligne |
| Score de Prédiction TxGNN | 99,08 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Autorisation annulée uniquement |
| Nombre d'AMM | 1 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le labétalol associe un blocage alpha-1 et un blocage bêta non sélectif, ce qui réduit les résistances vasculaires et la fréquence cardiaque. Il est déjà utilisé dans les urgences hypertensives.

L'hypertension rénovasculaire maligne est en grande partie entraînée par l'activation du système rénine-angiotensine, et le blocage bêta diminue dans une certaine mesure la libération de rénine. Il s'agit toutefois d'une simple extension de l'indication hypertension existante, et non d'un véritable signal de repositionnement. Le score élevé du modèle reflète probablement la proximité avec l'indication déjà approuvée.

Les autres prédictions (maladie rénale hypertensive maligne, deux formes d'hypertension pulmonaire) sont plus faibles. Pour l'hypertension pulmonaire, aucun rationnel mécanistique n'est soutenu : le remodelage vasculaire pulmonaire n'est pas ciblé par le blocage alpha/bêta, et le blocage bêta non sélectif peut aggraver un bronchospasme ou altérer le débit cardiaque compensatoire en cas de surcharge cardiaque droite.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Cas clinique | Med J Aust | Hypertension maligne chez un homme de 20 ans après prise de drogues hallucinogènes, avec vascularite rénale ; le minoxidil et le labétalol ont permis le contrôle initial de la tension, et la prednisone a fait régresser l'artérite |

Cette seule publication est un cas clinique isolé. Pour les autres indications prédites, les publications retrouvées (hypertension de la grossesse, intoxication aux bêta-bloquants, hypertension postopératoire, modèles animaux) ne concernent pas le traitement de l'hypertension pulmonaire.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60558554 | TRANDATE 5 mg/ml, solution injectable (ASPEN PHARMA TRADING, Irlande) | Solution injectable | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : insuffisance hépatique, maladie hépatique, encéphalopathie hépatique, coma hépatique, maladie rénale, anurie, bloc auriculo-ventriculaire, emphysème pulmonaire, maladie bronchique, diabète et acidocétose diabétique, lupus érythémateux systémique, goutte, hypotension, pancréatite, maladie de la vésicule biliaire, troubles anxieux, hyperparathyroïdie, hypercalcémie, néphrocalcinose, carence en potassium, ictère néonatal et syndrome de l'iris flasque peropératoire.
- **Interactions médicamenteuses** : 241 interactions recensées. Parmi les principales :
  - Majeures : épinéphrine, dolasétron.
  - Modérées : corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide), morphine, atropine et anticholinergiques (hyoscyamine, méthscopolamine, dicyclomine), cimétidine, canagliflozine, dapagliflozine, chlorpropamide, sels de calcium.
  - Mineures : acide acétylsalicylique, oxyde de magnésium.

Les mises en garde et contre-indications de la notice n'ont pas pu être consultées. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction principale est une extension proche de l'indication hypertension déjà connue, sans essai clinique et avec un seul cas clinique ancien. L'AMM française est annulée, et les données de sécurité issues de la notice manquent, ce qui bloque le passage à l'étape de criblage de sécurité. Pour l'hypertension pulmonaire, la prédiction n'est pas soutenue par les preuves et pose un problème de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice officielle (mises en garde et contre-indications) auprès de l'ANSM
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Rechercher des études cliniques ou observationnelles ciblant l'hypertension rénovasculaire maligne et la maladie rénale hypertensive maligne
- Clarifier la disponibilité d'une formulation commercialisée en France, l'AMM étant annulée
- Évaluer la compatibilité des voies d'administration et la similarité avec l'indication d'origine (actuellement en attente)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

