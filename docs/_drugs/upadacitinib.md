---
layout: default
title: Upadacitinib
parent: Prédiction du modèle uniquement (L5)
nav_order: 797
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Upadacitinib : nouvelle indication prédite, Syndrome de microphtalmie colobomateuse avec dysplasie rhizomélique (niveau de preuve L5). Indication d'origine : Polyarthrite rhumatoïde"
---

# Upadacitinib
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **2** 
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

# Upadacitinib : De la polyarthrite rhumatoïde au syndrome de dysplasie rhizomélique avec microphtalmie colobomateuse

## Résumé en Une Phrase

Upadacitinib (RINVOQ) était à l'origine utilisé pour le traitement de la polyarthrite rhumatoïde.
Le modèle TxGNN le prédit comme potentiellement efficace pour le **syndrome de microphtalmie colobomateuse avec dysplasie rhizomélique**, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction issue du seul modèle.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Polyarthrite rhumatoïde (issue du graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Syndrome de microphtalmie colobomateuse avec dysplasie rhizomélique |
| Score de Prédiction TxGNN | 99,61 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Uniquement des AMM annulées |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. D'après les connaissances générales, l'upadacitinib est un inhibiteur sélectif de JAK1, qui module la signalisation des cytokines et l'inflammation immunitaire. Son efficacité dans la polyarthrite rhumatoïde repose sur ce mécanisme.

La nouvelle indication prédite est un syndrome congénital rare affectant le développement oculaire et squelettique. Aucun lien mécanistique ne peut être établi à partir des données compilées : rien ne relie la voie JAK-STAT à la physiopathologie de ce syndrome, et un modulateur de la signalisation immunitaire n'a pas de justification évidente pour corriger une malformation structurelle du développement.

Le score élevé (0,996) est probablement lié à des artefacts de topologie du graphe de connaissances (voisins de gènes ou de voies partagés) plutôt qu'à une relation biologique validée. Cette prédiction doit être considérée comme une hypothèse à explorer, non comme un argument en faveur d'un usage thérapeutique.

La seconde prédiction du modèle, le syndrome de brachydactylie-syndactylie (score 99,58 %), présente la même limite : malformation congénitale fixe, sans cible évidente pour un traitement immunomodulateur, et sans aucune preuve associée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66709721 | RINVOQ 45 mg, comprimé à libération prolongée | Comprimé à libération prolongée | Non renseignée (AMM annulée) |
| 62457931 | RINVOQ 30 mg, comprimé à libération prolongée | Comprimé à libération prolongée | Non renseignée (AMM annulée) |
| 65852428 | RINVOQ 15 mg, comprimé à libération prolongée | Comprimé à libération prolongée | Non renseignée (AMM annulée) |

Le titulaire de ces AMM est ABBVIE DEUTSCHLAND (Allemagne). Aucune AMM n'est actuellement valide dans les données compilées.

## Considérations de Sécurité

**Interactions médicamenteuses** : 359 interactions ont été recensées. Parmi les principales :
- **Majeures** : corticoïdes (hydrocortisone, triamcinolone, dexaméthasone, béclométasone, bétaméthasone, budésonide, prednisone, prednisolone), clarithromycine, cobicistat, déférip­rone, iobenguane (I-131).
- **Modérées** : aprépitant, cimétidine, miconazole, déférasirox.
- **Mineures** : sels de zinc (sulfate, acétate, gluconate).

Veuillez consulter la notice pour les mises en garde et contre-indications.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique, sans publication et sans lien mécanistique plausible avec une inhibition de JAK1. Par ailleurs, toutes les AMM françaises sont annulées.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action (MOA), à compléter via DrugBank
- Mises en garde et contre-indications issues de la notice ANSM, indispensables avant tout examen de sécurité
- Preuves précliniques ou mécanistiques reliant la signalisation JAK-STAT à la physiopathologie du syndrome
- Clarification du statut réglementaire en France (AMM annulées)
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

