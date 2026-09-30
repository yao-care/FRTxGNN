---
layout: default
title: Terbutaline
parent: Preuves élevées (L1-L2)
nav_order: 303
evidence_level: L1
indication_count: 3
---

# Terbutaline
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **3** 
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

# Terbutaline : Du Bronchospasme à la Maladie Pulmonaire Obstructive

## Résumé en Une Phrase

La terbutaline est un agoniste bêta-2 adrénergique sélectif, commercialisé en France sous forme de poudre pour inhalation (Bricanyl Turbuhaler). Le texte d'indication de l'AMM n'est pas renseigné dans les données reçues, et le bronchospasme (asthme, BPCO) correspond à son usage établi.
Le modèle TxGNN prédit qu'elle pourrait être efficace dans la **maladie pulmonaire obstructive**, avec **48 essais cliniques** et **20 publications** associés. Il s'agit surtout de la confirmation d'une indication déjà connue, et non d'un repositionnement au sens strict.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans l'AMM (usage établi : bronchospasme de l'asthme et de la BPCO) |
| Nouvelle Indication Prédite | Maladie pulmonaire obstructive |
| Score de Prédiction TxGNN | 99,96 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 1 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans DrugBank pour ce dossier. Sur la base des connaissances pharmacologiques établies, la terbutaline est un agoniste bêta-2 sélectif. Elle relâche le muscle lisse bronchique via le récepteur bêta-2, la protéine Gs, l'adénylate cyclase et l'AMPc.

Ce mécanisme correspond directement à l'obstruction des voies aériennes dans l'asthme et la BPCO. La prédiction TxGNN ne décrit donc pas un nouvel usage. Elle rejoint l'usage clinique historique du médicament, ce que confirment de nombreux essais et publications.

Cette cohérence explique le score élevé. Il faut toutefois rester prudent : dans la majorité des essais récents, la terbutaline est le comparateur (traitement de secours à la demande) et non le médicament expérimental.

## Preuves d'Essais Cliniques

