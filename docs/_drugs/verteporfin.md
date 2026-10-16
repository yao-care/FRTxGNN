---
layout: default
title: Verteporfin
parent: Prédiction du modèle uniquement (L5)
nav_order: 810
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Verteporfin : nouvelle indication prédite, Trouble de la phosphorylation oxydative mitochondriale dû à des anoma… (niveau de preuve L5). Indication d'origine : Dégénérescence maculaire"
---

# Verteporfin
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Vertéporfine : De la Dégénérescence Maculaire à un Trouble de la Phosphorylation Oxydative Mitochondriale d'Origine Nucléaire

## Résumé en Une Phrase

La vertéporfine est un photosensibilisant, initialement utilisé pour le traitement de la dégénérescence maculaire.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **trouble de la phosphorylation oxydative mitochondriale dû à des anomalies de l'ADN nucléaire**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : la prédiction repose uniquement sur le score du modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dégénérescence maculaire (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Trouble de la phosphorylation oxydative mitochondriale dû à des anomalies de l'ADN nucléaire |
| Score de Prédiction TxGNN | 99,49 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les informations connues, la vertéporfine est un photosensibilisant activé par une lumière rouge non thermique (environ 689 nm). Il génère des espèces réactives de l'oxygène dans les tissus néovasculaires, ce qui explique son usage dans la dégénérescence maculaire. Des travaux précliniques rapportent aussi une inhibition de l'interaction YAP-TEAD, indépendante de la lumière.

Aucun lien mécanistique direct n'est établi entre ces propriétés et les troubles de la phosphorylation oxydative (OXPHOS) liés à l'ADN nucléaire. Une connexion via les voies du stress mitochondrial ou oxydatif est plausible, mais non vérifiée.

Il faut surtout signaler que la production d'espèces réactives de l'oxygène pourrait **aggraver** un dysfonctionnement mitochondrial. Le sens de l'effet est donc incertain, voire potentiellement défavorable. Le score élevé du modèle doit être interprété avec une grande prudence.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 64637807 | VISUDYNE 15 mg, poudre pour solution pour perfusion (CHEPLAPHARM ARZNEIMITTEL, Allemagne) | Poudre pour solution pour perfusion | Non renseignée (AMM annulée) |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de la notice) : porphyrie héréditaire, maladie du métabolisme des porphyrines, porphyrie, maladie hépatique, maladie de la vésicule biliaire.
- **Interactions médicamenteuses** : 117 interactions recensées. Parmi les principales (niveau modéré) :
  - tétracyclines : doxycycline, tétracycline, minocycline (y compris formes topiques) ;
  - sulfamides hypoglycémiants : glimépiride, glipizide, glibenclamide (glyburide), tolbutamide, tolazamide, acétohexamide, chlorpropamide ;
  - autres : acide acétylsalicylique, lévofloxacine, mannitol, sulfasalazine, bêta-carotène, papavérine.
  - Une interaction de niveau mineur est signalée avec la polymyxine B.

  Beaucoup de ces substances sont photosensibilisantes ou susceptibles de l'être, ce qui est pertinent avec la vertéporfine.
- Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai clinique ni publication. Le mécanisme est incertain et potentiellement défavorable, et il n'existe plus d'AMM valide en France.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications officielles de la notice (ANSM), élément bloquant pour le criblage de sécurité.
- Les données détaillées sur le mécanisme d'action (DrugBank).
- Des études précliniques évaluant l'effet de la vertéporfine sur la fonction mitochondriale, notamment le risque d'aggravation par le stress oxydatif.
- Une revue de la littérature et des registres d'essais pour cette indication.
- Une évaluation de la faisabilité de la voie d'administration (perfusion avec activation lumineuse) pour une maladie systémique.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

