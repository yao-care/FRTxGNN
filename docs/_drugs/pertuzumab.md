---
layout: default
title: Pertuzumab
parent: Prédiction du modèle uniquement (L5)
nav_order: 593
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
monitor_inn: "PERTUZUMAB"
predicted_indications: ["ectomesenchymoma", "malignant cutaneous granular cell skin tumor", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma"]
description: "Pertuzumab : nouvelle indication prédite, Ectomesenchymoma (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Pertuzumab
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

## Pertuzumab: Ectomesenchymoma
{: .text-alpha }

## Résumé en Une Phrase

Pertuzumab est un anticorps monoclonal anti-HER2, initialement utilisé pour le traitement du cancer du sein HER2 positif.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **cancer du sein positif aux récepteurs de la progestérone**, avec **1 essai clinique** et **20 publications** soutenant actuellement cette direction.
Il s'agit toutefois en pratique d'un sous-groupe de l'indication HER2 positive déjà établie (maladie HR+/HER2+), plutôt que d'un repositionnement au sens strict.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Ectomesenchymoma |
| Score de Prédiction TxGNN | 0.9971 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 3 sur 3) |
| Nombre d'AMM | 3 (valides : 3) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne figurent pas dans les données compilées pour ce rapport. D'après les informations connues, le pertuzumab se lie au domaine de dimérisation extracellulaire de HER2 (sous-domaine II) et bloque l'hétérodimérisation HER2-HER3. Cela inhibe les voies de signalisation PI3K/AKT et MAPK.

Les tumeurs positives aux récepteurs de la progestérone qui co-expriment HER2 (maladie HR+/HER2+) sont pilotées par cette même voie. La nouvelle indication prédite correspond donc à un sous-ensemble du cancer du sein HER2 positif. La signalisation endocrinienne coexistante est une voie de résistance connue. L'essai WSG TP-II soutient l'association pertuzumab + trastuzumab + hormonothérapie dans ce sous-groupe.

Garde-fou : le bénéfice est limité à la maladie HER2 positive. Les tumeurs PR positives/HER2 négatives ne doivent pas être traitées par pertuzumab.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Terminé | 517 | Essai d'équivalence randomisé en double aveugle comparant un biosimilaire du pertuzumab (QL1209) au pertuzumab de référence, avec trastuzumab et docétaxel, en néoadjuvant dans le cancer du sein HER2 positif, ER/PR négatif. Les résultats stratifiés selon le statut hormonal ne sont pas rapportés. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | ECR (Phase 2) | Lancet Oncol | NeoSphere : analyse à 5 ans de la survie sans progression, de la survie sans maladie et de la sécurité du pertuzumab + trastuzumab en néoadjuvant |
| [42150145](https://pubmed.ncbi.nlm.nih.gov/42150145/) | 2026 | ECR | J Clin Oncol | WSG TP-II : analyse de survie, trastuzumab + pertuzumab + hormonothérapie vs chimiothérapie en néoadjuvant (HR+/HER2+) |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | ECR | JAMA Oncol | WSG TP-II : hormonothérapie + double blocage HER2 vs chimiothérapie désescaladée dans le cancer du sein précoce HR+/HER2+ |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | ECR (Phase 2) | Ann Oncol | WSG-ADAPT HER2+/HR- : stratégies de désescalade avec double blocage trastuzumab + pertuzumab ± paclitaxel hebdomadaire |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | ECR | Br J Cancer | Essai d'équivalence de phase 3 du biosimilaire QL1209 vs pertuzumab de référence (HER2+, ER/PR négatif) |
| [41401771](https://pubmed.ncbi.nlm.nih.gov/41401771/) | 2026 | ECR | ESMO Open | Essai d'équivalence de phase 3 du biosimilaire TQB2440 vs pertuzumab de référence |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Recommandation | J Clin Oncol | Mise à jour des recommandations ASCO sur le traitement systémique du cancer du sein avancé HER2 positif |
| [41387082](https://pubmed.ncbi.nlm.nih.gov/41387082/) | 2026 | Cohorte | Breast | Suppression ovarienne et inhibiteurs de l'aromatase chez les patientes préménopausées HR+/HER2+ |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Revue | Cancer Treat Rev | Cancer du sein HR+/HER2+ : état des connaissances et perspectives |
| [40983817](https://pubmed.ncbi.nlm.nih.gov/40983817/) | 2025 | Revue | Breast Cancer | Voies de signalisation intrinsèques et traduction clinique du cancer du sein HR+/HER2+ |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60912227 | PERJETA 420 mg, solution à diluer pour perfusion | Solution à diluer pour perfusion | Non renseignée (AMM active) |
| 63806777 | PHESGO 600 mg/600 mg, solution injectable | Solution injectable | Non renseignée (AMM active) |
| 67178992 | PHESGO 1200 mg/600 mg, solution injectable | Solution injectable | Non renseignée (AMM active) |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (anticorps monoclonal anti-HER2) |
| Risque de Myélosuppression | Non documenté dans les données compilées. Le risque hématologique provient surtout des chimiothérapies associées (par exemple docétaxel). |
| Classification d'Émétogénicité | Faible (anticorps monoclonal) ; à évaluer selon la chimiothérapie associée |
| Éléments de Surveillance | Fonction cardiaque (FEVG), NFS, fonction hépatique et rénale |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice |

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : une interaction de niveau modéré est signalée avec l'idélalisib. Une interaction pharmacologique est également répertoriée avec la cible ERBB2 (HER2), conforme au mécanisme d'action de l'anticorps.

Pour les mises en garde et contre-indications, veuillez consulter la notice.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Plusieurs essais randomisés (dont un essai de phase 3 terminé et l'essai WSG TP-II) soutiennent le double blocage HER2 incluant le pertuzumab. Il s'agit d'un sous-groupe de l'indication HER2 positive déjà reconnue, et non d'une indication réellement nouvelle.

**Pour avancer, les éléments suivants sont nécessaires :**
- Confirmation du statut HER2 positif avant toute utilisation (exclure les tumeurs PR positives/HER2 négatives).
- Données de mécanisme d'action issues de DrugBank.
- Mises en garde et contre-indications issues de la notice ANSM (non disponibles actuellement, point bloquant pour l'évaluation de sécurité).
- Clarification du statut réglementaire en France : les 3 AMM sont annulées et leurs indications ne sont pas renseignées.
- Résultats stratifiés par statut des récepteurs hormonaux pour les essais de biosimilaires.
- Surveillance cardiaque et plan de sécurité pour les populations particulières.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

