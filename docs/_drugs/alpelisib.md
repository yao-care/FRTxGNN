---
layout: default
title: Alpelisib
parent: Prédiction du modèle uniquement (L5)
nav_order: 45
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Alpelisib : nouvelle indication prédite, Hypertension pulmonaire (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM compilées"
monitor_inn: "alpelisib"
predicted_indications: ["pulmonary hypertension"]
---

# Alpelisib
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

## Alpélisib : Du cancer du sein à l'hypertension pulmonaire
{: .text-alpha }

## Résumé en Une Phrase

L'alpélisib (commercialisé sous le nom PIQRAY) est un inhibiteur de la PI3K alpha, connu en oncologie pour le traitement du cancer du sein. Les données compilées pour ce rapport n'incluent toutefois pas le texte de l'indication approuvée en France.
Le modèle TxGNN le prédit comme potentiellement efficace pour l'**hypertension pulmonaire**, mais cette prédiction ne repose sur **aucun essai clinique** et sur **une seule publication**, qui décrit un effet indésirable pulmonaire et non un bénéfice.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM compilées |
| Nouvelle Indication Prédite | Hypertension pulmonaire |
| Score de Prédiction TxGNN | 99,03 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. Sur la base des connaissances générales, l'alpélisib est un inhibiteur de la sous-unité alpha de la PI3K, et la voie PI3K/AKT/mTOR est impliquée dans la prolifération des cellules musculaires lisses et endothéliales ainsi que dans le remodelage vasculaire pulmonaire. Cela rend l'hypothèse mécanistique plausible.

Ce lien reste toutefois **purement hypothétique** : aucune donnée fournie ne le confirme. Le score TxGNN est très élevé (0,990), mais il s'agit d'une prédiction de modèle uniquement, sans étude réelle à l'appui.

Un point de vigilance important : la seule publication retrouvée rapporte une **pneumopathie interstitielle induite par l'alpélisib**. Ce signal de toxicité pulmonaire va à l'encontre de l'hypothèse de repositionnement tant qu'il n'est pas clarifié.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Rapport de cas | Journal of Oncology Pharmacy Practice | Pneumopathie interstitielle induite par l'alpélisib chez une patiente atteinte d'un cancer du sein avancé. Effet indésirable, sans preuve de bénéfice dans l'hypertension pulmonaire. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69009763 | PIQRAY 200 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 62444026 | PIQRAY 150 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 62801026 | PIQRAY 50 mg et 200 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de la PI3K alpha) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Signal de toxicité pulmonaire** : un cas de pneumopathie interstitielle induite par l'alpélisib est rapporté dans la littérature, ce qui constitue une préoccupation directe pour une indication pulmonaire.
- **Interactions Médicamenteuses** : 284 interactions ont été recensées. Parmi celles listées, toutes sont de niveau modéré, notamment avec des antidiabétiques (acarbose, metformine, pioglitazone, glimépiride, glipizide, canagliflozine, dapagliflozine, empagliflozine, exénatide, dulaglutide, albiglutide, alogliptine, acétohexamide, chlorpropamide), ainsi qu'avec la dexaméthasone, le bupropion, l'alosétron, le dronabinol et la fidaxomicine.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni preuve de bénéfice, et la seule publication disponible signale une toxicité pulmonaire. Toutes les AMM françaises sont par ailleurs annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications de la notice ANSM (lacune bloquante pour le criblage de sécurité)
- Données sur le mécanisme d'action (DrugBank)
- Études précliniques de l'inhibition de la PI3Kα dans des modèles d'hypertension pulmonaire
- Analyse du risque de pneumopathie interstitielle/pneumonite et de sa compatibilité avec une population atteinte d'hypertension pulmonaire
- Clarification des voies d'administration et de la compatibilité avec la nouvelle indication
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

