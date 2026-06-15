---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib : De la Leucémie Myéloïde Chronique à l'Ewing Sarcoma

## Résumé en Une Phrase

Dasatinib (Sprycel®) est un inhibiteur oral multi-cible de tyrosine kinases, reconnu mondialement comme traitement de référence de la leucémie myéloïde chronique (LMC) et de la leucémie aiguë lymphoblastique à chromosome Philadelphie positif (LAL Ph+).
Le modèle TxGNN prédit qu'il pourrait être efficace pour l'**Ewing Sarcoma**, avec **3 essais cliniques** et **7 publications** soutenant actuellement cette direction.
La plausibilité repose sur l'inhibition de l'axe Src/FAK, dont la dépendance dans l'invasion et la métastase de l'Ewing sarcoma est établie précliniquement, mais l'activité clinique en monothérapie reste insuffisamment prouvée.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie myéloïde chronique (LMC) — usage mondial établi ; aucune AMM enregistrée dans la base consultée |
| Nouvelle Indication Prédite | Ewing Sarcoma |
| Score de Prédiction TxGNN | 99.90% |
| Niveau de Preuve | L2 |
| Statut de Marché | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données formelles sur le mécanisme d'action ne sont pas disponibles dans la base consultée. Sur la base des informations connues, Dasatinib est un inhibiteur oral de multiples tyrosine kinases, incluant BCR-ABL, les kinases de la famille Src (Src, Yes, Fyn, Lck), c-KIT et PDGFR-α/β. Son efficacité établie dans la LMC repose sur l'inhibition puissante de la fusion oncogénique BCR-ABL, 325 fois plus active qu'imatinib in vitro. Ce profil d'inhibition élargi est précisément ce qui justifie d'explorer son activité dans des tumeurs solides.

L'Ewing Sarcoma est une tumeur osseuse et des tissus mous hautement agressive, principalement diagnostiquée chez les adolescents et jeunes adultes, avec un pronostic sévère en cas de maladie métastatique ou récidivante. Des études de mécanisme ont démontré que la kinase Src joue un rôle clé dans l'invasion et la progression métastatique des cellules d'Ewing sarcoma : sous stress microenvironnemental (hypoxie, privation de nutriments), le complexe FAK-Src active la formation d'invadopodes et stimule la migration cellulaire. La protéine matricielle ténascine C amplifie ce signal, créant une boucle pro-métastatique Src-dépendante.

Plusieurs études in vitro confirment l'activité antiproliférative et antimigrante de dasatinib dans les lignées cellulaires d'Ewing sarcoma, via l'inhibition de c-KIT et PDGFR en plus de Src. Cependant, un signal clinique important doit être noté : l'essai pédiatrique spécifique (NCT00788125, Phase 1/2, dasatinib + ICE) a été terminé prématurément après seulement 7 patients, ce qui suggère des difficultés de recrutement, des problèmes de sécurité, ou une activité insuffisante en combinaison. L'essai de Phase 2 NCT00464620 (n=366, sarcomes avancés toutes sous-types) représente la meilleure source de données cliniques disponibles, bien que les résultats spécifiques au sous-groupe Ewing sarcoma nécessitent une analyse séparée.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Terminé | 366 | Taux de réponse et survie sans progression à 6 mois dans les sarcomes avancés multi-sous-types (potentiellement incluant l'Ewing sarcoma) — meilleure source de données cliniques disponible |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminé prématurément | 7 | Dasatinib associé à ICE (ifosfamide, carboplatine, étoposide) dans les sarcomes pédiatriques dont l'Ewing sarcoma — arrêt prématuré, signal de prudence |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | En recrutement | 41 | Cellules CAR-T anti-B7-H3 dans les tumeurs solides réfractaires pédiatriques incluant l'Ewing sarcoma — dasatinib non traitement principal, rôle de sensibilisateur CAR-T possible |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Étude in vitro | Cancer Research | Dasatinib inhibe la migration et l'invasion de multiples lignées de sarcomes humains ; apoptose induite dans les sarcomes osseux dépendants de Src — fondement préclinique clé |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Étude in vitro | Oncology Reports | Activité antiproliférative et antimigrante de dasatinib dans les lignées de neuroblastome et d'Ewing sarcoma ; implication de c-KIT et PDGFR dans la prolifération et la survie cellulaire |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Mécanisme | Neoplasia | Le stress microenvironnemental active Src de manière dépendante, induisant la formation d'invadopodes et la migration cellulaire dans l'Ewing sarcoma — justification biologique de la cible |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Mécanisme | Neoplasia | La ténascine C et Src coopèrent pour promouvoir la formation d'invadopodes dans l'Ewing sarcoma via des facteurs microenvironnementaux — renforcement de la pertinence de l'axe Src |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Étude de mécanisme | Sarcoma | Ciblage du complexe FAK-Src dans DSRCT, Ewing sarcoma et rhabdomyosarcome ; dasatinib en monothérapie insuffisant dans ces sous-types — signal négatif, combinaisons nécessaires |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Revue | Oncology Letters | Revue du rôle de Src dans la prolifération, l'apoptose, l'invasion et les métastases sarcomateuses ; analyse de Src comme cible thérapeutique potentielle dans les sarcomes |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | Étude in vitro | Cell Communication and Signaling | Le blocage de CXCR4 active la signalisation des tyrosine kinases dans l'Ewing sarcoma — contexte de l'activation RTK comme voie de résistance ou co-cible |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase de 2ème génération — classe BCR-ABL/Src/c-KIT/PDGFR) |
| Risque de Myélosuppression | Modéré (neutropénie, thrombopénie et anémie fréquemment rapportées en contexte LMC ; profil possiblement différent dans les sarcomes — données insuffisantes) |
| Classification d'Émétogénicité | Faible à modérée (administration orale, comprimés) |
| Éléments de Surveillance | NFS avec différentielle, bilan hépatique (ASAT/ALAT), fonction rénale, électrolytes, surveillance de l'épanchement pleural (effet indésirable caractéristique de dasatinib) |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques en vigueur |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Des données précliniques mécanistiquement cohérentes (inhibition Src/FAK validée dans l'Ewing sarcoma) et un essai de Phase 2 complété dans les sarcomes avancés (n=366) fournissent une base suffisante pour envisager une exploration clinique structurée, mais l'arrêt prématuré de l'essai pédiatrique spécifique (n=7) et l'absence de données d'efficacité en monothérapie imposent une approche encadrée, préférablement en combinaison thérapeutique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtention et analyse des données de sous-groupe Ewing sarcoma dans l'essai NCT00464620 (Phase 2, n=366)
- Clarification des raisons d'arrêt de l'essai NCT00788125 (toxicité, recrutement ou décision administrative)
- Données détaillées sur le mécanisme d'action (MOA) — consultation DrugBank API (référence DG002)
- Évaluation des combinaisons thérapeutiques : dasatinib associé au protocole standard Ewing (VDC/IE — vincristine, doxorubicine, cyclophosphamide / ifosfamide, étoposide)
- Confirmation des voies d'administration disponibles et compatibilité posologique en population pédiatrique et jeunes adultes
- Plan de surveillance de sécurité spécifique incluant la gestion de l'épanchement pleural et la myélosuppression
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

