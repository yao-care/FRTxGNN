---
layout: default
title: Quinapril
parent: Prédiction du modèle uniquement (L5)
nav_order: 643
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "QUINAPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
description: "Quinapril : nouvelle indication prédite, Malignant hypertensive renal disease (niveau de preuve L5). En France, AMM dans la BDPM : 2 (valides : 0)"
---

# Quinapril
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

## Quinapril: Malignant hypertensive renal disease
{: .text-alpha }

## Résumé en Une Phrase

Quinapril est un inhibiteur de l'enzyme de conversion de l'angiotensine (IEC), initialement utilisé pour le traitement de l'hypertension artérielle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension rénovasculaire maligne**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette indication précise : la prédiction repose uniquement sur le modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Malignant hypertensive renal disease |
| Score de Prédiction TxGNN | 0.9986 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé (autorisations annulées : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 0) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Quinapril (traduction non officielle) : « Le quinapril est désestérifié en son principal métabolite, le quinaprilate, qui est un inhibiteur de l'activité de l'ECA chez l'homme et l'animal. L'ECA est une peptidyl dipeptidase qui catalyse la conversion de l'angiotensine I en un vasoconstricteur, l'angiotensine II. » Texte original en anglais : "Quinapril is deesterified to the principal metabolite, quinaprilat, which is an inhibitor of ACE activity in human subjects and animals. ACE is apeptidyl dipeptidase that catalyzes the conversion of angiotensin I to the vasoconstrictor, angiotensin II." ([DailyMed: quinapril prescribing information, Proficient Rx LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f33dbbb1-1a4a-42b0-a5c5-3ac905823206), version du 2021-01-01 ; consulté le 2026-11-19). Sur la base des connaissances générales, le quinapril appartient à la classe des IEC : il bloque la transformation de l'angiotensine I en angiotensine II, un puissant vasoconstricteur, et réduit ainsi la pression artérielle.

L'hypertension rénovasculaire est en grande partie entretenue par l'activation du système rénine-angiotensine. Le blocage de ce système est donc biologiquement plausible. Il faut toutefois souligner que cette prédiction est essentiellement une extension de l'indication déjà connue (l'hypertension), et non une indication réellement nouvelle sur le plan mécanistique.

Une réserve importante s'impose : les IEC peuvent provoquer une dégradation aiguë de la fonction rénale en cas de sténose bilatérale des artères rénales. Cette population exigerait donc une grande prudence. Le score élevé du modèle (0,9986) reste une simple prédiction.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour l'hypertension rénovasculaire maligne.

## Autres Indications Prédites (pour information)

| Rang | Maladie Prédite | Score TxGNN | Niveau de Preuve | Recommandation |
|------|------|------|------|------|
| 2 | Néphropathie hypertensive maligne | 0,9986 | L5 | Hold |
| 3 | Hypertension pulmonaire liée à une maladie pulmonaire et/ou à l'hypoxie | 0,9985 | L5 | Question de recherche |
| 4 | Hypertension pulmonaire à mécanisme multifactoriel mal défini | 0,9985 | L5 | Hold |
| 5 | Syndrome de Braddock | 0,9979 | L5 | Hold |

