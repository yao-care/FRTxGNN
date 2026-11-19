---
layout: default
title: Belimumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 92
evidence_level: L5
indication_count: 6
monitor_inn: "belimumab"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "severe nonproliferative diabetic retinopathy", "autosomal dominant macrothrombocytopenia"]
last_modified_at: 2026-11-20
description: "Belimumab : nouvelle indication prédite, Trouble de la libération plaquettaire primaire (primary release disorder of platelets) (niveau de preuve L5). Indication d'origine : Non renseignée dans les d…"
---

# Belimumab
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

## Belimumab : inhibiteur de BLyS (BAFF), anti-survie des lymphocytes B → trouble de la libération plaquettaire primaire (primary release disorder of platelets)
{: .text-alpha }

## Résumé en Une Phrase

Belimumab est un anticorps monoclonal dirigé contre BLyS (BAFF), un facteur de survie des lymphocytes B.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble de la libération plaquettaire primaire (primary release disorder of platelets)**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Trouble de la libération plaquettaire primaire (primary release disorder of platelets) |
| Score de Prédiction TxGNN | 0,9996 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Belimumab (traduction non officielle) : « BENLYSTA est un inhibiteur spécifique de BLyS qui bloque la liaison de BLyS soluble, un facteur de survie des lymphocytes B, à ses récepteurs sur les lymphocytes B. BENLYSTA ne se lie pas directement aux lymphocytes B, mais en se liant à BLyS, BENLYSTA inhibe la survie des lymphocytes B, y compris des lymphocytes B autoréactifs, et réduit la différenciation des lymphocytes B en plasmocytes producteurs d'immunoglobulines. » Texte original en anglais : "BENLYSTA is a BLyS-specific inhibitor that blocks the binding of soluble BLyS, a B-cell survival factor, to its receptors on B cells. BENLYSTA does not bind B cells directly, but by binding BLyS, BENLYSTA inhibits the survival of B cells, including autoreactive B cells, and reduces the differentiation of B cells into immunoglobulin-producing plasma cells." ([DailyMed: Benlysta (belimumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2fa3c528-1777-4628-8a55-a69dae2381a3), version du 2026-10-30 ; consulté le 2026-11-19). Sur la base des informations connues, le belimumab inhibe BLyS (BAFF) et réduit ainsi la survie des lymphocytes B.

Les troubles de la libération plaquettaire sont des défauts héréditaires ou intrinsèques de la fonction des plaquettes, et ne sont pas médiés par les lymphocytes B. Aucun lien mécanistique n'est étayé par les données disponibles. Le score élevé (0,9996) reflète une prédiction du modèle, probablement liée à la proximité de nœuds plaquettaires et auto-immuns, et ne constitue pas une preuve d'efficacité.

Cette prédiction doit donc être considérée comme très spéculative. Le mécanisme d'action n'étant pas renseigné, ce lien n'a pas pu être recoupé.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65592934 | BENLYSTA 120 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | Non renseignée |
| 60205159 | BENLYSTA 200 mg, solution injectable en stylo prérempli | Solution injectable | Non renseignée |
| 65600733 | BENLYSTA 400 mg, poudre pour solution à diluer pour perfusion | Poudre pour solution à diluer pour perfusion | Non renseignée |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 69 interactions recensées. Parmi les principales :
  - Majeures : adalimumab, baricitinib, certolizumab pegol, vaccin BCG (souche Tice vivante)
  - Modérées : roflumilast, azathioprine, anakinra, canakinumab, alemtuzumab, alefacept, anatoxine tétanique, vaccin contre l'anthrax, ainsi que d'autres vaccins vivants ou agents apparentés
  - Mineures : sels de zinc (acétate, gluconate, sulfate, chlorure)

Les mises en garde et contre-indications ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour les informations de sécurité complètes.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle, sans essai clinique, sans publication et sans lien mécanistique plausible entre l'inhibition de BLyS et un défaut intrinsèque de la fonction plaquettaire.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mécanisme d'action détaillé et analyse d'un éventuel lien mécanistique avec le trouble plaquettaire
- Mises en garde et contre-indications issues de la notice ANSM
- Toute donnée préclinique ou clinique portant directement sur cette maladie
- Évaluation de la compatibilité des voies d'administration et du profil de sécurité dans la population concernée

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Benlysta (belimumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2fa3c528-1777-4628-8a55-a69dae2381a3) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

