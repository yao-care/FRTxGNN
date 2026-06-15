---
layout: default
title: Ataluren
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 6
---

# Ataluren
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ataluren : De la Dystrophie Musculaire de Duchenne à la Cholestase Intrahépatique Bénigne Récurrente

## Résumé en Une Phrase

Ataluren (PTC124) est un agent de lecture à travers les codons stop prématurés (*PTC readthrough*), développé dans le cadre de la dystrophie musculaire de Duchenne à mutation nonsense (nmDMD), avec une sécurité établie par des essais cliniques de grande envergure. Le modèle TxGNN prédit qu'il pourrait être efficace pour la **cholestase intrahépatique bénigne récurrente (BRIC)** ainsi que pour 3 autres maladies hépatiques héréditaires liées à des mutations nonsense, avec un mécanisme d'action directement applicable. Ce dossier multi-indications est soutenu par **1 essai clinique de Phase 2** (terminé) et **1 étude in vitro** publiée dans *Hepatology*.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Dystrophie Musculaire de Duchenne à mutation nonsense (nmDMD) |
| Principale Indication Prédite (Rang 1) | Cholestase Intrahépatique Bénigne Récurrente (BRIC) |
| Score de Prédiction TxGNN | 99,42% |
| Niveau de Preuve | L5 (BRIC) — L4 (PFIC2) — L3 (maladies du métabolisme bilirubine) |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Research Question (4 indications) / Hold (2 indications) |

---

## Vue d'Ensemble Multi-Indications

| Rang | Maladie | Score TxGNN | Preuve | Mécanisme PTC | Décision |
|---|---|---|---|---|---|
| 1 | Cholestase intrahépatique bénigne récurrente (BRIC) | 99,42% | L5 | ✓ Plausible (*ATP8B1/ABCB11*) | Research Question |
| 2 | Maladie congénitale du métabolisme de la bilirubine | 99,40% | L3 | ✓ Plausible (CN syndrome / *UGT1A1*) | Research Question |
| 3 | Cirrhose héréditaire amérindienne de l'enfant (NAIC) | 99,33% | L5 | ❌ Incompatible (mutation splicing) | Hold |
| 4 | Cholestase intrahépatique familiale (PFIC2) | 99,26% | L4 | ✓ Confirmé in vitro (*ABCB11*) | Research Question |
| 5 | Rétinopathie diabétique non proliférative sévère | 99,24% | L5 | ❌ Incompatible (maladie multifactorielle) | Hold |
| 6 | Maladie du métabolisme de la bilirubine | 99,11% | L3 | ✓ Plausible (CN syndrome / *UGT1A1*) | Research Question |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Ataluren agit au niveau ribosomal : il permet aux ribosomes de lire à travers un codon stop prématuré (PTC — *premature termination codon*) résultant d'une mutation nonsense, rétablissant ainsi la synthèse d'une protéine fonctionnelle de pleine longueur. Ce mécanisme est par nature **indépendant du gène cible** : il ne corrige pas la séquence d'ADN mais restaure la traduction. Sa validité a été démontrée dans les essais DMD sur le gène *DMD*, et le principe est transposable à toute maladie monogénique causée par une mutation nonsense, sous réserve que celle-ci soit effectivement présente dans la population considérée.

Les maladies hépatiques prédites par TxGNN aux rangs 1, 2, 4 et 6 appartiennent toutes au spectre des cholestases héréditaires ou des troubles du métabolisme de la bilirubine, causés par des mutations dans les gènes *ATP8B1* ou *ABCB11* (transporteurs canaliculaires biliaires) ou *UGT1A1* (enzyme de conjugaison de la bilirubine dans le syndrome de Crigler-Najjar). Pour la **PFIC2** (*ABCB11* nonsense mutations), une étude in vitro publiée en 2021 dans *Hepatology* (PMID 32702170) a directement confirmé la capacité d'ataluren à induire la lecture à travers 6 mutations nonsense spécifiques, avec restauration partielle de l'expression de BSEP — il s'agit de la connexion mécanistique la plus robuste de ce dossier.

