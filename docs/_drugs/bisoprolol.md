---
layout: default
title: Bisoprolol
parent: Prédiction du modèle uniquement (L5)
nav_order: 110
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Bisoprolol : nouvelle indication prédite, Hypertension rénovasculaire maligne (niveau de preuve L5). Indication d'origine : Hypertension artérielle (selon la base de connaissances TxGNN"
monitor_inn: "BISOPROLOL"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Bisoprolol
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

# Bisoprolol : De l'Hypertension Artérielle à l'Hypertension Rénovasculaire Maligne

## Résumé en Une Phrase

Le bisoprolol est un bêta-bloquant cardiosélectif, initialement utilisé pour le traitement de l'hypertension artérielle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension rénovasculaire maligne**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.
Il s'agit d'une forme sévère de l'indication d'origine plutôt que d'un véritable repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypertension artérielle (selon la base de connaissances TxGNN ; aucun texte d'indication n'est disponible dans les AMM) |
| Nouvelle Indication Prédite | Hypertension rénovasculaire maligne |
| Score de Prédiction TxGNN | 99,94 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Toutes les AMM sont annulées |
| Nombre d'AMM | 12 (toutes annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le bisoprolol est un bêta-bloquant sélectif des récepteurs bêta-1. Il abaisse la pression artérielle et freine la libération de rénine, ce qui est plausiblement pertinent pour l'hypertension d'origine rénovasculaire.

L'hypertension rénovasculaire maligne est une forme sévère de l'hypertension, indication d'origine du médicament. Le score élevé de TxGNN (99,94 %) reflète ce chevauchement dans le graphe de connaissances et ne constitue pas une preuve clinique.

Cette inférence reste purement mécanistique. La prise en charge de l'hypertension maligne repose généralement sur un traitement parentéral urgent et sur le traitement de la sténose artérielle rénale sous-jacente. Un bêta-bloquant oral ne serait donc pas l'approche principale.

**Autres prédictions du modèle (toutes de niveau L4-L5) :**

| Maladie prédite | Score TxGNN | Niveau de preuve | Remarque |
|------|------|------|------|
| Néphropathie hypertensive maligne | 99,94 % | L5 | Score identique à l'entrée rénovasculaire, ce qui suggère une proximité dans le graphe plutôt qu'un soutien indépendant |
| Hypertension pulmonaire d'origine multifactorielle peu claire | 99,93 % | L5 | Aucune justification mécanistique ; les bêta-bloquants sont utilisés avec prudence dans l'hypertension artérielle pulmonaire |
| Hypertension pulmonaire liée à une maladie pulmonaire et/ou à l'hypoxie | 99,93 % | L4 | Littérature indirecte uniquement (modèles précliniques, insuffisance cardiaque) |
| Syndrome de Braddock | 99,91 % | L5 | Aucun lien mécanistique évident |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'hypertension rénovasculaire maligne.

À titre indicatif, 8 publications indirectes ont été identifiées pour l'hypertension pulmonaire liée à une maladie pulmonaire ou à l'hypoxie (prédiction de rang 4). Elles portent sur des modèles précliniques de cardioprotection, la tolérance respiratoire des bêta-bloquants dans l'insuffisance cardiaque et l'adaptation cardiaque à l'hypoxie. Aucune n'a testé le bisoprolol chez des patients atteints d'hypertension pulmonaire. Parmi elles, une étude comparative clinique (carvédilol, névibolol et bisoprolol dans l'insuffisance cardiaque modérée, PMID [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/), 2013) est la plus proche de la pratique clinique, mais elle ne concerne pas l'hypertension.

---

## Informations de Marché en France

Les 12 AMM recensées sont annulées ; aucune n'est actuellement valide. Le texte de l'indication approuvée n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69455705 | BISOPROLOL BGR 7,5 mg | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |
| 65591063 | BISOPROLOL KRKA 5 mg | Comprimé pelliculé sécable | Non renseignée (AMM annulée) |
| 62969789 | BISOPROLOL TEVA 5 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 63162282 | CARDENSIEL 1,25 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 60524826 | BISOPROLOL TEVA 10 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie, et non texte de notice) : asthme (y compris allergique et intrinsèque), diabète et acidocétose diabétique, maladie rénale, anurie, maladie hépatique, encéphalopathie hépatique, pancréatite, lupus érythémateux systémique, psoriasis, goutte, myasthénie, troubles anxieux et dysthymiques, ainsi que plusieurs troubles métaboliques (carence en potassium, hypercalcémie, hyperparathyroïdie, néphrocalcinose, troubles du métabolisme du phosphore).
- **Interactions médicamenteuses** : 100 interactions recensées (extrait des 20 premières). La plupart sont de niveau modéré : épinéphrine, corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide), anticholinergiques (atropine, hyoscyamine, méthscopolamine), bupropion, morphine, acétohexamide et sels de calcium. Les interactions avec l'acide acétylsalicylique, l'hydroxyde d'aluminium et l'attapulgite sont mineures.
- **Risque propre aux nouvelles indications** : les bêta-bloquants sont utilisés avec prudence dans l'hypertension pulmonaire en raison du risque de baisse du débit cardiaque et de la fonction du ventricule droit.

Pour les mises en garde officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Elle recoupe l'indication déjà connue (hypertension) et ne constitue pas un repositionnement réel.
- Toutes les AMM françaises sont annulées, et les données de sécurité officielles ainsi que le mécanisme d'action sont manquants.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications officielles à partir de la notice (site de l'ANSM).
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Documenter la place réelle d'un bêta-bloquant oral dans l'hypertension maligne d'origine rénovasculaire, par rapport aux traitements de référence.
- Clarifier le statut réglementaire en France (motifs d'annulation des AMM et existence éventuelle d'autres spécialités).
- Pour l'hypertension pulmonaire, générer des données de sécurité dédiées avant toute exploration.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

