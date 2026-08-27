---
layout: default
title: Palbociclib
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 4
---

# Palbociclib
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

# Palbociclib : Du Cancer du Sein Métastatique à l'Hyperthyroïdie

## Résumé en Une Phrase

Palbociclib est un inhibiteur de CDK4/6, initialement utilisé dans le traitement du cancer du sein métastatique HR+/HER2- (identité de classe confirmée par la littérature du dossier, les champs réglementaires officiels étant absents).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Hyperthyroïdie**,
mais cette direction n'est actuellement soutenue par **aucun essai clinique** ni **aucune publication** — il s'agit d'un score de prédiction pur, sans validation externe.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer du sein métastatique HR+/HER2- *(déduit du contexte littérature du dossier ; aucune AMM française disponible, médicament non commercialisé)* |
| Nouvelle Indication Prédite | Hyperthyroïdie |
| Score de Prédiction TxGNN | 99.44 % (rang 4021) |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles via DrugBank (écart de données bloquant pour l'évaluation de sécurité, DG002). Sur la base des publications incluses dans ce dossier — notamment une décrivant Palbociclib comme « a dual CDK4/6 kinase inhibitor used for breast cancer » —, on sait que le médicament appartient à la classe des inhibiteurs de CDK4/6, agissant sur l'axe cycline-dépendante-kinase/Rb pour bloquer la prolifération cellulaire, et que son usage établi concerne le cancer du sein métastatique.

Contrairement aux autres indications candidates de ce dossier (par exemple la polyarthrite rhumatoïde, qui dispose d'un rationnel mécanistique via l'action de CDK4/6 sur la prolifération des fibroblastes synoviaux), **aucun lien biologique connu n'existe entre l'inhibition de CDK4/6 et la régulation de la sécrétion des hormones thyroïdiennes**. Le rationnel du dossier le confirme explicitement : « CDK4/6 抑制與甲狀腺激素分泌調控無已知生物路徑關聯 » (aucune voie biologique connue reliant l'inhibition de CDK4/6 à la régulation de la sécrétion thyroïdienne).

Cette prédiction repose donc uniquement sur le score du modèle TxGNN, sans hypothèse mécanistique vérifiable ni preuve clinique ou préclinique à l'appui.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Cytotoxicité

*(Section incluse car Palbociclib est un anticancéreux à cible moléculaire — CDK4/6 — d'après le contexte du dossier, bien que l'indication d'origine ne soit pas formellement enregistrée dans les champs réglementaires.)*

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de CDK4/6) |
| Risque de Myélosuppression | Élevé — la littérature du dossier rapporte une myélosuppression induite par palbociclib et des événements de suppression médullaire fréquents pour la classe des inhibiteurs de CDK4/6 |
| Classification d'Émétogénicité | Non documentée dans le dossier — consulter la notice |
| Éléments de Surveillance | NFS complète (risque de neutropénie documenté), fonction hépatique et rénale (à confirmer via la notice TFDA, cf. DG001) |
| Protection de Manipulation | Non documentée dans le dossier — se référer aux règlements locaux de manipulation des médicaments dangereux/cytotoxiques |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité (mises en garde, contre-indications et interactions médicamenteuses ne sont pas disponibles dans ce dossier — DG001, écart bloquant).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Aucune preuve clinique ou de littérature ne soutient l'hyperthyroïdie comme indication candidate, et le rationnel mécanistique proposé par le dossier lui-même exclut tout lien biologique connu avec l'inhibition de CDK4/6. Le score TxGNN élevé n'est à ce stade pas corroboré.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action (MOA) complètes via DrugBank (DG002)
- Mises en garde/contre-indications de la notice TFDA — écart bloquant pour l'évaluation de sécurité S1 (DG001)
- Recherche ciblée (préclinique ou cas clinique) d'un lien entre l'axe CDK4/6-Rb et la fonction thyroïdienne, avant toute réévaluation

**Note :** parmi les 4 indications candidates évaluées dans ce dossier pour Palbociclib, la **polyarthrite rhumatoïde** (rang 2, niveau de preuve L4, étape S1, recommandation « Research Question ») dispose de la base de preuves la plus solide (4 publications, dont un cas clinique humain et des modèles précliniques cohérents) et pourrait justifier un rapport dédié distinct.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

