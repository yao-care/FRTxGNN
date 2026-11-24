---
layout: default
title: Raloxifene
parent: Prédiction du modèle uniquement (L5)
nav_order: 646
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "raloxifene"
predicted_indications: ["duodenal ulcer (disease)", "hypoalphalipoproteinemia", "duodenal obstruction", "duodenogastric reflux"]
description: "Raloxifene : nouvelle indication prédite, Ulcère duodénal (duodenal ulcer (disease)) (niveau de preuve L5). En France, AMM dans la BDPM : 10 (valides : 9)"
---

# Raloxifene
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

## Raloxifene: Ulcère duodénal (duodenal ulcer (disease))
{: .text-alpha }

## Résumé en Une Phrase

Le raloxifène est un modulateur sélectif des récepteurs des œstrogènes (SERM), initialement utilisé pour le traitement de l'ostéoporose postménopausique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**ulcère duodénal**,
mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Ulcère duodénal (duodenal ulcer (disease)) |
| Score de Prédiction TxGNN | 0.9972 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 9 sur 10) |
| Nombre d'AMM | 10 (valides : 9) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Raloxifene (traduction non officielle) : « Le raloxifène est un agoniste/antagoniste des œstrogènes, communément appelé modulateur sélectif des récepteurs aux œstrogènes (SERM). Les actions biologiques du raloxifène s'exercent en grande partie par la liaison aux récepteurs aux œstrogènes. Cette liaison entraîne l'activation des voies œstrogéniques dans certains tissus (agonisme) et le blocage des voies œstrogéniques dans d'autres (antagonisme). » Texte original en anglais : "Raloxifene is an estrogen agonist/antagonist, commonly referred to as a selective estrogen receptor modulator (SERM). The biological actions of raloxifene are largely mediated through binding to estrogen receptors. This binding results in activation of estrogenic pathways in some tissues (agonism) and blockade of estrogenic pathways in others (antagonism)." ([DailyMed: Evista (raloxifene hydrochloride) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fcaaa6dc-74e8-4fb8-800c-5574bf0f8de9), version du 2026-02-11 ; consulté le 2026-11-19). Sur la base des connaissances générales, le raloxifène est un SERM : il exerce une activité agoniste œstrogénique sur l'os et une activité antagoniste dans le sein et l'utérus. Son efficacité dans l'ostéoporose postménopausique est établie.

Aucun lien mécanistique n'est démontré entre cette action et l'ulcère duodénal. Une éventuelle implication de la signalisation des récepteurs des œstrogènes dans la protection de la muqueuse gastroduodénale reste purement spéculative et n'est pas appuyée par les données disponibles. Le score élevé (0,9972) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique ni un signal thérapeutique confirmé.

Trois autres prédictions figurent dans les données, toutes de niveau L5 et sans essai ni publication : l'hypoalphalipoprotéinémie (score 0,9965), l'obstruction duodénale (0,9964, peu plausible car il s'agit d'une affection structurelle) et le reflux duodénogastrique (0,9959). Ces pistes ne sont pas détaillées ici.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69445593 (annulée) | OPTRUMA 60 mg, comprimé pelliculé (ELI LILLY NEDERLAND BV, Pays-Bas) | Comprimé pelliculé | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : hypertension, maladie hépatique, maladie de la vésicule biliaire, fibrillation auriculaire, hypertriglycéridémie, thrombophlébite, maladie coronarienne, accident vasculaire cérébral et troubles cérébrovasculaires, infarctus cérébral, embolie pulmonaire, occlusion de l'artère rétinienne, thrombophilie, insuffisance rénale, accident ischémique transitoire, insuffisance vertébrobasilaire, syndrome des antiphospholipides.
- **Interactions médicamenteuses** : 129 interactions recensées, dont les 20 premières (niveau de gravité non précisé) concernent notamment le calcitriol, le pantoprazole, le glimépiride, la mésalazine, la doxycycline, le clotrimazole, la morphine, la metformine, l'oméprazole, le lansoprazole, le sucralfate, la rosiglitazone, la vancomycine, le lactulose, la triamcinolone, la simvastatine, la nystatine, le natéglinide, la scopolamine et la tétracycline.

Les mises en garde et contre-indications de la notice ANSM n'ont pas pu être exploitées ; veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (L5), sans essai clinique, sans publication ni lien mécanistique établi.

<!-- review:begin fr-lic-20261106-raloxifene-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La prédiction repose uniquement sur le modèle (L5), sans essai clinique, sans publication ni lien mécanistique établi. De plus, la seule AMM française est annulée et le profil de sécurité (risques thromboemboliques et cardiovasculaires notamment) n'a pas pu être vérifié à partir de la notice. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 0 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-raloxifene-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice ANSM (mises en garde et contre-indications), étape bloquante pour le criblage de sécurité
- Données détaillées sur le mécanisme d'action (DrugBank)
- Revue de la littérature et des registres d'essais sur le raloxifène dans l'ulcère duodénal
- Études précliniques permettant d'évaluer la plausibilité biologique
- Clarification du statut réglementaire

<!-- review:begin fr-lic-20261106-raloxifene-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarification du statut réglementaire, l'AMM étant annulée » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 0 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-raloxifene-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « De plus, la seule AMM française est annulée et le profil de sécurité (risques thromboemboliques et cardiovasculaires notamment) n'a pas pu ê » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « l'AMM étant annulée » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-13 | Tableau : l'AMM 69445593 (OPTRUMA) est active, non annulée | Vérification retirée (2026-11-24 : d'après la BDPM (données du 2026-11-23 ; fiche produit consultée le 2026-11-24), l'AMM 69445593 (OPTRUMA 60 mg) est abrogée depuis le 15-10-2026 ; le texte d'origine est donc exact et la correction est retirée ; auparavant : Corrigé) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Evista (raloxifene hydrochloride) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=fcaaa6dc-74e8-4fb8-800c-5574bf0f8de9) |
| 2026-11-24 | Autres AMM de raloxifène actives dans la BDPM | Vérification retirée (2026-11-24 : les 9 AMM actives de raloxifène (dont EVISTA 67365141) font désormais partie des données compilées (complément par code de substance BDPM, 2026-11-24) ; la note n'est plus nécessaire ; auparavant : Note ajoutée) | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

