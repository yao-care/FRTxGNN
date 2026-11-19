---
layout: default
title: Amoxicillin
parent: Prédiction du modèle uniquement (L5)
nav_order: 61
evidence_level: L5
indication_count: 8
monitor_inn: "amoxicillin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-10-28
description: "Amoxicillin : nouvelle indication prédite, Hyperamylasémie (hyperamylasemia) (niveau de preuve L5). En France, AMM dans la BDPM : 15 (valides : 15)"
---

# Amoxicillin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Amoxicilline : bêta-lactamine bactéricide (inhibiteur de la synthèse de la paroi bactérienne) → hyperamylasémie (hyperamylasemia)
{: .text-alpha }

## Résumé en Une Phrase

L'amoxicilline est un antibiotique de la famille des bêta-lactamines, qui agit en bloquant la synthèse de la paroi des bactéries.
Le modèle TxGNN prédit qu'elle pourrait être utile pour l'**hyperamylasémie (hyperamylasemia)**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hyperamylasémie (hyperamylasemia) |
| Score de Prédiction TxGNN | 0,9963 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 15 sur 15) |
| Nombre d'AMM | 15 (valides : 15) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon les rubriques « Mechanism of Action » et « Microbiology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Amoxicillin (traduction non officielle) : « L'amoxicilline est un médicament antibactérien. […] L'amoxicilline est similaire à la pénicilline par son action bactéricide sur les bactéries sensibles pendant la phase de multiplication active. Elle agit par inhibition de la biosynthèse de la paroi cellulaire, ce qui entraîne la mort des bactéries. » Texte original en anglais : "Amoxicillin is an antibacterial drug. […] Amoxicillin is similar to penicillin in its bactericidal action against susceptible bacteria during the stage of active multiplication. It acts through the inhibition of cell wall biosynthesis that leads to the death of the bacteria." ([DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77), version du 2026-11-13 ; consulté le 2026-11-19). Sur la base des informations connues, l'amoxicilline est une bêta-lactamine bactéricide : elle inhibe la synthèse de la paroi bactérienne et agit donc sur des infections.

L'hyperamylasémie, elle, est une anomalie biologique (origine pancréatique, salivaire ou rénale) et non une maladie infectieuse. Aucun lien mécanistique plausible n'a été identifié entre l'action antibactérienne du médicament et cette anomalie.

Le score élevé du modèle (0,9963) reste donc une prédiction statistique isolée, qui ne repose sur aucune donnée clinique ou publiée. Elle doit être considérée comme une hypothèse très préliminaire, voire comme un artefact du modèle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les données compilées recensent 15 AMM, toutes de statut valide. Les 5 premières sont listées ci-dessous (les textes d'indication ne sont pas renseignés).

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 66918105 | AMOXICILLINE PANPHARMA 1 g, poudre pour solution injectable | Poudre pour solution injectable |
| 69915160 | AMOXICILLINE PANPHARMA 1 g/5 ml, poudre et solution pour solution injectable (IM) | Poudre et solution pour solution injectable |
| 69416855 | AMOXICILLINE PANPHARMA 2 g, poudre pour solution injectable | Poudre pour solution injectable |
| 61645058 | XYLLOMAC 500 mg, poudre pour solution injectable/pour perfusion (IM-IV) | Poudre pour solution injectable ou pour perfusion |
| 60271045 | XYLLOMAC 2 g, poudre pour solution injectable/pour perfusion (IV) | Poudre pour solution injectable ou pour perfusion |

## Considérations de Sécurité

- **Interactions médicamenteuses** : 271 interactions sont recensées. Parmi les principales :
  - **Majeures** : méthotrexate ; vaccin vivant contre le choléra (souche *Vibrio cholerae* CVD 103-HgR).
  - **Modérées** : doxycycline, minocycline, déméclocycline, éthinylestradiol, estradiol, anisindione, dicoumarol, balsalazide, entécavir, mycophénolate mofétil, certains probiotiques (*Lactobacillus acidophilus*, *Bifidobacterium longum infantis*) et l'indium In-111 oxyquinoline.
  - **Mineures** : allopurinol, amiloride, azithromycine, clarithromycine, érythromycine.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun lien mécanistique plausible n'existe entre l'amoxicilline et l'hyperamylasémie, et aucune étude ne l'a évaluée. Le niveau de preuve est L5 : la prédiction repose uniquement sur le modèle.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action et justification biologique d'un effet sur l'hyperamylasémie
- Études précliniques ou observationnelles évaluant directement cette association
- Récupération des mises en garde et contre-indications de la notice ANSM pour l'évaluation de la sécurité

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

