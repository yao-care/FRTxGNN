---
layout: default
title: Metoclopramide
parent: Preuves modérées (L3-L4)
nav_order: 491
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Metoclopramide : nouvelle indication prédite, Ulcère gastrique (niveau de preuve L4). Indication d'origine : Reflux gastro-œsophagien, œsophagite"
monitor_inn: "metoclopramide"
predicted_indications: ["gastroduodenitis"]
---

# Metoclopramide
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **5** 
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

# Métoclopramide : Du reflux gastro-œsophagien à l'ulcère gastrique

## Resume en Une Phrase

La métoclopramide est un médicament prokinétique, initialement utilisé pour le traitement du reflux gastro-œsophagien et de l'œsophagite (y compris l'œsophagite peptique).
Le modèle TxGNN prédit qu'elle pourrait être utile pour l'**ulcère gastrique**, mais les preuves restent très limitées : **1 essai clinique** (de pertinence indirecte) et **20 publications**, pour la plupart des revues sans lien direct avec la cicatrisation des ulcères.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Reflux gastro-œsophagien, œsophagite (source : graphe de connaissances TxGNN ; aucune AMM française disponible) |
| Nouvelle Indication Predite | Ulcère gastrique |
| Score de Prediction TxGNN | 99,93 % |
| Niveau de Preuve | L4 |
| Statut de Marche en France | Non commercialisé (selon les données compilées) |
| Nombre d'AMM | 0 |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées. D'après les connaissances pharmacologiques générales, la métoclopramide est un prokinétique : antagoniste dopaminergique D2 et agoniste des récepteurs 5-HT4, qui accélère la vidange gastrique et augmente le tonus du sphincter inférieur de l'œsophage. Son efficacité sur les symptômes liés au reflux a été établie, ce qui explique sa proximité avec les indications d'origine.

La relation avec l'ulcère gastrique est toutefois indirecte. La métoclopramide ne réduit pas l'acidité gastrique et ne protège pas la muqueuse : elle ne cicatrise donc pas les ulcères. Le score élevé du modèle traduit surtout la proximité, dans le réseau de connaissances, avec les maladies de motilité et de reflux, et non une preuve directe d'effet sur la cicatrisation ulcéreuse.

Les autres prédictions (gastroduodénite, ulcère peptique, ulcère gastro-jéjunal, perforation d'ulcère peptique) présentent toutes un niveau de preuve L4 ou L5. Pour la perforation, un rôle thérapeutique est peu plausible, et un usage pourrait même être néfaste (la perforation digestive est une contre-indication connue de la métoclopramide).

## Preuves d'Essais Cliniques

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | Inconnu | 60 | Prémédication par métoclopramide dans les hémorragies digestives hautes : objectif de réduire les réinterventions (endoscopie, radiologie interventionnelle, chirurgie) et d'améliorer la visualisation. Pertinence indirecte pour l'ulcère. |

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [8439639](https://pubmed.ncbi.nlm.nih.gov/8439639/) | 1993 | ECR (bras comparateur) | Aliment Pharmacol Ther | L'oméprazole est supérieur à la ranitidine + métoclopramide dans l'œsophagite érosive |
| [8792695](https://pubmed.ncbi.nlm.nih.gov/8792695/) | 1996 | ECR (bras comparateur) | Am J Gastroenterol | L'oméprazole est comparé à la ranitidine ou ranitidine/métoclopramide dans le RGO peu répondeur |
| [786607](https://pubmed.ncbi.nlm.nih.gov/786607/) | 1976 | Revue | Drugs | Propriétés pharmacologiques et usage clinique de la métoclopramide |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Revue | Ann Intern Med | Pharmacologie et applications cliniques de la métoclopramide |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | Étude préclinique (rat) | Arch Int Pharmacodyn Ther | Effet protecteur contre les ulcères induits par l'aspirine et la ligature du pylore chez le rat |
| [42127996](https://pubmed.ncbi.nlm.nih.gov/42127996/) | 2026 | Recommandations | Endoscopy | Recommandations ESGE 2026 sur l'hémorragie ulcéreuse peptique (contexte de la maladie, pas un soutien à la métoclopramide) |
| [38059896](https://pubmed.ncbi.nlm.nih.gov/38059896/) | 2024 | ECR | Am J Gastroenterol | Efficacité de la métoclopramide pour la visualisation endoscopique dans l'hémorragie digestive haute active |
| [42259699](https://pubmed.ncbi.nlm.nih.gov/42259699/) | 2026 | ECR | Rev Gastroenterol Mex | Métoclopramide à forte dose versus placebo pour la visualisation endoscopique dans l'hémorragie digestive haute |

Les trois dernières références relèvent de l'usage procédural (visualisation avant endoscopie) et non du traitement de l'ulcère. Les autres publications identifiées sont majoritairement des revues générales sur la dyspepsie, la gastroparésie et le reflux.

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (non issues de la notice) : hypertension, épilepsie, phéochromocytome et paragangliome sympathique, porphyrie, cirrhose du foie, insuffisance rénale, ulcère peptique actif, syndrome malin des neuroleptiques, dyskinésie tardive, maladie de Parkinson et syndromes parkinsoniens, dystonie de torsion, troubles anxieux et dysthymiques, certains cancers (duodénum, intestin grêle, cœur, surrénale), déficit en pyruvate déshydrogénase E3, méthémoglobinémie par déficit en méthémoglobine réductase.
- **Interactions médicamenteuses** : 670 interactions recensées. Parmi les principales : **majeures** avec le tramadol et l'amisulpride ; **modérées** avec notamment le fentanyl, la codéine, la dihydrocodéine, l'alfentanil, l'alprazolam, l'amitriptyline, l'amantadine, l'éthanol, la cétirizine, la chlorphéniramine et l'abiratérone ; **mineure** avec le paracétamol.

Les mises en garde et contre-indications de la notice française ne sont pas disponibles : veuillez consulter la notice pour les informations de sécurité complètes. Point d'attention : l'ulcère peptique actif figure parmi les contre-indications du graphe de connaissances, ce qui est en tension directe avec l'indication prédite.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
- La prédiction repose sur la proximité dans le réseau de connaissances. Le seul essai clinique porte sur la visualisation endoscopique, la littérature disponible est surtout composée de revues, et les études comparatives montrent que la métoclopramide apporte peu par rapport à la suppression acide. Le médicament n'est pas commercialisé en France d'après les données compilées.

**Pour avancer, les elements suivants sont necessaires :**
- Récupérer la notice ANSM (mises en garde et contre-indications), bloquant pour le criblage de sécurité
- Obtenir les données sur le mécanisme d'action (DrugBank)
- Clarifier la contradiction entre l'indication prédite et la contre-indication « ulcère peptique actif »
- Disposer d'essais contrôlés évaluant directement la cicatrisation ou la récidive de l'ulcère gastrique
- Vérifier le statut réglementaire réel en France, l'absence d'AMM dans les données devant être confirmée
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

