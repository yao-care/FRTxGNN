---
layout: default
title: Yohimbine
parent: 僅模型預測 (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Yohimbine
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

# Yohimbine : D'une Indication d'Origine Non Documentée vers la Migraine

## Résumé en Une Phrase

L'indication d'origine de la Yohimbine n'est pas documentée dans les données disponibles (aucune AMM ni indication approuvée enregistrée). Le modèle TxGNN prédit que la Yohimbine pourrait être efficace pour la **Migraine** (migraine disorder), avec un score de prédiction de **99.94%**, mais **aucun essai clinique** et seulement des publications indirectes (mécanistiques, précliniques) soutiennent actuellement cette direction — dont plusieurs suggèrent un mécanisme d'action opposé à l'effet thérapeutique recherché.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée (aucune licence ni indication d'origine enregistrée dans les données disponibles) |
| Nouvelle Indication Prédite | Migraine (migraine disorder) |
| Score de Prédiction TxGNN | 99.94% |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données structurées sur le mécanisme d'action (champ MOA officiel) ne sont pas disponibles — c'est d'ailleurs un écart de données de sévérité élevée (DG002, source recommandée : DrugBank API). Cependant, l'analyse mécanistique associée à cette prédiction indique que la Yohimbine est un **antagoniste des récepteurs α2-adrénergiques**, augmentant la libération centrale de noradrénaline.

La littérature rattachée à cette prédiction ne porte pas sur la Yohimbine elle-même, mais sur l'hypothèse sérotoninergique/catécholaminergique de la migraine (notamment via des modèles à la réserpine, qui déplète la sérotonine et les catécholamines). Ces travaux établissent un lien indirect entre systèmes noradrénergique/sérotoninergique et physiopathologie migraineuse, sans jamais tester directement la Yohimbine dans ce contexte.

Point important : plusieurs traitements prophylactiques établis de la migraine (β-bloquants, agonistes α2 comme la clonidine) agissent dans le sens **opposé** à celui de la Yohimbine, qui est un antagoniste α2. Le blocage α2 tend à augmenter le tonus sympathique, ce qui va à l'encontre du mécanisme recherché en prophylaxie migraineuse. Cette prédiction repose donc sur une association topologique du graphe de connaissances plutôt que sur un rationnel mécanistique convergent — d'où la recommandation de prudence.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [5634006](https://pubmed.ncbi.nlm.nih.gov/5634006/) | 1967 | Revue | Trans Am Neurol Assoc | Revue historique du rôle de la sérotonine dans la physiopathologie de la migraine |
| [39842732](https://pubmed.ncbi.nlm.nih.gov/39842732/) | 2025 | Animal | Free Radic Biol Med | Modèle murin d'allodynie périorbitaire induite par la réserpine (fibromyalgie/migraine) ; voie Schwann TRPA1/NOX1 impliquée |
| [468534](https://pubmed.ncbi.nlm.nih.gov/468534/) | 1979 | Cohorte | Headache | Association entre céphalée induite par réserpine et libération de prolactine chez les migraineux |
| [1270244](https://pubmed.ncbi.nlm.nih.gov/1270244/) | 1976 | Cohorte | Headache | Étude de la tyramine et de la sérotonine plasmatique chez les patients migraineux |
| [15829916](https://pubmed.ncbi.nlm.nih.gov/15829916/) | 2005 | Animal | J Cereb Blood Flow Metab | Les agonistes/antagonistes noradrénergiques influencent la propagation de la dépression corticale (mécanisme de l'aura migraineuse) chez le rat |
| [171561](https://pubmed.ncbi.nlm.nih.gov/171561/) | 1975 | pending | MMW | Rôle des médiateurs humoraux (kinines, sérotonine, histamine, tyramine) dans la pathogenèse et le traitement de la migraine |
| [15778266](https://pubmed.ncbi.nlm.nih.gov/15778266/) | 2005 | pending | J Pharmacol Exp Ther | Rôle de la dopamine dans un modèle de nociception trigémino-vasculaire lié à la migraine |
| [5297855](https://pubmed.ncbi.nlm.nih.gov/5297855/) | 1967 | pending | Arch Neurol | Sérotonine plasmatique dans la migraine et le stress |
| [934534](https://pubmed.ncbi.nlm.nih.gov/934534/) | 1976 | pending | Minerva Med | Essai en double aveugle sur la réserpine (300 patients) en prophylaxie de la migraine sévère |
| [13707746](https://pubmed.ncbi.nlm.nih.gov/13707746/) | 1960 | pending | Br Med J | Essai clinique contrôlé de prophylaxie médicamenteuse de la migraine (période pré-moderne, agents non précisés dans le résumé) |

*Note : aucune de ces publications ne teste la Yohimbine directement — elles portent sur des molécules apparentées (réserpine notamment) ou sur la physiopathologie générale de la migraine.*

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Un écart de données bloquant a été identifié : les mises en garde et contre-indications officielles (notice TFDA) ne sont pas disponibles (DG001, sévérité *Blocking*), ce qui empêche à ce stade toute évaluation de sécurité initiale (S1).

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Aucun essai clinique n'évalue la Yohimbine dans la migraine, et la littérature disponible est indirecte (modèles à la réserpine, physiopathologie générale), pas spécifique à la molécule.
- L'analyse mécanistique associée à la prédiction elle-même signale une direction pharmacologique potentiellement opposée à l'effet prophylactique recherché (antagonisme α2 vs agonisme α2/bêta-blocage utilisés en prophylaxie), ce qui pèse contre — et non en faveur — de cette piste.
- La Yohimbine n'est pas commercialisée en France (0 AMM) et l'écart de données sur les mises en garde/contre-indications (DG001) est bloquant pour toute évaluation de sécurité.

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice/mises en garde officielle TFDA (résolution de DG001, bloquant)
- Mécanisme d'action confirmé via DrugBank (résolution de DG002)
- Clarification de l'indication d'origine de la Yohimbine (actuellement non documentée dans les données disponibles)
- Étude préclinique ou clinique testant spécifiquement la Yohimbine (et non des molécules apparentées) dans la migraine
- Revue pharmacologique dédiée pour trancher la contradiction mécanistique identifiée (antagonisme α2) avant toute progression vers une évaluation d'hypothèse
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

