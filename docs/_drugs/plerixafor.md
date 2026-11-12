---
layout: default
title: Plerixafor
parent: Prédiction du modèle uniquement (L5)
nav_order: 614
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-12
monitor_inn: "plerixafor"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "bronchitis", "vulvar melanoma (disease)", "myeloid leukemia"]
description: "Plerixafor : nouvelle indication prédite, CMM7 (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Plerixafor
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **6** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Rapport d'évaluation pharmaceutique

</div>

## Plerixafor: CMM7
{: .text-alpha }

## Résumé en Une Phrase

Le plerixafor est un antagoniste du récepteur CXCR4, utilisé comme mobilisateur de cellules souches hématopoïétiques.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **myélome plasmocytaire indolent**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette prédiction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | CMM7 |
| Score de Prédiction TxGNN | 0.9934 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 7 sur 7) |
| Nombre d'AMM | 7 (valides : 7) |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Le plerixafor bloque la liaison de CXCL12 au récepteur CXCR4. Cette liaison ancre normalement les cellules souches hématopoïétiques, et les cellules de myélome, dans le microenvironnement de la moelle osseuse. En la perturbant, le médicament favorise la sortie de ces cellules de leur niche protectrice. Les données compilées confirment que CXCR4 est la cible principale du plerixafor, avec ACKR3 comme cible secondaire. Elles ne contiennent pas de description détaillée du mécanisme d'action issue de DrugBank.

Le médicament est déjà utilisé pour mobiliser les cellules souches chez les patients atteints de myélome multiple en vue d'une autogreffe. Le lien avec la biologie du myélome est donc plausible. Le myélome indolent est un stade précoce de la même maladie, ce qui rend l'extension de l'indication théoriquement cohérente.

Ce lien repose cependant uniquement sur la prédiction du modèle. Aucun essai clinique ni aucune publication n'a été retrouvé pour le sous-type indolent. Cette prédiction doit donc être considérée comme une hypothèse.

## Informations de Marché en France

Le texte d'indication approuvée n'est pas renseigné dans les données compilées. Les 5 premières sont listées ci-dessous.

<!-- review:begin fr-lic-20261106-plerixafor-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « Les 7 AMM associées au plerixafor (solution injectable) sont annulées. Le texte d'indication approuvée n'est pas renseigné dans les données compilées. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 7 AMM pour ce médicament, dont 7 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-plerixafor-1 -->

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire | Statut |
|---------|------|------|------|------|
| 64981594 | PLERIXAFOR VIATRIS 20 mg/mL | Solution injectable | VIATRIS SANTE | Active |
| 60626514 | PLERIXAFOR ACCORD 20 mg/ml | Solution injectable | ACCORD HEALTHCARE (Espagne) | Active |
| 69530271 | PLERIXAFOR TILLOMED 20 mg/mL | Solution injectable | TILLOMED PHARMA (Allemagne) | Active |
| 69389575 | PLERIXAFOR ARROW 20 mg/mL | Solution injectable | EUGIA PHARMA (Malte) | Active |
| 65998504 | PLERIXAFOR TEVA 20 mg/mL | Solution injectable | TEVA SANTE | Active |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (relations médicament-maladie, et non texte de notice) : thrombopénie, insuffisance rénale, leucémie.
- **Cibles pharmacologiques** : CXCR4 et ACKR3. Aucune interaction médicamenteuse cliniquement caractérisée n'est disponible dans les données compilées.

Veuillez consulter la notice pour les mises en garde et contre-indications officielles.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction pour le myélome plasmocytaire indolent n'est soutenue par aucun essai clinique ni aucune publication (niveau L5).
- À titre d'information, une autre indication prédite pour ce médicament, la leucémie myéloïde, dispose de nombreux essais de phase 1 et 1/2 en chimiosensibilisation. Elle fait l'objet d'une évaluation distincte.

**Pour avancer, les éléments suivants sont nécessaires :**
- Une recherche ciblée d'études précliniques ou cliniques sur le plerixafor dans le myélome indolent ou smoldering.
- Les données de mécanisme d'action détaillées (DrugBank).
- Les mises en garde et contre-indications officielles de la notice ANSM.
- La clarification du statut réglementaire actuel du plerixafor en France et de la disponibilité du produit.

<!-- review:begin fr-lic-20261106-plerixafor-2 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « La clarification du statut réglementaire actuel du plerixafor en France (AMM annulées) et de la disponibilité du produit. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 7 AMM pour ce médicament, dont 7 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-plerixafor-2 -->

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « Les 7 AMM associées au plerixafor (solution injectable) sont annulées » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |
| 2026-11-06 | Supprimé : « (AMM annulées) » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

