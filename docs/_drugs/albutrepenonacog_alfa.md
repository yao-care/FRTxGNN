---
layout: default
title: Albutrepenonacog Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 33
evidence_level: L5
indication_count: 6
monitor_inn: "albutrepenonacog alfa"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia"]
last_modified_at: 2026-11-24
description: "Albutrepenonacog Alfa : nouvelle indication prédite, Maladie de von Willebrand de type plaquettaire (pseudo-von Willebrand disease) (niveau de preuve L5). Indication d'origine : Non renseignée dans l…"
---

# Albutrepenonacog Alfa
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
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

## Albutrepenonacog alfa : facteur IX recombinant fusionné à l'albumine → maladie de von Willebrand de type plaquettaire (pseudo-von Willebrand disease)
{: .text-alpha }

## Résumé en Une Phrase

L'albutrepenonacog alfa est une protéine de fusion recombinante associant le facteur IX de la coagulation à l'albumine, utilisée pour remplacer le facteur IX manquant.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie de von Willebrand de type plaquettaire (pseudo-von Willebrand disease)**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Maladie de von Willebrand de type plaquettaire (pseudo-von Willebrand disease) |
| Score de Prédiction TxGNN | 0,9994 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 5 sur 5) |
| Nombre d'AMM | 5 (valides : 5) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon ChEMBL (EMBL-EBI), le mécanisme d'action enregistré pour Albutrepenonacog Alfa est (traduction non officielle) : « Protéine exogène de facteur IX de coagulation ». Texte original en anglais : "Coagulation factor IX exogenous protein" ([ChEMBL CHEMBL5315076 (albutrepenonacog alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL5315076), CC BY-SA 3.0 ; consulté le 2026-11-19). Sur la base des informations connues, l'albutrepenonacog alfa est un facteur IX recombinant fusionné à l'albumine, qui remplace le facteur IX dans la cascade de coagulation.

Le lien mécanistique avec la nouvelle indication est faible. La pseudo-maladie de von Willebrand est un trouble plaquettaire causé par un gain de fonction du gène GP1BA, qui augmente la liaison des plaquettes au facteur von Willebrand. Le défaut se situe dans l'hémostase primaire (interaction plaquettes–facteur von Willebrand) et non dans un déficit en facteur IX.

Le score élevé du modèle (0,9994) reflète une prédiction fondée sur les relations entre maladies et médicaments, sans preuve clinique ou bibliographique à l'appui. Il doit donc être interprété avec une grande prudence.

## Informations de Marché en France

<!-- licenses:begin -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|------|------|------|------|------|
| 63369480 | IDELVION 3500 UI poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | CSL BEHRING (ALLEMAGNE) | Active |
| 63102506 | IDELVION 1000 UI, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | CSL BEHRING (ALLEMAGNE) | Active |
| 60216127 | IDELVION 2000 UI, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | CSL BEHRING (ALLEMAGNE) | Active |
| 61645574 | IDELVION 250 UI, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | CSL BEHRING (ALLEMAGNE) | Active |
| 65247870 | IDELVION 500 UI, poudre et solvant pour solution injectable | Poudre et solvant pour solution injectable | CSL BEHRING (ALLEMAGNE) | Active |

Source : Base de données publique des médicaments (BDPM), statut administratif de l'AMM ; AMM actives en premier.

<!-- licenses:end -->

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle, sans essai clinique ni publication. Le mécanisme du médicament (remplacement du facteur IX) ne correspond pas au défaut plaquettaire de cette maladie, ce qui place le niveau de preuve à L5.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action
- Informations de sécurité issues de la notice officielle (mises en garde et contre-indications)
- Données précliniques ou études de mécanisme montrant un bénéfice du facteur IX dans les troubles de l'adhésion plaquettaire au facteur von Willebrand
- Évaluation de la compatibilité de la voie d'administration et de la similarité avec l'indication d'origine

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé (révisé le 2026-11-20 ; version antérieure conservée dans le journal) | [ChEMBL CHEMBL5315076 (albutrepenonacog alfa): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL5315076) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

