---
layout: default
title: Metoprolol
parent: Prédiction du modèle uniquement (L5)
nav_order: 492
evidence_level: L5
indication_count: 6
monitor_inn: "metoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "trichotillomania"]
last_modified_at: 2026-10-28
description: "Metoprolol : nouvelle indication prédite, Maladie rénale hypertensive maligne (malignant hypertensive renal disease) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données loca…"
---

# Metoprolol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Metoprolol: Maladie rénale hypertensive maligne (malignant hypertensive renal disease)
{: .text-alpha }

## Résumé en Une Phrase

Le métoprolol est un bêtabloquant cardiosélectif, utilisé à l'origine dans le traitement de l'hypertension artérielle et des maladies coronariennes (syndrome coronarien aigu, infarctus du myocarde).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie rénale hypertensive maligne**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Maladie rénale hypertensive maligne (malignant hypertensive renal disease) |
| Score de Prédiction TxGNN | 0.9991 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 14 sur 14) |
| Nombre d'AMM | 14 (valides : 14) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Metoprolol (traduction non officielle) : « Le métoprolol est un agent bloquant des récepteurs adrénergiques bêta 1 -sélectif (cardiosélectif). Cet effet préférentiel n'est toutefois pas absolu et, à des concentrations plasmatiques plus élevées, le métoprolol inhibe également les adrénorécepteurs bêta 2, situés principalement dans la musculature bronchique et vasculaire. » Texte original en anglais : "Metoprolol is a beta 1 -selective (cardioselective) adrenergic receptor blocking agent. This preferential effect is not absolute, however, and at higher plasma concentrations, metoprolol also inhibits beta 2 -adrenoreceptors, chiefly located in the bronchial and vascular musculature." ([DailyMed: Toprol Xl (metoprolol succinate) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=496ddfaa-7c9c-4888-b747-a210249b367a), version du 2026-03-03 ; consulté le 2026-11-19). D'après les connaissances générales, le métoprolol est un bêtabloquant bêta-1 sélectif : il diminue la fréquence cardiaque et la pression artérielle, et réduit la libération de rénine par le rein.

L'hypertension et la maladie rénale hypertensive maligne appartiennent au même spectre pathologique. Réduire la pression artérielle et la sécrétion de rénine est plausible dans une atteinte rénale hypertensive.

Cette prédiction reste toutefois fragile. L'hypertension maligne est une urgence, habituellement prise en charge par des antihypertenseurs intraveineux titrés ; le métoprolol oral n'est pas une option standard. Aucune donnée spécifique à cette maladie n'a été compilée.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Le métoprolol (substance seule) est commercialisé en France. Les données compilées recensent 14 AMM valides, toutes pour des produits à base de métoprolol seul, sans texte d'indication approuvée renseigné. Les 5 premières sont listées ci-dessous.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65340488 | SELOZOK LP 95 mg | Comprimé pelliculé à libération prolongée | Non renseignée dans les données compilées |
| 64930518 | METOPROLOL SANDOZ 50 mg | Comprimé | Non renseignée dans les données compilées |
| 66459997 | METOPROLOL VIATRIS 100 mg | Comprimé sécable | Non renseignée dans les données compilées |
| 68679426 | SELOKEN L P 200 mg | Comprimé à libération prolongée | Non renseignée dans les données compilées |
| 69376930 | LOPRESSOR L.P. 200 mg | Comprimé sécable à libération prolongée | Non renseignée dans les données compilées |

---

## Considérations de Sécurité

- **Contre-indications (relations enregistrées dans le graphe de connaissances, et non texte de notice)** : trouble anxieux, pancréatite, maladie hépatique, lupus érythémateux systémique, psoriasis, diabète sucré et acidocétose diabétique, hypotension, goutte, myasthénie grave, phéochromocytome, encéphalopathie hépatique, anurie, hyperparathyroïdie, entre autres.
- **Interactions médicamenteuses** : 338 interactions recensées. Parmi les principales, de niveau modéré : épinéphrine, corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), bupropion, morphine, cimétidine, atropine, canagliflozine, dapagliflozine, chlorpropamide ; de niveau mineur : acide acétylsalicylique, oxyde de magnésium.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai ni publication ne porte sur la maladie rénale hypertensive maligne. Cette urgence relève de traitements intraveineux titrés, et non du métoprolol oral.

**Pour avancer, les éléments suivants sont nécessaires :**
- Études cliniques ou observationnelles évaluant le métoprolol dans l'atteinte rénale hypertensive maligne
- Données sur le mécanisme d'action (MOA)
- Mises en garde et contre-indications officielles issues de la notice de l'ANSM
- Analyse de la compatibilité des voies d'administration (voie orale vs voie intraveineuse requise en urgence)

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Toprol Xl (metoprolol succinate) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=496ddfaa-7c9c-4888-b747-a210249b367a) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

