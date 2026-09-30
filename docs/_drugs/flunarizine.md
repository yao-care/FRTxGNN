---
layout: default
title: Flunarizine
parent: Prédiction du modèle uniquement (L5)
nav_order: 135
evidence_level: L5
indication_count: 1
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

<div id="pharmacist">

## Rapport d'évaluation pharmaceutique

</div>

# Flunarizine : Vers le Trouble Migraineux (indication d'origine non renseignée)

## Résumé en Une Phrase

La flunarizine est un inhibiteur calcique, traditionnellement utilisé contre le vertige et la migraine. Le texte d'indication de son AMM française (SIBELIUM 10 mg) n'est pas renseigné dans le dossier.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **trouble migraineux (migraine)**,
avec **19 essais cliniques** et **20 publications** rattachés à cette direction. Cette utilisation est probablement déjà établie dans de nombreux pays : le dossier ne permet donc pas de parler de repositionnement au sens strict.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM |
| Nouvelle Indication Prédite | Trouble migraineux (migraine) |
| Score de Prédiction TxGNN | 99,12 % |
| Niveau de Preuve | L3 (méta-analyses et revues systématiques, sans essai de phase 3 complété sur la flunarizine) |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Proceed with Guardrails |

Le dossier source attribuait le niveau L1. En appliquant strictement la grille (L1 = au moins 2 ECR de phase 3 complétés), aucun essai de phase 3 ne figure dans les données. Le niveau retenu est donc L3.

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans le dossier (champ DrugBank vide). D'après la pharmacologie générale, la flunarizine est un inhibiteur calcique non sélectif (canaux de type T et L). Elle bloque aussi certains canaux sodiques et possède une activité antihistaminique H1. Ces éléments ne proviennent pas du dossier fourni et restent à confirmer.

Ces actions pourraient atténuer l'hyperexcitabilité neuronale et la dépression corticale envahissante, un mécanisme proposé pour l'aura migraineuse et les crises. Les canaux calciques sont aussi impliqués dans la migraine hémiplégique familiale (gène CACNA1A). La cohérence est forte entre le score TxGNN très élevé et la littérature, qui traite majoritairement de la flunarizine dans la prophylaxie de la migraine.

