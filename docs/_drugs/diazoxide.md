---
layout: default
title: Diazoxide
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
---

# Diazoxide
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

# Diazoxide : De l'Hypoglycémie Hyperinsulinémique à l'Hypotrichosis Simplex du Cuir Chevelu

## Résumé en Une Phrase

Diazoxide est un ouvreur des canaux KATP, historiquement utilisé dans le traitement de l'hypoglycémie hyperinsulinémique et des urgences hypertensives, sans enregistrement actuel en France.
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Hypotrichosis Simplex du Cuir Chevelu** — une maladie génétique rare caractérisée par une perte de cheveux progressive et diffuse du cuir chevelu —
avec **0 essai clinique** et **0 publication** soutenant directement cette indication à ce jour. Des preuves indirectes de niveau L4 existent cependant pour l'alopécie en général (9 publications, prédiction rang 4).

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypoglycémie hyperinsulinémique (non enregistré en France) |
| Nouvelle Indication Prédite | Hypotrichosis Simplex du Cuir Chevelu |
| Score de Prédiction TxGNN | 99.96% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations référencées dans la littérature incluse (notamment PMID 2085505, 8326148, 27161588), diazoxide agit comme **ouvreur des canaux KATP** (canaux potassiques sensibles à l'ATP). En activant les canaux KATP des cellules β pancréatiques (via la sous-unité SUR1), il inhibe la sécrétion d'insuline — d'où son usage de première ligne dans les hyperinsulinismes congénitaux. En activant les canaux SUR2B du muscle lisse vasculaire, il induit une vasodilatation périphérique — d'où son usage antihypertenseur historique.

La prédiction pour l'hypotrichosis simplex du cuir chevelu repose sur une analogie mécanistique directe avec le **minoxidil**, traitement approuvé de l'alopécie : les deux molécules ouvrent les canaux KATP, provoquant une vasodilatation périvasculaire folliculaire et une activation directe des cellules de la papille dermique, ce qui prolonge la phase anagène (croissance) du cycle pilaire. Cette hypothèse est indirectement validée par un fait pharmacologique bien établi : l'**hypertrichose** (croissance excessive des poils) est l'un des effets indésirables les plus fréquemment rapportés du diazoxide systémique, observé chez les nourrissons traités pour hyperinsulinisme (PMID 30083030 : 8,6 % des patients). Une étude chez le macaque à queue de moignon a par ailleurs démontré une repousse des cheveux après application topique de diazoxide à 5 % (PMID 2085505), constituant une preuve préclinique directe de la classe.

Toutefois, l'hypotrichosis simplex du cuir chevelu est une maladie génétique rare impliquant des mutations structurelles (laminine LAMA3, cornéodesmosine CDSN, etc.) dont la physiopathologie va au-delà d'une simple insuffisance de vascularisation folliculaire. Aucune étude clinique ni préclinique n'a été publiée spécifiquement pour cette indication, ce qui justifie le niveau de preuve L5 et la décision Hold.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

Diazoxide ne dispose d'aucune autorisation de mise sur le marché (AMM) en France. Aucune donnée réglementaire française disponible dans ce dossier.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
L'indication « hypotrichosis simplex du cuir chevelu » est de niveau L5, sans aucune preuve clinique ou préclinique spécifique, et diazoxide n'est pas commercialisé en France. La plausibilité mécanistique reste théorique (analogie KATP/minoxidil, confirmée indirectement par l'hypertrichose iatrogène), mais elle est insuffisante pour justifier un avancement sans données empiriques dédiées.

> ⚠️ **Note sur le paysage de prédictions :** Parmi les 10 prédictions TxGNN analysées, le rang 10 (**hyperinsulinisme dominant autosomique par déficit en Kir6.2**) présente le lien mécanistique le plus solide et direct — diazoxide compensant précisément la perte de fonction de la sous-unité Kir6.2 du canal KATP. Cette piste mérite une évaluation prioritaire en parallèle.

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmation du mécanisme d'action complet via DrugBank API et consultation de la notice ANSM
- Données de sécurité complètes (contre-indications, mises en garde, interactions médicamenteuses)
- Études précliniques sur follicules pileux humains ou modèles ex vivo de cuir chevelu
- Évaluation d'une formulation topique (5 % diazoxide, analogue à l'étude chez le macaque, PMID 2085505) pour limiter les effets systémiques (hyperglycémie, rétention hydrique)
- Consultation d'un dermatologue spécialisé en maladies rares du cheveu pour évaluer la pertinence clinique dans ce sous-type génétique précis
- Stratégie réglementaire pour une indication orpheline (procédure d'accès précoce/ATU en France, étiquetage ORPHA)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

