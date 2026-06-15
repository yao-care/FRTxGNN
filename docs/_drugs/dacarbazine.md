---
layout: default
title: Dacarbazine
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 1
---

# Dacarbazine
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

# Dacarbazine : Du Mélanome aux Néoplasmes des Voies Aérodigestives Supérieures

## Résumé en Une Phrase

Dacarbazine (DTIC) est un agent alkylant de classe triazène, classiquement utilisé en première ligne pour le mélanome malin avancé et la maladie de Hodgkin réfractaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour les **Néoplasmes des Voies Aérodigestives Supérieures**, avec **1 essai clinique** indirect et **20 publications** documentant actuellement cette direction de recherche.
La majorité des données disponibles concernent toutefois son analogue pharmacologique temozolomide (TMZ) plutôt que dacarbazine directement, ce qui constitue la principale limite du dossier de preuve actuel.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Mélanome malin avancé |
| Nouvelle Indication Prédite | Néoplasmes des Voies Aérodigestives Supérieures |
| Score de Prédiction TxGNN | 99.26% |
| Niveau de Preuve | L3 |
| Statut de Marché en France | ✗ Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Dacarbazine (DTIC) est un promédicament activé par voie hépatique en son métabolite actif MTIC (5-(3-methyltriazen-1-yl)imidazole-4-carboxamide). Ce métabolite méthyle les résidus guanine de l'ADN aux positions O6 et N7, induisant des mésappariements que le système de réparation MMR (*Mismatch Repair*) ne peut pas corriger, aboutissant à l'apoptose cellulaire. Ce mécanisme d'alkylation est identique à celui du temozolomide (TMZ), lequel produit le même métabolite actif MTIC par décomposition spontanée à pH physiologique — les deux molécules sont donc pharmacologiquement équivalentes sur le plan mécanistique.

Les voies aérodigestives supérieures regroupent plusieurs sous-types tumoraux présentant une sensibilité théorique aux alkylants : les paragangliomes malins, le carcinome médullaire de la thyroïde (CMT), l'esthésioneuroblastome et l'angiosarcome de la tête et du cou. Pour ces tumeurs rares à nature neuroendocrine ou mésenchymateuse, le schéma CVD (cyclophosphamide + vincristine + dacarbazine) a été utilisé en pratique clinique, et des données directes existent pour dacarbazine dans le CMT avancé. En revanche, pour le carcinome épidermoïde de la tête et du cou (HNSCC) — sous-type de loin le plus fréquent — dacarbazine n'est pas un traitement standard et les preuves directes restent absentes.