Une méta-analyse de l'European Headache Federation (2023) décrit la flunarizine comme un traitement repositionné, de première ou deuxième intention dans la prophylaxie de la migraine. Il faut donc d'abord vérifier le libellé exact de l'AMM française avant de qualifier cette indication de nouvelle.

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | Terminé | 62 | Flunarizine 10 mg/j vs topiramate 50 mg/j en prophylaxie de la migraine chronique |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | Non applicable | Terminé | 120 | Blocage du nerf grand occipital vs topiramate vs flunarizine dans la migraine épisodique (scores EVA, fréquence des crises) |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | Non applicable | Inconnu | 84 | Flunarizine vs amitriptyline en prophylaxie de la migraine (fréquence des crises, douleur), Lahore, Pakistan |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | Non applicable | En recrutement | 44 | Flunarizine vs propranolol dans la migraine pédiatrique (score PedMIDAS) ; pas encore de résultats |
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | Pas encore en recrutement | 460 | Comparaison pragmatique des traitements préventifs de première ligne (amitriptyline, flunarizine, topiramate, propranolol) en soins primaires |
| [NCT06753825](https://clinicaltrials.gov/study/NCT06753825) | Non applicable | Actif, hors recrutement | 60 | Radiofréquence pulsée transcutanée vs inhibiteurs calciques dans la migraine de l'enfant (le rôle exact de la flunarizine reste à confirmer) |
| [NCT07068815](https://clinicaltrials.gov/study/NCT07068815) | Phase 1 | Pas encore en recrutement | 60 | Aiguilletage sous-cutané de Fu vs flunarizine dans la migraine sans aura |
| [NCT03828539](https://clinicaltrials.gov/study/NCT03828539) | Phase 4 | Terminé | 777 | Érénumab vs topiramate ; la flunarizine figure parmi les prophylaxies antérieures possibles (preuve indirecte) |
| [NCT04064814](https://clinicaltrials.gov/study/NCT04064814) | Phase 4 | Terminé | 60 | Acide alpha-lipoïque en appoint dans la migraine de l'adolescent (preuve indirecte pour la flunarizine) |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | Terminé | 75 | Étude d'interaction pharmacocinétique flunarizine-topiramate, en mono- et co-administration |

Les 9 autres essais du dossier sont non pertinents ou peu pertinents pour l'efficacité de la flunarizine. Parmi eux figure un essai de phase 4 sur la schizophrénie (NCT00740259).

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [37723437](https://pubmed.ncbi.nlm.nih.gov/37723437/) | 2023 | Méta-analyse | J Headache Pain | Réévaluation critique de l'EHF sur la flunarizine en prophylaxie de la migraine (traitement de première ou deuxième intention) |
| [40553594](https://pubmed.ncbi.nlm.nih.gov/40553594/) | 2025 | Méta-analyse | J Assoc Physicians India | Efficacité et sécurité de l'amitriptyline vs propranolol et flunarizine en prophylaxie de la migraine |
| [38964249](https://pubmed.ncbi.nlm.nih.gov/38964249/) | 2024 | Méta-analyse | Clinics (Sao Paulo) | Chlorhydrate de flunarizine associé aux décoctions de médecine chinoise dans la migraine |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Méta-analyse en réseau | JAMA Netw Open | Traitements préventifs de la migraine pédiatrique : efficacité et sécurité |
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Revue systématique | Health Technol Assess | Traitements préventifs de la migraine chronique de l'adulte, avec modélisation économique |
| [30428122](https://pubmed.ncbi.nlm.nih.gov/30428122/) | 2019 | ECR | Acta Neurol Scand | Flunarizine associée à la neurostimulation supraorbitaire transcutanée, comparée à chacune seule en prophylaxie de la migraine |
| [2404346](https://pubmed.ncbi.nlm.nih.gov/2404346/) | 1990 | ECR (double insu) | S Afr Med J | Flunarizine 10 mg vs propranolol 60 mg × 3/j pendant 4 mois chez 58 patients |
| [31413170](https://pubmed.ncbi.nlm.nih.gov/31413170/) | 2019 | Recommandations | Neurology | Mise à jour AAN/AHS du traitement pharmacologique préventif de la migraine pédiatrique |
| [22683887](https://pubmed.ncbi.nlm.nih.gov/22683887/) | 2012 | Recommandations | Can J Neurol Sci | Recommandations de la Société canadienne des céphalées sur la prophylaxie de la migraine |
| [40614441](https://pubmed.ncbi.nlm.nih.gov/40614441/) | 2025 | Étude comparative | Brain Dev | Topiramate vs flunarizine chez l'enfant : douleur et impact sur la vie scolaire et sociale |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 61247136 | SIBELIUM 10 mg | Comprimé sécable | JANSSEN CILAG |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

Dans la littérature, une étude post-commercialisation (1997) a surveillé en priorité la survenue de dépression et de syndrome extrapyramidal sous flunarizine.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs méta-analyses, recommandations et essais comparatifs vont dans le même sens que la prédiction TxGNN (99,12 %). En revanche, aucun essai de phase 3 complété sur la flunarizine ne figure dans les données, et les informations de sécurité de la notice ANSM manquent.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice ANSM (mises en garde, contre-indications). Cette étape est bloquante pour le criblage de sécurité.
- Vérifier l'indication exacte de l'AMM SIBELIUM, pour établir si la migraine est déjà une indication autorisée en France.
- Compléter les données sur le mécanisme d'action (DrugBank).
- Confirmer le rôle de la flunarizine dans les essais NCT06753825 et NCT06499116, et évaluer les essais encore en attente de classement.
- Prévoir une surveillance de la dépression et des symptômes extrapyramidaux, notamment chez les populations vulnérables.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant toute application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

