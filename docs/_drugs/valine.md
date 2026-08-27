---
layout: default
title: Valine
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 10
---

# Valine
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

# Valine : D'un Acide Aminé Essentiel à la Cholangite Sclérosante (Prédiction)

## Résumé en Une Phrase

La valine est un acide aminé essentiel à chaîne ramifiée (BCAA), sans indication thérapeutique enregistrée et non commercialisée comme médicament en France (0 AMM). Le modèle TxGNN prédit une association avec la **Cholangite Sclérosante**, mais cette direction n'est actuellement soutenue par **aucun essai clinique** et seulement **2 publications** dont la pertinence mécanistique est faible et indirecte.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible — la valine est un acide aminé essentiel, sans indication thérapeutique enregistrée |
| Nouvelle Indication Prédite | Cholangite Sclérosante (sclerosing cholangitis) |
| Score de Prédiction TxGNN | 99.42% |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la valine est un acide aminé essentiel à chaîne ramifiée (BCAA), impliqué dans la synthèse protéique et le métabolisme énergétique ; elle n'est enregistrée dans aucune AMM en France et ne possède pas d'indication thérapeutique établie.

Le lien mécanistique proposé par le modèle TxGNN entre la valine et la cholangite sclérosante repose sur une littérature qui concerne en réalité le métabolisme de la **tyrosine** (et non de la valine) dans le cadre de maladies hépatiques cholestatiques (cirrhose biliaire primitive et cholangite sclérosante primitive). Aucune des publications identifiées ne décrit d'action directe de la valine sur cette pathologie.

Ce lien doit donc être considéré comme **faible et indirect** : il s'agit d'une association statistique du modèle plutôt que d'une hypothèse mécanistique étayée. Aucune étude interventionnelle ou clinique n'a testé la valine dans cette indication à ce jour.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39015781](https://pubmed.ncbi.nlm.nih.gov/39015781/) | 2024 | Randomisation Mendélienne | Frontiers in medicine | Étude de causalité entre métabolites sanguins et maladies hépatiques cholestatiques (PBC/PSC) — ne porte pas spécifiquement sur la valine |
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohorte | BMC gastroenterology | Relation entre concentration plasmatique de tyrosine et fatigue dans la cirrhose biliaire primitive et la cholangite sclérosante primitive — porte sur la tyrosine, pas la valine |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le lien mécanistique entre la valine et la cholangite sclérosante repose sur des études portant sur un autre métabolite (la tyrosine) et non sur la valine elle-même. Aucun essai clinique n'existe, la littérature disponible est indirecte, et la valine n'a ni statut de médicament ni AMM en France. Les preuves sont actuellement insuffisantes pour justifier une investigation active.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de notice/mises en garde TFDA (DG001, bloquant) — indisponibles actuellement
- Données de mécanisme d'action (MOA) via DrugBank (DG002)
- Étude mécanistique dédiée reliant spécifiquement la valine (et non la tyrosine) au métabolisme biliaire
- Vérification du statut réglementaire de la valine comme produit thérapeutique (vs. supplément nutritionnel) avant toute évaluation clinique ultérieure

*Note méthodologique : les autres indications prédites pour ce candidat (rangs 2–10, non détaillées ici selon le format) présentent un niveau de preuve encore plus faible (L5) — la plupart des articles associés correspondent en réalité à des coïncidences de nomenclature de mutations génétiques (ex. « Val→X » dans le nom de variants), et non à des preuves pharmacologiques réelles concernant la valine.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

