---
layout: default
title: Ipilimumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 410
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Ipilimumab : nouvelle indication prédite, Choroïdérémie (niveau de preuve L5). Indication d'origine : Mélanome métastatique (issue de la base de connaissances du modèle"
monitor_inn: "IPILIMUMAB"
predicted_indications: ["choroideremia"]
---

# Ipilimumab
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

## Ipilimumab : Du Mélanome Métastatique à la Choroïdérémie
{: .text-alpha }

## Résumé en Une Phrase

L'ipilimumab est un anticorps monoclonal anti-CTLA-4, initialement utilisé dans le traitement du mélanome métastatique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **choroïdérémie**, une dégénérescence rétinienne héréditaire rare.
Actuellement, **aucun essai clinique** et **aucune publication** ne soutiennent cette prédiction, qui repose uniquement sur le modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mélanome métastatique (issue de la base de connaissances du modèle ; le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Choroïdérémie |
| Score de Prédiction TxGNN | 0,9906 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Ipilimumab (traduction non officielle) : « CTLA-4 est un régulateur négatif de l'activité des lymphocytes T. L'ipilimumab est un anticorps monoclonal qui se lie à CTLA-4 et bloque l'interaction de CTLA-4 avec ses ligands, CD80/CD86. Il a été démontré que le blocage de CTLA-4 augmente l'activation et la prolifération des lymphocytes T, y compris l'activation et la prolifération des lymphocytes T effecteurs infiltrant la tumeur. » Texte original en anglais : "CTLA-4 is a negative regulator of T-cell activity. Ipilimumab is a monoclonal antibody that binds to CTLA-4 and blocks the interaction of CTLA-4 with its ligands, CD80/CD86. Blockade of CTLA-4 has been shown to augment T-cell activation and proliferation, including the activation and proliferation of tumor infiltrating T-effector cells." ([DailyMed: Yervoy (ipilimumab) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2265ef30-253e-11df-8a39-0800200c9a66), version du 2026-08-20 ; consulté le 2026-11-19). L'ipilimumab est un anticorps anti-CTLA-4 qui lève un frein de l'activation des lymphocytes T et amplifie la réponse immunitaire antitumorale. Son efficacité est établie dans le mélanome.

**En pratique, cette prédiction n'est pas étayée sur le plan mécanistique.** La choroïdérémie est une maladie monogénique liée à l'X, causée par la perte de fonction du gène *CHM* (REP1). Elle se caractérise par la dégénérescence progressive de l'épithélium pigmentaire rétinien, des photorécepteurs et de la choroïde. Aucun mécanisme dépendant des points de contrôle immunitaires n'est établi dans cette maladie.

Le score élevé du modèle (0,9906) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non des preuves biologiques. Il n'est confirmé par aucune donnée clinique ou bibliographique. L'activation immunitaire systémique expose en outre à des événements indésirables d'origine immunitaire, notamment des inflammations oculaires comme l'uvéite, ce qui serait défavorable dans une rétine déjà en dégénérescence.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66532840 | YERVOY 5 mg/mL, solution à diluer pour perfusion (BRISTOL-MYERS SQUIBB / PFIZER EEIG, Irlande) | Solution à diluer pour perfusion | Texte d'indication non renseigné |

<!-- review:begin fr-row-20261112-ipilimumab-1 -->

> **Correction de vérification (2026-11-12)**: Texte initial : « 66532840 (annulée) » Selon la BDPM (données du 2026-11-09), l’AMM 66532840 (YERVOY 5 mg/mL, solution à diluer pour perfusion) a le statut « Autorisation active » ; la mention « annulée » a été retirée. Source: [Base de données publique des médicaments (BDPM)](https://base-donnees-publique.medicaments.gouv.fr/).

<!-- review:end fr-row-20261112-ipilimumab-1 -->

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Immunothérapie (anticorps anti-CTLA-4) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Surveillance des événements indésirables d'origine immunitaire, notamment oculaires (uvéite) ; pour le reste, consulter la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

- **Événements indésirables d'origine immunitaire** : l'activation immunitaire systémique peut provoquer des inflammations oculaires, dont l'uvéite. Ce risque est particulièrement préoccupant dans une rétine dégénérative.
- **Interactions médicamenteuses** : 100 interactions sont répertoriées. Les principales sont :
  - **Majeures** : anticoagulants (apixaban, bétrixaban, édoxaban, bivalirudine, dalteparine, désirudine, argatroban, danaparoïde).
  - **Modérées** : corticoïdes (hydrocortisone, prednisone, prednisolone, dexaméthasone, bétaméthasone, triamcinolone, budésonide), statines (rosuvastatine, simvastatine), métronidazole, tinidazole et naltrexone.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Aucun lien mécanistique crédible n'existe avec la choroïdérémie, et le risque d'inflammation oculaire immuno-induite est défavorable.
- Le seul produit français est de plus annulé. À titre de comparaison, d'autres indications prédites par le modèle, comme le mélanome non cutané, disposent de bien plus de données.

**Pour avancer, les éléments suivants sont nécessaires :**
- Des données précliniques ou mécanistiques justifiant l'implication de la voie CTLA-4 dans la choroïdérémie.
- Les données détaillées sur le mécanisme d'action et les informations de sécurité issues de la notice (mises en garde et contre-indications).
- Une évaluation du risque d'uvéite et d'effets oculaires immuno-induits dans un contexte de dégénérescence rétinienne.
- La confirmation du statut réglementaire en France.

<!-- review:begin fr-lic-20261106-ipilimumab-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La confirmation du statut réglementaire en France, l'AMM étant annulée. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-ipilimumab-1 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « l'AMM étant annulée » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-12 | Tableau : l’AMM 66532840 (YERVOY 5 mg/mL) est active, non annulée | Corrigé | [Base de données publique des médicaments (BDPM)](https://base-donnees-publique.medicaments.gouv.fr/) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Yervoy (ipilimumab) prescribing information, E.R. Squibb & Sons, L.L.C.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2265ef30-253e-11df-8a39-0800200c9a66) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

