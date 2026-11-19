---
layout: default
title: Elosulfase Alfa
parent: Prédiction du modèle uniquement (L5)
nav_order: 276
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-20
monitor_inn: "elosulfase alfa"
predicted_indications: ["Scheie syndrome", "Hurler syndrome", "Sanfilippo syndrome", "camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye", "ptosis-vocal cord paralysis syndrome", "ptosis-strabismus-ectopic pupils syndrome", "ptosis-upper ocular movement limitation-absence of lacrimal punctum syndrome", "congenital Horner syndrome (disease)"]
description: "Elosulfase Alfa : nouvelle indication prédite, Syndrome de Scheie (Scheie syndrome) (niveau de preuve L5). En France, AMM dans la BDPM : 1 (valides : 1)"
---

# Elosulfase Alfa
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
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

## Elosulfase Alfa: Syndrome de Scheie (Scheie syndrome)
{: .text-alpha }

## Résumé en une phrase

Elosulfase alfa est une enzyme thérapeutique de remplacement (N-acétylgalactosamine-6-sulfatase, GALNS) administrée par perfusion.
Le modèle TxGNN prédit qu'il pourrait être utile pour le **syndrome de Scheie (Scheie syndrome)**, avec un score de 0.9990.
Aucun essai clinique ni aucune publication ne soutient actuellement cette direction : la prédiction repose uniquement sur le modèle.

## Aperçu rapide

| Élément | Contenu |
|------|------|
| Indication originale | Non renseignée dans les données locales |
| Nouvelle indication prédite | Syndrome de Scheie (Scheie syndrome) |
| Score de prédiction TxGNN | 0.9990 |
| Niveau de preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision recommandée | Hold |

## Pourquoi cette prédiction est-elle raisonnable ?

Selon la rubrique « Mechanism of Action » des informations de prescription approuvées par la FDA américaine (Prescribing Information) pour Elosulfase Alfa (traduction non officielle) : « Les mucopolysaccharidoses constituent un groupe de maladies lysosomales de surcharge causées par le déficit en enzymes lysosomales spécifiques nécessaires au catabolisme des glycosaminoglycanes (GAG). La mucopolysaccharidose de type IVA (MPS IVA, syndrome de Morquio A) se caractérise par l'absence ou la réduction marquée de l'activité de la N-acétylgalactosamine-6-sulfatase. […] La captation de l'élosulfase alfa par les cellules dans les lysosomes est médiée par la liaison des chaînes oligosaccharidiques terminées par le mannose-6-phosphate de l'élosulfase alfa aux récepteurs du mannose-6-phosphate. » Texte original en anglais : "Mucopolysaccharidoses comprise a group of lysosomal storage disorders caused by the deficiency of specific lysosomal enzymes required for the catabolism of glycosaminoglycans (GAG). Mucopolysaccharidosis IVA (MPS IVA, Morquio A Syndrome) is characterized by the absence or marked reduction in N -acetylgalactosamine-6-sulfatase activity. […] Elosulfase alfa uptake by cells into lysosomes is mediated by the binding of mannose-6-phosphate-terminated oligosaccharide chains of elosulfase alfa to mannose-6-phosphate receptors." ([DailyMed: Vimizim (elosulfase alfa) prescribing information, BioMarin Pharmaceutical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0caa2565-12b2-0ad0-1f9a-273e81c3d4cc), version du 2025-10-30 ; consulté le 2026-11-19). Sur la base des informations connues, elosulfase alfa remplace l'enzyme GALNS, qui dégrade le sulfate de kératane et le chondroïtine-6-sulfate.

Le syndrome de Scheie (forme atténuée de la mucopolysaccharidose de type I) est dû à un déficit en alpha-L-iduronidase, entraînant l'accumulation de sulfate de dermatane et de sulfate d'héparane. Les enzymes et les substrats concernés sont donc différents de ceux d'elosulfase alfa.

Le score élevé reflète vraisemblablement la proximité des maladies de surcharge lysosomale (mucopolysaccharidoses) dans le modèle, et non une correspondance mécanistique réelle. Par ailleurs, une enzymothérapie ciblant l'iduronidase (laronidase) existe déjà pour cette maladie. Cette prédiction doit donc être interprétée avec une grande prudence.

## Preuves d'essais cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la littérature

Aucune littérature associée disponible actuellement.

## Informations de marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61673965 | VIMIZIM 1 mg/ml, solution à diluer pour perfusion | Solution à diluer pour perfusion | Non renseignée |

Une AMM est enregistrée et valide ; le médicament est commercialisé en France (titulaire : BIOMARIN INTERNATIONAL LIMITED, Irlande).

## Considérations de sécurité

Veuillez consulter la notice pour les informations de sécurité. Aucune interaction médicamenteuse n'a été retrouvée dans les données compilées pour ce rapport.

## Conclusion et prochaines étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score du modèle (niveau L5), sans essai ni publication, et le mécanisme d'elosulfase alfa (GALNS) ne correspond pas à l'enzyme déficiente dans le syndrome de Scheie. Un traitement spécifique par enzymothérapie existe déjà pour cette maladie.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données détaillées sur le mécanisme d'action
- Mises en garde et contre-indications issues de la notice ANSM
- Données précliniques ou cliniques étudiant directement l'effet d'elosulfase alfa dans le syndrome de Scheie

<!-- review:begin log -->

## Journal de vérification

Ci-dessous le journal de vérification de cette page. La phrase indiquant que les données sur le mécanisme d'action n'étaient pas disponibles a été remplacée par un extrait des informations de prescription officielles citées (avec traduction non officielle) ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-19 | Phrase « données sur le mécanisme d'action non disponibles » remplacée par un extrait de l'étiquetage américain | Phrase indiquant l'absence de données sur le mécanisme d'action remplacée par un extrait sourcé | [DailyMed: Vimizim (elosulfase alfa) prescribing information, BioMarin Pharmaceutical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0caa2565-12b2-0ad0-1f9a-273e81c3d4cc) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

