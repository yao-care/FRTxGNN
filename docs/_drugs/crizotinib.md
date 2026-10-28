---
layout: default
title: Crizotinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 200
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
monitor_inn: "CRIZOTINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
description: "Crizotinib : nouvelle indication prédite, Fibromatose gingivale (fibromatosis, gingival) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Crizotinib
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

## Crizotinib: Fibromatose gingivale (fibromatosis, gingival)
{: .text-alpha }

## Résumé en Une Phrase

Crizotinib est un inhibiteur de tyrosine kinase (ALK, ROS1, MET), initialement utilisé pour le traitement du cancer bronchique non à petites cellules (CBNPC) et du cancer du poumon.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **fibromatose gingivale**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** et **aucune publication** ne la soutient actuellement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Fibromatose gingivale (fibromatosis, gingival) |
| Score de Prédiction TxGNN | 0.9981 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après la littérature récupérée, le crizotinib est un inhibiteur compétitif de l'ATP des récepteurs à tyrosine kinase ALK, ROS1 et c-MET. Son efficacité est établie dans le CBNPC avec réarrangement d'ALK ou de ROS1.

Pour la fibromatose gingivale, aucun lien mécanistique plausible avec l'inhibition d'ALK, ROS1 ou MET n'a pu être établi à partir des données disponibles. Le score élevé (0.9981) provient du modèle TxGNN (deep learning) et peut refléter des similitudes apprises par le modèle entre maladies apparentées, et non une preuve biologique ou clinique. Cette prédiction doit donc être considérée comme une simple hypothèse.

À titre de comparaison, d'autres indications prédites présentent des signaux un peu plus étayés, mais ils restent faibles ou relèvent de l'indication déjà approuvée :
- **Carcinome du hile pulmonaire** (niveau L4) : cas cliniques d'efficacité dans le CBNPC ROS1+ et ALK+, ce qui correspond à la biologie de l'indication d'origine plutôt qu'à un véritable repositionnement.
- **Tumeur germinale du poumon** (niveau L3) : essais agnostiques de type panier, sans donnée propre à cette tumeur.

## Preuves d'Essais Cliniques

Aucun essai clinique associé n'est enregistré actuellement pour la fibromatose gingivale.

## Preuves de la Littérature

Aucune littérature associée n'est disponible actuellement pour la fibromatose gingivale.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66937155 | XALKORI 200 mg, gélule (active) | Gélule | Non renseignée |
| 61506083 | XALKORI 250 mg, gélule (active) | Gélule | Non renseignée |

Les deux AMM, détenues par PFIZER EUROPE MA EEIG (Belgique), sont valides ; le médicament est commercialisé.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase ALK/ROS1/MET) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Fonction hépatique (cas d'insuffisance hépatique fulminante fatale rapportés), ECG et fréquence cardiaque (bradycardie, allongement du QT et autres toxicités cardiaques rapportées), NFS |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Interactions médicamenteuses** : 100 interactions sont recensées. Parmi celles listées :
  - **Majeures** : clarithromycine, cisapride, dolasétron, éliglustat, granisétron.
  - **Modérées** : famotidine, metformine, lopéramide, bupropion, aprépitant, dexaméthasone, bisacodyl, budésonide, entre autres.
- **Signaux de toxicité issus de la littérature** : insuffisance hépatique fulminante fatale, toxicités cardiaques multiples (bradycardie, allongement du QT, syndrome sinusal), érythème polymorphe et œsophagite érosive chez un patient pédiatrique (rapports de cas).

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour la fibromatose gingivale repose uniquement sur le score du modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible. De plus, le profil de toxicité du crizotinib et l'absence d'AMM valide en France plaident pour la prudence.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (MOA) pour analyser un éventuel lien mécanistique.
- Mises en garde et contre-indications issues de la notice de l'ANSM (données bloquantes pour le criblage de sécurité).
- Études précliniques démontrant un rôle d'ALK, ROS1 ou MET dans la fibromatose gingivale.
- Clarification du statut réglementaire en France (AMM annulées).
- Si un repositionnement oncologique est visé, privilégier les pistes plus documentées (carcinome du hile pulmonaire, tumeurs avec altération ALK/ROS1/MET dans des essais de type panier).
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

