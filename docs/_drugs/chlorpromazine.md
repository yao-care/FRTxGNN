---
layout: default
title: Chlorpromazine
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Chlorpromazine
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

# Chlorpromazine : De l'Antipsychotique Classique à la Schizophrénie à Début Précoce

## Résumé en Une Phrase

Chlorpromazine est le premier antipsychotique de la classe des phénothiazines, synthétisé en 1952, dont l'efficacité dans la schizophrénie et les troubles psychotiques est établie depuis sept décennies via un antagonisme des récepteurs dopaminergiques D2. Le modèle TxGNN prédit qu'il pourrait être efficace pour la **Schizophrénie à Début Précoce** — seule prédiction cliniquement pertinente dans ce dossier —, avec **1 étude observationnelle** et **8 publications** soutenant cette direction. ⚠️ Les 9 premières prédictions TxGNN (rangs 1–9) correspondent à des signaux inverses documentés (dont la rétinopathie aux phénothiazines) ou à des maladies génétiques sans lien mécanistique : elles sont exclues de l'analyse de repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non disponible dans le dossier (antipsychotique historique reconnu) |
| Nouvelle Indication Prédite | Schizophrénie à Début Précoce (rang TxGNN 10 — première prédiction cliniquement pertinente) |
| Score de Prédiction TxGNN | 99,47% |
| Niveau de Preuve | L3 |
| Statut de Marché | Non commercialisé |
| Nombre d'AMM | 0 |
| Décision Recommandée | Hold |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans ce dossier. Sur la base des informations connues, chlorpromazine est un antipsychotique typique (phénothiazine aliphatique) dont le mécanisme central repose sur l'antagonisme des récepteurs dopaminergiques D2 dans les voies méso-limbiques. Ce mécanisme cible directement l'hyperactivité dopaminergique considérée comme la base physiopathologique des symptômes positifs de la schizophrénie — hallucinations et idées délirantes.

La schizophrénie à début précoce (EOS, onset < 18 ans) partage cette même neurobiologie dopaminergique, mais constitue une population spécifique avec une présentation clinique plus sévère, une plus grande prévalence de résistance primaire au traitement, et une sensibilité accrue aux effets extrapyramidaux des antipsychotiques typiques. La prédiction TxGNN au rang 10 (score 99,47%) reflète la continuité mécanistique directe entre l'indication adulte établie et cette sous-population pédiatrique.

