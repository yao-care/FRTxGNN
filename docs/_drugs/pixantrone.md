---
layout: default
title: Pixantrone
parent: Prédiction du modèle uniquement (L5)
nav_order: 613
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Pixantrone : nouvelle indication prédite, Cataracte diabétique (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM disponibles"
monitor_inn: "PIXANTRONE"
predicted_indications: ["diabetic cataract"]
---

# Pixantrone
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

## Pixantrone : De l'indication d'origine non documentée à la cataracte diabétique
{: .text-alpha }

## Résumé en Une Phrase

Pixantrone est un agent antinéoplasique cytotoxique (aza-anthracènedione), dont l'indication d'origine n'est pas renseignée dans les données d'autorisation françaises compilées pour ce rapport.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **cataracte diabétique**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM disponibles |
| Nouvelle Indication Prédite | Cataracte diabétique |
| Score de Prédiction TxGNN | 0,9901 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé (autorisations annulées : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 0) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. D'après les connaissances générales, la pixantrone est une aza-anthracènedione qui agit comme inhibiteur de la topoisomérase II et agent intercalant de l'ADN. C'est un médicament cytotoxique destiné au traitement de cancers.

Aucun lien mécanistique plausible avec la cataracte diabétique n'apparaît. Cette maladie fait intervenir l'activation de la voie des polyols, l'aldose réductase, le stress oxydatif et la glycation des protéines du cristallin. Un agent cytotoxique qui endommage l'ADN n'est pas biologiquement cohérent avec une atteinte chronique non maligne du cristallin.

Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, par exemple liées au diabète ou au stress oxydatif, et non une preuve biologique. Pour une affection chronique oculaire ou métabolique, le rapport bénéfice-risque serait en outre défavorable, compte tenu de la cardiotoxicité et de la myélosuppression connues de cette classe.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69454261 | PIXUVRI 29 mg, poudre pour solution à diluer pour perfusion (LES LABORATOIRES SERVIER), statut : active | Poudre pour solution à diluer pour perfusion | Non renseignée |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (aza-anthracènedione, inhibiteur de la topoisomérase II) |
| Risque de Myélosuppression | Élevé (effet attendu de la classe) |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | NFS avec formule, fonction cardiaque (fraction d'éjection ventriculaire gauche), fonction hépatique et rénale |
| Protection de Manipulation | Suivre les réglementations de manipulation des médicaments cytotoxiques |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai ni publication, et sans lien mécanistique plausible entre un cytotoxique et la cataracte diabétique.
- Les données de sécurité de la notice sont absentes, ce qui bloque l'évaluation de sécurité initiale.

<!-- review:begin fr-lic-20261106-pixantrone-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « L'autorisation française est annulée, et les données de sécurité de la notice sont absentes, ce qui bloque l'évaluation de sécurité initiale. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 0 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-pixantrone-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice ANSM (mises en garde et contre-indications)
- Données sur le mécanisme d'action issues de DrugBank
- Données précliniques ou mécanistiques reliant la pixantrone à la physiopathologie de la cataracte diabétique
- Évaluation du rapport bénéfice-risque (cardiotoxicité, myélosuppression) pour une affection chronique non maligne
- Analyse de la compatibilité des voies d'administration (voie perfusion uniquement, non adaptée à une atteinte oculaire chronique)

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « 'autorisation française est annulée, et l » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

