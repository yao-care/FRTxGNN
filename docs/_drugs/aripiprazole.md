---
layout: default
title: Aripiprazole
parent: Preuves élevées (L1-L2)
nav_order: 43
evidence_level: L1
indication_count: 10
---

# Aripiprazole
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

# Aripiprazole : De l'Antipsychotique Atypique au Trouble Affectif Majeur

## Résumé en Une Phrase

L'aripiprazole est un antipsychotique atypique. Les données ANSM fournies ne précisent pas son indication d'origine.
Le modèle TxGNN prédit qu'il pourrait être efficace pour le **trouble affectif majeur** (dépression majeure),
avec **50 essais cliniques** enregistrés (dont plusieurs essais de Phase 3 terminés en traitement adjuvant) et **20 publications** associés à cette direction.
Cette indication correspond probablement à un usage déjà reconnu de l'aripiprazole (traitement adjuvant de la dépression) plutôt qu'à un repositionnement véritablement nouveau.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données ANSM (texte d'indication vide pour toutes les AMM) |
| Nouvelle Indication Prédite | Trouble affectif majeur (major affective disorder) |
| Score de Prédiction TxGNN | 99,62 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | ✓ Commercialisé |
| Nombre d'AMM | 20 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

La donnée officielle sur le mécanisme d'action (DrugBank) n'est pas disponible dans le dossier. La littérature fournie décrit toutefois l'aripiprazole comme un agoniste partiel des récepteurs dopaminergiques D2/D3 et sérotoninergique 5-HT1A, et comme un antagoniste des récepteurs 5-HT2A (revue PMID 21254788). Ce profil explique plausiblement son effet d'appoint dans la dépression et son effet stabilisateur de l'humeur dans le trouble bipolaire.

Les essais de Phase 3 portent sur l'aripiprazole ajouté à un antidépresseur chez des patients répondant insuffisamment au traitement antidépresseur seul. Cette utilisation est cohérente avec l'usage déjà décrit dans la littérature, où l'aripiprazole figure parmi les antipsychotiques de deuxième génération approuvés comme traitement adjuvant du trouble dépressif majeur (PMID 25963405).

Comme aucune indication d'origine n'est renseignée dans les données, la prédiction est probablement conforme à l'AMM plutôt que nouvelle. Il faut la confronter au RCP réel avant de la présenter comme une découverte.

## Preuves d'Essais Cliniques

Sur les 50 essais enregistrés, 10 parmi les plus pertinents sont listés ci-dessous. Les résumés sont ceux des fiches d'enregistrement : ils décrivent l'objectif des études, pas leurs résultats. Le statut « Terminé » ne signifie pas que l'essai est positif.

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00683852](https://clinicaltrials.gov/study/NCT00683852) | Phase 3 | Terminé | 225 | Aripiprazole en adjuvant d'un antidépresseur contre placebo (double aveugle) chez des patients déprimés répondant insuffisamment ; évaluation d'une dose réduite |
| [NCT00105196](https://clinicaltrials.gov/study/NCT00105196) | Phase 3 | Terminé | 349 | Aripiprazole contre placebo en adjuvant d'un antidépresseur, sur 14 semaines, après réponse incomplète |
| [NCT00876343](https://clinicaltrials.gov/study/NCT00876343) | Phase 3 | Terminé | 586 | Aripiprazole contre placebo en adjuvant d'un ISRS ou IRSN dans le trouble dépressif majeur |
| [NCT02046564](https://clinicaltrials.gov/study/NCT02046564) | Phase 3 | Terminé | 412 | Association aripiprazole/sertraline (ASC-01) contre sertraline seule chez des patients répondant incomplètement |
| [NCT01111552](https://clinicaltrials.gov/study/NCT01111552) | Phase 3 | Arrêté | 237 | Association aripiprazole/escitalopram en double aveugle ; arrêt anticipé, donc soutien partiel seulement |
| [NCT01111539](https://clinicaltrials.gov/study/NCT01111539) | Phase 3 | Arrêté | 211 | Même schéma d'association aripiprazole/escitalopram ; arrêt anticipé |
| [NCT00953745](https://clinicaltrials.gov/study/NCT00953745) | Non applicable | Terminé | 43 | Étude d'imagerie (TEP/IRMf) de l'effet dopaminergique de l'aripiprazole adjuvant dans la dépression résistante ; étude mécanistique, pas d'efficacité |
| [NCT00873795](https://clinicaltrials.gov/study/NCT00873795) | Non applicable | Terminé | 41 | Aripiprazole 2,5 mg + sertraline 50 mg dans la dépression majeure récente ; petite étude |
| [NCT01429831](https://clinicaltrials.gov/study/NCT01429831) | Phase 4 | Terminé | 300 | Étude observationnelle à Taïwan sur l'efficacité et la tolérance de l'aripiprazole en appoint |
| [NCT07153406](https://clinicaltrials.gov/study/NCT07153406) | Phase 3 | Pas encore en recrutement | 220 | Eskétamine contre aripiprazole (avec ISRS/IRSN) dans la dépression résistante du sujet âgé (>60 ans) |

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [36239033](https://pubmed.ncbi.nlm.nih.gov/36239033/) | 2023 | ECR | J Psychopharmacol | Essai randomisé contre placebo de l'aripiprazole adjuvant dans la dépression majeure avec symptômes somatiques, avec données EEG (résultats non détaillés dans l'extrait fourni) |
| [38669232](https://pubmed.ncbi.nlm.nih.gov/38669232/) | 2024 | Revue systématique / méta-analyse d'ECR | PLoS One | Efficacité et sécurité de l'augmentation ou du changement de traitement par aripiprazole ou bupropion dans la dépression résistante ou le trouble dépressif majeur |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Revue systématique / méta-analyse en réseau | J Affect Disord | Comparaison de l'efficacité et des arrêts de traitement entre agents d'augmentation dans la dépression résistante |
| [38219278](https://pubmed.ncbi.nlm.nih.gov/38219278/) | 2024 | Revue systématique / méta-analyse en réseau | Neuropsychopharmacol Rep | Comparaison brexpiprazole, aripiprazole et placebo chez des patients japonais avec dépression majeure |
| [34167174](https://pubmed.ncbi.nlm.nih.gov/34167174/) | 2021 | Revue systématique / méta-analyse | Prim Care Companion CNS Disord | Efficacité et tolérance à long terme (≥ 6 mois) de l'aripiprazole adjuvant ; critère principal : rémission |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Revue systématique / méta-analyse | Psychol Med | Efficacité et tolérance des antipsychotiques en monothérapie ou en appoint dans la dépression majeure de l'adulte |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Revue systématique / méta-analyse | J Psychopharmacol | Traitements d'augmentation et associations dans la dépression résistante de stade précoce |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Revue / méta-analyse | J Psychopharmacol | Antidépresseur + antipsychotique de 2e génération contre eskétamine contre lithium dans la dépression majeure |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | Revue | Psychiatr Clin North Am | Pharmacothérapie de la dépression résistante ; les antipsychotiques atypiques, dont l'aripiprazole, sont les agents d'augmentation les plus étudiés |
| [21254788](https://pubmed.ncbi.nlm.nih.gov/21254788/) | 2011 | Revue | CNS Drugs | Aperçu des données d'essais sur l'aripiprazole adjuvant dans la dépression et justification pharmacologique |

## Informations de Marché en France

Cinq des 20 AMM sont présentées. D'autres formes existent, notamment une suspension injectable à libération prolongée.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 66950163 | ARIPIPRAZOLE ZYDUS 10 mg (ZYDUS FRANCE) | Comprimé | Non précisée dans les données |
| 68190271 | ARIPIPRAZOLE EVOLUGEN 5 mg (EVOLUPHARM) | Comprimé | Non précisée dans les données |
| 69675822 | ARIPIPRAZOLE BGR 10 mg (BIOGARAN) | Comprimé | Non précisée dans les données |
| 67941085 | ARIPIPRAZOLE TEVA 15 mg (TEVA SANTE) | Comprimé orodispersible | Non précisée dans les données |
| 68349332 | ARIPIPRAZOLE ZYDUS 5 mg (ZYDUS FRANCE) | Comprimé | Non précisée dans les données |

## Considérations de Sécurité

Veuillez consulter la notice pour les informations de sécurité.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de Phase 3 terminés (NCT00683852, NCT00105196, NCT00876343, NCT02046564) et des méta-analyses soutiennent l'usage adjuvant de l'aripiprazole dans la dépression majeure, ce qui justifie le niveau L1.
- Les données de sécurité de l'ANSM sont absentes (lacune bloquante), et l'indication d'origine est inconnue, donc rien ne permet de dire s'il s'agit d'un vrai repositionnement.

**Pour avancer, les éléments suivants sont nécessaires :**
- Télécharger et analyser la notice/RCP ANSM (mises en garde, contre-indications, interactions) et confirmer si l'indication est déjà couverte par l'AMM.
- Renseigner l'indication d'origine et le mécanisme d'action officiel (DrugBank).
- Examiner les résultats publiés des essais de Phase 3, en particulier les essais arrêtés avec l'association aripiprazole/escitalopram.

**Autres prédictions :** parmi les autres pistes, seule la trichotillomanie (niveau L3, essai de Phase 2 pas encore en recrutement) a un début de preuve. Les publications signalent aussi que l'aripiprazole peut induire des comportements impulsifs-compulsifs, ce qui impose de peser ce risque. Les autres prédictions sont limitées au modèle (L5) et restent en Hold.

*Ces résultats sont fournis à titre de recherche uniquement et ne constituent pas un avis médical. Tout candidat au repositionnement doit être validé cliniquement avant application.*
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

