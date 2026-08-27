---
layout: default
title: Selpercatinib
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 3
---

# Selpercatinib
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

Utilisation du contexte fourni pour rédiger le rapport directement (tâche de génération de contenu structuré, pas de recherche de code nécessaire).

# Selpercatinib : Des Cancers RET Fusion-Positifs à l'Hypertension Pulmonaire

## Résumé en Une Phrase

Selpercatinib est un inhibiteur sélectif de la tyrosine kinase RET, dont l'usage connu concerne les cancers RET fusion-positifs ou RET-mutés (mentionnés dans les données comme cancer médullaire de la thyroïde, CBNPC). Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Hypertension Pulmonaire**, mais cette direction n'est actuellement soutenue par **aucun essai clinique** et seulement **3 publications** dont la pertinence directe avec l'indication prédite reste à établir.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancers RET fusion-positifs / RET-mutés (ex. carcinome médullaire de la thyroïde, CBNPC) — non documentée formellement dans ce pack (donnée manquante côté réglementaire) |
| Nouvelle Indication Prédite | Hypertension Pulmonaire |
| Score de Prédiction TxGNN | 99.18% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce pack. Sur la base des informations connues, selpercatinib est un inhibiteur hautement sélectif de la tyrosine kinase RET, dont l'efficacité dans les cancers RET fusion-positifs/mutés a été établie, et mécanistiquement il pourrait exister un lien avec l'hypertension pulmonaire via la voie de signalisation RET/GDNF.

La voie GDNF/RET a été évoquée dans la littérature préclinique sur le remodelage vasculaire pulmonaire, mais aucune étude n'établit à ce jour de lien direct entre l'inhibition de RET par le selpercatinib et le traitement de l'hypertension pulmonaire. Ce lien mécanistique reste donc **spéculatif** : il repose sur une analogie de voie de signalisation et non sur une preuve directe de repositionnement.

En l'état, cette prédiction relève exclusivement du score algorithmique TxGNN, sans corroboration clinique ou préclinique ciblée sur l'hypertension pulmonaire à ce jour.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Étude de cohorte (pharmacovigilance réelle) | Frontiers in pharmacology | Comparaison des effets indésirables entre pralsetinib et selpercatinib à partir de la base FAERS ; pas de données spécifiques sur l'hypertension pulmonaire |
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Étude de cohorte rétrospective | Therapeutic advances in medical oncology | Efficacité en vie réelle du selpercatinib dans le CBNPC RET fusion-positif (programme d'accès, étude SIREN) ; ne porte pas sur l'hypertension pulmonaire |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Rapport de cas | Cureus | Carcinome médullaire thyroïdien métastatique associé au syndrome MEN2B (mutation RET M918T), défis de prise en charge à long terme sous thérapie ciblée ; sans lien avec l'hypertension pulmonaire |

**Note :** ces trois publications documentent l'usage oncologique du selpercatinib (efficacité, tolérance, contexte génétique RET) mais aucune n'aborde directement l'hypertension pulmonaire. Elles ne constituent donc pas une preuve de repositionnement, seulement un contexte pharmacologique général sur la molécule.

---

## Cytotoxicité

*Cette section s'applique car le selpercatinib cible des cancers RET-dépendants (carcinome médullaire de la thyroïde, CBNPC RET+).*

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase, sélectif RET) — non cytotoxique conventionnel |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Fonction hépatique et tension artérielle recommandées en surveillance générale des inhibiteurs de tyrosine kinase — à confirmer par la notice officielle |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La prédiction repose uniquement sur le score algorithmique TxGNN (Niveau de preuve L5) : aucun essai clinique ne cible l'hypertension pulmonaire, et la littérature disponible concerne l'usage oncologique du selpercatinib sans lien direct établi. L'absence totale de données de sécurité TFDA (仿單/warnings) bloque par ailleurs toute évaluation de sécurité initiale (S1).

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice/RCP TFDA du selpercatinib pour lever le blocage sur l'évaluation de sécurité (DG001)
- Données détaillées de mécanisme d'action via DrugBank (DG002)
- Études précliniques ciblées sur le rôle de RET dans le remodelage vasculaire pulmonaire, pour étayer ou infirmer le lien mécanistique actuellement spéculatif
- Recherche complémentaire d'essais cliniques ou d'ICTRP dédiés à l'hypertension pulmonaire
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

