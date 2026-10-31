---
layout: default
title: Perindopril
parent: Prédiction du modèle uniquement (L5)
nav_order: 592
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "perindopril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
description: "Perindopril : nouvelle indication prédite, Néphropathie hypertensive maligne (malignant hypertensive renal disease) (niveau de preuve L5). Indication d'origine : Non renseignée dans les données local…"
---

# Perindopril
{: .fs-9 }

Niveau de preuve: **L5** | Indications prédites: **4** 
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

## Perindopril: Néphropathie hypertensive maligne (malignant hypertensive renal disease)
{: .text-alpha }

## Résumé en Une Phrase

Le périndopril est un inhibiteur de l'enzyme de conversion de l'angiotensine (IEC), initialement utilisé pour traiter l'hypertension artérielle.
Le modèle TxGNN prédit qu'il pourrait être efficace pour la **néphropathie hypertensive maligne**, mais cette prédiction repose uniquement sur le modèle : **aucun essai clinique** n'est enregistré et **aucune publication** ne traite directement de cette association.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Non renseignée dans les données locales |
| Nouvelle Indication Prédite | Néphropathie hypertensive maligne (malignant hypertensive renal disease) |
| Score de Prédiction TxGNN | 0.9977 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, le périndopril appartient à la classe des IEC. Son efficacité dans l'hypertension est établie. Il réduit la production d'angiotensine II, ce qui abaisse la pression artérielle.

L'activation du système rénine-angiotensine-aldostérone (SRAA) joue un rôle dans l'hypertension maligne et dans l'atteinte rénale qui l'accompagne. Un rationnel mécanistique existe donc.

Les autres prédictions du modèle sont encore plus fragiles : l'hypertension rénovasculaire maligne (même score, aucune donnée), l'hypertension pulmonaire (indices précliniques chez le rat uniquement) et le syndrome de Braddock (lien probablement artefactuel).

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Une seule publication est liée à la prédiction principale, et elle n'est pas pertinente :

| PMID | Année | Type | Revue | Résultats Principaux |
|------|-----|------|------|---------|
| [36382821](https://pubmed.ncbi.nlm.nih.gov/36382821/) | 2022 | Autre (hors cible) | Urologiia | Fonction du rein unique après néphrectomie pour cancer du rein ; ne traite pas du périndopril dans la néphropathie hypertensive maligne |

Pour information, parmi les autres indications prédites, seule une étude préclinique chez le rat présente un lien direct avec le périndopril : [11282121](https://pubmed.ncbi.nlm.nih.gov/11282121/) (2001, Eur J Pharmacol), où l'association amlodipine + périndopril prévient le remodelage vasculaire pulmonaire dans l'hypertension pulmonaire hypoxique. Il s'agit d'une preuve indirecte, au niveau animal.

## Informations de Marché en France

Le texte d'indication n'est pas renseigné. Principales AMM :

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Indication Approuvée |
|---------|------|------|-----------|
| 69699257 | PERINDOPRIL SANDOZ 2 mg | Comprimé | Non renseignée |
| 62746131 | PERINDOPRIL ARGININE HCS 5 mg | Comprimé sécable | Non renseignée |
| 61947423 | PERINDOPRIL ARGININE SERVIER 2,5 mg | Comprimé pelliculé | Non renseignée |
| 63849839 | COVERSYL 5 mg | Comprimé pelliculé sécable | Non renseignée |
| 68762014 | COGYR 2 mg | Comprimé | Non renseignée |

## Considérations de Sécurité

- **Contre-indications issues du graphe de connaissances** (et non du texte de la notice) : maladie rénale, maladie hépatique, maladie de la vésicule biliaire, angio-œdème (acquis, héréditaire, induit par les bloqueurs du SRAA, non histaminique), neutropénie, agranulocytose, hypotension, maladie du tissu conjonctif, maladies osseuses et cartilagineuses, obstruction de l'artère rénale.
- **Interactions médicamenteuses** : 213 interactions recensées. Deux sont majeures : le citrate de potassium et le bicarbonate de potassium (risque d'hyperkaliémie). Les interactions modérées comprennent notamment les corticoïdes (hydrocortisone, dexaméthasone, bétaméthasone, budésonide, triamcinolone), la metformine, les gliptines et les gliflozines, l'acide acétylsalicylique, la morphine et le bupropion.
- **Point d'attention propre à la nouvelle indication** : les IEC comportent un risque d'insuffisance rénale aiguë en cas de sténose bilatérale de l'artère rénale ou de rein unique sténosé, ce qui est directement pertinent pour une atteinte rénale hypertensive. Deux publications rapportent par ailleurs des cas d'angio-œdème sous IEC, dont un engageant le pronostic vital.

Les mises en garde et contre-indications officielles de la notice n'ont pas pu être consultées ; veuillez consulter la notice pour ces informations.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- Les preuves se limitent à la prédiction du modèle (L5) : aucun essai clinique, et la seule publication liée est hors sujet.

**Pour avancer, les éléments suivants sont nécessaires :**
- Les mises en garde et contre-indications de la notice ANSM (étape de sécurité actuellement bloquée)
- Les données sur le mécanisme d'action (DrugBank)
- Une recherche ciblée dans la littérature clinique sur les IEC dans la néphropathie hypertensive maligne
- Une évaluation du risque rénal (sténose de l'artère rénale, hyperkaliémie) propre à cette population
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

