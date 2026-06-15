---
layout: default
title: Imatinib
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
---

# Imatinib
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

# Imatinib : De la Leucémie Myéloïde Chronique aux Néoplasmes Fibroblastiques

## Résumé en Une Phrase

Imatinib est un inhibiteur sélectif de tyrosine kinase ciblant BCR-ABL, c-KIT et PDGFR, initialement développé et approuvé pour le traitement de la leucémie myéloïde chronique (LMC) et des tumeurs stromales gastro-intestinales (GIST).
Le modèle TxGNN prédit qu'il pourrait être efficace pour **10 nouvelles indications** dans le spectre des tumeurs fibroblastiques et des sarcomes des tissus mous ; la preuve la plus solide concerne les **néoplasmes fibroblastiques (dont le dermatofibrosarcome de Darier-Ferrand / DFSP)** — appuyée par **20 publications** et une approbation FDA existante depuis 2006 comme soutien déterminant.
La recommandation principale est **Proceed with Guardrails** pour les néoplasmes fibroblastiques, et **Hold** pour la majorité des 9 autres indications faute de preuves cliniques suffisantes.

---

## Aperçu Rapide

> **Note** : Ce rapport couvre 10 indications prédites (candidat multi-indications). L'indication présentée ci-dessous est celle disposant du niveau de preuve le plus élevé.

| Élément | Contenu |
|------|------|
| Indication Originale | Leucémie myéloïde chronique (LMC) / GIST (données AMM non disponibles dans la base) |
| Nouvelle Indication Principale Prédite | Néoplasme fibroblastique (DFSP) |
| Score de Prédiction TxGNN | 99,94% |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Non enregistré (base de données sans AMM) |
| Nombre d'AMM | 0 |
| Décision Recommandée | Proceed with Guardrails |

---

## Vue d'Ensemble des 10 Indications Prédites

| Rang | Indication | Score TxGNN | Niveau de Preuve | Essais Cliniques | Publications | Recommandation |
|------|-----------|-------------|-----------------|:---:|:---:|----------------|
| 1 | Heart fibrosarcoma | 99,94% | L4 | 0 | 1 | Hold |
| **2** | **Néoplasme fibroblastique (DFSP)** | **99,94%** | **L2** | **0*** | **20** | **Proceed with Guardrails** |
| 3 | Fibrosarcome conventionnel | 99,93% | L3 | 1 | 9 | Research Question |
| 4 | Kidney fibrosarcoma | 99,93% | L4 | 1† | 2 | Hold |
| 5 | Low grade fibromyxoid sarcoma | 99,93% | L5 | 0 | 1 | Hold |
| 6 | Liposarcome | 99,88% | L3 | 5† | 20 | Research Question |
| 7 | Liver fibrosarcoma | 99,86% | L4 | 0 | 2 | Hold |
| 8 | FMF autosomique récessive | 99,86% | L5 | 0 | 0 | Hold |
| 9 | Ovarian myxoid liposarcoma | 99,85% | L5 | 0 | 0 | Hold |
| 10 | Familial rhabdoid tumor | 99,83% | L5 | 0 | 0 | Hold |

*Un essai clinique ciblant directement le DFSP est identifié dans la recherche "fibrosarcome conventionnel" (NCT00085475).
†Essais parapluie ou incluant de multiples sous-types — non spécifiques à l'indication.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Imatinib (Glivec®) est un inhibiteur de petites molécules ciblant sélectivement trois tyrosine kinases oncogéniques : **BCR-ABL** (responsable de la LMC), **c-KIT** (impliqué dans les GIST, certaines leucémies et mastocytoses) et **PDGFR-α/β** (récepteur du facteur de croissance dérivé des plaquettes). C'est cette troisième cible, le PDGFRB, qui constitue le lien mécanistique central justifiant les prédictions TxGNN pour les tumeurs fibroblastiques.

Le **dermatofibrosarcome de Darier-Ferrand (DFSP)**, prototype des néoplasmes fibroblastiques, est caractérisé par une translocation chromosomique spécifique **t(17;22)(q22;q13)** présente dans plus de 90 % des cas. Cette translocation génère une protéine de fusion **COL1A1-PDGFB** qui entraîne une activation autocrine/paracrine constitutive du PDGFRB, stimulant la prolifération tumorale de façon ininterrompue. Imatinib, en inhibant directement le PDGFRB, bloque cette voie oncogénique à la source — ce qui explique son efficacité documentée dans le DFSP et son **approbation FDA en 2006** pour les formes avancées ou métastatiques. La translocation COL1A1-PDGFB est également retrouvée dans le fibroblastome à cellules géantes (GCF), variant pédiatrique du DFSP.

