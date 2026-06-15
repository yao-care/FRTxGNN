---
layout: default
title: Amiloride
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 6
---

# Amiloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Amiloride : Du Traitement de l'Œdème à la Néphropathie Hypertensive Maligne

## Résumé en Une Phrase

Amiloride est un diurétique épargneur de potassium classiquement utilisé dans la prise en charge de l'œdème (insuffisance cardiaque, cirrhose hépatique) et de l'hypertension artérielle, souvent en association avec d'autres diurétiques pour prévenir l'hypokaliémie.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Néphropathie Hypertensive Maligne**,
avec **0 essai clinique** et **0 publication** soutenant directement cette direction à ce stade.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Non disponible (médicament non commercialisé en France) |
| Nouvelle Indication Prédite | Néphropathie Hypertensive Maligne |
| Score de Prédiction TxGNN | 99.82% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations pharmacologiques connues, amiloride appartient à la classe des diurétiques épargneurs de potassium : il agit par blocage des canaux épithéliaux sodiques (ENaC) dans le tubule distal et le canal collecteur rénal, réduisant ainsi la réabsorption tubulaire de sodium tout en préservant le potassium et le magnésium. Ce profil en fait un agent de contrôle du volume hydrosodé sans risque d'hypokaliémie.

La néphropathie hypertensive maligne constitue une complication grave de l'hypertension non contrôlée, associant une élévation tensionnelle sévère, une atteinte rénale aiguë rapide et des lésions microvasculaires. En théorie, le blocage ENaC par l'amiloride pourrait réduire la charge sodique systémique, alléger la pression artérielle et ainsi ralentir la progression de la néphropathie.

Toutefois, la crise d'hypertension maligne constitue une urgence médicale nécessitant en pratique des agents antihypertenseurs par voie intraveineuse à action rapide (nicardipine, labétalol, etc.). Le rôle d'un bloqueur ENaC oral dans ce contexte aigu reste sans justification clinique établie, et le score TxGNN élevé reflète vraisemblablement une connexion indirecte dans le graphe de connaissances plutôt qu'un rationnel mécanistique direct.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
L'absence totale de preuves cliniques et précliniques spécifiques à cette indication (niveau L5), conjuguée à l'inadéquation entre un diurétique oral à action progressive et la prise en charge d'une urgence hypertensive maligne, ne permet pas de recommander une progression pour cette indication à ce stade.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action (MOA) via DrugBank (DG002 — sévérité Haute)
- Informations de sécurité complètes : mises en garde, contre-indications et interactions médicamenteuses via la notice ANSM (DG001 — Bloquant)
- Études précliniques explorant l'effet de l'amiloride dans des modèles animaux de néphropathie hypertensive maligne
- Réévaluation de la pertinence clinique : distinguer la phase chronique (où un diurétique oral pourrait jouer un rôle adjuvant) de la phase aiguë maligne
- **Note prioritaire :** parmi les 6 indications prédites, la **maladie cardiaque pulmonaire chronique (Cor Pulmonale)** (rang 6, score 99.68%, niveau L3, 1 ECR disponible — PMID 2888942) présente un niveau de preuve nettement supérieur et une recommandation « Proceed with Guardrails » ; elle mérite d'être traitée en priorité dans un rapport dédié
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

