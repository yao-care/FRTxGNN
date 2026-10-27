---
layout: default
title: Cyclophosphamide
parent: Preuves élevées (L1-L2)
nav_order: 203
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-14
description: "Cyclophosphamide : nouvelle indication prédite, Leucémie myéloïde (niveau de preuve L1). Indication d'origine : Lymphomes (mycosis fongoïde, lymphome cutané à cellules T)…"
monitor_inn: "CYCLOPHOSPHAMIDE"
predicted_indications: ["myeloid leukemia", "ganglioneuroblastoma (disease)", "vertebral anomalies and variable endocrine and T-cell dysfunction", "retroperitoneal neoplasm", "lymph node cancer"]
---

# Cyclophosphamide
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **5** 
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

## Cyclophosphamide : Des Lymphomes et Cancers du Sein à la Leucémie Myéloïde
{: .text-alpha }

## Résumé en Une Phrase

Le cyclophosphamide est un agent alkylant utilisé à l'origine dans le traitement de plusieurs cancers : lymphomes (dont le mycosis fongoïde), myélome multiple, neuroblastome, cancer du sein et rétinoblastome.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **leucémie myéloïde**,
avec **35 essais cliniques** et **20 publications** soutenant actuellement cette direction.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Lymphomes (mycosis fongoïde, lymphome cutané à cellules T), myélome multiple, neuroblastome, cancer du sein, rétinoblastome (le texte d'indication des AMM n'est pas renseigné ; indications issues du graphe de connaissances) |
| Nouvelle Indication Prédite | Leucémie myéloïde |
| Score de Prédiction TxGNN | 99,47 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Annulé uniquement (aucune AMM valide) |
| Nombre d'AMM | 3 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances pharmacologiques établies, le cyclophosphamide est un agent alkylant : ses métabolites actifs (notamment la moutarde de phosphoramide) forment des liaisons croisées avec l'ADN et sont cytotoxiques pour les cellules en prolifération.

Ses indications d'origine sont déjà des hémopathies malignes (lymphomes, myélome) et des tumeurs solides chimiosensibles. Une extension aux cellules myéloïdes malignes, également très prolifératives, est donc mécanistiquement plausible.

En pratique, le cyclophosphamide est déjà utilisé dans la leucémie myéloïde au sein de **régimes de conditionnement** avant allogreffe (busulfan-cyclophosphamide) et en **cyclophosphamide post-greffe (PTCy)** pour déplétionner les lymphocytes T alloréactifs et prévenir la maladie du greffon contre l'hôte. Il s'agit donc surtout d'un usage en association ou dans un contexte de greffe, et non d'une monothérapie.

---

## Preuves d'Essais Cliniques

