---
layout: default
title: Rifabutin
parent: Preuves élevées (L1-L2)
nav_order: 665
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Rifabutin : nouvelle indication prédite, Infection par le VIH (contexte des infections opportunistes) (niveau de preuve L1). Indication d'origine : Non renseignée dans l'AMM française"
monitor_inn: "rifabutin"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "sclerosing cholangitis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "conjunctivitis", "leprosy", "endocarditis", "pneumocystosis", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
---

# Rifabutin
{: .fs-9 }

Niveau de preuve: **L1** | Indications prédites: **10** 
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

# Rifabutine : D'une indication non documentée à l'infection par le VIH

## Résumé en Une Phrase

La rifabutine est un antibiotique de la famille des rifamycines, utilisé contre les infections à mycobactéries. Les données compilées pour ce rapport ne précisent pas son indication originale, car le texte d'indication de l'AMM française est vide.
Le modèle TxGNN la prédit comme potentiellement utile dans l'**infection par le VIH**, avec **34 essais cliniques** et **20 publications** associés. Il s'agit en pratique du contexte des infections opportunistes liées au VIH (complexe *Mycobacterium avium* et tuberculose), et non d'une activité antirétrovirale directe.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans l'AMM française |
| Nouvelle Indication Prédite | Infection par le VIH (contexte des infections opportunistes) |
| Score de Prédiction TxGNN | 99,88 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Uniquement annulée |
| Nombre d'AMM | 1 |
| Décision Recommandée | Proceed with Guardrails |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. D'après les connaissances établies, la rifabutine est une rifamycine qui inhibe l'ARN polymérase ADN-dépendante bactérienne (rpoB). Elle n'est pas un antirétroviral.

Son intérêt chez les personnes vivant avec le VIH tient à la prévention et au traitement des infections mycobactériennes opportunistes (complexe *M. avium* et tuberculose). Comparée à la rifampicine, elle est un inducteur plus faible du CYP3A4. Elle est donc privilégiée lorsqu'elle est associée à des inhibiteurs de protéase.

Le score élevé du modèle reflète donc un contexte d'infections associées au VIH, et non une action directe sur le virus. Cette nuance est essentielle pour interpréter la prédiction.

## Preuves d'Essais Cliniques

