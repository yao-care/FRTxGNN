---
layout: default
title: Dibotermin Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 236
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Dibotermin Alfa : nouvelle indication prédite, Ésotropie (niveau de preuve L5). Indication d'origine : Trouble dégénératif des disques intervertébraux"
monitor_inn: "dibotermin alfa"
predicted_indications: ["esotropia", "HER2 positive breast carcinoma", "normal breast-like subtype of breast carcinoma", "progesterone-receptor positive breast cancer", "breast tumor luminal A or B", "progesterone-receptor negative breast cancer", "non-syndromic esophageal malformation", "multifocal choroiditis", "atypical coarctation of aorta"]
---

# Dibotermin Alfa
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

## Dibotermin alfa : De la dégénérescence discale intervertébrale et de la fracture du tibia à l'ésotropie
{: .text-alpha }

## Résumé en Une Phrase

Dibotermin alfa (BMP-2 humaine recombinante) était initialement utilisé pour la formation osseuse, notamment dans les troubles dégénératifs des disques intervertébraux et les fractures du tibia.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**ésotropie**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Trouble dégénératif des disques intervertébraux ; fracture du tibia (texte d'indication de l'AMM non disponible) |
| Nouvelle Indication Prédite | Ésotropie |
| Score de Prédiction TxGNN | 0,9997 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon ChEMBL (EMBL-EBI), le mécanisme d'action enregistré pour Dibotermin Alfa est (traduction non officielle) : « Agoniste du récepteur de type 1A des protéines morphogénétiques osseuses ; agoniste du récepteur de type 2B de l'activine ; agoniste du récepteur de type 2 des protéines morphogénétiques osseuses ; agoniste du récepteur de type 1B des protéines morphogénétiques osseuses ». Texte original en anglais : "Bone morphogenetic protein receptor type-1A agonist; Activin receptor type-2B agonist; Bone morphogenetic protein receptor type-2 agonist; Bone morphogenetic protein receptor type-1B agonist" ([ChEMBL CHEMBL2109171 (dibotermin alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2109171), CC BY-SA 3.0 ; consulté le 2026-11-19). Sur la base des informations connues, dibotermin alfa est une protéine morphogénétique osseuse de type 2 (BMP-2) recombinante. Elle agit sur les voies ostéoinductrices et stimule la formation osseuse lorsqu'elle est implantée localement sur une matrice.

L'ésotropie est un trouble de l'alignement moteur oculaire. Aucun lien mécanistique plausible n'a été identifié entre une protéine ostéoinductrice et ce trouble. Le score élevé de TxGNN reflète une prédiction du modèle TxGNN (apprentissage profond), sans élément clinique ou bibliographique à l'appui. Cette prédiction doit donc être considérée avec une grande prudence.

Les autres indications prédites présentent la même fragilité : plusieurs cancers du sein (HER2 positif, luminal A/B, récepteurs de la progestérone positifs ou négatifs, sous-type de type mammaire normal), la malformation œsophagienne non syndromique, la choroïdite multifocale et la coarctation atypique de l'aorte. Pour les cancers du sein, l'utilisation d'un facteur de croissance ostéoinducteur soulève en outre une inquiétude théorique de promotion tumorale. Pour la coarctation, une activité BMP-2 ectopique en tissu vasculaire pourrait être nocive (calcification).

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour l'ésotropie.

À titre indicatif, une seule publication a été retrouvée pour une autre indication prédite (tumeur du sein luminale A ou B) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [27441597](https://pubmed.ncbi.nlm.nih.gov/27441597/) | 2016 | Préclinique (expression génique in vitro) | European Surgical Research | Réponse génique des ostéoblastes humains au traitement par BMP2 ; jusqu'à 33 % des patients ne répondent pas à ce traitement dans les fractures complexes. Concerne la biologie osseuse, pas le cancer du sein. |

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 60897889 | INDUCTOS 1,5 mg/ml, poudre, solvant et matrice pour matrice implantable | Poudre et solvant et matrice pour matrice implantable | MEDTRONIC BIOPHARMA (PAYS-BAS) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées. Par ailleurs, une préoccupation théorique de promotion tumorale s'applique aux prédictions en oncologie (cancers du sein).

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, et sans lien mécanistique plausible entre la BMP-2 et l'ésotropie.
- Les informations de sécurité (mises en garde, contre-indications) sont absentes, ce qui bloque toute évaluation de sécurité.

<!-- review:begin fr-lic-20261106-dibotermin_alfa-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « L'unique AMM française est annulée, et les informations de sécurité (mises en garde, contre-indications) sont absentes, ce qui bloque toute évaluation de sécurité. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les nombres et statuts à jour des AMM figurent dans l'Aperçu rapide et dans le tableau des informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-dibotermin_alfa-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications)
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Mener une recherche bibliographique ciblée sur BMP-2 et l'ésotropie, et démontrer une plausibilité biologique
- Évaluer la compatibilité des voies d'administration (implant local sur matrice versus indication oculaire)
- Si les indications en oncologie du sein sont envisagées, évaluer d'abord le risque de promotion tumorale

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle).

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « 'unique AMM française est annulée, et l » | Corrigé (révisé le 2026-11-24 ; version antérieure conservée dans le journal) | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé (révisé le 2026-11-20 ; version antérieure conservée dans le journal) | [ChEMBL CHEMBL2109171 (dibotermin alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL2109171) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

