---
layout: default
title: Tildrakizumab
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 4
---

# Tildrakizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Tildrakizumab : Du Psoriasis en Plaques à la Rétinopathie Diabétique Non Proliférante Sévère

## Résumé en Une Phrase

Tildrakizumab (DB14004) est un anticorps monoclonal anti-IL-23p19, dont l'indication d'origine connue est le psoriasis en plaques modéré à sévère — le médicament n'est toutefois pas commercialisé en France à ce jour.
Le modèle TxGNN prédit qu'il pourrait être pertinent pour la **rétinopathie diabétique non proliférante sévère**,
mais **aucun essai clinique** ni **aucune publication** ne soutient actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Psoriasis en plaques (classe IL-23p19, non commercialisé en France — donnée non disponible dans l'Evidence Pack) |
| Nouvelle Indication Prédite | Rétinopathie diabétique non proliférante sévère |
| Score de Prédiction TxGNN | 99.63% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action officiel (champ `original_moa`) ne sont pas disponibles dans cet Evidence Pack. Sur la base des informations disponibles dans l'analyse de repositionnement, tildrakizumab est un inhibiteur de l'IL-23p19 qui bloque l'axe IL-23/Th17, une voie inflammatoire connue pour son rôle dans le psoriasis.

Le lien proposé avec la rétinopathie diabétique repose sur une hypothèse mécanistique indirecte : l'axe IL-17/IL-23 est décrit dans la littérature générale comme pouvant contribuer à l'inflammation rétinienne et à la néovascularisation, des processus impliqués dans la rétinopathie diabétique. Cependant, il n'existe aucune preuve directe reliant spécifiquement la rétinopathie diabétique à l'inhibition de l'IL-23, ni aucun rapport clinique ou préclinique concernant tildrakizumab (ou une molécule de la même classe) dans cette indication.

Cette prédiction doit donc être considérée comme une inférence de graphe de connaissances (TxGNN) sans validation biologique ou clinique spécifique au médicament à ce stade.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

## Preuves de la Littérature

Aucune littérature associée disponible actuellement

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur une association du graphe TxGNN (score 99.63%) sans aucun essai clinique ni publication à l'appui, et le lien mécanistique avec l'axe IL-23/Th17 reste théorique et non spécifique au médicament. Le niveau de preuve L5 ne justifie pas de progression au-delà de la phase d'évaluation préliminaire.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mécanisme d'action officiel complet (actuellement Data Gap)
- Données de sécurité TFDA (mises en garde, contre-indications, interactions) — actuellement bloquantes
- Études précliniques ciblées évaluant l'effet de l'inhibition de l'IL-23 dans des modèles de rétinopathie diabétique
- Surveillance continue des bases d'essais cliniques (ClinicalTrials.gov, ICTRP) et de la littérature (PubMed) pour détecter l'apparition de preuves spécifiques
- Statut réglementaire en France à réévaluer si le médicament venait à être commercialisé
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

