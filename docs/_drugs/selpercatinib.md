---
layout: default
title: Selpercatinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 697
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Selpercatinib : nouvelle indication prédite, Hypertension pulmonaire (niveau de preuve L5). Indication d'origine : Non renseignée dans les données compilées (texte d'indication vide po…"
monitor_inn: "SELPERCATINIB"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura"]
---

# Selpercatinib
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

## Selpercatinib : D'un inhibiteur de RET en oncologie à l'hypertension pulmonaire
{: .text-alpha }

## Résumé en Une Phrase

Selpercatinib est un inhibiteur sélectif de la kinase RET, dont les autorisations françaises (RETSEVMO) sont aujourd'hui toutes annulées. Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**hypertension pulmonaire**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutiennent directement (les 3 publications retrouvées portent sur d'autres sujets).

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données compilées (texte d'indication vide pour les 3 AMM) |
| Nouvelle Indication Prédite | Hypertension pulmonaire |
| Score de Prédiction TxGNN | 99,18 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | AMM annulées uniquement |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Selon les informations connues, selpercatinib est un inhibiteur sélectif de la kinase RET. Les publications retrouvées le situent dans le cancer du poumon non à petites cellules avec fusion de RET et dans le carcinome médullaire de la thyroïde, mais l'indication d'origine n'est pas documentée dans les données d'AMM.

Le score TxGNN est très élevé (0,992), mais il provient d'une inférence sur graphe de connaissances. Aucune voie biologique reliant l'inhibition de RET à l'hypertension pulmonaire n'a été identifiée. Le sens de l'effet est inconnu : certains inhibiteurs de kinases (par exemple le dasatinib) ont été associés à l'hypertension artérielle pulmonaire, de sorte qu'un inhibiteur de RET pourrait aussi bien aggraver la maladie que l'améliorer.

Les autres prédictions (migraine, rang 2 ; migraine avec aura du tronc cérébral, rang 3) ne reposent pas non plus sur un lien mécanistique établi. La seconde est probablement corrélée à la première et ne constitue donc pas une preuve indépendante.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Les publications ci-dessous ont été retrouvées pour ce médicament, mais aucune n'étudie l'hypertension pulmonaire.

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Étude de pharmacovigilance en vie réelle | Frontiers in Pharmacology | Comparaison des profils d'événements indésirables du pralsétinib et du selpercatinib (base FAERS) |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Analyse rétrospective | Therapeutic Advances in Medical Oncology | Étude SIREN : selpercatinib dans le CBNPC avec fusion de RET, via un programme d'accès |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Rapport de cas | Cureus | Carcinome médullaire de la thyroïde métastatique dans la NEM 2B (mutation RET M918T) : difficultés de prise en charge à long terme et thérapie ciblée |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66580529 | RETSEVMO 40 mg, gélule | Gélule | Non renseignée (AMM annulée) |
| 65136400 | RETSEVMO 80 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 61648467 | RETSEVMO 80 mg, gélule | Gélule | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de kinase RET) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions ont été recensées dans les données compilées ; les principales, de niveau majeur, concernent :
  - les antiacides et inhibiteurs de la sécrétion gastrique : famotidine, ranitidine, cimétidine, oméprazole, rabéprazole, dexlansoprazole, oxyde de magnésium ;
  - l'aprépitant ;
  - la clarithromycine ;
  - la dexaméthasone.
- Des interactions de niveau modéré concernent notamment l'hydrocortisone, la triamcinolone, la bétaméthasone, le budésonide, la pioglitazone, le lopéramide, le bisacodyl, la saxagliptine et le polyéthylène glycol.

Les mises en garde et contre-indications de la notice n'ont pas pu être obtenues : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication sur l'hypertension pulmonaire, et sans lien mécanistique identifié. Un risque d'effet inverse (aggravation) ne peut pas être exclu. Toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Données détaillées sur le mécanisme d'action (par exemple via l'API DrugBank)
- Données précliniques ou mécanistiques sur le rôle de RET dans l'hypertension pulmonaire, avec la direction de l'effet
- Revue de la littérature sur les signaux de toxicité pulmonaire ou vasculaire des inhibiteurs de kinases
- Clarification du statut réglementaire actuel et de l'indication d'origine
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

