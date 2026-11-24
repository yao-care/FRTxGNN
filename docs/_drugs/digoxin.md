---
layout: default
title: Digoxin
parent: Prédiction du modèle uniquement (L5)
nav_order: 241
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "digoxin"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "hypoalphalipoproteinemia"]
description: "Digoxin : nouvelle indication prédite, Angor de Prinzmetal (Prinzmetal angina) (niveau de preuve L5). En France, AMM dans la BDPM : 4 (valides : 4)"
---

# Digoxin
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

## Digoxin: Angor de Prinzmetal (Prinzmetal angina)
{: .text-alpha }

## Résumé en Une Phrase

La digoxine est un glycoside cardiotonique, initialement utilisé pour traiter la fibrillation auriculaire et l'intoxication digitalique.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**angor de Prinzmetal**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction issue du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Angor de Prinzmetal (Prinzmetal angina) |
| Score de Prédiction TxGNN | 0.9981 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 4 sur 4) |
| Nombre d'AMM | 4 (valides : 4) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Digoxin (traduction non officielle) : « Toutes les actions de la digoxine sont médiées par ses effets sur la Na-K ATPase. Cette enzyme, la « pompe à sodium », est responsable du maintien du milieu intracellulaire dans l'ensemble de l'organisme en faisant sortir les ions sodium des cellules et entrer les ions potassium dans celles-ci. » Texte original en anglais : "All of digoxin’s actions are mediated through its effects on Na-K ATPase. This enzyme, the “sodium pump,” is responsible for maintaining the intracellular milieu throughout the body by moving sodium ions out of and potassium ions into cells." ([DailyMed: Lanoxin (digoxin) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9ec84cac-6ecc-43dc-8006-6ccc029e2707), version du 2025-10-17 ; consulté le 2026-11-19). D'après les connaissances générales, la digoxine inhibe la pompe Na+/K+-ATPase, ce qui augmente le calcium intracellulaire et renforce la contractilité myocardique, tout en ralentissant la conduction auriculo-ventriculaire. Ce mécanisme explique son usage dans la fibrillation auriculaire.

Le lien avec l'angor de Prinzmetal est en revanche **spéculatif**. Cet angor est dû à un vasospasme coronarien, habituellement traité par des inhibiteurs calciques et des dérivés nitrés. L'augmentation du calcium intracellulaire induite par la digoxine n'est pas évidemment compatible avec cette indication, et un effet vasoconstricteur potentiel pourrait même être défavorable.

Le score TxGNN très élevé (0,9981) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve clinique ou biologique. Les autres prédictions du modèle (obstruction duodénale, ulcère duodénal, reflux duodéno-gastrique, hypoalphalipoprotéinémie) ne présentent pas non plus de lien plausible identifié et ne sont pas développées ici.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'angor de Prinzmetal.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 65458013 | DIGOXINE NATIVELLE ADULTES 0,50 mg/2 ml, solution injectable IV | Solution injectable | TEOFARMA | Active |
| 63593820 | HEMIGOXINE NATIVELLE 0,125 mg, comprimé | Comprimé | TEOFARMA | Active |
| 61917063 | DIGOXINE NATIVELLE 5 microgrammes/0,1 ml, solution buvable en gouttes | Solution buvable en gouttes | TEOFARMA | Active |
| 67681303 | DIGOXINE NATIVELLE 0,25 mg, comprimé | Comprimé | TEOFARMA | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

Les quatre AMM, détenues par TEOFARMA, sont valides ; le médicament est commercialisé.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : insuffisance rénale, hypokaliémie, hypercalcémie, néphrocalcinose, troubles du métabolisme du phosphore, infarctus du myocarde, thrombose coronarienne, hémoglobinopathie, cœur pulmonaire, syndrome de Wolff-Parkinson-White, maladie du sinus (y compris familiale), fibrillation ventriculaire, cardiomyopathie hypertrophique (y compris familiale), bloc auriculo-ventriculaire, myxœdème et hypothyroïdie (y compris congénitale), myocardite, péricardite constrictive, cardiomyopathie restrictive, pyouretère.
- **Interactions médicamenteuses** : 304 interactions recensées. Parmi les exemples de niveau modéré : acarbose, rabéprazole, doxycycline, épinéphrine, hydrocortisone, cholécalciférol, metformine, amphotéricine B, bupropion, triamcinolone, acide acétylsalicylique, dexaméthasone, bétaméthasone, tétracycline, phosphate de calcium. Niveau mineur : albiglutide, hyoscyamine, atropine, glycopyrronium.

Les mises en garde et contre-indications issues de la notice ANSM n'ont pas pu être obtenues. Veuillez consulter la notice pour les informations de sécurité complètes. La digoxine a un index thérapeutique étroit ; un suivi de la kaliémie, de la fonction rénale et de la digoxinémie est classiquement requis.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle TxGNN (niveau L5), sans essai ni publication, avec un lien mécanistique peu plausible et un risque potentiel de vasoconstriction. Les 4 AMM sont valides en France, mais les données de sécurité issues de la notice sont manquantes, ce qui empêche l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications)
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Mener une revue de la littérature ciblée sur la digoxine et le vasospasme coronarien, et rechercher d'éventuels essais
- Examiner la pertinence mécanistique au regard des traitements de référence (inhibiteurs calciques, dérivés nitrés)
- Vérifier le statut réglementaire (4 AMM valides sur 4)

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Lanoxin (digoxin) prescribing information, Covis Pharma US, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=9ec84cac-6ecc-43dc-8006-6ccc029e2707) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

