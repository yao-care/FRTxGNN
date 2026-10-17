---
layout: default
title: Flunarizine
parent: Prédiction du modèle uniquement (L5)
nav_order: 336
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Flunarizine : nouvelle indication prédite, Trouble migraineux (migraine) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données compilées"
monitor_inn: "FLUNARIZINE"
predicted_indications: ["migraine disorder"]
---

# Flunarizine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **1** 
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

# Flunarizine : D'une indication non renseignée au Trouble Migraineux

## Résumé en Une Phrase

La flunarizine est un inhibiteur calcique de la famille des diphénylpipérazines. Son indication d'origine n'est pas renseignée dans la seule AMM française recensée, aujourd'hui annulée.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **trouble migraineux** (migraine), avec **13 essais cliniques** et **20 publications** soutenant actuellement cette direction.
Il s'agit toutefois davantage de la confirmation d'un usage déjà établi dans de nombreux pays (prophylaxie de la migraine) que d'un repositionnement réellement nouveau.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données compilées |
| Nouvelle Indication Prédite | Trouble migraineux (migraine) |
| Score de Prédiction TxGNN | 99,12 % |
| Niveau de Preuve | L2 (niveau attribué dans les données compilées ; voir la réserve ci-dessous) |
| Statut de Marché en France | ✗ AMM annulée uniquement |
| Nombre d'AMM | 1 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. Sur la base des connaissances pharmacologiques générales, la flunarizine est un inhibiteur calcique de type diphénylpipérazine, dotée aussi d'une activité antihistaminique et antagoniste des récepteurs dopaminergiques D2. Les données de pharmacologie compilées indiquent qu'elle cible le récepteur D2 ainsi que les canaux calciques de type T (Cav3.1, Cav3.2 et Cav3.3).

Le blocage des canaux calciques voltage-dépendants (de type T et P/Q) est considéré comme réduisant l'hyperexcitabilité neuronale et la dépression corticale envahissante, à l'origine de l'aura migraineuse et du déclenchement des crises. Ce mécanisme est cohérent avec le score TxGNN très élevé.

La flunarizine figure dans de nombreuses revues et recommandations sur le traitement préventif de la migraine, y compris dans des contextes pédiatriques et de migraine hémiplégique familiale. Les données de pharmacologie la décrivent comme principalement utilisée en prophylaxie de la migraine, approuvée dans de nombreux pays mais pas par la FDA.

---

## Preuves d'Essais Cliniques

