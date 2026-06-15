---
layout: default
title: Dimercaprol
parent: 僅模型預測 (L5)
nav_order: 105
evidence_level: L5
indication_count: 1
---

# Dimercaprol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Dimercaprol : De l'Intoxication aux Métaux Lourds à la Bronchite

## Résumé en Une Phrase

Dimercaprol (BAL — British Anti-Lewisite) est un agent chélateur des métaux lourds, utilisé pour traiter les intoxications à l'arsenic, au mercure et au plomb.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Bronchite**, avec un score de **99,54%**.
Cependant, les preuves directes sont très limitées : **aucun essai clinique** ne teste Dimercaprol dans cette indication, et seulement **1 publication sur 3** établit un lien mécanistique direct — un rapport de cas de bronchite chimique par inhalation de vapeurs de mercure.

---

## Aperçu Rapide

| Élément | Contenu |
|---|---|
| Indication Originale | Intoxication aux métaux lourds (arsenic, mercure, plomb) |
| Nouvelle Indication Prédite | Bronchite |
| Score de Prédiction TxGNN | 99,54% |
| Niveau de Preuve | L4 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Dimercaprol est un agent chélateur dont le mécanisme repose sur la formation de complexes stables avec les ions de métaux lourds (arsenic, mercure, plomb). En se liant à ces métaux, il empêche leur interaction avec les groupements thiol des protéines cellulaires, permettant ainsi leur élimination rénale. Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans la base de données actuelle ; la description ci-dessus est fondée sur les propriétés pharmacologiques connues de la classe des chélateurs dithiol.

Le lien entre l'indication originale et la bronchite est mécanistiquement cohérent mais **extrêmement étroit** : l'inhalation de vapeurs de mercure peut déclencher une bronchite chimique aiguë. Dans ce contexte précis, Dimercaprol pourrait théoriquement interrompre la toxicité en chélatant les ions mercuriques au niveau des voies respiratoires. Ce lien est documenté par un unique rapport de cas historique datant de 1963 (PMID 14068440).

Cette connexion ne s'applique qu'à la **bronchite d'origine mercurielle aiguë** — une entité clinique rare — et non aux formes communes de bronchite (infectieuse, allergique, tabagique, post-virale). Le score TxGNN élevé reflète très probablement un raisonnement par voie indirecte dans le graphe de connaissances : toxicité mercurielle → lésion pulmonaire → bronchite, sans support clinique direct pour une application thérapeutique générale.

---

## Preuves d'Essais Cliniques

> ⚠️ **Aucun essai clinique ne teste Dimercaprol dans la bronchite.** Les essais identifiés ci-dessous concernent des pathologies bronchiques au sens large mais impliquent d'autres médicaments. Leur pertinence directe pour cette prédiction est de grade C (faible).

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---|---|---|---|---|
| [NCT00423137](https://clinicaltrials.gov/study/NCT00423137) | Phase 2 | Terminé | 48 | BIBW 2948 BS vs placebo chez des patients BPCO avec bronchite chronique — évalue les réserves de mucine épithéliale et l'efficacité clinique ; aucun lien avec Dimercaprol |
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Phase 4 | Terminé | 30 | Montélukast pour ralentir la progression du rejet chronique (bronchiolite oblitérante) post-transplantation pulmonaire — médicament testé non applicable |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Phase 2 | Terminé | 25 | Montélukast pour la bronchiolite oblitérante après greffe de cellules souches hématopoïétiques — médicament testé non applicable |
| [NCT01287078](https://clinicaltrials.gov/study/NCT01287078) | Phase 2 | Terminé | 25 | Ciclosporine inhalée pour la bronchiolite oblitérante post-transplantation — médicament testé non applicable |
| [NCT01212406](https://clinicaltrials.gov/study/NCT01212406) | Phase 4 | Terminé | 100 | Vitamine D pour prévenir la bronchiolite oblitérante après transplantation pulmonaire — médicament testé non applicable |
| [NCT02006576](https://clinicaltrials.gov/study/NCT02006576) | Phase 2 | Terminé | 118 | Ibuprofène pour inhiber la production de prostaglandine E dans les voies respiratoires inférieures (étude PIE) — médicament testé non applicable |
| [NCT02669251](https://clinicaltrials.gov/study/NCT02669251) | Phase 1/2 | Actif, sans recrutement | 14 | Alvelestat (inhibiteur de l'élastase neutrophilique) pour la bronchiolite oblitérante post-greffe de cellules souches — médicament testé non applicable |
| [NCT01334892](https://clinicaltrials.gov/study/NCT01334892) | Phase 2/3 | Terminé (arrêté prématurément) | 130 | Ciclosporine liposomale aérosolisée pour la prévention de la bronchiolite oblitérante — essai arrêté, médicament testé non applicable |
| [NCT02631720](https://clinicaltrials.gov/study/NCT02631720) | N/A | Terminé | 884 | Étude observationnelle prospective multicentrique sur les facteurs de risque de dysfonction chronique de l'allogreffe pulmonaire (CLAD) — non interventionnel |
| [NCT00774449](https://clinicaltrials.gov/study/NCT00774449) | N/A | Inconnu | 261 | Caractérisation de la bronchiolite oblitérante post-transplantation pulmonaire — étude observationnelle longitudinale, non interventionnel |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|---|---|---|---|---|
| [14068440](https://pubmed.ncbi.nlm.nih.gov/14068440/) | 1963 | Rapport de cas | Am Rev Respir Dis | **Seul lien direct** : deux cas de bronchite chimique aiguë consécutive à l'inhalation de vapeurs de mercure — documente la voie mécanistique mercure→lésion bronchique qui fonde la prédiction TxGNN |
| [3048217](https://pubmed.ncbi.nlm.nih.gov/3048217/) | 1988 | Série de cas / Revue | Ann Surg | 11 cas sur 30 de bronchiolite oblitérante immunologique après transplantation cardiopulmonaire — pathogenèse immuno-médiée, sans lien avec Dimercaprol |
| [2261963](https://pubmed.ncbi.nlm.nih.gov/2261963/) | 1990 | Observationnelle / Cohorte | Eur Respir J | Réduction du tabagisme associée à une diminution de l'inflammation des voies respiratoires inférieures chez 15 fumeurs — sans lien avec Dimercaprol |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Le seul lien mécanistique plausible concerne la bronchite d'origine mercurielle aiguë, une indication clinique très étroite et rare qui ne correspond pas à la définition générale de « bronchite » ciblée par la prédiction TxGNN. Aucun essai clinique ne teste Dimercaprol dans cette indication, les données de sécurité sont indisponibles, et le médicament n'est pas commercialisé en France (0 AMM), ce qui représente un obstacle réglementaire majeur.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer les données complètes de mécanisme d'action (MOA) via DrugBank (DG002)
- Récupérer les mises en garde, contre-indications et interactions médicamenteuses (DG001)
- Redéfinir le périmètre clinique cible : restreindre à la **« bronchite chimique aiguë par intoxication au mercure »** plutôt qu'à la bronchite en général
- Recherche ciblée sur les cas publiés de bronchite mercurielle traités par chélation (BAL ou DMSA)
- Évaluer si une indication orpheline ou urgence toxicologique justifie une demande d'AMM en France
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

