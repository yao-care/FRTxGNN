---
layout: default
title: Ganirelix
parent: Prédiction du modèle uniquement (L5)
nav_order: 356
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-04
monitor_inn: "ganirelix"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial male-limited precocious puberty", "persistent fetal circulation syndrome", "aromatase excess syndrome", "centra precocious puberty 1", "familial isolated trichomegaly"]
description: "Ganirelix : nouvelle indication prédite, Hypertrichose (hypertrichosis (disease)) (niveau de preuve L5). Indication d'origine : Non renseignée da…"
---

# Ganirelix
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Ganirelix: Hypertrichose (hypertrichosis (disease))
{: .text-alpha }

## Résumé en Une Phrase

Le ganirelix est un antagoniste du récepteur de la GnRH, utilisé dans la stimulation ovarienne lors des traitements de fertilité pour prévenir l'ovulation prématurée.
Le modèle TxGNN le prédit comme potentiellement efficace pour l'**hypertrichose**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hypertrichose (hypertrichosis (disease)) |
| Score de Prédiction TxGNN | 0.9998 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Ganirelix (traduction non officielle) : « La libération pulsatile de la GnRH stimule la synthèse et la sécrétion de l'hormone lutéinisante (LH) et de l'hormone folliculo-stimulante (FSH). La fréquence des pulses de LH au milieu et à la fin de la phase folliculaire est d'environ 1 pulse par heure. […] L'acétate de ganirelix agit en bloquant de manière compétitive les récepteurs de la GnRH sur les cellules gonadotropes hypophysaires et la voie de transduction qui en découle. » Texte original en anglais : "The pulsatile release of GnRH stimulates the synthesis and secretion of luteinizing hormone (LH) and follicle-stimulating hormone (FSH). The frequency of LH pulses in the mid and late follicular phase is approximately 1 pulse per hour. […] Ganirelix acetate acts by competitively blocking the GnRH receptors on the pituitary gonadotroph and subsequent transduction pathway." ([DailyMed: Fyremadel (ganirelix acetate) prescribing information, Ferring Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f0908b5-3551-47fd-95f7-3669b0dff7f1), version du 2026-10-16 ; consulté le 2026-11-19). Sur la base des informations connues, le ganirelix est un antagoniste peptidique du récepteur GnRH1 (gène GNRHR). Il freine la sécrétion de LH et de FSH, donc la production des stéroïdes sexuels gonadiques.

Le lien avec l'hypertrichose reste **spéculatif**. Une baisse des androgènes pourrait aider dans l'hirsutisme, mais l'hypertrichose vraie est en général indépendante des androgènes et non pilotée par l'axe hypophyso-gonadique. Le score très élevé de TxGNN provient du modèle TxGNN (apprentissage profond) et peut refléter des similitudes apprises par le modèle entre maladies apparentées, et non une preuve biologique.

Les autres prédictions du top 10 sont aussi sans soutien clinique (toutes en L5). Trois méritent d'être notées comme questions de recherche, car mécanistiquement plus cohérentes :
- **Puberté précoce centrale** (score 0,9975) : la modulation du récepteur GnRH est le principe thérapeutique établi, mais la formulation à courte durée d'action n'est pas adaptée à une suppression chronique.
- **Puberté précoce familiale limitée au sexe masculin** (0.9985) : la maladie est périphérique (mutation activatrice du récepteur LH), le ganirelix n'agirait que sur une éventuelle composante centrale secondaire.
- **Syndrome d'excès d'aromatase** (0.9980) : suppression hormonale adjuvante plausible, mais les inhibiteurs de l'aromatase sont l'approche directe.

Les autres prédictions (syndrome d'Ambras, malformation de Dandy-Walker, anomalies de la tige pilaire, trichomégalie familiale, circulation fœtale persistante, etc.) n'ont pas de plausibilité mécanistique identifiée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61125958 | GANIRELIX EG 0,25 mg/0,5 mL, solution injectable en seringue préremplie (active) | Solution injectable | Non renseignée |
| 62225235 | ORGALUTRAN 0,25 mg/0,5 mL, solution injectable (active) | Solution injectable | Non renseignée |
| 61462270 | FYREMADEL 0,25 mg/0,5 mL, solution injectable en seringue pré-remplie (active) | Solution injectable | Non renseignée |
| 62428488 | GANIRELIX THERAMEX 0,25 mg/0,5 mL, solution injectable en seringue pré-remplie (active) | Solution injectable | Non renseignée |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 6 interactions de niveau modéré sont recensées (source : DDInter) avec d'autres médicaments agissant sur l'axe gonadotrope : gonadoréline, gonadotrophine chorionique humaine, ménotropines, triptoréline, follitropine et urofollitropine.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'hypertrichose repose uniquement sur une prédiction du modèle (L5), sans essai, sans publication, et avec un lien mécanistique jugé spéculatif. Par ailleurs, le médicament est commercialisé en France, avec 4 AMM valides sur 4.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (mises en garde et contre-indications), indispensable avant tout examen de sécurité
- Obtenir les données détaillées sur le mécanisme d'action
- Mener une revue de littérature ciblée et rechercher des essais, en priorité pour la puberté précoce centrale, qui est l'hypothèse la plus cohérente
- Évaluer la compatibilité des voies d'administration et la pertinence d'une formulation à action prolongée pour une utilisation chronique

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Fyremadel (ganirelix acetate) prescribing information, Ferring Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f0908b5-3551-47fd-95f7-3669b0dff7f1) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

