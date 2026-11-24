---
layout: default
title: Eptifibatide
parent: Prédiction du modèle uniquement (L5)
nav_order: 290
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "EPTIFIBATIDE"
predicted_indications: ["rheumatoid arthritis", "sickle cell-hemoglobin E disease syndrome", "sickle cell-hemoglobin c disease syndrome", "sickle cell-hemoglobin d disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "hemoglobinopathy", "female breast carcinoma", "beta-thalassemia with other manifestations", "partial deletion of the short arm of chromosome 16"]
description: "Eptifibatide : nouvelle indication prédite, Polyarthrite rhumatoïde (rheumatoid arthritis) (niveau de preuve L5). En France, AMM dans la BDPM : 4 (valides : 2)"
---

# Eptifibatide
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

## Eptifibatide: Polyarthrite rhumatoïde (rheumatoid arthritis)
{: .text-alpha }

## Résumé en Une Phrase

L'eptifibatide est un antagoniste des récepteurs GPIIb/IIIa (antiagrégant plaquettaire injectable), initialement utilisé dans le **syndrome coronarien aigu**.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **polyarthrite rhumatoïde**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Polyarthrite rhumatoïde (rheumatoid arthritis) |
| Score de Prédiction TxGNN | 0.9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 4) |
| Nombre d'AMM | 4 (valides : 2) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Eptifibatide (traduction non officielle) : « L'eptifibatide inhibe de manière réversible l'agrégation plaquettaire en empêchant la liaison du fibrinogène, du facteur von Willebrand et d'autres ligands adhésifs à la GP IIb/IIIa. Administré par voie intraveineuse, l'eptifibatide inhibe l'agrégation plaquettaire ex vivo de manière dose- et concentration-dépendante. » Texte original en anglais : "Eptifibatide reversibly inhibits platelet aggregation by preventing the binding of fibrinogen, von Willebrand factor, and other adhesive ligands to GP IIb/IIIa. When administered intravenously, eptifibatide inhibits ex vivo platelet aggregation in a dose- and concentration-dependent manner." ([DailyMed: eptifibatide prescribing information, Avenacy, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c0781dae-3ef6-4cab-b084-01d2e45f3764), version du 2026-10-02 ; consulté le 2026-11-19). D'après les connaissances générales, l'eptifibatide bloque le récepteur GPIIb/IIIa (intégrine αIIbβ3) des plaquettes et empêche leur agrégation. Cette action explique son utilité dans le syndrome coronarien aigu.

Le lien avec la polyarthrite rhumatoïde reste **spéculatif**. L'inflammation d'origine plaquettaire et la signalisation des intégrines pourraient jouer un rôle dans l'inflammation synoviale, mais aucune donnée clinique ou bibliographique n'a été trouvée pour étayer cette hypothèse. La similarité entre l'indication d'origine (maladie cardiovasculaire thrombotique) et la nouvelle indication (maladie auto-immune articulaire) n'a pas pu être évaluée.

À titre d'information, parmi les autres indications prédites, l'**hémoglobinopathie** (drépanocytose) est la mieux documentée (niveau L2, voir la conclusion). Elle repose sur le rôle de l'activation plaquettaire dans les crises vaso-occlusives.

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
| 67185951 | EPTIFIBATIDE ACCORD 2 mg/ml | Solution injectable | Active | Non renseignée |
| 61707499 | EPTIFIBATIDE ACCORD 0,75 mg/ml | Solution pour perfusion | Active | Non renseignée |

Des 4 AMM recensées, 2 sont valides (ACCORD HEALTHCARE, Espagne, spécialités à base d'eptifibatide seul) et 2 sont abrogées (INTEGRILIN, GlaxoSmithKline).

<!-- review:begin fr-lic-20261124-eptifibatide-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « Les deux AMM appartiennent à ACCORD HEALTHCARE (Espagne) et concernent des spécialités à base d'eptifibatide seul. » Corrigé d'après la BDPM (fichiers complets du 2026-11-24) : les AMM de ce médicament ont été complétées par code de substance BDPM (certaines n'étaient pas reprises dans les données compilées) ; les chiffres actuels figurent dans le Résumé rapide. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-eptifibatide-1 -->

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : thrombocytopénie, maladie de la coagulation, insuffisance rénale.
- **Interactions médicamenteuses** (100 interactions recensées, principales citées) :
  - **Majeures** : déférasirox, ibritumomab tiuxétan, tositumomab (I-131).
  - **Modérées** : acide acétylsalicylique, dexfenfluramine, fenfluramine, sibutramine.
  - D'autres interactions, de niveau non précisé, concernent notamment les inhibiteurs de la pompe à protons (oméprazole, pantoprazole, lansoprazole), la morphine, la simvastatine et la prednisone.

Le risque hémorragique inhérent à tout antiagrégant doit être pris en compte. Pour les mises en garde officielles, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la polyarthrite rhumatoïde repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication. Le profil de risque hémorragique, et les contre-indications relevées dans le graphe de connaissances, pèsent contre une avancée sans données solides.
- L'hémoglobinopathie (drépanocytose) est la piste la mieux étayée, avec un essai de phase 1/2 randomisé (NCT00834899, arrêté prématurément après 13 patients) et trois études pilotes ou de phase I. L'efficacité n'y est pas démontrée, et aucune donnée de phase 3 n'existe. Elle mérite d'être traitée comme une question de recherche à part entière.

<!-- review:begin fr-lic-20261106-eptifibatide-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Le profil de risque hémorragique, et les contre-indications relevées dans le graphe de connaissances, pèsent contre une avancée sans données solides. / L'eptifibatide n'a plus d'AMM valide en France, ce qui complique tout développement local. » Supprimé : le nombre ou le statut des AMM indiqué ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 2 AMM pour ce médicament, dont 2 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-eptifibatide-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer le texte de la notice (mises en garde, contre-indications, indications) auprès de l'ANSM, pour permettre un premier examen de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank.
- Réaliser une revue de la littérature ciblée sur le rôle des plaquettes et de GPIIb/IIIa dans la polyarthrite rhumatoïde, puis des études précliniques si elle est concluante.
- Clarifier la situation réglementaire (abrogation des AMM) et la disponibilité du produit en France.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « L'eptifibatide n'a plus d'AMM valide en France, ce qui complique tout développement local » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: eptifibatide prescribing information, Avenacy, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c0781dae-3ef6-4cab-b084-01d2e45f3764) |
| 2026-11-24 | Nombre d'AMM mis à jour | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

