---
layout: default
title: Lorlatinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 465
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lorlatinib : nouvelle indication prédite, Fibromatose gingivale (niveau de preuve L5). Indication d'origine : Cancer bronchique non à petites cellules (CBNPC) / cancer du poumon"
monitor_inn: "LORLATINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Lorlatinib
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

# Lorlatinib : Du Cancer Bronchique Non à Petites Cellules à la Fibromatose Gingivale

## Résumé en Une Phrase

Lorlatinib est un inhibiteur de tyrosine kinase de troisième génération ciblant ALK et ROS1, initialement utilisé pour le traitement du cancer bronchique non à petites cellules (CBNPC) et du cancer du poumon.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **fibromatose gingivale**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer bronchique non à petites cellules (CBNPC) / cancer du poumon |
| Nouvelle Indication Prédite | Fibromatose gingivale |
| Score de Prédiction TxGNN | 99,81 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Autorisations annulées uniquement |
| Nombre d'AMM | 2 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances établies, lorlatinib est un inhibiteur de ALK et ROS1, dont l'efficacité dans le CBNPC ALK-positif a été démontrée, notamment par l'essai de phase 3 CROWN.

En revanche, **aucun lien mécanistique n'a été identifié** avec la fibromatose gingivale : aucune pathologie dépendante d'ALK n'est établie dans cette maladie. Le score élevé du modèle (99,81 %) est une prédiction purement computationnelle, non étayée par des essais ou des publications. Cette prédiction doit donc être considérée comme très spéculative.

Parmi les autres prédictions examinées, certaines reposent sur des preuves apparentées mais ne constituent pas du repositionnement au sens strict. Pour le « néoplasme bénin du poumon », les essais de phase 3 portent sur le CBNPC ALK-positif (l'indication d'origine) et non sur la maladie bénigne : il s'agit probablement d'un artefact d'ontologie des maladies. Pour la « tumeur germinale du poumon », la littérature concerne le neuroblastome ALK-dépendant, ce qui soutient l'idée d'un usage dans d'autres tumeurs pilotées par ALK, mais pas dans les tumeurs germinales.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la fibromatose gingivale.

À titre de contexte, les publications retrouvées pour les autres prédictions concernent l'indication d'origine (CBNPC ALK-positif, par exemple l'étude CROWN, PMID 33207094) ou le neuroblastome ; elles ne constituent pas des preuves en faveur de la fibromatose gingivale.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63776483 | LORVIQUA 25 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |
| 66586838 | LORVIQUA 100 mg, comprimé pelliculé | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase ALK/ROS1) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter la notice. La littérature signale des effets métaboliques (hypercholestérolémie, hypertriglycéridémie) justifiant un suivi lipidique |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions ont été recensées. Parmi celles listées, les interactions de niveau **majeur** concernent la **dexaméthasone** et la **clarithromycine**. Des interactions de niveau modéré concernent notamment l'hydrocortisone, la bétaméthasone, la triamcinolone, l'aprépitant, le bupropion, la cimétidine, la morphine, l'alosétron, la dapagliflozine, l'empagliflozine, la saxagliptine, la linagliptine, le glimépiride, le chlorpropamide, le dronabinol, l'éliglustat, le naldémédine et le naloxégol.
- **Signaux de sécurité issus de la littérature** : dyslipidémie et effets métaboliques, toxicité pulmonaire (dont syndrome de détresse respiratoire aiguë rapporté), réactions cutanées d'origine médicamenteuse (syndrome de Sweet), et toxicité pulmonaire en association avec un anticorps anti-GD2.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la fibromatose gingivale repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication ni lien mécanistique plausible. De plus, les AMM françaises sont toutes annulées et les données de sécurité officielles sont absentes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de la notice (mises en garde et contre-indications) via le site de l'ANSM : lacune bloquante pour le dépistage de sécurité
- Données détaillées sur le mécanisme d'action (MOA), par exemple via DrugBank
- Démonstration d'un lien biologique entre la voie ALK/ROS1 et la fibromatose gingivale, par des études précliniques
- Clarification du statut réglementaire en France (AMM annulées)
- Si une piste de repositionnement est recherchée, étudier en priorité les tumeurs pilotées par ALK (par exemple le neuroblastome), pour lesquelles des données cliniques de phase 1 existent
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