Deux indications sont mécanistiquement incompatibles : la cirrhose NAIC (mutation fondatrice *CIRH1A* c.1434+5G>A de type splicing — ataluren n'agit pas sur les variants d'épissage) et la rétinopathie diabétique non proliférative (pathologie vasculaire multifactorielle acquise sans mutation nonsense causale). Ces deux prédictions reflètent vraisemblablement une proximité topologique dans le réseau de maladies TxGNN plutôt qu'une vraie applicabilité pharmacologique.

---

## Preuves d'Essais Cliniques

*(Indications rangs 2 et 6 — maladies métaboliques héréditaires à mutation nonsense)*

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT01141075](https://clinicaltrials.gov/study/NCT01141075) | Phase 2 | Terminé | 11 | Ataluren pour l'acidémie méthylmalonique (MMA) à mutation nonsense du gène *MCM*. Essai terminé prématurément (n=11), efficacité non établie. Fournit une preuve de concept pour l'utilisation d'ataluren dans les maladies métaboliques héréditaires à PTC, mais la maladie cible ne correspond pas directement aux troubles biliaires prédits. Pertinence : grade C (contexte IEM, voie pathologique distincte). |

---

## Preuves de la Littérature

*(Indication rang 4 — Cholestase intrahépatique familiale / PFIC2)*

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [32702170](https://pubmed.ncbi.nlm.nih.gov/32702170/) | 2021 | In vitro / Préclinique | Hepatology | Étude directe du readthrough pharmacologique de 6 mutations nonsense d'*ABCB11* (p.Y354X, p.R415X, p.R470X, p.R1057X, p.R1090X, p.E1302X) dans la PFIC2. Ataluren a induit une restauration partielle de l'expression de BSEP au niveau cellulaire. Preuve in vitro la plus directement pertinente de ce dossier, ciblant exactement le gène et le mécanisme impliqués dans la PFIC2. |

---

## Considérations de Sécurité

Les données de sécurité spécifiques au marché français (mises en garde, contre-indications, interactions médicamenteuses) ne sont pas disponibles dans ce dossier.

> Veuillez consulter la notice pour les informations de sécurité. Le profil de tolérance d'ataluren est documenté dans le cadre des essais cliniques nmDMD (Translarna®, approbation conditionnelle EMA). Une revue de l'EPAR EMA (Translarna®) est recommandée avant toute analyse de repositionnement approfondie.

---

## Conclusion et Prochaines Étapes

**Décision :**
- **Research Question** — Rangs 1, 2, 4, 6 (mécanisme PTC compatible)
- **Hold** — Rangs 3 et 5 (mécanisme incompatible, ne pas poursuivre)

**Justification :**
La connexion mécanistique PTC readthrough → gènes *ATP8B1*, *ABCB11*, *UGT1A1* est biologiquement cohérente et directement soutenue par une étude in vitro publiée (PFIC2). La priorité de recherche la plus élevée revient à la **PFIC2 (rang 4)** en raison de la preuve in vitro directe, et au **syndrome de Crigler-Najjar de type I** (sous-jacent aux rangs 2 et 6) en raison de la sévérité de la maladie et de l'existence d'un précédent orphan drug. La BRIC (rang 1) reste une piste valide mais nécessite d'abord une caractérisation moléculaire de la prévalence des PTC dans la population BRIC.

**Pour avancer, les éléments suivants sont nécessaires :**

- **Caractérisation moléculaire** : Confirmer la prévalence des mutations nonsense (PTC) dans chaque population cible — BRIC (*ATP8B1/ABCB11*), PFIC2 (*ABCB11*), Crigler-Najjar (*UGT1A1*) — variable clé pour la faisabilité clinique
- **Revue du profil de sécurité EMA** : Consulter l'EPAR Translarna® pour les mises en garde complètes, contre-indications et interactions médicamenteuses
- **Données MOA détaillées** : Compléter les données DrugBank (DB05016) sur le mécanisme d'action
- **Modèles précliniques in vivo** : Valider l'efficacité in vivo dans des modèles murins de cholestase héréditaire (modèles *Atp8b1* et *Abcb11* knock-in nonsense)
- **Consultation maladies rares** : Engager des centres de référence (filière FILFOIE) pour identifier les cohortes de patients porteurs de mutations nonsense éligibles
- **Évaluation statut orphelin** : Explorer l'extension de la désignation orpheline existante (nmDMD) à la PFIC2 et au syndrome de Crigler-Najjar de type I auprès de l'EMA/ANSM
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

