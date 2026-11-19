---
layout: default
title: Avelumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 83
evidence_level: L5
indication_count: 9
monitor_inn: "avelumab"
predicted_indications: ["human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "adenosine deaminase deficiency", "reticular dysgenesis", "Immunoerythromyeloid hypoplasia", "non-severe combined immunodeficiency", "kidney pelvis sarcomatoid transitional cell carcinoma"]
last_modified_at: 2026-11-20
description: "Avelumab : nouvelle indication prédite, Tumeur liée à l'herpèsvirus humain 8 (human herpesvirus 8-related tumor) (niveau de preuve L5). En France, AMM dans la BDPM : 1 (valides : 1)"
---

# Avelumab
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

## Avelumab : anticorps anti-PD-L1 → Tumeur liée à l'herpèsvirus humain 8 (human herpesvirus 8-related tumor)
{: .text-alpha }

## Résumé en Une Phrase

L'avelumab est un anticorps monoclonal anti-PD-L1 (inhibiteur de point de contrôle immunitaire).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **tumeur liée à l'herpèsvirus humain 8 (human herpesvirus 8-related tumor)**,
mais **aucun essai clinique ni publication** n'est actuellement disponible pour soutenir cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Tumeur liée à l'herpèsvirus humain 8 (human herpesvirus 8-related tumor) |
| Score de Prédiction TxGNN | 0,9997 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Avelumab (traduction non officielle) : « PD-L1 peut être exprimé sur les cellules tumorales et sur les cellules immunitaires infiltrant la tumeur, et peut contribuer à l'inhibition de la réponse immunitaire antitumorale dans le microenvironnement tumoral. La liaison de PD-L1 aux récepteurs PD-1 et B7.1 présents sur les lymphocytes T et les cellules présentatrices d'antigène supprime l'activité des lymphocytes T cytotoxiques, la prolifération des lymphocytes T et la production de cytokines. […] L'avélumab se lie à PD-L1 et bloque l'interaction entre PD-L1 et ses récepteurs PD-1 et B7.1. » Texte original en anglais : "PD-L1 may be expressed on tumor cells and tumor-infiltrating immune cells and can contribute to the inhibition of the anti-tumor immune response in the tumor microenvironment. Binding of PD-L1 to the PD-1 and B7.1 receptors found on T cells and antigen presenting cells suppresses cytotoxic T-cell activity, T-cell proliferation, and cytokine production. […] Avelumab binds PD-L1 and blocks the interaction between PD-L1 and its receptors PD-1 and B7.1." ([DailyMed: Bavencio (avelumab) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5cd725a1-2fa4-408a-a651-57a7b84b2118), version du 2026-09-22 ; consulté le 2026-11-19). Sur la base des informations connues, l'avelumab est un anticorps dirigé contre PD-L1, qui lève le frein exercé sur les lymphocytes T par cette voie de contrôle immunitaire.

Les tumeurs liées à l'herpèsvirus humain 8 (par exemple le sarcome de Kaposi ou le lymphome primitif des séreuses) impliquent une échappée immunitaire d'origine virale et une possible surexpression de la voie PD-L1/PD-1. Un blocage de ce point de contrôle est donc biologiquement plausible.

Cependant, aucun essai ni publication n'a été fourni : le lien repose uniquement sur le score de prédiction et sur un raisonnement mécanistique général. Il s'agit d'une hypothèse à vérifier, non d'un résultat démontré.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60199966 | BAVENCIO 20 mg/mL, solution à diluer pour perfusion | Solution à diluer pour perfusion | Non renseignée dans les données locales |

## Considérations de Sécurité

**Interactions médicamenteuses** (niveau majeur) :
- Lénalidomide
- Pomalidomide
- Thalidomide

Veuillez consulter la notice pour les autres informations de sécurité (mises en garde et contre-indications).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (0,9997) et un raisonnement mécanistique général, sans aucun essai ni publication étudiant cette maladie. Le niveau de preuve est L5.

**Pour avancer, les éléments suivants sont nécessaires :**
- Recherche et analyse d'études (séries de cas, essais) de blocage PD-L1/PD-1 dans les tumeurs liées à l'HHV-8
- Données détaillées sur le mécanisme d'action
- Mises en garde et contre-indications issues de la notice ANSM
- Évaluation de la sécurité des associations avec les immunomodulateurs (lénalidomide, pomalidomide, thalidomide)

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Bavencio (avelumab) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5cd725a1-2fa4-408a-a651-57a7b84b2118) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

