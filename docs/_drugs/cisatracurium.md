---
layout: default
title: Cisatracurium
parent: Prédiction du modèle uniquement (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Cisatracurium : nouvelle indication prédite, Syndrome de la queue de cheval (niveau de preuve L5). Indication d'origine : Non renseignée dans les données d'AMM"
monitor_inn: "cisatracurium"
predicted_indications: ["cauda equina syndrome", "preeclampsia", "obsolete neurogenic bladder (disease)", "migraine disorder", "thrombotic disease", "irritable bowel syndrome", "migraine with brainstem aura", "mild pre-eclampsia", "severe pre-eclampsia", "neurocirculatory asthenia"]
---

# Cisatracurium
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

## Cisatracurium : D'un curare non dépolarisant au Syndrome de la queue de cheval
{: .text-alpha }

## Résumé en Une Phrase

Le cisatracurium est un myorelaxant non dépolarisant, utilisé en anesthésie et en réanimation pour obtenir un relâchement musculaire (indication déduite de sa classe pharmacologique, car le texte d'indication des AMM n'est pas renseigné dans les données compilées).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de la queue de cheval**, mais **aucun essai clinique** ni **aucune publication** ne soutient cette prédiction : elle repose uniquement sur le modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données d'AMM |
| Nouvelle Indication Prédite | Syndrome de la queue de cheval |
| Score de Prédiction TxGNN | 0,9999 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 10 sur 10) |
| Nombre d'AMM | 10 (valides : 10) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances générales, le cisatracurium est un bloqueur neuromusculaire non dépolarisant : il agit sur les récepteurs nicotiniques de l'acétylcholine de la jonction neuromusculaire et provoque une paralysie des muscles squelettiques.

**Cette prédiction n'apparaît pas raisonnable sur le plan mécanistique.** Le syndrome de la queue de cheval est une urgence neurologique compressive, dont le traitement repose sur la décompression chirurgicale. La paralysie musculaire n'a aucun rôle plausible de modification de la maladie. Le score élevé provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées, non une preuve biologique ; il ne repose sur aucun soutien clinique.

Les autres prédictions du modèle, examinées dans les données compilées, présentent le même problème :

| Maladie prédite | Score TxGNN | Niveau de preuve | Commentaire |
|------|------|------|------|
| Prééclampsie | 0,9999 | L5 | Deux articles sur l'anesthésie pour césarienne : usage accessoire, pas un traitement de la maladie |
| Maladie thrombotique | 0,9997 | L5 | Un article sur l'anesthésie en transplantation hépatique pédiatrique : pas de lien thérapeutique |
| Vessie neurogène (terme obsolète) | 0,9999 | L5 | Aucune preuve ; le blocage systémique n'agit pas sur le contrôle nerveux |
| Migraine (et migraine avec aura du tronc cérébral) | 0,9998 / 0,9997 | L5 | Aucune action sur les voies trigéminovasculaires et CGRP |
| Syndrome de l'intestin irritable | 0,9997 | L5 | Aucune action utile sur le muscle lisse ou le système nerveux entérique |
| Prééclampsie légère / sévère | 0,9996 / 0,9995 | L5 | Proximité ontologique avec le terme parent, sans rationnel thérapeutique |
| Asthénie neurocirculatoire | 0,9995 | L5 | Aucune activité autonomique ou anxiolytique pertinente |

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour le syndrome de la queue de cheval.

À titre indicatif, des publications ont été retrouvées pour d'autres indications prédites, mais elles décrivent un usage du médicament en contexte anesthésique, non un traitement de la maladie :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [41103680](https://pubmed.ncbi.nlm.nih.gov/41103680/) | 2025 | Cohorte | Anesthesiology and Pain Medicine | Comparaison des taux sériques d'interleukine 6, de leptine et d'adiponectine après césarienne sous anesthésie générale versus rachianesthésie (prééclampsie) |
| [18383970](https://pubmed.ncbi.nlm.nih.gov/18383970/) | 2008 | Série de cas | Revista Española de Anestesiología y Reanimación | Bolus de rémifentanil pour césarienne chez 12 patientes à haut risque non éligibles à la rachianesthésie (prééclampsie) |
| [12565113](https://pubmed.ncbi.nlm.nih.gov/12565113/) | 2002 | Revue | Journal of Clinical Anesthesia | Soins anesthésiques lors de transplantations hépatiques apparentées chez l'enfant (maladie thrombotique) |

---

## Informations de Marché en France

Les 10 AMM identifiées sont toutes annulées ; le texte d'indication approuvée n'est pas renseigné.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 67403581 | Cisatracurium Accordpharma 5 mg/mL | Solution injectable ou pour perfusion | Active |
| 62067536 | Cisatracurium Accordpharma 2 mg/mL | Solution injectable ou pour perfusion | Active |
| 68123109 | Nimbex 2 mg/mL | Solution injectable ou pour perfusion | Active |
| 68405756 | Cisatracurium Accord 5 mg/mL | Solution injectable ou pour perfusion | Active |
| 63324453 | Cisatracurium Accord 2 mg/mL | Solution injectable ou pour perfusion | Active |

---

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

**Interactions médicamenteuses** : 61 interactions sont répertoriées. Parmi les 20 premières examinées :

- **Majeures** : kanamycine, néomycine, paromomycine, polymyxine B, streptomycine (potentialisation du blocage neuromusculaire, avec risque de paralysie prolongée et de dépression respiratoire).
- **Modérées** : amphotéricine B (et ses formulations lipidiques), doxycycline, minocycline, tétracycline, néomycine (topique), sulfate et chlorure de magnésium, mannitol, métoclopramide, vancomycine.
- **Mineures** : ranitidine (y compris citrate de bismuth).

Le sulfate de magnésium, utilisé dans la prééclampsie, potentialise les myorelaxants : c'est un point de vigilance anesthésique, non un argument thérapeutique.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai ni publication directe, et sans lien mécanistique plausible entre le blocage neuromusculaire et le syndrome de la queue de cheval.
- Le produit est commercialisé en France (10 AMM valides sur 10), et les données de sécurité de la notice sont absentes.

**Pour avancer, les éléments suivants seraient nécessaires :**
- Récupération des mises en garde et contre-indications dans la notice ANSM (lacune bloquante pour le criblage de sécurité).
- Données détaillées sur le mécanisme d'action (DrugBank).
- Justification biologique solide avant toute étude, ainsi que la vérification du statut réglementaire actuel du produit.
- En l'état, il est déconseillé d'investir dans cette piste de repositionnement.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

