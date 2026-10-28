---
layout: default
title: Epinephrine
parent: Prédiction du modèle uniquement (L5)
nav_order: 287
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
monitor_inn: "epinephrine"
predicted_indications: ["obstructive lung disease", "Rienhoff syndrome", "respiratory malformation"]
description: "Epinephrine : nouvelle indication prédite, Maladie pulmonaire obstructive (obstructive lung disease) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données locales"
---

# Epinephrine
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **3** 
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

## Epinephrine: Maladie pulmonaire obstructive (obstructive lung disease)
{: .text-alpha }

## Résumé en Une Phrase

L'épinéphrine (adrénaline) est un agoniste adrénergique utilisé à l'origine dans l'anaphylaxie, l'asthme, la bronchite, l'emphysème pulmonaire, les troubles hypotensifs et le glaucome à angle ouvert.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie pulmonaire obstructive**.
Les données compilées pour ce rapport font état de **15 essais cliniques** (dont 4 essais de Phase 3 terminés) et de **20 publications** autour de cette direction.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Maladie pulmonaire obstructive (obstructive lung disease) |
| Score de Prédiction TxGNN | 0.9971 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | 20 (toutes annulées) |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les sources compilées. Sur la base des connaissances pharmacologiques établies, l'épinéphrine est un agoniste adrénergique non sélectif : l'activation des récepteurs bêta-2 relâche la musculature lisse bronchique, et l'activation alpha-1 réduit l'œdème de la muqueuse des voies respiratoires par vasoconstriction.

Ce mécanisme est cohérent avec les indications d'origine (asthme, bronchite, emphysème, bronchectasie). La « maladie pulmonaire obstructive » regroupe notamment l'asthme et la BPCO ; la prédiction est donc en grande partie une extension d'usages déjà établis. Le score élevé (0,9971) concorde avec les preuves cliniques existantes. L'incertitude de repositionnement concerne surtout la bronchiolite du nourrisson, pour laquelle les résultats sont plus hétérogènes.

## Preuves d'Essais Cliniques

