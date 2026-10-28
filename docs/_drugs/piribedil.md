---
layout: default
title: Piribedil
parent: Prédiction du modèle uniquement (L5)
nav_order: 610
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Piribedil : nouvelle indication prédite, Dystrophie rétinienne avec ou sans anomalies extraoculaires (niveau de preuve L5). Indication d'origine : Maladie de Parkinson / syndrome parkinsonien (texte …"
monitor_inn: "piribedil"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "paralysis agitans, juvenile, of Hunt", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "PLA2G6-associated neurodegeneration"]
---

# Piribedil
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

## Piribédil : De la maladie de Parkinson à la dystrophie rétinienne avec ou sans anomalies extraoculaires
{: .text-alpha }

## Résumé en Une Phrase

Le piribédil est un agoniste dopaminergique, initialement utilisé pour le traitement de la maladie de Parkinson et des syndromes parkinsoniens.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **dystrophie rétinienne avec ou sans anomalies extraoculaires**, mais **aucun essai clinique** et **une seule publication** (sans lien direct avec le médicament) soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Parkinson / syndrome parkinsonien (texte d'indication de l'AMM non renseigné dans les données compilées) |
| Nouvelle Indication Prédite | Dystrophie rétinienne avec ou sans anomalies extraoculaires |
| Score de Prédiction TxGNN | 0,9934 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 2) |
| Nombre d'AMM | 2 (valides : 1) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales, le piribédil est un agoniste des récepteurs dopaminergiques D2/D3, avec une activité antagoniste alpha-2 adrénergique. Son efficacité dans la maladie de Parkinson est établie.

La signalisation dopaminergique intervient dans la physiologie rétinienne, ce qui rend plausible un lien lointain avec les maladies de la rétine. Toutefois, la seule publication retrouvée porte sur la prise en charge de la syncope dans le syndrome de Kearns-Sayre, une maladie mitochondriale comprenant une rétinopathie. Elle n'évalue pas le piribédil : le lien reste donc indirect au mieux.

Le score élevé de TxGNN (0,9934) est une prédiction computationnelle, sans donnée clinique à l'appui. Cette hypothèse doit être considérée comme exploratoire.

## Prédictions Complémentaires

D'autres indications prédites ont également été examinées. Aucune ne dispose d'essai clinique ni de publication spécifique :

| Rang | Indication Prédite | Score TxGNN | Niveau de Preuve | Commentaire |
|------|------|------|------|------|
| 2 | Parkinsonisme juvénile de Hunt | 0,9934 | L5 | Variante précoce de la maladie de Parkinson ; justification mécanistique solide (agonisme D2/D3), mais preuves indirectes |
| 3 | Polymicrogyrie périsylvienne avec hypoplasie cérébelleuse et arthrogrypose | 0,9912 | L5 | Malformation congénitale ; aucun mécanisme plausible |
| 4 | Neurodégénérescence associée à PLA2G6 | 0,9907 | L5 | Traitement symptomatique dopaminergique envisageable, sans modification de la maladie |

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [17086014](https://pubmed.ncbi.nlm.nih.gov/17086014/) | 2006 | Revue | The American Heart Hospital Journal | Physiopathologie et prise en charge de la syncope dans le syndrome de Kearns-Sayre (bloc auriculo-ventriculaire complet chez une jeune femme). Ne concerne pas le piribédil. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62551633 | TRIVASTAL 20 mg, comprimé enrobé (Laboratoires Servier) | Comprimé enrobé | Non renseignée (AMM annulée) |
| 61598530 | TRIVASTAL 50 mg L.P., comprimé enrobé à libération prolongée (Laboratoires Servier) | Comprimé enrobé à libération prolongée | Non renseignée (AMM active) |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5) : aucun essai clinique et aucune publication évaluant le piribédil dans la dystrophie rétinienne. De plus, les deux AMM françaises sont annulées, ce qui limite la faisabilité pratique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications issues de la notice de l'ANSM (lacune bloquante pour le criblage de sécurité)
- Données détaillées sur le mécanisme d'action (par exemple via DrugBank)
- Études précliniques ou mécanistiques sur le rôle de la dopamine D2/D3 dans la dystrophie rétinienne
- Évaluation de la compatibilité de la voie d'administration et de la disponibilité du produit, compte tenu de l'annulation des AMM
- À titre alternatif, examiner en priorité les indications parkinsoniennes proches (parkinsonisme juvénile de Hunt, maladie de Parkinson juvénile 19A), dont la justification mécanistique est plus solide
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

