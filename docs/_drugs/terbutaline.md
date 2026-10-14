---
layout: default
title: Terbutaline
parent: Preuves élevées (L1-L2)
nav_order: 743
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

# Terbutaline : De l'asthme à la maladie pulmonaire obstructive

## Resume en Une Phrase

Terbutaline est un bronchodilatateur bêta-2 agoniste, initialement utilisé pour traiter l'asthme, la bronchite et l'emphysème pulmonaire.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **maladie pulmonaire obstructive**, avec **14 essais cliniques** et **20 publications** soutenant actuellement cette direction.
Cette prédiction recoupe toutefois largement les indications déjà connues du médicament : il s'agit davantage d'une indication cohérente avec l'usage existant que d'un véritable repositionnement.

---

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Asthme (selon le graphe de connaissances ; le texte d'indication de l'AMM n'est pas renseigné) |
| Nouvelle Indication Predite | Maladie pulmonaire obstructive |
| Score de Prediction TxGNN | 99,96 % |
| Niveau de Preuve | L1 |
| Statut de Marche en France | Uniquement des AMM annulées |
| Nombre d'AMM | 1 |
| Decision Recommandee | Proceed with Guardrails |

---

## Pourquoi Cette Prediction est-elle Raisonnable ?

Les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées pour ce rapport. D'après les connaissances pharmacologiques générales, la terbutaline est un agoniste sélectif des récepteurs bêta-2 adrénergiques. Elle relâche le muscle lisse bronchique via la voie de l'AMPc et provoque ainsi une bronchodilatation.

Ce mécanisme est directement pertinent pour les maladies obstructives des voies respiratoires. L'asthme, la bronchite et l'emphysème figurent déjà parmi les indications d'origine du médicament. Le score très élevé de TxGNN (99,96 %) est donc cohérent avec une pharmacologie déjà connue, et non avec une découverte inattendue.

Les autres prédictions du modèle sont beaucoup moins solides. La « malformation respiratoire » (score 99,5 %) ne repose sur aucun lien mécanistique clair : la bronchodilatation ne traite pas un défaut de développement structurel, et le score semble refléter la proximité du réseau avec l'asthme. Le « syndrome de Rienhoff » (99,4 %) n'a ni essai ni publication, et reste une prédiction purement computationnelle.

---

## Preuves d'Essais Cliniques

La terbutaline est le plus souvent le comparateur ou le traitement de secours dans ces essais, et non le produit expérimental. Les essais ci-dessous sont classés par pertinence.

| Numero d'Essai | Phase | Statut | Inscription | Resultats Principaux |
|---------|------|------|------|---------|
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Phase 3 | Terminé | 4215 | Symbicort à la demande vs budésonide deux fois par jour + terbutaline à la demande dans l'asthme léger |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Phase 3 | Terminé | 3850 | Symbicort à la demande vs terbutaline à la demande vs budésonide + terbutaline dans l'asthme |
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Phase 3 | Terminé | 120 | Sulfate de magnésium IV vs terbutaline chez l'enfant en exacerbation aiguë d'asthme |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Phase 3 | Terminé | 860 | Budésonide/formotérol à la demande vs régulier + terbutaline à la demande dans l'asthme persistant léger à modéré |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | Terminé | 2091 | Symbicort SMART vs Symbicort + terbutaline 0,4 mg à la demande dans l'asthme |
| [NCT00259766](https://clinicaltrials.gov/study/NCT00259766) | Phase 3 | Terminé | 1970 | Étude en vie réelle des coûts de santé : Symbicort vs association libre + Bricanyl à la demande |
| [NCT00252863](https://clinicaltrials.gov/study/NCT00252863) | Phase 3 | Terminé | 1600 | Symbicort en traitement unique (SMART) vs meilleure pratique conventionnelle dans l'asthme persistant |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Phase 3 | Terminé | 95 | Étude pharmacodynamique croisée de Bricanyl Turbuhaler M3 vs M2 sur la bronchoconstriction induite par la méthacholine |
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Phase 3 | Terminé | 24 | Efficacité relative de la terbutaline Turbuhaler 0,4 mg vs salbutamol pMDI chez des adultes japonais asthmatiques |
| [NCT00837967](https://clinicaltrials.gov/study/NCT00837967) | Phase 3 | Terminé | 25 | Comparaison de la tolérance de 10 inhalations de Symbicort vs terbutaline chez des adultes japonais asthmatiques |

Un essai de phase 2/3 sur la relation exposition-réponse de la terbutaline ([NCT04973345](https://clinicaltrials.gov/study/NCT04973345)) a été retiré avec 0 participant et n'apporte aucune preuve.

---

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [29768149](https://pubmed.ncbi.nlm.nih.gov/29768149/) | 2018 | ECR | N Engl J Med | Budésonide-formotérol à la demande comme alternative aux stratégies conventionnelles dans l'asthme léger |
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | ECR | Acad Emerg Med | Terbutaline nébulisée + ipratropium vs terbutaline seule dans l'exacerbation aiguë de BPCO sous ventilation non invasive |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | ECR | Br J Dis Chest | La terbutaline orale augmente la force du diaphragme dans la BPCO (double aveugle, croisé) |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | ECR | Int J Clin Pharmacol Ther Toxicol | Clenbutérol vs terbutaline orale dans la bronchopneumopathie obstructive chronique |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | ECR croisé | Lung | Effet d'une dose unique de terbutaline (Turbuhaler) sur la fonction pulmonaire et la capacité d'effort dans la BPCO |
| [36227333](https://pubmed.ncbi.nlm.nih.gov/36227333/) | 2023 | Revue systématique | Naunyn Schmiedebergs Arch Pharmacol | Pharmacocinétique clinique de la terbutaline chez l'humain |
| [23348973](https://pubmed.ncbi.nlm.nih.gov/23348973/) | 2013 | Revue | Am J Respir Crit Care Med | Les bêta-2 agonistes à courte durée d'action, dont la terbutaline, soulagent rapidement les symptômes |
| [33065789](https://pubmed.ncbi.nlm.nih.gov/33065789/) | 2020 | Étude clinique | Ann Palliat Med | N-acétylcystéine associée au sulfate de terbutaline chez le sujet âgé atteint de BPCO |
| [2951811](https://pubmed.ncbi.nlm.nih.gov/2951811/) | 1986 | Étude randomisée | Respiration | Fénotérol-ipratropium vs terbutaline dans la bronchopneumopathie obstructive chronique |
| [2031046](https://pubmed.ncbi.nlm.nih.gov/2031046/) | 1991 | Étude croisée randomisée | Pneumologie | Terbutaline nébulisée et pression expiratoire positive dans la BPCO |

---

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 60961427 | BRICANYL TURBUHALER 500 microgrammes/dose, poudre pour inhalation (AstraZeneca) | Poudre pour inhalation | Non renseignée (AMM annulée) |

---

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (ce ne sont pas les termes de la notice) : hypertension, épilepsie, hyperglycémie, diabète et acidocétose diabétique, carence en potassium, arrêt cardiaque subit, troubles de la conduction cardiaque, insuffisance respiratoire, hyperthyroïdie (maladie de Basedow, thyrotoxicose), œdème pulmonaire, ischémie myocardique, maladie coronarienne et décollement placentaire.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les principales :
  - Modérées : épinéphrine, antidiabétiques (acarbose, alogliptine, pioglitazone, canagliflozine, chlorpropamide, albiglutide), famotidine, clarithromycine, lopéramide, isométheptène, laxatifs (bisacodyl, acide picosulfurique, polyéthylène glycol avec électrolytes).
  - Mineures : corticoïdes (hydrocortisone, triamcinolone, dexaméthasone, bêtaméthasone, béclométasone, budésonide).

Les mises en garde et contre-indications de la notice ne sont pas disponibles. Veuillez consulter la notice pour ces informations.

---

## Conclusion et Prochaines Etapes

**Decision : Proceed with Guardrails**

**Justification :**
- De nombreux essais de phase 3 et des ECR publiés confirment l'utilité de la terbutaline dans les maladies obstructives des voies respiratoires (asthme, BPCO), mais cette indication recoupe l'usage déjà connu. Dans la plupart des essais, elle est comparateur ou traitement de secours. Les prédictions secondaires (malformation respiratoire, syndrome de Rienhoff) ne sont pas étayées et relèvent de la décision « Hold ».

**Pour avancer, les elements suivants sont necessaires :**
- Les mises en garde et contre-indications de la notice ANSM (données bloquantes pour l'évaluation de sécurité)
- Les données détaillées sur le mécanisme d'action (DrugBank)
- La clarification du statut réglementaire en France, la seule AMM étant annulée
- Un plan de surveillance cardiovasculaire, métabolique (glycémie, kaliémie) et thyroïdien pour les populations à risque
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