Les essais ci-dessous sont les plus pertinents parmi les 13 recensés. Aucun ne présente de résultats publiés dans les données compilées.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | Terminé | 62 | Flunarizine 10 mg/j vs topiramate 50 mg/j en prophylaxie de la migraine chronique |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | NA | Terminé | 120 | Comparaison du bloc du nerf grand occipital, du topiramate et de la flunarizine dans la migraine épisodique |
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | Pas encore en recrutement | 460 | Essai pragmatique comparant amitriptyline, flunarizine, topiramate et propranolol en soins primaires |
| [NCT07655700](https://clinicaltrials.gov/study/NCT07655700) | Phase 4 | Pas encore en recrutement | 177 | Propranolol, flunarizine et leur association en prophylaxie de la migraine |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | NA | Inconnu | 84 | Flunarizine vs amitriptyline : fréquence des crises et douleur (EVA) |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | NA | En recrutement | 44 | Flunarizine vs propranolol dans la migraine pédiatrique (score PedMIDAS) |
| [NCT07751497](https://clinicaltrials.gov/study/NCT07751497) | Phase 2 | Pas encore en recrutement | 400 | Non-infériorité du rimégépant vs flunarizine dans la migraine vestibulaire |
| [NCT06753825](https://clinicaltrials.gov/study/NCT06753825) | NA | Actif, non en recrutement | 60 | Radiofréquence pulsée transcutanée vs inhibiteurs calciques dans la migraine de l'enfant |
| [NCT07068815](https://clinicaltrials.gov/study/NCT07068815) | Phase 1 | Pas encore en recrutement | 60 | Aiguilletage sous-cutané de Fu vs flunarizine dans la migraine sans aura |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | Terminé | 75 | Étude pharmacocinétique d'interaction flunarizine–topiramate ; pas de données d'efficacité |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Revue systématique avec modélisation économique | Health Technol Assess | Efficacité clinique et coût-efficacité des traitements préventifs de la migraine chronique |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Méta-analyse en réseau | JAMA Netw Open | Efficacité et sécurité des traitements préventifs de la migraine pédiatrique |
| [40553594](https://pubmed.ncbi.nlm.nih.gov/40553594/) | 2025 | Revue systématique et méta-analyse | J Assoc Physicians India | Amitriptyline comparée au propranolol et à la flunarizine en prophylaxie de la migraine |
| [42673559](https://pubmed.ncbi.nlm.nih.gov/42673559/) | 2026 | Revue systématique | Neurology | Mise à jour des conclusions AAN/AHS sur la prévention pharmacologique de la migraine de l'adulte |
| [31413170](https://pubmed.ncbi.nlm.nih.gov/31413170/) | 2019 | Recommandation | Neurology | Recommandations AAN/AHS sur la prévention pharmacologique de la migraine pédiatrique |
| [30428122](https://pubmed.ncbi.nlm.nih.gov/30428122/) | 2019 | Étude clinique | Acta Neurol Scand | Association flunarizine + neurostimulation supraorbitaire transcutanée, prophylaxie améliorée |
| [41572863](https://pubmed.ncbi.nlm.nih.gov/41572863/) | 2026 | Revue | Dtsch Arztebl Int | Médicaments de la prophylaxie de la migraine |
| [28497257](https://pubmed.ncbi.nlm.nih.gov/28497257/) | 2017 | Revue | Nervenarzt | La flunarizine figure parmi les options de traitement prophylactique |
| [21049704](https://pubmed.ncbi.nlm.nih.gov/21049704/) | 2010 | Revue | J Assoc Physicians India | Bêtabloquants, flunarizine, topiramate, valproate et amitriptyline comme traitements de première intention |
| [9218683](https://pubmed.ncbi.nlm.nih.gov/9218683/) | 1997 | Étude préclinique | Eur J Pharmacol | La flunarizine altère la fonction des nerfs nitrergiques dans les artères cérébrales (artères canines) |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61247136 | SIBELIUM 10 mg, comprimé sécable (JANSSEN CILAG) | Comprimé sécable | Non renseignée (AMM annulée) |

---

## Considérations de Sécurité

**Interactions et pharmacologie :** les données d'interaction compilées ne mentionnent pas d'interaction médicamenteuse cliniquement classée. Elles décrivent des cibles pharmacologiques : récepteur D2 et canaux calciques Cav3.1, Cav3.2 et Cav3.3. L'activité antagoniste D2 justifie une vigilance particulière. Une étude pharmacocinétique de phase 1 (NCT00752466) a évalué l'association avec le topiramate, mais ses résultats ne sont pas détaillés dans les données compilées.

Veuillez consulter la notice pour les mises en garde et contre-indications, qui ne sont pas disponibles dans les données compilées.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- La flunarizine est un traitement préventif de la migraine déjà établi dans de nombreux pays et cité dans les revues et recommandations. Les essais comparatifs de phase 4 et les méta-analyses soutiennent cette direction.
- Réserve : le niveau L2 est celui attribué dans les données compilées. Les essais listés sont majoritairement comparatifs, de phase 4 ou NA, sans résultats publiés ; aucun essai de phase 3 contrôlé par placebo n'est identifié. La seule AMM française est annulée, et les données de sécurité sont absentes (l'étape de criblage de sécurité ne peut donc pas être franchie).

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde, contre-indications, indication approuvée) pour permettre le criblage de sécurité.
- Compléter les données sur le mécanisme d'action (DrugBank).
- Clarifier la raison de l'annulation de l'AMM française et le statut réglementaire actuel.
- Obtenir les résultats des essais comparatifs en cours ou terminés (par ex. NCT02639598, NCT03712917).
- Prévoir une surveillance de sécurité pour les populations spécifiques (enfants, personnes âgées), compte tenu de l'activité antagoniste D2.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

