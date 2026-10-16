---
layout: default
title: Idebenone
parent: Prédiction du modèle uniquement (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Idebenone : nouvelle indication prédite, Porphyrie hépatique (niveau de preuve L5). Indication d'origine : Neuropathie optique héréditaire de Leber"
---

# Idebenone
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

# Idébénone : De la neuropathie optique héréditaire de Leber à la porphyrie hépatique

## Résumé en Une Phrase

L'idébénone (RAXONE 150 mg, comprimé pelliculé) était initialement utilisée pour le traitement de la neuropathie optique héréditaire de Leber.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **porphyrie hépatique**, mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Neuropathie optique héréditaire de Leber (selon le graphe de connaissances ; le texte d'indication de l'AMM française n'est pas renseigné) |
| Nouvelle Indication Prédite | Porphyrie hépatique |
| Score de Prédiction TxGNN | 99,92 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 1 (annulée) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, l'idébénone est un analogue synthétique de la benzoquinone à chaîne courte, apparenté à la coenzyme Q10. Elle agit comme antioxydant et transporteur d'électrons dans la chaîne respiratoire mitochondriale. Son efficacité dans la neuropathie optique héréditaire de Leber, une maladie mitochondriale, est l'indication de référence du médicament.

Un lien avec la porphyrie hépatique reste spéculatif : le stress oxydant et le dysfonctionnement mitochondrial pourraient intervenir dans les troubles de la synthèse de l'hème. Cette hypothèse n'est étayée par aucune donnée compilée pour ce rapport.

Le score élevé (99,92 %) doit être interprété avec prudence. Plusieurs autres maladies hépatiques et portales présentent des scores identiques ou quasi identiques, ce qui évoque un artefact de voisinage dans le graphe plutôt qu'un signal propre à la maladie.

**Autres indications prédites (toutes de niveau L5, sans essai ni publication, décision Hold) :**

| Rang | Maladie | Score TxGNN |
|------|------|------|
| 2 | Thrombose portale primitive | 99,92 % |
| 3 | Hypertension portale non cirrhotique familiale à début précoce | 99,92 % |
| 4 | Cirrhose idiopathique associée au cuivre | 99,92 % |
| 5 | Sclérose hépatoportale | 99,92 % |
| 6 | Syndrome hépatopulmonaire | 99,92 % |
| 7 | Myopathie nécrosante à médiation immunitaire | 99,76 % |
| 8 | Syndrome ostéogenèse imparfaite-rétinopathie-convulsions-déficience intellectuelle | 99,75 % |
| 9 | Syndrome des antisynthétases | 99,75 % |
| 10 | Myosite focale | 99,74 % |

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
| 62612837 | RAXONE 150 mg, comprimé pelliculé (CHIESI FARMACEUTICI) | Comprimé pelliculé | Non renseignée ; AMM annulée |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les mises en garde et contre-indications de la notice n'ont pas pu être exploitées, et aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication, avec une plausibilité mécanistique faible à spéculative.
- La seule AMM française est annulée et les données de sécurité de la notice sont absentes, ce qui bloque le passage à l'étape de criblage de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde et contre-indications)
- Obtenir les données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Réaliser une recherche ciblée dans la littérature et les registres d'essais sur l'idébénone dans la porphyrie hépatique
- Vérifier si les scores identiques observés pour plusieurs maladies hépatiques relèvent d'un artefact du graphe
- Évaluer la faisabilité d'une voie d'administration, la compatibilité n'ayant pas été établie
- Clarifier le statut réglementaire, l'AMM étant annulée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

