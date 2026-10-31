---
layout: default
title: Levothyroxine
parent: Prédiction du modèle uniquement (L5)
nav_order: 451
evidence_level: L5
indication_count: 4
monitor_inn: "levothyroxine"
predicted_indications: ["renal hypodysplasia/aplasia", "bilateral renal agenesis", "Potter sequence", "Carney complex"]
last_modified_at: 2026-10-31
description: "Levothyroxine : nouvelle indication prédite, Hypoplasie/aplasie rénale (niveau de preuve L5). Indication d'origine : Hypothyroïdie"
---

# Levothyroxine
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

## Lévothyroxine : De l'hypothyroïdie à l'hypoplasie/aplasie rénale
{: .text-alpha }

## Résumé en Une Phrase

La lévothyroxine est une hormone thyroïdienne de substitution, utilisée à l'origine pour traiter l'hypothyroïdie et d'autres maladies de la thyroïde.
Le modèle TxGNN prédit qu'elle pourrait être efficace pour l'**hypoplasie/aplasie rénale**, mais **aucun essai clinique et aucune publication** ne soutiennent actuellement cette direction : il s'agit d'une prédiction du modèle uniquement.

## Aperçu Rapide

| Élément | Contenu |
|------|------|
| Indication Originale | Hypothyroïdie (relation enregistrée dans le graphe de connaissances ; les textes d'indication des AMM ne sont pas renseignés dans les données compilées) |
| Nouvelle Indication Prédite | Hypoplasie/aplasie rénale |
| Score de Prédiction TxGNN | 0,9967 |
| Niveau de Preuve | L5 |
| Statut de Marché en France | Commercialisé (autorisations valides : au moins 20) |
| Nombre d'AMM | au moins 20 |
| Décision Recommandée | Hold |

## Pourquoi Cette Prédiction est-elle Raisonnable ?

Actuellement, les données détaillées sur le mécanisme d'action ne sont pas disponibles. Sur la base des informations connues, la lévothyroxine est une forme synthétique de la thyroxine (T4), dont l'efficacité dans l'hypothyroïdie est établie. Les hormones thyroïdiennes jouent un rôle général dans le développement et la maturation de plusieurs organes, dont le rein.

Cependant, ce lien reste très faible. L'hypoplasie/aplasie rénale est un défaut du développement, le plus souvent d'origine génétique (par exemple PAX2, HNF1B, RET), qu'une hormone administrée après la naissance ne peut pas raisonnablement corriger. Le score élevé du modèle (0.9967) provient du modèle TxGNN (apprentissage profond) et peut refléter des similarités apprises par le modèle entre maladies apparentées (rénales et thyroïdiennes), et non une preuve biologique ni un mécanisme thérapeutique validé.

D'autres prédictions du modèle (agénésie rénale bilatérale, séquence de Potter, complexe de Carney) présentent les mêmes limites : aucune preuve clinique, et une plausibilité biologique faible ou indirecte.

## Preuves d'Essais Cliniques

Aucun essai clinique associé enregistré actuellement.

## Preuves de la Littérature

Aucune littérature associée disponible actuellement.

## Informations de Marché en France

La liste ci-dessous porte sur 5 des AMM de spécialités à base de lévothyroxine seule ; la liste complète peut comporter davantage d'AMM. Les textes d'indication approuvée ne sont pas renseignés dans les données compilées.

| Numéro d'AMM | Nom du Produit | Forme Pharmaceutique | Titulaire |
|---------|------|------|-----------|
| 66426100 | LEVOTHYROX 112 microgrammes | comprimé sécable | MERCK SANTE |
| 65706277 | L-THYROXIN HENNING 137 microgrammes | comprimé sécable | SANOFI WINTHROP INDUSTRIE |
| 60254754 | TSOLUDOSE 150 microgrammes | solution buvable en récipient unidose | IBSA PHARMA SAS |
| 61296560 | TCAPS 137 microgrammes | capsule molle | IBSA PHARMA SAS |
| 64952190 | THYROFIX 125 microgrammes | comprimé | UNI-PHARMA KLEON TSETIS PHARMACEUTICAL LABORATORIES (Grèce) |

## Considérations de Sécurité

Les mises en garde et contre-indications issues de la notice ne sont pas disponibles dans les données compilées. Veuillez consulter la notice pour ces informations.

- **Contre-indications enregistrées dans le graphe de connaissances** (relations du graphe, et non texte de la notice) : hypertension, déficits hypophysaires (dont hypopituitarisme et syndrome de Sheehan), hypogonadisme hypogonadotrope et syndrome de Kallmann, maladies du thymus, ostéoporose (dont post-ménopausique), diabète et acidocétose diabétique, maladie coronarienne et infarctus du myocarde.
- **Interactions médicamenteuses** : 666 interactions recensées. Parmi les principales, de niveau modéré : antidiabétiques (metformine, pioglitazone, acarbose, canagliflozine, dapagliflozine, empagliflozine, alogliptine, albiglutide, dulaglutide, chlorpropamide), inhibiteurs de la pompe à protons (oméprazole, rabéprazole, dexlansoprazole), sels de calcium et de magnésium (phosphate et acétate de calcium, oxyde de magnésium), épinéphrine, isométheptène et diéthylpropion. L'interaction avec la cimétidine est de niveau mineur.

## Conclusion et Prochaines Étapes

**Décision : Hold**

**Justification :**
- La prédiction repose uniquement sur le score du modèle (L5) : aucun essai clinique ni publication n'étudie cette maladie, et le lien biologique est peu plausible pour une malformation structurelle congénitale.

**Pour avancer, les éléments suivants sont nécessaires :**
- Données sur le mécanisme d'action de la lévothyroxine
- Mises en garde et contre-indications issues de la notice de l'ANSM
- Preuves précliniques ou cliniques directement liées à l'hypoplasie/aplasie rénale
- Justification mécanistique expliquant comment une hormone thyroïdienne pourrait agir sur un défaut de développement rénal
## Avertissement

Ce contenu est uniquement destiné à la recherche et ne constitue pas un avis médical.
Une validation clinique est requise avant toute application clinique.

---