La prédiction TxGNN est donc mécanistiquement cohérente pour les sous-types sensibles aux alkylants, et elle est renforcée par l'analogie pharmacologique solide avec TMZ, dont l'activité dans les cancers aérodigestifs à méthylation MGMT a été formellement étudiée en Phase 2. La transposabilité des résultats TMZ à dacarbazine comme entité thérapeutique distincte reste cependant à confirmer par des essais cliniques directs.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00423150](https://clinicaltrials.gov/study/NCT00423150) | Phase 2 | Terminé (arrêt anticipé) | 86 | Temozolomide (analogue pharmacologique de dacarbazine, même métabolite MTIC) dans les cancers aérodigestifs avancés sélectionnés pour la méthylation du promoteur MGMT — essai interrompu avant atteinte complète des objectifs d'inscription ; résultats publiés sous PMID 23443801 |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [23443801](https://pubmed.ncbi.nlm.nih.gov/23443801/) | 2013 | Essai de Phase 2 | Mol Cancer Ther | Résultats publiés de NCT00423150 : TMZ (analogue de dacarbazine) chez des patients MGMT-méthylés atteints de cancers aérodigestifs avancés — taux de réponse limité ; la méthylation MGMT seule ne suffit pas à prédire l'efficacité dans ces tumeurs |
| [41481311](https://pubmed.ncbi.nlm.nih.gov/41481311/) | 2026 | ECR Phase 3 | JAMA Oncol | Toripalimab vs dacarbazine en première ligne pour le mélanome acral avancé (n = non précisé) — confirme dacarbazine comme standard de référence actif en mono-chimiothérapie ; fournit la base pharmacologique pour les extrapolations d'indication |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | Série de cas | Ann Oncol | Dacarbazine + 5-fluorouracile dans le carcinome médullaire de la thyroïde (CMT) avancé — activité partielle documentée dans ce sous-type neuroendocrine des voies aérodigestives supérieures ; seule donnée d'usage direct de dacarbazine dans la zone anatomique cible |
| [8346929](https://pubmed.ncbi.nlm.nih.gov/8346929/) | 1993 | Revue clinique | Gan To Kagaku Ryoho | Schéma CYVADIC (cyclophosphamide + vincristine + doxorubicine + dacarbazine) pour l'angiosarcome maligne de la tête et du cou — usage de dacarbazine documenté en pratique dans une tumeur mésenchymateuse des voies aérodigestives |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | Série rétrospective | Ear Nose Throat J | 6 patients atteints de paragangliomes malins de la tête et du cou — caractérisation clinicopathologique et analyse des mutations génétiques ; contexte thérapeutique pertinent pour l'indication prédite, sous-type considéré sensible aux alkylants |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | Revue | Clin Oncol | Carcinome médullaire de la thyroïde : revue de la prise en charge actuelle incluant les options de chimiothérapie cytotoxique — fournit le contexte thérapeutique positionnel pour dacarbazine dans ce sous-type des voies aérodigestives |
| [11163509](https://pubmed.ncbi.nlm.nih.gov/11163509/) | 2001 | Série de cas / Revue | Int J Radiat Oncol | Esthésioneuroblastome (tumeur neuroendocrine nasale) : évaluation de l'efficacité de la radiothérapie — sous-type anatomiquement inclus dans les voies aérodigestives supérieures, présentant une sensibilité théorique aux alkylants |
| [3153227](https://pubmed.ncbi.nlm.nih.gov/3153227/) | 1986 | Cas clinique | Pediatr Hematol Oncol | Neuroblastome olfactif pédiatrique avec extension intracrânienne traité par chimiothérapie combinée incluant cyclophosphamide — illustre la stratégie alkylante dans les tumeurs neuroendocrines des voies aérodigestives supérieures |
| [12113649](https://pubmed.ncbi.nlm.nih.gov/12113649/) | 2002 | Revue | Am J Clin Dermatol | Prise en charge complète du mélanome : rôle établi de dacarbazine en mono-chimiothérapie de référence — ancre pharmacologique pour l'extrapolation vers d'autres tumeurs sensibles aux alkylants |
| [34705104](https://pubmed.ncbi.nlm.nih.gov/34705104/) | 2022 | Revue systématique / Épidémiologie | J Cancer Res Clin Oncol | Charge mondiale des cancers associés à l'EBV incluant le carcinome nasopharyngé — contexte épidémiologique pour les néoplasmes des voies aérodigestives supérieures à étiologie virale |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel — Agent alkylant de classe Triazène (promédicament activé en MTIC par voie hépatique) |
| Risque de Myélosuppression | Modéré à élevé — leucopénie et thrombocytopénie fréquentes ; nadir typiquement observé entre J21 et J28 après administration |
| Classification d'Émétogénicité | Élevée — dacarbazine IV figure parmi les agents les plus émétisants ; prophylaxie antiémétique de niveau élevé (antagonistes 5-HT3 + corticoïdes ± aprépitant) obligatoire |
| Éléments de Surveillance | NFS avec formule leucocytaire (avant chaque cure), transaminases et bilirubine (hépatotoxicité dose-dépendante), créatinine et clairance rénale, bilan pré-cure systématique |
| Protection de Manipulation | Oui — manipulation impérativement selon les procédures réglementaires des médicaments cytotoxiques : hotte à flux laminaire, équipements de protection individuelle, procédures de déversement et de destruction sécurisée |

---

## Considérations de Sécurité

Les données structurées de mises en garde, contre-indications et interactions médicamenteuses ne sont pas disponibles dans le dossier actuel (données manquantes en attente d'extraction de la notice officielle ANSM/TFDA). Veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Les preuves directes de dacarbazine dans les néoplasmes des voies aérodigestives supérieures se limitent à des séries rétrospectives de petite taille portant sur des sous-types rares (CMT, paragangliomes malins, angiosarcomes) ; le seul essai clinique prospectif identifié (NCT00423150) a été arrêté prématurément et testait l'analogue TMZ — non dacarbazine lui-même. L'absence d'AMM en France, le manque de données de sécurité structurées et l'hétérogénéité des sous-types tumoraux inclus dans la catégorie « voies aérodigestives supérieures » imposent une phase de consolidation des preuves avant toute démarche réglementaire ou clinique formelle.

**Pour avancer, les éléments suivants sont nécessaires :**
- Extraction des mises en garde, contre-indications et données de toxicité depuis la notice officielle ANSM ou TFDA
- Données de mécanisme d'action (MOA) détaillées issues de DrugBank (DrugBank ID : DB00851)
- Stratification des sous-types tumoraux cibles : séparer les tumeurs neuroendocrines rares (CMT, paragangliome, esthésioneuroblastome) des HNSCC, dont la sensibilité à dacarbazine est hautement improbable
- Recherche bibliographique ciblée sur dacarbazine/DTIC direct — en excluant les études TMZ — dans les tumeurs neuroendocrines aérodigestives
- Évaluation de la faisabilité d'un essai clinique de Phase 2 dans les sous-types rares neuroendocrines de la tête et du cou, avec critère de sélection MGMT et/ou MMR
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

