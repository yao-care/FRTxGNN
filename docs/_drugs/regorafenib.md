---
layout: default
title: Regorafenib
parent: Prédiction du modèle uniquement (L5)
nav_order: 657
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Regorafenib : nouvelle indication prédite, Liposarcome (niveau de preuve L5). Indication d'origine : Métastases d'une tumeur maligne du côlon"
---

# Regorafenib
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **8** 
{: .fs-6 .fw-300 }

---

## Table des matières
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Regorafenib : Du Cancer Colorectal Métastatique au Liposarcome

## Résumé en Une Phrase

Regorafenib (STIVARGA) est un inhibiteur multikinase initialement utilisé dans le cancer colorectal métastatique, le carcinome hépatocellulaire et les tumeurs stromales gastro-intestinales (GIST).
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **liposarcome**, avec **1 essai clinique** et **9 publications** disponibles. Cependant, l'essai randomisé spécifique au liposarcome **ne soutient pas** l'usage en routine de regorafenib dans cette population.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Métastases d'une tumeur maligne du côlon (indications issues du graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Prédite | Liposarcome |
| Score de Prédiction TxGNN | 99,76 % |
| Niveau de Preuve | L1 (selon l'évaluation compilée ; voir réserve ci-dessous) |
| Statut de Marché en France | Uniquement annulée |
| Nombre d'AMM | 1 |
| Décision Recommandée | Proceed with Guardrails (avec réserves importantes, voir Conclusion) |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Regorafenib est un inhibiteur multikinase oral qui cible les récepteurs angiogéniques (VEGFR1-3, TIE2), stromaux (PDGFR, FGFR) et oncogéniques (KIT, RET, RAF). Ces voies favorisent l'angiogenèse et la prolifération tumorale, y compris dans les sarcomes des tissus mous. Les données détaillées sur le mécanisme d'action ne figurent pas dans la fiche du médicament, mais ces informations proviennent de la littérature compilée.

Le lien avec l'indication d'origine est plausible : regorafenib est déjà utilisé dans une tumeur mésenchymateuse (GIST), et d'autres inhibiteurs multikinases (pazopanib, sunitinib, sorafenib) ont montré une activité dans certains sarcomes des tissus mous.

**Point essentiel :** les preuves dépendent du sous-type histologique. L'essai de phase 2 REGOSARC a montré un bénéfice sur la survie sans progression dans les sarcomes non adipocytaires, mais **pas dans le liposarcome**. La cohorte liposarcome de SARC024 (essai randomisé en double aveugle contre placebo) conclut que ses résultats « ne soutiennent pas l'usage en routine de regorafenib » dans cette population. Le score TxGNN très élevé n'est donc pas confirmé par les données cliniques.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Terminé | 131 | SARC024 : protocole de type « panier » évaluant regorafenib oral dans des sous-types de sarcome sélectionnés, dont le liposarcome. Signal d'efficacité spécifique au liposarcome limité. |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | ECR | The Oncologist | Cohorte liposarcome de SARC024 (phase 2, contre placebo) : les résultats ne soutiennent pas l'usage en routine de regorafenib. |
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | ECR | The Lancet Oncology | REGOSARC (phase 2, placebo) : efficacité et sécurité de regorafenib dans les sarcomes des tissus mous après anthracycline. |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | ECR | European Journal of Cancer | Analyse actualisée de REGOSARC : bénéfice dans les sarcomes non adipocytaires, mais pas dans le liposarcome. |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | Cohorte | Cancer | Analyse Q-TWiST de REGOSARC : amélioration de la survie sans progression dans le sarcome non adipocytaire. |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Revue | Targeted Oncology | Rôle croissant de regorafenib dans les sarcomes, selon le sous-type. |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Revue | Critical Reviews in Oncology/Hematology | Traitement d'entretien après première ligne dans le sarcome des tissus mous avancé. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Protocole d'étude | BMC Cancer | Protocole de l'essai REGOSARC. |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Étude rétrospective | Anti-Cancer Drugs | Anlotinib dans le liposarcome bien/dédifférencié (autre médicament, contexte indirect). |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Cas clinique | Rare Tumors | Pazopanib dans le sarcome d'Ewing extra-osseux ; justifie un bras Ewing dans SARC024. |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69548508 | STIVARGA 40 mg, comprimé pelliculé (BAYER AG, Allemagne) | Comprimé pelliculé | Non renseignée (AMM annulée) |

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée (inhibiteur multikinase) |
| Risque de Myélosuppression | Veuillez consulter les mises en garde et précautions de la notice |
| Classification d'Émétogénicité | Veuillez consulter les mises en garde et précautions de la notice |
| Éléments de Surveillance | Fonction hépatique (toxicité hépatique documentée avec les ITK anti-angiogéniques), tension artérielle, protéinurie, NFS |
| Protection de Manipulation | Veuillez consulter la notice pour les mesures de manipulation applicables |

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 213 interactions recensées. Parmi celles listées :
  - **Majeures** : acide acétylsalicylique, déférasirox, ibritumomab tiuxétan, tositumomab (y compris I-131), abciximab, altéplase, antithrombine III humaine, apixaban. Les interactions avec les antithrombotiques et thrombolytiques suggèrent un risque hémorragique accru.
  - **Modérées** : dexaméthasone, clarithromycine, naltrexone, dexfenfluramine, fenfluramine, rosuvastatine, sibutramine, cobicistat.
  - **Mineures** : dapagliflozine, naloxégol, prucalopride.
- Les données de la littérature signalent par ailleurs, pour cette classe, des risques de toxicité hépatique, de syndrome main-pied et de protéinurie (méta-analyses).

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles : veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails (à réexaminer, voir réserves)**

**Justification :**
- Un essai randomisé contre placebo existe, mais sa cohorte liposarcome est négative : le niveau L1 reflète la qualité méthodologique des études et non un résultat favorable. La prédiction TxGNN n'est pas confirmée cliniquement dans cette indication ; une décision plus prudente (Hold) serait défendable.
- L'AMM française est annulée et les données de sécurité de la notice sont manquantes (lacune bloquante pour le criblage de sécurité).

**Pour avancer, les éléments suivants sont nécessaires :**
- Notice ANSM (mises en garde, contre-indications) pour lever la lacune de sécurité bloquante
- Données détaillées sur le mécanisme d'action (DrugBank)
- Justification d'un sous-groupe de liposarcome susceptible de répondre, ou évaluation en association (comme suggéré par les auteurs de SARC024)
- Clarification du statut réglementaire en France (AMM annulée)

**Autres indications prédites (à titre d'information) :**
- **Carcinome rénal à cellules claires** (score 99,47 %, niveau L2, « Research Question ») : phase 2 de regorafenib en première ligne (PMID 22959186) et étude de repositionnement préclinique (2026), mais le traitement de référence a évolué vers d'autres ITK et immunothérapies.
- **Autres entités** (liposarcome myxoïde ovarien, carcinomes rénaux non classés, associés à des translocations Xp11.2/TFE3 ou au neuroblastome, carcinome rénal de l'enfant, sarcome de la vulve) : niveau L5, aucune donnée spécifique, **Hold**. Les scores élevés proviennent vraisemblablement de la proximité dans le graphe avec les nœuds parents.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

