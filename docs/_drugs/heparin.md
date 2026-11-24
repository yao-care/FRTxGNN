---
layout: default
title: Heparin
parent: Prédiction du modèle uniquement (L5)
nav_order: 377
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Heparin : nouvelle indication prédite, Thrombophilie par déficit en protéine C, autosomique récessive (niveau de preuve L5). Indication d'origine : Embolie pulmonaire, coagulation intravasculaire dis…"
monitor_inn: "heparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets"]
---

# Heparin
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

## Héparine : Thrombophilie par déficit en protéine C, autosomique récessif
{: .text-alpha }

## Résumé en Une Phrase

L'héparine est un anticoagulant initialement utilisé pour traiter l'embolie pulmonaire, la coagulation intravasculaire disséminée et le purpura fulminans.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **thrombophilie par déficit en protéine C (forme autosomique récessive)**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : la prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Embolie pulmonaire, coagulation intravasculaire disséminée, purpura fulminans (texte d'indication des AMM non renseigné) |
| Nouvelle Indication Prédite | Thrombophilie par déficit en protéine C, autosomique récessive |
| Score de Prédiction TxGNN | 0,9929 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 11 sur 11) |
| Nombre d'AMM | 11 (valides : 11) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Heparin (traduction non officielle) : « L'héparine interagit avec une protéine plasmatique naturellement présente, l'antithrombine III, pour induire un changement de conformation qui augmente nettement l'activité inhibitrice de sérine protéase de l'antithrombine III, inhibant ainsi les facteurs de coagulation activés impliqués dans la séquence finale, en particulier les facteurs Xa et IIa. De faibles quantités d'héparine inhibent le facteur Xa, et des quantités plus importantes inhibent la thrombine (facteur IIa). » Texte original en anglais : "Heparin interacts with the naturally occurring plasma protein, antithrombin III, to induce a conformational change, which markedly enhances the serine protease activity of antithrombin III, thereby inhibiting the activated coagulation factors involved in the closing sequence, particularly Xa and IIa. Small amounts of heparin inhibit Factor Xa, and larger amounts inhibit thrombin (Factor IIa)." ([DailyMed: Heparin Sodium And Dextrose (heparin sodium) prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eede8a0c-5ae6-4166-84b3-12081405f08e), version du 2026-05-25 ; consulté le 2026-11-19). Sur la base des connaissances pharmacologiques générales, l'héparine potentialise l'antithrombine et inhibe la thrombine ainsi que le facteur Xa. Son efficacité a été reconnue dans des états thrombotiques comme l'embolie pulmonaire.

Le déficit en protéine C entraîne la perte d'une voie anticoagulante naturelle et un état d'hypercoagulabilité. Une anticoagulation par héparine pourrait, en principe, compenser ce déséquilibre. Le lien avec l'indication d'origine est notable : le purpura fulminans est une manifestation typique du déficit sévère en protéine C.

Ce raisonnement reste toutefois théorique. Le score élevé du modèle est une prédiction computationnelle et aucune preuve directe (essai ou publication) n'a été identifiée pour cette indication.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

*Remarque : une seconde indication prédite (trouble primaire de la libération plaquettaire, score de 0,9906) est associée à 20 publications, mais celles-ci portent surtout sur la coagulation en général, la thrombopénie induite par l'héparine ou des sujets sans rapport. Aucune n'évalue l'héparine comme traitement de ce trouble. Le mécanisme est faible, voire contradictoire (l'héparine augmente le risque hémorragique), et cette piste n'est pas retenue.*

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 65476933 | HEPARINE CHOAY 25 000 UI/5 mL, solution injectable | Solution injectable | CHEPLAPHARM ARZNEIMITTEL (ALLEMAGNE) | Active |
| 63018531 | CALCIPARINE SOUS CUTANEE 25 000 UI/1 ml, solution injectable | Solution injectable | CHEPLAPHARM ARZNEIMITTEL (ALLEMAGNE) | Active |
| 65822577 | HEPARINE CHOAY 5 000 UI/1 mL, solution injectable | Solution injectable | CHEPLAPHARM ARZNEIMITTEL (ALLEMAGNE) | Active |
| 60852495 | CALCIPARINE SOUS CUTANEE 20 000 UI/0,8 ml, solution injectable | Solution injectable | CHEPLAPHARM ARZNEIMITTEL (ALLEMAGNE) | Active |
| 64395923 | HEPARINE SODIQUE PANPHARMA 5 000 UI/ml, solution injectable (I.V.) | Solution injectable | PANPHARMA | Active |
| 66346693 | HEPARINE CALCIQUE PANPHARMA 25 000 UI/mL, solution injectable (S.C.) | Solution injectable | PANPHARMA | Active |
| 64741268 | HEPARINE CALCIQUE PANPHARMA 25 000 UI/mL, solution injectable en seringue pré-remplie (S.… | Solution injectable | PANPHARMA | Active |
| 69636132 | CALCIPARINE 5 000 UI/0,2 ml, solution injectable en seringue pré-remplie (sous cutanée) | Solution injectable | CHEPLAPHARM ARZNEIMITTEL (ALLEMAGNE) | Active |
| 62187140 | CALCIPARINE 7 500 UI/0,3 ml, solution injectable en seringue pré-remplie (sous cutanée) | Solution injectable | CHEPLAPHARM ARZNEIMITTEL (ALLEMAGNE) | Active |
| 66977349 | CALCIPARINE SOUS CUTANEE 12 500 UI/0,5 ml, solution injectable | Solution injectable | CHEPLAPHARM ARZNEIMITTEL (ALLEMAGNE) | Active |
| 60810368 | FLECTOR TISSUGEL HEPARINE 1 g/40 000 UI pour 100 g, emplâtre médicamenteux | Emplâtre médicamenteux(se) | IBSA PHARMA SAS | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

Au total, 11 AMM figurent dans les données, dont 11 valides.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : insuffisance hépatique, thrombopénie, thrombopénie induite par l'héparine, hémophilie, maladies de la coagulation, déficit en antithrombine III, hémorragie intracrânienne ou intracérébrale, ulcère gastroduodénal actif, endocardite infectieuse, rétinopathie diabétique ou hypertensive, ostéoporose, rectocolite hémorragique et maladies inflammatoires chroniques de l'intestin, décollement placentaire, thrombasthénie de Glanzmann, anomalies qualitatives des plaquettes, entre autres.
- **Interactions médicamenteuses** : 614 interactions recensées. Les principales de niveau modéré concernent l'acide acétylsalicylique et plusieurs antidiabétiques (glimépiride, glipizide, glibenclamide, répaglinide, natéglinide, tolbutamide, chlorpropamide, etc.), ainsi que la fenfluramine, la dexfenfluramine et la sibutramine.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être obtenues. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication pour l'indication principale.
- Les 11 AMM françaises sont valides ; les données de sécurité officielles sont absentes, ce qui bloque l'évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Mener une revue ciblée de la littérature sur l'héparine dans le déficit en protéine C (cas cliniques, séries, recommandations).
- Clarifier le statut réglementaire actuel de l'héparine en France.
- Évaluer la compatibilité des voies d'administration et la similarité avec l'indication d'origine, aujourd'hui non évaluées.

<!-- review:begin fr-lic-20261106-heparin-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarifier le statut réglementaire actuel de l'héparine en France, les AMM étant toutes annulées. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-heparin-1 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « les AMM étant toutes annulées » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Heparin Sodium And Dextrose (heparin sodium) prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=eede8a0c-5ae6-4166-84b3-12081405f08e) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

