---
layout: default
title: Sunitinib
parent: 僅模型預測 (L5)
nav_order: 293
evidence_level: L5
indication_count: 10
---

# Sunitinib
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

# Sunitinib : Du Cancer du Rein Avancé au Liposarcome

## Résumé en Une Phrase

Le sunitinib (DrugBank DB01268) est un inhibiteur de tyrosine kinase multi-cible utilisé à l'international dans le cancer du rein avancé, les tumeurs stromales gastro-intestinales (GIST) et les tumeurs neuroendocrines pancréatiques.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Liposarcome**,
avec **3 essais cliniques** et **9 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer du rein avancé, GIST, tumeurs neuroendocrines pancréatiques (usages internationaux établis — non commercialisé en France) |
| Nouvelle Indication Prédite | Liposarcome |
| Score de Prédiction TxGNN | 99.87% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans notre base (donnée manquante côté DrugBank). Sur la base des informations pharmacologiques publiques largement établies, le sunitinib est un inhibiteur de tyrosine kinase multi-cible (VEGFR1-3, PDGFRα/β, KIT, FLT3, RET), dont l'efficacité antitumorale repose sur le double blocage de l'angiogenèse tumorale et de la prolifération cellulaire dépendante de PDGFR/KIT.

Le liposarcome est une tumeur des tissus mous fortement dépendante de la néoangiogenèse et, pour certains sous-types, de la signalisation PDGFR. Le paradigme thérapeutique des sarcomes des tissus mous partage d'ailleurs plusieurs cibles moléculaires avec les indications déjà validées du sunitinib (GIST notamment), ce qui rend l'hypothèse de repositionnement mécanistiquement cohérente.

Cette hypothèse est renforcée par des données cliniques réelles : plusieurs essais de phase II ont testé le sunitinib dans les sarcomes des tissus mous en incluant spécifiquement des cohortes de liposarcome, et un cas clinique publié rapporte un bénéfice clinique durable chez un patient lourdement prétraité. La prédiction TxGNN est donc cohérente avec un signal clinique préexistant, bien que non encore confirmé par un essai randomisé dédié au liposarcome.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | Terminé | 48 | Étude ouverte de phase II visant à identifier une dose prometteuse de sunitinib malate chez des patients atteints de sarcome des tissus mous métastatique/non résécable, incluant leiomyosarcome, liposarcome, fibrosarcome et MFH |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Terminé | 131 | Protocole SARC024 sur le régorafénib dans des sous-types de sarcomes sélectionnés ; le sunitinib y est cité comme précédent d'activité clinique dans les sarcomes des tissus mous (médicament testé principal : régorafénib, pas le sunitinib) |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | Terminé | 53 | Étude multicentrique de phase II du sunitinib en administration continue dans les sarcomes non-GIST métastatiques, localement avancés ou récidivants |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Étude clinique (Phase II) | International journal of cancer | Étude de phase II du sunitinib malate dans les sarcomes des tissus mous réfractaires, avec focus sur leiomyosarcome, liposarcome et MFH |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Rapport de cas | Anticancer research | Bénéfice clinique durable du sunitinib malate chez un patient atteint de liposarcome métastatique lourdement prétraité |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Revue | Cancers | Altérations génétiques, épigénétiques et transcriptomiques du liposarcome pour la sélection de thérapies ciblées |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Étude translationnelle | Oncotarget | Séquençage nouvelle génération du chondrosarcome myxoïde extrasquelettique, évaluant les facteurs prédictifs de réponse au sunitinib |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Revue | Expert review of anticancer therapy | Thérapies émergentes pour le sarcome des tissus mous de l'adulte |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Revue | Annals of oncology | Traitement dirigé ou non par l'histologie des sarcomes des tissus mous, incluant les données d'activité du sunitinib |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Revue | Magyar onkologia | Traitement médical des sarcomes des tissus mous selon le sous-type histologique |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Étude de cas / série | The American journal of surgical pathology | Analyse clinicopathologique de 25 cas d'un sarcome myofibroblastique myxoïde inflammatoire distinctif |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Protocole d'essai | BMC cancer | Protocole de l'essai REGOSARC (régorafénib) dans le sarcome des tissus mous avancé, mentionnant le précédent d'activité du sunitinib |

---

## Informations de Marché en France

Le sunitinib n'est actuellement pas commercialisé en France dans ce jeu de données (0 AMM enregistrée, statut « non commercialisé »). Aucune information d'AMM locale n'est donc disponible pour évaluer une extension d'indication.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur de tyrosine kinase multi-cible : VEGFR1-3, PDGFRα/β, KIT, FLT3, RET) |
| Risque de Myélosuppression | Modéré — neutropénie et thrombocytopénie sont des effets indésirables fréquemment rapportés avec les inhibiteurs de tyrosine kinase multi-cibles de cette classe |
| Classification d'Émétogénicité | Faible à modérée (profil typique des TKI oraux) |
| Éléments de Surveillance | NFS complète, fonction hépatique, fonction thyroïdienne, tension artérielle, fonction cardiaque (FEVG) |
| Protection de Manipulation | Thérapie orale ciblée (non cytotoxique classique) ; suivre néanmoins les procédures locales de manipulation des anticancéreux oraux |

*Note : ces éléments reposent sur le profil pharmacologique international connu du sunitinib, les données de sécurité spécifiques TFDA/France étant actuellement manquantes (voir section suivante).*

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- L'hypothèse de repositionnement est mécanistiquement plausible et soutenue par un niveau de preuve L3 (3 essais de phase II complétés incluant des cohortes de liposarcome, 9 publications dont un cas de bénéfice clinique durable), mais aucun essai randomisé n'a spécifiquement validé cette indication.
- Un écart de données **bloquant** (DG001) empêche toute évaluation de sécurité initiale (S1) : les mises en garde et contre-indications de l'étiquetage TFDA sont manquantes, tout comme les données d'interactions médicamenteuses (DDI : « not_found »). Le sunitinib n'étant en outre pas commercialisé en France, une décision « Go » ne peut être prise avant de sécuriser ces éléments.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupération et analyse de la notice TFDA (mises en garde, contre-indications) — remédiation DG001
- Interrogation complète de la base DDI pour le sunitinib
- Données détaillées de mécanisme d'action (MOA) via l'API DrugBank — remédiation DG002
- Évaluation de la stratégie d'entrée sur le marché français (statut actuel : non commercialisé, 0 AMM)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

