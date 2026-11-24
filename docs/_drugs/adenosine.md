---
layout: default
title: Adenosine
parent: Prédiction du modèle uniquement (L5)
nav_order: 28
evidence_level: L5
indication_count: 1
monitor_inn: "adenosine"
predicted_indications: ["obsolete bundle branch block"]
last_modified_at: 2026-11-24
description: "Adenosine : nouvelle indication prédite, Bloc de branche (obsolete bundle branch block) (niveau de preuve L5). En France, AMM dans la BDPM : 6 (valides : 4)"
---

# Adenosine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Adénosine : agent de ralentissement de la conduction auriculo-ventriculaire → bloc de branche (obsolete bundle branch block)
{: .text-alpha }

## Résumé en Une Phrase

L'adénosine est un médicament administré par voie injectable, dont la fiche de mécanisme détaillée n'est pas disponible dans les données compilées pour ce rapport.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **bloc de branche (obsolete bundle branch block)**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Bloc de branche (obsolete bundle branch block) |
| Score de Prédiction TxGNN | 0,9994 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 6) |
| Nombre d'AMM | 6 (valides : 4) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Adenosine (traduction non officielle) : « L'adénosine injectable ralentit le temps de conduction à travers le nœud auriculo-ventriculaire, peut interrompre les voies de réentrée passant par le nœud auriculo-ventriculaire et peut rétablir un rythme sinusal normal chez les patients atteints de tachycardie supraventriculaire paroxystique (TSVP), y compris la TSVP associée au syndrome de Wolff-Parkinson-White. L'adénosine injectable est antagonisée de manière compétitive par les méthylxanthines telles que la caféine et la théophylline, et potentialisée par les inhibiteurs du transport des nucléosides tels que le dipyridamole. » Texte original en anglais : "Adenosine Injection slows conduction time through the A-V node, can interrupt the reentry pathways through the A-V node, and can restore normal sinus rhythm in patients with paroxysmal supraventricular tachycardia (PSVT), including PSVT associated with Wolff-Parkinson-White Syndrome. Adenosine Injection is antagonized competitively by methylxanthines such as caffeine and theophylline, and potentiated by blockers of nucleoside transport such as dipyridamole." ([DailyMed: adenosine prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9508caf5-0e3a-4d32-909d-bff7ea40ec30), version du 2026-08-31 ; consulté le 2026-11-19). Sur la base des informations connues, l'adénosine est connue pour ralentir la conduction du nœud auriculo-ventriculaire, ce qui est le principe de son usage dans certains troubles du rythme.

Le lien avec un bloc de branche est toutefois peu plausible. Le bloc de branche est un défaut de conduction situé en aval du nœud (système de His-Purkinje), que l'adénosine n'est pas censée corriger ; elle pourrait même aggraver des troubles de conduction. Le terme de la maladie est en outre signalé comme obsolète, ce qui suggère un artefact d'ontologie plutôt qu'une piste thérapeutique réelle.

Le score élevé (0,9994, rang 1161) traduit une prédiction purement computationnelle, sans justification mécanistique étayée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 67537114 | ADENOSINE HIKMA 6 mg/2 mL, solution injectable | Solution injectable | HIKMA FARMACEUTICA (PORTUGAL) | Active |
| 61855583 | ADENOSCAN 30 mg/10 mL, solution pour perfusion | Solution pour perfusion | SANOFI WINTHROP INDUSTRIE | Active |
| 60710318 | KRENOSIN 6 mg/2 ml, solution injectable | Solution injectable | SANOFI WINTHROP INDUSTRIE | Active |
| 63052537 | ADENOSINE MEDISOL 6 mg/2 ml, solution injectable | Solution injectable | MEDISOL | Active |
| 62967603 | ADENOSINE ACCORD 30 mg/10 ml, solution pour perfusion | Solution pour perfusion | ACCORD HEALTHCARE FRANCE | Abrogée |
| 68352264 | ADENOSINE ACCORD 6 mg/2 ml, solution injectable | Solution injectable | ACCORD HEALTHCARE FRANCE | Abrogée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 138 interactions recensées. Les interactions de niveau majeur incluent le cisapride, le dolasétron et la papavérine. Parmi les interactions de niveau modéré figurent la famotidine, la clarithromycine, le granisétron, la lévofloxacine, l'ondansétron et le palonosétron. Plusieurs de ces médicaments sont associés à un allongement de l'intervalle QT ou à des effets sur la conduction cardiaque.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Etapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle, sans essai ni publication, et le mécanisme de l'adénosine (ralentissement de la conduction nodale) ne soutient pas un effet bénéfique sur un bloc de branche. Le terme de maladie obsolète laisse penser à un artefact.

**Pour avancer, les elements suivants sont necessaires :**
- Clarifier la correspondance du terme obsolète avec un concept actuel de trouble de la conduction
- Données détaillées sur le mécanisme d'action
- Mises en garde et contre-indications issues de la notice ANSM
- Toute étude clinique ou publication portant directement sur cette maladie avant de reconsidérer la décision

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: adenosine prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9508caf5-0e3a-4d32-909d-bff7ea40ec30) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

