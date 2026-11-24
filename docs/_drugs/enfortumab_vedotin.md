---
layout: default
title: Enfortumab Vedotin
parent: Prédiction du modèle uniquement (L5)
nav_order: 282
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Enfortumab Vedotin : nouvelle indication prédite, Lèpre (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "enfortumab vedotin"
predicted_indications: ["leprosy", "multiple endocrine neoplasia", "cytomegalovirus infection", "candidiasis", "cerebral infarction", "HIV infectious disease", "homozygous familial hypercholesterolemia", "malignant catarrh", "infectious bovine rhinotracheitis"]
---

# Enfortumab Vedotin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

## Enfortumab vedotin : D'un médicament antinéoplasique à la lèpre (prédiction non étayée)
{: .text-alpha }

## Résumé en Une Phrase

L'enfortumab vedotin est un conjugué anticorps-médicament ciblant la Nectine-4 et délivrant la MMAE (un agent perturbateur des microtubules). Les données compilées pour ce rapport ne précisent pas d'indication originale (aucun texte d'indication n'est renseigné dans les AMM françaises).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **lèpre**, mais **aucun essai clinique** et **aucune publication** ne soutiennent cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Lèpre |
| Score de Prédiction TxGNN | 0,9953 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Enfortumab Vedotin (traduction non officielle) : « L'enfortumab védotine-ejfv est un ADC. L'anticorps est une IgG1 kappa humaine dirigée contre Nectin-4, une protéine d'adhésion située à la surface des cellules. La petite molécule, la MMAE, est un agent perturbateur des microtubules, fixée à l'anticorps par un lieur clivable par les protéases. » Texte original en anglais : "Enfortumab vedotin-ejfv is an ADC. The antibody is a human IgG1 kappa directed against Nectin-4, an adhesion protein located on the surface of cells. The small molecule, MMAE, is a microtubule-disrupting agent, attached to the antibody via a protease-cleavable linker." ([DailyMed: Padcev Ejfv (enfortumab vedotin) prescribing information, SEAGEN INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b5631d3e-4604-4363-8f20-11dfc5a4a8ed), version du 2026-08-04 ; consulté le 2026-11-19). D'après les informations connues, l'enfortumab vedotin est un conjugué anticorps-médicament dirigé contre la Nectine-4, qui libère la MMAE, un agent cytotoxique perturbant les microtubules, dans les cellules tumorales exprimant cette cible.

Aucun lien mécanistique n'est établi entre ce mode d'action et l'infection par *Mycobacterium leprae*. Rien dans les données ne relie le ciblage de la Nectine-4 ou la délivrance d'une charge cytotoxique à la lèpre. Le score TxGNN élevé (0,9953) reflète vraisemblablement des artefacts liés à la structure du réseau de connaissances plutôt qu'une plausibilité biologique.

Les autres prédictions du modèle (néoplasie endocrinienne multiple, infection à cytomégalovirus, candidose, infarctus cérébral, infection par le VIH, hypercholestérolémie familiale homozygote, etc.) présentent le même constat : aucun essai clinique, aucun rationnel mécanistique, et le niveau de preuve reste L5 pour toutes.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la lèpre.

À titre d'information, deux publications liées à d'autres indications prédites sont des signaux de sécurité et non des preuves thérapeutiques :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [42647281](https://pubmed.ncbi.nlm.nih.gov/42647281/) | 2026 | Rapport de cas | Reports (MDPI) | Œsophagite ulcérative diffuse sévère sous enfortumab vedotin et pembrolizumab dans le carcinome urothélial métastatique (événement indésirable) |
| [41341429](https://pubmed.ncbi.nlm.nih.gov/41341429/) | 2025 | Pharmacovigilance (FAERS) | Clinical Epidemiology | Signaux de risque des conjugués anticorps-médicament dans le cancer de la vessie en vie réelle |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 67032044 | PADCEV 20 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | ASTELLAS PHARMA EUROPE (PAYS-BAS) | Active |
| 67688034 | PADCEV 30 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | ASTELLAS PHARMA EUROPE (PAYS-BAS) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Conjugué anticorps-médicament (thérapie ciblée) avec charge cytotoxique (MMAE) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter la notice (NFS, fonction hépatique et rénale, glycémie à envisager) |
| Protection de Manipulation | Manipulation selon les réglementations applicables aux médicaments cytotoxiques |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 147 interactions recensées. Parmi celles listées, une est de niveau **majeur** (clarithromycine) ; les autres sont de niveau **modéré**, notamment les antidiabétiques (acarbose, metformine, pioglitazone, glimépiride, glipizide, glibenclamide, inhibiteurs de la DPP-4, inhibiteurs du SGLT2, analogues du GLP-1) et l'aprépitant.

Les mises en garde et contre-indications de la notice ne sont pas disponibles dans les données compilées ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la lèpre repose uniquement sur le score du modèle, sans essai, sans publication ni lien mécanistique. Le niveau de preuve est L5.

<!-- review:begin fr-lic-20261106-enfortumab_vedotin-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Le niveau de preuve est L5, et les AMM françaises sont toutes annulées. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-enfortumab_vedotin-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (DrugBank) et analyse d'un éventuel lien Nectine-4 / infection mycobactérienne
- Mises en garde et contre-indications issues de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Données précliniques ou études de mécanisme justifiant la plausibilité biologique avant tout essai clinique

<!-- review:begin fr-lic-20261106-enfortumab_vedotin-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Mises en garde et contre-indications issues de la notice ANSM (lacune bloquante pour le criblage de sécurité) / Indications originales approuvées et clarification du statut des AMM annulées » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-enfortumab_vedotin-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « et les AMM françaises sont toutes annulées » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « Indications originales approuvées et clarification du statut des AMM annulées » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Padcev Ejfv (enfortumab vedotin) prescribing information, SEAGEN INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b5631d3e-4604-4363-8f20-11dfc5a4a8ed) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

