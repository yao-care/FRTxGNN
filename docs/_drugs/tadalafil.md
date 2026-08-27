---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 295
evidence_level: L5
indication_count: 8
---

# Tadalafil
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

Utilisation du contexte fourni (Evidence Pack v4, TW-DB00820-multi) pour rédiger le rapport selon le gabarit v5.

# Tadalafil : De la Dysfonction Érectile à l'Hypertrichose Universelle Congénitale de Type Ambras

## Résumé en Une Phrase

Le tadalafil est un inhibiteur de la PDE5 connu principalement pour le traitement de la dysfonction érectile, de l'hyperplasie bénigne de la prostate et de l'hypertension artérielle pulmonaire. Le modèle TxGNN prédit qu'il pourrait être pertinent pour l'**hypertrichose universelle congénitale de type Ambras**, une maladie rare, mais **aucun essai clinique ni publication** ne soutient actuellement cette direction — le score élevé est explicitement signalé par le pipeline lui-même comme un probable artefact du modèle.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Dysfonction érectile / HBP / hypertension artérielle pulmonaire (classe pharmacologique connue ; non documentée dans les sources TFDA/ANSM disponibles — lacune DG002) |
| Nouvelle Indication Prédite | Hypertrichose universelle congénitale de type Ambras |
| Score de Prédiction TxGNN | 99.98% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données structurées sur le mécanisme d'action (MOA) ne sont pas disponibles dans les sources actuelles (lacune de données DG002, sévérité Élevée). Sur la base des informations générales connues sur cette molécule, le tadalafil est un inhibiteur de la phosphodiestérase de type 5 (PDE5) qui potentialise la voie du GMPc pour provoquer un relâchement du muscle lisse vasculaire — mécanisme qui sous-tend ses indications connues (dysfonction érectile, HBP, hypertension artérielle pulmonaire).

L'hypertrichose universelle congénitale de type Ambras est une maladie génétique rare de croissance pileuse excessive et généralisée, sans lien physiopathologique connu avec la voie PDE5/GMPc. Le rationnel fourni par le pipeline TxGNN indique lui-même qu'aucune publication ni essai clinique ne relie le tadalafil à la croissance folliculaire, et qualifie ce score élevé de probable **bruit du modèle**, en l'absence de tout signal DDI ou de présence commerciale du produit en France.

Sur le plan strictement mécanistique, il n'existe donc à ce stade aucune justification pharmacologique plausible reliant le tadalafil à cette indication ; la prédiction doit être interprétée comme une piste exploratoire de très faible confiance (niveau de preuve L5), non comme un signal d'efficacité.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le niveau de preuve est L5 (prédiction du modèle seule) : aucun essai clinique, aucune publication, aucun rationnel mécanistique solide ne relient le tadalafil à l'hypertrichose de type Ambras, et le pipeline signale lui-même ce score comme un possible artefact. De plus, le produit n'est pas commercialisé en France (0 AMM) et une lacune bloquante subsiste sur le résumé des caractéristiques du produit (DG001).

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir les mises en garde et contre-indications officielles (notice TFDA/ANSM) — lacune bloquante DG001
- Documenter formellement le mécanisme d'action (MOA) — lacune DG002
- Rechercher des données précliniques spécifiques (in vitro/in vivo) sur PDE5 et croissance folliculaire avant toute réévaluation
- Noter, à titre de pharmacovigilance et non de piste de repositionnement, le signal isolé rapporté dans un autre candidat prédit (migraine avec aura typique associée au tadalafil, PMID [17059442](https://pubmed.ncbi.nlm.nih.gov/17059442/), rapport de cas) — à surveiller mais sans lien avec l'indication ici évaluée
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

