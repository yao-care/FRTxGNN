---
layout: default
title: Voxelotor
parent: Prédiction du modèle uniquement (L5)
nav_order: 822
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "voxelotor"
predicted_indications: ["hereditary thrombocytopenia with normal platelets", "marcothrombocytopenia with mitral valve insufficiency", "dense granule disease", "transient neonatal thrombocytopenia", "thrombocytopenia", "acquired monoclonal Ig light chain-associated Fanconi syndrome", "primary release disorder of platelets"]
description: "Voxelotor : nouvelle indication prédite, Hereditary thrombocytopenia with normal platelets (niveau de preuve L5). En France, aucune AMM dans la BDPM pour ces données"
---

# Voxelotor
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **7** 
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

## Voxelotor: Hereditary thrombocytopenia with normal platelets
{: .text-alpha }

## Résumé en Une Phrase

Voxelotor est un inhibiteur de la polymérisation de l'hémoglobine S, initialement utilisé pour le traitement de l'anémie falciforme.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **thrombopénie héréditaire avec plaquettes normales**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hereditary thrombocytopenia with normal platelets |
| Score de Prédiction TxGNN | 0.9958 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé (aucune autorisation enregistrée) |
| Nombre d'AMM | 0 (valides : 0) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Voxelotor (traduction non officielle) : « Le voxélotor est un inhibiteur de la polymérisation de l'hémoglobine S (HbS) qui se lie à l'HbS selon une stœchiométrie 1:1 et présente une distribution préférentielle dans les globules rouges (GR). En augmentant l'affinité de l'Hb pour l'oxygène, le voxélotor entraîne une inhibition dose-dépendante de la polymérisation de l'HbS. » Texte original en anglais : "Voxelotor is a hemoglobin S (HbS) polymerization inhibitor that binds to HbS with a 1:1 stoichiometry and exhibits preferential partitioning to red blood cells (RBCs). By increasing the affinity of Hb for oxygen, voxelotor demonstrates dose-dependent inhibition of HbS polymerization." ([DailyMed: Oxbryta (voxelotor) prescribing information, Global Blood Therapeutics, Inc, A subsidiary of Pfizer Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3c557fac-29ec-483f-b691-8a935d4decc3), version du 2023-12-26 ; consulté le 2026-11-19). Sur la base des informations connues, voxelotor est un inhibiteur de la polymérisation de l'hémoglobine S qui augmente l'affinité de l'hémoglobine pour l'oxygène. Son intérêt a été établi dans l'anémie falciforme, mais aucun lien mécanistique n'a pu être établi avec les troubles héréditaires du nombre de plaquettes.

Les maladies prédites (thrombopénies héréditaires, déficit en granules denses, troubles de la sécrétion plaquettaire) relèvent de défauts des mégacaryocytes ou des plaquettes, sans rapport évident avec la polymérisation de l'hémoglobine.

Les autres prédictions du modèle présentent la même faiblesse : thrombopénie macrocytaire avec insuffisance mitrale, maladie des granules denses, thrombopénie néonatale transitoire, thrombopénie (score 0,9951), syndrome de Fanconi associé à une chaîne légère monoclonale acquise et trouble primaire de la libération plaquettaire. Pour aucune d'elles, un mécanisme plausible n'a été identifié.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

## Considérations de Sécurité

**Interactions Médicamenteuses** : 130 interactions ont été répertoriées (source : DDInter). Parmi celles affichées, les plus importantes sont :

- **Majeures** : dexaméthasone, clarithromycine, éliglustat, naloxégol
- **Modérées** : hydrocortisone, aprépitant, triamcinolone, bétaméthasone, budésonide, saxagliptine, naldémédine, nitisinone, prednisone, répaglinide, simvastatine, tinidazole (ainsi que des formes ophtalmiques ou nasales de corticoïdes)

Ce profil évoque surtout des interactions métaboliques, notamment avec des inducteurs ou inhibiteurs enzymatiques. Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice auprès de l'ANSM (point bloquant pour le criblage de sécurité)
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Démontrer un lien biologique plausible entre l'affinité de l'hémoglobine pour l'oxygène et les troubles plaquettaires, par des données précliniques
- Clarifier la disponibilité du médicament en France et son statut réglementaire
- Envisager de prioriser des indications plus proches de l'indication d'origine (maladies de l'hémoglobine ou hémolytiques)

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Oxbryta (voxelotor) prescribing information, Global Blood Therapeutics, Inc, A subsidiary of Pfizer Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3c557fac-29ec-483f-b691-8a935d4decc3) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

