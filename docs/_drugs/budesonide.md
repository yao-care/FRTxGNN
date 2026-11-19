---
layout: default
title: Budesonide
parent: Prédiction du modèle uniquement (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
monitor_inn: "budesonide"
predicted_indications: ["atopic eczema", "bronchitis", "dermatitis, atopic", "polyp of vocal cord", "polyp of middle ear", "epulis", "fibroepithelial polyp", "uterine polyp", "polyp of frontal sinus", "polyp of external auditory canal"]
last_modified_at: 2026-11-20
description: "Budesonide : nouvelle indication prédite, Eczéma atopique (atopic eczema) (niveau de preuve L5). En France, AMM dans la BDPM : au moins 20"
---

# Budesonide
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

## Budésonide : corticoïde à action anti-inflammatoire → Eczéma atopique (atopic eczema)
{: .text-alpha }

## Résumé en Une Phrase

La budésonide est un glucocorticoïde à large activité anti-inflammatoire et immunosuppressive, disponible en France sous de nombreuses formes (inhalation, voie nasale, voie orale).
Le modèle TxGNN prédit qu'elle pourrait être utile dans l'**eczéma atopique (atopic eczema)**, avec un score de 0,9996.
Aucun essai clinique ni aucune publication ne soutient actuellement cette prédiction précise : elle repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Eczéma atopique (atopic eczema) |
| Score de Prédiction TxGNN | 0,9996 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 19) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Budesonide (traduction non officielle) : « Le budésonide est un corticostéroïde anti-inflammatoire qui présente une activité glucocorticoïde puissante et une activité minéralocorticoïde faible. Dans des modèles standard in vitro et chez l'animal, le budésonide présente une affinité pour le récepteur des glucocorticoïdes environ 200 fois supérieure et une puissance anti-inflammatoire topique 1000 fois supérieure à celles du cortisol (test de l'œdème de l'oreille induit par l'huile de croton chez le rat). » Texte original en anglais : "Budesonide is an anti-inflammatory corticosteroid that exhibits potent glucocorticoid activity and weak mineralocorticoid activity. In standard in vitro and animal models, budesonide has approximately a 200-fold higher affinity for the glucocorticoid receptor and a 1000-fold higher topical anti-inflammatory potency than cortisol (rat croton oil ear edema assay)." ([DailyMed: Budesonide Inhalation Suspension (budesonide) prescribing information, Cipla USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c52c5382-1400-44b9-95be-a30e1cf706da), version du 2026-06-10 ; consulté le 2026-11-19). Sur la base des connaissances générales, la budésonide est un glucocorticoïde : elle freine l'inflammation et la réponse immunitaire, notamment la production de cytokines inflammatoires.

L'eczéma atopique est une inflammation cutanée chronique, largement liée à une réponse immunitaire de type Th2. Une molécule anti-inflammatoire et immunosuppressive est donc, sur le plan biologique, plausible dans cette maladie.

Cette plausibilité reste toutefois théorique. Le score élevé du modèle est une prédiction et ne remplace pas des données cliniques, qui sont absentes ici.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'eczéma atopique (atopic eczema) en tant que tel.

## Informations de Marché en France

Les données compilées signalent un statut de marché « commercialisé ». Les autorisations de mise sur le marché recensées sont des spécialités à base de budésonide seule, sous plusieurs formes : suspension pour nébuliseur, poudre pour inhalation, solution pour inhalation, spray nasal, comprimé orodispersible, gélules gastro-résistantes ou à libération modifiée et comprimé à libération prolongée. La liste fournie est partielle et ne mentionne pas de formulation cutanée.

## Considérations de Sécurité

- **Interactions médicamenteuses** : 599 interactions sont recensées. Parmi celles listées, certaines sont de niveau majeur, notamment avec l'adalimumab et le fosamprénavir. D'autres, de niveau modéré, concernent par exemple l'ibuprofène, le kétorolac, la nifédipine, la fluvoxamine et l'isotrétinoïne.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations de sécurité.

## Conclusion et Prochaines Etapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication étudiant directement l'eczéma atopique avec la budésonide. Les données de sécurité de la notice sont également manquantes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action
- Études cliniques évaluant la budésonide dans l'eczéma atopique, avec une voie d'administration adaptée (cutanée)
- Mises en garde et contre-indications issues de la notice (ANSM)
- Évaluation du risque d'allergie de contact aux corticoïdes, la budésonide étant un sensibilisant connu

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Budesonide Inhalation Suspension (budesonide) prescribing information, Cipla USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c52c5382-1400-44b9-95be-a30e1cf706da) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

