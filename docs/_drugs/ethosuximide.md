---
layout: default
title: Ethosuximide
parent: Prédiction du modèle uniquement (L5)
nav_order: 305
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "ethosuximide"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
description: "Ethosuximide : nouvelle indication prédite, Syndrome néphrogénique d'antidiurèse inappropriée (nephrogenic syndrome of inappropriate antidiuresis) (niveau de preuve L5). Indication d'origine : Non re…"
---

# Ethosuximide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

## Ethosuximide: Syndrome néphrogénique d'antidiurèse inappropriée (nephrogenic syndrome of inappropriate antidiuresis)
{: .text-alpha }

## Résumé en Une Phrase

Ethosuximide est un antiépileptique, initialement utilisé pour le traitement de l'épilepsie-absence.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome néphrogénique d'antidiurèse inappropriée (NSIAD)**, mais **aucun essai clinique** et **aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction purement algorithmique.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Syndrome néphrogénique d'antidiurèse inappropriée (nephrogenic syndrome of inappropriate antidiuresis) |
| Score de Prédiction TxGNN | 0.9991 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : 1 sur 1) |
| Nombre d'AMM | 1 (valides : 1) |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances générales, l'éthosuximide est un bloqueur des canaux calciques de type T (Cav3.x), agissant principalement sur les neurones thalamiques, ce qui explique son efficacité dans l'épilepsie-absence.

Le NSIAD est causé par des mutations gain de fonction du récepteur V2 de la vasopressine (AVPR2, par exemple R137C/R137L). Ces mutations entraînent une activité constitutive du récepteur et une rétention d'eau indépendante de la vasopressine. Les canaux calciques de type T sont exprimés dans le tissu rénal, mais **aucun lien mécanistique établi** n'existe avec la signalisation constitutive du récepteur V2.

Le score très élevé de TxGNN (0.9991) provient du modèle TxGNN (deep learning) et peut refléter des similarités que le modèle a apprises entre maladies apparentées, et non une preuve biologique. Il ne doit **pas** être interprété comme une preuve d'efficacité. De plus, l'hyponatrémie/SIADH a été rapportée comme effet indésirable de certains anticonvulsivants, ce qui soulève un doute sur la plausibilité de la direction de l'effet. La similarité avec l'indication originale reste à évaluer.

---

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 68481191 | ZARONTIN 250 mg/5 ml, sirop (ESSENTIAL PHARMA (M), Malte) | Sirop | Non renseignée (AMM active) |

---

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Contre-indications issues du graphe de connaissances** (associations médicament-maladie, et non texte de la notice) : trouble anxieux, trouble névrotique, trouble dysthymique, maladie rénale, pyo-uretère, maladie hématologique, maladie hépatique, maladie de la vésicule biliaire, lupus érythémateux systémique (y compris pédiatrique), neutropénie, agranulocytose, porphyrie aiguë intermittente.
- **Interactions médicamenteuses** : 92 interactions recensées. Les 20 premières affichées sont toutes de niveau modéré : aprépitant, morphine (y compris liposomale), dronabinol, nabilone, métoclopramide, opium, sibutramine, éthanol, cobicistat, acide folique, déférasirox, prométhazine, lévoleucovorine, leucovorine, fostamatinib, chloroquine, méfloquine, hydroxychloroquine, chlorphéniramine. Les autres interactions n'ont pas été détaillées.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le modèle (niveau L5), sans essai clinique ni publication. Aucun lien mécanistique n'est établi, et la direction de l'effet est douteuse, certains antiépileptiques étant associés à l'hyponatrémie/SIADH.
- Les données de sécurité de la notice sont absentes, ce qui bloque le passage à l'évaluation de sécurité.

<!-- review:begin fr-lic-20261106-ethosuximide-1 -->

> **Correction de vérification (2026-11-06)**: Texte initial : « L'unique AMM française est annulée, et les données de sécurité de la notice sont absentes, ce qui bloque le passage à l'évaluation de sécurité. » Supprimé : l'affirmation selon laquelle les AMM seraient abrogées, annulées ou non valides ne correspondait pas aux données d'AMM (Base de données publique des médicaments (BDPM), au 2026-11-06). Les données (Base de données publique des médicaments (BDPM)) recensent 1 AMM pour ce médicament, dont 1 valides ; les chiffres à jour figurent dans l'aperçu rapide et dans les informations de marché. Source: [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt).

<!-- review:end fr-lic-20261106-ethosuximide-1 -->

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications), lacune bloquante.
- Compléter les données sur le mécanisme d'action (DrugBank).
- Mener une revue de littérature préclinique ciblée sur les canaux calciques de type T et la signalisation du récepteur V2 rénal.
- Évaluer la compatibilité des voies d'administration et la similarité avec l'indication originale.
- Réexaminer la pertinence de la prédiction au vu du risque d'hyponatrémie/SIADH associé à certains antiépileptiques.

<!-- review:begin log -->

## Journal de vérification

Voici le journal de vérification de cette page : affirmations contrôlées à partir des données officielles d'AMM (Base de données publique des médicaments (BDPM)). Les corrections se limitent aux faits de base ; les prédictions du modèle, les niveaux de preuve et les conclusions n'ont pas été réécrits.

| Date de vérification | Élément | Action | Source |
|------|------|------|------|
| 2026-11-06 | Supprimé : « 'unique AMM française est annulée, et l » | Corrigé | [Base de données publique des médicaments (BDPM) – CIS_bdpm](https://base-donnees-publique.medicaments.gouv.fr/index.php/download/file/CIS_bdpm.txt) |

<!-- review:end log -->

## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

