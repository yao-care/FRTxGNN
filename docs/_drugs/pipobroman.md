---
layout: default
title: Pipobroman
parent: Prédiction du modèle uniquement (L5)
nav_order: 608
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Pipobroman : nouvelle indication prédite, Cataracte diabétique (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées (usage historique : p…"
monitor_inn: "PIPOBROMAN"
predicted_indications: ["diabetic cataract"]
drugbank_id: DB00236
---

# Pipobroman
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

## Pipobroman : D'un usage antineoplasique à la Cataracte diabétique
{: .text-alpha }

## Résumé en Une Phrase

Pipobroman est un agent cytotoxique de type alkylant, historiquement utilisé dans les syndromes myéloprolifératifs (polyglobulie de Vaquez, thrombocytémie essentielle).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **cataracte diabétique**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées (usage historique : polyglobulie de Vaquez et thrombocytémie essentielle) |
| Nouvelle Indication Prédite | Cataracte diabétique |
| Score de Prédiction TxGNN | 0,9901 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon ChEMBL (EMBL-EBI), le mécanisme d'action enregistré pour Pipobroman est (traduction non officielle) : « Inhibiteur de l'ADN » Texte original en anglais : "DNA inhibitor" ([ChEMBL CHEMBL1585 (pipobroman): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1585), CC BY-SA 3.0 ; consulté le 2026-11-19). Sur la base des informations connues, le pipobroman est un dérivé de la pipérazine à activité cytotoxique de type alkylant, utilisé dans des affections myéloprolifératives. Son action repose sur l'alkylation de l'ADN et une myélosuppression.

Aucun lien mécanistique n'est établi avec la cataracte diabétique. Cette dernière résulte principalement de l'activation de la voie des polyols (aldose réductase), de l'accumulation de sorbitol et d'un stress osmotique et oxydatif dans le cristallin. L'activité alkylante et myélosuppressive du pipobroman n'a pas de connexion reconnue avec ces processus.

Le score élevé (0,9901) est une sortie du modèle TxGNN (apprentissage profond) et peut refléter des similitudes apprises par le modèle entre maladies apparentées, et non une preuve biologique. Tout lien proposé serait spéculatif et devrait être validé in vitro ou sur modèle animal avant toute autre considération.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60195398 | VERCYTE 25 mg, comprimé (LABORATOIRES DELBERT) – active | Comprimé | Non renseignée |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication, et sans lien mécanistique plausible. De plus, le produit n'est plus autorisé en France et son profil cytotoxique rend un repositionnement dans une pathologie non cancéreuse peu favorable.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (interrogation de DrugBank)
- Mises en garde et contre-indications issues de la notice de l'ANSM (lacune bloquante pour tout dépistage de sécurité)
- Preuves précliniques (in vitro ou modèle animal de cataracte diabétique) justifiant un lien biologique
- Évaluation de la compatibilité de voie d'administration (une forme orale est a priori peu adaptée à une atteinte du cristallin)
- Analyse du rapport bénéfice/risque, compte tenu de la toxicité cytotoxique du médicament

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [ChEMBL CHEMBL1585 (pipobroman): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1585) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

