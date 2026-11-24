---
layout: default
title: Minocycline
parent: Prédiction du modèle uniquement (L5)
nav_order: 502
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "MINOCYCLINE"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis"]
description: "Minocycline : nouvelle indication prédite, Kératoconjonctivite épithéliale ponctuée (punctate epithelial keratoconjunctivitis) (niveau de preuve L5). Indication d'origine : Non renseignée dans les do…"
---

# Minocycline
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

## Minocycline: Kératoconjonctivite épithéliale ponctuée (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## Résumé en Une Phrase

Minocycline est un antibiotique de la famille des tétracyclines, initialement utilisé pour traiter des infections bactériennes (infections urinaires, bronchite, acné, gonorrhée, parodontite, entre autres).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **kératoconjonctivite épithéliale ponctuée**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Kératoconjonctivite épithéliale ponctuée (punctate epithelial keratoconjunctivitis) |
| Score de Prédiction TxGNN | 0.9963 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Minocycline (traduction non officielle) : « Le mécanisme d'action d'ARESTIN en complément des procédures de détartrage et de surfaçage radiculaire pour la réduction de la profondeur des poches chez les patients atteints de parodontite de l'adulte est inconnu. » Texte original en anglais : "The mechanism of action of ARESTIN as an adjunct to scaling and root planing procedures for reduction of pocket depth in patients with adult periodontitis is unknown." ([DailyMed: Arestin (minocycline hydrochloride) prescribing information, OraPharma, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8515df41-1936-4f3b-86ba-d2bb2a8441fb), version du 2024-05-31 ; consulté le 2026-11-19). Sur la base des informations connues, la minocycline appartient à la classe des tétracyclines. Son efficacité antibactérienne est établie dans les indications d'origine, et elle pourrait mécanistiquement être applicable à certaines atteintes de la surface oculaire.

Au-delà de son activité antibactérienne, la minocycline est décrite comme ayant des propriétés anti-inflammatoires, inhibitrices des métalloprotéinases matricielles (MMP) et anti-apoptotiques. Ces effets pourraient être pertinents pour l'inflammation de la surface oculaire. Par analogie, d'autres tétracyclines (comme la doxycycline) sont utilisées dans des atteintes de la surface oculaire telles que le dysfonctionnement des glandes de Meibomius et la blépharite.

Ce lien est cependant **déduit et non démontré** par les données compilées pour ce rapport. Le mécanisme ne peut pas être recoupé avec la pharmacologie documentée du médicament. Une seconde prédiction du modèle, la **kératite d'exposition** (score de 0,9920), repose sur le même raisonnement spéculatif (inhibition de MMP-9, effets anti-inflammatoires). Elle est également de niveau L5 avec une recommandation Hold, car sa prise en charge repose avant tout sur la lubrification et le traitement de la cause de l'exposition.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 60929447 | MYNOCINE 100 mg, gélule | Gélule | LABORATOIRE XO | Active |
| 66680127 | PAROCLINE 2 %, gel pour usage dentaire | Gel pour usage dentaire | SUNSTAR FRANCE | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

Le médicament est commercialisé et ses AMM sont valides (statut des AMM : voir l'Aperçu rapide) dans les données compilées. En revanche, la forme disponible est une gélule orale : la compatibilité avec une voie d'administration oculaire n'a pas été évaluée.

<!-- review:begin fr-lic-20261124-minocycline-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « sa seule AMM est valide (1 AMM valide sur 1) » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans l'Aperçu rapide. Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés : le nombre et le statut à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché, générés à partir des données BDPM. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-minocycline-1 -->

## Considérations de Sécurité

- **Maladies associées à des contre-indications (graphe de connaissances, hors texte de la notice)** : maladie rénale, pyo-uretère, maladie hépatique, maladie de la vésicule biliaire, colite à *Clostridium difficile*, entérocolite nécrosante périnatale, pseudotumeur cérébrale, hypertension intracrânienne, dyskinésie de l'œsophage.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi celles listées :
  - **Majeures** : isotrétinoïne, acitrétine (risque notamment lié à l'hypertension intracrânienne).
  - **Modérées** : éthinylestradiol, amoxicilline, ampicilline, acide aminolévulinique (topique), citrate de sodium, asparaginases, balsalazide, citrate de bismuth potassique, phosphate et acétate de calcium, brentuximab védotine, calaspargase pégol, cannabidiol.
  - **Mineures** : acétazolamide, hydrochlorothiazide, amiloride, bumétanide.

Les mises en garde et contre-indications issues de la notice n'ont pas pu être consultées. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (0,9963), sans aucun essai clinique ni publication. Le niveau de preuve est L5.
- Les données de sécurité issues de la notice sont manquantes (lacune bloquante), le mécanisme d'action n'est pas documenté.

<!-- review:begin fr-lic-20261106-minocycline-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les données de sécurité issues de la notice sont manquantes (lacune bloquante), le mécanisme d'action n'est pas documenté, et la seule AMM française est annulée. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-minocycline-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications) pour permettre le dépistage de sécurité.
- Obtenir les données de mécanisme d'action (par exemple via DrugBank).
- Réaliser une revue systématique de la littérature et des registres d'essais sur la minocycline dans les atteintes de la surface oculaire.
- Évaluer la compatibilité de la voie d'administration (orale actuelle vs oculaire) et la disponibilité réelle du produit en France.
- Démontrer la pertinence préclinique de l'effet anti-MMP et anti-inflammatoire dans la kératoconjonctivite épithéliale ponctuée.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « et la seule AMM française est annulée » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-12 | Tableau : l’AMM 60929447 (MYNOCINE 100 mg) est active, non annulée | Remplacé par le tableau d'AMM généré par programme (auparavant : Corrigé) | [Base de données publique des médicaments (BDPM)](https://base-donnees-publique.medicaments.gouv.fr/) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Arestin (minocycline hydrochloride) prescribing information, OraPharma, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8515df41-1936-4f3b-86ba-d2bb2a8441fb) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

