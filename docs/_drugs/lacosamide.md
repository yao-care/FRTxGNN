---
layout: default
title: Lacosamide
parent: Prédiction du modèle uniquement (L5)
nav_order: 429
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "LACOSAMIDE"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "nephrogenic syndrome of inappropriate antidiuresis", "migraine disorder", "insomnia (disease)", "migraine with brainstem aura", "myofascial pain syndrome", "obsessive-compulsive disorder", "papillary conjunctivitis"]
description: "Lacosamide : nouvelle indication prédite, Manic bipolar affective disorder (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Lacosamide
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **10** 
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

## Lacosamide: Manic bipolar affective disorder
{: .text-alpha }

## Résumé en Une Phrase

Lacosamide est un antiépileptique, dont les autorisations françaises recensées sont toutes annulées.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble migraineux** (migraine disorder), avec **4 essais cliniques** et **16 publications** soutenant actuellement cette direction.

> Remarque : l'indication prédite en première position par TxGNN est le trouble bipolaire maniaque (score de 0,9996), mais les preuves disponibles sont faibles (niveau L3, études observationnelles et cas isolés). Ce rapport se concentre sur la migraine, l'indication la mieux étayée parmi les dix prédictions, avec un score de 0,9987.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Manic bipolar affective disorder |
| Score de Prédiction TxGNN | 0.9996 |
| Niveau de Preuve | L5 selon l'évaluation compilée, à nuancer (voir ci-dessous) |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Proceed with Guardrails |

Sur le niveau de preuve : trois essais de phase 3 sont recensés (NCT05632133, NCT05851781, NCT06243692), mais l'un porte sur un biomarqueur (CGRP), un autre a un statut inconnu, et aucun n'est contrôlé par placebo. Seul un essai de phase 3 est terminé avec une publication d'ECR correspondante. Le niveau L1 doit donc être interprété avec prudence.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. D'après les informations de la littérature, lacosamide renforce l'inactivation lente des canaux sodiques voltage-dépendants et module la protéine CRMP2. Ce sont des mécanismes partagés avec des anticonvulsivants établis.

La migraine et l'épilepsie sont deux troubles de l'hyperexcitabilité neuronale, et plusieurs antiépileptiques (topiramate, par exemple) sont déjà utilisés en prévention de la migraine. Une hypothèse avance que lacosamide, via CRMP2, inhibe la libération du CGRP (peptide lié au gène de la calcitonine) dans le système trigéminal. Une étude chez la souris montre en outre un effet sur la dépression corticale envahissante, mécanisme reconnu de la migraine.

