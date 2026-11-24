---
layout: default
title: Bisoprolol
parent: Prédiction du modèle uniquement (L5)
nav_order: 110
evidence_level: L5
indication_count: 4
monitor_inn: "BISOPROLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
last_modified_at: 2026-11-24
description: "Bisoprolol : nouvelle indication prédite, Néphropathie hypertensive maligne (malignant hypertensive renal disease) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locale"
---

# Bisoprolol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

## Bisoprolol : bêtabloquant cardiosélectif bêta-1 → Néphropathie hypertensive maligne (malignant hypertensive renal disease)
{: .text-alpha }

## Résumé en Une Phrase

Le bisoprolol est un bêtabloquant qui bloque de façon sélective les récepteurs bêta-1 adrénergiques.
Le modèle TxGNN prédit qu'il pourrait être utile dans la **néphropathie hypertensive maligne (malignant hypertensive renal disease)**.
Aucun essai clinique ni aucune publication ne soutient actuellement cette prédiction, qui reste purement théorique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Néphropathie hypertensive maligne (malignant hypertensive renal disease) |
| Score de Prédiction TxGNN | 0,9994 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 17) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Bisoprolol (traduction non officielle) : « Le FUMARATE DE BISOPROLOL est un agent bêtabloquant adrénergique sélectif des récepteurs bêta 1 (cardiosélectif), dépourvu d'activité stabilisatrice de membrane significative et d'activité sympathomimétique intrinsèque dans sa gamme de doses thérapeutiques. La cardiosélectivité n'est cependant pas absolue et, à des doses plus élevées (≥ 20 mg), le fumarate de bisoprolol inhibe également les récepteurs bêta 2 -adrénergiques, principalement situés dans la musculature bronchique et vasculaire ; afin de conserver la sélectivité, il est donc important d'utiliser la dose efficace la plus faible. » Texte original en anglais : "BISOPROLOL FUMARATE is a beta 1 -selective (cardioselective) adrenoceptor blocking agent without significant membrane stabilizing activity or intrinsic sympathomimetic activity in its therapeutic dosage range. Cardioselectivity is not absolute, however, and at higher doses (≥ 20 mg) bisoprolol fumarate also inhibits beta 2 -adrenoceptors, chiefly located in the bronchial and vascular musculature; to retain selectivity it is therefore important to use the lowest effective dose." ([DailyMed: bisoprolol fumarate prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6517d564-ea55-4084-a8ab-34fea548c24e), version du 2026-11-11 ; consulté le 2026-11-19). Le bisoprolol est un bêtabloquant bêta-1 sélectif. En bloquant les récepteurs bêta-1, il réduit la fréquence cardiaque et le débit cardiaque, et freine la sécrétion de rénine par le rein.

Ces effets sur la pression artérielle et sur le système rénine-angiotensine pourraient être pertinents pour une atteinte rénale liée à l'hypertension. C'est la seule base de la prédiction, et aucune étude ne la confirme.

Cette piste a des limites importantes. La prise en charge de l'hypertension maligne avec atteinte rénale repose sur une baisse rapide et contrôlée de la pression artérielle, avec des médicaments autres que le bisoprolol oral. Le score élevé du modèle ne remplace donc pas une preuve clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Considérations de Sécurité

**Interactions médicamenteuses** : 100 interactions ont été recensées. Parmi les principales :

- **Modérées** : épinéphrine, bupropion, morphine, atropine, hyoscyamine, méthscopolamine, acétohexamide, corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide) et sels de calcium (acétate, carbonate, citrate, gluconate, glubionate).
- **Mineures** : acide acétylsalicylique, hydroxyde d'aluminium, attapulgite.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication.
- Les traitements de référence de cette situation d'urgence sont d'autres médicaments.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les données détaillées sur le mécanisme d'action du bisoprolol.
- Les mises en garde et contre-indications de la notice officielle (ANSM), pour un examen de sécurité.
- Une revue de la littérature ciblée sur le bisoprolol dans l'atteinte rénale hypertensive.
- Des études précliniques ou cliniques justifiant un éventuel intérêt par rapport aux traitements standards.

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: bisoprolol fumarate prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6517d564-ea55-4084-a8ab-34fea548c24e) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

