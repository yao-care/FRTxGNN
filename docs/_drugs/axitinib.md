---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib : Du Carcinome Rénal Avancé au Carcinome Rénal associé aux Translocations Xp11.2/Fusions du Gène TFE3

## Résumé en Une Phrase

Axitinib (Inlyta®) est un inhibiteur sélectif de deuxième génération des récepteurs du VEGF (VEGFR-1/2/3), approuvé dans de nombreux pays pour le traitement du carcinome rénal avancé en deuxième ligne de traitement, mais non commercialisé en France.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Carcinome Rénal associé aux Translocations Xp11.2/Fusions du Gène TFE3**,
avec **1 essai clinique** en cours apportant des preuves directes pour cette indication rare — un sous-type pour lequel les options thérapeutiques restent très limitées et aucune publication indexée n'est actuellement disponible.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Carcinome rénal avancé/métastatique — deuxième ligne (approbation FDA/EMA ; non enregistré en France) |
| Nouvelle Indication Prédite | Carcinome Rénal associé aux Translocations Xp11.2/Fusions du Gène TFE3 |
| Score de Prédiction TxGNN | 99.90% |
| Niveau de Preuve | L2 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier local (Data Gap DG002). Sur la base des données publiées dans la littérature internationale, axitinib est un inhibiteur oral puissant et sélectif des récepteurs à activité tyrosine kinase du facteur de croissance endothélial vasculaire (VEGFR-1, VEGFR-2 et VEGFR-3), avec une affinité 10 fois supérieure à celle du sunitinib ou du sorafénib pour ces cibles. Il inhibe l'angiogenèse tumorale en bloquant la signalisation VEGF/VEGFR, privant les cellules cancéreuses de leur apport vasculaire.

Le carcinome rénal à translocation Xp11.2/TFE3 est un sous-type rare (<5 % de tous les carcinomes rénaux), survenant préférentiellement chez les enfants et jeunes adultes. Les protéines de fusion TFE3 qui en résultent activent de manière aberrante des programmes transcriptionnels qui induisent une surexpression des gènes pro-angiogéniques — notamment le VEGF — entraînant une activation relative de la voie VEGFR. Ce mécanisme moléculaire constitue le rationnel biologique principal justifiant l'utilisation d'axitinib dans ce sous-type, par analogie avec le carcinome rénal à cellules claires où la perte de VHL active la même cascade VEGF.

La stratégie d'association axitinib + immunothérapie (nivolumab), déjà validée dans le carcinome rénal à cellules claires (essais KEYNOTE-426, JAVELIN Renal 101), est directement testée dans ce sous-type rare via l'essai NCT03595124, qui recrute toutes tranches d'âge. L'approche combinée est biologiquement cohérente : la voie VEGFR étant activée, axitinib peut potentialiser la réponse immunitaire induite par le nivolumab en normalisant la vascularisation tumorale. Cependant, la taille d'échantillon extrêmement réduite (n=15) et la rareté de la maladie imposent une interprétation prudente des résultats à venir.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | Actif, non en recrutement | 15 | Essai randomisé évaluant axitinib + nivolumab versus nivolumab seul dans le carcinome rénal à translocation TFE3 (tRCC) non résécable ou métastatique, tous groupes d'âge confondus. L'axitinib agit en bloquant les enzymes nécessaires à la croissance cellulaire tumorale ; le nivolumab mobilise le système immunitaire contre les cellules cancéreuses. Fin de l'étude prévue en novembre 2026 — données de maturité attendues. |

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour ce sous-type spécifique (carcinome rénal avec translocation Xp11.2/TFE3).

---

## Informations de Marché en France

Axitinib ne dispose d'aucune Autorisation de Mise sur le Marché (AMM) en France. Le médicament est commercialisé sous la marque **Inlyta®** (Pfizer) dans plusieurs pays (États-Unis, Japon, Union Européenne) pour le traitement du carcinome rénal avancé en deuxième ligne après échec d'un traitement antérieur. Toute utilisation en France relèverait d'une procédure d'accès précoce (AAP) ou d'une autorisation temporaire d'utilisation (ATU/RTU) auprès de l'ANSM.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée — Inhibiteur de tyrosine kinase VEGFR (TKI de 2e génération, classe anti-angiogénique orale) |
| Risque de Myélosuppression | Faible à modéré (nettement inférieur à la chimiothérapie cytotoxique conventionnelle ; thrombocytopénie et neutropénie peu fréquentes) |
| Classification d'Émétogénicité | Faible (administration orale ; nausées légères à modérées possibles) |
| Éléments de Surveillance | Pression artérielle (hypertension artérielle : effet de classe fréquent et dose-dépendant), NFS avec différentielle, bilan hépatique et rénal, fonction thyroïdienne, protéinurie, cicatrisation des plaies |
| Protection de Manipulation | Précautions standard pour médicaments oraux antinéoplasiques : manipulation avec gants, ne pas écraser ou fractionner les comprimés, élimination selon les filières déchets cytotoxiques |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. Les données de mises en garde, contre-indications et interactions médicamenteuses locales n'ont pas été transmises dans ce dossier (Data Gap DG001 — sévérité : Bloquante).

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Un essai clinique de Phase 2 dédié (NCT03595124) évalue directement la combinaison axitinib + nivolumab dans ce sous-type rare, confirmant un rationnel clinique suffisant et une faisabilité de la démarche ; cependant, l'échantillon extrêmement réduit (n=15), l'absence totale de publications spécifiques à ce sous-type et l'indisponibilité du médicament en France imposent une surveillance rigoureuse et une décision au cas par cas.

**Pour avancer, les éléments suivants sont nécessaires :**
- **Données de sécurité complètes** : extraction de la notice officielle (mises en garde, contre-indications, interactions médicamenteuses) — DG001 bloquant
- **Données MOA confirmées** : requête DrugBank API pour compléter le profil pharmacologique — DG002
- **Résultats finaux de NCT03595124** : données d'efficacité et de tolérance attendues à la clôture de l'étude (novembre 2026)
- **Démarche réglementaire en France** : évaluation de l'éligibilité à un Accès Précoce (ANSM) pour ce sous-type rare, notamment en population pédiatrique
- **Plan de pharmacovigilance spécifique** : adaptation pour la population pédiatrique et jeunes adultes, avec suivi de la tolérance cardiovasculaire (hypertension) et du développement osseux
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

