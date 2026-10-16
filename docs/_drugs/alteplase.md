---
layout: default
title: Alteplase
parent: Prédiction du modèle uniquement (L5)
nav_order: 48
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Alteplase : nouvelle indication prédite, Infarctus du myocarde postérolatéral (niveau de preuve L5). Indication d'origine : Infarctus du myocarde, embolie pulmonaire…"
---

# Alteplase
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **9** 
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

# Alteplase : De l'infarctus du myocarde à l'infarctus du myocarde postérolatéral

## Résumé en Une Phrase

Alteplase est un thrombolytique recombinant (activateur tissulaire du plasminogène), initialement utilisé pour l'infarctus du myocarde, l'embolie pulmonaire et l'accident vasculaire cérébral ischémique.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**infarctus du myocarde postérolatéral**, mais **aucun essai clinique** ni **aucune publication** spécifique ne soutient actuellement cette prédiction. Il s'agit d'un sous-type anatomique d'une indication déjà existante, et non d'un véritable repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Infarctus du myocarde, embolie pulmonaire, accident vasculaire cérébral (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Infarctus du myocarde postérolatéral |
| Score de Prédiction TxGNN | 99,79 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulé uniquement (aucune AMM valide) |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, l'alteplase est un activateur du plasminogène : il le transforme en plasmine, qui dissout la fibrine des caillots. Son efficacité dans l'infarctus du myocarde est déjà établie.

L'infarctus postérolatéral est un sous-type anatomique de l'infarctus du myocarde. Le mécanisme (lyse du thrombus coronaire occlusif) est donc plausible. Le score très élevé du modèle reflète probablement la proximité de ces deux entités dans le graphe de connaissances plutôt qu'une découverte nouvelle.

Aucun essai ni publication propre à ce sous-type n'a été fourni : le score de prédiction seul ne constitue pas une preuve suffisante.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 63617876 | ACTILYSE, poudre et solvant pour solution injectable et perfusion | Poudre et solvant pour solution injectable et pour perfusion | Non renseignée (AMM annulée) |
| 67177673 | ACTILYSE 2 mg, poudre pour solution injectable et perfusion | Poudre pour solution injectable ou pour perfusion | Non renseignée (AMM annulée) |

Les deux AMM (BOEHRINGER INGELHEIM FRANCE) sont annulées ; aucune AMM valide n'existe actuellement dans les données compilées.

---

## Considérations de Sécurité

- **Interactions médicamenteuses** : 140 interactions sont recensées. Parmi les principales :
  - **Majeures** : abciximab, acalabrutinib, apixaban, anisindione, fondaparinux, déférasirox, ibritumomab tiuxétan, tositumomab (y compris I-131).
  - **Modérées** : acide acétylsalicylique, ibuprofène, kétorolac, fluvoxamine, fosinopril, acide aminocaproïque, aprotinine, fenfluramine, dexfenfluramine, sibutramine.

Le risque hémorragique est la préoccupation centrale pour un thrombolytique associé à des antithrombotiques. Veuillez consulter la notice pour les mises en garde et contre-indications, qui ne sont pas disponibles dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (L5), sans essai ni publication spécifique. Il s'agit d'un sous-type d'une indication déjà connue, et toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications issues de la notice de l'ANSM (lacune bloquante pour le criblage de sécurité)
- Données sur le mécanisme d'action (DrugBank)
- Données cliniques spécifiques aux sous-types d'infarctus (postérolatéral, postéro-inférieur)
- Clarification du statut réglementaire actuel en France (AMM annulées)

---

## Autres Prédictions Examinées

Les autres prédictions classées ont également été évaluées, avec les niveaux de preuve suivants :

- **Thrombophilie (L3, score 99,43 %)** : un essai de phase 2 en recrutement (NCT05540834, 70 participants) sur l'alteplase guidée par tests viscoélastiques dans l'insuffisance respiratoire aiguë prothrombotique, dont le lien avec la thrombophilie n'est pas confirmé. La littérature est quasi exclusivement composée de rapports de cas. Le bénéfice porte sur l'événement thrombotique et non sur l'état thrombophilique. Orientation : question de recherche.
- **Sténose coronaire (L3, score 99,14 %)** : la littérature comprend un essai randomisé de 1993 contre placebo dans la douleur thoracique de repos (PMID 8299637), et surtout des travaux sur la thrombolyse de l'infarctus. L'alteplase ne traite pas une sténose athéroscléreuse fixe, et la thrombolyse est largement supplantée par l'angioplastie primaire quand elle est disponible. Orientation : question de recherche.
- **Infarctus du myocarde septal (L4, score 99,77 %)** : trois publications indirectes (rapport de cas, étude de 1996 sur la thrombolyse tardive, cohorte 2025 sur le syndrome coronarien aigu au Bhoutan), aucun essai. Orientation : Hold.
- **Infarctus postéro-inférieur, déficit en cofacteur II de l'héparine, anomalie coronaire congénitale, excès de facteur 5, déficit en antithrombine de type 2 (tous L5)** : aucun essai ni publication spécifique. Orientation : Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

