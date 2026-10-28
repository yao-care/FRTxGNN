---
layout: default
title: Gefitinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 357
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
monitor_inn: "gefitinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung benign neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "lung germ cell tumor", "pulmonary sulcus neoplasm", "junctional epidermolysis bullosa"]
description: "Gefitinib : nouvelle indication prédite, Fibromatose gingivale (fibromatosis, gingival) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Gefitinib
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

## Gefitinib: Fibromatose gingivale (fibromatosis, gingival)
{: .text-alpha }

## Résumé en Une Phrase

Le géfitinib est un inhibiteur de la tyrosine kinase de l'EGFR, initialement utilisé pour traiter le cancer bronchique non à petites cellules (CBNPC) et le cancer du poumon.
Le modèle TxGNN le prédit comme potentiellement efficace pour la **fibromatose gingivale**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Fibromatose gingivale (fibromatosis, gingival) |
| Score de Prédiction TxGNN | 0.9989 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 7 sur 8) |
| Nombre d'AMM | 8 (valides : 7) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des informations connues, le géfitinib est un inhibiteur sélectif de la tyrosine kinase du récepteur du facteur de croissance épidermique (EGFR). Son efficacité dans le CBNPC porteur de mutations activatrices de l'EGFR est établie.

Un lien hypothétique pourrait passer par la signalisation EGFR/ErbB dans la prolifération des fibroblastes, qui intervient dans la fibromatose gingivale. Ce lien reste toutefois **spéculatif** : aucune donnée ne l'étaye, et la parenté avec l'indication d'origine (une tumeur maligne du poumon) est faible.

Le score élevé (0,9989) provient du modèle TxGNN (deep learning) et peut refléter des similarités apprises par le modèle entre des maladies apparentées, et non une preuve biologique ou clinique. Il doit être interprété avec prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Les 8 AMM suivantes sont toutes annulées ; le texte d'indication approuvée n'est pas renseigné dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65070509 | GEFITINIB EG 250 mg (EG LABO) | Comprimé pelliculé | Non renseignée (AMM active) |
| 66530743 | GEFITINIB SANDOZ 250 mg | Comprimé pelliculé | Non renseignée (AMM active) |
| 61571533 | GEFITINIB TEVA 250 mg | Comprimé pelliculé | Non renseignée (AMM active) |
| 67522920 | GEFITINIB ZENTIVA 250 mg | Comprimé pelliculé | Non renseignée (AMM active) |
| 68862107 | GEFITINIB ACCORD 250 mg | Comprimé pelliculé | Non renseignée (AMM annulée) |

Trois autres AMM annulées existent (IRESSA 250 mg, GEFITINIB BIOGARAN 250 mg, GEFITINIB ARROW 250 mg).

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase de l'EGFR) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Fonction hépatique ; surveillance respiratoire (risque de pneumopathie interstitielle) |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie hépatique, maladie de la vésicule biliaire, pneumopathie interstitielle, fibrose pulmonaire, fibrose pulmonaire post-inflammatoire.
- **Interactions médicamenteuses** : 349 interactions recensées. Parmi les principales, de niveau modéré : antiacides et inhibiteurs de la sécrétion gastrique (famotidine, ranitidine, cimétidine, nizatidine, oméprazole, ésoméprazole, lansoprazole, dexlansoprazole, pantoprazole, rabéprazole), clarithromycine, aprépitant, dexaméthasone, naltrexone, miconazole, clotrimazole, troglitazone. Le calcitriol et le glimépiride sont signalés avec un niveau inconnu.

Pour les mises en garde et contre-indications officielles, veuillez consulter la notice, le texte réglementaire n'ayant pas pu être obtenu.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication.
- Le profil de toxicité cutanée et pulmonaire connu du géfitinib, ainsi que l'absence d'AMM valide en France, renforcent la prudence.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (MOA), à interroger via DrugBank
- Notice ANSM (mises en garde et contre-indications), bloquante pour le criblage de sécurité
- Données précliniques montrant un rôle de l'EGFR dans la fibromatose gingivale
- Revue systématique de la littérature et des registres d'essais pour confirmer l'absence de données
- Évaluation de la voie d'administration et de la formulation adaptées à cette indication
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

