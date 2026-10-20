---
layout: default
title: Bexarotene
parent: Prédiction du modèle uniquement (L5)
nav_order: 104
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Bexarotene : nouvelle indication prédite, Syndrome de Sézary (niveau de preuve L5). Indication d'origine : Lymphome cutané à cellules T primitif"
monitor_inn: "bexarotene"
predicted_indications: ["primary cutaneous B-cell lymphoma", "Sezary syndrome", "lymphosarcoma"]
---

# Bexarotene
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

# Bexarotène : Du Lymphome T Cutané Primitif au Syndrome de Sézary

## Résumé en Une Phrase

Le bexarotène est un rétinoïde de synthèse administré par voie orale, initialement utilisé pour le traitement du lymphome cutané à cellules T primitif.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **syndrome de Sézary** (variante leucémique du lymphome cutané à cellules T), avec **6 essais cliniques** et **19 publications** soutenant actuellement cette direction.

Remarque : la prédiction classée en premier par TxGNN est le lymphome cutané primitif à cellules B (score de 99,44 %), mais elle ne repose sur aucun essai clinique ni donnée spécifique au bexarotène (niveau de preuve L5, décision Hold). Ce rapport retient le syndrome de Sézary, indication la mieux documentée parmi les prédictions, et mentionne les deux autres en conclusion.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Lymphome cutané à cellules T primitif (selon le graphe de connaissances ; le texte d'indication des AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Syndrome de Sézary |
| Score de Prédiction TxGNN | 99,29 % |
| Niveau de Preuve | L1 (essai de phase 3 randomisé NCT00056056 ; **arrêté prématurément**, ce qui limite la solidité de ce niveau) |
| Statut de Marché en France | ✗ Annulé uniquement (aucune AMM valide) |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les connaissances pharmacologiques établies, le bexarotène est un agoniste sélectif des récepteurs X des rétinoïdes (RXR). Ces récepteurs sont des facteurs de transcription activés par un ligand, qui contrôlent la croissance, l'apoptose et la différenciation cellulaires. Dans le lymphome cutané à cellules T, le bexarotène favorise l'apoptose et la différenciation des lymphocytes T malins.

Le syndrome de Sézary est la forme leucémique du lymphome cutané à cellules T, au même titre que le mycosis fongoïde. Il s'inscrit donc dans le même spectre que l'indication originale. Il s'agit plutôt d'un usage dans l'indication ou très proche de celle-ci que d'un véritable repositionnement.

Une étude mécanistique (PMID 17546636) rapporte en outre que le bexarotène atténue la chimiotaxie des cellules T malines dans le syndrome de Sézary, en réduisant les lymphocytes exprimant le récepteur de chimiokine CCR4.

---

## Preuves d'Essais Cliniques

Les essais ci-dessous concernent le lymphome cutané à cellules T, population dont relève le syndrome de Sézary.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00056056](https://clinicaltrials.gov/study/NCT00056056) | Phase 3 | Arrêté | 93 | Bexarotène + PUVA versus PUVA seul dans le mycosis fongoïde (essai randomisé ouvert) ; résultats limités par l'arrêt précoce |
| [NCT00306969](https://clinicaltrials.gov/study/NCT00306969) | Phase 1/2 | Terminé | 18 | Bexarotène oral + photophérèse : sécurité, tolérance et réponse clinique dans le lymphome cutané à cellules T |
| [NCT00030589](https://clinicaltrials.gov/study/NCT00030589) | Phase 2 | Inconnu | Non renseignée | Bexarotène + PUVA à doses randomisées dans le lymphome cutané à cellules T de stade IB-IIA |
| [NCT01134341](https://clinicaltrials.gov/study/NCT01134341) | Phase 1 | Terminé | 34 | Pralatrexate + bexarotène systémique dans le lymphome cutané à cellules T en rechute ou réfractaire ; recherche de dose et sécurité |
| [NCT00660231](https://clinicaltrials.gov/study/NCT00660231) | Phase 2 | Terminé | 36 | Gemcitabine + bexarotène (Gembex) dans le lymphome cutané à cellules T progressif ou réfractaire |
| [NCT00255801](https://clinicaltrials.gov/study/NCT00255801) | Phase 2 | Terminé | 37 | Doxorubicine liposomale suivie de bexarotène dans le lymphome cutané à cellules T avancé (le bexarotène n'est pas le médicament principal de l'étude) |
| [NCT00178841](https://clinicaltrials.gov/study/NCT00178841) | Phase 2 | Terminé | 4 | Pilote rosiglitazone + bexarotène ; effectif trop faible pour conclure |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [25678803](https://pubmed.ncbi.nlm.nih.gov/25678803/) | 2015 | Revue | OncoTargets and Therapy | Place du bexarotène dans le mycosis fongoïde et le syndrome de Sézary |
| [19222457](https://pubmed.ncbi.nlm.nih.gov/19222457/) | 2009 | Revue | Br J Dermatol | Bexarotène (Targretin), rétinoïde de synthèse autorisé dans le lymphome cutané à cellules T réfractaire avancé |
| [40072489](https://pubmed.ncbi.nlm.nih.gov/40072489/) | 2025 | Revue | J Cutan Med Surg | Efficacité et sécurité des traitements oraux du mycosis fongoïde et du syndrome de Sézary |
| [33415447](https://pubmed.ncbi.nlm.nih.gov/33415447/) | 2021 | Revue | Curr Treat Options Oncol | Mise à jour des traitements du mycosis fongoïde et du syndrome de Sézary |
| [29572582](https://pubmed.ncbi.nlm.nih.gov/29572582/) | 2018 | Revue | Curr Oncol Rep | Options systémiques dans les formes avancées de mycosis fongoïde et de syndrome de Sézary |
| [17546636](https://pubmed.ncbi.nlm.nih.gov/17546636/) | 2007 | Étude mécanistique | Am J Hematol | Le bexarotène atténue la chimiotaxie des cellules T malignes dans le syndrome de Sézary (réduction des lymphocytes CCR4+) |
| [16634713](https://pubmed.ncbi.nlm.nih.gov/16634713/) | 2006 | Revue | Expert Opin Pharmacother | Bexarotène dans le traitement du lymphome cutané à cellules T |
| [19696197](https://pubmed.ncbi.nlm.nih.gov/19696197/) | 2009 | Revue | Blood | Prise en charge par stade du mycosis fongoïde et du syndrome de Sézary |
| [30213403](https://pubmed.ncbi.nlm.nih.gov/30213403/) | 2018 | Revue | Best Pract Res Clin Haematol | Intégration des nouveaux traitements systémiques, dont le bexarotène, chez les patients avec formes avancées |
| [27151889](https://pubmed.ncbi.nlm.nih.gov/27151889/) | 2016 | Revue | Blood | Prise en charge du mycosis fongoïde et du syndrome de Sézary ; absence d'essais randomisés robustes |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 65407392 | BEXAROTENE CIPLA 75 mg, capsule molle (annulée) | Capsule molle | Non renseignée |
| 69197468 | TARGRETIN 75 mg, capsule molle (annulée) | Capsule molle | Non renseignée |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (rexinoïde, agoniste des RXR) |
| Risque de Myélosuppression | Faible à moyen ; la leucopénie figure parmi les contre-indications relevées dans le graphe de connaissances |
| Classification d'Émétogénicité | Faible |
| Éléments de Surveillance | Bilan lipidique (triglycérides, cholestérol), fonction thyroïdienne (hypothyroïdie centrale), NFS, fonction hépatique, glycémie |
| Protection de Manipulation | Veuillez consulter les mises en garde et précautions de la notice (tératogène : contraception indispensable chez les femmes en âge de procréer) |

---

## Considérations de Sécurité

- **Contre-indications relevées dans le graphe de connaissances** (et non dans le texte de la notice) : insuffisance hépatique, maladie du foie, pancréatite, maladie de la vésicule biliaire, maladie des voies biliaires, ictère obstructif, hypothyroïdie (dont myxœdème et hypothyroïdie congénitale), diabète sucré, acidocétose diabétique, abus ou dépendance à des substances, leucopénie.
- **Interactions médicamenteuses** : 495 interactions sont recensées. Parmi celles listées :
  - **Majeures** : albiglutide, alogliptine, dulaglutide, eluxadoline, exénatide.
  - **Modérées** : hydrocortisone, triamcinolone, dexaméthasone, bétaméthasone, acétohexamide, chlorpropamide, cisapride, éliglustat, glimépiride, glipizide, glibenclamide, granisétron.
  - **Mineures** : aprépitant, clarithromycine, clotrimazole.
  - Les analyses disponibles signalent aussi le gemfibrozil et les modulateurs du CYP3A4 comme à examiner en priorité.
- **Points de vigilance cliniques** : hyperlipidémie, hypothyroïdie centrale (documentée, PMID 30903705) et tératogénicité.

Les mises en garde et contre-indications issues de la notice française n'ont pas pu être obtenues. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Le syndrome de Sézary relève du même spectre que l'indication originale. Il est soutenu par un essai de phase 3 randomisé (arrêté prématurément), plusieurs essais de phase 2 et de nombreuses revues décrivant le bexarotène comme option systémique établie. La preuve est donc réelle mais fragilisée par l'arrêt de l'essai de phase 3 et par l'absence de mécanisme documenté dans les données compilées.

**Autres prédictions du modèle (non retenues) :**
- **Lymphome cutané primitif à cellules B** (score 99,44 %) : niveau L5, décision Hold. Aucun essai, aucune publication démontrant une activité du bexarotène dans les lymphomes B ; le score élevé reflète probablement la proximité des maladies dans le graphe.
- **Lymphosarcome** (score 99,12 %) : niveau L2, question de recherche. Terme obsolète et non spécifique ; les essais concernent exclusivement le lymphome cutané à cellules T. À résoudre en sous-types précis avant toute recommandation.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (blocage actuel pour le criblage de sécurité).
- Les données détaillées sur le mécanisme d'action (DrugBank).
- La clarification du statut réglementaire en France : les deux AMM sont annulées, la disponibilité du produit doit donc être vérifiée.
- Un plan de surveillance des lipides, de la thyroïde et de la contraception, ainsi qu'une revue des interactions (gemfibrozil, inhibiteurs et inducteurs du CYP3A4, antidiabétiques).
- L'analyse des résultats de l'essai NCT00056056 et des motifs de son arrêt.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