Parmi les 15 essais compilés, voici les 10 plus pertinents :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT01357642](https://clinicaltrials.gov/study/NCT01357642) | Phase 3 | Terminé | 373 | Efficacité et sécurité sur 12 semaines de l'épinéphrine inhalée (HFA-MDI) vs placebo et Primatene Mist chez des asthmatiques adolescents et adultes |
| [NCT01476904](https://clinicaltrials.gov/study/NCT01476904) | Phase 3 | Terminé | 208 | Extension de sécurité de 3 mois (profil de sécurité à 6 mois) de l'épinéphrine inhalée vs placebo dans l'asthme |
| [NCT01460511](https://clinicaltrials.gov/study/NCT01460511) | Phase 3 | Terminé | 70 | Efficacité et sécurité de E004 sur 4 semaines vs placebo chez des enfants asthmatiques de 4 à 11 ans |
| [NCT01737905](https://clinicaltrials.gov/study/NCT01737905) | Phase 3 | Terminé | 28 | Dose unique de E004 chez des enfants asthmatiques (essai croisé, double aveugle, contrôlé par placebo) |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Phase 4 | Terminé | 49 | Épinéphrine intramusculaire en appoint des bronchodilatateurs inhalés dans l'exacerbation sévère d'asthme pédiatrique |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Phase 4 | Terminé | 120 | Épinéphrine, dexaméthasone et sérum salé hypertonique dans la bronchiolite de l'enfant (étude pilote randomisée) |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Phase 4 | Inconnu | 500 | Traitement inhalé optimal chez les nourrissons de 0 à 12 mois atteints de bronchiolite aiguë |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | Non applicable | Inconnu | 600 | Épinéphrine vs salbutamol dans la bronchiolite |
| [NCT00622817](https://clinicaltrials.gov/study/NCT00622817) | Non applicable | Terminé | 65 | Épinéphrine inhalée vs gouttes nasales de xylométazoline dans la bronchiolite |
| [NCT02585531](https://clinicaltrials.gov/study/NCT02585531) | Phase 2 | Inconnu | 100 | Épinéphrine, dexaméthasone et sérum salé hypertonique dans la bronchiolite de l'enfant |

Les autres essais compilés sont des études pharmacocinétiques chez des volontaires sains ou des études dont l'épinéphrine n'est pas l'intervention principale ; elles n'apportent pas de preuve d'efficacité.

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33893229](https://pubmed.ncbi.nlm.nih.gov/33893229/) | 2021 | Méta-analyse en réseau | Pediatrics | Efficacité comparée des interventions dans la bronchiolite en soins aigus |
| [35093318](https://pubmed.ncbi.nlm.nih.gov/35093318/) | 2022 | ECR | The Journal of Pediatrics | Corticoïdes systémiques et épinéphrine nébulisée vs soins standard chez des enfants en soins intensifs pour bronchiolite (durée du support en pression positive) |
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Épinéphrine dans la bronchiolite |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Revue systématique (Cochrane) | Cochrane Database Syst Rev | Épinéphrine dans la bronchiolite ; les bronchodilatateurs apportent un bénéfice modeste à court terme dans les formes légères à modérées |
| [35953216](https://pubmed.ncbi.nlm.nih.gov/35953216/) | 2022 | Revue | Emerg Med Clin North Am | Évaluation et prise en charge des exacerbations d'asthme et de BPCO aux urgences |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Revue | Expert Rev Respir Med | Rôle de l'épinéphrine racémique, des corticoïdes, du sérum salé hypertonique et de l'oxygénothérapie à haut débit dans la bronchiolite |
| [21157348](https://pubmed.ncbi.nlm.nih.gov/21157348/) | 2011 | Revue | Curr Opin Pediatr | Mise à jour sur la prise en charge de la bronchiolite : aucun traitement n'a montré de modification conclusive de l'évolution |
| [20876171](https://pubmed.ncbi.nlm.nih.gov/20876171/) | 2010 | Analyse coût-efficacité | Pediatrics | Rapport coût-efficacité de l'épinéphrine et de la dexaméthasone dans la bronchiolite |

## Informations de Marché en France

Le texte d'indication approuvée n'est pas renseigné. Voici les 5 premières :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 61846627 | EPIPEN 0,15 mg/0,3 ml, stylo pré-rempli | Solution injectable | Non renseignée |
| 69549631 | EMERADE 300 microgrammes, stylo prérempli | Solution injectable | Non renseignée |
| 61072758 | ADRENALINE AGUETTANT 1 mg/ml, ampoule | Solution injectable | Non renseignée |
| 69556177 | ADRENALINE RENAUDIN 0,50 mg/mL | Solution injectable | Non renseignée |
| 66305127 | ADRENALINUM BOIRON (2CH à 30CH ou 4DH à 60DH) | Comprimé, solution, granules, poudre et pommade | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : hypertension, maladies cardiovasculaires et cardiaques (infarctus du myocarde, maladie coronarienne, fibrillation auriculaire, troubles de la conduction, arrêt cardiaque soudain), glaucome à angle fermé, hyperthyroïdie, diabète et acidocétose diabétique, insuffisance hépatique, maladie rénale, épilepsie, hyperplasie bénigne de la prostate, insuffisance respiratoire, myasthénie grave, entre autres.
- **Interactions médicamenteuses** : 385 interactions recensées. Parmi les principales, de niveau **majeur** : l'amitriptyline et l'amoxapine (antidépresseurs tricycliques). De niveau modéré : bêtabloquants (aténolol, acébutolol, bétaxolol), bêta-2 agonistes (salbutamol, formotérol, arformotérol), stimulants (méthylphénidate, amphétamine, atomoxétine), antidiabétiques (acarbose, alogliptine, acétohexamide, albiglutide) et antipsychotiques (aripiprazole, asénapine, amisulpride).

Les mises en garde et contre-indications de la notice ne sont pas disponibles dans les données compilées ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
Plusieurs essais de Phase 3 terminés (épinéphrine inhalée dans l'asthme chez l'adulte et l'enfant) et des revues systématiques soutiennent l'usage dans les maladies obstructives, ce qui correspond à un niveau de preuve L1. La prédiction relève surtout d'une extension d'usages établis, mais le profil cardiovasculaire et les nombreuses interactions imposent des garde-fous.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice officielle (ANSM) pour les mises en garde et contre-indications, ce point bloquant empêchant le passage au dépistage de sécurité
- Obtenir les données détaillées sur le mécanisme d'action (DrugBank)
- Clarifier le statut réglementaire en France, le médicament étant commercialisé avec 20 AMM valides, et la voie d'administration visée (inhalée vs injectable)
- Définir un plan de surveillance cardiovasculaire et de gestion des interactions (tricycliques, bêtabloquants)
- Confirmer les résultats dans la bronchiolite et la BPCO, où les preuves restent hétérogènes
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

