---
layout: default
title: Acetazolamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
monitor_inn: "acetazolamide"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "unclassified intestinal pseudoobstruction"]
last_modified_at: 2026-11-24
description: "Acetazolamide : nouvelle indication prédite, Hyperthermie maligne d'effort (exercise-induced malignant hyperthermia) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données loca…"
---

# Acetazolamide
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

## Acétazolamide : inhibiteur de l'anhydrase carbonique → hyperthermie maligne d'effort (exercise-induced malignant hyperthermia)
{: .text-alpha }

## Résumé en Une Phrase

L'acétazolamide est un inhibiteur de l'anhydrase carbonique, présenté en France sous le nom DIAMOX.
Le modèle TxGNN prédit qu'il pourrait être utile pour l'**hyperthermie maligne d'effort (exercise-induced malignant hyperthermia)**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hyperthermie maligne d'effort (exercise-induced malignant hyperthermia) |
| Score de Prédiction TxGNN | 0.9995 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Acetazolamide (traduction non officielle) : « L'acétazolamide est un puissant inhibiteur de l'anhydrase carbonique, efficace dans le contrôle de la sécrétion de liquide (par exemple, certains types de glaucome), dans le traitement de certains troubles convulsifs (par exemple, l'épilepsie) et dans la stimulation de la diurèse en cas de rétention hydrique anormale (par exemple, l'œdème cardiaque). L'acétazolamide n'est pas un diurétique mercuriel. » Texte original en anglais : "Acetazolamide is a potent carbonic anhydrase inhibitor, effective in the control of fluid secretion (e.g., some types of glaucoma), in the treatment of certain convulsive disorders (e.g., epilepsy), and in the promotion of diuresis in instances of abnormal fluid retention (e.g., cardiac edema). Acetazolamide is not a mercurial diuretic." ([DailyMed: acetazolamide prescribing information, Chartwell RX, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e8e48a25-5f6c-4b5a-a5f2-ee87aabea33b), version du 2026-11-10 ; consulté le 2026-11-19). Sur la base des informations connues, l'acétazolamide appartient à la classe des inhibiteurs de l'anhydrase carbonique, enzyme qui régule le pH et le transport des ions dans de nombreux tissus.

Un lien plausible serait une modification du pH et de la gestion des ions dans le muscle squelettique, ce qui pourrait théoriquement influencer une atteinte musculaire liée à l'effort. Cette hypothèse reste toutefois spéculative et n'est étayée par aucune donnée compilée pour ce rapport. Le score élevé du modèle (0.9995) ne constitue pas une preuve clinique.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 68693244 | DIAMOX 250 mg, comprimé sécable | Comprimé sécable | COOPER (ABRÉGÉ DE COOPERATION PHARMACEUTIQUE FRANCAISE) | Active |
| 63463588 | DIAMOX 500 mg, poudre et solvant pour préparation injectable | Poudre et solution pour préparation injectable | COOPER (ABRÉGÉ DE COOPERATION PHARMACEUTIQUE FRANCAISE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

Les données locales comportent deux AMM, toutes deux pour des spécialités à base d'acétazolamide seule. Le statut de marché indiqué par les données est « commercialisé ».

## Considérations de Sécurité

- **Interactions médicamenteuses** : 165 interactions sont recensées. Parmi les exemples disponibles :
  - Majeures : acide acétylsalicylique, cisapride.
  - Modérées : antidiabétiques (acarbose, acétohexamide, alogliptine, canagliflozine, chlorpropamide, dapagliflozine, dulaglutide, albiglutide), corticoïdes (bétaméthasone, dexaméthasone, béclométasone), amphotéricine B (plusieurs formes), bisacodyl, huile de ricin.
  - Mineure : doxycycline.
- **Signaux de sécurité issus de la littérature associée aux autres prédictions** : cas rapportés d'iléus adynamique sous acétazolamide et d'œdème pulmonaire non cardiogénique après administration intraveineuse. Ils ne concernent pas la prédiction principale mais sont à garder à l'esprit.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles, qui n'ont pas pu être compilées dans les données de ce rapport.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (0.9995), sans essai clinique ni publication portant sur l'hyperthermie maligne d'effort. Le niveau de preuve est L5 et aucun mécanisme n'est démontré.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action de l'acétazolamide
- Études précliniques ou observationnelles évaluant un effet sur l'hyperthermie maligne d'effort
- Mises en garde et contre-indications extraites de la notice ANSM pour un dépistage de sécurité
- Évaluation du profil de sécurité (interactions, troubles électrolytiques et acido-basiques) chez les patients concernés

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: acetazolamide prescribing information, Chartwell RX, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e8e48a25-5f6c-4b5a-a5f2-ee87aabea33b) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

