---
layout: default
title: Simoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
---

# Simoctocog Alfa
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

Utilisation directe du format demandé (génération de rapport à partir de l'Evidence Pack fourni — pas de tâche de code nécessitant un skill spécifique).

# Simoctocog Alfa : De l'Hémophilie A à la Maladie de Pseudo-von Willebrand

## Résumé en Une Phrase

Simoctocog alfa est un facteur VIII de coagulation recombinant (rFVIII), utilisé pour la prévention et le traitement des hémorragies dans l'**hémophilie A**. Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie de Pseudo-von Willebrand**, avec un score de prédiction de 99.99%, mais **aucun essai clinique ni aucune publication** ne soutient actuellement cette direction, et le mécanisme d'action proposé est jugé peu plausible par l'analyse de repositionnement elle-même.

> Note : le champ structuré `original_indications` est vide dans les données source (data gap). L'indication d'origine ci-dessus est reconstituée à partir du texte de justification mécanistique associé au candidat n°9 de ce même pack de preuves (facteur VIII recombinant → hémophilie A), et non d'une source réglementaire structurée.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémophilie A (prévention et traitement des hémorragies) — reconstituée, non issue d'une licence structurée |
| Nouvelle Indication Prédite | Maladie de Pseudo-von Willebrand |
| Score de Prédiction TxGNN | 99.99% (rang TxGNN global : 114) |
| Niveau de Preuve | L5 (prédiction du modèle uniquement, aucune étude réelle) |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles (data gap classé "High"). Sur la base des informations connues, simoctocog alfa fait partie de la classe des facteurs VIII de coagulation recombinants (rFVIII) ; son efficacité dans l'hémophilie A — une maladie liée à un déficit quantitatif ou qualitatif du facteur VIII — est bien établie, et le mécanisme repose sur la restauration directe de la voie de coagulation endogène.

La maladie de Pseudo-von Willebrand, en revanche, n'est pas causée par un déficit en facteur VIII : il s'agit d'une anomalie du récepteur plaquettaire GPIb, qui présente une affinité anormalement élevée pour le facteur von Willebrand (VWF). Selon l'analyse de repositionnement associée à ce candidat, la supplémentation en rFVIII ne dispose pas de mécanisme direct pour corriger cette interaction plaquette-VWF anormale ; un effet indirect via l'effet porteur du VWF sur le FVIII n'est pas exclu, mais reste spéculatif et n'est appuyé par aucune preuve clinique ou de laboratoire dans ce dossier.

En résumé, le lien mécanistique entre l'indication d'origine et l'indication prédite est jugé **faible et non démontré** — la prédiction TxGNN repose sur une association du graphe de connaissances, sans support expérimental ou clinique à ce stade.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

Simoctocog alfa n'est actuellement pas commercialisé en France (0 AMM enregistrée dans les données disponibles).

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. (Les mises en garde, contre-indications et interactions médicamenteuses ne sont pas encore documentées dans ce dossier — data gap classé "Blocking" pour l'accès au résumé réglementaire.)

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le score TxGNN est élevé, mais aucun essai clinique ni aucune publication ne soutient ce repositionnement, et le mécanisme d'action proposé (correction indirecte via le VWF) est explicitement qualifié de faible dans l'analyse de justification. L'absence de données de sécurité réglementaire (mises en garde, contre-indications) empêche par ailleurs toute évaluation de sécurité préliminaire (S1).

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir le résumé des caractéristiques du produit / notice officielle pour lever le data gap bloquant sur la sécurité
- Confirmer le mécanisme d'action (MOA) détaillé via DrugBank ou littérature pharmacologique
- Rechercher des données précliniques ou des séries de cas spécifiques à l'usage du rFVIII dans la maladie de Pseudo-von Willebrand avant toute réévaluation
- Note complémentaire : parmi les 10 indications prédites pour ce médicament, le candidat classé n°9 (« hémophilie A avec anomalie vasculaire ») présente un lien mécanistique nettement plus direct avec l'indication d'origine et un niveau de preuve supérieur (L4, stade S1) ; il pourrait constituer une piste de repositionnement plus solide à documenter séparément.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

