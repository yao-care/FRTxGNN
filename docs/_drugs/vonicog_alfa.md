---
layout: default
title: Vonicog Alfa
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 10
---

# Vonicog Alfa
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

# Vonicog Alfa : De la Maladie de von Willebrand au Trouble Primaire de la Libération Plaquettaire

## Résumé en Une Phrase

Vonicog alfa (DB12872) est un facteur von Willebrand recombinant (rVWF), dont les essais cliniques et publications rattachés à ce dossier concernent le traitement de la **maladie de von Willebrand** sévère. Le modèle TxGNN le classe en priorité pour le **Trouble Primaire de la Libération Plaquettaire**, avec un score de 99,98 %, mais **aucun essai clinique ni publication ne soutient actuellement cette direction spécifique**, et la note mécanistique jointe qualifie elle-même le lien de « faible ».

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de von Willebrand (sévère) — déduite du contexte des essais cliniques du pack ; aucune AMM française disponible |
| Nouvelle Indication Prédite | Trouble Primaire de la Libération Plaquettaire |
| Score de Prédiction TxGNN | 99,98 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles (écart de données DG002, sévérité High). Sur la base des informations connues issues des essais cliniques rattachés à ce dossier, vonicog alfa fait partie de la classe des facteurs von Willebrand recombinants, et son efficacité a été démontrée dans plusieurs essais de Phase 3 chez des patients atteints de maladie de von Willebrand sévère.

Le rationnel de repositionnement fourni pour cette indication est cependant explicitement défavorable : « VWF médie principalement l'adhésion plaquettaire et non la voie de libération des granules ; le lien mécanistique est faible, sans essai clinique ni littérature à l'appui. » Autrement dit, le score TxGNN élevé (99,98 %) reflète une similarité computationnelle entre entités du graphe de connaissances, mais ne correspond pas à une voie biologique validée pour ce trouble spécifique de sécrétion plaquettaire — à la différence de la maladie de von Willebrand, où VWF est directement le facteur déficitaire.

Il n'existe donc pas, en l'état des données transmises, de justification mécanistique solide reliant l'indication d'origine à cette nouvelle indication prédite.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

*(Note : l'obtention des mises en garde/contre-indications TFDA — écart DG001, sévérité Blocking — est un préalable indispensable avant toute évaluation de sécurité S1 pour ce candidat, quelle que soit l'indication considérée.)*

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le score TxGNN est élevé mais n'est appuyé par aucun essai clinique ni publication, et le rationnel mécanistique fourni indique lui-même une faible correspondance biologique (VWF agit sur l'adhésion plaquettaire, non sur la libération des granules). Combiné à l'absence totale de données de sécurité (DG001, Blocking) et à l'absence de commercialisation en France, le dossier ne permet pas de dépasser le stade S0.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les mises en garde/contre-indications TFDA (DG001, Blocking) pour débloquer l'évaluation de sécurité S1
- Obtenir les données de mécanisme d'action via l'API DrugBank (DG002)
- Rechercher des preuves précliniques ou mécanistiques spécifiques reliant VWF à la voie de libération plaquettaire avant toute exploration clinique
- À noter pour information : dans ce même pack, l'indication « hemophilia » (rang 4) dispose d'un niveau de preuve nettement supérieur (L2, S2, Proceed with Guardrails), bien que les essais et la littérature associés portent en réalité sur la maladie de von Willebrand — un possible désalignement d'étiquette d'ontologie à vérifier séparément
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

