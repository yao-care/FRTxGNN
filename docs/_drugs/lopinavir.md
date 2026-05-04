---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 3
---

# Lopinavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Lopinavir : Évaluation de Repositionnement — Données Insuffisantes pour ce Cycle

## Résumé en Une Phrase

Lopinavir est un inhibiteur de protéase antirétroviral, dont les indications d'origine et les données mécanistiques ne sont pas renseignées dans ce cycle d'évaluation.
Le modèle TxGNN **n'a produit aucune prédiction d'indication** pour ce médicament lors de ce cycle.
Les lacunes de données critiques identifiées empêchent toute évaluation de repositionnement à ce stade.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Non renseignée dans ce cycle |
| Nouvelle Indication Prédite | Aucune prédiction disponible |
| Score de Prédiction TxGNN | N/A |
| Niveau de Preuve | L5 — Aucune étude réelle, aucune prédiction de modèle disponible |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Lacunes de Données Critiques

Deux lacunes ont été identifiées comme bloquantes ou à fort impact pour ce dossier :

| ID | Élément manquant | Sévérité | Impact |
|---|---|---|---|
| DG001 | Avertissements / Contre-indications réglementaires | **Bloquant** | Impossible de réaliser l'évaluation initiale de sécurité |
| DG002 | Mécanisme d'action (MOA) | **Élevé** | Analyse de pertinence mécanistique impossible |

**Sources de remédiation :**
- DG001 : Télécharger et analyser la notice officielle (PDF) depuis le site de l'ANSM ou équivalent
- DG002 : Interroger l'API DrugBank pour le profil mécanistique de DB01601

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le pipeline TxGNN n'a retourné aucune indication prédite pour Lopinavir dans ce cycle, et les deux lacunes de données critiques (avertissements réglementaires, mécanisme d'action) rendent impossible toute évaluation de repositionnement rigoureuse. Aucun dossier de preuve clinique ou littéraire n'est disponible pour étayer une direction thérapeutique alternative.

**Pour avancer, les éléments suivants sont nécessaires :**

- Relancer le pipeline TxGNN avec les paramètres de graphe de connaissances mis à jour pour obtenir des scores de prédiction d'indication
- Résoudre DG002 : récupérer le mécanisme d'action via l'API DrugBank (DB01601)
- Résoudre DG001 : extraire les avertissements et contre-indications depuis la notice officielle PDF
- Vérifier si Lopinavir est commercialisé sous une association fixe (ex. Lopinavir/Ritonavir) et si des AMM existent sous cette forme combinée en France — ce qui pourrait modifier le statut réglementaire et alimenter les sections de sécurité
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

