---
layout: default
title: Glucagon
parent: Preuves modérées (L3-L4)
nav_order: 139
evidence_level: L4
indication_count: 1
---

# Glucagon
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **1** 
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

# Glucagon : Une Piste Predite pour le Syndrome de l'Intestin Irritable

## Resume en Une Phrase

Le glucagon est commercialise en France sous forme de poudre nasale (Baqsimi 3 mg), mais son indication d'origine n'est pas renseignee dans les donnees disponibles.
Le modele TxGNN predit qu'il pourrait etre efficace pour le **syndrome de l'intestin irritable (SII)**.
**10 essais cliniques** et **20 publications** ont ete identifies, mais **aucun ne teste le glucagon lui-meme dans le SII** : les signaux viennent d'analogues du GLP-1 (ROSE-010, liraglutide), qui ciblent une voie voisine.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Nouvelle Indication Predite | Syndrome de l'intestin irritable |
| Score de Prediction TxGNN | 99.24% |
| Niveau de Preuve | L4 |
| Statut de Marche en France | ✓ Commercialise |
| Nombre d'AMM | 1 |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les donnees detaillees sur le mecanisme d'action ne sont pas disponibles. Sur la base des informations connues, le glucagon est un peptide derive du proglucagon. Il agit sur le recepteur du glucagon et peut aussi provoquer une relaxation transitoire du muscle lisse, ce qui explique son usage dans certains gestes digestifs.

Les signaux cliniques cites pour le SII viennent d'une voie proche mais distincte. Les agonistes du recepteur du GLP-1 (autre peptide derive du proglucagon) inhibent la motricite gastro-intestinale. L'analogue ROSE-010 a reduit la douleur lors des crises de SII et modifie la motricite digestive chez des patientes atteintes de SII avec constipation. Le glucagon, en tant que relaxant de la musculature lisse, pourrait donc avoir un effet sur la motricite et la douleur du SII. Cette hypothese est plausible mais non demontree.

Le score TxGNN eleve (0.992) est une prediction purement computationnelle. Le passage des analogues du GLP-1 au glucagon n'a jamais ete valide directement. Toute extrapolation demande une verification experimentale specifique.

## Preuves d'Essais Cliniques

Aucun essai ne teste le glucagon dans le SII. Les deux essais les plus proches portent sur des analogues du GLP-1. Quatre autres essais recenses (NCT06333717, NCT00802971, NCT04230655, NCT06113146) sont sans rapport avec la question et ne sont pas detailles ici.

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Termine | 52 | ROSE-010 (analogue du GLP-1) sur la motricite digestive chez des femmes atteintes de SII avec constipation. C'est l'essai le plus proche de la maladie et de la voie, mais ce n'est pas le glucagon. |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Termine | 12 | Le GLP-1 natif et ROSE-010 inhibent la motricite antro-duodeno-jejunale postprandiale. Appui mecanistique uniquement, sans population SII. |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Arrete | 8 | Liraglutide dans le reservoir iléo-anal avec frequence des selles elevee. Population peu liee au SII, effectif trop faible pour conclure. |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Termine | 66 | Entrainement physique, dysbiose et taux de GLP-1 dans le SII. Intervention non medicamenteuse, sans glucagon. |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Actif, sans recrutement | 375 | Organoides intestinaux et antigenes nutritionnels. Lien avec le SII seulement indirect. |

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [22517769](https://pubmed.ncbi.nlm.nih.gov/22517769/) | 2012 | ECR (phase 1/2) | Am J Physiol Gastrointest Liver Physiol | Etude randomisee en double aveugle contre placebo de ROSE-010 (analogue du GLP-1) sur la motricite digestive dans le SII avec constipation. |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | ECR (analyse secondaire) | Scand J Gastroenterol | ROSE-010 a reduit la douleur pendant les crises de SII. L'analyse identifie les sous-populations les plus susceptibles de repondre. |
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Revue systematique / meta-analyse | Front Endocrinol | Amelioration du SII avec les agonistes du recepteur du GLP-1. Le GLP-1 et ROSE-010 inhibent le complexe moteur migrant. |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohorte | Ann Gastroenterol | Prescription et arret des agonistes du GLP-1 chez des patients atteints de SII, dans un contexte d'effets indesirables digestifs. |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Revue | Exp Physiol | Role possible des cellules L et du GLP-1 dans la physiopathologie du SII. |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Etude clinique | Clin Res Hepatol Gastroenterol | Le GLP-1 serique est diminue et correle a la douleur abdominale dans le SII avec constipation. |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Preclinique (rat) | Neurogastroenterol Motil | L'exendine-4 ameliore la dysfonction digestive dans un modele de SII chez le rat. |
| [23338623](https://pubmed.ncbi.nlm.nih.gov/23338623/) | 2013 | Preclinique (rat) | Int J Mol Med | Role du GLP-1 dans la pathogenese de modeles experimentaux de SII. |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Revue / preclinique | Adv Exp Med Biol | GLP-1 en aerosol pour le diabete et le SII. |
| [30023410](https://pubmed.ncbi.nlm.nih.gov/30023410/) | 2018 | Revue | Cell Mol Gastroenterol Hepatol | Interactions bidirectionnelles de l'axe cerveau-intestin-microbiote. |

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique |
|---------|------|------|
| 67972497 | BAQSIMI 3 mg, poudre nasale en recipient unidose (AMPHASTAR FRANCE PHARMACEUTICALS) | Poudre |

## Considerations de Securite

Veuillez consulter la notice pour les informations de securite.

## Conclusion et Prochaines Etapes

**Decision : Hold**

**Justification :**
La prediction repose sur un score computationnel et sur des donnees obtenues avec des analogues du GLP-1, pas avec le glucagon. Aucun essai ne teste le glucagon dans le SII, et les donnees de securite ne sont pas disponibles. Le niveau de preuve reste L4 : c'est une question de recherche, pas une candidature prete pour une evaluation clinique.

**Pour avancer, les elements suivants sont necessaires :**
- Recuperer la notice de l'ANSM (mises en garde et contre-indications) pour lancer le criblage de securite
- Obtenir les donnees de mecanisme d'action (par exemple via l'API DrugBank) et l'indication d'origine de l'AMM
- Verifier experimentalement, avec le glucagon lui-meme, l'effet sur la motricite et la douleur du SII (etude mecanistique ou essai de phase 1/2), sans se limiter a l'extrapolation depuis les analogues du GLP-1
- Evaluer la compatibilite de la voie d'administration (poudre nasale) avec l'usage envisage dans le SII
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

