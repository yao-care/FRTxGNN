---
layout: default
title: Felbamate
parent: Preuves modérées (L3-L4)
nav_order: 318
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "FELBAMATE"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
description: "Felbamate : nouvelle indication prédite, Trigeminal nerve neoplasm (niveau de preuve L4). Indication d'origine : Non renseignée dans les données locales"
---

# Felbamate
{: .fs-9 }

Niveau de preuve: **L4** | Indications prédites: **2** 
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

## Felbamate: Trigeminal nerve neoplasm
{: .text-alpha }

## Resume en Une Phrase

Felbamate est un antiépileptique, initialement utilisé pour traiter l'épilepsie (y compris l'épilepsie partielle et le syndrome de Lennox-Gastaut).
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **névralgie du trijumeau**, avec **aucun essai clinique** et **4 publications** (dont un seul rapport de cas directement pertinent) à ce jour.

Une première prédiction, le **néoplasme du nerf trijumeau** (score de 0,9962), n'est étayée par aucune donnée et n'est pas retenue comme piste. Ce rapport se concentre donc sur la névralgie du trijumeau, seconde prédiction et seule à disposer d'un début de littérature.

## Apercu Rapide

| Element | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Predite | Trigeminal nerve neoplasm |
| Score de Prediction TxGNN | 0.9962 |
| Niveau de Preuve | L4 |
| Statut de Marche en France | Commercialisé (autorisations valides : 2 sur 2) |
| Nombre d'AMM | 2 (valides : 2) |
| Decision Recommandee | Hold |

## Pourquoi Cette Prediction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les données compilées pour ce rapport. Sur la base des connaissances générales, le felbamate est un antiépileptique dont l'action est classiquement attribuée à l'antagonisme du site glycine du récepteur NMDA et à la potentialisation GABAergique, avec d'éventuels effets sur les canaux sodiques. Ces éléments restent à confirmer par une source dédiée.

La névralgie du trijumeau est une douleur faciale paroxystique, unilatérale et intense, liée à une hyperexcitabilité neuronale. Son profil temporel proche de celui des crises a conduit à utiliser des anticonvulsivants : la carbamazépine est le traitement de référence, et le baclofène, la phénytoïne et le valproate sont également efficaces. Un lien mécanistique plausible existe donc entre l'indication d'origine (épilepsie) et la nouvelle indication.

Le seul signal clinique direct est un rapport de 1995 intitulé « Felbamate relieved trigeminal neuralgia ». Il s'agit d'un rapport de cas, donc d'une preuve anecdotique et non contrôlée.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Litterature

| PMID | Annee | Type | Revue | Resultats Principaux |
|------|-----|------|------|---------|
| [7549170](https://pubmed.ncbi.nlm.nih.gov/7549170/) | 1995 | Rapport de cas | Clin J Pain | Évaluation de l'efficacité analgésique du felbamate dans la névralgie du trijumeau ; le titre rapporte un soulagement |
| [23338129](https://pubmed.ncbi.nlm.nih.gov/23338129/) | 1997 | Revue | CNS Drugs | Guide de choix thérapeutique : carbamazépine en premier choix, baclofène, phénytoïne et valproate également efficaces |
| [22022008](https://pubmed.ncbi.nlm.nih.gov/22022008/) | 2011 | Préclinique (animal) | Indian J Pharmacol | Comparaison carbamazépine, gabapentine et lamotrigine dans la douleur neuropathique chez le rat ; le felbamate n'est cité que comme contexte |
| [7633024](https://pubmed.ncbi.nlm.nih.gov/7633024/) | 1995 | Rapport de cas (événement indésirable) | Ann Pharmacother | Anaphylaxie retardée induite par le felbamate (signal de sécurité) |

## Informations de Marche en France

| Numero d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvee |
|---------|------|------|-----------|
| 60223278 | TALOXA 600 mg, comprimé (ORGANON FRANCE) | Comprimé | Non renseignée (AMM active) |
| 62313468 | TALOXA 600 mg/5 ml, suspension buvable (ORGANON FRANCE) | Suspension buvable | Non renseignée (AMM active) |

## Considerations de Securite

- **Contre-indications issues du graphe de connaissances** (non issues de la notice) : syndrome du QT long (y compris familial), torsades de pointes, insuffisance hépatique et maladie du foie, anémie aplasique (dont idiopathique), maladies hématologiques, maladie rénale, porphyries (dont porphyries héréditaires), maladie de la vésicule biliaire, pyo-uretère, troubles anxieux, troubles névrotiques et dysthymie.
- **Risques graves connus du felbamate** : anémie aplasique et insuffisance hépatique. Un cas d'anaphylaxie retardée a également été rapporté (PMID 7633024).
- **Interactions médicamenteuses** : 100 interactions recensées, dont les premières sont de niveau modéré, notamment avec la morphine, l'opium, l'aprépitant, le métoclopramide, la naltrexone, le dronabinol, la nabilone, le répaglinide, la saxagliptine, la linagliptine, le rolapitant, l'éliglustat, la nitisinone, le naloxégol et plusieurs formes de vitamine D (cholécalciférol, calcifédiol, calcitriol, ergocalciférol, dihydrotachystérol).

Les mises en garde et contre-indications de la notice française n'ont pas pu être consultées ; veuillez vous référer à la notice.

## Conclusion et Prochaines Etapes

**Décision : Hold**

**Justification :**
- Le score TxGNN est très élevé, mais les preuves se limitent à un rapport de cas de 1995 et à du contexte indirect, sans aucun essai clinique (niveau L4). Le profil de risque du felbamate (anémie aplasique, hépatotoxicité) est défavorable alors que des alternatives plus sûres existent, et toutes ses AMM françaises sont annulées. La prédiction « néoplasme du nerf trijumeau » n'a aucune base et ne doit pas être poursuivie.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice (mises en garde et contre-indications) auprès de l'ANSM
- Compléter les données de mécanisme d'action via DrugBank
- Lire le texte intégral du rapport de 1995 et mener une revue systématique de la littérature
- Réaliser une analyse bénéfice-risque, limitée aux cas réfractaires avec surveillance hématologique et hépatique stricte
- Vérifier la disponibilité réelle du produit en France, compte tenu de l'annulation des AMM
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