La prédiction TxGNN pour les autres tumeurs fibroblastiques repose sur la même logique d'extension du paradigme PDGFR : le **fibrosarcome conventionnel** exprime PDGFR dans une fraction de cas (en particulier les formes fibrosarcomateuses de DFSP ou FS-DFSP), tandis que le **liposarcome** présente une hétérogénéité moléculaire où certains sous-types expriment PDGFR/KIT. En revanche, pour les indications à mécanisme divergent — low grade fibromyxoid sarcoma (FUS-CREB3L2), liposarcome myxoïde (FUS-DDIT3), rhabdoid tumor (SMARCB1/INI1) ou FMF (MEFV/pyrin) — le mécanisme PDGFR est absent ou non établi, justifiant les recommandations Hold.

---

## Preuves d'Essais Cliniques

### Indication Principale : Néoplasme Fibroblastique (DFSP)

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|:---:|---------|
| [NCT00085475](https://clinicaltrials.gov/study/NCT00085475) | Phase 2 | Terminé | 17 | Imatinib mésylate dans les DFSP et fibroblastomes à cellules géantes avancés/métastatiques porteurs de la translocation t(17;22)(q22;q13) / fusion COL1A1-PDGFB |

### Indications Secondaires avec Essais Cliniques Disponibles

| Numéro d'Essai | Indication | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|:---:|---------|
| [NCT00006357](https://clinicaltrials.gov/study/NCT00006357) | Liposarcome | Phase 1/2 | Terminé | 91 | Imatinib (STI571) dans les sarcomes des tissus mous avancés — essai dose-finding et Phase 2 sur multiples sous-types dont liposarcome |
| [NCT00031915](https://clinicaltrials.gov/study/NCT00031915) | Fibrosarcome / Liposarcome | Phase 2 | Terminé | N/D | Gleevec dans les sarcomes des tissus mous et osseux métastatiques ou localement avancés non résécables — essai multicentrique CTOSS/NASSG |
| [NCT00154388](https://clinicaltrials.gov/study/NCT00154388) | Maladies malignes rares (parapluie) | Phase 2 | Terminé | 185 | Imatinib dans les maladies malignes rares associées aux tyrosine kinases sensibles — couvre kidney fibrosarcoma et autres entités |
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Liposarcome | Phase 2 | Terminé | 48 | Sunitinib (TKI de même classe) dans les sarcomes des tissus mous dont liposarcome — référence comparative indirecte |

---

## Preuves de la Littérature

### Indication Principale : Néoplasme Fibroblastique (DFSP) — 20 publications

| PMID | Année | Type | Revue | Résultats Principaux |
|------|:---:|------|------|---------|
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | 2025 | Recommandation de Pratique Clinique | Eur J Cancer | Recommandations européennes interdisciplinaires EADO/EDF/UEMS/EADV pour le diagnostic et traitement du DFSP (mise à jour 2024) — imatinib validé pour les formes avancées/non résécables |
| [41236573](https://pubmed.ncbi.nlm.nih.gov/41236573/) | 2025 | Translationnel | Human Cell | Établissement d'une ligne cellulaire DFSP résistante à l'imatinib (DFSP-DPH1) — modèle préclinique pour l'étude des mécanismes de résistance |
| [39580648](https://pubmed.ncbi.nlm.nih.gov/39580648/) | 2025 | Rapport de cas / Translationnel | Genet Med | Variant germinal PDGFRB associé à la myofibromatose infantile et résistance à l'imatinib — illustre la dépendance PDGFRB des tumeurs fibroblastiques |
| [37610680](https://pubmed.ncbi.nlm.nih.gov/37610680/) | 2023 | Translationnel | Human Cell | Profilage multi-omique et modélisation ex vivo du DFSP résistant à l'imatinib avec transformation fibrosarcomateuse |
| [36630365](https://pubmed.ncbi.nlm.nih.gov/36630365/) | 2023 | Revue | Clin Exp Dermatol | Revue complète du DFSP : caractéristiques cliniques, sous-types histologiques, translocation COL1A1-PDGFB dans >90 % des cas, imatinib en thérapie systémique |
| [36999599](https://pubmed.ncbi.nlm.nih.gov/36999599/) | 2023 | Revue | J Surg Oncol | Prise en charge chirurgicale du DFSP — les directives NCCN recommandent la chirurgie de Mohs ; imatinib pour la maladie avancée/non résécable |
| [33993132](https://pubmed.ncbi.nlm.nih.gov/33993132/) | 2021 | Revue | Curr Opin Otolaryngol | Mise à jour de la prise en charge diagnostique et thérapeutique du DFSP — approche multidisciplinaire |
| [26027711](https://pubmed.ncbi.nlm.nih.gov/26027711/) | 2015 | Revue | Expert Rev Anticancer Ther | Options de traitement actuelles du DFSP — mécanisme de la translocation t(17;22) et efficacité d'imatinib dans les formes non résécables ou métastatiques |
| [25852058](https://pubmed.ncbi.nlm.nih.gov/25852058/) | 2015 | Translationnel | Mol Cancer Ther | Perte de CDKN2A/p16 comme mécanisme de résistance à l'imatinib dans le DFSP — CDK4 identifié comme cible de seconde ligne |
| [30901500](https://pubmed.ncbi.nlm.nih.gov/30901500/) | 2019 | Préclinique | Drug Dev Res | Efficacité de liposomes ciblés et nanocochléates contenant imatinib + dexkétoprofène contre le fibrosarcome — données de délivrance ciblée |

---

## Cytotoxicité

Imatinib est un agent antinéoplasique (inhibiteur de tyrosine kinase ciblé). Cette section s'applique.

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Thérapie ciblée — Inhibiteur de tyrosine kinase (classe phénylaminopyrimidine) ; non cytotoxique conventionnel |
| Risque de Myélosuppression | Modéré — neutropénie et thrombocytopénie fréquentes (grade 3-4 rapporté chez ~7-14 % des patients en traitement LMC) ; risque variable selon l'indication et la dose |
| Classification d'Émétogénicité | Faible à modérée (administration orale ; risque émétogène modéré selon les lignes directrices MASCC/ESMO pour les thérapies orales ciblées) |
| Éléments de Surveillance | NFS avec différentielle (hebdomadaire le 1er mois, bimensuelle le 2e mois, puis périodiquement) ; transaminases et bilirubine (mensuellement pendant la 1ère année) ; créatinine ; poids et surveillance des œdèmes/rétention hydrique |
| Protection de Manipulation | Suivre les protocoles institutionnels de manipulation des agents cytotoxiques oraux ; éviter la manipulation des comprimés écrasés ou brisés ; port de gants recommandé lors de la dispense |

---

## Considérations de Sécurité

Les données de sécurité spécifiques (mises en garde, contre-indications, interactions médicamenteuses) ne sont pas disponibles dans cet Evidence Pack.

> Veuillez consulter la notice officielle (SmPC/RCP Glivec® ou équivalent national) pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails** *(pour les néoplasmes fibroblastiques / DFSP)*

**Justification :**
Le mécanisme d'action d'imatinib (inhibition sélective du PDGFRB) est directement applicable au DFSP grâce à la translocation oncogénique COL1A1-PDGFB présente dans >90 % des cas ; cette indication a déjà obtenu une approbation réglementaire (FDA 2006) et figure dans les recommandations de pratique clinique européennes 2024 (EADO/EDF). La richesse de la littérature (20 publications dont une guideline de niveau 1) et un essai clinique de Phase 2 ciblé (NCT00085475) confirment la solidité du rationnel, même si le niveau de preuve reste L2 faute d'essais de Phase 3.

**Pour avancer, les éléments suivants sont nécessaires :**
- **Statut réglementaire en France** : vérifier l'enregistrement ANSM de Glivec® / imatinib générique et les indications officiellement approuvées (discordance probable avec les données actuelles qui indiquent 0 AMM)
- **Sélection moléculaire obligatoire** : confirmation préalable de la translocation t(17;22) ou de la surexpression PDGFB avant toute initiation thérapeutique dans le DFSP
- **Données MOA complètes** : extraction des informations mécanistiques via DrugBank (ID : DB00619) pour consolider l'analyse de repositionnement
- **Mises en garde et contre-indications officielles** : récupération de la notice ANSM/EMA
- **Pour le fibrosarcome conventionnel et le liposarcome** (statut "Research Question") : analyse moléculaire individuelle de l'expression PDGFR/KIT pour identifier les patients susceptibles de bénéficier du traitement avant tout développement clinique
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

