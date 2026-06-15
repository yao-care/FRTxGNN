---
layout: default
title: Chlorambucil
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 8
---

# Chlorambucil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Chlorambucil : De la Leucémie Lymphoïde Chronique à la LLC/SLL avec Hypermutation Somatique IGHV

---

## Résumé en Une Phrase

Chlorambucil est un agent alkylant historiquement utilisé pour le traitement de la leucémie lymphoïde chronique (LLC) et des lymphomes B indolents, bien qu'il ne soit pas approuvé en France.
Le modèle TxGNN prédit qu'il pourrait être particulièrement efficace pour la **LLC/SLL avec hypermutation somatique des gènes de la région variable des chaînes lourdes d'immunoglobulines (IGHV-muté)**, sous-type moléculaire de meilleur pronostic.
Aucune publication ni essai clinique n'est disponible pour ce sous-type moléculaire en tant que population cible indépendante, mais des données de sous-groupes issues de grands essais Phase 3 de LLC apportent un soutien mécanistique solide.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Non approuvé en France (usage historique mondial : leucémie lymphoïde chronique) |
| Nouvelle Indication Prédite | LLC/SLL avec hypermutation somatique des gènes IGHV (sous-type IGHV-muté) |
| Score de Prédiction TxGNN | 99.72% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action (MOA) de Chlorambucil ne sont pas disponibles dans ce pack. Sur la base des informations connues dans la littérature mondiale, Chlorambucil est un agent alkylant de la famille des moutardes azotées (chloroéthylamine). Il agit en formant des ponts covalents entre les deux brins d'ADN (liaisons croisées interbrins), bloquant la réplication et induisant l'apoptose des cellules B en prolifération. Ce mécanisme est indépendant du cycle cellulaire, ce qui lui confère une activité sur les lymphocytes B malins à faible index mitotique, caractéristiques des LLC indolentes.

La LLC/SLL avec hypermutation somatique IGHV (sous-type IGHV-muté) constitue une entité biologiquement distincte. Ce sous-type conserve une capacité de réparation par recombinaison homologue relativement préservée et présente une dépendance moindre aux voies de signalisation BCR par rapport au sous-type IGHV non muté. Cette caractéristique le rend plus sensible aux dommages à l'ADN induits par les agents alkylants, dont Chlorambucil. Cliniquement, plusieurs essais de Phase 3 majeurs (CLL11, RESONATE-2) ont établi une meilleure réponse au Chlorambucil dans le sous-type IGHV-muté, où les taux de réponse globale et la survie sans progression sont supérieurs à ceux observés dans le sous-type non muté.

La prédiction TxGNN est donc biologiquement cohérente : elle identifie le sous-type moléculaire de la LLC pour lequel Chlorambucil présente le meilleur rationnel thérapeutique. Toutefois, aucun essai randomisé n'a été conçu avec ce sous-type moléculaire comme critère d'inclusion principal, et les thérapies ciblées modernes (BTKi, BCL-2i ± anti-CD20) ont largement supplanté Chlorambucil en première ligne, même dans le sous-type IGHV-muté.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour ce sous-type moléculaire spécifique (LLC/SLL IGHV-muté comme population cible principale).

> **Note clinique :** Les essais Phase 3 CLL11 (Chlorambucil ± Obinutuzumab/Rituximab) et RESONATE-2 (Ibrutinib vs Chlorambucil) incluent le statut IGHV comme facteur d'analyse en sous-groupe, mais ne ciblent pas ce sous-type moléculaire en tant que population principale.

---

## Preuves de la Littérature

Aucune littérature publiée spécifiquement dédiée à Chlorambucil dans la LLC/SLL IGHV-muté en tant que population cible indépendante.

---

## Informations de Marché en France

Chlorambucil n'est pas commercialisé en France. Aucune autorisation de mise sur le marché (AMM) n'est enregistrée auprès de l'ANSM.

---

## Cytotoxicité

Chlorambucil est un agent antinéoplasique cytotoxique (agent alkylant, classe moutardes azotées). La section suivante s'applique.

| Élément | Contenu |
|---|---|
| Classification de Cytotoxicité | Cytotoxique conventionnel — Agent alkylant / Moutarde azotée (chloroéthylamine) |
| Risque de Myélosuppression | **Élevé** — neutropénie, thrombocytopénie et anémie fréquentes, cumulatives et dose-dépendantes ; nadirs typiques à J14–J21 |
| Classification d'Émétogénicité | **Faible à modérée** (administration per os, dose standard) |
| Éléments de Surveillance | NFS avec différentielle (avant chaque cycle et à mi-cycle), fonction hépatique (ASAT, ALAT, bilirubine), fonction rénale (créatinine), surveillance cumulative de la myélosuppression |
| Protection de Manipulation | Manipulation selon les réglementations applicables aux médicaments cytotoxiques — préparation sous hotte à flux laminaire en pharmacie hospitalière, équipements de protection individuelle (gants, masque, surblouse) obligatoires |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité (données de mises en garde, contre-indications et interactions médicamenteuses non disponibles dans ce pack).

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Les données de sous-groupes issues des essais Phase 3 de référence dans la LLC (CLL11, RESONATE-2) confirment une meilleure réponse de Chlorambucil dans le sous-type IGHV-muté, et le mécanisme alkylant est biologiquement cohérent avec la biologie de ce sous-type. Cependant, l'absence d'essai randomisé dédié à cette entité moléculaire, conjuguée au remplacement progressif de Chlorambucil par des thérapies ciblées de nouvelle génération, impose une progression avec garde-fous stricts.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données complètes de mécanisme d'action (MOA) — à récupérer via DrugBank API
- Données de sécurité détaillées (mises en garde, contre-indications, interactions médicamenteuses) — à récupérer via fiche ANSM / notice internationale
- Extraction et méta-analyse des données de sous-groupes IGHV issues des essais CLL11, RESONATE-2, CLL10 et MABLE
- Évaluation du positionnement thérapeutique actuel face aux BTKi (Ibrutinib, Acalabrutinib) et BCL-2i (Venetoclax ± Obinutuzumab) en première ligne, y compris dans le sous-type IGHV-muté
- Analyse de faisabilité réglementaire pour une démarche AMM en France dans une indication à entité moléculaire spécifique
- Plan de surveillance de sécurité adapté à la population cible (patients âgés, comorbidités cardiovasculaires fréquentes)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

