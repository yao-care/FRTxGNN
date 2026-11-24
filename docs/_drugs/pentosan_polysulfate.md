---
layout: default
title: Pentosan Polysulfate
parent: Prédiction du modèle uniquement (L5)
nav_order: 588
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "pentosan polysulfate"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease"]
description: "Pentosan Polysulfate : nouvelle indication prédite, Trouble primaire de la libération plaquettaire (primary release disorder of platelets) (niveau de preuve L5). Indication d'origine : Non renseignée…"
---

# Pentosan Polysulfate
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Pentosan Polysulfate: Trouble primaire de la libération plaquettaire (primary release disorder of platelets)
{: .text-alpha }

## Résumé en Une Phrase

Le pentosane polysulfate (ELMIRON 100 mg, gélule) était initialement utilisé pour le traitement de la **cystite interstitielle**.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble primaire de la libération plaquettaire** (« primary release disorder of platelets »).
Cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Trouble primaire de la libération plaquettaire (primary release disorder of platelets) |
| Score de Prédiction TxGNN | 0.9971 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Clinical Pharmacology » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Pentosan Polysulfate (traduction non officielle) : « Le mécanisme d'action du polysulfate de pentosane sodique dans la cystite interstitielle n'est pas connu. » Texte original en anglais : "The mechanism of action of pentosan polysulfate sodium in interstitial cystitis is not known." ([DailyMed: Elmiron (pentosan polysulfate sodium) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f0ba651e-3d8a-11df-8fbe-119855d89593), version du 2024-09-18 ; consulté le 2026-11-19). Sur la base des informations connues, le pentosane polysulfate est un polysaccharide sulfaté dont les propriétés ressemblent à celles de l'héparine : il possède une activité anticoagulante et un effet antiplaquettaire faible. Son efficacité dans la cystite interstitielle est l'indication d'origine.

**La plausibilité biologique de cette prédiction est faible.** Un composé à action anticoagulante et antiplaquettaire devrait plutôt aggraver un défaut de sécrétion plaquettaire qu'en améliorer l'évolution. L'association retrouvée par le modèle reflète probablement une proximité dans le réseau de connaissances (nœuds communs de coagulation et de fonction plaquettaire) plutôt qu'une véritable relation thérapeutique.

Le même constat s'applique aux deux autres prédictions les mieux classées, également sans aucune preuve clinique ni publication :
- **Thrombasthénie de Glanzmann** (score 0,9965) : liée à un déficit ou un dysfonctionnement de l'intégrine αIIbβ3 (GPIIb/IIIa). Un effet anticoagulant risquerait d'aggraver le phénotype hémorragique.
- **Pseudo-maladie de von Willebrand** (score 0,9962) : liée à un gain de fonction de la GPIbα plaquettaire. Une interaction du pentosane polysulfate avec le facteur von Willebrand ou les glycoprotéines plaquettaires est spéculative, et l'effet anticoagulant augmenterait le risque hémorragique.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut | Indication Approuvée |
|---------|------|------|------|-----------|
| 60027685 | ELMIRON 100 mg, gélule | Gélule | Active | Non renseignée |

Le produit est fabriqué par BENE-ARZNEIMITTEL (Allemagne). Il est commercialisé, avec 2 AMM valides sur 2.

<!-- review:begin fr-lic-20261124-pentosan_polysulfate-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « avec 1 AMM valide sur 1. » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-pentosan_polysulfate-1 -->

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de la notice) : maladie du foie, maladie de la vésicule biliaire, thrombopénie, trouble de la coagulation sanguine, hémophilie, thrombopénie induite par l'héparine.
- **Interactions médicamenteuses** : 58 interactions recensées, toutes celles listées étant de niveau modéré. Elles concernent principalement des médicaments affectant l'hémostase, avec un risque hémorragique additif :
  - Antiagrégants plaquettaires : acide acétylsalicylique, clopidogrel, cilostazol, dipyridamole, abciximab, cangrelor
  - Anticoagulants : warfarine, apixaban, édoxaban, bétrixaban, daltéparine, bivalirudine, antithrombine III
  - Thrombolytiques et autres : altéplase, anistreplase, défibrotide, caplacizumab
  - Radio-immunothérapies : ibritumomab tiuxétan, tositumomab (I-131) et tositumomab

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication. Le mécanisme anticoagulant du médicament va à l'encontre d'un bénéfice dans des troubles plaquettaires hémorragiques, et les contre-indications du graphe incluent déjà les troubles de la coagulation et la thrombopénie.

<!-- review:begin fr-lic-20261106-pentosan_polysulfate-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Le mécanisme anticoagulant du médicament va à l'encontre d'un bénéfice dans des troubles plaquettaires hémorragiques, et les contre-indications du graphe incluent déjà les troubles de la coagulation et la thrombopénie. L'AMM française est en outre annulée. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-pentosan_polysulfate-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice officielle (mises en garde et contre-indications) auprès de l'ANSM : lacune bloquante pour tout examen de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (par ex. via l'API DrugBank)
- Rechercher d'éventuelles études précliniques ou publications sur le pentosane polysulfate et la fonction plaquettaire
- Réévaluer la pertinence biologique de la prédiction avant tout investissement, compte tenu du risque hémorragique attendu
- Clarifier la compatibilité des voies d'administration et la similarité avec l'indication d'origine (actuellement non évaluées)

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « L'AMM française est en outre annulée » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Elmiron (pentosan polysulfate sodium) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f0ba651e-3d8a-11df-8fbe-119855d89593) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

