---
layout: default
title: Clozapine
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
---

# Clozapine
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

# Clozapine : De la Schizophrénie Résistante au Trouble Bipolaire Maniaque

## Résumé en Une Phrase

Clozapine est un antipsychotique atypique de deuxième génération, largement reconnu comme traitement de référence de la schizophrénie résistante aux traitements conventionnels.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **Trouble Bipolaire avec Épisode Maniaque** (*manic bipolar affective disorder*),
avec **6 essais cliniques** recensés et **20 publications** soutenant actuellement cette direction de repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Schizophrénie résistante aux traitements (contexte clinique établi) |
| Nouvelle Indication Prédite | Trouble Bipolaire avec Épisode Maniaque (*Manic Bipolar Affective Disorder*) |
| Score de Prédiction TxGNN | 99,95% |
| Niveau de Preuve | L2 |
| Statut de Marché en France | Non référencé dans le système (données TFDA absentes) |
| Nombre d'AMM | 0 (aucune donnée disponible dans le système) |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action officiel ne sont pas disponibles dans le système actuel. Sur la base des informations cliniques connues, la clozapine est un antipsychotique atypique à action multi-récepteurs dont le profil pharmacologique est particulièrement large : elle exerce des propriétés antagonistes sur les récepteurs dopaminergiques D1, D2 et D4, sérotoninergiques 5-HT2A et 5-HT2C, histaminiques H1, muscariniques M1 à M5, ainsi qu'adrénergiques α1 et α2. Ce profil multi-cibles lui confère une action stabilisatrice multimodale qui peut simultanément réduire la suractivité dopaminergique à l'origine des symptômes maniaques, tout en modulant le système sérotoninergique — notamment via le blocage des récepteurs 5-HT2C, qui possède un mécanisme stabilisateur de l'humeur indépendant.

Le trouble bipolaire avec épisode maniaque et la schizophrénie partagent plusieurs mécanismes neurobiologiques fondamentaux, notamment une hyperactivité dopaminergique mésolimbique et des dysfonctions des circuits glutamatergiques préfrontaux. Cette proximité pathophysiologique explique pourquoi les antipsychotiques, initialement développés pour la schizophrénie, ont démontré une utilité dans les épisodes maniaques sévères. La faible occupation des récepteurs D2 par la clozapine, combinée à un puissant antagonisme D4 et 5-HT2A, présente un profil particulièrement adapté aux patients en échec thérapeutique aux traitements conventionnels (lithium, valproate, antipsychotiques de première ligne).

