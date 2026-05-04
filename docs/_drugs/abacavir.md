---
layout: default
title: Abacavir
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
---

# Abacavir
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

# Abacavir : Rapport d'Évaluation de Repositionnement

## Résumé en Une Phrase

Abacavir (DrugBank : DB01048) est un antirétroviral de la classe des inhibiteurs nucléosidiques de la transcriptase inverse (INTI), principalement utilisé dans le traitement de l'infection par le VIH-1. À ce stade, le modèle TxGNN **n'a généré aucune prédiction de nouvelle indication** pour ce médicament. Les données disponibles dans l'Evidence Pack présentent des lacunes significatives qui empêchent une évaluation complète.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans l'Evidence Pack (connu : infection par le VIH-1) |
| Nouvelle Indication Prédite | Aucune prédiction disponible |
| Score de Prédiction TxGNN | — |
| Niveau de Preuve | L5 (aucune donnée de repositionnement) |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | **Hold** |

---

## Pourquoi Cette Évaluation est-elle Limitée ?

Abacavir est un analogue nucléosidique de la guanosine qui inhibe la transcriptase inverse du VIH-1, bloquant ainsi la réplication virale. Il est couramment utilisé en association avec d'autres antirétroviraux (notamment lamivudine et dolutégravir) dans les schémas thérapeutiques de première ligne contre le VIH.

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans l'Evidence Pack fourni (lacune identifiée DG002). De plus, le modèle TxGNN n'a produit **aucune prédiction de nouvelle indication** pour Abacavir, ce qui signifie qu'aucune piste de repositionnement n'a été identifiée à cette étape.

L'absence d'AMM en France et le manque de données réglementaires exploitables (lacune DG001 — mises en garde et contre-indications non disponibles) limitent davantage la possibilité de progresser dans l'évaluation. Une collecte de données complémentaire est indispensable avant toute réévaluation.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé à une nouvelle indication de repositionnement n'est enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée à une nouvelle indication de repositionnement n'est disponible actuellement.

---

## Informations de Marché en France

Abacavir ne dispose actuellement d'**aucune AMM** enregistrée dans la base de données consultée. Le statut de marché est : **Non commercialisé**.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

> **Note :** Les données relatives aux mises en garde, contre-indications et interactions médicamenteuses n'ont pas pu être récupérées (lacune DG001). Il est cependant connu qu'Abacavir présente un risque important de **réaction d'hypersensibilité** (potentiellement fatale) chez les porteurs de l'allèle **HLA-B\*5701**. Un dépistage génétique est obligatoire avant l'initiation du traitement.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Aucune nouvelle indication n'a été prédite par le modèle TxGNN pour Abacavir. De plus, plusieurs lacunes de données critiques (mécanisme d'action, informations réglementaires, données de sécurité) empêchent toute progression vers une évaluation de repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Compléter la collecte des données de mécanisme d'action (MOA) via l'API DrugBank (DG002)
- Obtenir les mises en garde et contre-indications officielles via la notice/RCP (DG001)
- Relancer le modèle TxGNN avec des données d'entrée enrichies pour vérifier l'absence de prédictions
- Vérifier le statut réglementaire auprès de l'ANSM et des bases de données européennes (EMA)
- Si une indication cible est identifiée ultérieurement, procéder à une recherche ciblée d'essais cliniques et de littérature

---

*Rapport généré le 2026-04-03 — Version Evidence Pack : v4 — Candidat : TW-DB01048-multi*
*Ce rapport est fourni à titre de recherche uniquement et ne constitue pas un avis médical.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

