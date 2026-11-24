---
layout: default
title: Amoxicillin
parent: Prédiction du modèle uniquement (L5)
nav_order: 61
evidence_level: L5
indication_count: 8
monitor_inn: "amoxicillin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-11-24
description: "Amoxicillin : nouvelle indication prédite, Hyperamylasémie (hyperamylasemia) (niveau de preuve L5). En France, AMM dans la BDPM : 18 (valides : 18)"
---

# Amoxicillin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Amoxicilline : bêta-lactamine bactéricide (inhibiteur de la synthèse de la paroi bactérienne) → hyperamylasémie (hyperamylasemia)
{: .text-alpha }

## Résumé en Une Phrase

L'amoxicilline est un antibiotique de la famille des bêta-lactamines, qui agit en bloquant la synthèse de la paroi des bactéries.
Le modèle TxGNN prédit qu'elle pourrait être utile pour l'**hyperamylasémie (hyperamylasemia)**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Hyperamylasémie (hyperamylasemia) |
| Score de Prédiction TxGNN | 0,9963 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 18 sur 18) |
| Nombre d'AMM | 18 (valides : 18) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon les rubriques « Mechanism of Action » et « Microbiology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Amoxicillin (traduction non officielle) : « L'amoxicilline est un médicament antibactérien. […] L'amoxicilline est similaire à la pénicilline par son action bactéricide sur les bactéries sensibles pendant la phase de multiplication active. Elle agit par inhibition de la biosynthèse de la paroi cellulaire, ce qui entraîne la mort des bactéries. » Texte original en anglais : "Amoxicillin is an antibacterial drug. […] Amoxicillin is similar to penicillin in its bactericidal action against susceptible bacteria during the stage of active multiplication. It acts through the inhibition of cell wall biosynthesis that leads to the death of the bacteria." ([DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77), version du 2026-11-13 ; consulté le 2026-11-19). Sur la base des informations connues, l'amoxicilline est une bêta-lactamine bactéricide : elle inhibe la synthèse de la paroi bactérienne et agit donc sur des infections.

L'hyperamylasémie, elle, est une anomalie biologique (origine pancréatique, salivaire ou rénale) et non une maladie infectieuse. Aucun lien mécanistique plausible n'a été identifié entre l'action antibactérienne du médicament et cette anomalie.

