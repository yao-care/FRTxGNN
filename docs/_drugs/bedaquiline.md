---
layout: default
title: Bedaquiline
parent: Prédiction du modèle uniquement (L5)
nav_order: 91
evidence_level: L5
indication_count: 4
monitor_inn: "bedaquiline"
predicted_indications: ["vulvovaginal candidiasis", "fascioliasis", "urea cycle disorder", "esophageal candidiasis"]
last_modified_at: 2026-11-20
description: "Bedaquiline : nouvelle indication prédite, Candidose vulvovaginale (vulvovaginal candidiasis) (niveau de preuve L5). En France, AMM dans la BDPM : 1 (valides : 1)"
---

# Bedaquiline
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

## Bedaquiline : inhibiteur de l'ATP synthase mycobactérienne → candidose vulvovaginale (vulvovaginal candidiasis)
{: .text-alpha }

## Résumé en Une Phrase

La bédaquiline est un antibiotique antimycobactérien commercialisé en France sous le nom SIRTURO (comprimé).
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **candidose vulvovaginale (vulvovaginal candidiasis)**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Candidose vulvovaginale (vulvovaginal candidiasis) |
| Score de Prédiction TxGNN | 0,9988 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon les rubriques « Mechanism of Action » et « Microbiology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Bedaquiline (traduction non officielle) : « La bédaquiline est un médicament antimycobactérien de la classe des diarylquinoléines. […] SIRTURO est un médicament antimycobactérien de la classe des diarylquinoléines qui inhibe l'ATP (adénosine 5'-triphosphate) synthase mycobactérienne, en se liant à la sous-unité c de l'enzyme, essentielle à la production d'énergie chez M. tuberculosis. » Texte original en anglais : "Bedaquiline is a diarylquinoline antimycobacterial drug. […] SIRTURO is a diarylquinoline antimycobacterial drug that inhibits mycobacterial ATP (adenosine 5'- triphosphate) synthase, by binding to subunit c of the enzyme that is essential for the generation of energy in M. tuberculosis." ([DailyMed: Sirturo (bedaquiline fumarate) prescribing information, Janssen Products, LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1534c9ae-4948-4cf4-9f66-222a99db6d0e), version du 2025-10-17 ; consulté le 2026-11-19). D'après les connaissances générales, la bédaquiline cible l'ATP synthase des mycobactéries, une cible propre aux bactéries de ce groupe.

Aucun lien mécanistique clair n'a été établi avec la candidose vulvovaginale : la bédaquiline n'a pas d'activité antifongique démontrée. Le score élevé du modèle (0,9988) est vraisemblablement un artefact de prédiction, d'autant qu'aucun essai ni aucune publication ne le corrobore. La similarité avec l'indication d'origine n'a pas été évaluée à ce stade.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65690588 | SIRTURO 100 mg, comprimé | Comprimé | Non renseignée dans les données locales |

## Considérations de Sécurité

**Interactions médicamenteuses** : 226 interactions sont recensées dans les données compilées. Parmi celles de niveau majeur figurent :
- Dexaméthasone
- Clarithromycine
- Acide picosulfurique
- Polyéthylène glycol (3350 avec électrolytes)
- Dolasétron
- Palonosétron
- Sulfate de sodium

De nombreuses interactions de niveau modéré sont aussi listées (par exemple acarbose, famotidine, doxycycline, pioglitazone, lopéramide, bupropion, minocycline, tétracycline, naltrexone).

Veuillez consulter la notice pour les mises en garde et contre-indications.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible entre un antibiotique antimycobactérien et une infection fongique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action et démonstration d'une éventuelle activité antifongique (études in vitro)
- Mises en garde et contre-indications issues de la notice ANSM
- Études précliniques ou cliniques portant directement sur la candidose vulvovaginale

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Sirturo (bedaquiline fumarate) prescribing information, Janssen Products, LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1534c9ae-4948-4cf4-9f66-222a99db6d0e) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

