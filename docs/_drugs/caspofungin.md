---
layout: default
title: Caspofungin
parent: Prédiction du modèle uniquement (L5)
nav_order: 145
evidence_level: L5
indication_count: 1
monitor_inn: "caspofungin"
predicted_indications: ["gastrin secretion abnormality"]
last_modified_at: 2026-11-24
description: "Caspofungin : nouvelle indication prédite, Anomalie de la sécrétion de gastrine (gastrin secretion abnormality) (niveau de preuve L5). En France, AMM dans la BDPM : 16 (valides : 12)"
---

# Caspofungin
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

## Caspofungine : échinocandine antifongique → anomalie de la sécrétion de gastrine (gastrin secretion abnormality)
{: .text-alpha }

## Résumé en Une Phrase

La caspofungine est un antifongique de la classe des échinocandines, administré par perfusion.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**anomalie de la sécrétion de gastrine (gastrin secretion abnormality)**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction informatique uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Anomalie de la sécrétion de gastrine (gastrin secretion abnormality) |
| Score de Prédiction TxGNN | 0,9944 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 12 sur 16) |
| Nombre d'AMM | 16 (valides : 12) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon les rubriques « Mechanism of Action » et « Microbiology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Caspofungin (traduction non officielle) : « La caspofungine est un médicament antifongique de la classe des échinocandines. […] La caspofungine, une échinocandine, inhibe la synthèse du bêta (1,3)-D-glucane, un composant essentiel de la paroi cellulaire des espèces sensibles d'Aspergillus et de Candida. Le bêta (1,3)-D-glucane n'est pas présent dans les cellules de mammifères. » Texte original en anglais : "Caspofungin is an echinocandin antifungal drug. […] Caspofungin, an echinocandin, inhibits the synthesis of beta (1,3)-D-glucan, an essential component of the cell wall of susceptible Aspergillus species and Candida species. Beta (1,3)-D-glucan is not present in mammalian cells." ([DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c), version du 2024-10-11 ; consulté le 2026-11-19). D'après les connaissances générales, la caspofungine appartient à la classe des échinocandines, qui inhibent la bêta-(1,3)-D-glucane synthase, une enzyme propre aux cellules fongiques et absente des cellules de mammifères.

Aucun lien mécanistique plausible n'apparaît entre cette activité antifongique et la régulation de la gastrine (fonction des cellules G, sécrétion d'acide gastrique, signalisation du récepteur CCK2). Le score élevé du modèle (0,9944) reflète une prédiction informatique ; il peut provenir d'une proximité dans le réseau de données ou de voisins communs, plutôt que d'une causalité biologique.

En l'état, cette prédiction reste donc spéculative et ne doit pas être interprétée comme un signal d'efficacité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les données compilées recensent des autorisations de mise sur le marché (tableau ci-dessous) pour des spécialités à base de caspofungine seule, toutes sous forme de poudre pour solution à diluer pour perfusion. Le texte d'indication approuvée n'est pas renseigné dans les données locales.

<!-- review:begin fr-lic-20261124-caspofungin-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les données compilées recensent 12 autorisations de mise sur le marché » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans l'Aperçu rapide. Les nombres d'AMM écrits en dur dans le texte corrigé sont retirés : le nombre et le statut à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché, générés à partir des données BDPM. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-caspofungin-1 -->

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 63197689 | CASPOFUNGINE STRAGEN 70 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | STRAGEN-FRANCE | Active |
| 66400785 | CASPOFUNGINE LORIEN 70 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | LABORATORIOS LORIEN (ESPAGNE) | Active |
| 64566502 | CASPOFUNGINE LORIEN 50 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | LABORATORIOS LORIEN (ESPAGNE) | Active |
| 63609267 | CASPOFUNGINE TILLOMED 70 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | TILLOMED PHARMA (ALLEMAGNE) | Active |
| 67108093 | CASPOFUNGINE SUN 70 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | SUN PHARMACEUTICAL INDUSTRIES EUROPE (PAYS BAS) | Active |
| 60140010 | CASPOFUNGINE STRAGEN 50 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | STRAGEN-FRANCE | Active |
| 65358970 | CASPOFUNGINE HIKMA 50 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | HIKMA FARMACEUTICA (PORTUGAL) | Active |
| 64960760 | CASPOFUNGINE HIKMA 70 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | HIKMA FARMACEUTICA (PORTUGAL) | Active |
| 69919835 | CASPOFUNGINE VIATRIS 50 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | VIATRIS SANTE | Active |
| 67987353 | CASPOFUNGINE TILLOMED 50 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | TILLOMED PHARMA (ALLEMAGNE) | Active |
| 61215042 | CASPOFUNGINE VIATRIS 70 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | VIATRIS SANTE | Active |
| 66869238 | CASPOFUNGINE SUN 50 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | SUN PHARMACEUTICAL INDUSTRIES EUROPE (PAYS BAS) | Active |
| 62080334 | CASPOFUNGINE TEVA SANTE 50 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | TEVA SANTE | Abrogée |
| 62517531 | CASPOFUNGINE FRESENIUS KABI 50 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | FRESENIUS KABI FRANCE | Abrogée |
| 68718338 | CASPOFUNGINE FRESENIUS KABI 70 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | FRESENIUS KABI FRANCE | Abrogée |
| 69061411 | CASPOFUNGINE TEVA SANTE 70 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | TEVA SANTE | Abrogée |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Interactions médicamenteuses** : 81 interactions sont recensées. Les principales :
  - **Majeure** : dexaméthasone
  - **Modérée** : naltrexone
  - Niveau non déterminé : calcitriol, pantoprazole, doxycycline, morphine, oméprazole, lansoprazole, vancomycine, sucralfate, lactulose, prednisone, simvastatine, nystatine, épinéphrine, amphotéricine B, hydrocortisone, mannitol, chlorure de potassium, prednisolone.

Veuillez consulter la notice pour les mises en garde et contre-indications détaillées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau de preuve L5) : aucun essai clinique ni publication ne l'étaye, et aucun lien mécanistique plausible avec la sécrétion de gastrine n'est identifié.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action et analyse d'un éventuel lien avec la régulation de la gastrine
- Études précliniques ou de mécanisme portant directement sur l'anomalie de la sécrétion de gastrine
- Mises en garde et contre-indications issues de la notice de l'ANSM
- Évaluation de la compatibilité de la voie d'administration (perfusion) avec l'usage envisagé

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