Le score élevé du modèle (0,9963) reste donc une prédiction statistique isolée, qui ne repose sur aucune donnée clinique ou publiée. Elle doit être considérée comme une hypothèse très préliminaire, voire comme un artefact du modèle.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les données compilées recensent 18 AMM, toutes de statut valide. Les 5 premières sont listées ci-dessous (les textes d'indication ne sont pas renseignés).

<!-- review:begin fr-lic-20261124-amoxicillin-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les données compilées recensent 15 AMM, toutes de statut valide. » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-amoxicillin-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 66918105 | AMOXICILLINE PANPHARMA 1 g, poudre pour solution injectable | Poudre pour solution injectable | PANPHARMA | Active |
| 69915160 | AMOXICILLINE PANPHARMA 1 g/5 ml, poudre et solution pour solution injectable (IM) | Poudre et solution pour solution injectable | PANPHARMA | Active |
| 69416855 | AMOXICILLINE PANPHARMA 2 g, poudre pour solution injectable | Poudre pour solution injectable | PANPHARMA | Active |
| 61645058 | XYLLOMAC 500 mg, poudre pour solution injectable/pour perfusion (IM-IV) | Poudre pour solution injectable ou pour perfusion | LABORATOIRES DELBERT | Active |
| 60271045 | XYLLOMAC 2 g, poudre pour solution injectable/pour perfusion (IV) | Poudre pour solution injectable ou pour perfusion | LABORATOIRES DELBERT | Active |
| 61801023 | XYLLOMAC 1 g, poudre pour solution injectable/pour perfusion (I.M.-I.V.) | Poudre pour solution injectable ou pour perfusion | LABORATOIRES DELBERT | Active |
| 63084015 | LEVMENTIN 2 g/200 mg ADULTES, poudre pour solution pour perfusion | Poudre pour solution pour perfusion | LABORATOIRES DELBERT | Active |
| 64473140 | AMOXICILLINE/ACIDE CLAVULANIQUE PANPHARMA 2 g/200 mg ADULTES, poudre pour solution inject… | Poudre pour solution injectable | PANPHARMA | Active |
| 64582182 | LEVMENTIN 1 g/200 mg, poudre pour solution injectable/pour perfusion (IV) | Poudre pour solution injectable ou pour perfusion | LABORATOIRES DELBERT | Active |
| 63327759 | AMOXICILLINE/ACIDE CLAVULANIQUE SANDOZ 2 g/200 mg, poudre pour solution pour perfusion | Poudre pour solution pour perfusion | SANDOZ | Active |
| 65324007 | AMOXICILLINE/ACIDE CLAVULANIQUE SANDOZ 500 mg/50 mg, poudre pour solution injectable/pour… | Poudre pour solution injectable ou pour perfusion | SANDOZ | Active |
| 69325964 | LEVMENTIN 500 mg/50 mg, poudre pour solution injectable/pour perfusion (IV) | Poudre pour solution injectable ou pour perfusion | LABORATOIRES DELBERT | Active |
| 61119706 | AMOXICILLINE/ACIDE CLAVULANIQUE PANPHARMA 500 mg/50 mg nourrissons et enfants, poudre pou… | Poudre pour solution injectable | PANPHARMA | Active |
| 69493182 | AMOXICILLINE/ACIDE CLAVULANIQUE PANPHARMA 1 g/200 mg ADULTES, poudre pour solution inject… | Poudre pour solution injectable | PANPHARMA | Active |
| 62096413 | AMOXICILLINE/ACIDE CLAVULANIQUE SANDOZ 1 g/200 mg, poudre pour solution injectable/pour p… | Poudre pour solution injectable ou pour perfusion | SANDOZ | Active |
| 68021727 | AMOXICILLINE PANPHARMA 500 mg, poudre pour solution injectable | Poudre pour solution injectable | PANPHARMA | Active |
| 64160423 | AMOXICILLINE/ACIDE CLAVULANIQUE REIG JOFRE 1 g/200 mg, poudre pour solution injectable/po… | Poudre pour solution injectable ou pour perfusion | LABORATORIO REIG JOFRE (ESPAGNE) | Active |
| 68592117 | AMOXICILLINE/ACIDE CLAVULANIQUE REIG JOFRE 2 g/200 mg, poudre pour solution pour perfusion | Poudre pour solution pour perfusion | LABORATORIO REIG JOFRE (ESPAGNE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Interactions médicamenteuses** : 271 interactions sont recensées. Parmi les principales :
  - **Majeures** : méthotrexate ; vaccin vivant contre le choléra (souche *Vibrio cholerae* CVD 103-HgR).
  - **Modérées** : doxycycline, minocycline, déméclocycline, éthinylestradiol, estradiol, anisindione, dicoumarol, balsalazide, entécavir, mycophénolate mofétil, certains probiotiques (*Lactobacillus acidophilus*, *Bifidobacterium longum infantis*) et l'indium In-111 oxyquinoline.
  - **Mineures** : allopurinol, amiloride, azithromycine, clarithromycine, érythromycine.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun lien mécanistique plausible n'existe entre l'amoxicilline et l'hyperamylasémie, et aucune étude ne l'a évaluée. Le niveau de preuve est L5 : la prédiction repose uniquement sur le modèle.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action et justification biologique d'un effet sur l'hyperamylasémie
- Études précliniques ou observationnelles évaluant directement cette association
- Récupération des mises en garde et contre-indications de la notice ANSM pour l'évaluation de la sécurité

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: amoxicillin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98e9274c-c02e-44d9-8cc5-17536ef03a77) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

