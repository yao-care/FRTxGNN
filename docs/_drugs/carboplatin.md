---
layout: default
title: Carboplatin
parent: Preuves élevées (L1-L2)
nav_order: 142
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Carboplatin : nouvelle indication prédite, Carcinome mammaire féminin (niveau de preuve L1). Indication d'origine : Cancer de l'ovaire"
---

# Carboplatin
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

# Carboplatine : Du Cancer de l'Ovaire au Carcinome Mammaire Féminin

## Résumé en Une Phrase

La carboplatine est un agent de chimiothérapie à base de platine, initialement utilisé pour le traitement du cancer de l'ovaire.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour le **carcinome mammaire féminin**, en particulier le cancer du sein triple négatif et les formes HER2-positives.
Les données compilées pour ce rapport comptent **40 essais cliniques** et **20 publications** soutenant cette direction, dont plusieurs essais randomisés de phase 3.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Cancer de l'ovaire (le texte d'indication des AMM françaises n'est pas renseigné ; indication issue du graphe de connaissances) |
| Nouvelle Indication Prédite | Carcinome mammaire féminin |
| Score de Prédiction TxGNN | 99,86 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Toutes les AMM sont abrogées ou annulées |
| Nombre d'AMM | 8 |
| Décision Recommandée | Proceed with Guardrails |

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la carboplatine est un agent alkylant de la classe des sels de platine, qui crée des pontages de l'ADN. Son efficacité dans le cancer de l'ovaire est établie, et mécanistiquement elle pourrait être applicable au cancer du sein.

Les tumeurs présentant un déficit de recombinaison homologue (associées à BRCA1/2 et de nombreux cancers du sein triple négatifs) sont particulièrement sensibles aux lésions de l'ADN induites par le platine. C'est le même mécanisme qui sous-tend l'activité du médicament dans le cancer de l'ovaire. Le syndrome héréditaire du cancer du sein et de l'ovaire figure d'ailleurs parmi les indications d'origine, ce qui renforce le lien entre les deux maladies.

Une réserve s'impose : les données compilées ne fournissent pour la littérature que les titres et résumés, de sorte que le design exact de chaque publication est déduit des titres et non vérifié. Par ailleurs, la liste d'essais contient surtout des essais de phase 1/2 pour cette indication, avec quelques essais de phase 3 où la carboplatine fait partie d'un schéma combiné.

---

## Preuves d'Essais Cliniques