Plusieurs revues systématiques avec méta-analyse, une étude en double aveugle complétée (Phase 2, NCT00029458), ainsi que des données pharmacoépidémiologiques asiatiques confirment l'efficacité de la clozapine dans le trouble bipolaire résistant. La prédiction TxGNN s'appuie sur cette convergence mécanistique et clinique pour classer cette indication parmi les plus prometteuses pour un repositionnement encadré.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00029458](https://clinicaltrials.gov/study/NCT00029458) | Phase 2 | Terminé | 42 | Essai en double aveugle évaluant directement l'efficacité et la sécurité de la clozapine dans la phase maniaque du trouble bipolaire résistant au traitement ; preuve directe et centrale pour cette indication |
| [NCT05603104](https://clinicaltrials.gov/study/NCT05603104) | Phase 3 | En recrutement | 1 254 | Grand ECR multicentrique évaluant l'effet d'un traitement pharmacologique intensifié pour la schizophrénie, le TDM et le trouble bipolaire dépressif après premier échec thérapeutique |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | En recrutement | 40 | Évaluation de l'association pharmacothérapie + programme RECOVERYTRSBDGR pour le trouble bipolaire résistant au traitement |
| [NCT07398365](https://clinicaltrials.gov/study/NCT07398365) | N/A | En recrutement | 100 | Étude observationnelle caractérisant les phénotypes médicaux et psychiatriques des patients hospitalisés en psychiatrie adulte NHS |
| [NCT03651674](https://clinicaltrials.gov/study/NCT03651674) | N/A | Inconnu | 200 | Étude IRM longitudinale sur les effets de l'ECT dans la schizophrénie et le trouble bipolaire, cherchant des marqueurs neuroimageurs prédictifs de réponse |
| [NCT06993662](https://clinicaltrials.gov/study/NCT06993662) | Phase 1 | Actif, non en recrutement | 107 | Évaluation de l'association pharmacothérapie et thérapie cognitive et comportementale individuelle dans une pratique privée pour les troubles psychiatriques |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [32182485](https://pubmed.ncbi.nlm.nih.gov/32182485/) | 2020 | Revue systématique / Méta-analyse | Journal of Psychiatric Research | Évalue l'efficacité clinique de la clozapine dans le trouble bipolaire et son profil d'effets indésirables ; référence méthodologique de niveau 1 |
| [25346322](https://pubmed.ncbi.nlm.nih.gov/25346322/) | 2015 | Revue systématique | Bipolar Disorders | Évalue spécifiquement l'efficacité et la sécurité de la clozapine pour le trouble bipolaire résistant au traitement (TRBD) |
| [33719158](https://pubmed.ncbi.nlm.nih.gov/33719158/) | 2021 | Revue narrative | Bipolar Disorders | Synthèse des connaissances actuelles sur la clozapine dans le trouble bipolaire et perspectives de recherche futures |
| [31488793](https://pubmed.ncbi.nlm.nih.gov/31488793/) | 2019 | Revue | Psychiatria Danubina | Clozapine comme traitement prometteur de la suicidalité dans le trouble bipolaire, grâce à ses propriétés anti-agressivité et anti-impulsivité uniques |
| [37068038](https://pubmed.ncbi.nlm.nih.gov/37068038/) | 2023 | Cross-sectionnel / Registre | Journal of Clinical Psychopharmacology | Étude pharmacoépidémiologique multicentrienne asiatique (APPS Consortium) sur les caractéristiques cliniques et les modalités de prescription de la clozapine pour le trouble bipolaire |
| [40174308](https://pubmed.ncbi.nlm.nih.gov/40174308/) | 2025 | Cohorte rétrospective nationale | Journal of Psychiatric Research | Étude coréenne en vie réelle à l'échelle nationale évaluant l'efficacité antisuicidaire de la clozapine, du lithium et du valproate dans la schizophrénie et le trouble bipolaire |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Revue de pratique clinique | Acta Psychiatrica Scandinavica | Revue des options de traitement fondées sur les preuves pour la manie bipolaire, incluant le choix du stabilisateur d'humeur et de l'antipsychotique approprié |
| [16432528](https://pubmed.ncbi.nlm.nih.gov/16432528/) | 2006 | Revue | Molecular Psychiatry | Analyse détaillée du trouble bipolaire résistant : options thérapeutiques établies et émergentes, dont les antipsychotiques de deuxième génération (SGAs) |
| [11280956](https://pubmed.ncbi.nlm.nih.gov/11280956/) | 2001 | Revue | Bulletin of the Menninger Clinic | Vue d'ensemble des nouvelles pharmacothérapies pour le trouble bipolaire résistant, notamment les anticonvulsivants et les SGAs |
| [10682225](https://pubmed.ncbi.nlm.nih.gov/10682225/) | 2000 | Revue / Série de cas | Clinical Neuropharmacology | Revue de 36 patients traités par association ECT + clozapine : 67% ont bénéficié du traitement combiné, profil de sécurité globalement acceptable |

---

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

> Les données de mise en garde, contre-indications et interactions médicamenteuses n'ont pas été retrouvées dans le système lors de la consultation. Une attention particulière est recommandée pour le risque d'agranulocytose, complication grave connue de la clozapine nécessitant une surveillance hématologique régulière (programme REMS dans de nombreux pays).

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Un essai clinique de Phase 2 en double aveugle complété (NCT00029458, n=42) et deux revues systématiques avec méta-analyse soutiennent directement l'utilisation de la clozapine dans le trouble bipolaire maniaque résistant au traitement. Le niveau de preuve L2 est suffisant pour envisager une utilisation encadrée, mais l'absence de données réglementaires françaises disponibles dans le système et l'absence de données de sécurité structurées exigent une vigilance accrue avant toute application clinique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Vérification du statut AMM auprès de la base de données ANSM (la clozapine est connue sous les marques Leponex® et génériques en Europe)
- Données complètes sur le mécanisme d'action (MOA) via DrugBank API (DG002)
- Données de sécurité ANSM/TFDA : mises en garde, contre-indications et interactions médicamenteuses (DG001)
- Protocole de surveillance hématologique formalisé (risque d'agranulocytose — programme type REMS)
- Plan de gestion des risques pour une utilisation dans le trouble bipolaire résistant, population cible clairement définie
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

