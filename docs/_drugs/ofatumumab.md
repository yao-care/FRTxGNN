---
layout: default
title: Ofatumumab
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 8
---

# Ofatumumab
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

# Ofatumumab : De la Leucémie Lymphoïde Chronique à la LLC/LPL avec Hypermutation Somatique du Gène IGHV

## Résumé en Une Phrase

Ofatumumab est un anticorps monoclonal humain anti-CD20, dont la littérature du dossier (PMID 22830942) rapporte l'approbation initiale pour la leucémie lymphoïde chronique (LLC) réfractaire à la fludarabine et à l'alemtuzumab. Le modèle TxGNN prédit qu'il pourrait être pertinent pour la **LLC/LPL avec hypermutation somatique du gène IGHV**, un sous-groupe moléculaire pronostique de la LLC, mais **aucun essai clinique ni publication spécifique** à ce sous-groupe n'est actuellement répertorié dans le dossier de preuves.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible via les AMM françaises (produit non commercialisé) ; d'après la littérature du dossier : leucémie lymphoïde chronique (LLC) réfractaire (PMID 22830942) |
| Nouvelle Indication Prédite | Leucémie lymphoïde chronique/lymphome lymphocytique à petits lymphocytes (LLC/LPL) avec hypermutation somatique du gène IGHV |
| Score de Prédiction TxGNN | 99,77 % |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le champ structuré de mécanisme d'action (MOA) est marqué comme donnée manquante. Cependant, la littérature contenue dans le dossier (ex. PMID 20068404, 20481657, 22830942) décrit Ofatumumab comme un anticorps monoclonal humain IgG1κ entièrement humain, ciblant un épitope distinct proche de la membrane sur la molécule CD20, et induisant la lyse des lymphocytes B via la cytotoxicité dépendante du complément (CDC) et la cytotoxicité cellulaire dépendante des anticorps (ADCC). Le même PMID 22830942 indique que son approbation initiale par la FDA (2009) concernait la LLC réfractaire à la fludarabine et à l'alemtuzumab.

L'indication prédite en tête de classement n'est pas une nouvelle aire pathologique, mais un sous-groupe moléculaire de l'indication d'origine : la LLC/LPL stratifiée selon le statut de mutation somatique du gène IGHV, un marqueur pronostique bien établi en LLC. Il s'agit donc d'un raffinement de population plutôt que d'un repositionnement vers une maladie distincte.

L'expression de CD20 étant conservée indépendamment du statut mutationnel IGHV, le mécanisme anti-CD20 est en principe applicable de façon similaire à ce sous-groupe. Cette continuité mécanistique est indirectement appuyée par le volume important de preuves déjà disponibles pour l'indication apparentée « LLC/LPL » non stratifiée (rang 5 du dossier : 34 essais cliniques et 20 publications), bien qu'aucune étude stratifiée spécifiquement par statut IGHV ne soit encore recensée dans ce dossier.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement pour ce sous-groupe moléculaire spécifique.

*Note : l'indication apparentée non stratifiée « LLC/LPL » (rang 5 du dossier de preuves) dispose de 34 essais cliniques répertoriés, dont plusieurs essais de Phase 3, qui pourraient éclairer une future revue de preuves ciblée sur ce sous-groupe.*

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement pour ce sous-groupe moléculaire spécifique.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée — anticorps monoclonal anti-CD20 de 2ᵉ génération (classe identifiée via la littérature du dossier, ex. PMID 20068404) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Veuillez consulter les mises en garde et précautions de la notice |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'indication prédite en tête de classement (LLC/LPL avec hypermutation somatique IGHV) affiche un score TxGNN élevé (99,77 %) mais ne dispose d'aucun essai clinique ni publication spécifique répertorié (niveau de preuve L5).
- Un data gap bloquant (DG001 — mises en garde/contre-indications TFDA) empêche toute évaluation de sécurité S1 pour ce candidat.
- Le produit n'est pas commercialisé en France (0 AMM), ce qui limite toute mise en œuvre opérationnelle immédiate.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice TFDA/EMA pour lever le data gap bloquant DG001 (mises en garde, contre-indications)
- Compléter les données structurées de mécanisme d'action via l'API DrugBank (DG002)
- Rechercher spécifiquement des essais et publications stratifiés par statut de mutation IGHV en LLC/LPL, afin d'étayer directement l'indication de rang 1
- Examiner en parallèle l'indication de rang 5 (LLC/LPL non stratifiée), déjà appuyée par 34 essais cliniques et 20 publications, comme piste de repositionnement plus mature
- Évaluer la stratégie d'enregistrement en France compte tenu de l'absence actuelle d'AMM
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