> **⚠️ Alerte sur les rangs 1–9 — Signaux inverses et prédictions non pertinentes**
>
> Les 9 premières prédictions TxGNN doivent être rejetées comme candidats de repositionnement :
>
> - **Rang 1 – Dystrophie rétinienne** : Signal inverse. Chlorpromazine cause elle-même une rétinopathie aux phénothiazines (dépôts pigmentaires rétiniens) à doses cumulées élevées — c'est un effet indésirable documenté, non une indication. Le modèle TxGNN a probablement confondu la co-occurrence médicament/maladie rétinienne dans le graphe de connaissances (chemin d'effet indésirable interprété comme chemin thérapeutique).
> - **Rangs 2–9** : Maladies génétiques ou malformations congénitales (CDG-fucosylation, myopies liées à l'X, hydranencéphalie, polymicrogyrie, CMT1G, encéphalopathie glycinique) sans lien mécanistique avec l'antagonisme D2 et sans aucune preuve clinique ou préclinique disponible.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT06128408](https://clinicaltrials.gov/study/NCT06128408) | N/A | Inconnu | 300 | Étude observationnelle sur les caractéristiques de la schizophrénie résistante depuis le début de la maladie : 30% des patients naïfs aux antipsychotiques ne répondent pas au traitement standard ; ces patients à résistance primaire (TRO) représentent 80% de tous les cas TRS en suivi à long terme |

> Cet essai est observationnel et descriptif — non interventionnel pour chlorpromazine spécifiquement. Aucun essai randomisé contrôlé dédié à l'EOS avec chlorpromazine n'a été identifié dans ce dossier.

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [10703271](https://pubmed.ncbi.nlm.nih.gov/10703271/) | 1999 | Cohorte rétrospective | Soc Psychiatry Psychiatr Epidemiol | Corrélation entre âge précoce au début de la schizophrénie et dosage des neuroleptiques typiques en ambulatoire — données de base pour calibrage posologique pédiatrique |
| [18408624](https://pubmed.ncbi.nlm.nih.gov/18408624/) | 2008 | Étude d'association génétique | Pharmacogenetics Genomics | Gène BDNF comme facteur de risque génétique de schizophrénie et déterminant du syndrome extrapyramidal induit par chlorpromazine (population chinoise) — pertinence pharmacogénomique directe |
| [28976410](https://pubmed.ncbi.nlm.nih.gov/28976410/) | 2017 | Étude clinique | Clin Neuropharmacology | Caractéristiques cliniques de l'EOS comorbide avec trouble obsessionnel-compulsif : implications pour la sélection et le dosage des antipsychotiques |
| [24289465](https://pubmed.ncbi.nlm.nih.gov/24289465/) | 2013 | Cohorte rétrospective | Psychogeriatrics | Comparaison clinique entre schizophrénie à début tardif et précoce au Japon — profils de réponse aux antipsychotiques selon l'âge d'onset |
| [17915974](https://pubmed.ncbi.nlm.nih.gov/17915974/) | 2007 | Étude d'association génétique | J Clin Psychiatry | Polymorphismes AKT1 associés au risque de schizophrénie et à la réponse aux antipsychotiques dans la population chinoise — voie de signalisation liée au D2 |
| [26916502](https://pubmed.ncbi.nlm.nih.gov/26916502/) | 2016 | Étude transversale | Acta Neuropsychiatrica | Capacités de théorie de l'esprit chez adolescents avec EOS — corrélations avec évaluation clinique et fonctions exécutives |
| [24854724](https://pubmed.ncbi.nlm.nih.gov/24854724/) | 2015 | Étude transversale | L'Encéphale | Signes neurologiques doux dans l'EOS — données soutenant le modèle neurodéveloppemental et orientant la surveillance clinique |
| [22802957](https://pubmed.ncbi.nlm.nih.gov/22802957/) | 2012 | Étude de neuroimagerie | PLoS ONE | Réduction du volume de matière grise du gyrus temporal dans l'EOS lors du premier épisode — marqueur neuropathologique de la sévérité précoce |

---

## Considérations de Sécurité

Les données de sécurité officielles (notices réglementaires, contre-indications formelles) ne sont pas disponibles dans ce dossier.

Sur la base des données cliniques documentées pour chlorpromazine :

- **Syndrome extrapyramidal** : Parkinsonisme médicamenteux, akathisie, dystonie aiguë — risque significativement augmenté chez les enfants et adolescents par rapport aux adultes ; facteur limitant majeur en population pédiatrique
- **Rétinopathie aux phénothiazines** : Toxicité pigmentaire rétinienne dose-cumulée dépendante — impose une surveillance ophtalmologique régulière lors d'un usage prolongé
- **Syndrome malin des neuroleptiques** : Complication rare mais potentiellement fatale — surveillance obligatoire en début de traitement

> Veuillez consulter la notice officielle pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
Ce dossier présente une configuration atypique : les 9 premières prédictions TxGNN sont des signaux inverses ou biologiquement non pertinents, et seule la schizophrénie à début précoce constitue une direction cliniquement fondée. Cependant, chlorpromazine étant déjà un antipsychotique historiquement établi pour la schizophrénie de l'adulte, la question réelle n'est pas un repositionnement thérapeutique classique mais une extension vers une population pédiatrique — pour laquelle son profil extrapyramidal représente un obstacle significatif face aux antipsychotiques de deuxième génération (risperidone, aripiprazole) disposant d'un meilleur cadre réglementaire pédiatrique.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données de mécanisme d'action (MOA) complètes via DrugBank (lacune DG002)
- Notices officielles avec contre-indications et mises en garde formelles (lacune DG001)
- Revue systématique des essais contrôlés randomisés : antipsychotiques de 1ère génération en EOS (0–18 ans)
- Analyse comparative risque-bénéfice avec antipsychotiques atypiques de 2ème génération en population pédiatrique
- Révision du pipeline TxGNN pour filtrer les associations issues d'effets indésirables (faux positifs par adjacence dans le graphe de connaissances, illustrés par les rangs 1–9 de ce dossier)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

