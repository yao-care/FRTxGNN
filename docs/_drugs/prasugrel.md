---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel : Du Syndrome Coronarien Aigu à l'Hypertension Pulmonaire

## Résumé en Une Phrase

Prasugrel est un antiagrégant plaquettaire (inhibiteur du récepteur P2Y12, classe thiénopyridine) initialement utilisé en association avec l'aspirine chez les patients sous stent après un syndrome coronarien aigu traité par intervention coronarienne percutanée (ICP). Le modèle TxGNN prédit qu'il pourrait être pertinent pour l'**hypertension pulmonaire**, mais avec seulement **2 essais cliniques** et **2 publications** identifiés, dont aucun n'étudie directement le prasugrel dans cette indication — le lien reste à ce stade une coïncidence de mots-clés plutôt qu'un signal mécanistique solide.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Syndrome coronarien aigu sous ICP — antiagrégation plaquettaire (association avec l'aspirine) |
| Nouvelle Indication Prédite | Hypertension pulmonaire |
| Score de Prédiction TxGNN | 99.88 % |
| Niveau de Preuve | L4 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action (MOA) ne sont actuellement pas disponibles dans le dossier de preuves. Sur la base des informations connues issues de la littérature fournie, le prasugrel appartient à la classe des thiénopyridines et agit comme inhibiteur du récepteur plaquettaire P2Y12 ; son efficacité dans la prévention de la thrombose de stent après un syndrome coronarien aigu est bien établie et documentée (voir PMID 21241206 ci-dessous).

Le lien mécanistique proposé entre l'agrégation plaquettaire et certains sous-types d'hypertension pulmonaire (notamment l'hypertension pulmonaire thromboembolique chronique, où un remodelage vasculaire lié à des phénomènes thrombotiques est décrit) est théoriquement envisageable. Cependant, aucun des essais cliniques ni des publications recueillis pour cette prédiction ne porte réellement sur l'utilisation du prasugrel — ou même d'un antiagrégant plaquettaire — dans le traitement de l'hypertension pulmonaire.

En pratique, les deux essais identifiés concernent respectivement la gestion des anticoagulants oraux (NOAC, une classe pharmacologique différente) chez des patients âgés en fibrillation atriale, et l'éligibilité de patients atteints de thrombose associée au cancer à un essai de référence (CARAVAGGIO). Les deux publications concernent l'effet des traitements de fond sur la mortalité liée à la COVID-19 et l'adhésion au clopidogrel après ICP. Aucune ne traite de l'hypertension pulmonaire. Cette prédiction doit donc être considérée comme un rapprochement de proximité dans le graphe de connaissances (co-occurrence de concepts), et non comme un signal clinique ou mécanistique direct.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Terminé | 500 | Étude observationnelle transversale décrivant l'usage des anticoagulants oraux (NOAC) chez des patients âgés en fibrillation atriale non valvulaire — sans lien avec l'hypertension pulmonaire ni le mécanisme du prasugrel (chevauchement de mots-clés uniquement, pertinence jugée faible). |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Terminé | 300 | Étude rétrospective évaluant la proportion de patients atteints de thrombose associée au cancer non éligibles à l'essai CARAVAGGIO — sans rapport direct avec l'hypertension pulmonaire ou le prasugrel. |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohorte | Curr Med Res Opin | Étude des facteurs associés à l'adhésion au clopidogrel après ICP chez des patients avec syndrome coronarien aigu ; confirme l'usage standard du prasugrel comme alternative dans cette indication, mais n'étudie pas l'hypertension pulmonaire. |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohorte (registre ACTIV) | Kardiologiia | Analyse de l'effet des traitements de fond des comorbidités avant infection sur la mortalité liée à la COVID-19 — ne concerne pas l'hypertension pulmonaire ni un mécanisme antiplaquettaire spécifique. |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Aucun essai clinique ni publication ne porte réellement sur le prasugrel dans l'hypertension pulmonaire — les preuves collectées sont des correspondances de mots-clés sans rapport direct, et le lien mécanistique proposé reste spéculatif. De plus, l'évaluation de sécurité initiale (étape S1) ne peut pas être engagée : la notice TFDA (avertissements/contre-indications) n'a pas pu être obtenue, ce qui constitue un blocage. Le prasugrel n'étant par ailleurs pas commercialisé en France (0 AMM), il n'existe aucune base réglementaire locale immédiate pour ce repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice TFDA (avertissements et contre-indications) — actuellement bloquant pour toute évaluation de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (MOA) via l'API DrugBank
- Identifier des études cliniques ou précliniques portant spécifiquement sur le prasugrel (ou une classe d'antiagrégants P2Y12) dans l'hypertension pulmonaire, en particulier son sous-type thromboembolique chronique (CTEPH)
- À titre secondaire : la piste « migraine avec foramen ovale perméable » (rang 2, niveau de preuve L3, statut « Research Question ») présente un signal légèrement plus construit — effet de classe des thiénopyridines (clopidogrel) et de la ticagrelor rapporté dans de petites études pilotes — mais reste elle aussi sans étude spécifique au prasugrel ; elle pourrait justifier un suivi de veille bibliographique distinct.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