Sur 48 essais retrouvés, voici les 10 plus pertinents :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Phase 3 | Terminé | 3850 | Symbicort à la demande vs terbutaline à la demande vs budésonide 2 fois/jour + terbutaline, dans l'asthme léger. Terbutaline = comparateur, données d'efficacité et de sécurité à grande échelle |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Phase 3 | Terminé | 860 | Budésonide/formotérol à la demande vs traitement régulier + terbutaline à la demande, asthme persistant léger à modéré |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | Terminé | 2091 | Symbicort SMART vs Symbicort + terbutaline Turbuhaler 0,4 mg à la demande, sur 12 mois |
| [NCT00242775](https://clinicaltrials.gov/study/NCT00242775) | Phase 3 | Terminé | 2100 | Symbicort à dose variable vs Seretide + terbutaline Turbuhaler à la demande, asthme persistant |
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Phase 3 | Terminé | 24 | Efficacité relative de la terbutaline Turbuhaler 0,4 mg vs salbutamol pMDI chez des adultes asthmatiques japonais (croisé, dose unique) |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Phase 3 | Terminé | 95 | Bricanyl Turbuhaler M3 vs M2 : protection contre la bronchoconstriction induite par la méthacholine (asthme léger à modéré) |
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Phase 3 | Terminé | 120 | Sulfate de magnésium IV vs terbutaline chez l'enfant en exacerbation aiguë d'asthme |
| [NCT01944033](https://clinicaltrials.gov/study/NCT01944033) | Phase 3 | Terminé | 250 | Bêta-2 agoniste seul vs ipratropium + bêta-2 agoniste dans l'exacerbation de BPCO (le titre ne confirme pas que la terbutaline est l'agent) |
| [NCT00750568](https://clinicaltrials.gov/study/NCT00750568) | Non précisée | Inconnu | 36 | Pharmacocinétique et pharmacodynamie de la terbutaline en perfusion IV continue dans l'état de mal asthmatique pédiatrique |
| [NCT00837967](https://clinicaltrials.gov/study/NCT00837967) | Phase 3 | Terminé | 25 | Tolérance de 10 inhalations de Symbicort vs 10 inhalations de terbutaline Turbuhaler chez des asthmatiques japonais (croisé) |

## Preuves de la Littérature

Sur 20 publications, voici les 10 plus pertinentes (ECR en priorité) :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | ECR | Acad Emerg Med | Terbutaline + ipratropium nébulisés vs terbutaline seule dans l'exacerbation de BPCO nécessitant une ventilation non invasive |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | ECR | Br J Dis Chest | La terbutaline orale augmente la force de contraction diaphragmatique dans la BPCO (vs placebo) |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | ECR | Int J Clin Pharmacol Ther Toxicol | Clenbutérol vs terbutaline orale dans la BPCO, effet bronchodilatateur sur 2 semaines |
| [33065789](https://pubmed.ncbi.nlm.nih.gov/33065789/) | 2020 | Étude clinique (schéma non confirmé) | Ann Palliat Med | N-acétylcystéine + terbutaline chez le sujet âgé atteint de BPCO |
| [1615190](https://pubmed.ncbi.nlm.nih.gov/1615190/) | 1992 | Étude clinique (schéma non confirmé) | Respir Med | Terbutaline inhalée (Turbuhaler) : effet sur le VEMS, la CVF, la dyspnée et la distance de marche dans la BPCO (double aveugle, croisé, contre placebo) |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | Non classé | Lung | Dose unique de terbutaline (Turbuhaler) : effet sur la fonction pulmonaire et la capacité à l'effort dans la BPCO (double aveugle, contre placebo, croisé) |
| [18761816](https://pubmed.ncbi.nlm.nih.gov/18761816/) | 2008 | Non classé | Cell Mol Immunol | Terbutaline + budésonide en nébulisation : amélioration de l'immunité et de la fonction pulmonaire dans l'exacerbation de BPCO |
| [8882073](https://pubmed.ncbi.nlm.nih.gov/8882073/) | 1996 | Non classé | Thorax | Effets de l'arrêt de la terbutaline sur l'obstruction et la réactivité bronchiques dans la BPCO |
| [8296260](https://pubmed.ncbi.nlm.nih.gov/8296260/) | 1993 | Non classé | Thorax | Réversibilité bronchodilatatrice à faibles et fortes doses de terbutaline et d'ipratropium dans la BPCO |
| [2951811](https://pubmed.ncbi.nlm.nih.gov/2951811/) | 1986 | Non classé | Respiration | Fénotérol-ipratropium vs terbutaline inhalée dans la BPCO (étude en simple aveugle) |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 60961427 | BRICANYL TURBUHALER 500 microgrammes/dose (AstraZeneca) | Poudre pour inhalation | Non précisée dans les données |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Plusieurs essais de phase 3 terminés, portant sur plusieurs milliers de patients asthmatiques et sur la BPCO, soutiennent l'usage de la terbutaline dans les maladies obstructives. Cette prédiction confirme surtout une indication déjà établie, et la terbutaline est souvent le comparateur plutôt que l'agent testé. Les autres prédictions du modèle (malformation respiratoire, syndrome de Rienhoff) restent en attente (Hold), faute de preuves directes.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice de l'ANSM (mises en garde, contre-indications), une lacune bloquante pour le dépistage de sécurité
- Obtenir le texte d'indication de l'AMM et les données détaillées sur le mécanisme d'action (DrugBank)
- Prévoir une surveillance de la tachycardie, de l'hypokaliémie et des tremblements, avec prudence chez les patients atteints de maladie cardiovasculaire

*Ces résultats sont fournis à titre de référence pour la recherche et ne constituent pas un avis médical. Toute piste de repositionnement doit être validée cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

