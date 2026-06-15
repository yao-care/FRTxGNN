---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib : Du Cancer du Poumon Non à Petites Cellules à la Fibromatose Gingivale

## Résumé en Une Phrase

Crizotinib est un inhibiteur de tyrosine kinase ciblant ALK, ROS1 et MET, mondialement approuvé pour le traitement du cancer du poumon non à petites cellules (CPNPC) porteurs de réarrangements ALK ou ROS1.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Fibromatose Gingivale**,
avec **0 essai clinique** et **0 publication** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible (aucune AMM enregistrée en France) |
| Nouvelle Indication Prédite | Fibromatose Gingivale |
| Score de Prédiction TxGNN | 99,81 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Crizotinib est un inhibiteur de tyrosine kinase compétitif de l'ATP ciblant trois récepteurs : **ALK** (Anaplastic Lymphoma Kinase), **ROS1** (ROS Proto-Oncogene 1) et **MET** (Mesenchymal-Epithelial Transition). Son mécanisme d'action repose sur le blocage de la phosphorylation constitutive de ces kinases oncogéniques, induisant l'arrêt de la prolifération tumorale et l'apoptose dans les cellules porteuses de réarrangements ALK ou ROS1. Bien que les données détaillées de mécanisme d'action ne soient pas disponibles dans le présent dossier réglementaire (lacune DG002), ce profil pharmacologique est largement documenté dans la littérature internationale.

La fibromatose gingivale est une pathologie rare caractérisée par une prolifération fibreuse bénigne et progressive de la gencive. Elle est principalement causée par des mutations des gènes **SOS1** (voie RAS/MAPK) ou **GINGF1**, qui n'entretiennent **aucun croisement connu** avec les voies ALK, ROS1 ou MET ciblées par Crizotinib. Bien que l'axe MET/HGF joue théoriquement un rôle mineur dans la prolifération des fibroblastes en contexte général, aucune donnée préclinique (in vitro ou in vivo) ni clinique ne soutient une activité de Crizotinib spécifiquement dans cette maladie.

Cette prédiction TxGNN (rang 1922 sur l'ensemble du graphe de connaissances) semble résulter d'une inférence indirecte via des nœuds partagés liés à la fibroprolifération dans le graphe, plutôt que d'une relation mécanistique directe. La convergence biologique entre les cibles de Crizotinib et la pathogenèse de la fibromatose gingivale reste à ce stade non établie.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Crizotinib ne dispose d'**aucune autorisation de mise sur le marché (AMM) en France** selon les données disponibles à la date de ce rapport. Le médicament est en revanche approuvé dans d'autres pays (notamment États-Unis, Union européenne hors France dans le périmètre de ce dossier) pour le CPNPC ALK+ et ROS1+, ainsi que pour les tumeurs myofibroblastiques inflammatoires (IMT) ALK+.

---

## Cytotoxicité

Crizotinib est un médicament antinéoplasique (inhibiteur de tyrosine kinase, classe des thérapies ciblées). La section suivante s'applique.

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée — Inhibiteur de tyrosine kinase ALK/ROS1/MET (petite molécule orale) |
| Risque de Myélosuppression | Faible à modéré (neutropénie observée dans les essais cliniques ; moins fréquente qu'avec la chimiothérapie cytotoxique conventionnelle) |
| Classification d'Émétogénicité | Faible (voie orale ; nausées et vomissements de grade 1-2 rapportés) |
| Éléments de Surveillance | NFS avec différentielle, transaminases hépatiques (ALAT/ASAT), bilirubine, créatinine, ECG avec intervalle QTc, bilan ophtalmologique (troubles visuels fréquents sous Crizotinib) |
| Protection de Manipulation | Précautions de manipulation selon les réglementations en vigueur pour les médicaments anticancéreux oraux |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
La fibromatose gingivale est une pathologie à médiation génétique (SOS1/GINGF1) sans intersection établie avec les cibles moléculaires de Crizotinib (ALK/ROS1/MET). En l'absence de toute preuve préclinique ou clinique soutenant cette indication, et compte tenu d'un niveau de preuve L5 (prédiction du modèle uniquement), il n'est pas justifié de poursuivre une exploration clinique à ce stade.

**Pour avancer, les éléments suivants sont nécessaires :**

- Données précliniques explorant l'effet de l'inhibition MET/HGF sur la prolifération des fibroblastes gingivaux (études in vitro sur cultures primaires de cellules gingivales)
- Caractérisation moléculaire des tumeurs gingivales porteuses de mutations SOS1 et analyse de l'expression MET dans ces tissus
- Données de mécanisme d'action complètes pour Crizotinib issues de DrugBank (résoudre lacune DG002)
- Notice officielle ANSM et données de sécurité réglementaires françaises (résoudre lacune DG001 — actuellement bloquante pour toute évaluation de sécurité)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

