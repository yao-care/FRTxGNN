---
layout: default
title: Palonosetron
parent: Preuves modérées (L3-L4)
nav_order: 574
evidence_level: L4
indication_count: 4
last_modified_at: 2026-11-24
description: "Palonosetron : nouvelle indication prédite, Migraine (« migraine disorder ») (niveau de preuve L4). Indication d'origine : Non renseignée dans les données d'AMM compilées"
monitor_inn: "palonosetron"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis"]
---

# Palonosetron
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **4** 
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

## Palonosétron : Des Nausées et Vomissements Induits par la Chimiothérapie à la Migraine
{: .text-alpha }

## Résumé en Une Phrase

Le palonosétron est un antagoniste des récepteurs 5-HT3, commercialisé en France sous le nom d'ALOXI en solution injectable. Le texte de son indication autorisée n'est toutefois pas renseigné dans les données compilées pour ce rapport.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **migraine** (score élevé), mais **aucun essai clinique** n'existe et la seule publication associée est un **rapport de cas** décrivant une céphalée de type migraineux *induite* par le palonosétron, c'est-à-dire un signal d'effet indésirable plutôt que de bénéfice.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Migraine (« migraine disorder ») |
| Score de Prédiction TxGNN | 0,9974 |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Commercialisé (autorisations valides : 5 sur 5) |
| Nombre d'AMM | 5 (valides : 5) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Palonosetron (traduction non officielle) : « Le palonosétron est un antagoniste des récepteurs 5-HT 3 doté d'une forte affinité de liaison pour ce récepteur et d'une affinité faible ou nulle pour les autres récepteurs. La chimiothérapie anticancéreuse peut être associée à une incidence élevée de nausées et de vomissements, en particulier lorsque certains agents, tels que le cisplatine, sont utilisés. » Texte original en anglais : "Palonosetron is a 5-HT 3 receptor antagonist with a strong binding affinity for this receptor and little or no affinity for other receptors. Cancer chemotherapy may be associated with a high incidence of nausea and vomiting, particularly when certain agents, such as cisplatin, are used." ([DailyMed: Posfrea (palonosetron) prescribing information, Avyxa Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=13a201ba-c86d-48c5-a0e1-a3e0b4e6a2a7), version du 2025-04-29 ; consulté le 2026-11-19). Sur la base des informations connues, le palonosétron fait partie de la classe des antagonistes des récepteurs 5-HT3 (sétrons), utilisés comme antiémétiques, et son blocage de la sérotonine au niveau de ces récepteurs pourrait, sur le plan théorique, être lié à la physiopathologie de la migraine.

Le lien est plausible mais non démontré. Les voies sérotoninergiques et trigémino-vasculaires interviennent dans la migraine, et les nausées et vomissements en sont une comorbidité fréquente. Le score provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, et non une preuve biologique.

Il faut cependant rester prudent. Le score TxGNN est très élevé (0,9974), mais la seule publication spécifique rapporte une céphalée de type migraineux déclenchée par le palonosétron. Ce signal va dans le sens opposé à un bénéfice thérapeutique. Les autres prédictions (migraine avec aura du tronc cérébral, atrophodermie vermiculée, ulérythème ophryogène) reposent sur la seule prédiction informatique, sans mécanisme plausible. Les deux dernières semblent refléter des similarités apprises par le modèle TxGNN (apprentissage profond) entre maladies apparentées, et non des preuves biologiques.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Rapport de cas | Canadian Journal of Anaesthesia | Céphalée de type migraineux induite par le palonosétron : signal d'effet indésirable, non d'efficacité |

Une revue de 2026 ([42748473](https://pubmed.ncbi.nlm.nih.gov/42748473/), *European Heart Journal – Cardiovascular Pharmacotherapy*) porte sur l'allongement de l'intervalle QT associé aux antiémétiques. Elle est liée à la prédiction « susceptibilité à la migraine avec ou sans aura ». Elle relève de la sécurité et n'apporte aucune preuve d'efficacité dans la migraine.

---

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 61794949 | ALOXI 250 microgrammes, solution injectable | Solution injectable | HELSINN BIREX PHARMACEUTICALS | Active |
| 67538668 | PALONOSETRON KALCEKS 250 microgrammes, solution injectable | Solution injectable | KALCEKS (LETTONIE) | Active |
| 67044648 | PALONOSETRON REIG JOFRE 250 microgrammes, solution injectable | Solution injectable | LABORATORIO REIG JOFRE (ESPAGNE) | Active |
| 67300396 | PALONOSETRON ACCORD 250 microgrammes, solution injectable | Solution injectable | ACCORD HEALTHCARE (ESPAGNE) | Active |
| 67693946 | AKYNZEO 300 mg/0,5 mg, gélules | Gélule | HELSINN BIREX PHARMACEUTICALS | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

---

## Considérations de Sécurité

- **Interactions médicamenteuses** : 398 interactions sont recensées. Parmi celles affichées, plusieurs sont de niveau **majeur** :
  - opioïdes et apparentés : fentanyl, alfentanil, tramadol, dextrométhorphane ;
  - triptans : almotriptan, sumatriptan ;
  - médicaments à risque cardiaque ou de syndrome sérotoninergique : amiodarone, amisulpride, amitriptyline, anagrélide.
  
  Des interactions de niveau modéré concernent notamment l'abiratérone, la famotidine, le formotérol, l'adénosine, le salbutamol, l'alfuzosine, le propofol, le lopéramide, la codéine et la dihydrocodéine.
- **Allongement du QT** : la littérature récente souligne un risque d'allongement de l'intervalle QT pour la classe des antiémétiques.
- **Céphalée de type migraineux** : un cas documenté, déclenchée par le palonosétron.

Les mises en garde et contre-indications de la notice n'ont pas pu être obtenues. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est élevé, mais la prédiction repose sur aucun essai clinique et sur un seul rapport de cas indiquant un possible effet délétère (niveau de preuve L4). Les autres indications prédites sont de niveau L5.
- Les données de sécurité de la notice sont manquantes, ce qui bloque l'étape de criblage de sécurité.

<!-- review:begin fr-lic-20261106-palonosetron-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les AMM françaises sont toutes annulées, et les données de sécurité de la notice sont manquantes, ce qui bloque l'étape de criblage de sécurité. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 2 AMM pour ce médicament, dont 2 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-palonosetron-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde, contre-indications, indication autorisée).
- Obtenir les données sur le mécanisme d'action (par exemple via DrugBank).
- Examiner la littérature sur les antagonistes 5-HT3 dans la migraine pour déterminer si l'effet est protecteur ou aggravant.
- Évaluer le risque d'allongement du QT et des interactions majeures chez les patients migraineux, notamment avec les triptans.
- Clarifier la situation réglementaire et la compatibilité de la voie d'administration (injectable) avec un usage dans la migraine.

<!-- review:begin fr-lic-20261106-palonosetron-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Clarifier la situation réglementaire (AMM annulées) et la compatibilité de la voie d'administration (injectable) avec un usage dans la migraine. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 2 AMM pour ce médicament, dont 2 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-palonosetron-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « es AMM françaises sont toutes annulées, et l » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulées) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Posfrea (palonosetron) prescribing information, Avyxa Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=13a201ba-c86d-48c5-a0e1-a3e0b4e6a2a7) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

