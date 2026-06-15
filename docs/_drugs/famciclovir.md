---
layout: default
title: Famciclovir
parent: 僅模型預測 (L5)
nav_order: 122
evidence_level: L5
indication_count: 9
---

# Famciclovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Famciclovir : De l'Infection Herpétique à la Névralgie Post-Infectieuse

## Résumé en Une Phrase

Famciclovir est un antiviral nucléoside analogue, prodrug du penciclovir, reconnu pour le traitement des infections à virus varicelle-zona (VZV), notamment l'herpès zoster et la varicelle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **névralgie post-infectieuse**,
avec **2 essais cliniques** documentés dans ce domaine — bien qu'aucun ne teste directement le famciclovir pour cette indication — et **aucune publication** spécifiquement associée.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible (médicament non commercialisé dans la base consultée) |
| Nouvelle Indication Prédite | Névralgie post-infectieuse |
| Score de Prédiction TxGNN | 99.75% |
| Niveau de Preuve | L3 |
| Statut de Marché | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Famciclovir est le prodrug oral du penciclovir. Après absorption intestinale, il est rapidement converti en penciclovir actif, lequel est phosphorylé par la thymidine kinase virale spécifique du VZV. Sous forme triphosphatée, il inhibe sélectivement la DNA polymérase virale, bloquant ainsi la réplication du VZV. Ce mécanisme est bien établi dans le traitement de l'herpès zoster et de la varicelle, comme en témoignent les données des essais cliniques présents dans ce pack (notamment NCT01327144 Phase 3 et NCT00098046 Phase 3 pédiatrique).

La névralgie post-infectieuse — et plus spécifiquement la névralgie post-zostérienne (PHN) — représente la complication la plus fréquente et la plus invalidante de l'herpès zoster. Elle résulte de lésions nerveuses induites par la réplication virale intensive lors de la phase aiguë : plus la charge virale et la durée d'infection aiguë sont élevées, plus les dommages neuronaux sont importants et la probabilité de PHN augmente. Il existe donc un lien mécanistique indirect cohérent : en inhibant la réplication du VZV dès la phase aiguë, le famciclovir pourrait atténuer l'ampleur des lésions nerveuses et, par conséquent, réduire l'incidence ou la sévérité de la PHN.

Cette hypothèse « inhibition virale aiguë → réduction des dommages neuronaux → prévention de la PHN » est biologiquement plausible. Des données provenant d'études sur l'herpès zoster suggèrent que les antiviraux, administrés précocement (dans les 72 heures), réduisent la durée des douleurs zostériennes aiguës. Toutefois, les essais cliniques disponibles dans ce pack d'évidence ne testent pas directement le famciclovir pour la prévention ou le traitement de la névralgie post-infectieuse établie, ce qui maintient le niveau de preuve à L3.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | NA | Inconnu | 140 | Évaluation de l'oxycodone précoce pendant la phase aiguë de l'herpès zoster pour prévenir la PHN — famciclovir non testé directement ; fournit un contexte sur la recherche en prévention de la PHN |
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | NA | Pas encore recruté | 120 | Bloc nerveux multimodal à la bupivacaïne liposomale et ropivacaïne pour la douleur aiguë de l'herpès zoster — intervention non pharmacologique ; famciclovir absent du schéma expérimental |

> **Note :** Les deux essais identifiés sont classés pertinence C — ils illustrent le domaine de recherche en prévention de la PHN mais ne testent pas directement le famciclovir pour cette indication.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour la névralgie post-infectieuse en lien direct avec le famciclovir.

---

## Informations de Marché en France

Aucune autorisation de mise sur le marché (AMM) n'est enregistrée pour le famciclovir dans la base de données réglementaire consultée.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le lien mécanistique entre famciclovir et la névralgie post-infectieuse est biologiquement plausible (inhibition virale aiguë → réduction des lésions nerveuses), mais les preuves directes sont insuffisantes : aucun essai clinique ne teste directement le famciclovir pour cette indication, et aucune publication spécifique n'est disponible. L'absence d'AMM locale renforce la prudence.

> **Signal à surveiller :** L'analyse comparative du pack révèle que l'indication **varicelle** (chickenpox, rang 7 par score TxGNN) présente un niveau de preuve **L1** avec 5 essais cliniques (dont 2 Phase 3 complétés directement sur famciclovir) et 20 publications — ce qui représente le dossier de repositionnement le plus solide dans ce pack et mériterait une évaluation prioritaire distincte.

**Pour avancer, les éléments suivants sont nécessaires :**

- Données formelles sur le mécanisme d'action (MOA) issues de DrugBank — actuellement manquantes
- Essais cliniques randomisés contrôlés évaluant directement le famciclovir dans la prévention ou le traitement de la névralgie post-zostérienne établie
- Données de sécurité complètes : avertissements, contre-indications et interactions médicamenteuses (données actuellement indisponibles dans ce pack)
- Clarification du statut réglementaire en France/UE (famciclovir est commercialisé dans d'autres pays sous le nom Famvir® — vérification auprès de l'ANSM recommandée)
- Méta-analyse des données d'essais herpès zoster existants pour extraire les données de PHN secondaires liées au famciclovir
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