Cette plausibilité mécanistique est cohérente avec la prédiction du modèle, mais elle reste à confirmer par des essais contrôlés par placebo.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT05851781](https://clinicaltrials.gov/study/NCT05851781) | Phase 3 | Terminé | 600 | Lacosamide versus propranolol : réduction des jours de migraine par mois et proportion de patients avec une réduction ≥ 50 % |
| [NCT06243692](https://clinicaltrials.gov/study/NCT06243692) | Phase 3 | Inconnu | 600 | Lacosamide versus topiramate dans la migraine, même critères de jugement ; pas de résultats disponibles |
| [NCT05632133](https://clinicaltrials.gov/study/NCT05632133) | Phase 3 | Terminé | 200 | Étude pilote randomisée : effet de lacosamide 50 mg 2 fois/jour sur le CGRP sérique, en plus de l'ibuprofène (critère biologique) |
| [NCT00440518](https://clinicaltrials.gov/study/NCT00440518) | Phase 2 | Terminé | 218 | Essai en double aveugle contre placebo (100 et 300 mg/jour) pour la prophylaxie de la migraine ; résultats non fournis, indication à vérifier |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [41863672](https://pubmed.ncbi.nlm.nih.gov/41863672/) | 2026 | ECR | Molecular Neurobiology | Lacosamide versus propranolol dans la migraine épisodique, en double aveugle ; alternative évaluée chez les patients ne tolérant pas le propranolol |
| [38502425](https://pubmed.ncbi.nlm.nih.gov/38502425/) | 2024 | ECR | Acta Neurologica Belgica | Effet de lacosamide sur le taux sérique de CGRP chez des patients migraineux épisodiques |
| [40670944](https://pubmed.ncbi.nlm.nih.gov/40670944/) | 2025 | Préclinique (souris) | The Journal of Headache and Pain | Effet de lacosamide sur la dépression corticale envahissante |
| [27917413](https://pubmed.ncbi.nlm.nih.gov/27917413/) | 2016 | Préclinique | Pain Reports | Efficacité de (S)-lacosamide dans des modèles de douleur céphalique, via CRMP2 et la libération de CGRP |
| [22779776](https://pubmed.ncbi.nlm.nih.gov/22779776/) | 2013 | Revue systématique / méta-analyse | Epilepsia | Profil d'événements indésirables de lacosamide dans les ECR |
| [22862686](https://pubmed.ncbi.nlm.nih.gov/22862686/) | 2012 | Revue | Expert Opinion on Emerging Drugs | Traitements émergents de la migraine chronique et réfractaire |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 62229123 | VIMPAT 150 mg | Comprimé pelliculé | Non renseignée (AMM active) |
| 60137021 | LACOSAMIDE ACCORD 10 mg/mL | Solution pour perfusion | Non renseignée (AMM active) |
| 60788509 | LACOSAMIDE ACCORD 50 mg | Comprimé pelliculé | Non renseignée (AMM active) |
| 60575525 | LACOSAMIDE EG 100 mg | Comprimé pelliculé | Non renseignée (AMM active) |
| 61150979 | LACOSAMIDE ZENTIVA 100 mg | Comprimé pelliculé | Non renseignée (AMM active) |

Au total, 20 AMM sont recensées, toutes annulées ; seules les 5 premières sont listées ici.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : arythmies et troubles de la conduction (fibrillation auriculaire, flutter auriculaire, bloc auriculo-ventriculaire, maladie du sinus), maladie coronarienne, ischémie myocardique, hypotension orthostatique, syndrome de tachycardie orthostatique posturale, atrophie multisystématisée, maladie hépatique, maladie de la vésicule biliaire.
- **Interactions médicamenteuses** : 25 interactions recensées. Les interactions majeures concernent le dolasétron, le céritinib et le siponimod. Parmi les interactions modérées : clarithromycine, éthanol, cobicistat, chloroquine, hydroxychloroquine, méfloquine, lidocaïne, kétoconazole, pasiréotide, alectinib, brigatinib, crizotinib, fingolimod, idélalisib, imatinib, ozanimod et sunitinib. Beaucoup concernent des médicaments allongeant l'intervalle PR ou QT, ce qui est cohérent avec les signaux cardiaques ci-dessus.
- **Signal d'alerte clinique** : un cas de neutropénie induite par lacosamide chez un patient bipolaire a été rapporté.

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- La migraine est l'indication la mieux étayée, avec des essais de phase 3 et un ECR publié en 2026 contre le propranolol. Les comparaisons actives ne montrent toutefois qu'une efficacité relative, sans confirmation contre placebo ni réplication indépendante.

**Pour avancer, les éléments suivants sont nécessaires :**
- Vérification des critères de jugement principaux et des résultats de NCT05851781, NCT06243692 et NCT00440518 (l'indication exacte de ce dernier est à confirmer).
- Essai contrôlé par placebo et réplication indépendante.
- Récupération des mises en garde et contre-indications de la notice ANSM (donnée bloquante pour le criblage de sécurité).
- Données sur le mécanisme d'action issues de DrugBank.
- Évaluation du risque cardiaque (ECG, intervalle PR) et surveillance hématologique.

**Autres prédictions (pour information) :**
- Le trouble bipolaire maniaque (L3, recommandation « Research Question ») repose sur une étude rétrospective et un essai ouvert pilote, avec un signal de sécurité.
- Le syndrome myofascial (L2, « Research Question ») repose sur un essai de phase 2 sans résultats fournis, dont l'intitulé porte sur la fibromyalgie.
- La migraine avec aura du tronc cérébral est classée « Research Question » (L4), sans donnée directe.
- Le syndrome de Gilles de la Tourette, la trichotillomanie, le SIAD néphrogénique, l'insomnie, le TOC et la conjonctivite papillaire restent en « Hold » (L4-L5), sans preuve de soutien.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