Parmi les essais compilés, voici les plus pertinents (10 sur 34) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | Terminé | 400 | Quatre schémas (clarithromycine à deux doses + éthambutol, avec rifabutine ou clofazimine) dans le MAC disséminé du SIDA |
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | Terminé | 450 | Clarithromycine/éthambutol avec rifabutine (450 mg ou 300 mg) ou placebo dans la bactériémie à MAC |
| [NCT00001995](https://clinicaltrials.gov/study/NCT00001995) | Non applicable | Terminé | 200 | Essai randomisé en double aveugle d'un schéma contenant de la rifabutine dans la bactériémie à MAC |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | Terminé | 1100 | Clarithromycine vs rifabutine vs association pour prévenir le MAC (CD4 ≤ 100) |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | Terminé | 720 | Azithromycine et rifabutine, seules ou associées, pour prévenir le MAC disséminé |
| [NCT00002267](https://clinicaltrials.gov/study/NCT00002267) | Non applicable | Terminé | 750 | Rifabutine en monothérapie vs placebo pour prévenir la bactériémie à MAC (CD4 ≤ 200) |
| [NCT00023361](https://clinicaltrials.gov/study/NCT00023361) | Non applicable | Terminé | 215 | Schéma intermittent à base de rifabutine dans la tuberculose liée au VIH |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | Terminé | 47 | Pharmacocinétique de la rifabutine avec traitement antirétroviral, tuberculose/VIH (Vietnam) |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Phase 2 | Terminé | 48 | Étude pharmacocinétique parallèle en Afrique du Sud |
| [NCT01601626](https://clinicaltrials.gov/study/NCT01601626) | Phase 2 | Arrêté | 71 | Lopinavir/ritonavir à double dose avec rifampicine vs dose standard avec rifabutine, tuberculose/VIH |

Une grande partie des autres essais sont des études d'interactions pharmacocinétiques avec des antirétroviraux. Les études de phase 3 sont anciennes (années 1990) et portent surtout sur les infections à MAC.

## Preuves de la Littérature

Parmi les 20 publications compilées, voici les plus pertinentes :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohorte | J Antimicrob Chemother | Pharmacocinétique et sécurité de la rifabutine chez des enfants co-infectés TB/VIH ; une étude antérieure avait été arrêtée pour neutropénie sévère |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohorte | J Antimicrob Chemother | Sécurité et efficacité chez les enfants sous lopinavir/ritonavir ; neutropénie limitant le traitement |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | Modélisation PK | Br J Clin Pharmacol | Interaction rifabutine-dolutégravir |
| [21819645](https://pubmed.ncbi.nlm.nih.gov/21819645/) | 2012 | Revue | Int J Tuberc Lung Dis | La rifabutine peut remplacer la rifampicine avec les inhibiteurs de protéase |
| [17181373](https://pubmed.ncbi.nlm.nih.gov/17181373/) | 2006 | Revue | Drugs | Approche thérapeutique pratique de la co-infection TB/VIH |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Revue | Microbiol Spectr | Tuberculose associée à l'infection par le VIH |
| [10456381](https://pubmed.ncbi.nlm.nih.gov/10456381/) | 1999 | Revue | Drug Saf | Rapport bénéfice-risque des traitements des infections à MAC |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Revue | BMJ Clin Evid | Prophylaxie primaire et secondaire des infections opportunistes liées au VIH |
| [11996607](https://pubmed.ncbi.nlm.nih.gov/11996607/) | 2002 | Revue | Arch Intern Med | Mise à jour des interactions de la rifampicine et de la rifabutine |
| [39037240](https://pubmed.ncbi.nlm.nih.gov/39037240/) | 2024 | PK de population | Antimicrob Agents Chemother | Pharmacocinétique et optimisation de la dose chez l'enfant sous lopinavir/ritonavir |

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67699269 | ANSATIPINE 150 mg, gélule (SERB) | Gélule | Non renseignée (AMM annulée) |

## Cytotoxicité

Cette section est omise : la rifabutine est un antibiotique et non un antinéoplasique.

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances (non issues de la notice)** : thrombopénie, neutropénie, agranulocytose, colite à *Clostridium difficile*, entérocolite nécrosante périnatale.
- **Interactions médicamenteuses** : 163 interactions recensées. Parmi celles présentées, une est majeure (éliglustat). La plupart sont modérées : doxycycline, hydrocortisone, dexaméthasone, bétaméthasone, triamcinolone, clarithromycine, métronidazole, morphine, aprépitant, pioglitazone, saxagliptine, linagliptine, chlorpropamide, acétohexamide, cholécalciférol, calcifédiol, calcitriol et acide picosulfurique. Une est mineure (dolasétron). Un ajustement de dose est nécessaire avec de nombreux antirétroviraux.
- **Points d'attention issus des données** : neutropénie sévère observée chez l'enfant avec les inhibiteurs de protéase, et risque d'uvéite, notamment en association avec la clarithromycine ou l'itraconazole.

Les mises en garde et contre-indications de la notice n'ont pas pu être récupérées. Veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais randomisés de phase 3 soutiennent l'usage de la rifabutine dans les infections à MAC et la tuberculose chez les personnes vivant avec le VIH. L'indication est cependant à lire comme une prise en charge des infections opportunistes, sans effet antirétroviral. L'AMM française est annulée et les essais pivots sont anciens.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer et analyser la notice de l'ANSM (mises en garde et contre-indications), ce qui bloque le criblage de sécurité.
- Obtenir les données de mécanisme d'action détaillées depuis DrugBank.
- Clarifier l'indication originale de la rifabutine et son statut réglementaire actuel en France.
- Établir un plan de surveillance : numération formule sanguine (neutropénie), examen ophtalmologique (uvéite) et gestion des interactions avec les antirétroviraux, notamment chez l'enfant.

Les autres indications prédites (neoplasie endocrinienne multiple, cholangite sclérosante, trouble neurodéveloppemental rare, conjonctivite, endocardite, pneumocystose, SIDA félin, infection par le virus de l'immunodéficience simienne) relèvent de la décision Hold, avec un niveau de preuve L4-L5. La lèpre est classée comme question de recherche (L4), avec uniquement des données in vitro et animales.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

