---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 10
---

# Latanoprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Latanoprost : Du Glaucome/Hypertension Oculaire au Glaucome Hereditaire Primitif

## Resume en Une Phrase

Latanoprost est un analogue de la prostaglandine F2α, dont l'usage etabli concerne le traitement du glaucome et de l'hypertension oculaire (donnee issue du raisonnement mecanistique fourni, le champ MOA structure etant lui-meme marque comme donnee manquante).
Le modele TxGNN predit qu'il pourrait etre efficace pour le **Glaucome Hereditaire Primitif**,
avec **1 essai clinique** soutenant actuellement cette direction (aucune publication litteraire recensee).

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Glaucome / hypertension oculaire (deduit du mecanisme d'action decrit dans les donnees de preuve ; non confirme par une AMM francaise, le medicament n'etant pas commercialise en France) |
| Nouvelle Indication Predite | Glaucome Hereditaire Primitif |
| Score de Prediction TxGNN | 99.88% |
| Niveau de Preuve | L2 |
| Statut de Marche en France | Non commercialise |
| Nombre d'AMM | 0 |
| Decision Recommandee | Proceed with Guardrails |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Le champ structure du mecanisme d'action (MOA) de latanoprost n'est pas disponible dans les donnees actuelles (donnee manquante signalee, priorite Haute). Les donnees de preuve fournies indiquent cependant que latanoprost est un agoniste des recepteurs de la prostaglandine F2α, qui abaisse la pression intraoculaire en augmentant l'evacuation de l'humeur aqueuse par la voie uveosclerale — un mecanisme pharmacologique deja etabli comme standard dans le traitement du glaucome et de l'hypertension oculaire.

Le Glaucome Hereditaire Primitif appartient au meme cadre physiopathologique (trouble de l'evacuation de l'humeur aqueuse) que l'usage etabli du medicament. Il ne s'agit donc pas d'un repositionnement vers une aire therapeutique distincte, mais d'une extension a un sous-type genetique/pediatrique de la meme maladie, ce qui explique la forte plausibilite mecanistique de la prediction.

Cette coherence est appuyee par un essai clinique de Phase 2 termine, qui a directement teste latanoprost (associe a un inhibiteur de l'anhydrase carbonique) chez des patients atteints de glaucome pediatrique refractaire a la chirurgie — une population proche du glaucome hereditaire primitif.

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Termine | 37 | Evaluation de l'effet hypotenseur oculaire de latanoprost et dorzolamide chez des patients atteints de glaucome pediatrique primitif refractaire a la chirurgie ; securite egalement evaluee |

## Preuves de la Litterature

Aucune litterature associee disponible actuellement.

## Informations de Marche en France

Latanoprost n'est actuellement associe a aucune AMM enregistree dans les donnees disponibles (0 licence, statut « non commercialise »). Aucun tableau de produits n'est donc disponible.

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

## Conclusion et Prochaines Etapes

**Decision : Proceed with Guardrails**

**Justification :**
Un essai clinique de Phase 2 termine (37 patients) teste directement latanoprost dans une population de glaucome pediatrique proche de l'indication predite, avec un mecanisme d'action hautement coherent (extension a un sous-type de la meme maladie plutot qu'un repositionnement transversal). Les lacunes de donnees de securite et de statut reglementaire francais empechent toutefois une decision « Go » complete.

**Pour avancer, les elements suivants sont necessaires :**
- Mises en garde et contre-indications issues de la notice TFDA (donnee bloquante DG001, requise avant toute evaluation de securite S1)
- Donnees structurees sur le mecanisme d'action (MOA) via l'API DrugBank (DG002)
- Clarification du statut d'enregistrement en France (AMM) si une mise sur le marche est envisagee
- Confirmation par un essai cible sur le glaucome hereditaire primitif specifiquement (l'essai disponible porte sur le glaucome pediatrique au sens large)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

