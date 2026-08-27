---
layout: default
title: Ropinirole
parent: 僅模型預測 (L5)
nav_order: 268
evidence_level: L5
indication_count: 10
---

# Ropinirole
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

# Ropinirole : De la Maladie de Parkinson au Trouble Deficit de l'Attention avec Hyperactivite

## Résumé en Une Phrase

Ropinirole est un agoniste dopaminergique (D2/D3), utilisé à l'origine dans la maladie de Parkinson et le syndrome des jambes sans repos (SJSR).
Le modèle TxGNN prédit qu'il pourrait présenter un intérêt pour le **Trouble Déficit de l'Attention avec Hyperactivité (TDAH)**,
mais cette direction n'est actuellement soutenue que par **8 publications indirectes** (comorbidité SJSR-TDAH, un cas clinique pédiatrique), **sans aucun essai clinique enregistré**.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Maladie de Parkinson / Syndrome des jambes sans repos (donnée réglementaire française non disponible dans le jeu de données) |
| Nouvelle Indication Prédite | Trouble Déficit de l'Attention avec Hyperactivité (TDAH) |
| Score de Prédiction TxGNN | 99.99% |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce jeu de données (donnée manquante confirmée, sévérité élevée). Sur la base des informations connues issues de la littérature associée, le ropinirole est un agoniste des récepteurs dopaminergiques D2/D3, dont l'efficacité dans la maladie de Parkinson et le syndrome des jambes sans repos est bien établie ; mécanistiquement, une action sur la voie dopaminergique pourrait théoriquement être pertinente pour le TDAH, dont l'hypothèse physiopathologique dominante implique un déficit fonctionnel dopaminergique dans le circuit préfronto-strié.

Le lien mis en avant par les preuves disponibles n'est cependant pas une démonstration d'efficacité directe sur les symptômes du TDAH, mais repose principalement sur la **comorbidité fréquente entre SJSR et TDAH** (PMID 16218085, PMID 18656214) et sur un **cas clinique isolé** d'un enfant de 6 ans dont les symptômes de TDAH se sont améliorés de façon indirecte après traitement par ropinirole visant son SJSR associé (PMID 15866437).

Un point de prudence mécanistique important doit être souligné : les traitements standards du TDAH (méthylphénidate, amphétamines) agissent en **inhibant la recapture** ou en **stimulant la libération** de dopamine, un mode d'action pharmacologiquement distinct de l'**agonisme direct des récepteurs D2/D3** exercé par le ropinirole. Cette différence de mécanisme rend l'extrapolation d'efficacité incertaine, et aucune des publications disponibles n'étudie directement l'effet du ropinirole sur les symptômes centraux du TDAH en dehors du contexte du SJSR.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [16218085](https://pubmed.ncbi.nlm.nih.gov/16218085/) | 2005 | Revue | Sleep | Revue de l'association entre syndrome des jambes sans repos (SJSR) et TDAH, et intérêt potentiel d'un traitement pharmacologique commun |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Revue | Revue neurologique | Revue générale du SJSR, incluant sa relation avec le TDAH |
| [15866437](https://pubmed.ncbi.nlm.nih.gov/15866437/) | 2005 | Rapport de cas | Pediatric Neurology | Enfant de 6 ans avec TDAH et SJSR : le ropinirole a amélioré significativement à la fois les symptômes de TDAH et les troubles du sommeil liés au SJSR |
| [30950895](https://pubmed.ncbi.nlm.nih.gov/30950895/) | 2019 | Rapport de cas (sécurité) | Cornea | Œdème cornéen développé et résolu chez 3 patients exposés à des agonistes dopaminergiques systémiques |
| [24992083](https://pubmed.ncbi.nlm.nih.gov/24992083/) | 2014 | Cohorte (molécule différente, effet de classe) | Clinical Neuropharmacology | Essai comparatif de 11 semaines : effets du piribédil vs pramipexole/ropinirole sur la vigilance chez des patients parkinsoniens somnolents |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Pharmacologie moléculaire préclinique | Pharmacological Research | Hétéromérisation des récepteurs α2A-adrénergiques et D4 dopaminergiques, impliquée dans les troubles du contrôle des impulsions dont le TDAH |
| [17483695](https://pubmed.ncbi.nlm.nih.gov/17483695/) | 2007 | Préclinique (modèle animal) | J Neuropathol Exp Neurol | Modèle murin de SJSR par lésion A11 et carence en fer, augmentant l'activité locomotrice |
| [30460371](https://pubmed.ncbi.nlm.nih.gov/30460371/) | 2019 | Rapport de cas (sécurité) | Acta Dermato-Venereologica | Délire d'infestation induit par traitement, associé à une élévation des niveaux de dopamine cérébrale |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. *(Les mises en garde, contre-indications et interactions médicamenteuses officielles n'ont pas pu être récupérées à ce jour — voir Prochaines Étapes.)*

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'indication TDAH n'est actuellement soutenue par aucun essai clinique direct ni aucune littérature ciblant spécifiquement l'effet du ropinirole sur les symptômes centraux du TDAH ; les preuves disponibles reposent sur une comorbidité (SJSR-TDAH) et un unique cas pédiatrique, ce qui correspond à un niveau de preuve L4 (mécanisme/observation isolée).
- Les données réglementaires de sécurité (mises en garde et contre-indications) sont totalement absentes du dossier, ce qui **bloque l'entrée en évaluation de sécurité initiale (S1)** selon le processus interne.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération de la notice officielle (ANSM/TFDA) : mises en garde, contre-indications, interactions médicamenteuses — élément bloquant prioritaire.
- Données détaillées sur le mécanisme d'action (MOA) via DrugBank pour consolider l'analyse mécanistique.
- Recherche d'essais cliniques dédiés évaluant le ropinirole spécifiquement dans le TDAH (hors contexte SJSR).
- Évaluation du risque psychiatrique (impulsivité, symptômes psychotiques) déjà documenté avec les agonistes dopaminergiques, particulièrement pertinent avant toute extrapolation à une population pédiatrique TDAH.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

