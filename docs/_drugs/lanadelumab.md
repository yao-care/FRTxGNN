---
layout: default
title: Lanadelumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 434
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "lanadelumab"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "pancreatitis", "pseudo-von Willebrand disease", "primary release disorder of platelets", "immune-mediated necrotizing myopathy", "Glanzmann thrombasthenia", "antisynthetase syndrome", "focal myositis", "Scott syndrome"]
description: "Lanadelumab : nouvelle indication prédite, Serpinopathie avec polymérisation toxique des serpines (serpinopathy with toxic serpin polymerization) (niveau de preuve L5)."
---

# Lanadelumab
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

## Lanadelumab: Serpinopathie avec polymérisation toxique des serpines (serpinopathy with toxic serpin polymerization)
{: .text-alpha }

## Résumé en Une Phrase

Lanadelumab est un anticorps monoclonal qui inhibe la kallikréine plasmatique (KLKB1).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **serpinopathie avec polymérisation toxique des serpines (serpinopathy with toxic serpin polymerization)**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Serpinopathie avec polymérisation toxique des serpines (serpinopathy with toxic serpin polymerization) |
| Score de Prédiction TxGNN | 0.9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Lanadelumab (traduction non officielle) : « Le lanadelumab-flyo est un anticorps monoclonal entièrement humain (IgG1/chaîne légère κ) qui se lie à la kallicréine plasmatique et inhibe son activité protéolytique. La kallicréine plasmatique est une protéase qui clive le kininogène de haut poids moléculaire (HMWK) pour générer du HMWK clivé (cHMWK) et de la bradykinine, un puissant vasodilatateur qui augmente la perméabilité vasculaire, entraînant le gonflement et la douleur associés à l'AOH. » Texte original en anglais : "Lanadelumab-flyo is a fully human monoclonal antibody (IgG1/κ-light chain) that binds plasma kallikrein and inhibits its proteolytic activity. Plasma kallikrein is a protease that cleaves high-molecular-weight-kininogen (HMWK) to generate cleaved HMWK (cHMWK) and bradykinin, a potent vasodilator that increases vascular permeability resulting in swelling and pain associated with HAE." ([DailyMed: Takhzyro (lanadelumab-flyo) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=15f99d8c-efe7-4f7d-aa20-0d0f1e30c6e8), version du 2026-09-18 ; consulté le 2026-11-19). D'après les informations pharmacologiques connues, lanadelumab cible la kallikréine plasmatique (gène KLKB1) et bloque ainsi l'axe kallikréine-bradykinine.

Le lien évoqué par le modèle semble reposer sur une biologie commune des serpines (par exemple SERPING1 et l'inhibiteur de la C1 estérase). Or la polymérisation toxique des serpines est un mécanisme de protéotoxicité, et non un mécanisme dépendant de la kallikréine. Inhiber la kallikréine plasmatique n'a donc pas de justification claire dans cette maladie.

Cette prédiction doit être considérée comme une hypothèse purement computationnelle, sans appui clinique ni mécanistique démontré.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Lanadelumab est commercialisé en France. Le statut des AMM recensées figure dans l'Aperçu rapide et dans le tableau ci-dessous.

<!-- review:begin fr-lic-20261124-lanadelumab-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les trois AMM recensées sont valides. » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans l'Aperçu rapide. Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés : le nombre et le statut à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché, générés à partir des données BDPM. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-lanadelumab-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 63473155 | TAKHZYRO 300 mg, solution injectable en seringue préremplie | Solution injectable | TAKEDA PHARMACEUTICALS INTERNATIONAL (IRLANDE) | Active |
| 61988861 | TAKHZYRO 300 mg, solution injectable | Solution injectable | TAKEDA PHARMACEUTICALS INTERNATIONAL (IRLANDE) | Active |
| 67650090 | TAKHZYRO 150 mg, solution injectable en seringue préremplie | Solution injectable | TAKEDA PHARMACEUTICALS INTERNATIONAL (IRLANDE) | Active |
| 61865798 | TAKHZYRO 300 mg, solution injectable en stylo prérempli | Solution injectable | TAKEDA PHARMACEUTICALS INTERNATIONAL (IRLANDE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Interactions Médicamenteuses** : une seule interaction de nature pharmacologique est répertoriée, avec la kallikréine B1 (KLKB1), cible du lanadelumab. Il s'agit de l'interaction avec sa cible thérapeutique et non d'une interaction médicamenteuse cliniquement graduée.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (score 0,9999), sans essai clinique, sans publication et sans lien mécanistique plausible entre l'inhibition de la kallikréine plasmatique et la polymérisation toxique des serpines.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA)
- Mises en garde et contre-indications issues de la notice de l'ANSM
- Études précliniques démontrant un rôle de la kallikréine plasmatique dans cette pathologie
- Évaluation de la pertinence biologique avant toute étude clinique

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Takhzyro (lanadelumab-flyo) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=15f99d8c-efe7-4f7d-aa20-0d0f1e30c6e8) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

