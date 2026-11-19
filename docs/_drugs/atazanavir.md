---
layout: default
title: Atazanavir
parent: Prédiction du modèle uniquement (L5)
nav_order: 76
evidence_level: L5
indication_count: 4
monitor_inn: "ATAZANAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-11-20
description: "Atazanavir : nouvelle indication prédite, Syndrome d'immunodéficience acquise féline (feline acquired immunodeficiency syndrome) (niveau de preuve L5). Indication d'origine : Non renseignée dans les …"
---

# Atazanavir
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

## Atazanavir : inhibiteur de protéase du VIH → syndrome d'immunodéficience acquise féline (feline acquired immunodeficiency syndrome)
{: .text-alpha }

## Résumé en Une Phrase

L'atazanavir est un inhibiteur de protéase utilisé contre le VIH.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome d'immunodéficience acquise féline (feline acquired immunodeficiency syndrome)**,
mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Syndrome d'immunodéficience acquise féline (feline acquired immunodeficiency syndrome) |
| Score de Prédiction TxGNN | 0,9998 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon les rubriques « Mechanism of Action » et « Microbiology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Atazanavir (traduction non officielle) : « L'atazanavir est un médicament antirétroviral anti-VIH-1. […] L'atazanavir (ATV) est un inhibiteur azapeptidique de la protéase (IP) du VIH-1. Le composé inhibe sélectivement la maturation spécifique au virus des polyprotéines virales Gag et Gag-Pol dans les cellules infectées par le VIH-1, empêchant ainsi la formation de virions matures. » Texte original en anglais : "Atazanavir is an HIV-1 antiretroviral drug. […] Atazanavir (ATV) is an azapeptide HIV-1 protease inhibitor (PI). The compound selectively inhibits the virus-specific processing of viral Gag and Gag-Pol polyproteins in HIV-1-infected cells, thus preventing formation of mature virions." ([DailyMed: Reyataz (atazanavir) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=165cff62-b284-4a27-a65d-9ec8a5bfcdd8), version du 2024-12-05 ; consulté le 2026-11-19). Sur la base des informations connues, l'atazanavir fait partie des inhibiteurs de protéase du VIH, et pourrait, mécanistiquement, être applicable à une infection voisine.

Le virus de l'immunodéficience féline (FIV) est un lentivirus dont la protéase est apparentée à celle du VIH-1. Un inhibiteur de protéase comme l'atazanavir pourrait donc, en théorie, agir sur cette cible. Le score élevé du modèle reflète probablement cette similarité avec le VIH.

Ce lien reste purement hypothétique : aucune donnée expérimentale n'est disponible, et la pertinence vétérinaire ainsi que la faisabilité n'ont pas été examinées.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour cette indication.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69443966 | REYATAZ 150 mg, gélule | Gélule | Non renseignée |
| 68301348 | REYATAZ 200 mg, gélule | Gélule | Non renseignée |
| 66745660 | REYATAZ 300 mg, gélule | Gélule | Non renseignée |

## Considérations de Sécurité

- **Contre-indications relevées dans les données compilées** (hors texte de la notice, à confirmer) : insuffisance hépatique, maladie hépatique, maladie de la vésicule biliaire, hyperglycémie, diabète, acidocétose diabétique, hépatite C chronique, hépatite B chronique, hémophilie, hyperbilirubinémie (dont syndrome de Gilbert), néphrolithiase, néphropathie urique aiguë, bloc auriculo-ventriculaire, acidose lactique.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi celles de niveau majeur : famotidine, ranitidine, rabéprazole, oméprazole (antiacides/inhibiteurs de la sécrétion gastrique), lopéramide, triamcinolone, budésonide. Parmi celles de niveau modéré : acarbose, metformine, pioglitazone, hydrocortisone, bétaméthasone, aprépitant, hydroxyde d'aluminium, carbonate de calcium.

Veuillez consulter la notice pour les informations de sécurité complètes (mises en garde et contre-indications officielles non disponibles).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle, sans essai ni publication, et il s'agit d'une maladie vétérinaire sans lien clinique humain établi. Le niveau de preuve est L5.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action de l'atazanavir
- Études in vitro ou vétérinaires sur l'activité contre la protéase du FIV
- Évaluation de la pertinence vétérinaire et de la faisabilité (voie d'administration, tolérance chez le chat)
- Mises en garde et contre-indications issues de la notice officielle

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Reyataz (atazanavir) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=165cff62-b284-4a27-a65d-9ec8a5bfcdd8) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

