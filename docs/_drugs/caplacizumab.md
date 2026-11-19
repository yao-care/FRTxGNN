---
layout: default
title: Caplacizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 136
evidence_level: L5
indication_count: 9
monitor_inn: "CAPLACIZUMAB"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "hemophilia", "platelet-type bleeding disorder"]
last_modified_at: 2026-11-20
description: "Caplacizumab : nouvelle indication prédite, Trouble de la libération primaire des plaquettes (primary release disorder of platelets) (niveau de preuve L5). Indication d'origine : Non renseignée dans …"
---

# Caplacizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Caplacizumab : inhibiteur du facteur von Willebrand (liaison vWF-GPIb) → trouble de la libération primaire des plaquettes (primary release disorder of platelets)
{: .text-alpha }

## Résumé en Une Phrase

Le caplacizumab est un nanocorps dirigé contre le facteur von Willebrand, qui bloque l'interaction entre ce facteur et les plaquettes.
Le modèle TxGNN le prédit comme potentiellement efficace pour le **trouble de la libération primaire des plaquettes (primary release disorder of platelets)**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction. La prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Trouble de la libération primaire des plaquettes (primary release disorder of platelets) |
| Score de Prédiction TxGNN | 0,9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Caplacizumab (traduction non officielle) : « Le caplacizumab-yhdp cible le domaine A1 du vWF et inhibe l'interaction entre le vWF et les plaquettes, réduisant ainsi à la fois l'adhésion plaquettaire médiée par le vWF et la consommation de plaquettes. » Texte original en anglais : "Caplacizumab-yhdp targets the A1-domain of vWF, and inhibits the interaction between vWF and platelets, thereby reducing both vWF-mediated platelet adhesion and platelet consumption." ([DailyMed: Cablivi (caplacizumab) prescribing information, Genzyme Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2348f06e-8004-4040-832e-e9e86a39f905), version du 2026-04-24 ; consulté le 2026-11-19). D'après les connaissances générales, le caplacizumab se fixe sur le domaine A1 du facteur von Willebrand et empêche son interaction avec le récepteur plaquettaire GPIb.

Ce mécanisme réduit l'adhésion plaquettaire. Or, dans un trouble de la fonction plaquettaire, l'hémostase primaire est déjà altérée. Un bénéfice thérapeutique est donc mécanistiquement peu plausible : le médicament risquerait plutôt d'aggraver la tendance hémorragique.

Le score élevé du modèle reflète probablement la proximité de termes liés aux plaquettes plutôt qu'une réelle plausibilité thérapeutique. Cette prédiction doit être considérée comme une hypothèse non étayée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64183564 | CABLIVI 10 mg, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | Non renseignée |

Les données locales font état d'une seule AMM, dont l'enregistrement est partiel ou non détaillé quant au texte d'indication.

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions sont recensées. Parmi celles listées, plusieurs sont de niveau **majeur**, notamment avec :
  - l'acide acétylsalicylique,
  - le fondaparinux,
  - l'alteplase,
  - l'abciximab,
  - l'anagrélide,
  - l'acalabrutinib,
  - le déférasirox,
  - l'ibritumomab tiuxétan, le tositumomab (avec ou sans iode 131) et le trastuzumab emtansine.

  Des interactions de niveau **modéré** sont également signalées, notamment avec l'ibuprofène, le kétorolac, le célécoxib, le diclofénac topique, la fluvoxamine, la fenfluramine, la dexfenfluramine et la sibutramine.

  La plupart de ces associations concernent des médicaments qui affectent l'hémostase, ce qui suggère un risque hémorragique additionnel.

- **Risque propre à l'indication prédite** : le blocage de l'interaction vWF-plaquettes pourrait aggraver le saignement chez des patients dont la fonction plaquettaire est déjà altérée.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication portant sur cette maladie. Le mécanisme d'action du caplacizumab va à l'encontre d'un bénéfice attendu et accroît le risque hémorragique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données mécanistiques précliniques montrant une plausibilité thérapeutique dans ce trouble plaquettaire
- Données détaillées sur le mécanisme d'action
- Mises en garde et contre-indications issues de la notice de l'ANSM
- Évaluation du rapport bénéfice/risque hémorragique avant toute étude clinique

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Cablivi (caplacizumab) prescribing information, Genzyme Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2348f06e-8004-4040-832e-e9e86a39f905) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

