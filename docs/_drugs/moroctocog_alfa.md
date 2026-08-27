---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 8
---

# Moroctocog Alfa
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

# Moroctocog Alfa : De l'Hémophilie A au Trouble Primaire de Libération des Plaquettes

## Résumé en Une Phrase

Moroctocog alfa est un facteur VIII de coagulation recombinant (délété du domaine B), utilisé pour le traitement de l'hémophilie A (déficit en facteur VIII) — cette indication d'origine n'est toutefois pas confirmée par un dossier réglementaire français dans ce pack de données. Le modèle TxGNN prédit une efficacité potentielle pour le **trouble primaire de libération des plaquettes** (score 99,97 %), mais cette direction repose sur **7 essais cliniques**, dont aucun ne cible directement cette pathologie (tous notés pertinence « C »), et **aucune publication** ne la soutient à ce jour.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hémophilie A (déduite du contexte des essais/rationnel ; non confirmée par un dossier réglementaire français) |
| Nouvelle Indication Prédite | Trouble primaire de libération des plaquettes |
| Score de Prédiction TxGNN | 99,97 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action (MOA) ne sont pas disponibles dans ce pack (donnée manquante DrugBank de sévérité « High »). Sur la base des informations contextuelles disponibles dans les essais et le rationnel de repositionnement, moroctocog alfa est un facteur VIII recombinant délété du domaine B, dont l'efficacité dans le traitement de l'hémophilie A (remplacement du facteur VIII) est bien établie.

Le lien mécanistique avec le trouble primaire de libération des plaquettes est cependant faible. Ce trouble résulte d'une anomalie de l'activation/sécrétion des granules plaquettaires (dense granule/alpha granule), un mécanisme distinct de la cascade de coagulation dépendante du facteur VIII. Selon le rationnel fourni : « moroctocog alfa compensant le FVIII n'a pas de correspondance physiopathologique directe pour ce type de maladie, et ne pourrait éventuellement contribuer à l'hémostase qu'en cas de déficit concomitant en facteurs de coagulation. »

Cette prédiction TxGNN doit donc être interprétée avec prudence : le score élevé du modèle ne s'accompagne pas d'un support mécanistique ou clinique direct, et plusieurs essais cliniques associés semblent être des liaisons de données imparfaites (essais sur l'hémophilie A plutôt que sur le trouble plaquettaire ciblé).

---

## Preuves d'Essais Cliniques

*Note : les 7 essais ci-dessous sont tous notés pertinence « C » (faible correspondance) — ils portent majoritairement sur l'hémophilie A ou sur des contextes de coagulation non spécifiques au trouble primaire de libération des plaquettes, possiblement en raison d'une liaison de données imparfaite dans le modèle TxGNN.*

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | Terminé | 159 | Efficacité et sécurité de BIVV001 (rFVIIIFc-VWF-XTEN) en prophylaxie et traitement des épisodes hémorragiques, hémophilie A sévère (≥12 ans) — sans lien direct avec le trouble ciblé |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | Terminé | 74 | Sécurité et pharmacocinétique de BIVV001 chez enfants <12 ans avec hémophilie A sévère |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | Terminé | 30 | Efficacité et sécurité du FVIII pégylé (BAX855) lors de procédures chirurgicales, hémophilie A sévère |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | Pas encore en recrutement | 80 | Profils hématologiques et de coagulation dans la leucémie myéloïde aiguë sous chimiothérapie d'induction — étude observationnelle, non interventionnelle |
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | En recrutement | 200 | Évaluation clinique et biologique du syndrome post-vaccination COVID-19 — sans lien direct avec le trouble ciblé |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | En recrutement | 25 | Système de support hépatique artificiel (DPMAS+TPE), effet sur la coagulation primaire en insuffisance hépatique aiguë sur chronique |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | En recrutement | 45 | Exploration de l'hémostase systémique et portale chez patients sous shunt portosystémique intrahépatique transjugulaire (TIPS) |

---

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le niveau de preuve (L4) repose uniquement sur des essais cliniques dont la pertinence mécanistique est jugée faible (grade C) et sans aucune publication scientifique à l'appui. Le rationnel de repositionnement lui-même indique une correspondance physiopathologique limitée entre le mécanisme du facteur VIII et le trouble primaire de libération des plaquettes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Mises en garde et contre-indications TFDA (donnée bloquante — nécessaire avant toute évaluation de sécurité S1)
- Données détaillées sur le mécanisme d'action (MOA) via DrugBank
- Clarification de l'indication d'origine réglementaire (aucune AMM française enregistrée dans ce pack)
- Vérification de la validité des liaisons essais-maladie du modèle TxGNN pour cette indication (risque d'erreur d'association)
- Étude préclinique ou mécanistique dédiée avant toute reconsidération de cette piste

**À noter :** parmi les 8 indications prédites pour ce médicament, le rang 4 (« déficit acquis en facteur de coagulation ») présente un niveau de preuve nettement supérieur (L3, stade S2 « Research Question », 13 essais et 4 publications, dont plusieurs directement pertinents pour le déficit acquis en FVIII) et pourrait justifier une évaluation prioritaire distincte.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

