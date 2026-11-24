---
layout: default
title: Clotrimazole
parent: Prédiction du modèle uniquement (L5)
nav_order: 191
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "CLOTRIMAZOLE"
predicted_indications: ["acne (disease)", "postmenopausal atrophic vaginitis"]
description: "Clotrimazole : nouvelle indication prédite, acné (acne (disease)) (niveau de preuve L5). En France, AMM dans la BDPM : 6 (valides : 6)"
---

# Clotrimazole
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

## Clotrimazole: acné (acne (disease))
{: .text-alpha }

## Résumé en Une Phrase

Le clotrimazole est un antifongique azolé à usage local, commercialisé en France sous forme de crèmes et de comprimés ou capsules vaginaux.
Le modèle TxGNN prédit qu'il pourrait être utile dans l'**acné (acne (disease))**, avec un score de 0.9986.
Les preuves restent très minces : **1 essai clinique** (une association de trois médicaments, suspendu) et **aucune publication**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | acné (acne (disease)) |
| Score de Prédiction TxGNN | 0.9986 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 6 sur 6) |
| Nombre d'AMM | 6 (valides : 6) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Clotrimazole (traduction non officielle) : « Le clotrimazole est un agent antifongique à large spectre qui inhibe la croissance des levures pathogènes en modifiant la perméabilité des membranes cellulaires. L'action du clotrimazole est fongistatique à des concentrations de médicament allant jusqu'à 20 mcg/mL et peut être fongicide in vitro contre Candida albicans et d'autres espèces du genre Candida à des concentrations plus élevées. » Texte original en anglais : "Clotrimazole is a broad-spectrum antifungal agent that inhibits the growth of pathogenic yeasts by altering the permeability of cell membranes. The action of clotrimazole is fungistatic at concentrations of drug up to 20 mcg/mL and may be fungicidal in vitro against Candida albicans and other species of the genus Candida at higher concentrations." ([DailyMed: clotrimazole prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=980736aa-751a-4642-ab85-a309435fd02f), version du 2025-03-27 ; consulté le 2026-11-19). D'après les connaissances générales, le clotrimazole est un antifongique azolé qui inhibe la synthèse de l'ergostérol fongique (enzyme CYP51). Des activités antibactérienne et anti-inflammatoire ont aussi été décrites.

Ces propriétés pourraient avoir un lien avec la physiopathologie de l'acné (implication de *Cutibacterium acnes* et de *Malassezia*, inflammation). Ce lien reste toutefois indirect et hypothétique.

Le seul essai identifié teste une association fixe (bêclométasone + gentamicine + clotrimazole) : aucun effet ne peut être attribué au clotrimazole seul. Le score élevé est un résultat de calcul du modèle, non étayé par des preuves cliniques ou bibliographiques. Aucun essai ni publication n'étudie directement l'acné avec le clotrimazole seul ; le niveau de preuve est donc L5.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspendu | 80 | Efficacité comparée d'une crème associant clotrimazole, gentamicine et bêclométasone dans des dermatoses surinfectées avec lésions bilatérales symétriques. Association de plusieurs médicaments : pertinence faible pour le clotrimazole seul, et indication « acné » peu claire. |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 67301480 | MYCOHYDRALIN 200 mg, comprimé vaginal | Comprimé | BAYER HEALTHCARE | Active |
| 62633525 | CLOTRIMAZOLE EG LABO CONSEIL 1%, crème | Crème | EG LABO - LABORATOIRES EUROGENERICS | Active |
| 67933494 | MYCOHYDRALIN 500 mg, comprimé vaginal | Comprimé | BB FARMA (ITALIE) | Active |
| 67777579 | MYCOHYDRALIN, crème | Crème | BAYER HEALTHCARE | Active |
| 60070359 | MYCOHYDRALIN 500 mg, capsule vaginale | Capsule | BAYER HEALTHCARE | Active |
| 68001621 | MYCOHYDRALIN 500 mg, comprimé vaginal | Comprimé | BAYER HEALTHCARE | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

Le clotrimazole est commercialisé en France ; les 6 AMM recensées sont valides.

## Considérations de Sécurité

- **Interactions médicamenteuses** : 100 interactions sont recensées. Parmi celles de niveau majeur figurent le fentanyl, l'alfentanil, l'amiodarone et l'hydrocodone. Des interactions de niveau modéré concernent notamment l'abémaciclib, le paclitaxel, l'acalabrutinib, la nifédipine, le lévonorgestrel, l'estradiol, l'alprazolam, la noréthistérone, l'amlodipine, l'apixaban et l'aprépitant.
- Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Etapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle. Le seul essai est suspendu et porte sur une association de médicaments, sans publication à l'appui.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des études (précliniques ou cliniques) évaluant le clotrimazole seul dans l'acné
- Les données détaillées sur le mécanisme d'action
- Les mises en garde et contre-indications issues de la notice officielle
- Une évaluation de la voie d'administration et de la tolérance cutanée pour cet usage

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: clotrimazole prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=980736aa-751a-4642-ab85-a309435fd02f) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