Seule l'hypertension pulmonaire liée à une maladie pulmonaire ou à l'hypoxie dispose de données de littérature, exclusivement précliniques :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [8873672](https://pubmed.ncbi.nlm.nih.gov/8873672/) | 1996 | Étude animale | Circulation | L'inhibition de l'ECA tissulaire par le quinapril réduit l'hypertension pulmonaire hypoxique et le remodelage vasculaire pulmonaire |
| [8720418](https://pubmed.ncbi.nlm.nih.gov/8720418/) | 1996 | Étude animale | J Cardiovasc Pharmacol | Préservation de la fonction mécanique et du métabolisme énergétique du ventricule gauche chez le rat après infarctus du myocarde (pertinence indirecte) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62206135 | ACUITEL 5 mg, comprimé enrobé sécable (archivée) | Comprimé enrobé sécable | Non précisée |
| 62927128 | ACUITEL 20 mg, comprimé enrobé sécable (archivée) | Comprimé enrobé sécable | Non précisée |

<!-- review:begin fr-row-20261112-quinapril-1 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « ACUITEL 5 mg, comprimé enrobé sécable (active) » Selon la BDPM (données du 2026-11-23 ; fiche produit consultée le 2026-11-24), l’AMM 62206135 (ACUITEL 5 mg, comprimé enrobé sécable) a le statut « Autorisation archivée ». Source: [Base de données publique des médicaments (BDPM) – fiche 62206135](https://base-donnees-publique.medicaments.gouv.fr/medicament/62206135/extrait).

<!-- review:end fr-row-20261112-quinapril-1 -->

<!-- review:begin fr-row-20261112-quinapril-2 -->

> **Correction de vérification (2026-11-24)**: Texte initial : « ACUITEL 20 mg, comprimé enrobé sécable (active) » Selon la BDPM (données du 2026-11-23 ; fiche produit consultée le 2026-11-24), l’AMM 62927128 (ACUITEL 20 mg, comprimé enrobé sécable) a le statut « Autorisation archivée ». Source: [Base de données publique des médicaments (BDPM) – fiche 62927128](https://base-donnees-publique.medicaments.gouv.fr/medicament/62927128/extrait).

<!-- review:end fr-row-20261112-quinapril-2 -->

<!-- review:begin fr-lic-20261124-quinapril-1 -->

> **Note de vérification (2026-11-24)**: Les données compilées pour ce rapport ne contiennent que les deux AMM ACUITEL (62206135, 62927128), archivées le 27-04-2025 ; le statut « Non commercialisé » du Résumé rapide ne porte que sur ces deux AMM. D’après la BDPM (fichiers complets consultés le 2026-11-24), QUINAPRIL BIOGARAN 20 mg (61168571) a le statut « Autorisation active », ainsi que deux associations quinapril/hydrochlorothiazide 20 mg/12,5 mg (EG 60455586, ARROW LAB 69777040). Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement).

<!-- review:end fr-lic-20261124-quinapril-1 -->

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : angiœdème (y compris héréditaire, acquis et induit par les bloqueurs du système rénine-angiotensine-aldostérone), insuffisance rénale, anurie, maladie hépatique, encéphalopathie hépatique, pancréatite, maladie de la vésicule biliaire, lupus érythémateux systémique, maladies du tissu conjonctif, diabète et acidocétose diabétique, carence en potassium, goutte, neutropénie, agranulocytose, hypotension, hyperparathyroïdie, ainsi que l'ictère néonatal.
- **Interactions médicamenteuses** : 100 interactions ont été recensées. Parmi les principales :
  - **Majeure** : citrate de potassium (risque d'hyperkaliémie).
  - **Modérées** : metformine, canagliflozine, dapagliflozine, chlorpropamide, acide acétylsalicylique, corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, budésonide), doxycycline, tétracycline, bupropion, morphine, atropine, ainsi que plusieurs laxatifs et préparations de lavage intestinal.
- **Point d'attention propre à l'indication** : risque de dégradation aiguë de la fonction rénale en cas de sténose bilatérale des artères rénales.

Les mises en garde et contre-indications issues de la notice française n'ont pas pu être obtenues ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction est plausible mais prolonge largement l'indication hypertensive déjà connue, sans aucun essai ni publication spécifique. Le niveau de preuve est L5.
- Les données de sécurité de la notice sont absentes, ce qui bloque une évaluation de sécurité complète.

<!-- review:begin fr-lic-20261106-quinapril-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les AMM françaises sont toutes annulées et les données de sécurité de la notice sont absentes, ce qui bloque une évaluation de sécurité complète. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 2 AMM pour ce médicament, dont 0 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-quinapril-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications.
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank).
- Rechercher des études cliniques ou observationnelles sur l'hypertension rénovasculaire maligne.
- Évaluer le risque rénal chez les patients atteints de sténose bilatérale des artères rénales.
- Clarifier la disponibilité du produit en France.
- Si une piste alternative est envisagée, l'hypertension pulmonaire liée à l'hypoxie (L4) pourrait constituer une question de recherche, à valider d'abord par des études chez l'humain.

<!-- review:begin fr-lic-20261106-quinapril-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarifier la disponibilité du produit en France, puisque seules des AMM annulées sont recensées. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 2 AMM pour ce médicament, dont 0 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-quinapril-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « es AMM françaises sont toutes annulées et l » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « puisque seules des AMM annulées sont recensées » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-24 | Tableau : l’AMM 62206135 (ACUITEL 5 mg) est archivée, non active | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – fiche 62206135](https://base-donnees-publique.medicaments.gouv.fr/medicament/62206135/extrait) |
| 2026-11-24 | Tableau : l’AMM 62927128 (ACUITEL 20 mg) est archivée, non active | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – fiche 62927128](https://base-donnees-publique.medicaments.gouv.fr/medicament/62927128/extrait) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: quinapril prescribing information, Proficient Rx LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f33dbbb1-1a4a-42b0-a5c5-3ac905823206) |
| 2026-11-24 | Autres AMM de quinapril actives dans la BDPM | Note ajoutée | [Base de données publique des médicaments (BDPM) – CIS_bdpm.txt et CIS_COMPO_bdpm.txt](https://base-donnees-publique.medicaments.gouv.fr/telechargement) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

