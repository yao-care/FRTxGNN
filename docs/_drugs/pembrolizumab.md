---
layout: default
title: Pembrolizumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 584
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pembrolizumab : nouvelle indication prédite, Fibromatose gingivale (niveau de preuve L5). Indication d'origine : Cancer du poumon non à petites cellules, cancer du poumon…"
monitor_inn: "PEMBROLIZUMAB"
predicted_indications: ["fibromatosis, gingival", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung hilum carcinoma", "fibroma of lung", "lung benign neoplasm", "ovarioleukodystrophy", "lung germ cell tumor", "pulmonary sulcus neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Pembrolizumab
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Pembrolizumab : Du Cancer du Poumon Non à Petites Cellules à la Fibromatose Gingivale

## Résumé en Une Phrase

Pembrolizumab est un anticorps monoclonal anti-PD-1, initialement utilisé pour le traitement du cancer du poumon non à petites cellules et du mélanome métastatique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **fibromatose gingivale** (score élevé), mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement computationnelle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer du poumon non à petites cellules, cancer du poumon, mélanome métastatique (le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Fibromatose gingivale |
| Score de Prédiction TxGNN | 99,40 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement annulé (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier compilé. Les informations pharmacologiques connues indiquent que pembrolizumab est un anticorps dirigé contre le récepteur PD-1 (CD279, gène *PDCD1*). Il lève le frein immunitaire exercé sur les lymphocytes T et renforce ainsi la réponse antitumorale. Son efficacité est établie dans le cancer du poumon et le mélanome.

**Cette prédiction n'est pas étayée mécanistiquement.** La fibromatose gingivale est une affection fibrotique bénigne, héréditaire ou médicamenteuse. Aucun lien n'est établi avec l'axe PD-1/PD-L1, et aucun essai ni aucune publication ne soutient un rôle du blocage de PD-1 dans cette maladie. Le score élevé reflète vraisemblablement des associations dans le graphe de connaissances plutôt qu'une biologie pertinente. Activer le système immunitaire dans une pathologie bénigne exposerait en outre à des effets indésirables immunologiques sans bénéfice démontré.

À titre de comparaison, parmi les autres prédictions de haut rang, seules les tumeurs pulmonaires malignes (carcinome du hile pulmonaire, tumeur de Pancoast) sont biologiquement plausibles. Elles relèvent toutefois de l'indication déjà approuvée et ne constituent pas un véritable repositionnement.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour la fibromatose gingivale.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la fibromatose gingivale.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62689214 | KEYTRUDA 25 mg/mL (MERCK SHARP & DOHME, Pays-Bas) — **annulée** | Solution à diluer pour perfusion | Non renseignée |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Immunothérapie (anticorps anti-PD-1), non cytotoxique conventionnel |
| Risque de Myélosuppression | Faible en monothérapie ; peut augmenter en association à une chimiothérapie |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice (surveillance usuelle des effets immunologiques : fonctions hépatique, thyroïdienne et surrénalienne, NFS) |
| Protection de Manipulation | Veuillez consulter la notice |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** (13 interactions recensées) :
  - **Majeures** : lénalidomide, pomalidomide, thalidomide.
  - **Modérées** : corticoïdes (hydrocortisone, triamcinolone, dexaméthasone, bétaméthasone, budésonide, prednisolone, prednisone, méthylprednisolone, déflazacort).
- **Profil de toxicité immunologique** : la littérature rapportée pour d'autres indications décrit des effets indésirables d'origine immunitaire (endocrinopathies, myocardite, myosite, atteintes neurologiques, hyperprogression). Ce risque est particulièrement préoccupant dans une maladie bénigne.

Les mises en garde et contre-indications de la notice n'étant pas disponibles, veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5) : aucun essai, aucune publication, aucun lien mécanistique pour la fibromatose gingivale, maladie bénigne pour laquelle le risque immunologique dépasse tout bénéfice spéculatif.
- Le produit n'a plus d'AMM valide en France (une seule AMM, annulée).

**Pour avancer, les éléments suivants sont nécessaires :**
- Mécanisme d'action détaillé (DrugBank) et analyse d'un éventuel lien PD-1/fibrose gingivale
- Données de la notice ANSM (mises en garde et contre-indications), actuellement bloquantes pour le criblage de sécurité
- Données précliniques démontrant une pertinence biologique avant toute étude clinique
- Clarification du statut réglementaire en France (AMM annulée)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

