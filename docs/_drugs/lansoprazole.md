---
layout: default
title: Lansoprazole
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 2
---

# Lansoprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Lansoprazole : De l'Ulcère Peptique au Reflux Duodéno-Gastrique

## Résumé en Une Phrase

Le lansoprazole est un inhibiteur de la pompe à protons (IPP), une classe historiquement utilisée pour l'ulcère peptique, l'infection à *Helicobacter pylori*, le reflux gastro-œsophagien et les lésions gastro-intestinales induites par les AINS. Le modèle TxGNN prédit une association avec le **reflux duodéno-gastrique**, avec un score de prédiction élevé (**99,69%**) mais soutenu uniquement par **2 publications** et **aucun essai clinique dédié** — le niveau de preuve reste très faible.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non documentée dans les licences de ce pack ; classe IPP, historiquement indiquée dans l'ulcère peptique, l'infection à *H. pylori*, le RGO et les lésions liées aux AINS (cf. littérature ci-dessous) |
| Nouvelle Indication Prédite | Reflux Duodéno-Gastrique |
| Score de Prédiction TxGNN | 99,69% |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action (MOA) ne sont pas disponibles dans ce pack. Sur la base des informations connues, le lansoprazole fait partie de la classe des inhibiteurs de la pompe à protons (IPP) et inhibe la sécrétion d'acide gastrique ; son efficacité dans l'ulcère peptique et le RGO est largement établie.

Cependant, le lien mécanistique avec le reflux duodéno-gastrique (RDG) est faible. Le RDG est principalement causé par un reflux biliaire/alcalin, contre lequel l'inhibition acide n'a pas d'action directe. À l'inverse, la littérature disponible suggère même que l'inhibition de l'acide gastrique pourrait modifier l'environnement gastrique et potentiellement favoriser l'effet du contenu reflué sur la muqueuse gastrique (cf. étude animale ci-dessous). Le score élevé de TxGNN (99,69%) relève donc d'une association purement prédictive par le modèle, sans support clinique direct à ce stade.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revue | European Journal of Clinical Pharmacology | Mise à jour sur l'usage clinique des IPP : ulcère peptique, *H. pylori*, RGO, lésions liées aux AINS, syndrome de Zollinger-Ellison — ne traite pas spécifiquement du RDG |
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Étude animale | Gastric Cancer | Chez le rat, le lansoprazole associé à un reflux duodéno-gastrique favoriserait la carcinogenèse gastrique, suggérant un effet potentiellement délétère plutôt que thérapeutique dans ce contexte |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité. *(Donnée bloquante identifiée : le résumé des mises en garde/contre-indications TFDA n'a pas encore été extrait — voir Prochaines Étapes.)*

---

## Indication Candidate Secondaire : Obstruction Duodénale

Le pack contient une seconde prédiction TxGNN, moins prioritaire mais avec davantage d'essais cliniques répertoriés (sans lien direct avec l'indication).

| Élément | Contenu |
|------|------|
| Nouvelle Indication Prédite | Obstruction Duodénale |
| Score de Prédiction TxGNN | 99,68% |
| Niveau de Preuve | L4 |
| Décision Recommandée | Hold |

**Rationnel mécanistique :** L'obstruction duodénale est majoritairement d'origine mécanique/anatomique (par ex. syndrome de l'artère mésentérique supérieure, tumeur, adhérences post-opératoires). Le mécanisme d'inhibition acide du lansoprazole ne permet pas de résoudre l'obstruction elle-même ; au mieux, il s'agirait d'un traitement adjuvant indirect dans le contexte de complications d'ulcère peptique. Le lien est ténu.

**Essais cliniques :**

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00175032](https://clinicaltrials.gov/study/NCT00175032) | Phase 3 | Terminé | 1045 | Lansoprazole 30mg vs naproxène vs célécoxib en prévention d'ulcère gastroduodénal chez patients arthrosiques sous aspirine — preuve de sécurité indirecte, non spécifique à l'obstruction duodénale |
| [NCT00854776](https://clinicaltrials.gov/study/NCT00854776) | Phase NA | Statut inconnu | 300 | IPP en prévention d'ulcère/saignement chez patients cardiaques sous aspirine+clopidogrel — contexte de complications de l'UGD, pas d'obstruction |
| [NCT04188119](https://clinicaltrials.gov/study/NCT04188119) | Phase 2 | Retiré (0 inscrit) | 0 | Avelumab + aspirine dans le cancer du sein triple négatif — sans rapport avec le lansoprazole ou l'obstruction duodénale (appariement erroné) |
| [NCT03794596](https://clinicaltrials.gov/study/NCT03794596) | Phase 2 | Retiré (0 inscrit) | 0 | Version quasi-identique de l'essai ci-dessus, également sans rapport |

**Littérature :**

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [18162841](https://pubmed.ncbi.nlm.nih.gov/18162841/) | 2008 | Rapport de cas | Journal of Pediatric Gastroenterology and Nutrition | Syndrome de l'artère mésentérique supérieure comme cause rare d'intolérance alimentaire chez le nourrisson — décrit une étiologie de l'obstruction duodénale, sans mention du lansoprazole |

---

## Conclusion et Prochaines Étapes

**Décision : Hold** (pour les deux indications candidates — reflux duodéno-gastrique et obstruction duodénale)

**Justification :**
Pour le reflux duodéno-gastrique, le score TxGNN est élevé mais repose sur un niveau de preuve L5 : aucun essai clinique, et la seule étude mécanistique disponible suggère un effet potentiellement délétère plutôt que bénéfique. Pour l'obstruction duodénale, la physiopathologie est essentiellement mécanique et peu compatible avec un mécanisme d'action anti-sécrétoire ; les essais cliniques retrouvés ne concernent pas directement cette indication. Aucune des deux prédictions ne dispose actuellement d'un support clinique suffisant pour avancer.

**Pour avancer, les éléments suivants sont nécessaires :**
- Téléchargement et analyse du RCP/notice TFDA pour les mises en garde et contre-indications (donnée bloquante DG001 — requis avant toute évaluation de sécurité S1)
- Données détaillées sur le mécanisme d'action via l'API DrugBank (DG002)
- Étude clinique contrôlée spécifique au reflux duodéno-gastrique (le RDG est actuellement traité chirurgicalement ou par agents chélateurs de sels biliaires, pas par IPP)
- Clarification de la pertinence clinique réelle de la piste « obstruction duodénale », qui semble mal appariée aux essais disponibles
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

