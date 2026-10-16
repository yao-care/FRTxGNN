---
layout: default
title: Famotidine
parent: Preuves élevées (L1-L2)
nav_order: 316
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Famotidine : nouvelle indication prédite, Maladie ulcéreuse peptique (peptic ulcer disease) (niveau de preuve L1). Indication d'origine : Non précisée dans les données d'AMM"
---

# Famotidine
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

# Famotidine : Des Ulcères Gastroduodénaux à la Maladie Ulcéreuse Peptique (Prévention des Récidives)

## Résumé en Une Phrase

La famotidine est un antagoniste des récepteurs H2 de l'histamine, initialement utilisé pour traiter l'ulcère gastrique, l'ulcère duodénal, le reflux gastro-œsophagien et le syndrome de Zollinger-Ellison.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour la **maladie ulcéreuse peptique** (prévention des récidives et des ulcères induits par des médicaments), avec **7 essais cliniques** et **20 publications** soutenant actuellement cette direction.
Cette prédiction est toutefois très proche des indications d'origine : il s'agit davantage d'une extension d'usage que d'un véritable repositionnement.

---

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non précisée dans les données d'AMM (les indications connues du graphe de connaissances incluent l'ulcère gastrique, le reflux gastro-œsophagien et l'ulcère duodénal) |
| Nouvelle Indication Prédite | Maladie ulcéreuse peptique (peptic ulcer disease) |
| Score de Prédiction TxGNN | 99,72 % |
| Niveau de Preuve | L1 |
| Statut de Marché en France | Annulée uniquement (aucune AMM valide) |
| Nombre d'AMM | 2 (toutes deux annulées) |
| Décision Recommandée | Proceed with Guardrails |

> Remarque : la prédiction la mieux classée par le modèle est le reflux duodéno-gastrique (score 99,99 %), mais elle repose sur peu de preuves (niveau L4, décision Hold). La maladie ulcéreuse peptique, classée 8ᵉ, est la mieux documentée et fait l'objet de ce rapport.

---

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles dans les informations compilées. D'après les connaissances pharmacologiques établies, la famotidine bloque les récepteurs H2 des cellules pariétales gastriques et réduit la sécrétion d'acide. C'est la base reconnue de la cicatrisation et de la prévention des ulcères.

La nouvelle indication chevauche donc largement les indications d'origine (ulcères gastrique et duodénal). Les données récentes portent sur la **prévention** des ulcères induits par des médicaments (thiénopyridines, aspirine), des récidives d'hémorragie ulcéreuse idiopathique et la prophylaxie des ulcères de stress. Il s'agit d'une extension de l'usage approuvé plutôt que d'un nouveau mécanisme.

Point de vigilance : plusieurs essais suggèrent que la famotidine est **inférieure aux inhibiteurs de la pompe à protons (IPP)** dans certaines situations de prévention secondaire, notamment avec l'aspirine.

---

## Preuves d'Essais Cliniques

