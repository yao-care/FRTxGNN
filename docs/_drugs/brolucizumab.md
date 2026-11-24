---
layout: default
title: Brolucizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 118
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Brolucizumab : nouvelle indication prédite, Trouble de la phosphorylation oxydative mitochondriale dû à des anomalies de l'ADN nucléaire (niveau de preuve L5). Indication d'origine : Dégénérescence maculaire (texte d'indi…"
monitor_inn: "BROLUCIZUMAB"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "esophageal varices with bleeding", "esophageal varices without bleeding", "exocrine pancreatic insufficiency"]
---

# Brolucizumab
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

## Brolucizumab : De la dégénérescence maculaire au trouble de la phosphorylation oxydative mitochondriale dû à des anomalies de l'ADN nucléaire
{: .text-alpha }

## Résumé en Une Phrase

Brolucizumab est un fragment d'anticorps à chaîne unique anti-VEGF-A, initialement utilisé pour le traitement de la dégénérescence maculaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble de la phosphorylation oxydative mitochondriale dû à des anomalies de l'ADN nucléaire**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dégénérescence maculaire (texte d'indication de l'AMM non renseigné) |
| Nouvelle Indication Prédite | Trouble de la phosphorylation oxydative mitochondriale dû à des anomalies de l'ADN nucléaire |
| Score de Prédiction TxGNN | 0,9967 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Brolucizumab (traduction non officielle) : « Le brolucizumab est un inhibiteur du VEGF humain. Le brolucizumab se lie aux trois principales isoformes du VEGF-A (p. ex. VEGF 110, VEGF 121 et VEGF 165 ), empêchant ainsi l'interaction avec les récepteurs VEGFR-1 et VEGFR-2. En inhibant le VEGF-A, le brolucizumab supprime la prolifération des cellules endothéliales, la néovascularisation et la perméabilité vasculaire. » Texte original en anglais : "Brolucizumab is a human VEGF inhibitor. Brolucizumab binds to the three major isoforms of VEGF-A (e.g., VEGF 110, VEGF 121, and VEGF 165 ), thereby preventing interaction with receptors VEGFR-1 and VEGFR-2. By inhibiting VEGF-A, brolucizumab suppresses endothelial cell proliferation, neovascularization, and vascular permeability." ([DailyMed: Beovu (brolucizumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5d1dc1fa-a2d3-46ed-9e9a-c1a036590d3d), version du 2026-10-26 ; consulté le 2026-11-19). Sur la base des informations connues, le brolucizumab est un inhibiteur du VEGF-A de type fragment d'anticorps à chaîne unique, dont l'usage est établi dans la dégénérescence maculaire.

Aucun lien mécanistique plausible n'est établi avec les défauts de phosphorylation oxydative d'origine nucléaire. Les maladies mitochondriales peuvent comporter une atteinte rétinienne et une signalisation VEGF liée à l'hypoxie, mais cette hypothèse reste spéculative.

Le score élevé de TxGNN (0,9967) provient d'une prédiction du modèle TxGNN (apprentissage profond). Il n'est étayé par aucun essai clinique ni aucune publication dans les données compilées pour ce rapport, et doit donc être interprété avec une grande prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 65607585 | BEOVU 120 mg/ml, solution injectable en seringue préremplie | Solution injectable | NOVARTIS EUROPHARM (IRLANDE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (liens médicament-maladie du graphe, et non texte de la notice) : uvéite, maladie de l'iris, maladie du corps ciliaire, panuvéite, maladie infectieuse oculaire, conjonctivite.

Pour les mises en garde, contre-indications officielles et interactions médicamenteuses, veuillez consulter la notice.

## Autres Indications Prédites (pour information)

| Rang | Indication Prédite | Score TxGNN | Niveau de Preuve | Commentaire |
|------|------|------|------|------|
| 2 | Varices œsophagiennes avec saignement | 0,9912 | L5 | Rationnel théorique (angiogenèse dépendante du VEGF, hypertension portale). Produit intravitréen, non conçu pour une voie systémique. Risque hémorragique et thromboembolique préoccupant en contexte de saignement actif. |
| 3 | Varices œsophagiennes sans saignement | 0,9912 | L5 | Même rationnel et mêmes réserves. Score identique à la forme hémorragique ; il provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, non une preuve biologique. |
| 4 | Insuffisance pancréatique exocrine | 0,9907 | L5 | Aucun lien mécanistique clair. Prise en charge par substitution enzymatique. Le score provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, non une preuve biologique. |

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique établi.
- Les données de sécurité officielles sont absentes. Il n'est pas possible de passer à l'étape de criblage de sécurité.

<!-- review:begin fr-lic-20261106-brolucizumab-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « L'AMM française est annulée, et les données de sécurité officielles sont absentes. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-brolucizumab-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les mises en garde et contre-indications de la notice ANSM (analyse du PDF de la notice).
- Obtenir les données sur le mécanisme d'action via DrugBank.
- Mener une revue de la littérature et des registres d'essais sur les maladies mitochondriales et le VEGF.
- Évaluer la compatibilité de la voie d'administration (produit intravitréen) avec l'indication visée.
- Clarifier la situation réglementaire de la spécialité.

<!-- review:begin fr-lic-20261106-brolucizumab-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarifier la situation réglementaire de la spécialité (AMM annulée). » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-brolucizumab-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « 'AMM française est annulée, et l » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulée) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Beovu (brolucizumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5d1dc1fa-a2d3-46ed-9e9a-c1a036590d3d) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