Parmi les essais retrouvés, voici les plus pertinents (selon l'évaluation de pertinence) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00003187](https://clinicaltrials.gov/study/NCT00003187) | Phase 2/3 | Terminé | 19 | Greffe de moelle de donneur non apparenté, conventionnelle vs déplétée en lymphocytes T ; cyclophosphamide dans le conditionnement |
| [NCT04473911](https://clinicaltrials.gov/study/NCT04473911) | Phase 1 | Terminé | 25 | Greffe haplo-identique à conditionnement réduit avec cyclophosphamide post-greffe (prévention de la GVHD) |
| [NCT00315705](https://clinicaltrials.gov/study/NCT00315705) | Phase 1/2 | Terminé | 50 | Clofarabine + étoposide + cyclophosphamide dans les leucémies aiguës pédiatriques réfractaires ou en rechute |
| [NCT00390793](https://clinicaltrials.gov/study/NCT00390793) | Phase 2 | Terminé | 107 | Hyper-CVAD + dasatinib dans la LAL Ph+ (population surtout lymphoïde ; association confondante) |
| [NCT01350245](https://clinicaltrials.gov/study/NCT01350245) | Phase 2 | Terminé | 28 | Allogreffe haplo-identique en deux étapes dans les hémopathies malignes en rémission |
| [NCT02441803](https://clinicaltrials.gov/study/NCT02441803) | Phase 2 | Terminé | 11 | Allogreffe comme sauvetage initial dans la LAM en échec d'induction (très petit effectif) |
| [NCT04904588](https://clinicaltrials.gov/study/NCT04904588) | Phase 2 | Actif, hors recrutement | 300 | Greffe de donneur non apparenté HLA-incompatible avec cyclophosphamide post-greffe |
| [NCT05515029](https://clinicaltrials.gov/study/NCT05515029) | Phase 3 | Actif, hors recrutement | 56 | Cyclophosphamide post-greffe + abatacept, vedolizumab et inhibiteur de la calcineurine chez l'enfant et le jeune adulte |
| [NCT02724163](https://clinicaltrials.gov/study/NCT02724163) | Phase 3 | Actif, hors recrutement | 700 | Essai international de LAM pédiatrique (gemtuzumab ozogamicine, chimiothérapie d'induction) |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | Terminé | 213 | Greffe de sang de cordon avec conditionnement cyclophosphamide/fludarabine/irradiation corporelle totale |

La plupart de ces essais testent le cyclophosphamide comme composant d'un régime de conditionnement ou de prévention de la GVHD, et non comme variable étudiée isolément.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39168989](https://pubmed.ncbi.nlm.nih.gov/39168989/) | 2024 | Essai randomisé (suivi à long terme) | Blood Cancer J | Busulfan-fludarabine vs busulfan-cyclophosphamide dans la LAM (GITMO AML-R2) : meilleure mortalité non liée à la rechute avec BuFlu |
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Revue systématique / méta-analyse en réseau | Bone Marrow Transplant | Comparaison des conditionnements myéloablatifs dans la LAM en rémission complète |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Cohorte | Haematologica | 217 patients LAM : survie globale à 2 ans de 77 % avec conditionnement myéloablatif et PTCy |
| [38758817](https://pubmed.ncbi.nlm.nih.gov/38758817/) | 2024 | Cohorte | Cancer | PTCy vs ATG vs association pour la prévention de la GVHD en greffe haplo-identique dans la LAM |
| [41046309](https://pubmed.ncbi.nlm.nih.gov/41046309/) | 2026 | Cohorte (registre) | Bone Marrow Transplant | Sang de cordon vs greffe haplo-identique avec PTCy en première rémission de LAM |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Cohorte | Cytotherapy | Facteurs pronostiques de la greffe haplo-identique avec PTCy dans la LAM |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Cohorte | Future Oncol | Busulfan-cyclophosphamide vs fludarabine-busulfan en allogreffe pour LAM |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | Cohorte | Am J Hematol | Allogreffe non myéloablative cyclophosphamide/fludarabine vs myéloablative dans la LAM (165 patients) |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Étude rétrospective | Int J Mol Sci | PTCy après greffe apparentée ou non apparentée HLA-compatible chez l'enfant atteint de LAM |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Étude clinique | Transpl Immunol | Cladribine + busulfan + cyclophosphamide comme conditionnement intensif dans la LAM réfractaire ou en rechute |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62554177 | ENDOXAN 50 mg, comprimé enrobé (annulée) | Comprimé enrobé | Non renseignée |
| 64635418 | ENDOXAN 500 mg, poudre pour solution injectable (annulée) | Poudre et solvant pour solution injectable | Non renseignée |
| 69586327 | ENDOXAN 1000 mg, poudre pour solution injectable (annulée) | Poudre pour solution injectable | Non renseignée |

Les trois AMM (titulaire : Baxter) sont annulées ; aucune AMM valide n'est actuellement recensée dans les données compilées.

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (agent alkylant, moutarde azotée) |
| Risque de Myélosuppression | Élevé (neutropénie, thrombopénie) ; à rapprocher des régimes de greffe où la myéloablation est recherchée |
| Classification d'Émétogénicité | Moyenne à élevée selon la dose |
| Éléments de Surveillance | NFS avec formule, fonction hépatique et rénale, électrolytes, analyse d'urine (cystite hémorragique), fonction cardiaque aux fortes doses |
| Protection de Manipulation | Doit suivre les réglementations de manipulation des médicaments cytotoxiques |

Les données de toxicité détaillées ne figurent pas dans les données compilées ; ces éléments reposent sur les connaissances générales de la classe. Veuillez consulter les mises en garde et précautions de la notice.

---

## Considérations de Sécurité

- **Interactions Médicamenteuses** : 100 interactions ont été recensées. Parmi les principales (niveau modéré, sauf mention) :
  - Amphotéricine B (formes conventionnelle, complexe lipidique, sulfate de cholestéryle et liposomale)
  - Bupropion
  - Aprépitant
  - Métronidazole
  - Sulfamides hypoglycémiants et apparentés : chlorpropamide, acétohexamide, glimépiride, glipizide, glibenclamide, tolazamide, tolbutamide
  - Névirapine non concernée ; autres : natéglinide, répaglinide, nitisinone, troglitazone
  - Lévofloxacine et ondansétron (niveau mineur)

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Les essais de phase 2/3 et la littérature (dont un essai randomisé et des méta-analyses) soutiennent l'usage du cyclophosphamide dans la leucémie myéloïde, mais presque toujours au sein de régimes de greffe ou d'associations ; l'effet propre du médicament est difficile à isoler. Cet usage correspond d'ailleurs à une pratique déjà établie plus qu'à un repositionnement inédit.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (donnée bloquante pour le criblage de sécurité), les AMM étant toutes annulées
- Les données détaillées sur le mécanisme d'action (DrugBank)
- Une attribution des effets au contexte du régime (conditionnement, PTCy, association)
- Un suivi de la toxicité cardiaque, de la cystite hémorragique et des infections, avec dosage selon le protocole de greffe

---

### Note sur les autres prédictions

Les autres indications prédites sont moins soutenues :
- **Lymph node cancer (cancer ganglionnaire)** : niveau L1 (essais de phase 3 dans le cancer du sein avec atteinte ganglionnaire), mais ce regroupement est hétérogène et recoupe en grande partie les indications existantes (lymphome, cancer du sein) ; il ne s'agit pas d'un véritable repositionnement.
- **Ganglioneuroblastome** : niveau L3, uniquement des cas cliniques et un seul essai précoce où le cyclophosphamide sert à la lymphodéplétion ; question de recherche.
- **Néoplasme rétropéritonéal** : niveau L4, cas isolés et petites séries sans essai enregistré ; question de recherche.
- **Anomalies vertébrales avec dysfonction endocrinienne et des lymphocytes T** : niveau L5, prédiction du modèle uniquement, sans lien mécanistique ni preuve ; Hold.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