| Numéro d'Essai | Phase | Statut | Inscription | Résultats Principaux |
|---------|------|------|------|---------|
| [NCT00843063](https://clinicaltrials.gov/study/NCT00843063) | Phase 4 | Terminé | 161 | Famotidine à forte dose vs pantoprazole pour prévenir la récidive d'ulcère/érosion liée à l'aspirine ; famotidine inférieure au pantoprazole |
| [NCT01180179](https://clinicaltrials.gov/study/NCT01180179) | Phase 4 | Terminé | 228 | Lansoprazole vs famotidine pour prévenir la récidive d'hémorragie ulcéreuse gastroduodénale idiopathique (H. pylori négatif) |
| [NCT02418312](https://clinicaltrials.gov/study/NCT02418312) | NA | Terminé | 228 | Antagoniste H2 pour la prévention de l'ulcère peptique lié aux thiénopyridines |
| [NCT02551744](https://clinicaltrials.gov/study/NCT02551744) | NA | Terminé | 101 | Pantoprazole vs famotidine pour prévenir les ulcères récidivants chez les utilisateurs de thiénopyridines |
| [NCT03667703](https://clinicaltrials.gov/study/NCT03667703) | Phase 4 | Terminé | 70 | Prophylaxie de l'ulcère de stress vs placebo chez des nourrissons en cardiopathie congénitale (la famotidine n'est pas confirmée comme agent testé) |
| [NCT00557349](https://clinicaltrials.gov/study/NCT00557349) | Phase 4 | Terminé | 40 | Zegerid vs famotidine (comparateur) pour prévenir les ulcères anastomotiques après bypass gastrique |
| [NCT00229424](https://clinicaltrials.gov/study/NCT00229424) | Phase 3 | Terminé | 325 | Lafutidine vs famotidine (comparateur) dans l'œsophagite par reflux légère ; pertinence partielle |
| [NCT00839488](https://clinicaltrials.gov/study/NCT00839488) | Phase 4 | Arrêté | 6 | Pantoprazole IV vs famotidine pour la prophylaxie de l'ulcère de stress après chirurgie abdominale majeure ; arrêté après 6 patients |

---

## Preuves de la Littérature

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [31229990](https://pubmed.ncbi.nlm.nih.gov/31229990/) | 2020 | ECR | Gut | Prévention des récidives d'hémorragie ulcéreuse idiopathique : lansoprazole comparé à la famotidine |
| [19837071](https://pubmed.ncbi.nlm.nih.gov/19837071/) | 2010 | ECR | Gastroenterology | La famotidine à forte dose est inférieure au pantoprazole pour prévenir la récidive d'ulcères/érosions liés à l'aspirine |
| [2875864](https://pubmed.ncbi.nlm.nih.gov/2875864/) | 1986 | Revue | Drugs | Propriétés pharmacodynamiques et pharmacocinétiques de la famotidine ; usage dans l'ulcère peptique et le syndrome de Zollinger-Ellison |
| [2573505](https://pubmed.ncbi.nlm.nih.gov/2573505/) | 1989 | Revue | Drugs | Mise à jour : la famotidine cicatrise les ulcères gastriques et duodénaux (essais contrôlés contre placebo) |
| [35348552](https://pubmed.ncbi.nlm.nih.gov/35348552/) | 2022 | Revue | Med Lett Drugs Ther | Médicaments du RGO et de la maladie ulcéreuse peptique |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | Revue | Hepato-gastroenterology | L'inhibition de l'acidité nocturne est associée à la cicatrisation ; effets de la famotidine 40 mg au coucher |
| [1621633](https://pubmed.ncbi.nlm.nih.gov/1621633/) | 1992 | Revue | Am Fam Physician | Les antagonistes H2 restent le traitement de base ; la famotidine est préférée chez les consommateurs d'alcool |
| [41405382](https://pubmed.ncbi.nlm.nih.gov/41405382/) | 2026 | Analyse comparative | Crit Care Med | Antagonistes H2 vs IPP pour la prophylaxie de l'ulcère de stress dans le choc septique |
| [1764869](https://pubmed.ncbi.nlm.nih.gov/1764869/) | 1991 | Pharmacocinétique | Clin Pharmacokinet | Pharmacocinétique clinique de la famotidine (demi-vie d'élimination d'environ 2 à 4 h) |
| [2883883](https://pubmed.ncbi.nlm.nih.gov/2883883/) | 1987 | Étude clinique | Am J Gastroenterol | Effet de la famotidine sur l'hémodynamique hépatique et l'ulcère peptique chez des patients atteints d'hépatopathie chronique |

---

## Informations de Marché en France

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 67557907 | FAMOTIDINE EG 40 mg (annulée) | Comprimé pelliculé | Non renseignée |
| 60005856 | FAMOTIDINE EG 20 mg (annulée) | Comprimé pelliculé | Non renseignée |

Les deux AMM sont annulées (laboratoire EG Labo). Aucune AMM valide n'est actuellement recensée dans les données compilées.

---

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (associations du graphe, et non texte de la notice) : maladie rénale, insuffisance rénale, maladie hépatique, maladie de la vésicule biliaire, lithiase rénale, néphrocalcinose, hypercalcémie, hyperparathyroïdie, sarcoïdose, diarrhée, constipation, cancer gastrique (adénocarcinome, linite plastique). Ces éléments doivent être confirmés par la notice officielle.
- **Interactions médicamenteuses** : 100 interactions recensées. Parmi les premières listées, la majorité sont de niveau modéré (abiratérone, acalabrutinib, tramadol, amiodarone, amitriptyline, aripiprazole, salbutamol, alfuzosine, aminophylline, etc.) et quelques-unes de niveau mineur (acide alendronique, hydroxyde d'aluminium).

Les mises en garde et contre-indications officielles de la notice ne sont pas disponibles. Veuillez consulter la notice pour les informations de sécurité complètes.

---

## Conclusion et Prochaines Étapes

**Décision : Proceed with Guardrails**

**Justification :**
- Plusieurs essais de phase 4 terminés et deux ECR publiés portent sur la prévention des ulcères, ce qui correspond à un niveau de preuve L1. Cependant, la famotidine y apparaît souvent comme comparateur ou comme inférieure aux IPP, et l'indication chevauche l'usage déjà reconnu.

**Pour avancer, les éléments suivants sont nécessaires :**
- Récupérer la notice officielle de l'ANSM (mises en garde, contre-indications), un manque bloquant pour le dépistage de sécurité.
- Obtenir les données détaillées sur le mécanisme d'action depuis DrugBank.
- Vérifier la disponibilité réelle et les formulations en France, puisque les deux AMM sont annulées.
- Comparer systématiquement la famotidine aux IPP dans les populations visées (aspirine, thiénopyridines, prophylaxie de stress).
- Pour les autres prédictions (reflux duodéno-gastrique, ulcère gastro-jéjunal, gastroduodénite), niveau de preuve faible à modéré : à conserver en « Hold » ou « question de recherche ». Les prédictions « obstruction duodénale », « anomalie de la sécrétion de glucagon » et « acné » ne reposent que sur le score du modèle.
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

