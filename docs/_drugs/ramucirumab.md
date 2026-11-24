---
layout: default
title: Ramucirumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 650
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "RAMUCIRUMAB"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "cervical adenosquamous carcinoma, glassy cell variant", "uterine ligament endometrioid adenocarcinoma", "uterine ligament clear cell adenocarcinoma", "uterine ligament mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
description: "Ramucirumab : nouvelle indication prédite, Adénocarcinome du ligament utérin (uterine ligament adenocarcinoma) (niveau de preuve L5). En France, AMM dans la BDPM : 1 (valides : 1)"
---

# Ramucirumab
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

## Ramucirumab: Adénocarcinome du ligament utérin (uterine ligament adenocarcinoma)
{: .text-alpha }

## Résumé en Une Phrase

Le ramucirumab est un anticorps monoclonal initialement utilisé dans le traitement de cancers solides, notamment le cancer gastrique, le cancer bronchique non à petites cellules et le carcinome hépatocellulaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**adénocarcinome du ligament utérin**, ainsi que pour plusieurs cancers gynécologiques apparentés (col de l'utérus, ligament utérin).
Aucun essai clinique ni aucune publication ne soutient actuellement cette direction : il s'agit d'une **prédiction purement computationnelle**.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Adénocarcinome du ligament utérin (uterine ligament adenocarcinoma) |
| Score de Prédiction TxGNN | 0.9995 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Ramucirumab (traduction non officielle) : « Le ramucirumab est un antagoniste du VEGFR2 qui se lie spécifiquement au VEGFR2 et bloque la liaison des ligands du VEGFR, le VEGF-A, le VEGF-C et le VEGF-D. En conséquence, le ramucirumab inhibe l'activation du VEGFR2 stimulée par les ligands, inhibant ainsi la prolifération et la migration des cellules endothéliales humaines induites par les ligands. Le ramucirumab a inhibé l'angiogenèse dans un modèle animal in vivo. » Texte original en anglais : "Ramucirumab is a VEGFR2 antagonist that specifically binds VEGFR2 and blocks binding of VEGFR ligands, VEGF-A, VEGF-C, and VEGF-D. As a result, ramucirumab inhibits ligand-stimulated activation of VEGFR2, thereby inhibiting ligand-induced proliferation, and migration of human endothelial cells. Ramucirumab inhibited angiogenesis in an in vivo animal model." ([DailyMed: Cyramza (ramucirumab) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6080942-dee6-423e-b688-1272c2ae90d4), version du 2026-06-09 ; consulté le 2026-11-19). Sur la base des connaissances générales, le ramucirumab est un antagoniste du récepteur VEGFR-2 : il bloque l'angiogenèse induite par le VEGF. Son efficacité a été établie dans des tumeurs solides dépendantes de l'angiogenèse, comme l'adénocarcinome gastrique, le cancer bronchique non à petites cellules et le carcinome hépatocellulaire.

Les adénocarcinomes gynécologiques (ligament utérin, col de l'utérus) dépendent souvent aussi de l'angiogenèse. Le blocage de la voie VEGF/VEGFR-2 a d'ailleurs un rôle établi dans le cancer du col avancé, avec une autre molécule anti-angiogénique (le bévacizumab). Cela offre un raisonnement plausible, mais indirect, au niveau de la classe thérapeutique.

Le score élevé de TxGNN (0,9995) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, comme d'autres adénocarcinomes et affections cervicales, et non une preuve biologique ou clinique. Les autres candidats prédits (carcinome endocervical, carcinome adénoïde kystique du col, adénocarcinomes séreux, endométrioïdes, à cellules claires ou mucineux du ligament utérin, variantes à cellules en bague à chaton ou de type intestinal du col) reposent sur le même raisonnement générique. Certaines analogies histologiques avec l'adénocarcinome gastrique (cellules en bague à chaton, type intestinal) restent lâches et n'établissent pas l'efficacité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 63848228 | CYRAMZA 10 mg/ml, solution à diluer pour perfusion | Solution à diluer pour perfusion | ELI LILLY (PAYS BAS) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (anticorps monoclonal anti-VEGFR-2), non cytotoxique conventionnel |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions ont été recensées dans les données compilées ; les principales sont de niveau majeur et concernent surtout des médicaments affectant l'hémostase (risque hémorragique potentiel) :
  - Anticoagulants et antithrombotiques : apixaban, bétrixaban, daltéparine, bivalirudine, antithrombine III humaine, défibrotide, caplacizumab
  - Antiagrégants plaquettaires : acide acétylsalicylique, clopidogrel, cilostazol, abciximab, cangrélor
  - Thrombolytique : alteplase
  - Autres : déférasirox, ibritumomab tiuxétan, tositumomab (dont I-131)
  - Niveau modéré : dexfenfluramine, fenfluramine, sibutramine

Les mises en garde et contre-indications de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Les données de sécurité de la notice et le mécanisme d'action sont manquants.

<!-- review:begin fr-lic-20261106-ramucirumab-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les données de sécurité de la notice et le mécanisme d'action sont manquants, et la seule AMM française est annulée. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-ramucirumab-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), indispensable avant tout examen de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Réaliser une revue systématique de la littérature et des registres d'essais sur le ramucirumab dans les cancers gynécologiques
- Hiérarchiser les entités prédites (par exemple le carcinome endocervical, mieux étayé par le rationnel anti-angiogénique) et évaluer leur plausibilité biologique
- Clarifier le statut réglementaire en France et la disponibilité réelle du produit
- Évaluer le risque hémorragique avec les médicaments antithrombotiques dans une population cible précise

<!-- review:begin fr-lic-20261106-ramucirumab-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarifier le statut réglementaire en France (AMM annulée) et la disponibilité réelle du produit » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-ramucirumab-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « et la seule AMM française est annulée » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulée) » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Cyramza (ramucirumab) prescribing information, Eli Lilly and Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c6080942-dee6-423e-b688-1272c2ae90d4) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

