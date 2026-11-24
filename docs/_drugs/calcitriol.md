---
layout: default
title: Calcitriol
parent: Prédiction du modèle uniquement (L5)
nav_order: 131
evidence_level: L5
indication_count: 5
monitor_inn: "CALCITRIOL"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "hereditary hypophosphatemic rickets"]
last_modified_at: 2026-11-24
description: "Calcitriol : nouvelle indication prédite, Carence en vitamine D obsolète (obsolete vitamin D deficiency) (niveau de preuve L5). En France, AMM dans la BDPM : 2 (valides : 2)"
---

# Calcitriol
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **5** 
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

## Calcitriol : analogue actif de la vitamine D (agoniste du récepteur de la vitamine D) → carence en vitamine D obsolète (obsolete vitamin D deficiency)
{: .text-alpha }

## Résumé en Une Phrase

Le calcitriol est la forme active de la vitamine D, un régulateur du métabolisme du calcium et du phosphore.
Le modèle TxGNN prédit qu'il pourrait être utile pour la **carence en vitamine D obsolète (obsolete vitamin D deficiency)**, avec un score de 0,9996.
Aucun essai clinique ni aucune publication ne soutient actuellement cette prédiction précise : elle repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Carence en vitamine D obsolète (obsolete vitamin D deficiency) |
| Score de Prédiction TxGNN | 0,9996 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Calcitriol (traduction non officielle) : « La synthèse et le catabolisme endogènes du calcitriol, ainsi que les mécanismes de contrôle physiologiques qui influent sur ces processus, jouent un rôle essentiel dans la régulation de la concentration sérique de calcitriol. La production quotidienne physiologique est normalement de 0,5 à 1,0 mcg et est légèrement plus élevée pendant les périodes de synthèse osseuse accrue (p. ex., croissance ou grossesse). » Texte original en anglais : "Endogenous synthesis and catabolism of calcitriol, as well as physiological control mechanisms affecting these processes, play a critical role regulating the serum level of calcitriol. Physiological daily production is normally 0.5 to 1.0 mcg and is somewhat higher during periods of increased bone synthesis (eg, growth or pregnancy)." ([DailyMed: calcitriol prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=45f78bbe-4bbc-404d-a061-ead3db50908e), version du 2026-10-15 ; consulté le 2026-11-19). Le calcitriol est connu comme la forme active (1,25-dihydroxy) de la vitamine D, qui agit via le récepteur de la vitamine D présent dans de nombreux tissus. Un traitement de remplacement dans une carence en vitamine D est donc plausible sur le plan mécanistique.

Cette prédiction appelle toutefois une grande prudence. L'entrée de maladie correspondante est classée comme obsolète dans l'ontologie, et le score élevé reflète probablement une proximité avec des indications déjà liées à la vitamine D plutôt qu'une preuve réelle. De plus, la carence en vitamine D est en pratique corrigée par la vitamine D native (cholécalciférol, ergocalciférol) et non par le calcitriol.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les données compilées pour ce rapport recensent deux autorisations de mise sur le marché pour des produits à base de calcitriol seul, sans texte d'indication enregistré :

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 61847953 | ROCALTROL 0,25 microgramme, capsule molle | Capsule molle | ATNAHS PHARMA NETHERLANDS (PAYS-BAS) | Active |
| 62597239 | SILKIS 3 microgrammes/g, pommade | Pommade | GALDERMA INTERNATIONAL | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Interactions médicamenteuses** (100 interactions recensées ; principales ci-dessous) :
  - Majeures : cholécalciférol, burosumab, calcifédiol.
  - Modérées : fosphénytoïne, carbamazépine, hydrochlorothiazide et autres diurétiques thiazidiques, barbituriques (amobarbital, butalbital, butabarbital), calcipotriol topique, hydroxyde d'aluminium, colestyramine, colesevelam, colestipol, digoxine, digitoxine.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication directe, et l'entrée de maladie est obsolète. La carence en vitamine D est par ailleurs habituellement traitée par la vitamine D native.

**Pour avancer, les éléments suivants sont nécessaires :**
- Clarifier la correspondance de l'entrée obsolète avec une maladie actuelle (par exemple carence ou résistance à la vitamine D, rachitisme).
- Données sur le mécanisme d'action.
- Mises en garde et contre-indications issues de la notice ANSM.
- Études cliniques comparant le calcitriol à la vitamine D native dans cette situation.

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: calcitriol prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=45f78bbe-4bbc-404d-a061-ead3db50908e) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

