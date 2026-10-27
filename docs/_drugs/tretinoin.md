---
layout: default
title: Tretinoin
parent: Prédiction du modèle uniquement (L5)
nav_order: 785
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tretinoin : nouvelle indication prédite, Nodulose rhumatoïde (niveau de preuve L5). Indication d'origine : Acné"
monitor_inn: "tretinoin"
predicted_indications: ["rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "juvenile idiopathic arthritis", "juvenile chronic polyarthritis", "spondyloarthropathy, susceptibility to", "juvenile arthritis due to defect in LACC1", "osteoarthritis", "pseudoachondroplasia", "acromesomelic dysplasia, Hunter-Thompson type", "Quinquaud's folliculitis decalvans"]
---

# Tretinoin
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

## Trétinoïne : De l'acné à la nodulose rhumatoïde
{: .text-alpha }

## Résumé en Une Phrase

La trétinoïne est un rétinoïde utilisé à l'origine pour le traitement de l'acné, de la leucémie aiguë promyélocytaire, de la kératose acquise et de la kératodermie palmoplantaire.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **nodulose rhumatoïde**.
Pour cette prédiction, **aucun essai clinique** et **aucune publication** ne la soutiennent actuellement : il s'agit d'une prédiction purement computationnelle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Acné (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Nodulose rhumatoïde |
| Score de Prédiction TxGNN | 99,84 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 7 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la trétinoïne fait partie de la classe des rétinoïdes (dérivés de la vitamine A). Son efficacité a été établie dans l'acné et dans la leucémie aiguë promyélocytaire, et elle agit sur la différenciation cellulaire et la kératinisation.

Un lien hypothétique, non vérifié, serait une modulation de la signalisation immunitaire et inflammatoire par les récepteurs de l'acide rétinoïque (par exemple des effets sur la différenciation des lymphocytes T). Rien dans les données compilées pour ce rapport ne soutient ce lien pour la nodulose rhumatoïde.

La similarité entre les indications d'origine (dermatologiques et hématologiques) et cette pathologie rhumatismale n'a pas été évaluée. Le score élevé du modèle doit donc être considéré comme une piste à explorer, et non comme une preuve d'efficacité.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la nodulose rhumatoïde.

À titre d'information, deux publications ont été retrouvées pour une autre prédiction du modèle (arthrose, rang 7), mais elles ne sont pas pertinentes : l'une concerne les injections de PRP dans l'arthrose du genou, l'autre est un cas clinique d'effets indésirables liés au trioxyde d'arsenic dans la leucémie aiguë promyélocytaire.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67020138 | EFFEDERM 0,05 %, crème | Crème | Non renseignée (AMM annulée) |
| 68553865 | RETACNYL 0,05 %, crème | Crème | Non renseignée (AMM annulée) |
| 60552619 | KETREL 0,050 %, crème | Crème | Non renseignée (AMM annulée) |
| 62373038 | RETACNYL 0,025 %, crème | Crème | Non renseignée (AMM annulée) |
| 65540866 | VESANOID 10 mg, capsule molle | Capsule molle | Non renseignée (AMM annulée) |

Deux autres AMM annulées existent (ERYLIK, gel ; ZANEA 10 mg/0,25 mg par g, gel), pour un total de 7 AMM, toutes annulées.

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Non déterminée à partir des données disponibles ; la trétinoïne est utilisée dans la leucémie aiguë promyélocytaire (agent de différenciation) |
| Risque de Myélosuppression | Données non disponibles |
| Classification d'Émétogénicité | Données non disponibles |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

## Considérations de Sécurité

- **Contre-indications relevées dans le graphe de connaissances** (et non dans le texte de la notice) : coup de soleil, troubles anxieux, troubles névrotiques, trouble dysthymique, maladie rénale, pyo-uretère, pancréatite, maladie hépatique, maladie de la vésicule biliaire, insuffisance cardiaque congestive, insuffisance surrénalienne, maladie d'Addison, maladie de Crohn, maladie inflammatoire chronique de l'intestin, eczéma atopique, ostéoporose (dont post-ménopausique), troubles psychotiques, schizophréniformes et schizo-affectifs, troubles mentaux, mycosis fongoïde et variantes (lymphomes cutanés à cellules T), diabète sucré et acidocétose diabétique.
- **Interactions médicamenteuses** : 323 interactions recensées. Parmi les principales, de niveau **majeur** : doxycycline, tétracycline, minocycline et vitamine A. De niveau **modéré** : aprépitant, clarithromycine et naltrexone. De niveau **mineur** : lévofloxacine.
- **Considérations spécifiques** : l'exposition excessive aux rétinoïdes est associée à une toxicité squelettique, ce qui appelle à la prudence dans les indications ostéoarticulaires. Chez l'enfant, l'usage systémique soulève des préoccupations connues (tératogénicité, toxicité mucocutanée et osseuse).

Les mises en garde et contre-indications issues de la notice de l'ANSM n'ont pas pu être obtenues. Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication pertinente. Toutes les AMM françaises sont annulées, et le profil de sécurité est incomplet.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), qui est un point bloquant pour l'évaluation de sécurité
- Obtenir les données sur le mécanisme d'action depuis DrugBank
- Effectuer une revue de la littérature ciblée sur les rétinoïdes dans la nodulose rhumatoïde et les atteintes rhumatismales apparentées
- Définir la voie d'administration envisagée, la compatibilité avec les formes disponibles n'ayant pas été évaluée
- Les autres prédictions du modèle (arthrite juvénile idiopathique, arthrose, dysplasies squelettiques) ne disposent pas non plus de preuves ; l'arthrose et les atteintes pédiatriques appellent une prudence particulière en raison de la toxicité osseuse des rétinoïdes
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