Parmi les essais enregistrés, voici les plus pertinents (jusqu'à 10) :

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | Terminé | 148 | Carboplatine vs docétaxel dans le cancer du sein métastatique d'origine génétique (BRCA) |
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | Terminé | 3222 | AC-T, AC-TH et TCH (docétaxel, carboplatine, trastuzumab) en adjuvant dans le cancer du sein HER2+ |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | Terminé | 263 | Docétaxel + trastuzumab avec ou sans carboplatine en première ligne, cancer du sein avancé HER2+ |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Terminé | 961 | GeparOcto : deux approches néoadjuvantes intensifiées, dont une avec carboplatine, dans le cancer du sein précoce à haut risque |
| [NCT00616967](https://clinicaltrials.gov/study/NCT00616967) | Phase 2 | Actif, hors recrutement | 68 | Carboplatine + nab-paclitaxel avec ou sans vorinostat en préopératoire, cancer du sein HER2-négatif |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Phase 2 | Terminé | 45 | Bevacizumab, docétaxel et carboplatine en néoadjuvant dans le cancer du sein triple négatif |
| [NCT00003612](https://clinicaltrials.gov/study/NCT00003612) | Phase 2 | Terminé | 92 | Paclitaxel, carboplatine et trastuzumab en première ligne, cancer du sein métastatique HER2+ |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Phase 2 | En recrutement | 85 | Réponse au traitement et biomarqueurs dans le cancer du sein triple négatif (épirubicine + cyclophosphamide, puis docétaxel + carboplatine) |
| [NCT00669747](https://clinicaltrials.gov/study/NCT00669747) | Phase 2 | Inconnu | 45 | Carboplatine intracanalaire dans le carcinome canalaire in situ |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | Terminé | 103 | Olaparib + carboplatine chez les porteuses de mutations BRCA1/2 et dans le cancer du sein triple négatif |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | ECR (phase 2) | Lancet Oncol | GeparSixto : carboplatine néoadjuvant dans les cancers du sein triple négatifs et HER2+ |
| [29501363](https://pubmed.ncbi.nlm.nih.gov/29501363/) | 2018 | ECR (phase 3) | Lancet Oncol | BrighTNess : véliparib + carboplatine ou carboplatine seul en néoadjuvant, cancer du sein triple négatif |
| [35044810](https://pubmed.ncbi.nlm.nih.gov/35044810/) | 2022 | ECR (phase 2) | J Clin Oncol | CALGB 40603 : résultats à long terme avec carboplatine et bevacizumab dans le cancer du sein triple négatif |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | ECR (phase 2) | Clin Cancer Res | NeoSTOP : schémas néoadjuvants à base de carboplatine avec ou sans anthracycline |
| [41436191](https://pubmed.ncbi.nlm.nih.gov/41436191/) | 2025 | ECR (phase 3) | BMJ | CITRINE : chimiothérapie adjuvante intensifiée par carboplatine, cancer du sein triple négatif à haut risque |
| [41115255](https://pubmed.ncbi.nlm.nih.gov/41115255/) | 2026 | ECR (phase 3) | J Clin Oncol | Ajout de platine à la chimiothérapie néoadjuvante taxane-anthracycline, cancer du sein triple négatif |
| [42218963](https://pubmed.ncbi.nlm.nih.gov/42218963/) | 2026 | ECR (phase 3) | Ann Oncol | PEARLY : taxane + carboplatine vs anthracyclines puis taxane, cancer du sein triple négatif |
| [38492276](https://pubmed.ncbi.nlm.nih.gov/38492276/) | 2024 | Revue | Breast | Chimiothérapie à base de platine dans le cancer du sein triple négatif précoce |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | ECR (phase 2b) | Nat Commun | ARX788 + pyrotinib vs schéma standard TCbHP (avec carboplatine) dans le cancer du sein HER2+ |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Revue | Med Oncol | Association paclitaxel-carboplatine dans le cancer du sein avancé : synergie, efficacité et tolérance |

---

## Informations de Marché en France

Les 8 AMM recensées sont toutes au statut annulé ; aucune AMM valide n'est actuellement répertoriée. Le texte d'indication approuvée n'est pas disponible dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Statut |
|---------|------|------|-----------|
| 68513956 | CARBOPLATINE MEDAC 10 mg/mL | Solution à diluer pour perfusion | Annulée |
| 65676955 | CARBOPLATINE TEVA 10 mg/mL | Solution pour perfusion | Annulée |
| 66150794 | CARBOPLATINE HOSPIRA 10 mg/ml | Solution injectable pour perfusion | Annulée |
| 65210982 | CARBOPLATINE ARROW LAB 10 mg/mL | Solution à diluer pour perfusion | Annulée |
| 61095461 | CARBOPLATINE HIKMA 10 mg/mL | Solution à diluer pour perfusion | Annulée |

---

## Cytotoxicité

| Élément | Contenu |
|------|------|
| Classification de Cytotoxicité | Cytotoxique conventionnel (agent alkylant, classe des sels de platine) |
| Risque de Myélosuppression | Élevé (la thrombopénie, la neutropénie et l'anémie sont des toxicités limitantes ; ces affections figurent parmi les contre-indications du graphe de connaissances) |
| Classification d'Émétogénicité | Moyenne à élevée, selon la dose |
| Éléments de Surveillance | NFS avec formule (plaquettes, neutrophiles, hémoglobine), fonction rénale et hépatique, audition, signes de neuropathie périphérique |
| Protection de Manipulation | Doit suivre les règles de manipulation des médicaments cytotoxiques |

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie rénale, maladie hépatique, maladie de la vésicule biliaire, thrombopénie, neutropénie, agranulocytose, leucopénie, anémie, troubles de la coagulation, neuropathie périphérique, troubles de l'audition et perte de vision fonctionnelle.
- **Interactions médicamenteuses** : 488 interactions recensées. Parmi les principales, de niveau modéré : les aminosides (kanamycine, néomycine, streptomycine), la vancomycine, les inhibiteurs de la pompe à protons (oméprazole, ésoméprazole, lansoprazole, pantoprazole, rabéprazole, dexlansoprazole), le métronidazole, le tinidazole, la rosuvastatine et la simvastatine. La lévofloxacine est de niveau mineur. Les associations avec des médicaments néphrotoxiques ou ototoxiques (aminosides, vancomycine) appellent une vigilance particulière.

Les mises en garde et contre-indications de la notice française ne sont pas disponibles ; veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais randomisés de phase 2 et 3 (GeparSixto, BrighTNess, CALGB 40603, CITRINE) et des essais de phase 3 intégrant la carboplatine dans des schémas HER2+ soutiennent son usage dans le cancer du sein, en particulier triple négatif. Toutefois, les AMM françaises sont toutes annulées et la sécurité est insuffisamment documentée dans les données disponibles.

**Pour avancer, les éléments suivants sont nécessaires :**
- Obtenir et analyser la notice officielle (mises en garde, contre-indications), identifiée comme lacune bloquante pour l'évaluation de sécurité
- Compléter les données sur le mécanisme d'action (DrugBank)
- Clarifier le statut réglementaire actuel : les AMM annulées peuvent refléter des substitutions administratives et non un retrait pour raison de sécurité
- Vérifier le design et les résultats de chaque essai cité, car les phases et schémas sont inférés des titres
- Définir un plan de surveillance hématologique, rénale et auditive

---

## Autres Indications Prédites

Les autres prédictions du modèle sont nettement moins étayées :

| Rang | Indication Prédite | Score TxGNN | Niveau de Preuve | Recommandation |
|---|---|---|---|---|
| 2 | Adénocarcinome mucineux du rectum | 99,28 % | L5 | Hold |
| 3 | Adénocarcinome mucineux du côlon | 99,26 % | L5 | Hold |
| 4 | Tumeur germinale de l'adulte | 99,24 % | L2 | Question de recherche |
| 5 | Adénocarcinome mucineux du col utérin | 99,24 % | L3 | Question de recherche |
| 6 | Adénocarcinome mucineux de la vésicule biliaire | 99,23 % | L5 | Hold |
| 7 | Adénocarcinome mucineux de l'endomètre | 99,20 % | L3 | Question de recherche |
| 8 | Adénocarcinome endométrioïde villoglandulaire de l'endomètre | 99,20 % | L5 | Hold |
| 9 | Adénocarcinome mixte de l'endomètre | 99,20 % | L1 | Proceed with Guardrails (prudence : la carboplatine est le socle commun des bras, non la variable testée) |
| 10 | Adénocarcinome mucineux des voies biliaires extrahépatiques | 99,18 % | L5 | Hold |

La tumeur germinale de l'adulte présente le soutien le plus substantiel après le cancer du sein : des essais de phase 2 de chimiothérapie à haute dose et une revue systématique (PMID 22976789) suggèrent une activité, mais la carboplatine semble inférieure au cisplatine dans certaines situations.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

